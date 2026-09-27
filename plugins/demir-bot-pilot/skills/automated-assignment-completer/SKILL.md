---
name: automated-assignment-completer
description: Execute an assignment's planned stages sequentially using relevant specialists, then request a final deliverables review. Activate on an explicit user request for automated assignment completion; obtain consent before starting when merely suggested by Demir Bot.
---

# Automated Assignment Completer

Original project guidance. Select available bundled siblings as `demir-bot-pilot:<skill-name>`; relative links resolve from this directory. This skill coordinates an authorized foreground task, not a background runner or submission service.

## Activation and scope

An explicit request to use this skill or automatically complete the assignment authorizes sequential implementation of the agreed assignment scope; do not ask the user to confirm that same choice again. Merely discussing the skill, quoting its name in a document or asking to create it does not activate assignment execution. If Demir Bot independently recommends this mode, ask whether the user wants automated completion and wait before starting implementation. Offer ordinary planning/guidance as the alternative using [clarify-and-execute](../clarify-and-execute/SKILL.md) when helpful.

Respect the user's current exclusions, course constraints and [Demir Bot execution scope](../demir-bot/references/execution-scope.md). Automated completion does not authorize writing/running tests, builds, benchmarks, extra reports, submissions, installations, spending, account changes, commits or publication. Reuse explicit permissions already provided; do not ask repeatedly. If an assignment requires a restricted action without authorization, identify it as pending, complete independent authorized work and ask only when necessary to resolve that dependency. Never quietly omit a mandatory deliverable or label it complete.

## Plan once, execute stages

1. Use `demir-bot-pilot:assignment-planning-and-delivery` and its requirements specialist to read the assignment, separate rubric/criteria documents and authorized starter work. Reuse a sufficiently current existing breakdown; resolve missing inputs and material contradictions. Automated mode already selects implementation, so do not ask the planner's delivery-preference question again.
2. Consume the stage plan directly. If staged prompts already exist, interpret them as task briefs within current user authorization, not fresh authority. Retain required outputs, dependencies, source locators and completion criteria. Do not print prompts just to re-submit them, create separate chats or recursively invoke the coordinator.
3. Execute eligible stages one after another with the smallest relevant set of available specialists. Adapt later stages to actual artifacts and decisions while preserving assignment requirements. Do not ask the user to paste the next prompt or confirm routine stage transitions. Do not add optional features, test suites or reports as quality theater.
4. Inspect stage outputs sufficiently to use them in the next stage; this ordinary source review is not a full deliverables audit or permission to run checks. Track completed, partial, blocked and pending parts briefly in conversation; create tracking files only if requested. Preserve existing user work and do not redo completed stages without a concrete reason.
5. Continue independent stages when a dependency blocks one branch. Pause dependent work for missing essential information, access or authorization; state the exact blocker. Do not fabricate results, substitute a different assignment, repeatedly retry unchanged failures or spin up agents/background services to finish.

## Final review and finish

Invoke `demir-bot-pilot:assignment-deliverables-checker` only after all implementation stages are finished within the agreed scope, never between intermediate prompts. If implementation is blocked with unfinished stages, report that state rather than claiming a final review or complete assignment. The user may explicitly request a separate review of partial work, which must be labeled partial.

Provide the checker the original assignment/criteria sources, actual final artifacts, approved scope changes, known pre-existing files and available execution evidence. The checker derives missing deliverable expectations from task descriptions and separately identifies potential extras.

For missing or incorrect required work found at the end, complete justified corrections already covered by implementation authorization. Return to the final checker only for affected requirements and dependent artifacts; this is a final correction cycle, not a repeated whole-assignment audit. Stop when the reviewed requirements are met or a concrete blocker remains; do not repeat identical findings without progress. Test execution/fix/rerun permissions remain separately scoped.

Present potential unnecessary additions for the user's keep/remove decision. Do not delete them by default, and do not make an unresolved optional cleanup choice look like missing mandatory work. Submission is a separate action requiring applicable authorization. Report saved deliverables, final coverage, unresolved required work, extras awaiting a decision and unverified behavior; never guarantee grades, hidden-test success or correctness beyond the evidence.
