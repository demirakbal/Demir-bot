# Select a route only when needed

These are capability hints, not installation claims. Prefer currently available skills; inspect public candidates before importing. Never bulk-load this list.

Apply Demir Bot's testing and extra-deliverable opt-in rules to every route. Code requests do not automatically authorize tests, execution checks or documents. Do not load QA, TDD or documentation workflows merely because implementation finished. Explicitly requested deliverables remain in scope; brief conversational completion feedback is sufficient otherwise.

| Task | Select | Keep focused |
|---|---|---|
| Simple question | Direct answer; verification if required | No setup ceremony |
| Rough request with material ambiguity, task scoping or prompt improvement | `demir-bot-pilot:clarify-and-execute` | Prefer one useful multiple-choice question, at most three per batch. Reuse answers and proceed with authorized work; prompt-only requests stay prompt-only. Skip questions for clear tasks. |
| Code creation or changes | Existing repository guidance; `demir-bot-pilot:code-refactoring-refactor-clean` only for requested refactoring/audits or concrete maintainability problems | Skip a separate refactoring pass for straightforward work; execute checks only when explicitly requested |
| Unclear requirements, specifications, traceability or scope-change impact | `demir-bot-pilot:requirements-and-traceability` | Define measurable criteria and source-linked requirements; distinguish links from executed evidence; skip routine self-contained edits. Use Documentation Officer for separate document maintenance. |
| Explicitly requested documentation, ADRs or document review | `demir-bot-pilot:documentation-and-adrs` (Documentation Officer) | Preserve evidence and decision history; changed code alone does not authorize extra documents. |
| Explicitly requested QA strategy, test implementation, test execution or evidence audit | `demir-bot-pilot:qa-and-test-evidence` | Match the specific request; writing, running and fixing tests are distinct scopes. No automatic test/fix/rerun campaign. |
| Bug | Systematic debugging workflow if available, constrained by opt-in rules | Inspect code and supplied evidence; reproduction runs and executable checks require an explicit request. Report untested changes honestly. |
| Requested privacy review or concrete personal-data collection, sharing, telemetry, retention, deletion or consent decision | `demir-bot-pilot:privacy-review` | Trace the relevant data flow; add privacy gaps without duplicating vulnerability scanning. No automatic tests or reports. |
| Requested repository or change security audit | `codex-security:security-scan` or `codex-security:security-diff-scan`, according to scope | Follow actual specialist prerequisites within authorization; reuse findings when adding privacy review. |
| System architecture, module boundaries, dependencies or significant structural decisions | `demir-bot-pilot:architecture-review` | Ground findings in source evidence and requirements; compare simpler alternatives and migration costs; review alone does not authorize implementation. Skip routine local fixes. |
| Full quality audit | Code review plus available actual analyzers | Include complexity, duplication, smells, naming, documentation, modularity, security, reliability, performance and tests; mark unexamined areas |
| RAG work | Retrieval/embedding and evaluation expertise | Mandatory instructions and rubrics first; course/version filters; citations; test retrieval separately from generation |
| Substantial research, technology comparisons or project-idea validation | `demir-bot-pilot:deep-research-and-idea-validation`; Firecrawl for current public-web research | Primary evidence, corroboration, counterevidence, alternatives, feasibility and demand; distinguish facts from inference. Skip for simple factual answers; no automatic experiments or reports. |
| Legal feasibility | `demir-bot-pilot:jurisdiction-specific-legal-feasibility` with existing research/privacy skills as needed | Establish jurisdiction, activity and date; current official sources; no certification or external legal actions |
| Email, applications and personal prose | `demir-bot-pilot:personal-writing` plus `demir-bot-pilot:email-tone` for mail; shared facts reference; relevant mail connector only if needed | Reuse approved facts and samples within their permissions; drafts do not authorize sending. |
| LinkedIn posts, current CS/data science/AI news, profile positioning, networking and analytics | `demir-bot-pilot:demir-linkedin` plus relevant available research/media/account tools | Share canonical facts with `demir-bot-pilot:personal-writing`; use `demir-bot-pilot:linkedin-tone` for posts; exact-action approval before publishing or outreach; access is separate from skill installation. |
| Multi-item progress feedback, remaining-work lists, skill/capability inventories and priority roadmaps | `visualize:visualize` from Visualize, automatically | Follow the Deliver clearly rule in SKILL.md; retain statuses, limitations and next actions; simple replies stay prose and explicit format requests take precedence. |
| Other visual explanations | Visualize or appropriate chart skill | Use when it improves understanding |
| PDF/document/deck/sheet | Corresponding artifact skill | Follow required validation and persistent saving rules |
| Web UI implementation or requested frontend/accessibility review | `demir-bot-pilot:frontend-quality-and-accessibility` | Semantics, keyboard/focus, forms, responsive states and reduced motion; actual stack first; Figma/Sites only when relevant; no automatic audits or execution checks. |
| Explicit release readiness, deployment configuration, observability or recovery work | `demir-bot-pilot:release-readiness-and-observability` | Actual stack and scoped evidence; distinguish assumptions and unverified operations; no numeric readiness scores or automatic tests/deployment. |
| Website | Sites skills when applicable | Preserve access controls; connectors are separate from app integration |
| SwiftUI state, performance or concurrency tasks | `demir-bot-pilot:swiftui-performance-and-concurrency` | Actual project versions, isolation settings and state ownership first; no automatic builds, simulators, profiling, benchmarks or tests. |
| Explicit assistant/skill/hook/MCP configuration review | `demir-bot-pilot:agent-configuration-review` | Scoped read-only evidence; no automatic scanner, fixes, credentials or tests |
| Default across Demir Bot tasks | `demir-bot-pilot:context-efficiency` | Load the main instructions once when needed and reuse them; apply lightweight habits even to simple answers. Read detailed references and maintain ledgers only when useful. Refresh affected evidence, preserve failures and requested depth; measure rather than promise savings. |

For refactoring, distinguish AI judgments from scanner output. Never fabricate numerical cognitive complexity, duplicate-code percentages, maintainability indices or measured scalability. Include location, evidence, impact, confidence and fix for material findings. Comments should explain non-obvious intent and contracts, not repeat obvious code.

Avoid importing Superpowers and several other planning orchestrators for the same task without resolving overlap. RTK and QMD are optional local tools, not automatically available ChatGPT plugins. API caching requires a supported runtime and does not reduce all forms of token usage.


For ML pipelines, training/fine-tuning implementation or research into learning-based Demir Bot improvements, select `demir-bot-pilot:ml-training-specialist`. Discover the actual project stack and distinguish skill edits/retrieval from model training. No automatic runs or self-modification loop.

For YouTube summaries, lectures/tutorials, video comparisons and applying demonstrated lessons: `demir-bot-pilot:youtube-learning`; use actual transcript/visual evidence and timestamped provenance. No automatic tests, persistent lessons, video library or training.
