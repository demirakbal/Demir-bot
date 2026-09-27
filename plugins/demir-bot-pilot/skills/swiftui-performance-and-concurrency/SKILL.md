---
name: swiftui-performance-and-concurrency
description: Implement or review SwiftUI state, view-update performance and safe Swift concurrency for Apple-platform projects. Use for relevant SwiftUI changes, task lifecycle, isolation diagnostics or performance problems; follow actual toolchain settings and do not automatically build, profile or test.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# SwiftUI performance and concurrency

## Focused source-review entrypoint

For concurrency, state-lifetime or identity work, follow one affected flow through the existing sections below rather than treating each topic as a separate skill:

1. Establish the requested outcome and available evidence: relevant source, a supplied diagnostic or reported behavior, and project settings. Separate compiler/toolchain version, Swift language mode, target isolation flags and deployment target; leave unknown values explicit.
2. Trace the source of truth and its owner from view creation through navigation or reconstruction. Identify injected services and whether their lifetime matches the state they own. Apply **State ownership and view updates** before changing wrappers or dependencies.
3. Trace work from its trigger through suspension to the final state update. Identify actor boundaries, captured values and any transfer across isolation boundaries. Apply **Actor isolation and safe sharing** to the actual diagnostic or ownership problem, preserving useful compiler checks.
4. Follow cancellation, restart, failure and cleanup along that same flow. Identify who owns each task and whether an older result or cleanup can overwrite newer state. For callback bridges, inspect completion and cancellation paths together; consult **Task lifetime and cancellation** and the continuation guidance below.
5. Relate list, navigation and task identity to the intended lifetime. Distinguish a deliberate reset from accidental recreation, unstable identifiers or work restarted by changing input. Trace the relevant source locations rather than assuming every repeated update is a performance defect.
6. Select the smallest supported correction using the project's existing architecture. Add async-sequence, continuation or task-group detail only when the affected flow demonstrates a missing case. Reuse architecture-review for a genuine ownership/boundary decision and QA only within explicitly requested testing scope.
7. Report the source-backed finding, changed guidance or code, and unresolved settings or runtime evidence. Source inspection alone does not establish compilation, cancellation behavior, race freedom or performance improvement.

Distinguish skill maintenance from app implementation. An explicitly requested reusable workflow improvement can be saved when inspection demonstrates a gap in this skill, even without a named app. Missing project evidence blocks project-specific fixes and version-dependent prescriptions, not an independently supported instruction change. Do not invent an app, diagnostic or observed runtime failure to justify an extension; if no instruction gap is found, explain what is already covered.

## Establish project context

For a named target's signing/provisioning diagnostics, reuse [code-signing and provisioning](references/xcodebuild-error-taxonomy.md#code-signing-and-provisioning). Distinguish identity, bundle ID, entitlements and profile evidence; no account, certificate or signing-asset changes follow from diagnosis alone.

For requested Xcode command-line integration, use [Xcode CLI integration](references/xcode-cli-integration.md) to establish installed-tool evidence and the exact operation contract. Revalidate upload tooling for the intended service; documentation or tool discovery does not authorise execution, account access or uploads.

For requested simulator/device selection, launches or screenshots, use [Simulator and device management](references/simulator-device-management.md). Establish the exact target and operation-specific authority; preserve unrelated devices and data. Instruction maintenance does not authorise device operations.

For requested Swift lint or formatting guidance, use [Swift lint and formatting](references/swiftlint-swiftformat-ios.md). Reuse the project's actual configuration and tool versions, keep changes scoped, and separate style findings from correctness evidence; do not run tools or enable hooks automatically.

For iOS-specific transport, storage, entitlement or interprocess-communication hardening, use [iOS security boundaries](references/ios-security-hardening.md). Reuse existing Codex Security/privacy routes; do not launch scans or infer vulnerabilities from configuration names alone.

For Apple privacy manifests, reuse privacy-review's [privacy-manifest guidance](../privacy-review/references/privacy-manifests.md). Trace actual app/SDK behavior and current Apple requirements before declaring data use or API reasons; a template is not compliance evidence.

For CloudKit ownership, conflicts, offline state or schema environments, use [CloudKit sync](references/cloudkit-sync.md). Distinguish framework-managed mirroring from direct CloudKit operations; source review does not authorise account access or sync activation.

For versioned SwiftData schemas, migration paths or migration recovery, use [SwiftData migrations](references/swiftdata-migrations.md). Inspect schema and container declarations without opening stores; defining a plan does not authorise migration execution.

For Core Data adoption or coexistence with SwiftData, use the same reference's [store-transition guidance](references/swiftdata-migrations.md#core-data-to-swiftdata-transitions). Establish model compatibility, ownership and rollback assumptions before proposing a change; preserve existing stores.

For secret storage, Keychain access policy or CryptoKit integration, use [Keychain and CryptoKit](references/keychain-cryptokit.md). Reuse privacy guidance, establish deployment and recovery requirements, and never access credentials or alter Keychain data merely to inspect the design.

