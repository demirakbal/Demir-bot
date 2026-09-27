# Backend and API contracts

Original roadmap item 026 guidance. Use for a requested backend/API contract or architectural review where consumer expectations or boundary semantics are unclear. Reuse [requirements and traceability](../../requirements-and-traceability/SKILL.md) for intended behavior and the existing [review checklist](review-checklist.md) for transactions, authorization, isolation, caching and operational trade-offs. The demonstrated instruction gap is a focused consumer-to-contract handoff, not a missing general backend coordinator. Do not load every topic or create separate pagination, jobs and caching specialists by default.

## Route by actual project and gap

For project work, identify the named repository, actual language/framework/database/runtime versions, deployment context, affected source, concrete consumers and operation-specific access. Follow existing coordinator routes and relevant available stack/provider specialists first. Availability does not establish authentication, expertise in every stack or permission to act. Do not install a missing provider or infer a backend stack from the UI framework.

Use current official stack documentation for version-sensitive APIs, transaction semantics, middleware, queue guarantees and deployment behavior. No stack is supplied by this roadmap request, so no stack-specific implementation or compatibility is claimed. Inspect only the affected request/data path and relevant project conventions; do not enumerate private configuration or query production systems to fill gaps.

Reuse installed Superpowers workflows when their actual trigger applies: debugging for a supplied failure, planning for substantial authorised implementation, and testing methodology only within authorised testing scope. Superpowers is an engineering methodology, not guaranteed backend expertise or proof of stack support. Do not invoke a workflow simply to add ceremony to prose maintenance. User restrictions still prohibit tests, checks, evaluations and delegation here; do not run those steps or claim they were completed.

## Establish one concrete contract

Name the real consumer and affected operation from evidence: for example an identified mobile client call site, integration or worker. Trace request entry, validation, authorization, domain/data ownership and response or deferred completion using relevant source locators. Separate observed behavior, documented intent and proposed changes. A hypothetical example is not evidence that a consumer exists.

Keep the contract in the project's existing schema/specification or concise task notes; no new specification system is required. Capture only relevant aspects:

- Consumer outcome and compatibility: who relies on the operation, supported versions and how a proposed change affects existing callers.
- Inputs and trust boundary: required/optional values, null/omitted distinctions, limits, server-derived identity and validation/error semantics.
- Authority and ownership: actor, action, resource and tenant boundary; where access is enforced and which service owns mutation.
- Observable result: response/state transition, durable completion versus receipt, defined failures and retry behavior.
- Evidence: source/requirement links and acceptance criteria; distinguish planned validation from supplied or actually observed results.

Use concrete acceptance criteria derived from the requirement. For a real mutation, specify what the consumer observes on success, unauthorized access, invalid input and applicable retry/concurrency paths. Do not invent status codes, latency targets, pagination sizes, retention periods or approved behavior. Missing criteria remain questions or clearly marked proposals. Source review is not endpoint execution.

## Deepen only the demonstrated concern

