"""Inspect explicitly selected plugin trees; never repair, run tools or read profiles."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

MAX_FILE = 2 * 1024 * 1024
MAX_TOTAL = 20 * 1024 * 1024
MAX_FILES = 2000


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result


def regular_bytes(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError('Expected regular file')
    with path.open('rb') as handle:
        data = handle.read(MAX_FILE + 1)
    if len(data) > MAX_FILE:
        raise ValueError('File exceeds limit')
    return data


def inspect_tree(root):
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError('Expected absolute plugin directory')
    hashes, manifest_data, total = {}, {}, 0
    pending = [root]
    visited = 0
    while pending:
        directory = pending.pop()
        for path in sorted(directory.iterdir()):
            visited += 1
            if visited > MAX_FILES * 3 or path.is_symlink():
                raise ValueError('Unsafe tree or entry limit exceeded')
            if path.is_dir():
                pending.append(path)
            elif path.is_file():
                if len(hashes) >= MAX_FILES:
                    raise ValueError('File count exceeds limit')
                data = regular_bytes(path)
                total += len(data)
                if total > MAX_TOTAL:
                    raise ValueError('Tree exceeds byte limit')
                name = path.relative_to(root).as_posix()
                hashes[name] = hashlib.sha256(data).hexdigest()
                if name in ('.codex-plugin/plugin.json', 'plugin.json'):
                    manifest_data[name] = json.loads(data, object_pairs_hook=unique_object)
            else:
                raise ValueError('Nonregular tree entry')
    manifest = manifest_data.get('.codex-plugin/plugin.json')
    if not isinstance(manifest, dict):
        raise ValueError('Local manifest unavailable')
    identity = {field: manifest.get(field) for field in ('name', 'version')}
    if any(not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9._+\-]{1,100}', value)
           for value in identity.values()):
        raise ValueError('Unsupported manifest identity')
    portable = manifest_data.get('plugin.json')
    agreement = ('not-present' if 'plugin.json' not in manifest_data else
                 'matches' if isinstance(portable, dict) and all(portable.get(k) == v for k, v in identity.items())
                 else 'differs')
    skills = sorted(name.split('/')[1] for name in hashes
                    if name.startswith('skills/') and name.count('/') == 2 and name.endswith('/SKILL.md'))
    metadata = sorted(name.split('/')[1] for name in hashes
                      if name.startswith('skills/') and name.count('/') == 3 and name.endswith('/agents/openai.yaml'))
    snapshot = hashlib.sha256(json.dumps(hashes, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    report = {'identity': identity, 'files': len(hashes), 'bytes': total,
              'snapshot': snapshot, 'portable_identity': agreement, 'skills': skills,
              'metadata_missing': sorted(set(skills) - set(metadata)),
              'metadata_without_skill': sorted(set(metadata) - set(skills))}
    return report, hashes


def compare_trees(source, installed):
    return {'missing': sorted(set(source) - set(installed)),
            'extra': sorted(set(installed) - set(source)),
            'changed': sorted(name for name in set(source) & set(installed)
                              if source[name] != installed[name])}


def index_evidence(path, snapshot):
    data = json.loads(regular_bytes(path), object_pairs_hook=unique_object)
    if not isinstance(data, dict) or set(data) != {'collection', 'source_snapshot', 'indexed_at', 'documents'}:
        raise ValueError('Unsupported index evidence fields')
    if not isinstance(data['collection'], str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,64}', data['collection']):
        raise ValueError('Invalid collection label')
    if not isinstance(data['source_snapshot'], str) or not re.fullmatch(r'[0-9a-f]{64}', data['source_snapshot']):
        raise ValueError('Invalid source snapshot')
    if type(data['documents']) is not int or not 0 <= data['documents'] <= 100000:
        raise ValueError('Invalid document count')
    if not isinstance(data['indexed_at'], str):
        raise ValueError('Invalid evidence date')
    indexed = datetime.fromisoformat(data['indexed_at'].replace('Z', '+00:00'))
    if indexed.tzinfo is None or (indexed - datetime.now(timezone.utc)).total_seconds() > 300:
        raise ValueError('Invalid evidence timezone/date')
    return {'collection': data['collection'], 'indexed_at': indexed.isoformat(),
            'documents': data['documents'],
            'supplied_snapshot_matches': data['source_snapshot'] == snapshot,
            'live_index_state': 'unverified', 'scope_coverage': 'unverified'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--installed', type=Path)
    parser.add_argument('--qmd-evidence', type=Path)
    args = parser.parse_args()
    try:
        source, source_hashes = inspect_tree(args.source)
        report = {'source': source, 'installed': {'state': 'not-provided'},
                  'qmd': {'live_index_state': 'unverified', 'evidence': 'not-provided'},
                  'host_discovery': 'unverified', 'authentication': 'not-inspected',
                  'behavior': 'not-executed', 'repair': 'none'}
        if args.installed:
            installed, installed_hashes = inspect_tree(args.installed)
            differences = compare_trees(source_hashes, installed_hashes)
            report['installed'] = {'state': 'differs' if any(differences.values()) else 'matches',
                                   'inventory': installed, 'differences': differences}
        if args.qmd_evidence:
            report['qmd'] = index_evidence(args.qmd_evidence, source['snapshot'])
        print(json.dumps(report, indent=2, sort_keys=True))
    except (OSError, ValueError, TypeError, UnicodeError, RecursionError, OverflowError):
        print('Inspection unavailable: review selected roots, regular files, schema and limits.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
