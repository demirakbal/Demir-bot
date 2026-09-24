"""Synthetic package contracts plus one read-only current-source acceptance case."""
import json
import tempfile
import unittest
from pathlib import Path

from structural import inspect


class StructuralContracts(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.inventory = {"plugin": "demir-bot-pilot", "skills": ["alpha", "beta"]}
        self.manifest = {
            "name": "demir-bot-pilot", "version": "0.1.0", "description": "One coordinator and 1 specialist skills.",
            "author": {"name": "Fixture author"}, "skills": "./skills/",
            "interface": {"displayName": "Demir Bot — Private Pilot", "shortDescription": "Fixture",
                          "longDescription": "2 instruction skills.", "developerName": "Fixture author",
                          "category": "Productivity", "capabilities": [],
                          "defaultPrompt": "Use demir-bot-pilot:alpha"}}
        self.save_manifest()
        for name in self.inventory["skills"]:
            self.write(f"skills/{name}/SKILL.md", f"---\nname: {name}\ndescription: Synthetic skill.\n---\n# Start\n")
            self.write(f"skills/{name}/agents/openai.yaml",
                       f"interface:\n  display_name: Fixture\n  short_description: Fixture\n  default_prompt: Use demir-bot-pilot:{name}\n")
        self.write("skills/alpha/references/source.md", "# Evidence\n\n# Evidence\n")

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def save_manifest(self):
        self.write(".codex-plugin/plugin.json", json.dumps(self.manifest))

    def append(self, text):
        path = self.root / "skills/alpha/SKILL.md"
        path.write_text(path.read_text() + text, encoding="utf-8")

    def errors(self):
        return inspect(self.root, self.inventory)["errors"]

    def rejects(self, code):
        self.assertTrue(any(e.startswith(code + ":") for e in self.errors()), code)

    def test_valid_package_and_reference_forms(self):
        self.append('\n[inline](references/source.md#evidence)\n[second][ref]\n\n[ref]: references/source.md#evidence-1\n')
        self.assertEqual([], self.errors())

    def test_wrong_manifest_type(self):
        self.manifest["version"] = 7
        self.save_manifest()
        self.rejects("manifest-schema")

    def test_manifest_duplicate_key(self):
        self.write(".codex-plugin/plugin.json", '{"name":"a","name":"b"}')
        self.rejects("parse")

    def test_manifest_unexpected_runtime(self):
        self.manifest["hooks"] = {"startup": "unwanted"}
        self.save_manifest()
        self.rejects("manifest-schema")

    def test_missing_description(self):
        self.write("skills/alpha/SKILL.md", "---\nname: alpha\n---\n# Start\n")
        self.rejects("description")

    def test_duplicate_skill_names(self):
        self.write("skills/beta/SKILL.md", "---\nname: alpha\ndescription: Duplicate.\n---\n")
        self.rejects("duplicate-name")
        self.rejects("directory-name")

    def test_duplicate_yaml_key(self):
        self.write("skills/alpha/SKILL.md", "---\nname: alpha\nname: beta\ndescription: Duplicate key.\n---\n")
        self.rejects("frontmatter")

    def test_missing_local_file(self):
        self.append("\n[missing](references/absent.md)\n")
        self.rejects("local-link")

    def test_missing_anchor(self):
        self.append("\n[missing](references/source.md#absent)\n")
        self.rejects("local-anchor")

    def test_link_escape(self):
        self.append("\n[private](../../../outside.md)\n")
        self.rejects("outside-package-link")

    def test_symlink_is_not_followed(self):
        (self.root / "skills/alpha/references/private.md").symlink_to(self.root.parent / "not-readable-private-file")
        self.rejects("symlink")

    def test_unknown_route(self):
        self.append("\nUse `demir-bot-pilot:missing-owner`.\n")
        self.rejects("routing-target")

    def test_missing_agent_metadata(self):
        (self.root / "skills/alpha/agents/openai.yaml").unlink()
        self.rejects("agent-metadata")

    def test_agent_routes_to_wrong_skill(self):
        self.write("skills/alpha/agents/openai.yaml", "interface:\n  display_name: A\n  short_description: A\n  default_prompt: Use demir-bot-pilot:beta\n")
        self.rejects("agent-route")

    def test_inventory_drift(self):
        self.inventory["skills"].append("gamma")
        self.rejects("inventory")

    def test_duplicate_inventory(self):
        self.inventory["skills"].append("alpha")
        self.rejects("inventory-duplicate")

    def test_manifest_count_drift(self):
        self.manifest["interface"]["longDescription"] = "3 instruction skills."
        self.save_manifest()
        self.rejects("inventory-count")

    def test_null_manifest(self):
        self.write(".codex-plugin/plugin.json", "null")
        self.rejects("manifest-schema")

    def test_optional_agent_fields_absent(self):
        self.write("skills/alpha/agents/openai.yaml", "interface:\n  display_name: Alpha\n")
        self.assertEqual([], self.errors())

    def test_optional_agent_field_present_but_invalid(self):
        self.write("skills/alpha/agents/openai.yaml", "interface:\n  display_name: Alpha\n  default_prompt: false\n")
        self.assertEqual(["agent-interface: skills/alpha/SKILL.md"], self.errors())

    def test_agent_route_prefix_collision(self):
        self.inventory["skills"].append("alpha-extra")
        self.write("skills/alpha-extra/SKILL.md", "---\nname: alpha-extra\ndescription: Fixture.\n---\n")
        for name in ("alpha", "alpha-extra"):
            self.write(f"skills/{name}/agents/openai.yaml", "interface:\n  display_name: A\n  short_description: A\n  default_prompt: Use demir-bot-pilot:alpha-extra\n")
        self.manifest["description"] = "One coordinator and 2 specialist skills."
        self.manifest["interface"]["longDescription"] = "3 instruction skills."
        self.save_manifest()
        self.assertEqual(["agent-route: skills/alpha/SKILL.md"], self.errors())

    def test_skill_directory_without_metadata(self):
        (self.root / "skills/extra").mkdir()
        self.assertEqual(["missing-skill-file: skills/extra/SKILL.md"], self.errors())

    def test_snapshot_changes_when_reference_changes(self):
        before = inspect(self.root, self.inventory)["snapshot"]
        self.write("skills/alpha/references/source.md", "# Changed\n")
        self.assertNotEqual(before, inspect(self.root, self.inventory)["snapshot"])


class CurrentSource(unittest.TestCase):
    def test_current_package(self):
        report = inspect()
        self.assertEqual([], report["errors"], json.dumps(report, indent=2))


if __name__ == "__main__":
    unittest.main()
