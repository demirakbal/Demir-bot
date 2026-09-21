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

## Migrations and data integrity

Inspect migration order, old/new application compatibility, locks, long-running changes, backfills and concurrency with live writes. Prefer staged expand/migrate/contract changes when appropriate to the actual database. Address retries, duplicate/out-of-order events and idempotency for consequential writes, payments, jobs and webhooks where relevant.

Separate application rollback, schema rollback, data restoration and forward repair. A migration status command or marking a migration rolled back does not undo schema changes or recover data. Do not run destructive migrations, restores or production backfills without explicit applicable scope and a concrete recovery plan. Note backup age, coverage, access and restore evidence; a configured backup is not a proven restore. Discuss recovery-point/time requirements when they affect the decision, without inventing targets or measurements.

## Health signals and observability

Distinguish startup (initialization), liveness (process needs restart) and readiness (can serve intended work). Design bounded, inexpensive checks for the platform; avoid turning a transient dependency outage into an uncontrolled restart cascade. A basic successful health response does not prove authentication, data correctness or the end-to-end user journey. Restrict detailed dependency diagnostics and never leak credentials or sensitive topology publicly.

Select signals for actual critical paths: errors, latency distributions, traffic, saturation, job queue age/failures, dependency failures and domain outcomes where relevant. Associate evidence with release/environment and measurement window. Instrument only within the requested scope; do not invent measured latency, uptime or success rates.

Use structured logs with useful event names, severity, timestamps and safe correlation IDs. Minimize sensitive payloads, redact secrets and personal data, and apply retention/access controls. Bound metric label cardinality and logging cost. Sampling and trace propagation must fit the stack and privacy requirements; do not add a paid provider by default.

Alerts should have an actionable symptom, meaningful threshold/window, owner, severity, destination and recovery behavior. Prefer user-impact signals over noisy raw events; distinguish warning information from urgent paging. Thresholds and service objectives need project evidence or explicit assumptions. Configuration does not prove alert delivery. Do not send test alerts, enable notification schedules or contact recipients without authorization.

## Rollback and recovery

Identify the previous usable artifact/config, version compatibility, feature-disable options, in-flight requests/jobs and irreversible external side effects. Define what stops rollout and who decides; avoid unconditional retry/rollback loops. If a command outcome is uncertain, inspect permitted evidence before retrying a consequential action.

For an incident, preserve relevant evidence, establish impact and affected versions, and choose the least disruptive authorized mitigation. Recovery should include data reconciliation, safe resumption and evidence of restored critical behavior when verification is requested. If execution is not authorized, provide concrete options and mark recovery unverified. Do not create runbooks, incident reports or other documents unless requested; use existing instructions and concise conversational guidance.

## Completion

Lead with the result and practical implications. State inspected evidence, concrete blockers, known remaining work, assumptions and unverified behavior; separate required next steps from optional hardening. Scope security/privacy reviews through existing specialists rather than launching a full audit. No automatic tests, browser checks, build/fix loops, deployment, recurring monitoring or external scanners. Preserve deferred cloud synchronization. Read references/provenance.md only for source history or maintenance.