For a requested typed connector or App Store Connect integration, also use the [typed connector operation contract](#typed-connector-operation-contract) below. It adds caller-side provider/access boundaries without duplicating server API design.

Use these prompts only when the affected contract or supplied evidence exposes the concern; they extend the existing checklist rather than prescribe infrastructure:

- Authorization and validation: distinguish authentication from server-side action/resource/tenant authorization. Check object and field access through the actual path, including background work. Validate untrusted input at the appropriate boundary; client validation and hidden UI controls do not enforce access. Avoid trusting caller-supplied ownership, blindly binding writable fields or exposing sensitive errors. Reuse available security/privacy routes for substantive security or personal-data questions, without automatically scanning.
- Pagination: establish ordering and a stable tie-breaker, cursor/offset semantics, filter consistency and behavior under concurrent insertion/deletion. Document what completeness or consistency is actually promised. Preserve authorization on every page; a cursor is not access authority. Do not introduce cursor pagination merely because it is fashionable.
- Idempotency and retries: identify the retrying consumer and side effect. If deduplication is required, define key scope, payload mismatch behavior, concurrent requests, retention and the outcome after a partial failure. Consider atomic persistence with the mutation and external side effects. Do not promise exactly-once execution from an idempotency header alone or retry non-idempotent operations indiscriminately.
- Jobs: distinguish enqueue acknowledgement from durable completion. Identify ownership, delivery/retry semantics, duplicate handling, timeout/cancellation, progress/error visibility and recovery responsibility. A failed worker can leave a completed side effect; do not add blind retries or a queue without a demonstrated need.
- Caching: define freshness, invalidation and cache-key dimensions including tenant/identity where applicable. Never share private responses across consumers through an incomplete key. Cache hits do not replace authorization. Describe failure/staleness behavior before choosing a caching layer.
- Rate limits: identify the protected resource, caller scope, applicable response/retry contract and behavior across instances. Do not invent thresholds or assume process-local counters protect a distributed deployment. Distinguish rate limiting from authorization, job backpressure and client retries.

Prefer the smaller correction within existing architecture. Do not introduce microservices, event sourcing, queues, caches or API gateways without evidence of benefit. Where a specialist already covers the concern, reuse it. Add another reference only for a demonstrated unresolved gap, and state what existing coverage lacks.

## Typed connector operation contract

Roadmap item 036. Use existing SDK/provider capabilities first, including relevant OpenAI Developers guidance when the actual integration involves OpenAI. Do not invoke an unrelated provider merely because it is available. The prerequisites are a named provider operation, its official SDK/API contract and supported access; there is no dependency on completing this item again. Defining a contract does not create access or authorise executing it.

### Define the narrow boundary

For implementation, identify the project/runtime and SDK version, exact provider/service, target resource/account context, caller and requested read/write effect. Consult current official version-appropriate SDK/API documentation before prescribing endpoints, types, authentication or permissions. Distinguish an official SDK from a community wrapper and generated schemas; do not invent an SDK or assume generated types guarantee runtime compatibility. Use available supported tools rather than installing an alternative or creating a general-purpose connector by default.

Describe one supported operation with typed inputs, required/optional/nullable distinctions, constrained resource identifiers and expected output/error states. Preserve provider error/status information while excluding credentials and private payloads. Validate untrusted boundary data according to the real contract; compile-time typing alone does not validate a remote response. Keep unsupported or newly introduced response states explicit rather than mapping them to success. Follow project conventions instead of inventing a new universal abstraction.

Name pagination behavior, limits, ordering assumptions and continuation ownership only where needed. Do not hide unbounded enumeration behind a single method or equate a partial page with complete results. Constrain continuation destinations to the expected provider boundary; do not forward authentication to arbitrary returned URLs. Route retry/idempotency design to the existing contract guidance above and the provider's actual guarantees, preserving total work limits and partial outcomes.

### Credentials, permissions and completion

Keep credentials in the existing approved secret mechanism outside the package, source, logs and fixtures. Record only non-secret metadata needed to describe authentication and minimum operation permissions. Tool installation is not authenticated access. Do not read Keychain, generate keys, log in, switch accounts, expand roles or bypass a provider boundary to complete this instruction task. Missing credentials/access is a named dependency, not permission to obtain them.

Separate reads from writes and identify downstream effects of each method. An operation with a read-like name can still incur charges or expose private data; use its actual documented behavior. Validate the exact target and authorised payload before a write. Do not expose a generic arbitrary-endpoint write method when a narrow operation suffices.

Distinguish cancellation of the local wait from cancellation of remote work. A timeout can leave a mutation or asynchronous job accepted; preserve the operation identifier and unknown outcome without blind retries. Where supported and authorised, later status evidence can distinguish pending, completed and failed work. Neither response acceptance nor a queued job proves the desired action completed. Do not invent polling, cancellation or idempotency support or start background monitoring.

### App Store Connect scope

Reuse [Xcode CLI integration](../../swiftui-performance-and-concurrency/references/xcode-cli-integration.md#verify-upload-tooling-for-the-actual-service) for current upload-tool verification and the existing release skill for release evidence. Identify the exact app/resource, intended account/team boundary and requested operation using supplied non-secret evidence. Keep metadata reads, metadata edits, build uploads, processing, TestFlight distribution, review submission and release as distinct effects. Read access does not authorise edits, and upload acceptance does not prove processing, submission or publication.

Derive the supported operation and minimum permissions from current Apple documentation and actual supported SDK/tool access. Do not assume historical altool commands, another provider's token scheme or a guessed account role fits. Preserve locale/version/resource relationships relevant to the real operation. No endpoint, credential method or permission mapping is invented by this generic guidance. Publishing and account changes remain prohibited in this roadmap scope even if a tool could perform them.

### Instruction acceptance and missing dependencies

Prose examples only: for a request to read metadata for an identified app, define a bounded typed read and its actual output/error contract; absent supported access, do not authenticate or substitute a write. For a supplied timeout after an upload, retain the uncertain remote outcome and distinguish authorised status inspection from another upload. For an API response with an unknown state, preserve it as unknown rather than reporting completion.

This roadmap request names a capability but supplies no concrete provider operation/target, SDK contract/version or supported authenticated access. Save reusable guidance now; authenticated connector implementation remains unperformed for those specific missing dependencies. Do not create speculative connector code, schemas, test suites or fixtures. Report guidance saved separately from source evidence, actual operations and unverified authentication, typing, pagination, permissions and completion behavior. The existing no-execution, no-account-change, no-publication, privacy and background-activity restrictions apply unchanged.

## Acceptance examples and no-action cases

These are prose examples, not test suites, fixtures or executable checks:

- Trigger: supplied client/server source shows a consumer retries a create request after a timeout. Expected action: trace the side effect and define the intended duplicate/concurrent-request outcome with the consumer's observable result, then assess existing idempotency boundaries. No-action case: no source or product requirement is supplied; do not invent endpoint behavior, send requests or create an idempotency service.
- Trigger: an identified client paginates a changing collection and supplied evidence shows duplicate rows. Expected action: inspect ordering and continuation semantics and define the actual consistency requirement before proposing a change. No-action case: no ordering guarantee is required or evidenced; do not impose a new pagination architecture.
- Trigger: roadmap instruction maintenance without a backend project. Expected action: save the focused contract guidance and owner links. No-action case: do not invent consumers, schemas, credentials, migrations, providers or endpoint results.

## Delivery and boundaries

Report saved guidance separately from project implementation, supplied evidence, observed operations and unverified behavior. For project delivery, name the consumer, contract change, acceptance criteria and relevant compatibility/recovery risks. Requirements owns intended outcomes; architecture owns technical trade-offs; QA owns authorised verification evidence. A documented contract does not prove authorization, concurrency safety, integration correctness or production readiness.

This request supplies no named backend project, stack versions, concrete consumer/source evidence or operation-specific access. Reusable guidance can be saved; project implementation and runtime claims cannot be invented. No test/check/fixture or executable integration is created by this work.

Preserve unrelated work and private data. No tests, builds, evaluations, benchmarks, delegation, commits/push, provider installation, publication, spending or account changes. Keep the coordinator unchanged, installed caches and QMD indexes untouched, and cloud synchronization, university RAG, training and background automation inactive.

Original synthesis from roadmap item 026 and existing architecture, requirements and coordinator methodology guidance. No backend stack, provider or runtime operation was verified by this instruction change.
