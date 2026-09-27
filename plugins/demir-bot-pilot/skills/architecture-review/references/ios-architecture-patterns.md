# iOS architecture patterns

Original guidance for roadmap item 003. Apply the existing architecture-review workflow to one relevant iOS flow. Reuse the [SwiftUI specialist](../../swiftui-performance-and-concurrency/SKILL.md) for state wrappers, identity, isolation and task lifetime, and its [project navigation reference](../../swiftui-performance-and-concurrency/references/ios-project-structure.md) when target or package ownership is unclear. Do not duplicate those workflows or introduce another coordinator.

## Trigger and required evidence

Use for an explicit iOS architecture decision or a source-backed problem involving competing state owners, feature coupling, persistence/network boundaries or module responsibilities. Start with the requested user behavior, relevant source, deployment/toolchain settings and existing conventions. Record only requirements that matter to the decision, such as offline editing, multiple windows, shared app/extension data or independent feature changes. Do not assume those requirements exist.

Without a named app and accessible source, reusable instruction maintenance can proceed, but an app-specific recommendation remains provisional. State missing evidence rather than inventing a repository, tool version or runtime defect. Skip architecture expansion when a local fix within the existing design addresses the problem.

## Trace state and data ownership

For failure contracts across these boundaries, reuse [iOS error handling](../../swiftui-performance-and-concurrency/references/ios-error-handling.md), including cancellation, uncertain mutation outcomes and recovery ownership.

Follow one actual interaction from the view through state changes and any service/storage boundary back to the displayed result. Retain source locators and distinguish observed declarations from inferred behavior.

- Separate temporary presentation state, editable drafts, shared feature/session state and persisted records. Identify each source of truth, permitted writers, lifetime and sharing scope. A draft can intentionally differ from stored data: make save, cancel and conflict behavior explicit rather than treating every copy as erroneous duplication.
- Identify where business rules are enforced and where network/storage representations become app-facing values. Add conversion layers only where formats, invariants or change pressure justify them; do not require a duplicate model for every layer.
- Trace reads, mutations, failures, cancellation and refresh. Clarify whether the UI displays confirmed or optimistic state and what happens on failure. Reuse SwiftUI guidance for actor boundaries and stale results; a view model, repository or module name alone provides no concurrency protection.
- Locate service construction and ownership. Match lifetime to the actual view, feature, scene or application requirement, preserve existing injection conventions and avoid accidental global mutable state. Shared storage across targets does not establish shared in-memory ownership or safe concurrent writes.
- Keep client validation separate from server authorization. If the affected flow handles sensitive data, reuse privacy-review for its concrete storage, logging or disclosure question without importing private records into the skill package.

## Choose the smallest adequate pattern

Compare retaining the current design with a narrow improvement before a larger restructuring. Use these as decision aids, not a mandatory layering scheme:

| Actual pressure | Candidate response | Cost or limit to consider |
|---|---|---|
| Simple local interaction with clear ownership | Retain view-local state and existing services | Extract only when responsibilities or lifetime become unclear. |
| Presentation logic is substantial or repeated | A feature model/view model with explicit inputs and state | Avoid duplicating the source of truth or creating a model for every view. |
| Several events must preserve explicit transition rules | A reducer or another explicit state-transition design | Weigh event/effect plumbing and migration cost; do not install a framework by default. |
| Repeated business rules span user flows | A focused domain operation or service | Do not add a pass-through use-case layer with no distinct responsibility. |
| Data-source coordination or persistence details leak across features | A repository or adapter at that boundary | Define consistency and failure behavior; abstraction alone does not solve synchronisation. |
| Features change independently or need actual reuse | A logical module, then a separate target/package if justified | Consider dependency direction, public API size, resources, configuration and integration cost. |

Existing MVVM, MVC, reducer-based or other conventions are evidence to understand, not automatic defects. Explain why the selected option meets the named requirement. Do not mandate Clean Architecture, a third-party framework, protocols for every type or a package per screen.

## Dependency injection and service lifetime

Roadmap item 004 extends this reference. Use when a requested change involves service construction, replacement, accidental recreation or sharing across features. Reuse the ownership trace above and the project's existing injection conventions; do not introduce a dependency-injection framework or global container by default.

