"""Synthetic, offline tests of the manual runner, not model evaluations."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('free_runner', Path(__file__).parents[1] / 'runner/free_runner.py')
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class RunnerContracts(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.package = self.root / 'package'
        self.behavioral = self.root / 'cases'
        self.behavioral.mkdir()
        owner = self.package / 'skills/example'
        owner.mkdir(parents=True)
        (owner / 'SKILL.md').write_text('# Example\nReturn a bounded answer.')
        self.case = {'id': 'CORE-001', 'source': 'skills/example/SKILL.md',
                     'input': 'Synthetic question', 'expected': 'SECRET_REVIEWER_ORACLE'}
        for name, cases in [('core-cases.json', [self.case]), ('a2-cases.json', [])]:
            (self.behavioral / name).write_text(json.dumps({'cases': cases}))
        self.run = self.root / 'run'
        runner.prepare(self.run, 'selected-model', self.package, self.behavioral)
        self.response = self.root / 'response.txt'
        self.response.write_text('Synthetic answer')

    def record(self, tools='none-observed'):
        runner.record(self.run, 'CORE-001', self.response, 'selected-model', tools)

    def test_subject_packet_excludes_oracle(self):
        self.assertNotIn('SECRET_REVIEWER_ORACLE', runner.packet(self.run, 'CORE-001'))
        self.assertIn('SECRET_REVIEWER_ORACLE', (self.run / 'reviewer.json').read_text())

    def test_prepare_never_overwrites_run(self):
        with self.assertRaises(FileExistsError):
            runner.prepare(self.run, 'selected-model', self.package, self.behavioral)

    def test_no_response_means_not_run(self):
        self.assertEqual(1, runner.report(self.run)['text_results']['not_run'])

    def test_record_does_not_auto_grade(self):
        self.record()
        self.assertEqual(1, runner.report(self.run)['text_results']['ungraded'])

    def test_second_attempt_rejected(self):
        self.record()
        with self.assertRaises(FileExistsError):
            self.record()

    def test_model_substitution_rejected(self):
        with self.assertRaises(ValueError):
            runner.record(self.run, 'CORE-001', self.response, 'other', 'none-observed')

    def test_unknown_tools_cannot_pass(self):
        self.record('unknown')
        with self.assertRaises(ValueError):
            runner.grade(self.run, 'CORE-001', 'met', 'Claimed result')

    def test_text_success_never_claims_full_functionality(self):
        self.record()
        runner.grade(self.run, 'CORE-001', 'met', 'Answer meets the synthetic requirement')
        result = runner.report(self.run)
        self.assertEqual(1, result['text_results']['met'])
        self.assertFalse(result['full_functionality_pass'])
        self.assertEqual(0, result['automatic_model_calls'])

    def test_unknown_id_cannot_escape_run(self):
        with self.assertRaises(ValueError):
            runner.packet(self.run, '../../outside')

    def test_changed_packet_rejected(self):
        (self.run / 'subject/CORE-001.json').write_text('changed')
        with self.assertRaises(ValueError):
            runner.packet(self.run, 'CORE-001')

    def test_changed_response_rejected(self):
        self.record()
        path = self.run / 'responses/CORE-001.json'
        data = json.loads(path.read_text())
        data['response'] = 'edited'
        path.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            runner.report(self.run)

    def test_escape_source_rejected(self):
        with self.assertRaises(ValueError):
            runner.source_text(self.package, '../private.txt')

    def test_symlink_source_rejected(self):
        secret = self.root / 'private.txt'
        secret.write_text('do not load')
        (self.package / 'linked.md').symlink_to(secret)
        with self.assertRaises(ValueError):
            runner.source_text(self.package, 'linked.md')

    def test_output_inside_plugin_rejected(self):
        with self.assertRaises(ValueError):
            runner.prepare(self.package / 'results', 'selected-model', self.package, self.behavioral)


if __name__ == '__main__':
    unittest.main()
