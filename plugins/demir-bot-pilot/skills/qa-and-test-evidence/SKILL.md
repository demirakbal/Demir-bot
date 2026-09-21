---
name: qa-and-test-evidence
description: Plan and implement risk-based tests, review test quality, investigate coverage gaps and produce honest execution evidence. Use only for explicitly requested QA strategy, test creation/execution, integration/export/persistence verification or evidence audits. Skip unnecessary test infrastructure for trivial low-impact edits.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# QA and Test Evidence

A focused adaptation of test-automator with Demir's course evidence practices. See references/sources.md. No scanners, browser helpers or paid test services are bundled or assumed installed.

1. Read relevant requirements, changed behavior, existing tests and configured commands. Search targeted files first. Identify risks, affected dependencies and real versus mocked boundaries. Reuse the project stack; do not automatically install frameworks or rewrite CI.
2. Choose the smallest sufficient test strategy. Use unit tests for logic, integration/contract tests for boundaries, real persistence/artifact tests for those claims, and system/acceptance checks for user outcomes. Use references/test-design.md for applicable techniques. Derive expected results from requirements and independent reasoning, not merely copying the implementation.
3. Implement tests when authorized and useful. Assert observable behavior with deterministic, isolated fixtures and cleanup. For meaningful bug fixes demonstrate the regression fails for the right reason before the fix where feasible. Reuse existing TDD/debugging workflows when relevant without duplicating ceremony. Never weaken assertions or delete failing tests just to obtain green results.
4. Execute checks only when explicitly requested, in an appropriate environment and within that scope. Writing tests does not authorize running them; running tests does not authorize fixes or reruns. Required gates remain unmet if execution is not authorized. Do not run destructive database operations, production load/chaos tests, paid services or external messages without applicable authorization. Use synthetic/sanitized data and avoid secrets in artifacts.
5. Inspect exit codes, results, assertion scope and artifacts. Diagnose failures rather than assuming product bugs or infrastructure errors. Preserve failure/retest history. Do not treat retries or self-healing selectors as permission to hide regressions. If execution is unavailable, explicitly mark checks not run.
6. Report changed tests, commands, actual outcomes, coverage boundaries and unresolved risk. Use references/evidence.md for formal reports and coverage claims; concise results suffice for ordinary changes. Tests passing does not establish deployment readiness, stakeholder acceptance or security outside the assessed scope.

Use requirements-and-traceability for substantial criterion ambiguity and documentation-and-adrs for separate document maintenance. Do not recursively invoke Demir Bot or load all specialists. Refactoring remains conditional on a concrete benefit. If no additional test provides meaningful confidence, explain that rather than adding implementation-mirroring tests.

For explicitly requested Demir Bot routing or workflow evaluation, read references/demir-bot-evaluation.md. No evaluation is triggered by skill installation or ordinary coding work.