1. **Find construction and consumers.** Trace the actual creation site, callers, retained references and teardown path for the affected service. Identify hidden singleton access, default arguments or factories that create another live service. A parameter named service is not evidence that all consumers use the injected instance.
2. **Choose the owner and scope.** State whether the dependency belongs to one operation, feature, scene, signed-in session or application, based on required sharing and lifetime. Construct it at the nearest stable boundary that owns that scope and pass it to consumers. Do not create owned services repeatedly during view reconstruction; use the existing SwiftUI lifetime guidance rather than prescribing one property wrapper for every deployment target. App-wide sharing must be justified, especially for account-specific data.
3. **Use a proportionate injection mechanism.** Prefer explicit initializer parameters for required dependencies where consistent with the project. A closure may suffice for one replaceable operation; a narrow protocol can describe multiple required behaviors when substitution is useful. Keep concrete types when an abstraction adds no value. Preserve an existing environment-based approach for appropriate descendants, but make required provision and ownership explicit. Do not silently fall back to a production service when a required dependency is missing. A factory is useful for intentionally fresh, scoped instances; define who owns each result and its cleanup.
4. **Separate wiring from work.** Keep network requests, subscriptions and other ongoing effects out of incidental dependency construction. Identify the deliberate start/stop boundary. Dependency injection does not change actor isolation or make a service safe to share across tasks; apply the existing concurrency guidance to the actual compiler settings and types.
5. **Define replacement behavior.** For logout, account changes or another requested runtime replacement, identify consumers retaining the old instance, work still in flight and state/cache tied to the old scope. Follow the existing cancellation and stale-result guidance before accepting results into the new scope. Merely passing a new dependency does not prove that an already-owned model adopted it. Decide explicitly whether to recreate the owner or support replacement; preserve unrelated drafts/navigation unless a reset is required. Do not delete persistent data or change accounts as part of guidance review.
6. **Keep substitution bounded.** When a caller supplies an alternative implementation, preserve the contract for results, errors, cancellation and isolation. Where preview/test support is explicitly requested, keep substitutes local to that scope and avoid accidental live network, storage or credential access. Describing a replacement boundary does not authorise writing fixtures, checks or running previews/tests.

For the affected dependency, a short conversational record is sufficient: `creation site -> owner/lifetime -> injection point -> consumers -> replacement/cleanup`, with source locators and unknowns. Do not create a separate inventory or redesign unrelated services. App-specific changes require actual project source/settings; missing access does not block saving reusable guidance but does block claims about an app's wiring or behavior.

Acceptance examples — illustrative, not executed checks:

- **Trigger:** supplied source creates a session-specific data service separately in two screens that must share the same session. **Expected action:** identify the session owner, reuse its service through the existing injection mechanism, and account for retained consumers and pending work when that session ends. Do not convert the service to an application-wide singleton merely to share it.
- **No-action case:** the existing owner creates a service once for the required lifetime and passes it explicitly to consumers. Retain that design; do not add a protocol, container or framework solely to satisfy a pattern name.
- **Missing evidence:** construction or lifecycle code is unavailable. Name the missing files or settings and keep the lifetime/replacement recommendation provisional; do not claim it compiles or cleans up correctly.

## Modularity and delivery

For a performance-driven iOS boundary decision, reuse [Apple performance evidence](../../swiftui-performance-and-concurrency/references/apple-performance-analysis.md). Tie restructuring to the affected workload and distinguish source hypotheses from measured bottlenecks.

For CloudKit data ownership and synchronisation boundaries, reuse [CloudKit sync](../../swiftui-performance-and-concurrency/references/cloudkit-sync.md), preserving the actual persistence mechanism and separating local durability from remote convergence.

For SwiftData schema evolution, reuse [SwiftData migrations](../../swiftui-performance-and-concurrency/references/swiftdata-migrations.md) for version history, upgrade paths and recovery assumptions. Keep architecture decisions tied to existing persistence ownership; do not open or migrate stores during source review.

For Core Data-to-SwiftData adoption, reuse its [transition guidance](../../swiftui-performance-and-concurrency/references/swiftdata-migrations.md#core-data-to-swiftdata-transitions) to compare retaining Core Data, compatible coexistence and an explicit store transition. Do not treat switching frameworks as proof of storage compatibility.

Inspect actual imports and call sites before claiming a cycle or boundary violation. Give each proposed module a cohesive responsibility, owned data and a minimal interface. Keep implementation details internal where possible; avoid a growing shared module that reconnects otherwise independent features. A folder split is organisational, not evidence of compiler-enforced isolation.

For an authorised change, prefer one reversible slice. Preserve externally visible behavior, stored-data compatibility, navigation identity and lifetime unless their change is requested. Name migration dependencies without executing migrations or broadening into a rewrite. Return the requirement, source evidence, chosen option, trade-off, affected boundary and remaining uncertainty. Create an ADR or separate report only when requested.

## Acceptance examples — illustrative, not executed checks

- **Trigger:** source shows two screens independently owning edits to the same record, and the user requires consistent save/cancel behavior. **Expected action:** identify draft versus persisted ownership, trace both save paths, and compare a shared owner or explicit commit boundary with the current design. Recommend the smallest supported change without selecting a framework merely by preference.
- **No-action case:** a local view owns a temporary toggle with no demonstrated sharing or lifetime problem. Keep the existing architecture; do not introduce a repository, reducer or package.
- **Missing evidence:** an app is described but its source and target settings are absent. State which inputs are needed for a concrete decision; do not claim the app has a dependency cycle or that a proposed design compiles.

This is saved decision guidance, not an executed app review. No tests, checks, builds, evaluations, benchmarks, delegation, provider installation, index refreshes or background activity follow from loading it. Project behavior and effectiveness remain unverified until separately observed within authorised scope.
