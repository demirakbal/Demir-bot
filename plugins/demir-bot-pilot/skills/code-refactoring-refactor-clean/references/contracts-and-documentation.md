# Contracts and documentation

Trace important changes through requirement/story → component/interface → code → assertion → run evidence. Detect duplicate/orphaned IDs and conflicting criteria. Update affected links proportionately, not a whole new matrix for tiny edits.

Preserve validation, missing versus malformed data, ordering/multiplicity, errors, stable identity versus display numbering, permissions, state lifetime, persistence and batch atomicity. Resolve contradictory specifications using current authoritative requirements and stakeholder intent, not implementation convenience. Historical changelogs may reflect legitimate evolution.

Review responsibilities, abstraction, dependency direction/cycles, public contracts, invariants and shared state. Apply SOLID/patterns to actual problems. Repetition does not automatically mean static methods. Inheritance requires substitutability; singletons do not automatically improve testability. Do not force MVC/BCE/microservices or a particular database.

Update affected API/setup/examples/glossary/diagrams/test instructions. Explain intent and constraints; remove stale comments. Separate current architecture from proposals. Diagrams need scope/title, element roles/types, legend and labeled directional relationships. Pick context/module/runtime/deployment views for the question; course four views are not C4 levels. Technology detail depends on abstraction.

Use lightweight ADRs for significant decisions: context, alternatives, decision, trade-offs, consequences, status. Match docs to reader needs: tutorial, how-to, reference or explanation. Keep one authoritative statement and link instead of duplicating.

Full elicitation, architecture or documentation projects should use dedicated relevant workflows if available. Verification concerns specified requirements; validation concerns stakeholder needs. Traceability supports both but is not a gray-box test itself.

## Error, type and recovery contracts

Apply only to the requested review or a concrete risk in the changed path. Reuse the ECC silent-failure and type-design perspectives recorded in [targeted-review-provenance.md](targeted-review-provenance.md); they are questions for the current reviewer, not a requirement to spawn agents or import upstream machinery. Read relevant declarations, construction/mutation paths, callers and external adapters before concluding that a pattern is defective. No target implementation was supplied by this guidance; actual findings require actual project evidence.

### Follow failures to their consumers

Trace a plausible failure from its origin through catches, result conversion, asynchronous completion and the caller's visible outcome. Inspect whether an empty collection, default value, success flag or stale cached result hides failure. Distinguish an intentional documented fallback, partial result, optional absence and cancellation from a failed operation. Logging alone does not establish that a caller receives the failure; conversely, an error propagated to an appropriate owner need not be logged at every layer.

Preserve actionable cause and operation context through error translation without exposing secrets, private payloads or internal details to unauthorized callers. Check whether fire-and-forget work, dropped results or cleanup exceptions lose the decisive error. Identify the actual consequence, such as a UI claiming a save completed when persistence failed. Do not flag every catch, fallback or optional as a bug without examining the contract.

### Distinguish absence, invalid input and domain states

Establish the language, declared types and actual boundary inputs. Distinguish missing, null, empty, zero and false where the domain treats them differently; a valid-zero fix must not silently accept or reject unrelated inputs. Examine optional fields, defaulting, coercion, narrowing, casts and assertions at serialization and API boundaries. Static annotations or a cast alone do not validate untrusted runtime data. Do not demand runtime validation of every already-trusted internal value without a concrete boundary risk.

Identify the invariant, where values are constructed and every relevant mutation path. Look for contradictory flags, partial initialization, invalid combinations and transitions that discard required state. Consider a small tagged state/result type or validated constructor when it prevents a demonstrated invalid state; preserve legitimate absence, compatibility and serialization behavior. Do not ban nullable types, add wrappers everywhere, invent quality scores or claim the type system prevents states reachable through unchecked input or mutation.

For example, a completed operation requiring a persisted identifier must not be represented as completed merely because a request was queued. Pending, completed, failed and outcome-unknown may need distinct handling if the real interface exposes those states. This is a contract illustration, not an executed case or a mandate to impose one state model on every project.

### Inspect boundaries and recovery together

Identify who validates input, owns state, authorizes the operation and translates errors at each relevant module/process/provider boundary. Inspect actual schema/version, units, identifiers, allowed transitions and partial-versus-atomic batch behavior. Type-correct data can still violate authorization or business rules. Use architecture-review only when ownership, transactions or cross-component dependencies require a separate architectural decision; local review stays here, and missing requirements return to requirements-and-traceability.

Classify recovery from evidence: retryable transient failure, permanent invalid request, denied operation, cancellation, partial completion or uncertain outcome. Do not prescribe universal retry counts or retry every exception. Before retrying a side effect, establish whether it may already have completed and whether supported idempotency or status reconciliation exists. A timeout is not proof that nothing happened; cancellation is not proof of rollback. Preserve the original failure, completed portions and pending cleanup when reporting partial work. Compensation or rollback requires its own real contract and authorization, not an assumed undo capability.

A safe source-level recommendation may be to preserve an error result, distinguish unknown completion, narrow a type or move validation to the actual trust boundary. Review alone does not authorize editing code, replaying requests, deleting data, changing accounts or probing a live service. Do not turn a missing provider or schema into an invented finding; report the specific gap and limit the conclusion.

### Evidence and completion

Report only supported findings: source location, triggering input/state, current path, expected contract and its source, practical impact, confidence/unknowns and the smallest useful correction. Distinguish demonstrated source behavior, plausible risk and observed runtime failure. If evidence is insufficient, state the unresolved question instead of declaring a defect or asserting no problems exist.

Observable acceptance for this guidance is a targeted explanation of how failure or invalid state reaches a real consumer and how the proposed correction preserves valid inputs and recovery semantics. Describe relevant acceptance scenarios in prose only where useful; do not write checks, fixtures or tests, run analyzers/builds, launch evaluations or delegate without explicit scoped authorization. Existing checks and supplied logs may be inspected as evidence but must not be presented as newly executed. Stop when the requested path and material boundaries are covered; retain unexamined areas and runtime behavior as unverified.
