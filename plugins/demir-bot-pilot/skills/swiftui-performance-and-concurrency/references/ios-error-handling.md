# iOS error handling

Original roadmap item 006 guidance. Use for a requested error-handling change or a source-backed gap in failure propagation, recovery or presentation. Reuse the parent skill's cancellation, isolation and task-lifetime rules and [iOS architecture patterns](../../architecture-review/references/ios-architecture-patterns.md) for state and service boundaries. Preserve existing project conventions; do not add an error framework or rewrite all failure types.

## Trace the actual failure contract

Inspect one affected operation from the view through its model/service and network or persistence boundary, then back through mapping, recovery and presentation. Identify success, valid empty data, expected absence, cancellation, failure and uncertain completion separately where relevant. A failed fetch is not an empty collection, and an unconfirmed save is not a successful save.

Use actual source, supplied diagnostics and project settings. Do not invent provider error codes, storage guarantees or supported language features. Structured domain error types do not require adopting Swift typed-throws syntax; check the actual compiler/language mode and current official documentation before prescribing version-sensitive syntax. Missing app source blocks a concrete app correction, not an independently supported reusable instruction update.

## Preserve useful error information

- Define meaningful cases at the boundary that owns their interpretation, using existing types where sufficient. Examples may include invalid input, unavailable data, access denial, conflict and temporary service failure, but add only cases the actual contract supports.
- Map low-level failures when a consumer needs a stable domain meaning. Preserve the underlying cause and useful operation context in an appropriate diagnostic representation; do not repeatedly replace errors with generic strings or classify them by matching localised text. Unknown failures remain failures rather than being forced into a misleading known case.
- Keep diagnostic detail separate from the user-facing message. Preserving cause does not mean logging full payloads, tokens, personal records or private URLs. Retain only necessary, redacted details under existing logging/retention policy; do not add telemetry or copy private data into the skill package.
- Respect isolation when errors or diagnostic values cross actor boundaries. Do not silence transfer diagnostics or retain arbitrary mutable framework objects just to preserve a cause. Use supported safe representations and explicitly retain uncertainty if information is unavailable.
- Avoid empty catches, blanket try?, fabricated defaults and unconditional success cleanup when they erase a meaningful failure. An intentional fallback must state its meaning: cached data can be stale, and a partial result can be incomplete. A successful empty result must come from the operation's contract, not its catch branch.

## Cancellation and result ownership

Reuse the parent skill's cooperative cancellation and generation/identity guidance. Recognise cancellation through the actual task and provider contracts; different operations may report it differently. Do not label every error as cancellation just because a task was later cancelled, or suppress unrelated failures indiscriminately.

Propagate cancellation where the caller owns lifecycle decisions. At the presentation boundary, avoid an alarming failure alert for work deliberately abandoned by navigation or a newer request. Ensure old failure, success and cleanup paths cannot overwrite the new request's state. Assign loading/error ownership explicitly and release resources according to the operation's contract.

Cancellation of local waiting does not prove a remote mutation was rolled back. Treat a timeout, lost response or cancelled save as potentially uncertain when the service contract allows it; do not claim success or failure of the remote action without evidence.

## Recovery and user messages

Assign recovery to one appropriate owner so view, model and network layers do not each retry independently. Choose actions from actual failure semantics:

| Situation supported by evidence | Recovery direction |
|---|---|
| Correctable input | Preserve the draft and identify the relevant field or requirement. |
| Temporary read failure | Offer a bounded retry or explicitly labelled cached state where useful. |
| Access/session problem | Use the existing access flow; do not endlessly retry or bypass authorisation. |
| Conflict or stale record | Preserve edits and follow the actual conflict/reload policy; do not silently overwrite. |
| Mutation with unknown completion | Reconcile status or use established idempotency support before repeating it. |
| Unsupported or unknown failure | Give a truthful failure message and only actions the app can actually perform. |

Automatic retry is not a default. Where explicitly required, bound attempts and delays, honour cancellation and provider rules, and prevent duplicate side effects. Retrying a write needs evidence that repetition is safe; a button labelled Retry does not establish that. No background retry service follows from this guidance.

Explain what did not complete, whether input was preserved and what the user can do next. Avoid raw stack traces, unsupported promises and messages that imply a save succeeded. Use existing localisation/accessibility conventions, choose inline versus alert presentation to match impact, and give one component responsibility for presentation so the same failure does not produce duplicate alerts. Clear obsolete errors when the operation's state actually changes; do not erase unsaved work merely to dismiss a message.

## Acceptance and boundaries

Illustrative acceptance examples, not executable checks:

- **Trigger:** a supplied fetch catches every error and returns an empty list. **Expected action:** preserve genuine empty success separately from failure, retain an appropriate cause and present an actionable error without replacing previously valid data misleadingly.
- **Uncertain save:** a response is lost after submission. **Expected action:** inspect the mutation contract, retain the draft and distinguish unknown completion from confirmed rejection; do not blindly resubmit or show Saved.
- **Cancellation:** a user navigates away during a request. **Expected action:** apply lifecycle ownership and cancellation rules without a stale alert or an older cleanup clearing a newer request's loading state.
- **No-action case:** existing error propagation and presentation already preserve the required distinctions. Reuse them; do not introduce a parallel hierarchy solely for uniformity.

Report saved guidance/code separately from source observations and unverified runtime behavior. A real app implementation needs its source, toolchain/settings and relevant error contract or evidence. No tests, fixtures, builds, previews, evaluations, benchmarks, delegation, commits, provider installation, publication, index refreshes or background activity are authorised by this reference. Preserve private data and leave installed caches, cloud sync, university RAG and training unchanged.
