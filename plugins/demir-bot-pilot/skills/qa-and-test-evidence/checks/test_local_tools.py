"""Written-only regression/negative cases for the selected local tools; never auto-run."""
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[2] / 'demir-bot' / 'tools'


def load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dashboard = load('status_dashboard')
notifications = load('notification_ledger')


class DashboardBoundaries(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / '.codex-plugin').mkdir()
        (self.root / '.codex-plugin/plugin.json').write_text(json.dumps({'name': 'synthetic-plugin', 'version': '1.0.0'}))
        (self.root / 'skills/synthetic').mkdir(parents=True)
        (self.root / 'skills/synthetic/SKILL.md').write_text('Synthetic instruction')

    def test_no_provider_probe_or_approval_inference(self):
        html = dashboard.render(self.root)
        self.assertIn('No provider evidence supplied', html)
        self.assertIn('not proof of installation', html)
        self.assertIn('cannot authorize an action', html)
        self.assertNotIn(str(self.root), html)
        self.assertNotIn('<script', html)

    def test_rejects_nonservice_labels(self):
        # A bounded invalid-input corpus, not a randomized fuzzing campaign.
        for label in ('', '<script>', 'person@example.test', '\nService', 'A' * 65, None, 1):
            with self.subTest(label=repr(label)), self.assertRaises(ValueError):
                dashboard.safe_label(label)

    def test_stale_and_unknown_evidence_stay_distinct(self):
        entries = [{'name': 'Synthetic', 'installed': 'yes', 'available': 'unknown',
                    'authenticated': 'unknown', 'operation': 'unverified',
                    'approval': 'recorded', 'observed_at': '2020-01-01T00:00:00Z'}]
        evidence = self.root / 'evidence.json'
        evidence.write_text(json.dumps({'providers': entries}))
        rows = dashboard.load_evidence(evidence, datetime(2026, 1, 1, tzinfo=timezone.utc), 30)
        self.assertEqual(rows[0]['freshness'], 'stale')
        self.assertEqual(rows[0]['authenticated'], 'unknown')
        self.assertEqual(rows[0]['operation'], 'unverified')

    def test_rejects_extra_raw_evidence_fields(self):
        evidence = self.root / 'evidence.json'
        evidence.write_text(json.dumps({'providers': [], 'raw_message': 'synthetic'}))
        with self.assertRaises(ValueError):
            dashboard.load_evidence(evidence, datetime.now(timezone.utc), 30)

    def test_symlink_skill_not_followed(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (outside / 'SKILL.md').write_text('Synthetic outside source')
        (self.root / 'skills/linked').symlink_to(outside, target_is_directory=True)
        _, names = dashboard.catalogue(self.root)
        self.assertEqual(names, ['synthetic'])


class JsonInputBoundaries(unittest.TestCase):
    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'evidence.json'
            path.write_text('{"providers": [], "providers": []}')
            with self.assertRaises(ValueError):
                dashboard.read_json(path)

    def test_oversized_final_read_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'evidence.json'
            path.write_bytes(b' ' * (dashboard.MAX_BYTES + 1))
            with self.assertRaises(ValueError):
                dashboard.read_json(path)



class NotificationStateBoundaries(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'private' / 'state.sqlite'
        self.ledger = notifications.NotificationLedger(self.path)

    def test_nonboolean_actionability_rejected(self):
        for flag in ('false', 1, None):
            with self.subTest(flag=flag), self.assertRaises(ValueError):
                self.ledger.reserve('event', 'synthetic', 'body', actionable=flag)

    def test_nonboolean_reconciliation_rejected(self):
        key, _ = self.ledger.reserve('event', 'synthetic', 'body', actionable=True)
        self.ledger.record_outcome(key, 'uncertain')
        with self.assertRaises(ValueError):
            self.ledger.reconcile_uncertain(key, delivered='false', evidence_receipt='synthetic receipt')

    def test_blank_or_nonstr_provider_receipt_rejected(self):
        key, _ = self.ledger.reserve('event', 'synthetic', 'body', actionable=True)
        for receipt in (' ', 1):
            with self.subTest(receipt=receipt), self.assertRaises(ValueError):
                self.ledger.record_outcome(key, 'delivered', provider_receipt=receipt)


    def test_nonactionable_event_does_not_reserve(self):
        _, state = self.ledger.reserve('event', 'synthetic', 'body', actionable=False)
        self.assertEqual(state, 'skip-non-actionable')
        _, state = self.ledger.reserve('event', 'synthetic', 'body', actionable=True)
        self.assertEqual(state, 'reserved')

    def test_identical_event_reserved_once(self):
        key, state = self.ledger.reserve('event', 'synthetic', 'body', actionable=True)
        self.assertEqual(state, 'reserved')
        self.assertEqual(self.ledger.reserve('event', 'synthetic', 'body', actionable=True),
                         (key, 'skip-reserved'))

    def test_uncertain_delivery_cannot_be_automatically_retried(self):
        key, _ = self.ledger.reserve('event', 'synthetic', 'body', actionable=True)
        self.ledger.record_outcome(key, 'uncertain')
        self.assertEqual(self.ledger.reserve('event', 'synthetic', 'body', actionable=True)[1], 'skip-uncertain')
        self.ledger.reconcile_uncertain(key, delivered=True, evidence_receipt='synthetic-confirmation')
        self.assertEqual(self.ledger.reserve('event', 'synthetic', 'body', actionable=True)[1], 'skip-delivered')

    def test_delivery_requires_confirmation_and_only_one_initial_outcome(self):
        key, _ = self.ledger.reserve('event', 'synthetic', 'body', actionable=True)
        with self.assertRaises(ValueError):
            self.ledger.record_outcome(key, 'delivered')
        self.ledger.record_outcome(key, 'delivered', provider_receipt='synthetic-confirmation')
        with self.assertRaises(ValueError):
            self.ledger.record_outcome(key, 'failed')

    def test_changed_content_or_destination_is_a_different_event_key(self):
        original = self.ledger.key('event', 'destination', 'body')
        self.assertNotEqual(original, self.ledger.key('event', 'other', 'body'))
        self.assertNotEqual(original, self.ledger.key('event', 'destination', 'changed'))

    def test_raw_recipient_and_message_are_not_stored(self):
        self.ledger.reserve('event', 'unique-recipient-marker', 'unique-message-marker', actionable=True)
        content = self.path.read_bytes()
        self.assertNotIn(b'unique-recipient-marker', content)
        self.assertNotIn(b'unique-message-marker', content)


if __name__ == '__main__':
    unittest.main()
