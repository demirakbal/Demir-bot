# Advanced modes with explicit containment

Use only for a named risk and selected project/target. Ordinary implementation does not start these modes. The current legacy assignment authorizes writing checks, not running tests/builds, installing runners or updating baselines.

| Mode | Required target/oracle | Containment, failure and interpretation |
| --- | --- | --- |
| Visual/snapshot regression | Named components/viewport/theme/font/data and reviewed baseline | Deterministic render inputs and explicit tolerance; inspect differences instead of blindly replacing snapshots. A pixel pass is not usability/accessibility proof. Reuse snapshot-testing.md. |
| Windows desktop E2E | Actual Windows app/runtime, selected user/error flows and stable selectors | Isolated disposable account/data, known app state, cancellation and cleanup. Local Mac source does not establish Windows execution. No broad desktop access implied. |
| Fuzzing | Bounded parser/API input model, invariant/oracle, seed and case/time/resource limits | Use synthetic inputs in an isolated target, retain minimal failing seeds, stop on limits/crashes; do not fuzz live external accounts. Invalid inputs must fail predictably without leaking raw payloads. |
| Mutation | Selected code scope, existing meaningful assertions and operator/time bound | Surviving mutants are clues, not automatic test failures. Preserve original source and distinguish equivalent/unreachable changes; do not rewrite production behavior to improve a score. |
| Load/performance | Actual workload, resource envelope and baseline/error criteria | Explicit isolated target, concurrency/ramp/duration and stop threshold; record latency distribution, throughput, saturation and errors. No production traffic or paid resource load without corresponding authority. |
| Fault injection | Named failure boundary and expected recovery/idempotency behavior | Inject only an isolated synthetic transport/storage fault. Define cancellation, cleanup, partial/uncertain state and retry bound before execution; do not break live infrastructure or treat retries as successful recovery. |

Choose the smallest mode that can resolve the actual risk; a broad advanced suite is not a prerequisite for a small edit. Record environment, revision, oracle, actual case count/seeds/limits and retained failures when a run is separately authorized. Written cases are NOT RUN until observed; no percentages or benchmark claims from fixture presence.

## Current local-tool cases

`checks/test_local_tools.py` contains synthetic checks for the new on-demand dashboard and notification ledger: unknown/stale evidence separation, invalid label corpus, extra/raw field rejection, symlink exclusion, non-actionable suppression, duplicate reservation, uncertain-result reconciliation, changed-payload identity and absence of raw message/recipient storage. They use temporary isolated files and no provider/network account. These are written negative/regression cases, not a completed fuzz, visual, load or fault-injection campaign. No runner/dependency was installed and no test was executed.

Actual project-specific advanced campaigns still require their named application, environment and oracle. For example, a future authorized notification transport-fault case can inject a timeout and assert uncertain state prevents automatic resend; it must not send a real message. No-action case: saving a skill's Markdown does not launch these checks.
