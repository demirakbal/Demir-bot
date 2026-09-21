# Sources and adaptation

Inspected with Firecrawl on 2026-09-21.

Primary foundation: [Addy Osmani, documentation-and-adrs](https://github.com/addyosmani/agent-skills/blob/main/skills/documentation-and-adrs/SKILL.md), under [MIT license](https://github.com/addyosmani/agent-skills/blob/main/LICENSE), copyright 2025 Addy Osmani. License retained. Substantially adapted for Demir, not an unchanged upstream copy. Live main-branch sources can change.

Compared alternatives in sickn33/agentic-awesome-skills:
- [documentation](https://github.com/sickn33/agentic-awesome-skills/blob/main/skills/documentation/SKILL.md): broad multi-skill orchestration with many dependencies; overlaps Demir Bot and risks unnecessary work.
- [documentation-templates](https://github.com/sickn33/agentic-awesome-skills/blob/main/skills/documentation-templates/SKILL.md): useful outlines, but insufficient maintenance/evidence workflow alone.
- [documentation-and-adrs mirror](https://github.com/sickn33/agentic-awesome-skills/blob/main/skills/documentation-and-adrs/SKILL.md): pointed to original; original includes useful project-convention matching absent from inspected mirror.

Chosen for focused ADR lifecycle, existing-convention matching, README/API coverage and rationale preservation. Assessment is based on inspected instructions, not proof of extensive upstream testing or a claim of best skill on the internet.

Adaptations: concise main workflow; optional references; requirements/design/test consistency from Demir's course; honest evidence/status and release/approval handling; conditional activation; no required dependencies or executable scripts. Removed unqualified database comparisons, generic npm assumptions, blanket TODO removal and a misleading sliding-window comment on reset-counter code. Existing project conventions and user scope remain authoritative.
