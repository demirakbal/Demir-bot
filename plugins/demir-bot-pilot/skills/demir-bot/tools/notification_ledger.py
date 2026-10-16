"""Minimal explicit notification deduplication state; never sends or grants approval."""
from __future__ import annotations
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path
import sqlite3


def digest(value: str) -> str:
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


class NotificationLedger:
    """Caller supplies an approved private DB path; bodies/recipients are not stored.

    A reservation records intent, not authority or delivery. 'uncertain' reservations
    require reconciliation and are deliberately not automatically retried.
    """
    def __init__(self, path: Path):
        path = Path(path).expanduser()
        if not path.is_absolute() or path.is_symlink() or path.parent.is_symlink():
            raise ValueError('Use an explicit absolute private ledger path without symlinks.')
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        if path.parent.stat().st_mode & 0o077:
            raise ValueError('Ledger directory must be private to its owner.')
        fd = os.open(path, os.O_RDWR | os.O_CREAT | getattr(os, 'O_NOFOLLOW', 0), 0o600)
        os.close(fd)
        if path.stat().st_mode & 0o077:
            raise ValueError('Ledger file must be private to its owner.')
        self.path = path
        with closing(self._connect()) as db, db:
            db.execute('''CREATE TABLE IF NOT EXISTS notifications (
                key TEXT PRIMARY KEY, state TEXT NOT NULL,
                observed_at TEXT NOT NULL, receipt_digest TEXT)''')

    def _connect(self):
        db = sqlite3.connect(self.path, timeout=5)
        db.execute('PRAGMA busy_timeout=5000')
        return db

    @staticmethod
    def key(event_id: str, destination: str, body: str) -> str:
        if not all(isinstance(x, str) and x.strip() for x in (event_id, destination, body)):
            raise ValueError('Event, destination and body must be non-empty.')
        # Structured length prefixes prevent separator collisions.
        return digest(''.join(f'{len(x)}:{x}' for x in (event_id, destination, body)))

    def reserve(self, event_id: str, destination: str, body: str, *, actionable: bool) -> tuple[str, str]:
        if type(actionable) is not bool:
            raise ValueError('Actionability must be an explicit boolean.')
        key = self.key(event_id, destination, body)
        if not actionable:
            return key, 'skip-non-actionable'
        now = datetime.now(timezone.utc).isoformat()
        with closing(self._connect()) as db, db:
            inserted = db.execute('INSERT OR IGNORE INTO notifications VALUES (?, ?, ?, NULL)',
                                  (key, 'reserved', now)).rowcount
            if inserted:
                return key, 'reserved'
            state = db.execute('SELECT state FROM notifications WHERE key=?', (key,)).fetchone()[0]
            return key, 'skip-' + state

    def record_outcome(self, key: str, outcome: str, *, provider_receipt: str | None = None) -> None:
        if not isinstance(outcome, str) or outcome not in {'delivered', 'failed', 'uncertain'}:
            raise ValueError('Unsupported notification outcome.')
        if provider_receipt is not None and (not isinstance(provider_receipt, str) or not provider_receipt.strip()):
            raise ValueError('Provider evidence must be a non-empty string.')
        if outcome == 'delivered' and provider_receipt is None:
            raise ValueError('Delivery needs actual provider confirmation evidence.')
        stamp = datetime.now(timezone.utc).isoformat()
        receipt = digest(provider_receipt) if provider_receipt else None
        with closing(self._connect()) as db, db:
            changed = db.execute('''UPDATE notifications SET state=?, observed_at=?, receipt_digest=?
                WHERE key=? AND state='reserved' ''', (outcome, stamp, receipt, key)).rowcount
            if changed != 1:
                raise ValueError('Only an existing reserved notification can receive an initial outcome.')

    def reconcile_uncertain(self, key: str, *, delivered: bool, evidence_receipt: str) -> None:
        if type(delivered) is not bool:
            raise ValueError('Reconciled delivery must be an explicit boolean.')
        if not isinstance(evidence_receipt, str) or not evidence_receipt.strip():
            raise ValueError('Reconciliation needs actual provider evidence.')
        with closing(self._connect()) as db, db:
            changed = db.execute('''UPDATE notifications SET state=?, observed_at=?, receipt_digest=?
                WHERE key=? AND state='uncertain' ''',
                ('delivered' if delivered else 'failed', datetime.now(timezone.utc).isoformat(),
                 digest(evidence_receipt), key)).rowcount
            if changed != 1:
                raise ValueError('Expected an uncertain notification to reconcile.')
