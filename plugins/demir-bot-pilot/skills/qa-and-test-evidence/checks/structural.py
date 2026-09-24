"""Read-only package inspection. No network, host discovery or external execution."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator
from markdown_it import MarkdownIt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MD = MarkdownIt("commonmark")


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError("duplicate YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_json)


def inspect(root=ROOT, inventory=None):
    root = Path(root).resolve()
    expected = inventory if inventory is not None else read_json(HERE / "inventory.json")
    errors, skipped = [], set()
    texts, hashes = {}, {}
    skill_directories = set()

    def fail(code, path):
        errors.append(f"{code}: {path}")

    # Never follow a package symlink into private profiles or other trees.
    def walk(folder):
        for path in sorted(folder.iterdir()):
            rel = path.relative_to(root).as_posix()
            if path.is_symlink():
                fail("symlink", rel)
            elif path.is_dir():
                if folder == root / "skills":
                    skill_directories.add(path.name)
                if path.name != "__pycache__":
                    yield from walk(path)
            elif path.is_file():
                yield path

    for path in walk(root):
        rel = path.relative_to(root).as_posix()
        try:
            raw = path.read_bytes()
            hashes[rel] = hashlib.sha256(raw).hexdigest()
            if path.suffix in {".md", ".yaml", ".json"}:
                texts[rel] = raw.decode("utf-8")
        except (OSError, UnicodeError):
            fail("unreadable", rel)

    def parse(rel, kind):
        try:
            text = texts[rel]
            return (json.loads(text, object_pairs_hook=unique_json) if kind == "json"
                    else yaml.load(text, Loader=UniqueLoader))
        except (KeyError, ValueError, yaml.YAMLError, TypeError):
            fail("parse", rel)
            return None

    manifest = parse(".codex-plugin/plugin.json", "json")
    if "parse: .codex-plugin/plugin.json" not in errors:
        schema = read_json(HERE / "manifest.schema.json")
        for problem in Draft202012Validator(schema).iter_errors(manifest):
            fail("manifest-schema", ".codex-plugin/plugin.json/" + "/".join(map(str, problem.path)))

    skills = sorted(p.split("/")[1] for p in texts
                    if re.fullmatch(r"skills/[^/]+/SKILL\.md", p))
    for missing in sorted(skill_directories - set(skills)):
        fail("missing-skill-file", f"skills/{missing}/SKILL.md")
    if len(expected["skills"]) != len(set(expected["skills"])):
        fail("inventory-duplicate", "checks/inventory.json")
    if skills != sorted(expected["skills"]):
        fail("inventory", "skills/")
    if manifest and isinstance(manifest, dict):
        if manifest.get("name") != expected["plugin"]:
            fail("identity", ".codex-plugin/plugin.json")
        interface = manifest.get("interface", {})
        if isinstance(interface, dict):
            prose = str(manifest.get("description", "")) + " " + str(interface.get("longDescription", ""))
            for count in re.findall(r"\b(\d+) instruction skills\b", prose):
                if int(count) != len(skills):
                    fail("inventory-count", ".codex-plugin/plugin.json")
            for count in re.findall(r"\b(\d+) specialist skills\b", prose):
                if int(count) != len(skills) - 1:
                    fail("inventory-count", ".codex-plugin/plugin.json")

    names = set()
    for skill in skills:
        rel = f"skills/{skill}/SKILL.md"
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", texts[rel], re.S)
        try:
            meta = yaml.load(match.group(1), Loader=UniqueLoader) if match else None
        except (ValueError, yaml.YAMLError, TypeError):
            meta = None
        if not isinstance(meta, dict):
            fail("frontmatter", rel)
            continue
        name = meta.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail("skill-name", rel)
        else:
            if name in names:
                fail("duplicate-name", rel)
            names.add(name)
        if name != skill:
            fail("directory-name", rel)
        if not isinstance(meta.get("description"), str) or not meta["description"].strip():
            fail("description", rel)
        agent = parse(f"skills/{skill}/agents/openai.yaml", "yaml")
        if not isinstance(agent, dict):
            fail("agent-metadata", rel)
        else:
            interface = agent.get("interface")
            if not isinstance(interface, dict) or any(
                not isinstance(interface.get(key), str) or not interface[key].strip()
                for key in ("display_name", "short_description", "default_prompt")
                if key == "display_name" or key in interface
            ):
                fail("agent-interface", rel)
            elif "default_prompt" in interface and skill not in re.findall(
                r"\bdemir-bot-pilot:([a-z0-9]+(?:-[a-z0-9]+)*)(?![\w-])",
                interface["default_prompt"],
            ):
                fail("agent-route", rel)

    for rel in texts:
        if re.fullmatch(r"skills/[^/]+/agents/openai\.yaml", rel) and rel.split("/")[1] not in skills:
            fail("orphan-agent", rel)

    def tokens(text):
        # Metadata is not Markdown; avoid treating its delimiters as headings.
        return MD.parse(re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", "", text, count=1, flags=re.S))

    def anchors(text):
        result, counts = set(), {}
        stream = tokens(text)
        for i, token in enumerate(stream):
            if token.type == "heading_open":
                inline = stream[i + 1]
                label = "".join(c.content for c in (inline.children or [])
                                if c.type in {"text", "code_inline"})
                slug = re.sub(r"[^\w\- ]", "", label.lower()).replace(" ", "-")
                n = counts.get(slug, 0)
                counts[slug] = n + 1
                result.add(slug + (f"-{n}" if n else ""))
        return result

    for rel, text in texts.items():
        for target in re.findall(r"\bdemir-bot-pilot:([a-z0-9]+(?:-[a-z0-9]+)*)", text):
            # Documented namespace placeholders are not literal routes.
            if target not in {"skill-name"} and target not in skills:
                fail("routing-target", rel + " -> " + target)
        if not rel.endswith(".md"):
            continue
        for token in tokens(text):
            for child in token.children or []:
                href = child.attrGet("href") if child.type == "link_open" else child.attrGet("src") if child.type == "image" else None
                if href is None:
                    continue
                url = urlsplit(href)
                if url.scheme or url.netloc:
                    skipped.add("external URLs not fetched")
                    continue
                if url.path.startswith("/"):
                    fail("absolute-local-link", rel)
                    continue
                dest = (root / rel).parent / unquote(url.path) if url.path else root / rel
                resolved = dest.resolve()
                try:
                    target_rel = resolved.relative_to(root).as_posix()
                except ValueError:
                    fail("outside-package-link", rel)
                    continue
                # Membership avoids reading symlink destinations even inside root.
                if target_rel not in hashes:
                    fail("local-link", rel + " -> " + target_rel)
                elif url.fragment and target_rel.endswith(".md"):
                    if unquote(url.fragment) not in anchors(texts[target_rel]):
                        fail("local-anchor", rel + " -> " + target_rel + "#" + url.fragment)
    snapshot = hashlib.sha256(json.dumps(hashes, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"errors": sorted(set(errors)), "snapshot": snapshot, "file_count": len(hashes),
            "skill_count": len(skills), "limits": sorted(skipped)}


if __name__ == "__main__":
    import sys
    report = inspect()
    print(json.dumps(report, indent=2))
    sys.exit(1 if report["errors"] else 0)
