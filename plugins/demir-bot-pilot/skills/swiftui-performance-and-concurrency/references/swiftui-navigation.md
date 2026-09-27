# SwiftUI navigation

Original roadmap item 005 guidance. Use for requested navigation changes or an identified route, restoration or deep-link problem. Reuse the parent skill's state, identity and task-lifetime guidance and [iOS architecture patterns](../../architecture-review/references/ios-architecture-patterns.md) for ownership decisions. This reference does not introduce a router framework or a separate specialist.

## Establish compatibility and the affected flow

Inspect the relevant navigation root, destination declarations, route/state owner and supplied symptom. Use [project navigation](ios-project-structure.md) only when target or configuration ownership is unclear. Establish deployment targets, SDK/toolchain evidence and the navigation APIs actually used, including UIKit interoperability where present. Do not infer minimum OS support from the development machine or replace an existing navigation approach solely because newer APIs exist. Consult current official Apple documentation before prescribing version-sensitive APIs or availability fallbacks.

Without app source and target settings, save reusable guidance but do not invent a working route, specific migration or compilation result. Review one relevant path through entry, selection, destination and back/dismiss behavior rather than mapping every screen.

## Navigation state and routes

- Identify the source of truth for each stack, tab, split-view selection and modal presentation involved. Match ownership to the relevant feature or scene; do not accidentally share one navigation history across independent windows. A separate router object is optional, not a prerequisite.
- Follow project conventions for route values and destination registration. Prefer stable identifiers or small route values over retained view instances, live services or full mutable records. Resolve current data at the appropriate boundary and define behavior when it is missing or inaccessible.
- Keep push/pop, tab selection and modal presentation semantics distinct. Trace user-driven back navigation and dismissal as well as programmatic changes so the recorded state stays consistent with the displayed interface. Avoid multiple independent flags that can request contradictory destinations.
- Define whether a request appends, replaces, selects or returns to an existing route. Preserve drafts and navigation identity unless the requested behavior requires a reset. Do not use changing view IDs as a general cure for stale route state.
- Apply the parent skill's isolation and cancellation guidance to asynchronous route resolution. An older lookup must not overwrite a newer route request or mutate navigation after its owning scene/session has ended. Source review alone does not prove those behaviors.

## Restoration

Restore navigation only when required. Identify what should survive view recreation, scene recreation or application relaunch; these are different lifetimes. Reuse the project's existing storage and privacy conventions rather than adding persistence automatically.

Persist only a minimal, versioned representation of restorable routes and selections, where authorised. Do not serialize live objects, services, credentials or sensitive content into navigation state. Establish the intended scene and account scope without copying private identifiers into reports.

Decode and validate saved state before applying it. Check supported route versions, record existence and current access. Define a safe fallback for obsolete, corrupt, missing or inaccessible destinations: for example a supported ancestor or the app's normal starting screen. Do not claim a saved path guarantees that its destinations remain valid. Do not migrate or delete real stored data as part of a guidance review.

Define precedence when restoration competes with an explicit incoming link or a newer user action. Avoid applying a late restoration result over the user's current navigation. Describe the expected back stack and tab/modal state after restoration instead of merely saying that a screen opens.

## Incoming links

Treat URLs and external route payloads as untrusted input. Parse with supported URL components and the app's explicit route contract; validate allowed schemes/hosts, path shape, parameter types and identifiers. Reject malformed or unsupported routes without executing embedded actions. Keep sensitive query values out of logs and retained navigation state.

Separate parsing a link into a route intent from resolving data, checking access and changing navigation. A URL identifying a record does not grant permission to read it. Use existing authentication/authorization boundaries; preserve a pending intent only within the intended scope, then revalidate it before use. Do not open protected content merely because a link parsed successfully.

Specify behavior for cold and already-running entry, duplicate delivery, unresolved data, expired sessions and an unavailable destination. Choose the relevant scene/tab/stack using actual app requirements. Define safe failure and back/dismiss behavior, and prevent repeated delivery from stacking duplicate destinations or triggering repeated side effects.

App-level parsing and routing do not prove universal-link delivery. When required, identify associated-domain, entitlement, URL registration or server association dependencies from actual configuration. Missing domain access or platform delivery evidence remains explicit. Do not provision domains, change accounts, edit server configuration or launch a device merely to complete this guidance. Deeper domain-association work belongs to the separately scoped universal-links item.

## Acceptance and delivery

Illustrative acceptance examples, not executable checks:

- **Trigger:** a supplied app must open a linked record in the correct tab after sign-in. **Expected action:** inspect the route owner and existing link/auth flow; validate the intent, resolve current access, apply it once to the intended scene and define the resulting back stack. Do not assume access or live link delivery from source alone.
- **Restoration case:** a saved destination names a deleted record. **Expected action:** specify a safe fallback while preserving valid navigation where appropriate; do not restore an unusable screen or overwrite a newer user choice.
- **No-action case:** a local view edit leaves existing routes, ownership and supported APIs unchanged. Do not introduce a router, persist history or migrate the navigation system.

Report saved guidance or authorised code changes separately from source observations and unverified behavior. App-specific work needs the actual project and target settings. No tests, fixtures, builds, previews, device launches, evaluations, benchmarks, delegation, installations, index refreshes or background activity are authorised by this reference. Keep the coordinator unchanged and reuse existing architecture/privacy guidance only for a concrete question.
