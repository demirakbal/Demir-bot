---
name: swiftui-performance-and-concurrency
description: Implement or review SwiftUI state, view-update performance and safe Swift concurrency for Apple-platform projects. Use for relevant SwiftUI changes, task lifecycle, isolation diagnostics or performance problems; follow actual toolchain settings and do not automatically build, profile or test.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# SwiftUI performance and concurrency

## Establish project context

Inspect relevant source, project/package manifests, xcconfig and available diagnostics before choosing a pattern. Determine deployment targets, supported Swift/Xcode versions, language mode, concurrency checking, default actor isolation and enabled upcoming features from existing evidence. Toolchain version, language mode and per-target settings are different facts; do not infer one from another. If effective settings remain unknown, state that limitation and avoid relying on a newer feature. Do not invoke build tools merely to discover settings without applicable authorization.

Preserve the actual project architecture and dependencies. No automatic Observation migration, concurrency-mode changes, library installation or repository-wide refactoring. Consult current official Apple/Swift documentation for version-sensitive syntax, isolation behavior or APIs when needed. Swift 6.2 does not by itself establish MainActor defaults or caller-isolation behavior for every target. Do not copy upstream examples without inspecting their assumptions.

Inspect the actual project repository when provided; this skill's installation does not establish project access or build settings. Apply project confidentiality restrictions from the active private profile before public reuse. Figma's SwiftUI workflow serves design translation when relevant, not concurrency or runtime-performance verification.

## State ownership and view updates

- Identify the source of truth, owner, lifetime and observation mechanism before selecting wrappers. Use local state for view-owned state and bindings for borrowed mutation; inject shared dependencies at an appropriate stable boundary.
- Use Observation/Observable models only where supported and compatible with the project. Preserve ObservableObject/StateObject/ObservedObject/EnvironmentObject patterns where appropriate; newer syntax alone is not a reason to migrate. A passed class reference is not immutable merely because no wrapper is present.
- Keep model lifetime stable across view reconstruction. Do not repeatedly create owned services or duplicate a parent's source of truth in a child. Model initialization should not start uncontrolled side effects.
- Keep body evaluation free of I/O and expensive transformation. Narrow state dependencies and split meaningful subviews when it reduces coupling or unnecessary work; do not promise that extraction prevents every update or that each body evaluation equals a full render.
- Preserve semantic identity across data refresh, insertion, reordering and navigation. Use stable unique model identifiers; avoid generating new IDs in body. Index identity only fits collections whose positional identity is intentionally stable. An explicit .id change can reset state and task lifetime; use deliberately.
- Choose List/lazy containers based on interaction, layout and collection size, not a universal performance rule. Avoid unnecessary type erasure, layout feedback cycles and costly effects on hot paths, but do not claim measured savings without evidence. Equatable-based optimizations require correct input equality and an appropriate integration mechanism; conformance alone is no blanket rendering guarantee.

## Expensive work and evidence

Use supplied profiling evidence when available. Without it, label suspected bottlenecks as hypotheses grounded in source: repeated decoding/sorting, synchronous I/O, excessive invalidation, redundant fetches or main-actor CPU work. Reduce repeated work with appropriately scoped caching/precomputation, including invalidation, memory bounds and concurrency ownership. Do not turn a cache into shared mutable unsynchronized state.

Async does not mean background execution. Task creation may inherit actor context; wrapping heavy work in Task does not inherently move it away from UI isolation. Choose an explicit, supported execution boundary and safe values for expensive processing; do not prescribe Task.detached or @concurrent universally. Avoid blocking cooperative executors with semaphores or synchronous waits on async work. Do not profile, benchmark or run Instruments without a request.

## Task lifetime and cancellation

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

Implement only the authorized change or provide a scoped read-only review when requested. Reuse existing diagnostics; no automatic builds, previews, simulator/device launches, profiling, benchmarks, test creation/execution or fix/rerun loops. Explicitly requested runs remain within their scope. Never claim successful compilation, improved frame times or freedom from races without relevant evidence.

Report changed behavior, rationale, known remaining work and unverified aspects. Use existing QA guidance only when testing is explicitly requested. No unsolicited reports or broad architectural rewrites. Preserve deferred cloud synchronization and university RAG. Read references/provenance.md only for source history or maintenance.
