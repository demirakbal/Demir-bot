#!/usr/bin/env python3
"""Render a local plugin catalogue and explicitly supplied evidence, without probes."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone, timedelta
from html import escape
import json
from pathlib import Path
import re
import sys

STATE = frozenset({'unknown', 'yes', 'no'})
OPERATIONS = frozenset({'unknown', 'unverified', 'observed', 'failed'})
APPROVALS = frozenset({'unknown', 'not-required', 'pending', 'recorded', 'expired'})
MAX_BYTES = 131072


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key.')
        result[key] = value
    return result


def read_json(path: Path) -> dict:
    if path.is_symlink() or not path.is_file():
        raise ValueError('Expected an explicit regular JSON file; symlinks are excluded.')
    with path.open('rb') as handle:
        data = handle.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError('JSON file exceeds the bounded input size.')
    value = json.loads(data.decode('utf-8'), object_pairs_hook=unique_object)
    if not isinstance(value, dict):
        raise ValueError('Expected a JSON object.')
    return value


def safe_label(value: object) -> str:
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9 _./-]{0,63}', value):
        raise ValueError('Evidence labels must be short non-personal service identifiers.')
    return value


def load_evidence(path: Path | None, now: datetime, stale_days: int) -> list[dict]:
    if path is None:
        return []
    data = read_json(path)
    if set(data) != {'providers'} or not isinstance(data['providers'], list) or len(data['providers']) > 100:
        raise ValueError('Evidence requires one providers array with at most 100 summaries.')
    rows = []
    names = set()
    fields = {'name', 'installed', 'available', 'authenticated', 'operation', 'approval', 'observed_at'}
    for entry in data['providers']:
        if not isinstance(entry, dict) or set(entry) != fields:
            raise ValueError('Provider evidence fields do not match the documented summary schema.')
        row = dict(entry)
        row['name'] = safe_label(row['name'])
        if row['name'].casefold() in names:
            raise ValueError('Duplicate service identifiers are not allowed.')
        names.add(row['name'].casefold())
        if any(not isinstance(row[key], str) or row[key] not in STATE for key in ('installed', 'available', 'authenticated')):
            raise ValueError('Evidence state must be unknown, yes or no.')
        if (not isinstance(row['operation'], str) or row['operation'] not in OPERATIONS
                or not isinstance(row['approval'], str) or row['approval'] not in APPROVALS):
            raise ValueError('Operation or approval state is unsupported.')
        value = row['observed_at']
        if value is None:
            freshness = 'unknown'
        else:
            if not isinstance(value, str) or len(value) > 40:
                raise ValueError('Evidence time must be an ISO timestamp with timezone, or null.')
            observed = datetime.fromisoformat(value.replace('Z', '+00:00'))
            if observed.tzinfo is None:
                raise ValueError('Evidence timestamps require a timezone.')
            age = now - observed.astimezone(timezone.utc)
            if age < -timedelta(minutes=5):
                raise ValueError('Evidence timestamp is in the future.')
            freshness = 'stale' if age > timedelta(days=stale_days) else 'recorded recently'
        row['freshness'] = freshness
        rows.append(row)
    return rows


def catalogue(root: Path) -> tuple[dict, list[str]]:
    root = root.resolve(strict=True)
    manifest_path = root / '.codex-plugin' / 'plugin.json'
    if manifest_path.parent.is_symlink():
        raise ValueError('Manifest directory symlinks are excluded.')
    manifest = read_json(manifest_path)
    name = safe_label(manifest.get('name'))
    version = manifest.get('version')
    if not isinstance(version, str) or not re.fullmatch(r'[A-Za-z0-9.+_-]{1,80}', version):
        raise ValueError('Plugin manifest version is missing or malformed.')
    skills = root / 'skills'
    if skills.is_symlink() or not skills.is_dir():
        raise ValueError('A regular skills directory is required.')
    names = []
    for entry in sorted(skills.iterdir(), key=lambda p: p.name):
        if entry.is_symlink() or not entry.is_dir():
            continue
        body = entry / 'SKILL.md'
        if body.is_file() and not body.is_symlink():
            names.append(safe_label(entry.name))
    return {'name': name, 'version': version}, names


def render(root: Path, evidence: Path | None = None, stale_days: int = 30) -> str:
    if stale_days < 1:
        raise ValueError('Staleness window must be at least one day.')
    now = datetime.now(timezone.utc)
    manifest, skills = catalogue(root)
    providers = load_evidence(evidence, now, stale_days)
    cells = ('name', 'installed', 'available', 'authenticated', 'operation', 'approval', 'freshness')
    provider_rows = ''.join('<tr>' + ''.join(f'<td>{escape(str(row[key]))}</td>' for key in cells) + '</tr>' for row in providers)
    if not provider_rows:
        provider_rows = '<tr><td colspan="7">No provider evidence supplied. Access and approvals are unknown.</td></tr>'
    skills_html = ''.join(f'<li>{escape(name)}</li>' for name in skills)
    return f'''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Demir Bot local status</title>
<style>body{{font:17px/1.55 system-ui,sans-serif;background:#101827;color:#eff4ff;margin:0}}main{{max-width:1100px;margin:auto;padding:32px 20px}}h1,h2{{line-height:1.2}}.note{{padding:16px;background:#1e2b42;border-left:4px solid #a6cdff}}table{{border-collapse:collapse;width:100%;font-size:15px}}th,td{{padding:10px;text-align:left;border:1px solid #52617b}}.scroll{{overflow-x:auto}}ul{{columns:2;column-width:260px}}small{{color:#c1cce0}}</style>
<main><h1>Demir Bot local status</h1>
<p>{escape(manifest['name'])} · manifest {escape(manifest['version'])} · {len(skills)} skill definitions</p>
<p class="note">Read-only snapshot. Source presence is not proof of installation, authentication or working behavior. Recorded approvals are display-only and cannot authorize an action.</p>
<h2>Provider evidence</h2><p>Only the explicit summary file is used. No account, profile, environment or network probes run. Unknown and stale states remain visible.</p>
<div class="scroll"><table><caption>Supplied evidence; freshness window {stale_days} days</caption><thead><tr><th scope="col">Service</th><th scope="col">Installed</th><th scope="col">Available</th><th scope="col">Authenticated</th><th scope="col">Operation</th><th scope="col">Approval</th><th scope="col">Freshness</th></tr></thead><tbody>{provider_rows}</tbody></table></div>
<h2>Skill definitions</h2><ul>{skills_html}</ul>
<p><small>Generated {now.isoformat()}. No private profile contents or absolute source paths are included. Refresh is on demand; no watcher or service is installed.</small></p></main></html>'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugin-root', type=Path, required=True)
    parser.add_argument('--evidence', type=Path, help='Explicit approved non-private evidence summary JSON')
    parser.add_argument('--stale-days', type=int, default=30)
    args = parser.parse_args(argv)
    try:
        output = render(args.plugin_root, args.evidence, args.stale_days)
    except (OSError, ValueError, TypeError, RecursionError, OverflowError):
        print('Dashboard input is unavailable or invalid; no private content or error payload is emitted.', file=sys.stderr)
        return 2
    print(output)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
