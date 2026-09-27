"""Offline integrity checks for A2 reviewer cases; never execute model subjects."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CASES = ROOT / 'skills/qa-and-test-evidence/behavioral/a2-cases.json'


class A2Coverage(unittest.TestCase):
    case_file = CASES
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(cls.case_file.read_text(encoding='utf-8'))
        cls.cases = cls.data['cases']

    def test_exact_independent_roadmap_inventory(self):
        self.assertEqual([f'A2-{i:03}' for i in range(1, 40)],
                         [case['id'] for case in self.cases])

    def test_sources_are_existing_package_files(self):
        for case in self.cases:
            with self.subTest(case=case['id']):
                relative = Path(case['source'])
                self.assertFalse(relative.is_absolute())
                self.assertNotIn('..', relative.parts)
                target = ROOT / relative
                for parent in [target, *target.parents]:
                    if parent == ROOT:
                        break
                    self.assertFalse(parent.is_symlink())
                self.assertTrue(target.is_file(), case['source'])
                self.assertTrue(target.read_text(encoding='utf-8').strip())

    def test_cases_are_not_falsely_marked_executed(self):
        self.assertEqual('reviewer_oracles_not_subject_instructions', self.data['mode'])
        for case in self.cases:
            self.assertEqual('not_run', case['status'])

    def test_inputs_and_oracles_are_separate_and_nonempty(self):
        for case in self.cases:
            with self.subTest(case=case['id']):
                self.assertTrue(case['input'].strip())
                self.assertTrue(case['expected'].strip())
                self.assertNotEqual(case['input'], case['expected'])
        self.assertEqual(len(self.cases), len({c['input'] for c in self.cases}))


class CoreCoverage(A2Coverage):
    case_file = CASES.with_name('core-cases.json')

    def test_exact_independent_roadmap_inventory(self):
        inventory = json.loads((Path(__file__).parent / 'inventory.json').read_text())
        self.assertEqual(sorted(inventory['skills']),
                         sorted(Path(c['source']).parts[1] for c in self.cases))
        self.assertEqual([f'CORE-{i:03}' for i in range(1, 27)],
                         [c['id'] for c in self.cases])


if __name__ == '__main__':
    unittest.main()
