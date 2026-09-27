---
name: release-readiness-and-observability
description: Assess release readiness or implement requested deployment and observability changes using project-specific evidence, configuration, migration, rollback, health, logging, alerting and recovery guidance. Use for explicit release preparation or operational tasks; no automatic post-merge audit, tests or deployment.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Release readiness and observability

## Establish scope and authorization

Use the actual repository, release artifact/version, target environment, hosting/runtime and data stores. Read relevant manifests, deployment scripts, CI definitions, configuration schemas, migration files and existing operational evidence selectively. Do not assume Docker, Kubernetes, a cloud provider or a particular language. Reuse project conventions and available provider skills; use Supabase or Sites guidance only when the task involves them. Verify current provider commands in official documentation before proposing or executing version-sensitive operations.

A readiness question authorizes a scoped evidence review, not fixes, tests or deployment. A requested implementation authorizes the relevant changes, not starting the configured pipeline. Do not automatically run builds, tests, scanners, browser/HTTP checks, migration dry runs or deploy commands. An explicitly requested build, preview or run permits only that scope. Preserve existing mandatory release gates; missing authorization for required checks means readiness stays unverified, not that gates should be disabled. Deployment, migrations, traffic changes, alerts to real recipients and recovery actions require applicable authorization for the actual target and effect. Reuse existing clear authorization rather than asking repeatedly.

## Readiness evidence

For material findings record the affected component/release/environment, source locator, observation and date/version where available, impact, uncertainty and next action. Separate:
- Observed: source/config inspection or an actual outcome; name which. Configuration presence does not establish runtime behavior.
- Verified operation: successful execution evidence for a specific artifact and environment; do not generalize staging evidence to production.
- Assumption: inference that still needs evidence.
- Unknown/unassessed: absent evidence or scope not reviewed.
- Blocker: concrete unmet release requirement or observed risk, with consequence and dependency.
- Deferred/accepted risk: only when the user or authorized owner actually made that decision.

Use an evidence-based recommendation such as blocked by named requirements, readiness unconfirmed, or no blockers found within the inspected scope. Avoid numeric readiness scores, invented metrics, blanket production-ready claims and treating green CI as sufficient. Existing CI results may be inspected when authorized/relevant; do not trigger new runs. For an idea with no implementation, explain prerequisites rather than claiming an audit.

## Deployment prerequisites and configuration

Identify the intended artifact and source revision, required runtime/dependencies, deploy destination, access, permissions, environment separation, capacity and critical external services. Consider auth, payment, background job and AI boundaries only where present. Distinguish public/demo launch from a high-impact production rollout. An immutable artifact identifier is stronger evidence than a moving branch/tag.

Check configuration names, required values/types and startup validation behavior without printing secrets. Keep secrets out of client bundles, images, logs and sample output. Follow the project's secret-management mechanism, least-privilege access and environment separation. Do not read or upload broad private configuration merely to populate a checklist. Do not copy example container versions, resource limits, credentials or CI templates as defaults.

Choose rollout strategy based on platform support, impact and data compatibility. Rolling deployment needs compatible old/new versions; blue-green/canary strategies do not automatically make shared data or side effects reversible. Identify rollout owner, stop conditions and rollback/recovery path. Do not provision extra infrastructure, enable automatic deployment or publish merely because a strategy was described.

## Containers and reproducible environments

Roadmap item 033. Apply project-specific container guidance only when repository evidence or the user's project scope establishes actual container use. This instruction-only plugin does not require Docker or container infrastructure. Reuse the deployment/configuration and recovery guidance above/below rather than adding another environment coordinator.

For project work, identify the named repository, actual container engine/orchestration and tool versions, host/CPU architecture, relevant manifests and intended development or production environment. Follow existing stack/provider instructions and consult official version-appropriate documentation before prescribing commands. A manifest is not proof of installed tooling, daemon access, registry authentication or a running environment. Missing project/access evidence is a dependency to report, not permission to install tools, pull images or connect to accounts.

Distinguish development conveniences from production requirements. Establish whether source mounts, hot reload, debug ports, development dependencies and local overrides are intentional for the chosen target. Do not copy development privileges, host access or debug exposure into production by default. Conversely, do not force a production image/workflow onto local development without a concrete need. Preserve existing runtime-user, network and filesystem boundaries; never add privileged mode or mount a host control socket merely to resolve an access problem.

Describe reproducibility within a stated support envelope: relevant source revision, image identity, platform, dependency lockfiles, build context, configuration schema and external services. Inspect existing version pins and immutable artifact references where available. A moving image tag or unpinned download can change the result; a digest alone does not establish security, availability, cross-platform compatibility or a reproducible build. Do not invent current image versions, replace pins, resolve dependencies or claim identical outputs without evidence. Follow the project's authorised update process rather than implying pins must never change.

