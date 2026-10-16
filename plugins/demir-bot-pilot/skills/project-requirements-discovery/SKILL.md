---
name: project-requirements-discovery
description: Interview the user to discover and challenge requirements for a substantial product or project, then produce atomic, independently verifiable requirement bullets. Use for deep project discovery such as a university hub; not rubric extraction, homework deliverables or routine feature clarification.
---

# Project Requirements Discovery

Original project guidance for an adaptive requirements interview. Select as `demir-bot-pilot:project-requirements-discovery`. This skill owns discovering what the user actually needs for a substantial project; requirements-and-traceability owns specification quality, existing-requirement analysis and downstream traceability. A university product is a project, not automatically a coursework assignment.

## Enter the interview deliberately

Use when the user requests a project requirements interview, wants help discovering what to build, or asks for thorough elicitation before a substantial project. The coordinator or requirements-and-traceability can hand off here without spawning an agent. Preserve supplied answers and sources; do not restart intake. Project size alone does not authorize interviewing instead of executing already settled work. For an assignment/rubric or a small clarification, keep the existing specialist workflow. If both apply, preserve mandatory assignment constraints and interview only the explicitly selected open product scope.

Briefly reflect the initial idea, known goals, constraints and unknowns. Treat a requested feature as a proposed solution until its underlying need is understood. Distinguish user evidence, confirmed decisions, hypotheses and assistant suggestions. Do not presume the original idea is wrong or push a different product merely to demonstrate discovery.

## Conduct successive discovery rounds

Ask one focused question or at most three closely related questions per round; choose the next round from the actual answer. This is an extended interview, not a single clarification gate: investigate valuable uncertainties even when they do not block immediate implementation. Do not let a generic minimal-clarification default end an explicitly requested deep interview early. Avoid dumping a questionnaire or asking every possible domain question regardless of relevance.

Use [the existing question interaction contract](../clarify-and-execute/references/choices.md) for genuine bounded choices. Start with open questions when learning the user's situation; do not constrain discovery to options invented by the assistant. Use the supported question tool in the current mode and leave room for free-text answers. Wait for answers before making dependent decisions; silence or elapsed time is not agreement. Continue only independent synthesis while an answer is pending.

1. **Discover the underlying job.** Ask for a recent concrete situation, current workaround, people involved, pain, consequences and what success would look like. Ask what must be preserved and what is outside the project. Separate stakeholder wishes from evidence about other users; do not invent interviews or consensus.
2. **Challenge proposed solutions respectfully.** Probe why a feature matters, what would happen without it and which simpler alternatives could achieve the outcome. Contrast concrete scenarios and trade-offs rather than leading the user toward a favorite architecture. Include keeping the current process when useful. Explain consequences so a nontechnical user can decide; do not offload routine technical choices.
3. **Walk the journey in detail.** Follow triggers, inputs, actions, decisions and outcomes through normal use and relevant failure/recovery cases. Use [coverage and requirement bullets](references/interview-and-requirements.md) as a selective gap guide. Drill into small details where they change observable behavior, not into implementation trivia.
4. **Reflect and revise.** After a coherent topic or meaningful change, summarize what was learned, which requirements changed and what remains uncertain. Invite correction; retain valid answers. If the underlying need differs from the initial idea, explain the evidence and confirm the changed direction rather than silently replacing scope. Preserve superseded IDs and rationale in the working specification when relevant.
5. **Prioritize after understanding.** Separate essential outcomes, preferences, later scope and exclusions, with reasons. Do not trim discovery to an MVP before understanding the larger goal; once understood, identify the smallest useful end-to-end release without dropping binding constraints.

Keep a compact working requirements set and open questions in the conversation. Resume from it when interrupted; do not create a private memory store, survey database or recurring interview. Read only user-selected project material; external research or stakeholder contact requires applicable scope.

## Turn answers into verifiable requirements

Produce numbered/identified bullet requirements grouped by workflow or capability, with one independently assessable obligation per bullet. For each include the statement, source/rationale, priority, status, acceptance criterion and suitable verification method. Use the reference for the compact bullet form and one example. Link dependencies by ID rather than bundling multiple obligations. Reuse existing project IDs and do not recycle retired ones.

Every confirmed requirement must have an observable pass/fail condition. Unknown values remain clearly marked questions or proposed criteria; they are not finalized requirements. Replace vague qualities with agreed measures and conditions, without inventing thresholds. Functional requirements, quality constraints and user needs remain distinct. Keep solution details out unless the user has made them actual constraints.

Independently verifiable does not mean every requirement is a unit test: select unit, integration, system/acceptance, inspection or a defined user-task evaluation as appropriate. Writing acceptance criteria is not writing or running executable tests. No tests, builds, experiments or evaluation loops follow automatically.

## Review coverage and finish

Review the relevant journeys, alternate paths, roles, data lifecycle and quality dimensions with the user. Identify missing coverage, conflicts and assumptions; mark irrelevant areas explicitly when useful. Do not claim that every future requirement has been discovered. The baseline is ready when the selected scope has been covered, confirmed requirements are atomic and verifiable, consequential conflicts are resolved or explicitly deferred, and the user has reviewed the resulting direction and remaining gaps. Do not label a draft approved from silence.

Stop at that baseline, the user's requested draft/time boundary, or a missing answer; do not create endless rounds to chase certainty. If the user stops early, return the partial requirements and specific unanswered questions. Do not force repeat approval for decisions already made.

Deliver the requirements document inline by default; save to the project's existing specification location only when requested. Include goals/users, scope/non-goals, grouped requirement bullets, priorities, dependencies, open issues and the next decision. Refer to requirements-and-traceability only for a distinct downstream traceability/impact task, carrying the existing answers rather than restarting discovery. Architecture can assess a real feasibility gap within authorized scope; selecting a skill is not agent dispatch. A requirements interview does not authorize implementation, adoption of personal rules, publication, indexes, cloud sync or background work.