For Swift package versions, resolution records, package resources or binary-target questions, use [Swift package management](references/spm-dependency-management.md). Preserve lockfiles and distinguish declared requirements from recorded resolution and observed compatibility; do not fetch, resolve, update or reset packages automatically.

For supplied Xcode build failures, use [Xcode diagnostic classification](references/xcodebuild-error-taxonomy.md) to distinguish the failed build phase from its underlying cause. Inspect existing evidence without automatically rerunning builds or clearing caches.

For suspected stale build artifacts or cache inconsistencies, use [DerivedData hygiene](references/xcodebuild-error-taxonomy.md#deriveddata-hygiene-and-scoped-recovery). Establish output ownership and consider non-cache causes before proposing narrowly scoped recovery; preserving working caches is the default.

For requested iOS project orientation, or when the affected target, scheme, package, resource or configuration is unclear, use [iOS project navigation](references/ios-project-structure.md). Reuse a focused existing map for a known-path edit; do not remap the repository each turn.

Inspect relevant source, project/package manifests, xcconfig and available diagnostics before choosing a pattern. Determine deployment targets, supported Swift/Xcode versions, language mode, concurrency checking, default actor isolation and enabled upcoming features from existing evidence. Toolchain version, language mode and per-target settings are different facts; do not infer one from another. If effective settings remain unknown, state that limitation and avoid relying on a newer feature. Do not invoke build tools merely to discover settings without applicable authorization.

Preserve the actual project architecture and dependencies. No automatic Observation migration, concurrency-mode changes, library installation or repository-wide refactoring. Consult current official Apple/Swift documentation for version-sensitive syntax, isolation behavior or APIs when needed. Swift 6.2 does not by itself establish MainActor defaults or caller-isolation behavior for every target. Do not copy upstream examples without inspecting their assumptions.

Inspect the actual project repository when provided; this skill's installation does not establish project access or build settings. Apply project confidentiality restrictions from the active private profile before public reuse. Figma's SwiftUI workflow serves design translation when relevant, not concurrency or runtime-performance verification.

## State ownership and view updates

For string catalogs, pluralisation, locale-sensitive formatting or right-to-left layouts, use [iOS localisation](references/ios-localization.md). Preserve approved translations and supported deployment/toolchain conventions; source inspection does not establish linguistic or rendered correctness.

For requested native iOS accessibility review or fixes, use [iOS accessibility](references/ios-accessibility-audit.md) for VoiceOver, Dynamic Type, focus, contrast and motion. Distinguish source evidence from device-tested behavior; do not launch an audit or app automatically.

For navigation state, route selection, restoration or incoming links, use [SwiftUI navigation](references/swiftui-navigation.md). Preserve the app's supported navigation APIs and existing ownership; do not migrate its navigation framework by default.

When the issue requires choosing feature boundaries, data ownership or module structure, reuse architecture-review's [iOS architecture patterns](../architecture-review/references/ios-architecture-patterns.md). Keep wrapper, identity and concurrency mechanics here; do not impose an architectural rewrite for a local state fix.

For service construction, stable ownership or replaceable dependencies, use the shared [dependency-injection guidance](../architecture-review/references/ios-architecture-patterns.md#dependency-injection-and-service-lifetime). Follow existing project conventions and distinguish replacing a passed dependency from changing one retained by an existing owner.

- Identify the source of truth, owner, lifetime and observation mechanism before selecting wrappers. Use local state for view-owned state and bindings for borrowed mutation; inject shared dependencies at an appropriate stable boundary.
- Use Observation/Observable models only where supported and compatible with the project. Preserve ObservableObject/StateObject/ObservedObject/EnvironmentObject patterns where appropriate; newer syntax alone is not a reason to migrate. A passed class reference is not immutable merely because no wrapper is present.
- Keep model lifetime stable across view reconstruction. Do not repeatedly create owned services or duplicate a parent's source of truth in a child. Model initialization should not start uncontrolled side effects.
- Keep body evaluation free of I/O and expensive transformation. Narrow state dependencies and split meaningful subviews when it reduces coupling or unnecessary work; do not promise that extraction prevents every update or that each body evaluation equals a full render.
- Preserve semantic identity across data refresh, insertion, reordering and navigation. Use stable unique model identifiers; avoid generating new IDs in body. Index identity only fits collections whose positional identity is intentionally stable. An explicit .id change can reset state and task lifetime; use deliberately.
- Choose List/lazy containers based on interaction, layout and collection size, not a universal performance rule. Avoid unnecessary type erasure, layout feedback cycles and costly effects on hot paths, but do not claim measured savings without evidence. Equatable-based optimizations require correct input equality and an appropriate integration mechanism; conformance alone is no blanket rendering guarantee.

## Expensive work and evidence

For source-based performance investigation or supplied Apple traces, use [performance evidence](references/apple-performance-analysis.md) for workload context, launch, CPU/wait time, memory and I/O interpretation. Keep capture and measurement separately authorised; no trace means no measured bottleneck claim.

Use supplied profiling evidence when available. Without it, label suspected bottlenecks as hypotheses grounded in source: repeated decoding/sorting, synchronous I/O, excessive invalidation, redundant fetches or main-actor CPU work. Reduce repeated work with appropriately scoped caching/precomputation, including invalidation, memory bounds and concurrency ownership. Do not turn a cache into shared mutable unsynchronized state.

Async does not mean background execution. Task creation may inherit actor context; wrapping heavy work in Task does not inherently move it away from UI isolation. Choose an explicit, supported execution boundary and safe values for expensive processing; do not prescribe Task.detached or @concurrent universally. Avoid blocking cooperative executors with semaphores or synchronous waits on async work. Do not profile, benchmark or run Instruments without a request.

## Task lifetime and cancellation

For failure types, recovery decisions or user-facing error messages, use [iOS error handling](references/ios-error-handling.md). Reuse the cancellation and stale-result rules below; do not convert failed or cancelled work into apparent success.

- Tie UI work to meaningful lifetime and input identity, using the existing architecture and view task APIs where appropriate. A task keyed to changing input can restart; avoid duplicate requests caused by view recreation, appearance callbacks and unstructured tasks.
- Cancellation is cooperative. Propagate cancellation, check it at meaningful boundaries and stop publishing results for abandoned work. Handle cancellation separately from genuine failures; do not turn cancellation into an empty successful result or an alarming error banner.
- Guard against stale/out-of-order results after suspension: confirm request identity or use an owned generation mechanism before committing state. Ensure an older task's cleanup cannot incorrectly clear a newer task's loading state.
- Prefer structured child tasks for bounded concurrent work. If unstructured work is needed, make ownership, handles, cancellation and cleanup explicit. Detached work does not automatically inherit structured lifetime or cancellation; document why it is needed within source when non-obvious.
- Review captured references and subscriptions for unwanted lifetime extension; weak references are not a universal substitute for explicit cancellation. Bound parallelism and manage resource cleanup. Do not swallow errors with try? unless losing the distinction is intentional and justified.

## Actor isolation and safe sharing

Map UI/model ownership and actor boundaries before changing annotations. Keep UI state updates on the required actor. Use actors or other appropriate synchronization for shared mutable services; do not isolate all work to MainActor just to silence diagnostics.

An actor protects isolated access but does not make an entire async operation atomic across await. Revalidate invariants after suspension and design reservations, version checks or sequencing where necessary. Avoid moving mutable non-Sendable references across isolation boundaries without a supported safe ownership design. Prefer immutable transferable values when appropriate.

Treat Sendable diagnostics as evidence to investigate, not invitations to add @unchecked Sendable, nonisolated(unsafe), unsafe casts or blanket preconcurrency suppressions. Such escape hatches need an actual safety argument and scoped necessity. Nonisolated does not itself guarantee background execution or thread safety. Match isolated conformances, @concurrent and default isolation features to the actual compiler/settings; preserve useful legacy interop instead of automatically replacing all DispatchQueue code.

When bridging callbacks, account for cancellation, errors, executor context and exactly-once continuation resumption. Prevent duplicate completion and abandonment; do not block an actor waiting for a callback that requires the same actor. Distinguish data-race safety from higher-level ordering, stale data and business-logic correctness.

## Delivery and boundaries

For an explicitly requested TestFlight workflow, use [TestFlight preparation](references/testflight-preparation.md). Reuse signing, submission and supported-operation guidance; preparing a workflow does not authorise building, uploading, distributing or notifying testers.

For a requested App Store submission review, use [App Store review guidance](references/app-store-review-compliance.md). Establish the named app/build and current official requirements; distinguish documented concerns, missing evidence and Apple's eventual decision. No acceptance guarantee or submission authority follows from review.

For a concrete visual regression risk, reuse QA's [Snapshot-testing guidance](../qa-and-test-evidence/references/snapshot-testing.md). Control rendering conditions and require explicit baseline approval; matching pixels do not prove accessibility or interaction correctness.

For focused UI-testing guidance, reuse QA's [UI test patterns](../qa-and-test-evidence/references/ui-test-patterns.md) for identifiers, asynchronous screen states and isolation. Preserve accessibility semantics; source review alone does not prove runtime element exposure or reliable interactions.

For explicitly requested Swift Testing work, reuse QA's [Swift Testing patterns](../qa-and-test-evidence/references/swift-testing-patterns.md). Establish project support and actor requirements; do not replace XCTest merely for newer syntax.

For explicitly requested XCTest work, reuse QA's [XCTest patterns](../qa-and-test-evidence/references/xctest-patterns.md), retaining this skill's actual-toolchain, isolation and lifetime guidance. Test guidance, test creation and test execution remain separate scopes.

Implement only the authorized change or provide a scoped read-only review when requested. Reuse existing diagnostics; no automatic builds, previews, simulator/device launches, profiling, benchmarks, test creation/execution or fix/rerun loops. Explicitly requested runs remain within their scope. Never claim successful compilation, improved frame times or freedom from races without relevant evidence.

Report changed behavior, rationale, known remaining work and unverified aspects. Use existing QA guidance only when testing is explicitly requested. No unsolicited reports or broad architectural rewrites. Preserve deferred cloud synchronization and university RAG. Read references/provenance.md only for source history or maintenance.
