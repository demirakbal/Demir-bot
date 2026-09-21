---
name: linkedin-tone
description: Apply the user's approved linkedin tone to requested drafts and revisions, keeping channel preferences separate from shared facts and delivery authorization.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Linkedin tone

Resolve the private profile through `../demir-bot/references/profile-loading.md`, then read only `tones/linkedin.md` for this channel. Use `facts.md` only for relevant approved claims and restrictions. Existing users retain their calibration in that private file; do not copy it into a distributable skill.

If no profile is available, use the user's current examples/preferences or a clearly provisional audience-appropriate tone. Do not claim calibration, invent biographical facts or block a simple draft on onboarding. Keep LinkedIn post conventions separate from email language and signatures. Unknown signature values remain placeholders. Store authorized style corrections in the selected private tone file; factual updates belong in private facts.md. Approval of tone does not authorize sending, publishing or model training. Use the relevant action workflow for external effects.