Keep configuration values separated by environment and follow existing secret injection mechanisms. Document required names/types and defaults without reading secret values. Do not bake credentials into images, build arguments, committed environment files, layers or logs; later deletion from a build context is not proof that earlier artifacts contain no secrets. Inspect only relevant source declarations and exclusions, never dump interpolated configuration or broad environment contents to populate a report. Do not introduce a new secret provider or copy private data into images/volumes.

For separately authorised runtime work, identify task-owned containers, networks, volumes, ports and output paths before changing state. Distinguish process startup, readiness and actual application health using the existing health guidance; do not invent startup guarantees from configuration order. Existing entrypoints may run migrations, jobs or network operations, so inspect the relevant effects before launching. Starting containers does not authorise those prohibited effects implicitly.

Plan clean teardown around ownership and persistence. Stop/remove only resources created for the authorised task when cleanup is in scope, preserving pre-existing sessions, images, caches, networks and user volumes. Volume deletion, database reset and global prune are not routine cleanup. Record retained resources and any unfinished cleanup rather than forcing deletion. Do not stop unrelated services to free a port or automatically recreate an environment after a failure. A stopped container does not imply that persistent data or external side effects were removed.

Acceptance examples (prose, not checks or fixtures): when supplied project manifests distinguish a development mount from a production image, explain the intended differences and missing compatibility evidence rather than merging them. When a requested teardown involves a shared database volume, preserve it and identify ownership/scope before a destructive action. When no container-using project is supplied, save reusable guidance only; do not add Dockerfiles, compose files, environment templates, scripts or a container requirement to this plugin.

Report saved instructions separately from inspected configuration, observed runtime operations and unverified reproducibility. This roadmap request provides no named container project, tool versions or operation-specific access; no container was built, pulled, started, inspected live or removed. No checks, fixtures, tests, builds, evaluations, benchmarks, delegation, commits/push, installation, publication, spending, account changes or private-data modification are authorised here. Keep unrelated work and coordinator routes intact, installed caches/QMD indexes unchanged, and cloud synchronization, university RAG, training and background automation inactive.

## Migrations and data integrity


Inspect migration order, old/new application compatibility, locks, long-running changes, backfills and concurrency with live writes. Prefer staged expand/migrate/contract changes when appropriate to the actual database. Address retries, duplicate/out-of-order events and idempotency for consequential writes, payments, jobs and webhooks where relevant.

Separate application rollback, schema rollback, data restoration and forward repair. A migration status command or marking a migration rolled back does not undo schema changes or recover data. Do not run destructive migrations, restores or production backfills without explicit applicable scope and a concrete recovery plan. Note backup age, coverage, access and restore evidence; a configured backup is not a proven restore. Discuss recovery-point/time requirements when they affect the decision, without inventing targets or measurements.

## Health signals and observability

Roadmap item 034 extends this existing workflow; no separate observability specialist is required. For a requested project operation, establish the named service/project, actual runtime/hosting and telemetry versions, release/environment, supplied evidence and operation-specific access. Reuse the existing hosting/provider tools and conventions before proposing another collector or dashboard. Tool installation is not proof of account access or active telemetry. Consult official version-appropriate documentation before prescribing instrumentation or provider settings; do not connect, install or enumerate private logs merely to fill an evidence gap.

For Apple-platform launch, responsiveness or memory evidence, reuse [performance evidence](../swiftui-performance-and-concurrency/references/apple-performance-analysis.md). Scope conclusions to the supplied workload, artifact and device; reading a trace does not authorise capture, benchmarks or release acceptance claims.

Distinguish startup (initialization), liveness (process needs restart) and readiness (can serve intended work). Design bounded, inexpensive checks for the platform; avoid turning a transient dependency outage into an uncontrolled restart cascade. A basic successful health response does not prove authentication, data correctness or the end-to-end user journey. Restrict detailed dependency diagnostics and never leak credentials or sensitive topology publicly.

Select signals for actual critical paths: errors, latency distributions, traffic, saturation, job queue age/failures, dependency failures and domain outcomes where relevant. Associate evidence with release/environment and measurement window. Instrument only within the requested scope; do not invent measured latency, uptime or success rates.

Use structured logs with useful event names, severity, timestamps and safe correlation IDs. Minimize sensitive payloads, redact secrets and personal data, and apply retention/access controls. Bound metric label cardinality and logging cost. Sampling and trace propagation must fit the stack and privacy requirements; do not add a paid provider by default.

