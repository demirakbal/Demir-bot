# Risk-based test design

Inspect applicable normal, boundary, invalid/missing/empty, duplicate/order, error and state-transition behavior. Include action-order regressions, authorization denial, user isolation, transaction rollback, partial success, retries, cancellation and concurrency when relevant.

Unit tests establish local logic. Mocked integration establishes behavior against a model, not the actual dependency. Real integration covers affected mappings, constraints, permissions, transactions, migrations and contracts. E2E covers selected whole workflows. Acceptance evaluates criteria for specified actors; usability observations and formal approval are separate.

Use arrange/act/assert/cleanup, descriptive names, controlled clocks/seeds, stable fixtures and explicit expected values. Clear tests may repeat setup. Avoid broad mocking that removes the behavior being tested. Test public contracts or extract meaningful units rather than making private APIs public solely for tests.

Browser tests: use semantic locators and observable readiness/assertions. Do not universally wait for networkidle or add fixed sleeps. Inspect rendered state when necessary; close resources. Screenshot existence alone is not a successful functional or accessibility check.

Exports: inspect real filenames, bytes, format and meaningful content (CSV rows, XLSX sheets/cells, ZIP members, image dimensions/content). Download callback mocks establish invocation only. Persistence: real write/read and transaction behavior need a controlled real dependency test, not only mocked return values.

Performance requires agreed thresholds, workload, environment and measured results. Security needs applicable negative paths and scoped scans; never claim absence of vulnerabilities. Accessibility needs applicable automated and manual checks; an automated scan alone is not complete conformance.

Property/metamorphic tests suit invariants and calculations; differential tests require a trustworthy reference. Mutation testing can assess assertion weakness when justified. Fuzz/load/fault-injection techniques are optional and risk-scaled. No fixed 70/20/10 test ratio or universal 80/100% coverage threshold. Respect actual project gates.
