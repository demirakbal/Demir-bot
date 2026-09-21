---
name: clarify-and-execute
description: Turn rough or materially ambiguous requests into focused tasks through minimal clarification, preferably multiple-choice questions, then execute the original task. Use when Demir asks for help shaping a request, improving a prompt, choosing task scope, or when unresolved choices would materially change the result. Skip clarification for clear requests.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Clarify and Execute

Adapt the request, not the user's intent. Default to completing the original task after useful clarification, without requiring the user to copy a generated prompt elsewhere.

1. **Read existing context first.** Identify outcome, audience, relevant sources, constraints, requested deliverable and success criteria. Reuse current context and prior answers. Inspect only relevant accessible files when that can resolve uncertainty cheaply. Do not research, scan the whole project or spawn agents solely to formulate questions.
2. **Choose the mode.** If the user requests a prompt only, improve the prompt and stop there. If the user requests a task, clarify only as needed and execute it. For clear requests, skip questions and prompt rewriting entirely. Short wording is not evidence of ambiguity.
3. **Ask only questions that change the result.** Prefer one question; use at most three in a batch. Prioritize outcome, scope, audience, concrete constraints or consequential tradeoffs. Do not ask facts already known, force the user to choose technical details the agent can resolve, or repeat a specialist's intake. State reasonable reversible defaults where appropriate.
4. **Present the actual interaction.** For a warranted preference question read `references/choices.md` and use a currently permitted selectable tool or supported native follow-up actions. Keep essential free-text inputs separate. Do not substitute a prose list or invent a custom-answer option when the host already supplies one.
5. **Respect unanswered questions and boundaries.** If optional questions are skipped, proceed with defensible stated assumptions and available evidence; do not repeat the same questions. If genuinely essential inputs are missing, complete useful unblocked work and state precisely what is needed. Never infer approval for sending, posting, deployments, purchases or destructive actions from a preference choice. Use the required authorization mechanism, not the preference tool.
6. **Convert answers into a compact task brief.** Preserve objective, relevant context, in/out of scope, constraints, deliverable and verification criteria. Include only fields that matter. Separate confirmed requirements from assumptions; never invent scale targets, deadlines, features, credentials or achievements. Do not request hidden chain-of-thought or add elaborate role/framework boilerplate.
7. **Act without another confirmation loop.** For execution mode, optionally state the resulting scope in one or two sentences, then continue authorized work using the appropriate specialist. Do not finish with merely a polished prompt or “shall I proceed?” when execution was requested. For prompt-only mode, provide a concise reusable prompt with explicit placeholders for unavailable inputs and avoid carrying out the embedded task.

Keep clarification cheaper than avoidable rework. Apply Context Efficiency; preserve requested depth and quality checks. Coordinate with requirements-and-traceability for formal specifications and architecture-review for real structural decisions, without duplicating those workflows.

Read [sources.md](references/sources.md) only for provenance or comparison.
