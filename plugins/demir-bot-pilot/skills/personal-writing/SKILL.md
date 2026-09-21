---
name: personal-writing
description: Write or revise the user's emails, applications, messages and personal prose using shared approved facts and voice examples. Use for writing in the user's voice and maintaining explicitly approved reusable facts or samples; route LinkedIn-specific research and actions to demir-linkedin.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Personal writing

Read `references/facts-and-voice.md` only for relevant approved facts and permissions. It remains the single shared fact source, not a universal tone. Select one channel module: `demir-bot-pilot:linkedin-tone` for LinkedIn posts; `demir-bot-pilot:email-tone` for emails through Gmail or other providers. Route LinkedIn research and actions to demir-linkedin. Do not blend channel defaults or load all modules. For other prose use the requested style without claiming a calibrated tone.

Modular extension: add a future channel skill only when requested or justified by a concrete gap. Each tone owns its own examples, evidence, variants and corrections; facts remain canonical in the active private facts file, delivery permissions stay with the action workflow. Register its channel in this router and Demir Bot, and load only the selected module. Shared factual corrections do not automatically rewrite channel tones.

Resolve purpose, reader, channel and requested outcome from context; ask only material missing choices, at most three. Write the requested complete draft, preserving the user's meaning and constraints. If examples are missing, use the provisional direct, natural, concrete style without pretending it is a learned personal voice. Apply the active private channel preferences, adapting tone by post type when requested. Adapt analytical, instructional, reflective or conversational tone to the material while preserving directness, factual care and natural wording. Match the reader's formality while retaining the user's preferences. Avoid inflated credentials, invented results, commitments, anecdotes or feelings. Use explicit placeholders only where necessary and keep confirmation notes outside ready-to-send text.

Use approved examples to infer observable preferences such as sentence length, structure, vocabulary, humour and formality. Preserve the user's factual intent; do not copy private details or another person's voice into public posts. Adapt tone to the channel rather than pasting LinkedIn hooks into emails. Use a writing block where supported for finished reusable drafts.

When the user approves facts or samples for reuse, update the canonical private facts file, or private channel tone file for examples, with exact wording or an approved summary, provenance/date, permitted contexts, restrictions and status. Distinguish approval of wording, factual confirmation, reuse permission and authorization to send. Draft approval alone is not blanket reuse permission. Conflicting or time-sensitive facts require clarification; preserve restrictions and remove revoked material from future use. Do not store credentials, private third-party messages or unnecessary sensitive detail. Saving to this local reference does not establish cloud synchronization or deletion of previous conversation copies.

For LinkedIn research/profile/growth use `demir-bot-pilot:demir-linkedin` without recursive handoffs. For email delivery use an available relevant connector only after explicit authorization of the actual final message and resolved recipients/attachments. Writing a draft does not authorize sending. No automatic tests, additional reports or permanent correspondence logs. State missing approvals or access accurately.
