# On-demand local status dashboard

Use for an explicitly requested read-only view of the local plugin catalogue and approved provider-evidence summaries. It is optional tooling, not a service, discovery probe or permission engine. The stdlib-only implementation is `tools/status_dashboard.py` relative to this skill. Running it is an explicit program operation; authoring/installing the file does not launch it.

## Inputs and operation

For a separately requested monitoring workflow, use [item 064's maintenance contract](capability-maintenance.md#bounded-maintenance-and-monitoring--item-064). This dashboard only renders a snapshot; scheduling, baseline comparison, notifications, repair permissions and disable controls belong to that contract and a real supported host runtime.

Pass `--plugin-root` as the actual approved plugin source or installed package. The tool reads its portable manifest and the immediate regular `skills/*/SKILL.md` paths only. It displays definition names/version/count, not profile contents or source paths. It makes no network request and reads no account/configuration/environment secrets. Skill entries and manifests using symlinks are excluded/rejected; the selected root itself is resolved to its actual location.

Optional `--evidence` is a bounded regular JSON file containing only approved non-private summaries. Schema: one `providers` array; each entry has exactly `name`, `installed`, `available`, `authenticated`, `operation`, `approval`, `observed_at`. Names are short service identifiers, never people/email/token values. Installation/access states are `unknown`, `yes`, `no`; operation is `unknown`, `unverified`, `observed`, `failed`; approval is `unknown`, `not-required`, `pending`, `recorded`, `expired`. Timestamps require a timezone or null. Duplicate names, unsupported fields/states, oversize input and materially future timestamps are rejected without printing raw data. The caller must approve the summary's content; label validation is not a universal secret classifier.

Without supplied evidence, access/approval remain unknown. `--stale-days` controls an explicit display window (default 30); recent recording is not fresh authentication or current action authority. Stale facts stay visibly stale. The output is standalone HTML on stdout with no remote assets, scripts, forms, active controls or action tokens. Open/save it only to the user's requested private destination; do not publish it by implication. A dashboard status cannot authorize an operation.

An explicitly requested run can use Python 3 with this script, `--plugin-root` and optionally the approved evidence file; redirect stdout to the user's chosen HTML output. No dependencies, browser launch, account connection, index, watcher or package install is required. Input errors return exit 2; success returns 0. Stop at failure and correct the named input boundary rather than broadening source access or retrying indefinitely.

Expected example, not an observed run: a source-only snapshot lists the included skills and displays provider access as unknown. Supplied old Gmail evidence stays stale and does not become permission to send mail. No-action case: an ordinary email draft does not render or refresh the dashboard. Source saved; execution and visual behavior remain unverified until a scoped run/review is authorized.
