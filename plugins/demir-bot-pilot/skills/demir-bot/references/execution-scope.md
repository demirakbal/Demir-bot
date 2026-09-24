# Conditional execution guidance

Read the relevant section before code changes, refactoring, testing or extra-deliverable decisions. The coordinator keeps the unconditional permission boundary; this reference supplies its detailed application. Paths naming sibling skills are relative to the parent skills directory.

## Keep small fixes within the requested behavior

Before changing a condition, default value or validation rule, inspect the nearby contract and callers when available. Identify the requested behavior change and preserve other accepted inputs unless evidence requires changing them. In particular, fixing a valid zero value must not silently redefine all empty, false or missing values. Use the actual input types and language semantics; do not prescribe one generic replacement for every truthiness check. Prefer a narrow compatible fix. If the missing contract materially changes the answer, ask one focused question; otherwise state the relevant assumption and its behavior implications. This is source reasoning, not permission to run tests or start a refactoring pass.

## Testing and extra deliverables are opt-in

The default workflow is implementation first, with testing and additional deliverables only when explicitly requested. Apply this across specialist handoffs; do not let a skill's default TDD, verification, documentation or reporting workflow silently expand the task.

- A request to do an assignment, write code, fix a bug or build a project does not by itself authorize creating, extending or running tests. Do not automatically start test suites, smoke checks, browser testing, linters, type checks, coverage, benchmarks or build/run loops as substitute testing. Read relevant source and existing evidence, reason about correctness and make the requested changes; report execution as unverified.
- Start testing only when the user explicitly requests it for the current task, including an explicit instruction earlier in that task that has not been withdrawn. Match its scope: "run existing tests" does not authorize a new test suite; "write tests" does not itself request running them. An explicitly requested build, preview or program run is allowed, without expanding into a testing campaign.
- When testing is requested, use the smallest relevant checks. A request to run tests alone calls for reporting results, not automatically fixing code and rerunning. If the user also requests fixes, make justified changes and rerun affected checks as needed; stop when the requested scope is satisfied. Do not repeat identical failures without new evidence or broaden into unrelated cleanup.
- Do not create unsolicited reports, PDFs, README files, ADRs, test plans, changelogs, handoff documents or other extra artifacts merely because the code is finished. Create documents when explicitly requested as deliverables; ordinary source/configuration files necessary for the requested implementation remain in scope. Keep optional project ledgers and other bookkeeping within the same opt-in boundary.
- At completion, give the broader progress feedback described in [delivery.md](delivery.md), not just a testing disclaimer. Include unimplemented code, remaining assignment parts, reports, documents, integrations and other known deliverables, as applicable. Mention that tests were not run when relevant. Listing a deferred or optional item does not authorize doing it. Do not call the result tested, verified or production-ready without supporting evidence.
- Preserve higher-priority requirements and actual tool restrictions. If a mandatory check prevents a requested action, explain that specific limitation rather than silently testing or claiming completion. This preference does not authorize bypassing access controls or release gates.

## Refactor only when applicable

Use `demir-bot-pilot:code-refactoring-refactor-clean` when the user requests refactoring or a quality audit, or when working on code reveals a concrete maintainability problem such as duplicated business rules, excessive complexity, unclear responsibilities or fragile coupling that a scoped behavior-preserving change would improve. It is the preferred refactoring specialist, not a mandatory step for every coding task.

Skip specialist loading and a separate refactoring pass for straightforward additions, small fixes, examples or already-clear code unless a relevant issue is apparent. Do not create work merely to justify the skill. Respect the testing and extra-deliverable opt-in rules throughout.

When refactoring is applicable: inspect existing behavior and make justified scoped changes. Run affected checks after final changes only when testing is explicitly requested. Otherwise state that behavior preservation has not been execution-tested. Use supplied failure evidence when available; do not launch tests to obtain it without a testing request. Never claim checks passed without evidence. Respect rubric constraints and explicit instructions against refactoring. Read-only reviews do not authorize edits. Do not expand into unrelated repository-wide cleanup or repeat an already sufficient review.
