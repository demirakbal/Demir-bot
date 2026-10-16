# Opt-in check tiers and skip policy

Use for an explicitly requested check strategy or release-gate decision. Reuse the actual project's configured checks and requirements. Tier names describe work scope; they never authorize execution or override Demir's separate write/run/fix permissions. Do not install on-save hooks, pre-commit hooks, CI triggers or an automatic test loop.

| Tier | Select only relevant evidence | Boundary |
|---|---|---|
| Cheap/local | Focused pure logic or structural checks for the changed contract, using existing deterministic fixtures | No network, real credentials or broad environment mutation; source inspection alone is not a passed check. |
| Boundary/integration | The selected real interface/persistence/export or client/provider boundary with isolated data | Name the actual environment and side effects, setup/cleanup owner, allowed resources and expected failure/recovery behavior. |
| Release | Named candidate against required installation, upgrade, privacy, licensing, critical-flow and recovery gates | Candidate/environment-specific evidence; no public release or production operation follows merely from passing. |

Choose checks from the changed behavior and plausible regression, not a quota or desired coverage percentage. Reuse earlier valid evidence only if its artifact/configuration/dependency and relevant assumptions still match. A small harmless prose edit may need source readback only; do not run unrelated tests to fill a tier. Conversely, a critical boundary change cannot be called ready because cheap checks alone passed.

For each applicable gate, record required/optional, source of requirement, planned scope, written/not-run/passed/failed/blocked/skipped state, actual evidence/version and owner. A skipped gate names the reason and consequence: not applicable, explicitly deferred, unavailable environment or outside execution authority. “Not run” is not a pass or a waiver. Preserve mandatory gates; missing permission leaves readiness unconfirmed rather than silently disabling them. User-approved risk acceptance must identify the actual scope; do not infer it from silence.

Acceptance example: for this source-only batch, requested check code is written and labeled NOT RUN; installation/runtime release gates remain unmet. No-action case: reading a roadmap does not execute a cheap tier. A later bounded run request selects exact checks/environment; it does not grant automatic repair/rerun or broader test tiers. This item saves the strategy only; no test, build, linter, scanner, hook or CI workflow ran or was enabled.
