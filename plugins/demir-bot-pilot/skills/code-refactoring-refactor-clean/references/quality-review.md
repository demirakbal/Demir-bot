# Quality review

Tie findings to location, consequence, remedy and validation. Smells are hypotheses. Prioritize impact, likelihood, change frequency and cost. Explain why an abstraction pays for itself.

| Dimension | Examine and respond |
|---|---|
| Cognitive load | Nesting, branches, hidden state, misleading names, mixed abstraction; use domain names, guard clauses and cohesive extraction |
| Maintainability | Change hotspots, fragile dependencies, ownership and setup; simplify responsibilities and contracts |
| Duplication | Repeated business knowledge; unify genuine shared rules, preserve similar code with distinct reasons to change |
| Modularity | Cohesion, coupling, cycles, fan-in/out, inappropriate inheritance, feature envy, God classes; move responsibility and improve boundaries |
| Correctness | Invariants, null/missing/empty, ordering, multiplicity, numerical behavior, errors and mutation |
| Comments/docs | Stale or redundant narration versus useful intent, constraints, units, contracts and decisions |
| Reliability | Partial failures, retries, cancellation, cleanup, idempotency, concurrency and atomicity |
| Performance/scalability | Hot paths, N+1 queries, unbounded work, memory, blocking I/O and cache invalidation; profile representative workloads |
| Security/privacy | Trust boundaries, server authorization, injection, secrets, sensitive logs and dependencies; use applicable negative tests/scanners |
| UI/accessibility | Semantics, keyboard/focus, labels, loading/error/empty states, units and chart meaning |
| Operability | Configuration, actionable errors, migrations, rollback and compatibility; avoid unnecessary infrastructure |
| Test quality | Assertions, isolation, meaningful coverage, flaky timing and behavior-to-test fit |

Use configured formatter/linter/type checker/tests/coverage/security and architecture tools. Discover commands from manifests and CI. Named language-aware analyzers may calculate cognitive/cyclomatic complexity, duplication and coupling; grep cannot supply accurate metrics. If unavailable, give qualitative findings explicitly.

For before/after comparison record revisions, dirty state, tool/version, rules, source scope, exclusions and coverage imports. Separate new/resolved/unchanged/suppressed issues. Do not weaken gates to improve scores. Missing baseline means no measured improvement claim.

Use goal → question → metric with context and interpretation. LOC, maintainability index, WMC, CBO, RFC, DIT, NOC, fan-in/out and LCOM are imperfect signals with differing definitions. Cohesion and coupling need independent assessment. Never impose global 20-line functions, 200-line classes, 3 parameters, 5 dependencies, 80/100% coverage or comment percentages. Follow justified project thresholds.

An optimization replacing nested matching pairs with an ID dictionary may discard duplicates, change ordering and return type. Preserve multiplicity and pair order; grouping into lists may help when hashing/equality assumptions hold. Producing k pairs takes at least O(k), and k may be quadratic. Verify semantics before benchmarking, including memory and mutation assumptions.
