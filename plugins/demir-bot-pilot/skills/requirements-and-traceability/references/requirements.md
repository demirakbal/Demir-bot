# Requirement quality

Use only relevant fields; match existing format.

`ID | statement | source/version | rationale | priority | scope/status | acceptance criteria | open issues`

For full specs: goal and users; scope/non-goals; capabilities and dependencies when needed; functional requirements; measurable quality requirements; data/interfaces; acceptance and verification approach; assumptions/conflicts; change history. Architecture and execution plans may be separate artifacts.

Check: one independently assessable obligation; clear actor/action/condition/outcome; defined terms and units; consistent priorities; realistic feasibility; source and need; implementation-neutral unless technology is an actual constraint. A story's persona/goal/value does not replace acceptance criteria. MoSCoW is a prioritization convention, not proof every Must has shipped. Won't means out of this scope/version, not permanently forbidden or security risk accepted.

Acceptance examples can use Given/When/Then or explicit input/expected-output tables. Cover applicable normal, alternate, invalid, boundary and forbidden-role behavior. Specify missing versus malformed data, duplicates/order, immutable IDs versus display numbers, per-item versus whole-batch failure, retry/timeout and cross-user isolation when relevant.

Replace 'fast', 'secure', 'easy' and 'scalable' with observable dimensions, measurement method, workload/environment and agreed threshold. If no threshold exists, label it unknown/proposed; never assert a made-up 200ms/100%/99.9% promise. Usability criteria require actual users/tasks and success measures where appropriate, not subjective adjectives alone.

For RAG projects when requested: homework versus exam mode; course/source versions; rubric constraints; retrieval relevance and citation support; permissions, isolation, freshness and agreed cost/latency targets. These are questions, not preapproved commitments.

Course lessons: reconcile duplicate IDs, incomplete criteria, priorities, stable identity and partial-success semantics. Detailed examples are in the active private profile at course-evidence/requirements-and-traceability/references/requirements.md when relevant; never export them.
