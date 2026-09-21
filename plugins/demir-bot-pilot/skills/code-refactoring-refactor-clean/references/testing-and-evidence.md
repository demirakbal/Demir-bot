# Testing and evidence

| Level | Establishes | Does not establish alone |
|---|---|---|
| Unit | Local behavior with controlled inputs | Actual database/network/UI integration |
| Integration with doubles | Contracts against modeled dependencies | Real dependency behavior/configuration |
| Real integration | Affected mappings, constraints, transactions, permissions, migrations and contracts | Complete user workflow |
| System/E2E | Workflow across actual selected boundaries | Every environment, persona and requirement |
| Acceptance/usability | Observed stakeholder outcomes for tested actors | Broad approval or untested security/accessibility |

Choose levels by risk and architecture, not fixed percentages. Unit tests need not map one-to-one to requirements. Framework tests do not verify your application's integration. Mock uncontrolled third parties where appropriate and state boundaries honestly.

Use arrange/act/assert/cleanup, independent fixtures, deterministic clocks/seeds where needed, descriptive names and behavior assertions. Prefer semantic UI locators and condition-based waits. Avoid shared mutable state and sleeps. Clear tests may repeat setup. Test public behavior or extract meaningful units; do not expose internals solely for testing.

Consider equivalence classes; boundary values; invalid/missing/empty inputs; duplicates/order; transitions and action order; permission denial and cross-user isolation; retry/timeouts; cancellation; concurrency; partial failures; rollback. Property/metamorphic testing suits invariants and math; differential testing suits trustworthy old behavior. Mutation testing can investigate assertion weakness when justified. Do not require all techniques for every change.

Retain failed runs and defect/retest links. Fix flaky causes rather than hiding failures. Separate intentional bug fixes from behavior-preserving changes. If actual results contradict a required step, flag failure or an explicitly approved requirement change; never silently pass.

Report line/branch/function coverage separately with scope, denominator and exclusions. Missing imported coverage differs from measured zero. Check classification, generation/import and revision before explaining anomalies. Passing gates and 100% coverage do not establish strong assertions, all requirements, security or defect absence.

For affected exports inspect actual bytes, filenames and contents: workbook sheets/cells, ZIP members, images. Mocked download calls do not verify artifacts. Mocked databases do not verify persistence. Performance claims need thresholds, workloads and environments. Authorization needs forbidden as well as permitted paths.

Ordinary refactoring needs commands/results, covered behaviors and limitations. Formal evidence can use:

`requirement ID | test ID/name | assertion | level and mocked/real boundary | actor/persona | fixtures/preconditions | command/steps | expected | actual | status | revision/environment/date | evidence | defect/retest`

Separate test IDs from run IDs. States: planned, not implemented, not run, blocked, passed, failed, explicitly waived with reason/owner. Excluded scope is not a pass or security waiver. Keep historical runs and latest status. Reconcile total/in-scope/excluded/execution counts; check ID uniqueness. One test may cover multiple requirements only if corresponding assertions exist. A filename mapping is not proof. Distinguish requirement coverage from code coverage.

Treat uploaded results as historical reports until actual evidence is checked. Screenshots are captured states, not reproducibility. Never invent run dates, participants, approvals or evidence links. Tests reveal defects; passing does not prove their absence.
