# Bounded agent/runtime diagnosis

Use for a supplied assistant failure or an explicitly requested runtime investigation. Record the intended outcome, actual symptom, host/version, relevant source/configuration and supplied sanitized trace. Identify which layer the evidence supports; a changed answer is not by itself proof of a model regression or stale cache. Review source and existing evidence first; reproductions, model calls, scanners and tests remain separate scopes.

| Suspected layer | Evidence to inspect | Contained next step |
|---|---|---|
| Instruction/route | Active owner, actual trigger/exclusions, loaded passage if observed | Correct the implicated rule or route only when edits are authorized; preserve unrelated guidance. |
| Source/cache/index | Canonical source versus selected installed copy, revision/hash and available index record | Name which copy is stale; use supported scoped refresh only with its authority. |
| Retrieval/context | Actual selected record, provenance/date, truncation or missing critical constraint | Reuse the canonical minimal passage; do not rescan all private memory. |
| Tool contract/access | Exposed schema, actual arguments, sanitized error and operation permissions | Fix a concrete schema mismatch or report unavailable/denied access; do not obtain credentials implicitly. |
| Dispatch/model | Actual runtime call site, model choice and observed call/usage metadata | Identify hidden extra calls only when source/trace exposes them; do not infer token costs or unseen thinking. |
| Retry/transport | Logical operation ID, attempts, status/error boundary, raw-versus-filtered output where supplied | Preserve partial/uncertain outcomes and reconcile before a consequential retry. |
| Host/platform | Supported feature/configuration and a specific documented limitation | Report the supported alternative without pretending an instruction can enable an unavailable mode. |

Follow the failing operation through its actual call chain. Distinguish the earliest evidenced failure from downstream symptoms and unsupported hypotheses. Inspect retry ownership across layers so a wrapper and provider do not multiply attempts. Local cancellation and transport timeout do not prove remote cancellation. Preserve unknown completion where necessary; apply the shared action-receipt contract to consequential operations.

For filtered output, inspect the existing unfiltered result only when needed and permitted; do not repeat a mutation to recover a log. Redact secrets/private payloads before sharing diagnostics, and avoid uploading repository traces to another provider without scope. Missing telemetry means unobserved, not zero calls or zero errors. Source configuration cannot prove effective host behavior or discovery.

Acceptance example: a saved specialist is absent from an active catalogue; identify source, installed version and session discovery separately before proposing a scoped refresh/new-session step. No-action case: a successful simple answer does not trigger agent diagnostics or a global environment scan. Return the finding, supporting locator, uncertainty and smallest authorized recovery. No global interception, new agent, automatic retry service, background monitor or evaluation campaign is introduced.
