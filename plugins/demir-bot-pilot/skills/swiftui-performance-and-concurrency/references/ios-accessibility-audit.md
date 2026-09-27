# iOS accessibility review

Original roadmap item 014 guidance. Use for an explicitly requested iOS accessibility review or an accessibility issue in the authorised UI change. Reuse [frontend accessibility guidance](../../frontend-quality-and-accessibility/SKILL.md) for meaningful labels, preserved input, reachable actions, responsive layout and honest evidence. Apply native Apple semantics rather than translating DOM, ARIA or browser focus rules mechanically. Reuse [navigation](swiftui-navigation.md) and [error handling](ios-error-handling.md) for their existing ownership contracts.

## Bound the review

Identify the named screen/task, relevant SwiftUI/UIKit source, supported deployment targets, component conventions and supplied accessibility evidence. Trace the requested user flow and its loading, empty, failure and presentation states where relevant. Do not expand a local fix into a whole-app audit or introduce another design system.

Source inspection can identify declarations and plausible barriers; screenshots show only a particular visual state. Neither proves the spoken output, traversal order, touch targets or interaction of the running app. Without a project, save reusable guidance and state that actual screen findings need source or supplied evidence. Consult current official Apple documentation before choosing version-sensitive modifiers or interoperability behavior.

## VoiceOver and semantics

Prefer native controls with appropriate actions and state. Inspect custom gestures and icon-only controls for an accessible purpose, value and operable action. Preserve visible wording in accessible names where practical. Avoid redundant labels that repeat traits already supplied by the control. Hints should explain a non-obvious outcome, not replace the name or repeat generic interaction instructions.

Review grouping deliberately: combining a row may improve comprehension but must not hide independently meaningful actions. Exclude purely decorative elements only; do not hide content or controls to reduce announcement clutter. Provide meaningful alternatives for images, charts and status indicators, and communicate selection, errors and progress without relying solely on colour or motion.

Inspect custom adjustable controls and gesture-only actions for equivalent accessible operations. Do not assume a tap gesture receives all native button semantics. Use [Apple's accessible controls guidance](https://developer.apple.com/documentation/swiftui/accessible-controls) for the selected platform/API. Actual VoiceOver discovery, wording and activation remain unverified until observed.

## Dynamic Type and layout

Review semantic text styles, custom-font scaling choices and layout constraints against the supported text-size range. Look for fixed heights, single-line truncation, clipping, overlapping elements and actions pushed outside reachable content. Consider long localised text, narrow layouts and accessibility sizes; preserve reading order when content reflows.

Do not solve clipping by globally disabling Dynamic Type, clamping accessibility sizes or shrinking essential text without a justified product requirement and usable alternative. Keep important labels and actions available, with appropriate wrapping or scrolling. Source can expose restrictive constraints but does not establish that every size fits. Apple's [accessibility testing guidance](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app) describes the runtime scenarios; reading it does not authorise running them.

## Focus and navigation

Distinguish text-input/keyboard focus from accessibility focus. [AccessibilityFocusState](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate) is a platform mechanism for requesting or observing assistive-technology focus, not proof of successful placement. Check availability before recommending it.

Inspect expected focus after navigation, sheet presentation/dismissal, validation, deletion and asynchronous content changes. Identify a logical surviving target when the old one disappears. Prefer existing native behavior; request focus only when necessary, and avoid repeatedly stealing it during refresh. Preserve stable element identity and do not impose sort priority merely to conceal a poorly ordered layout.

Review keyboard dismissal, modal escape paths and meaningful status feedback without importing browser-specific trapping rules. Avoid duplicate or overly frequent announcements; retain entered data and a clear correction path after errors. Source findings should identify the intended transition and unresolved runtime behavior, including interaction with UIKit components where present.

## Contrast and motion

Inspect foreground/background choices, semantic colours, opacity, materials and state indicators across the supported appearances. Account for increased contrast, differentiation without colour and reduced transparency where relevant. A named semantic colour or screenshot alone does not prove adequate contrast in every state; do not invent a ratio or declare standards conformance without the appropriate evidence and scope.

Use [Apple's accessible appearance guidance](https://developer.apple.com/documentation/swiftui/accessible-appearance) for native preferences. Inspect animation ownership and how the interface responds to [Reduce Motion](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion). Provide a less motion-intensive presentation while preserving the same information and available actions. Avoid animation as the only feedback, unnecessary large movement and uncontrolled flashing/autoplay. Do not claim motion preferences work merely because a preference is read somewhere in source.

## Findings and acceptance

For each material finding, identify the affected user action, source locator or supplied evidence, likely barrier, smallest authorised correction and what still needs runtime observation. Label conclusions as source-supported, inferred risk or observed behavior with its specific device/OS/settings evidence. Do not present a source review as an Accessibility Inspector run, full accessibility audit or certification; even a separately authorised automated scan would not establish complete accessibility.

Illustrative acceptance examples, not executable checks:

- **VoiceOver:** supplied source uses an unlabeled custom icon gesture for an essential action. Identify the missing semantic/action support and a suitable native correction; do not claim the corrected announcement was heard.
- **Dynamic Type:** source fixes a multi-line form row to a small height. Identify the clipping risk and propose adaptive layout while retaining accessible text sizes; runtime fit remains unverified.
- **Focus/motion:** a sheet closes after an animated save. Trace the intended focus destination and reduced-motion branch without launching the app or assuming the modifier works on every target.
- **No-action case:** an unrelated model-only edit changes no accessibility behavior. Do not initiate a UI audit or add decorative accessibility modifiers.

Source basis: official Apple resources linked above, consulted 27 September 2026; original guidance reusing the bundled frontend specialist. No code examples or checks imported.

Report saved guidance separately from unverified project behavior. This scope authorises no app/simulator/device launches, accessibility setting changes, screenshots, inspectors, scans, checks/fixtures, tests, builds, evaluations, benchmarks, delegation, commits, installations, package operations, index refreshes, cache deletion or background activity. Preserve private data, account/container restrictions and the deferrals for cloud sync, university RAG and training; leave the installed plugin unchanged.
