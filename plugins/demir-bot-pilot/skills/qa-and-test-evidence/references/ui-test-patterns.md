# UI test patterns

Original roadmap item 021 guidance. Use for explicitly requested iOS UI-testing instruction work, a focused review of supplied UI-test evidence or separately authorised UI-test implementation. Reuse [XCTest patterns](xctest-patterns.md) for assertions, async completion and cleanup, and the [SwiftUI accessibility guidance](../../swiftui-performance-and-concurrency/references/ios-accessibility-audit.md) for accessibility semantics. Do not introduce a new framework or broad UI campaign.

## Establish the project and scope

For project work, identify the named app, actual Xcode/Swift/SDK versions, deployment targets, UI-test target/scheme, required user journey and supplied source or failure evidence. Follow existing project conventions and verify version-sensitive APIs against official documentation. Reuse the [project navigation reference](../../swiftui-performance-and-concurrency/references/ios-project-structure.md) rather than loading a full repository map.

Instruction maintenance authorises prose only, not test suites, fixtures, checks, builds or app/simulator launches. Without project evidence, save reusable guidance and state which project decisions remain unknown; do not invent a target, runner, device or successful result.

## Stable identifiers and meaningful queries

Prefer explicit accessibility identifiers that describe a control's stable role within a feature, independent of translated display text, layout position and transient content. Follow existing naming conventions. For repeated rows, use synthetic stable record identity and scope queries to the relevant container; avoid private names, account identifiers or secrets in identifiers and diagnostics.

Keep identifiers separate from user-facing accessibility labels, values and hints. Do not change VoiceOver grouping or add misleading spoken labels solely to make a selector convenient. SwiftUI source modifiers do not prove the runtime accessibility tree exposes the expected element; grouping, containers and platform versions may affect exposure.

Resolve ambiguity deliberately. Avoid using first-match selection, row indexes or screen coordinates to hide duplicate identifiers or unstable ordering. Require uniqueness within the intended scope, or explain the requirement that makes a positional query meaningful. If supplied evidence shows a missing element, distinguish incorrect query scope, screen state, accessibility exposure and availability before proposing a fix. A reliable selector is not evidence of an accessible experience.

## Observable asynchronous states

Describe the journey as initial state, user action and required outcome, including loading, empty, success and recoverable failure states where relevant. Use bounded waits for the observable condition that permits the next step. Check timeout results; do not silently skip an action/assertion when waiting fails, retry until a failure disappears or use arbitrary sleeps as synchronization.

Apple's [XCUIElement documentation](https://developer.apple.com/documentation/xcuiautomation/xcuielement) distinguishes existence, hittability and property-based waits. Existence alone does not establish readiness for interaction or completion of the user's operation. Choose supported waits for the relevant state; a hidden spinner does not establish that saving succeeded. Preserve a meaningful final assertion derived from the requirement, not merely absence of an error.

After navigation or replacement of a screen, query the current intended element rather than assuming an old match still represents it. Bound any scrolling or recovery strategy and retain diagnostic failures. Handle expected system alerts explicitly within the authorised scenario; do not add blanket permission acceptance or interruption suppression. Do not capture private screenshots, element dumps or logs merely to enrich a report.

## Process and data isolation

Treat the UI-test runner and app as separate processes. Test-runner dependency substitution does not automatically replace an app service. Reuse existing app injection boundaries and controlled launch configuration only when app/test implementation is separately authorised. Document which configuration the app actually consumes; arbitrary arguments do not create an isolation mechanism.

Apple's [launchArguments](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/launcharguments) take effect on a subsequent launch when changed during a session. Set any authorised scenario configuration before the intended launch. Keep configuration synthetic and free of credentials; never introduce a production authentication bypass or a destructive reset switch as a default testing convenience.

A fresh app process does not guarantee fresh persistent data, Keychain contents, permissions, account state or remote data. Name those dependencies and distinguish isolated substitutes from genuine integration coverage. For separately authorised implementation, keep resources owned by each scenario, avoid reliance on execution order, and account for parallel runners sharing backend or device state. Scope cleanup to owned synthetic resources and account for partial setup; never reset user data, accounts or device contents to obtain a clean test.

Prefer controlled responses through existing seams for timing and failure scenarios. Do not perform purchases, send messages, change accounts or contact live services implicitly. If a required isolation seam, project or access is missing, explain the dependency and stop the affected operational work; do not fabricate coverage.

## Acceptance examples and evidence boundaries

These are instruction examples, not executable checks or fixtures:

- Trigger: a supplied review shows a button selected by translated text and a fixed delay. Expected action: propose a stable scoped identifier and a bounded wait for the required UI state, followed by the actual outcome assertion. No-action case: no app source or runtime tree is supplied; do not claim the selector works or launch the app to discover it.
- Trigger: supplied failures suggest one scenario inherits another's saved state. Expected action: trace process, persistent-state and dependency ownership and propose a narrowly scoped synthetic isolation boundary. No-action case: only real user storage is available; do not open, copy, reset or migrate it.
- Trigger: instruction-only roadmap maintenance. Expected action: save this guidance and its owner links. No-action case: do not create test code or fixtures, run checks, install tools or expand into a broad UI campaign.

Report saved guidance separately from supplied/observed evidence and unverified project behaviour. Source review does not demonstrate selector stability, wait reliability, cleanup, accessibility quality or passing UI tests. Keep installed-cache and QMD refreshes, cloud synchronization, university RAG, training and background automation inactive; no delegation, commits, publication or provider installation is implied.

## Source basis

Original synthesis for the existing QA and SwiftUI routes, reusing roadmap items 014 and 019. Official Apple XCUIElement and launchArguments documentation consulted on 27 September 2026; API choices still require the actual project's toolchain and deployment compatibility. No runtime validation performed.
