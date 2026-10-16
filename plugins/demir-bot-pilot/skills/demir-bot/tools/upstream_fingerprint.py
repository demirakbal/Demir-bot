"""Explicit-file fingerprints for an on-demand source review; no network or execution."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

MAX_FILE = 2 * 1024 * 1024


def read_regular(root, relative):
    path = Path(relative)
    if path.is_absolute() or not path.parts or any(p in ('.', '..') for p in path.parts):
        raise ValueError('Expected a contained relative file path')
    target = root
    for part in path.parts:
        target = target / part
        if target.is_symlink():
            raise ValueError('Symlink paths are not supported')
    if not target.is_file():
        raise ValueError('Selected file is unavailable')
    with target.open('rb') as handle:
        data = handle.read(MAX_FILE + 1)
    if len(data) > MAX_FILE:
        raise ValueError('Selected file exceeds size limit')
    return data


def snapshot(root, files):
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise ValueError('Expected an absolute source directory')
    if not 1 <= len(files) <= 100 or len(set(files)) != len(files):
        raise ValueError('Select 1 to 100 unique files')
    result = {}
    for relative in sorted(files):
        data = read_regular(root, relative)
        result[relative] = {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    return {'schema': 1, 'files': result}


def compare(before, after):
    if not isinstance(before, dict) or set(before) != {'schema', 'files'} or before['schema'] != 1:
        raise ValueError('Unsupported baseline schema')
    old = before['files']
    if not isinstance(old, dict) or len(old) > 100:
        raise ValueError('Invalid baseline files')
    for name, record in old.items():
        if not isinstance(name, str) or not isinstance(record, dict) or set(record) != {'sha256', 'bytes'}:
            raise ValueError('Invalid baseline record')
        digest = record['sha256']
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
            raise ValueError('Invalid baseline digest')
        if type(record['bytes']) is not int or not 0 <= record['bytes'] <= MAX_FILE:
            raise ValueError('Invalid baseline size')
    new = after['files']
    return {name: ('not-selected' if name not in new else 'new' if name not in old
                   else 'unchanged' if old[name] == new[name] else 'changed')
            for name in sorted(set(old) | set(new))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--file', action='append', required=True, dest='files')
    parser.add_argument('--compare', type=Path, metavar='BASELINE_JSON')
    args = parser.parse_args()
    try:
        current = snapshot(args.root, args.files)
        if args.compare:
            if args.compare.is_symlink() or not args.compare.is_file():
                raise ValueError('Baseline must be a regular file')
            with args.compare.open('rb') as handle:
                data = handle.read(MAX_FILE + 1)
            if len(data) > MAX_FILE:
                raise ValueError('Baseline exceeds size limit')
            current['comparison'] = compare(json.loads(data), current)
        print(json.dumps(current, indent=2, sort_keys=True))
    except (OSError, ValueError, TypeError, UnicodeError, RecursionError):
        print('Source fingerprint unavailable: inspect selected paths/schema/limits.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
