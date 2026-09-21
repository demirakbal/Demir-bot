# Contracts and documentation

Trace important changes through requirement/story → component/interface → code → assertion → run evidence. Detect duplicate/orphaned IDs and conflicting criteria. Update affected links proportionately, not a whole new matrix for tiny edits.

Preserve validation, missing versus malformed data, ordering/multiplicity, errors, stable identity versus display numbering, permissions, state lifetime, persistence and batch atomicity. Resolve contradictory specifications using current authoritative requirements and stakeholder intent, not implementation convenience. Historical changelogs may reflect legitimate evolution.

Review responsibilities, abstraction, dependency direction/cycles, public contracts, invariants and shared state. Apply SOLID/patterns to actual problems. Repetition does not automatically mean static methods. Inheritance requires substitutability; singletons do not automatically improve testability. Do not force MVC/BCE/microservices or a particular database.

Update affected API/setup/examples/glossary/diagrams/test instructions. Explain intent and constraints; remove stale comments. Separate current architecture from proposals. Diagrams need scope/title, element roles/types, legend and labeled directional relationships. Pick context/module/runtime/deployment views for the question; course four views are not C4 levels. Technology detail depends on abstraction.

Use lightweight ADRs for significant decisions: context, alternatives, decision, trade-offs, consequences, status. Match docs to reader needs: tutorial, how-to, reference or explanation. Keep one authoritative statement and link instead of duplicating.

Full elicitation, architecture or documentation projects should use dedicated relevant workflows if available. Verification concerns specified requirements; validation concerns stakeholder needs. Traceability supports both but is not a gray-box test itself.
