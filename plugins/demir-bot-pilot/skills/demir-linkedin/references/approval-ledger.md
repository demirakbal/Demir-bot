# Approval and delivery ledger guidance

Read only for persistent publishing queues, multiple workers, stale approvals or uncertain delivery outcomes. Current one-post-at-a-time approval does not require a database. This guidance sends nothing. The separately installed local text-post runtime is described in publishing-runtime.md; read it when using the queue.

Bind approval to immutable final text, attachments/media, destination/account, action and schedule. Preserve exactly what the user approved; hash/version can detect changes but cannot authenticate the approver. Material change invalidates approval. No timers, unanswered questions, inferred consent or general growth goals grant approval.

When implementing a durable publisher later within an explicit request, record draft/version, approved snapshot, authenticated decision, destination and operation ID. Atomically reserve one dispatch attempt and revalidate the approved payload before transport. Store provider receipt/identifier only after supported evidence. Do not append internal metadata to approved public text.

Timeout or missing receipt means unknown, not failed. Hold uncertain attempts; inspect authorized provider evidence before any retry and use supported idempotency semantics where available. Deduplicating local receipts does not guarantee exactly-once external delivery. An in-flight action cannot be assumed recalled; cancellation/revocation requires provider evidence. Keep internal approval metadata private and retention/access scoped.

Source: https://github.com/affaan-m/ECC/blob/main/skills/operator-approval-loop/SKILL.md (reviewed 2026-09-21). Borrowed immutable approval binding, exclusive dispatch and uncertain-outcome handling. Omitted SQL/Python runtime, mandatory contract baseline, automatic internal notices and time-based auto-approval. No implementation tests run.

Reviewed source SHA-256: 6f79952c1498c2748ea13d74ca665c7508ae72068e014e848dee0754e3d650e5
