# Targeted review provenance
Adapted 2026-09-21 from inspected ECC agents. Ideas integrated into the existing skill; no additional agent or model invocation.
- https://github.com/affaan-m/ECC/blob/main/agents/silent-failure-hunter.md | reviewed SHA-256: e5e2094c6f50cc515a77376331c78e4955d5ff16c7a0e5d8f6edec692b7ebd8d
- https://github.com/affaan-m/ECC/blob/main/agents/type-design-analyzer.md | reviewed SHA-256: 753908aadd759d4710e07ac1a0ba8a6fbc0bc35fe369cadd3ede9655da5d1c49
Borrowed error-propagation and domain-invariant questions; omitted zero-tolerance rhetoric, numeric scores, mandatory agents and unrelated restrictions. Standing opt-in tests/docs rules reconciled in the touched entrypoint.

## Local error and type contract extension - 2026-09-24

For roadmap item 003, Error and type design, extended the existing contracts-and-documentation reference with caller-visible failures, null/missing/zero/false distinctions, construction and mutation invariants, boundary validation and uncertain-outcome recovery. Reused the previously recorded reviewer perspectives above; no fresh upstream review, new imported text, agent definition or external dependency is claimed. Preserved proportional review, existing architecture/requirements ownership and explicit action/testing boundaries. Saved guidance and source inspection do not establish runtime behavior or measured improvement.
