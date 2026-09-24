# Requirement quality

Use only relevant fields; match existing format.

`ID | statement | source/version | rationale | priority | scope/status | acceptance criteria | open issues`

For full specs: goal and users; scope/non-goals; capabilities and dependencies when needed; functional requirements; measurable quality requirements; data/interfaces; acceptance and verification approach; assumptions/conflicts; change history. Architecture and execution plans may be separate artifacts.

Check: one independently assessable obligation; clear actor/action/condition/outcome; defined terms and units; consistent priorities; realistic feasibility; source and need; implementation-neutral unless technology is an actual constraint. A story's persona/goal/value does not replace acceptance criteria. MoSCoW is a prioritization convention, not proof every Must has shipped. Won't means out of this scope/version, not permanently forbidden or security risk accepted.

Acceptance examples can use Given/When/Then or explicit input/expected-output tables. Cover applicable normal, alternate, invalid, boundary and forbidden-role behavior. Specify missing versus malformed data, duplicates/order, immutable IDs versus display numbers, per-item versus whole-batch failure, retry/timeout and cross-user isolation when relevant.

Replace 'fast', 'secure', 'easy' and 'scalable' with observable dimensions, measurement method, workload/environment and agreed threshold. If no threshold exists, label it unknown/proposed; never assert a made-up 200ms/100%/99.9% promise. Usability criteria require actual users/tasks and success measures where appropriate, not subjective adjectives alone.

For RAG projects when requested: homework versus exam mode; course/source versions; rubric constraints; retrieval relevance and citation support; permissions, isolation, freshness and agreed cost/latency targets. These are questions, not preapproved commitments.

Course lessons: reconcile duplicate IDs, incomplete criteria, priorities, stable identity and partial-success semantics. Detailed examples are in the active private profile at course-evidence/requirements-and-traceability/references/requirements.md when relevant; never export them.

## Product discovery and delivery

Use for requested product discovery, capability mapping, MVP selection or delivery scoping. This extends the existing requirements workflow; it is not a new coordinator, project-management service or authority to implement the proposed product. Match depth to the decision. Keep the result conversational unless a document or persistent project record is requested; reuse the project's existing specification and IDs.

### Establish the user job and evidence

Identify who needs to accomplish what, in which situation, why the result matters and how they currently cope. A useful statement is “When [situation], [user] needs to [job] so that [observable outcome].” Ground it in supplied requirements, approved research or project evidence. Distinguish observed needs, stakeholder requests, assumptions and proposed solutions. Do not invent interviews, demand, user counts, willingness to pay or agreement. A feature request is evidence of a request, not proof that the proposed feature solves the underlying need.

Reuse known goals, constraints and non-goals; ask only questions that change the scope decision. Use deep-research-and-idea-validation only for a distinct research gap within the requested scope. Discovery does not authorize contacting users, collecting analytics, reading private histories or installing providers. If the target project, audience, source access or decision owner is missing, name that dependency and leave the affected decision proposed. Complete independent guidance without inventing a product or requiring a ceremonial intake.

### Map capabilities and existing coverage

Describe capabilities as outcomes the product must support, not a list of screens, tools, agents or services. Start with the user journey and include necessary failure/recovery and permission paths. Reuse actual existing capabilities before proposing additions; distinguish instruction guidance, executable implementation, accessible integration and observed operation.

Use only useful fields in the existing record:

`user job/source | capability/outcome | existing coverage and evidence | gap | dependencies | scope choice and reason | owner | acceptance/evidence gap`

Keep one canonical entry per capability; several features can contribute to it and one existing skill can cover several capabilities. Reconcile overlapping requests explicitly, preserving their distinct outcomes and constraints. A capability map is not a deployment diagram or proof of a connected provider. Do not recreate a specialist merely to match a product category.

### Choose the MVP and delivery slices

Choose the smallest end-to-end slice that delivers a useful user outcome while preserving required privacy, authorization, data integrity and recovery. Compare include-now, defer and exclude choices using evidence of user value, necessity, dependencies, risk and available capacity. Explain material cuts without fabricated numerical scores or estimates. Preserve a reason and revisit condition for deferred scope; deferral is not completion or permanent deletion.

Separate a useful first release from a prototype or learning experiment. A prototype with mocked access may answer a design question but does not establish a working integration. Never cut binding safety or acceptance requirements merely to call a smaller implementation an MVP. When capacity or feasibility is unknown, state the uncertainty; do not promise dates, staffing, costs or a viable release.

Order delivery by real prerequisites and useful increments. Bring forward only enabling work needed for the selected slice. For meaningful batches, describe the appropriate focused verification and later integration/release evidence, but do not write or run tests, checks, builds, evaluations or benchmarks without explicit scope. Writing a plan or acceptance criterion is not permission to create a check suite. Avoid automatic approval rounds or expanding a small task into a full roadmap.

### Ownership, architecture and acceptance

Separate the product decision owner, implementation owner and acceptance reviewer where those roles matter. Use actual assigned people/roles or existing project conventions; otherwise mark the owner unresolved with the decision needed. Do not assign someone work, contact them, create tracker issues or infer stakeholder approval. A skill owning guidance is not a person accepting delivery, and a proposed reviewer is not an executed review.

Pass the selected user outcome, scope/non-goals, constraints, capability gaps and acceptance criteria to architecture-review only when technical feasibility or boundaries need analysis. Architecture returns dependency/risk evidence, simpler alternatives and unresolved feasibility; requirements remains the owner of product scope. Reuse context-efficiency's existing handoff format when a handoff is useful, without spawning a worker, copying private context or adding another ledger.

For each selected slice, apply the acceptance guidance above: observable actor/action/condition/outcome, relevant alternate and forbidden behavior, evidence method and unknown thresholds. Link existing design/implementation/evidence through traceability.md. Separate proposed, agreed, implemented, observed and accepted states; an approved plan is not a delivered product. Finish with the concrete scope decision, remaining blockers, actual evidence and next authorized action.

### Illustrative acceptance, not an executed evaluation

For a supplied request to help a user organize reference links, identify the job as saving and finding an approved link. If existing storage is evidenced, a proposed first slice could save a link and retrieve it with defined invalid-input and access behavior. Defer recommendations and social sharing with stated reasons unless they are necessary to the actual requirement. If storage or the target project is unavailable, mark persistence blocked; do not imply a working product from a draft screen. Record the real owner or unresolved ownership and observable acceptance, without running examples or inventing demand. The guidance succeeds when it resolves these product choices and preserves the evidence gaps, not when it creates another coordinating layer.
