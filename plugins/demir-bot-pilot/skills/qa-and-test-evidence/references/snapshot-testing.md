# Snapshot-testing guidance

Original roadmap item 022 guidance. Use for instruction maintenance or a requested visual-regression review tied to a concrete risk, such as clipped translated text, a missing validation message or unintended layout changes at supported text sizes. For project implementation, identify the actual risk before proposing snapshots. Do not add a broad screenshot campaign merely because a screen exists.

Reuse [UI test patterns](ui-test-patterns.md) for observable screen states and isolation, [XCTest patterns](xctest-patterns.md) for meaningful assertions and ownership, and the SwiftUI specialist's [accessibility](../../swiftui-performance-and-concurrency/references/ios-accessibility-audit.md) and [localization](../../swiftui-performance-and-concurrency/references/ios-localization.md) guidance. Keep this capability in the existing QA and SwiftUI routes; no additional specialist or framework is required by this reference.

## Establish the risk and comparison boundary

For project work, require a named project, actual Xcode/Swift/SDK versions, deployment support, relevant source/design requirements, existing snapshot tooling and operation-specific access. Identify the component or screen, state, expected visual contract and regression a comparison should expose. Use existing tooling and conventions if suitable; do not install a provider, change CI or invent compatibility. Consult the actual tool's official documentation before prescribing version-sensitive capture or comparison options.

Choose the smallest useful set of states and rendering environments based on risk. Explain whether a component render or full-screen capture covers the requirement; an isolated component does not establish navigation, keyboard, safe-area or integration behavior. Prefer semantic assertions for logic and data correctness when images add no meaningful confidence. Do not migrate frameworks merely for snapshot support.

No named app, toolchain or visual evidence is supplied by this roadmap instruction. Saving reusable guidance is complete work in this scope; app-specific configuration and results remain unknown. This instruction-only request does not authorise test files, fixtures, checks, baseline images, capture scripts, builds, app launches or execution.

## Control and record rendering conditions

Describe the comparison environment alongside any separately authorised baseline: source revision, renderer/tool version, device model or simulator configuration, OS version, viewport and scale, orientation, safe-area treatment and capture boundary. Compare like with like; do not assume baselines transfer unchanged between OS or rendering engines.

Specify fonts and their availability, fallback behavior, Dynamic Type size, locale, calendar/time zone where relevant, layout direction, appearance, contrast and motion settings. Select supported variations that expose the named risk rather than multiplying every combination. Missing custom fonts or changed system typography may explain a difference but must not be dismissed without review.

Use owned synthetic content and controlled time, randomness, images and service responses when separately authorised. Reuse existing dependency seams. Settle the intended asynchronous state through observable completion; arbitrary sleeps or a vanished spinner do not prove readiness. Define how animation, transitions, caret/focus, scrolling, loading placeholders and remote assets affect the capture. Avoid disabling behavior that is itself the regression under review.

Control irrelevant status-bar or transient content only through supported project/tool mechanisms. Any crop or mask must be narrow, documented and outside the asserted contract; it must not conceal an error message, clipping or missing control. Do not open real user stores or capture private screens to obtain representative images. Screenshots and difference artifacts require the same privacy care as logs.

## Compare without hiding regressions

When supplied evidence exists, inspect expected, actual and difference images with their environment metadata. Classify the difference as a suspected product regression, intentional design change, environment mismatch or unresolved rendering variability. Separate observed image differences from inferred causes. A capture failure or missing baseline is not a passing comparison.

Use tolerances only when justified by the actual renderer and visual contract. Do not widen thresholds, mask more pixels, change the reference or retry until green to suppress an unexplained failure. Small pixel differences can still hide a meaningful glyph or contrast change; a numeric score alone does not establish acceptability. If conditions differ, retain the evidence and describe the controlled comparison needed, without running it automatically.

## Explicit baseline approval

Initial baseline creation and replacement are review decisions, not automatic consequences of a failing comparison. For any separately authorised baseline proposal, present the affected states, relevant environment, before/after/difference images where available, intended change and requirement or design basis. Name the approving person or established approval process. Approval to write test code or generate a candidate does not imply approval to accept that candidate as correct.

Keep candidate images separate from accepted references until explicit approval covers the exact affected baseline set. Preserve the prior baseline and rationale through the project's existing history process when authorised; do not overwrite references wholesale. A new OS/font/tool version may warrant a reviewed baseline change, but does not automatically justify it. Do not record all failures as new expected output or claim approval that was not supplied.

If approval is missing, report the proposed change and pending decision; do not promote the candidate. This guidance does not authorise generating candidates, committing artifacts, uploading images or publishing anything.

## Acceptance examples and evidence limits

These are prose examples, not test suites, fixtures or executable checks:

- Trigger: supplied evidence shows truncation of a translated validation message at a supported large text size. Expected action: scope a visual comparison to that message and state, specifying locale, font, text size and device/OS conditions, while retaining semantic validation assertions. No-action case: no actual project/risk evidence is supplied; save guidance without inventing snapshots or running an app.
- Trigger: an OS update changes text rendering in supplied differences. Expected action: identify environment mismatch, preserve the differences and propose a controlled review. No-action case: the change is unexplained or approval is absent; do not widen tolerances or replace accepted images.
- Trigger: a design change intentionally moves a control. Expected action: explain the affected baseline set and seek explicit approval for the concrete proposed images when image work is authorised. No-action case: permission covers instruction maintenance only; do not capture images or produce test code.

Report saved guidance, operations actually observed and unverified project behavior separately. A matching snapshot does not prove accessibility semantics, interaction, persistence or release readiness. Source review alone does not prove rendering stability or a passing visual comparison.

Keep installed caches and QMD indexes unchanged; no tests, builds, evaluations, benchmarks, delegation, provider installation, commits/push, spending, account changes or private-data modification is implied. Cloud synchronization, university RAG, training and background automation remain inactive.

## Source basis

Original instruction synthesis from roadmap item 022 and the existing QA, UI-testing, accessibility and localization references. No snapshot library/API compatibility, baseline approval or runtime behavior was verified by this guidance change.
