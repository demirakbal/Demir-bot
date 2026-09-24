---
name: code-refactoring-refactor-clean
description: Review and refactor existing code for maintainability, cognitive complexity, duplication, code smells, modularity, documentation, performance and test quality. Use for clean-code audits, safe restructuring and evidence-based quality reviews, including optional course traceability checks.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Refactor clean

Improve existing code through small, behavior-preserving changes. Adapted from a community workflow using primary sources and Demir's course lessons. This is a workflow, not a bundled scanner or a guarantee of defect-free code.

## Workflow

1. **Scope.** Read repository instructions and relevant configuration. Identify outcome, stack, touched code, callers, contracts and tests. Search first and read focused sections. Expand when dependency/risk evidence requires it; do not reread every file or reference. Recheck cached findings after revisions/configuration change.
2. **Baseline.** Inspect the diff; preserve unrelated work. Identify actual smells and consequences before choosing patterns. Run relevant existing checks only when explicitly requested. Separate inherited from introduced failures. Never invent scanner scores or results.
3. **Protect behavior.** Capture input/output, errors, ordering, duplicates, identity, mutation, authorization, persistence and transaction semantics. Resolve blocking ambiguities while continuing independent safe work. Distinguish authorized behavior changes from refactoring.
4. **Choose proportionately.** Prioritize correctness/security and costly change hotspots. Prefer the smallest useful extraction, simplification or boundary improvement. Avoid speculative frameworks, compulsory interfaces, blanket deduplication and universal size/coverage targets. Existing project gates still apply.
5. **Implement and verify.** Change in reviewable slices. Write characterization/regression tests for behavior at risk only when test creation is explicitly requested. No test scaffolding for trivial low-impact edits. Run targeted checks only when execution is explicitly requested; do not broaden beyond authorization. Preserve required gates and report unmet checks rather than bypassing them. Preserve useful encapsulation: never expose private APIs solely for a test framework.
6. **Finish.** Review the diff; update separate docs/contracts only when requested. Report changes, rationale, commands/results, remaining risks and unverified claims. Improvements require comparable before/after evidence. Mocked integration does not prove real persistence/export; green coverage does not establish complete correctness.

## Read only relevant detail

| Task | Reference |
|---|---|
| Quality audit, smells, scanners, scalability/security | [Quality review](references/quality-review.md) |
| Behavior-sensitive changes, testing, coverage/evidence | [Testing and evidence](references/testing-and-evidence.md) |
| Requirements, design impacts, comments and docs | [Contracts and documentation](references/contracts-and-documentation.md) |
| Course-specific evidence | [Course lessons](references/course-lessons.md) |
| Provenance and research | [Sources](references/sources.md) |

For tiny edits this main workflow suffices. A full audit considers every quality dimension and marks checked/not applicable/not assessed. Prefer configured project tools; explain missing analyzers rather than silently installing infrastructure. Reuse relevant available debugging/review/testing workflows without invoking every skill or duplicating their procedures. Do not delegate by default. Review findings do not authorize publishing or contacting people.

## Targeted error and type review

For a requested error/type review or a concrete risk in the touched behavior, use [error, type and recovery contracts](references/contracts-and-documentation.md#error-type-and-recovery-contracts). “This operation reports success after a failed save” or “review whether these states permit an invalid transition” are positive triggers. A cosmetic edit or a settled small change does not require an extra review pass. Use the relevant ECC-derived questions as review perspectives within the current agent, not separate worker roles; no automatic delegation or executable checks.

For relevant code reviews, examine swallowed errors, empty successful-looking fallbacks, lost error context, unawaited work and unsafe retries. Distinguish intentional cancellation/optional absence from genuine failure; do not demand noisy logging or expose sensitive payloads. Trace the actual caller/user impact before reporting a finding.

When domain invariants matter, inspect construction and mutation paths, encapsulation, validation at untrusted boundaries and whether types prevent actual invalid states. Prefer a small meaningful type change over elaborate wrappers or speculative restrictions. No numeric type-quality scores, mandatory agent pass or automatic repository-wide audit. Report location, evidence, impact, confidence and smallest useful change; fixes and tests stay within authorization.

Source history: references/targeted-review-provenance.md.
