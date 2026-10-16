"""Synthetic source/cache checks only. Real host lifecycle scenarios are separately documented."""
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


doctor = load('installation_doctor')
fingerprints = load('upstream_fingerprint')


class SourceCacheLifecycle(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.source = self.root / 'source'
        self.cache = self.root / 'cache'
        self.make_plugin(self.source)
        self.make_plugin(self.cache)

    def make_plugin(self, root, version='1.0.0'):
        (root / '.codex-plugin').mkdir(parents=True)
        identity = json.dumps({'name': 'synthetic-plugin', 'version': version})
        (root / '.codex-plugin/plugin.json').write_text(identity)
        (root / 'plugin.json').write_text(identity)
        (root / 'skills/example/agents').mkdir(parents=True)
        (root / 'skills/example/SKILL.md').write_text('Synthetic portable guidance')
        (root / 'skills/example/agents/openai.yaml').write_text('interface:\n  display_name: Example\n')

    def difference(self):
        _, source = doctor.inspect_tree(self.source)
        _, cache = doctor.inspect_tree(self.cache)
        return doctor.compare_trees(source, cache)

    def test_matching_synthetic_trees_do_not_claim_host_discovery(self):
        report, _ = doctor.inspect_tree(self.source)
        self.assertEqual(report['skills'], ['example'])
        self.assertEqual(report['metadata_missing'], [])
        self.assertEqual(report['portable_identity'], 'matches')
        self.assertNotIn('authenticated', report)
        self.assertEqual(self.difference(), {'missing': [], 'extra': [], 'changed': []})

    def test_new_source_file_detected_without_changing_cache(self):
        (self.source / 'skills/example/new.md').write_text('New supported behavior')
        self.assertEqual(self.difference()['missing'], ['skills/example/new.md'])
        self.assertFalse((self.cache / 'skills/example/new.md').exists())

    def test_stale_cache_detected_even_with_identical_version(self):
        (self.source / 'skills/example/SKILL.md').write_text('Changed source instruction')
        result = self.difference()
        self.assertEqual(result['changed'], ['skills/example/SKILL.md'])
        self.assertEqual(result['missing'], [])
        self.assertEqual(result['extra'], [])

    def test_removed_source_file_is_extra_in_retained_cache(self):
        (self.cache / 'skills/example/retired.md').write_text('Retained older file')
        self.assertEqual(self.difference()['extra'], ['skills/example/retired.md'])

    def test_source_rollback_restores_snapshot_without_repairing_cache(self):
        before, _ = doctor.inspect_tree(self.source)
        path = self.source / 'skills/example/SKILL.md'
        original = path.read_text()
        path.write_text('Candidate change')
        changed, _ = doctor.inspect_tree(self.source)
        self.assertNotEqual(before['snapshot'], changed['snapshot'])
        path.write_text(original)
        restored, _ = doctor.inspect_tree(self.source)
        self.assertEqual(before['snapshot'], restored['snapshot'])
        self.assertEqual(self.difference(), {'missing': [], 'extra': [], 'changed': []})

    def test_missing_installed_tree_is_not_successful_install(self):
        with self.assertRaises(ValueError):
            doctor.inspect_tree(self.root / 'uninstalled')

    def test_missing_optional_provider_has_no_implicit_dependency(self):
        report, _ = doctor.inspect_tree(self.source)
        self.assertEqual(report['identity']['name'], 'synthetic-plugin')
        self.assertFalse((self.root / 'providers').exists())

    def test_private_sibling_changes_do_not_enter_selected_snapshot(self):
        private = self.root / 'private'
        private.mkdir()
        canary = private / 'facts.md'
        canary.write_text('Synthetic private value A')
        before, hashes = doctor.inspect_tree(self.source)
        canary.write_text('Synthetic private value B')
        after, _ = doctor.inspect_tree(self.source)
        self.assertEqual(before['snapshot'], after['snapshot'])
        self.assertFalse(any('private' in name for name in hashes))
        self.assertNotIn('Synthetic private', json.dumps(before))

    def test_symlink_to_private_sibling_is_rejected(self):
        private = self.root / 'private.txt'
        private.write_text('Synthetic canary')
        (self.source / 'linked.txt').symlink_to(private)
        with self.assertRaises(ValueError):
            doctor.inspect_tree(self.source)

    def test_manifest_duplicate_key_rejected(self):
        (self.source / '.codex-plugin/plugin.json').write_text(
            '{"name":"synthetic-plugin","version":"1","version":"2"}')
        with self.assertRaises(ValueError):
            doctor.inspect_tree(self.source)

    def test_portable_identity_mismatch_remains_visible(self):
        (self.source / 'plugin.json').write_text('{"name":"other","version":"1.0.0"}')
        report, _ = doctor.inspect_tree(self.source)
        self.assertEqual(report['portable_identity'], 'differs')

    def test_index_evidence_never_establishes_live_freshness(self):
        report, _ = doctor.inspect_tree(self.source)
        path = self.root / 'index.json'
        path.write_text(json.dumps({'collection': 'synthetic', 'source_snapshot': report['snapshot'],
                                    'indexed_at': '2020-01-01T00:00:00Z', 'documents': 1}))
        evidence = doctor.index_evidence(path, report['snapshot'])
        self.assertTrue(evidence['supplied_snapshot_matches'])
        self.assertEqual(evidence['live_index_state'], 'unverified')
        self.assertEqual(evidence['scope_coverage'], 'unverified')
        evidence = doctor.index_evidence(path, '0' * 64)
        self.assertFalse(evidence['supplied_snapshot_matches'])


class UpstreamSelectionBoundaries(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / 'one.md').write_text('One')
        (self.root / 'two.md').write_text('Two')

    def test_omitted_selection_not_reported_as_deletion(self):
        old = fingerprints.snapshot(self.root, ['one.md', 'two.md'])
        new = fingerprints.snapshot(self.root, ['one.md'])
        self.assertEqual(fingerprints.compare(old, new),
                         {'one.md': 'unchanged', 'two.md': 'not-selected'})

    def test_modified_selected_content_is_changed(self):
        old = fingerprints.snapshot(self.root, ['one.md'])
        (self.root / 'one.md').write_text('Different')
        self.assertEqual(fingerprints.compare(old, fingerprints.snapshot(self.root, ['one.md'])),
                         {'one.md': 'changed'})

    def test_parent_escape_and_symlink_are_rejected(self):
        (self.root / 'linked.md').symlink_to(self.root / 'one.md')
        for name in ('../outside.md', '/absolute.md', 'linked.md'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                fingerprints.snapshot(self.root, [name])


if __name__ == '__main__':
    unittest.main()
