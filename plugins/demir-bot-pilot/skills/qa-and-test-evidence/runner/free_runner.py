"""Offline packet/response runner. No model, network, subprocess or account access."""
import argparse
import hashlib
import json
import re
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[3]
BEHAVIORAL = PACKAGE / 'skills/qa-and-test-evidence/behavioral'


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def save_new(path, value):
    with path.open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')


def source_text(package, relative):
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Source must be package-relative')
    path = package / rel
    for part in [path, *path.parents]:
        if part == package:
            break
        if part.is_symlink():
            raise ValueError('Symlink sources are not allowed')
    path.resolve().relative_to(package.resolve())
    return path.read_text(encoding='utf-8')


def prepare(destination, model, package=PACKAGE, behavioral=BEHAVIORAL):
    destination = Path(destination)
    resolved = destination.resolve()
    if resolved.is_relative_to(package.resolve()):
        raise ValueError('Keep evaluation records outside the plugin')
    cases = []
    for name in ('core-cases.json', 'a2-cases.json'):
        cases.extend(read_json(behavioral / name)['cases'])
    ids = [c['id'] for c in cases]
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r'(CORE|A2)-\d{3}', i) for i in ids):
        raise ValueError('Invalid or duplicate case IDs')
    # Resolve every source before creating output. Never follow private-profile pointers.
    sources = {}
    packets = {}
    for case in cases:
        paths = [case['source']]
        owner = '/'.join(Path(case['source']).parts[:2]) + '/SKILL.md'
        if owner not in paths:
            paths.insert(0, owner)
        excerpts = []
        for path in paths:
            content = source_text(package, path)
            sources[path] = digest(content)
            excerpts.append({'source': path, 'content': content})
        packets[case['id']] = {
            'mode': 'text-only instruction application; not native plugin discovery',
            'instructions': 'Answer only from supplied context. Do not use tools, follow links, run code or perform actions. If evidence is insufficient, state what is missing. This prompt is not enforced tool isolation.',
            'candidate_sources': excerpts,
            'input': case['input'],
        }
    # Exclusive directory prevents accidental overwrite/resume under a changed candidate.
    destination.mkdir(parents=True, exist_ok=False)
    (destination / 'subject').mkdir()
    (destination / 'responses').mkdir()
    (destination / 'grades').mkdir()
    packet_hashes = {}
    for case_id, packet in packets.items():
        text = json.dumps(packet, indent=2, ensure_ascii=False) + '\n'
        path = destination / 'subject' / (case_id + '.json')
        path.write_text(text, encoding='utf-8')
        packet_hashes[case_id] = digest(text)
    save_new(destination / 'reviewer.json', {c['id']: c['expected'] for c in cases})
    save_new(destination / 'manifest.json', {
        'version': 1, 'model': model, 'case_ids': ids, 'sources': sources,
        'packets': packet_hashes, 'attempt_limit': 1, 'automatic_model_calls': 0,
        'isolation': 'unverified; manual text-only',
        'source_scope': 'listed owner and reference excerpts, not the full package',
    })
    return len(cases)


def manifest(run):
    return read_json(run / 'manifest.json')


def case_path(run, case_id, folder):
    if case_id not in manifest(run)['case_ids']:
        raise ValueError('Unknown case ID')
    return run / folder / (case_id + '.json')


def packet(run, case_id):
    path = case_path(run, case_id, 'subject')
    content = path.read_text(encoding='utf-8')
    if digest(content) != manifest(run)['packets'][case_id]:
        raise ValueError('Packet changed since preparation')
    return content


def record(run, case_id, response_file, observed_model, tool_activity):
    packet(run, case_id)
    if observed_model != manifest(run)['model']:
        raise ValueError('Model mismatch; do not silently substitute')
    text = Path(response_file).read_text(encoding='utf-8')
    if not text.strip():
        raise ValueError('Empty response is not a completed attempt')
    if tool_activity not in ('none-observed', 'attempted', 'unknown'):
        raise ValueError('Invalid tool activity')
    save_new(case_path(run, case_id, 'responses'), {
        'response': text, 'sha256': digest(text), 'model': observed_model,
        'tool_activity': tool_activity, 'isolation_verified': False,
    })


def grade(run, case_id, outcome, evidence):
    response = read_json(case_path(run, case_id, 'responses'))
    if outcome not in ('met', 'violated', 'inconclusive') or not evidence.strip():
        raise ValueError('A valid result and evidence are required')
    if outcome == 'met' and response['tool_activity'] != 'none-observed':
        raise ValueError('Unknown or attempted tools prevent text-only acceptance')
    if response['sha256'] != digest(response['response']):
        raise ValueError('Response integrity mismatch')
    save_new(case_path(run, case_id, 'grades'), {
        'outcome': outcome, 'evidence': evidence, 'response_sha256': response['sha256'],
        'scope': 'human-reviewed text only; operational behavior unassessed',
    })


def report(run):
    counts = {'not_run': 0, 'ungraded': 0, 'met': 0, 'violated': 0, 'inconclusive': 0}
    for case_id in manifest(run)['case_ids']:
        packet(run, case_id)
        response_path = case_path(run, case_id, 'responses')
        grade_path = case_path(run, case_id, 'grades')
        if not response_path.exists():
            if grade_path.exists():
                raise ValueError('Grade has no response')
            counts['not_run'] += 1
            continue
        response = read_json(response_path)
        if response['sha256'] != digest(response['response']):
            raise ValueError('Response integrity mismatch')
        if not grade_path.exists():
            counts['ungraded'] += 1
            continue
        result = read_json(grade_path)
        if result['response_sha256'] != response['sha256']:
            raise ValueError('Grade does not match response')
        counts[result['outcome']] += 1
    return {'text_results': counts, 'tool_isolation': 'unverified',
            'full_functionality_pass': False, 'automatic_model_calls': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('run', type=Path)
    p.add_argument('--model', required=True, help='Exact model selected in the subscription UI')
    for name in ('packet', 'record', 'grade', 'report'):
        p = sub.add_parser(name)
        p.add_argument('run', type=Path)
        if name != 'report':
            p.add_argument('case_id')
        if name == 'record':
            p.add_argument('response_file', type=Path)
            p.add_argument('--model', required=True)
            p.add_argument('--tools', choices=['none-observed', 'attempted', 'unknown'], required=True)
        if name == 'grade':
            p.add_argument('--outcome', choices=['met', 'violated', 'inconclusive'], required=True)
            p.add_argument('--evidence', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'prepare':
            print(json.dumps({'prepared': prepare(args.run, args.model), 'model_calls': 0}))
        elif args.command == 'packet':
            print(packet(args.run, args.case_id))
        elif args.command == 'record':
            record(args.run, args.case_id, args.response_file, args.model, args.tools)
        elif args.command == 'grade':
            grade(args.run, args.case_id, args.outcome, args.evidence)
        else:
            print(json.dumps(report(args.run), indent=2))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f'{type(error).__name__}: {error}\n')


if __name__ == '__main__':
    main()
