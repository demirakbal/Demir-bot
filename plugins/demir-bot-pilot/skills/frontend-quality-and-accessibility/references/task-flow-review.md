# Interaction and task-flow review

Roadmap item 032. Use for a requested interaction/click-path review or instruction maintenance. The parent frontend skill already covers individual controls, states, keyboard/focus and responsive behavior. This reference fills the transition from those local concerns to a complete user task and evidence-backed findings. Reuse QA's [E2E and accessibility scope](../../qa-and-test-evidence/references/test-design.md#project-e2e-and-accessibility-scope) for browser-access, recording and execution boundaries and [evidence guidance](../../qa-and-test-evidence/references/evidence.md) for results. Do not create another coordinator or automatic browser campaign.

## Bound the task and evidence

For project work, identify the named project, relevant stack/tool versions, intended actor, user goal, entry point, expected completion and supplied evidence. Establish source/design review versus authorised browser interaction. A source review can trace handlers and state transitions; a design review can assess intended paths; neither proves the running experience. Provider availability is not authenticated access, a reachable application or permission to perform actions.

Choose one affected task or the requested small set. Name prerequisites, permission boundaries and external side effects. Reuse actual product requirements and existing flows rather than inventing personas, analytics, usability participants or success rates. A review remains read-only unless fixes are authorised. No named project, versions, source flow or browser access is supplied by this roadmap instruction; save guidance without inventing a task failure or opening an application.

## Trace entry through completion and recovery

Follow the path from discoverable entry through required decisions/input to an observable completion state. For each relevant transition, identify the action's meaning, resulting state, feedback and next available step. A button click, navigation change or vanished spinner alone does not prove the user's operation completed. Distinguish confirmed persistence from an optimistic presentation when that boundary matters.

Reuse the parent's loading, empty, no-results, permission, offline and error guidance at the places the actual flow can reach them. Check whether progress is understandable, user input survives recoverable failures, retry is safe and failure leads to a useful next step. Do not add every conceivable state to every control. Consider back/cancel/close, interruption and re-entry where requirements or source show they matter; expose unintended lost input, duplicate actions and dead ends as concrete risks rather than aesthetic opinions.

Review destructive or externally consequential actions for understandable scope and the project's intended recovery/confirmation behavior. Do not prescribe an extra confirmation for every ordinary action. Reviewing a purchase, send, delete or account path does not authorise triggering its real side effect. Use supplied evidence or an existing authorised synthetic boundary; missing isolation is a dependency, not permission to create accounts or modify data.

## Carry keyboard and mobile usability through the path

Trace the same task using keyboard-reachable controls, meaningful focus order, visible focus and appropriate focus movement/restoration after navigation, overlays, errors and removal. Reuse established widget semantics and the parent's form guidance. Do not substitute a mouse-only click sequence for keyboard evidence or claim screen-reader behavior from markup inspection alone.

For supported mobile contexts, consider content reflow, long labels, touch access, scroll position, overlays and on-screen keyboard obstruction along the task. Essential actions must remain discoverable and reachable; hover-only cues or drag-only actions need the existing accessible alternatives. A narrow viewport screenshot is not proof of physical-device usability. State whether findings derive from source, design artifacts, responsive-browser observation or actual device evidence.

## Findings tied to a user outcome

For each useful finding, record the task/step, expected outcome from requirements, actual evidence, impact and smallest relevant correction. Give a source locator or supplied artifact reference. Distinguish an observed failure from a source-supported risk or unresolved design question; do not write guessed reproductions as if performed. Prioritise inability to complete, loss/duplication of work and inaccessible actions using actual impact rather than arbitrary scores or raw click counts.

Use a concise path description only when it helps explain the issue. Do not create a comprehensive journey map, report or redesign automatically. If supplied evidence already establishes a working path and no useful issue is found within scope, say so without inventing findings. A limited review never establishes that every flow works or that accessibility conformance is complete.

Browser interaction, traces, screenshots, fixes and reruns require applicable scope. Do not start servers, log in, install tooling, record sessions or broaden the review merely to strengthen evidence. Reuse the QA execution boundaries rather than adding a second setup/retry procedure. Preserve failures and uncertainty; no silent retry-until-pass loop.

## Acceptance examples and boundaries

Prose examples only, not checks, fixtures or scripts:

- Trigger: supplied source shows a failed submission clears input and provides no retry. Expected action: tie the concern to the affected user task, source and expected recovery, marking runtime behavior unverified unless observed. No-action case: review-only scope; do not edit the component or run the app.
- Trigger: supplied mobile evidence shows an on-screen keyboard obscures the only completion action. Expected action: identify the exact step/environment and propose a scoped layout/focus correction. No-action case: only a static desktop design exists; do not claim a mobile failure was reproduced.
- Trigger: a requested path reaches a real purchase or message action. Expected action: identify the side-effect boundary and available authorised evidence. No-action case: no authority for the external action; stop before triggering it and report the unassessed step.
- Trigger: instruction maintenance. Expected action: save this focused reference and frontend link. No-action case: do not create browser cases, run tests or invent project findings.

Report saved guidance separately from source/design observations, executed operations and unverified behavior. No tests, checks, suites, fixtures, builds, evaluations, benchmarks, delegation, commits/push, provider installation, publication, spending, account changes or private-data modification are authorised here. Preserve unrelated work and keep coordinator routes minimal. Installed caches and QMD indexes stay unchanged; cloud synchronization, university RAG, training and background automation remain inactive.

Source basis: roadmap item 032 and existing frontend and QA guidance. No project flow, browser access, keyboard behavior or mobile usability was executed or verified by this instruction change.
