---
name: architecture-review
description: Review or design software architecture using requirements, repository evidence and explicit trade-offs. Use for repository onboarding, system design, module boundaries, dependency cycles, data flow, architectural risks and significant structural decisions. Skip routine small fixes; a review does not authorize implementation.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Architecture Review

Adapted from the community architecture decision framework, not the similarly named Ontoly-dependent skill. No external graph tool, scanner or service is required. Provenance and comparison are in references/sources.md.

## Review workflow

For requested repository onboarding, use [repository onboarding](references/review-checklist.md#repository-onboarding) to map relevant entry points, conventions and ownership and trace one real source-backed flow. “Show how a request moves through this repository” is a positive trigger; a known-path small edit does not require a repository tour. Reuse context-efficiency for scoped retrieval and freshness, and requirements-and-traceability for unresolved outcome or scope questions. Do not create a second coordinator or a persistent onboarding document by default.

1. Establish the question and authorized scope. Read current requirements and relevant repository instructions, manifests, interfaces, deployment configuration, tests and existing ADRs. Search first and follow affected dependency paths; do not ingest the whole repository. Reuse supplied context and ask only materially blocking questions.
2. Build a small evidence-based current-state map: responsibilities, boundaries, dependency direction, data ownership and one or more relevant runtime flows. Separate observed implementation, documented intent, inference and proposal. Mark missing evidence; diagrams and folder names alone do not prove runtime behavior.
3. Evaluate against actual quality goals and constraints: correctness, security/privacy, reliability, changeability, performance, scalability, operability, team capability, cost and delivery needs. Load references/review-checklist.md only for dimensions relevant to this task. Distinguish logical modules, runtime processes and deployment services.
4. Tie findings to exact source locations, demonstrated or plausible failure/change scenarios, impact and confidence. Distinguish architectural problems from local style issues. Do not invent dependency graphs, coupling scores, benchmarks, scanner findings or production readiness.
5. Compare retaining the current design, a smaller improvement and larger alternatives where warranted. Explain trade-offs, complexity and operational costs, migration/compatibility, reversibility and revisit triggers. Do not choose microservices, event sourcing, CQRS, DDD or Clean Architecture merely because of project labels, team size or arbitrary line counts.
6. Return prioritized findings and a practical recommendation with validation steps and limitations. Use a compact diagram only when it clarifies a relationship. Read-only review ends with recommendations; implement only if requested or already authorized. For implementation, preserve behavior unless a functional change is authorized and verify affected contracts after changes.

## Specialist boundaries

For product discovery and MVP delivery, reuse requirements-and-traceability's [product scope contract](../requirements-and-traceability/references/requirements.md#product-discovery-and-delivery). Take its selected user outcome, constraints and acceptance criteria as inputs; assess actual technical feasibility, dependencies, implementation/data ownership, reversible slices and simpler alternatives. Return risks and missing project/tool evidence without silently changing product priorities or promising delivery dates. Requirements owns capability maps, user jobs, MVP cuts and product acceptance; architecture owns technical trade-offs. This collaboration uses existing skills, not a second coordinator or automatic delegation. A requested MVP with uncertain persistence boundaries benefits from this review; a settled small feature does not require another planning pass.

Use requirements-and-traceability for substantial requirement conflicts, documentation-and-adrs for significant decision records and document maintenance, qa-and-test-evidence for meaningful verification work, and code-refactoring-refactor-clean for justified code restructuring. Load only the specialist that adds necessary capability; do not recursively invoke Demir Bot or all specialists.

Use current official documentation for uncertain/version-sensitive technology claims. Prefer Firecrawl for general web research when available, following required specialist source rules. External graph tooling can supplement review if already available and appropriate; verify its revision/scope and inspect source evidence when needed. Never install a new architecture tool merely to run this workflow.

## Proportional output

For a narrow question answer directly with evidence and trade-offs. A broad review may use:

`finding | evidence | consequence | confidence | recommended action | verification`

Keep proposed decisions clearly proposed. Match existing ADR conventions, preserve history and avoid drafting ADRs for every component. Do not alter external services, publish diagrams containing private data or change permissions from a review request alone.
