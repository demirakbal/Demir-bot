# Provenance

Reviewed 2026-09-21.

Adapted from [severity1/claude-code-prompt-improver](https://github.com/severity1/claude-code-prompt-improver/blob/main/skills/prompt-improver/SKILL.md), MIT license retained in LICENSE.upstream. Its targeted questions followed by execution closely match Demir's requested workflow.

Replace Claude-specific hooks, Task/Explore delegation, mandatory research and up to six questions with context-first selective inspection, the actually available question interface, and one to three useful questions. Do not install upstream hooks or assume client integration.

Also inspected [sickn33 prompt-engineer](https://github.com/sickn33/agentic-awesome-skills/blob/main/skills/prompt-engineer/SKILL.md). It emphasizes prompt-only output and framework selection, so it is a weaker default for executing tasks directly. Do not import its invented numerical example requirements, character-count complexity heuristics or requests for hidden reasoning.

These are inspected workflow designs, not proof of better model intelligence or guaranteed token savings. Preserve the user's scope and test clarification behavior on representative requests.
