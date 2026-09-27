# Swift lint and formatting

Original roadmap item 023 guidance. Use for instruction maintenance, a requested review of supplied Swift lint/format diagnostics, or separately authorised scoped formatting work. Reuse [project navigation](ios-project-structure.md) for relevant targets and configuration and [architecture review](../../architecture-review/SKILL.md) for actual boundaries and project conventions. Do not introduce another specialist, formatter or style policy by default.

## Establish configuration and authority

For project implementation, identify the named project, affected files, actual Swift/Xcode and tool versions, applicable repository instructions and operation-specific access. Inspect existing configuration and invocation definitions before proposing an operation. Distinguish SwiftLint, SwiftFormat and any other configured Swift formatter by their actual tool identity; similar names do not establish interchangeable configuration or flags.

Follow evidence to relevant configuration files, inherited/nested settings, include/exclude paths, language-version settings and existing package, script or CI integration. Record the working directory and explicit configuration selection where these affect scope. A configuration file's presence does not prove an invocation loads it. Preserve generated/vendor files and project exclusions. Do not read secrets or expand a focused inspection into a full repository inventory.

Use recorded version pins and supplied diagnostics rather than invoking binaries to discover versions in instruction-only work. Before prescribing version-sensitive rules, flags, precedence or autocorrection behavior, consult the identified tool version's official documentation. Do not install, update, resolve packages or fetch remote configuration to fill an evidence gap. If configuration depends on unavailable external material, name that dependency.

This roadmap request authorises prose only. It does not authorise lint/format execution, test suites, fixtures, checks, scripts, build phases, configuration changes or app launches. No named iOS project, tool versions or diagnostics are supplied here; save reusable guidance without inventing project settings or results.

## Interpret findings accurately

Separate formatting/style conventions from maintainability findings and suspected correctness issues. A style warning is not proof of a runtime defect; clean lint output is not proof of correct behavior, actor isolation, accessibility or successful compilation. If a rule identifies a plausible correctness concern, trace it through the actual source and requirements, reusing the SwiftUI specialist or architecture review rather than treating the rule name as a diagnosis.

For supplied diagnostics, record the rule, source location, effective configuration evidence and proposed remedy. Distinguish a source violation from unsupported syntax, configuration parsing, missing tooling or an environment/version mismatch. Preserve the original failure; do not disable a rule globally, blanket-suppress warnings or change thresholds merely to obtain a clean result. A justified local exception should have a narrow scope and reason under project conventions, and requires authority to edit that source/configuration.

Formatting is a source mutation even when a tool offers automatic correction. Review whether a proposed rule can affect expression structure, imports, directives, generated markers or behavior-sensitive code. Do not assume every correction is cosmetic or that formatter output establishes semantic equivalence.

## Keep any separately authorised operation narrow

Differentiate read-only diagnostic review, lint execution, formatter comparison mode, correction and source editing. Confirm the actual tool mode's effects before any authorised invocation; a command called lint or format is not necessarily non-mutating. Inspect relevant wrappers for additional actions. A request to review instructions does not authorise any of these executions.

When execution or formatting is explicitly requested, use the existing configuration and the smallest supported file scope matching that request. Do not format the whole repository to fix one file. If the tool cannot isolate the requested scope, state that limit before expanding it. Preserve unrelated edits, comments, license notices, generated files and private data. Do not combine opportunistic renames, architecture changes or concurrency migrations with style cleanup.

Keep formatting-only changes distinguishable from behavior changes so reviewers can assess each. Inspect the resulting affected diff when edits are authorised; unexpected changes require investigation, not wholesale acceptance or a reset that discards the user's work. A formatter conflict should be resolved from existing project policy and version/configuration evidence, not by repeatedly alternating tools.

Do not enable format-on-save, editor hooks, Git hooks, new CI gates or build plugins automatically. Existing hooks are configuration evidence, not permission to trigger them. Tool execution, fixes and reruns each remain within explicit scope; no automatic fix/rerun loop or additional tests/builds follows a formatting request.

## Acceptance examples and reporting

These are instruction examples, not executable checks or fixtures:

- Trigger: supplied diagnostics report a style violation in one Swift file. Expected action: identify the applicable configuration/version, explain the finding and propose a scoped remedy. No-action case: execution is not authorised; do not run lint or autocorrection.
- Trigger: an authorised formatting request concerns a small change in a project with existing configuration. Expected action: use the supported narrow scope and preserve unrelated work. No-action case: only repository-wide correction is available; do not silently expand the operation or enable a save hook.
- Trigger: tool output rejects syntax used by the project. Expected action: distinguish a suspected tool/version or configuration mismatch from a source defect, stating missing evidence. No-action case: versions are unknown; do not install a newer tool, rewrite valid source or claim compatibility.
- Trigger: instruction-only roadmap maintenance. Expected action: save this reference and its existing specialist route. No-action case: do not create checks, configuration, test code or automation.

Report saved guidance separately from supplied evidence, observed operations and unverified project behavior. For later authorised operations, state the actual scope, configuration/version evidence, changes and failures; never claim lint passed, formatting is stable or behavior is unchanged without appropriate evidence. Missing project/access dependencies do not prevent saving reusable instructions, but do prevent project-specific claims.

Keep installed caches and QMD indexes unchanged. No tests, builds, evaluations, benchmarks, delegation, commits/push, publication, provider installation, spending, account changes or private-data modification is implied. Cloud synchronization, university RAG, training and background automation remain inactive.

## Source basis

Original synthesis from roadmap item 023 and existing SwiftUI, project-navigation and architecture guidance. No tool-specific command, rule compatibility or project execution has been verified by this instruction change.