Alerts should have an actionable symptom, meaningful threshold/window, owner, severity, destination and recovery behavior. Prefer user-impact signals over noisy raw events; distinguish warning information from urgent paging. Thresholds and service objectives need project evidence or explicit assumptions. Configuration does not prove alert delivery. Do not send test alerts, enable notification schedules or contact recipients without authorization.

### Event contracts, correlation and measurement limits

For each useful signal, name the operational question, responsible owner, event boundary, destination, expected fields, access policy and retention/deletion responsibility. Reuse the project's existing event schema and instrumentation. Keep stable event names and structured outcomes tied to a user-visible operation; distinguish receipt, attempted work, completion and failure. Do not invent a parallel analytics system or emit every internal step merely because it can be recorded.

Use opaque scoped request/trace/job identifiers to connect relevant failures and retries across supported boundaries; avoid using email addresses, tokens, message contents or raw user identifiers as correlation fields. Treat caller-supplied identifiers as untrusted and follow the existing propagation scheme. Correlation is evidence of a relationship, not proof of causation or exactly-once execution. A retry needs to remain distinguishable from the logical operation so repeated attempts do not inflate success counts unnoticed.

Define the start/end boundary, units, population, aggregation window and environment for a latency/error claim. Separate client-perceived latency, server processing and queued work where relevant. Note sampling, missing events, dropped telemetry and low counts; missing data is not zero errors, and a fast average does not establish a healthy tail. Do not combine incompatible windows or average reported percentiles into a claimed aggregate percentile. No threshold, performance gain or availability result is assumed from configuration alone.

### Private payloads and retention

Reuse [privacy review](../privacy-review/SKILL.md) for personal-data handling gaps. Prefer an explicit allowlist of useful metadata and redaction before emission; exclude request/response bodies, credentials, cookies, authorization headers, private free text and sensitive URL parameters unless a separately justified and authorised design requires specific fields. Review error serialization and exception messages as possible leak paths rather than assuming structured logging sanitizes them. Do not collect raw private payloads now in order to redact them later, or paste them into findings and dashboards.

Apply the same scope to logs, traces, metric labels, dashboards, exports, alert text and retained copies. Pseudonymous identifiers can still be linkable; do not claim anonymity merely because values are hashed or masked. Name who can access each destination and who owns expiry/deletion, using actual project policy. Do not invent a universal retention period. Distinguish source retention from exported/dashboard copies and confirmed deletion from configured expiry; no deletion or access change is authorised by reviewing the design.

Choose instrumentation volume and label dimensions with privacy, utility and resource cost in mind. Avoid unbounded per-user/request identifiers in metric labels. Do not widen collection, retention, sampling or external export as an automatic debugging fallback. If supplied evidence is insufficient, name the missing metadata or access without requesting raw private logs.

### Acceptance and operation boundaries

Prose examples, not executable checks: if supplied sanitized events cannot distinguish a failed attempt from completed work, propose a scoped outcome/correlation contract and name its owner; do not enable tracing or invoke the service. If a dashboard reports a latency number without a population/window, state the measurement gap rather than claiming a bottleneck. If source logging includes a private payload, identify the exact emission boundary and propose minimal metadata/redaction; do not read production logs or upload examples to a provider.

Report saved guidance separately from inspected source/supplied telemetry, observed operations and unverified behavior. No named service, tool versions, operational evidence or access is supplied by this roadmap request. Event delivery, correlation, measured latency, health, retention enforcement and redaction effectiveness remain unverified. Instruction maintenance creates no instrumentation, health check, dashboard, alert or collector. No tests, builds, checks, evaluations, benchmarks, delegation, commits/push, installation, publication, spending, account changes or private-data modification. Preserve unrelated work and coordinator routes; keep installed caches/QMD indexes unchanged and cloud synchronization, university RAG, training and background automation inactive.

## Rollback and recovery

Identify the previous usable artifact/config, version compatibility, feature-disable options, in-flight requests/jobs and irreversible external side effects. Define what stops rollout and who decides; avoid unconditional retry/rollback loops. If a command outcome is uncertain, inspect permitted evidence before retrying a consequential action.

For an incident, preserve relevant evidence, establish impact and affected versions, and choose the least disruptive authorized mitigation. Recovery should include data reconciliation, safe resumption and evidence of restored critical behavior when verification is requested. If execution is not authorized, provide concrete options and mark recovery unverified. Do not create runbooks, incident reports or other documents unless requested; use existing instructions and concise conversational guidance.

## Completion

Lead with the result and practical implications. State inspected evidence, concrete blockers, known remaining work, assumptions and unverified behavior; separate required next steps from optional hardening. Scope security/privacy reviews through existing specialists rather than launching a full audit. No automatic tests, browser checks, build/fix loops, deployment, recurring monitoring or external scanners. Preserve deferred cloud synchronization. Read references/provenance.md only for source history or maintenance.
