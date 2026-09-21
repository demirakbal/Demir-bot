# External action contract

## Capability check

Discover available tools at use time. Installation, a skill file, a signed-in browser and a people-search tool are separate from authenticated publishing permission. Use the private capability record for historical account-specific evidence. Do not call name search a feed or employer-directory search.

LinkedIn documents member sharing with OAuth and `w_member_social`; this does not establish that Demir has a connected publisher. Consult current official documentation when configuring an integration. Do not collect passwords/tokens in conversation, use private endpoints or bypass denied browser/account controls. If a supported UI is used, first establish that the access and requested action are allowed. Unsupported actions stay manual.

## Exact-action approval

Prepare the complete reviewable content first. Show:
- Final text/version and action (publish, comment, reply, invite, message or edit).
- Verified account and destination/person/post/section; disambiguate names.
- Exact media, alt text, links, mentions, visibility and timing where applicable.

Ask explicitly to perform that action; use clickable choices if supported. "Looks good" about a draft, approval of a topic, skill installation, a calendar plan or general growth goals are not publishing permission. A clear affirmative to an exact publish question is sufficient; don't ask again for the same authorized action.

Any material change invalidates approval for the changed version. No auto-publish after a timer or unanswered question. An approved post does not authorize a follow-up comment, DM, connection request, repost or profile change. Batches require explicit itemized approval, never an open-ended recipient list.

## Execution and outcome

After approval and capability confirmation, perform the exact action once. Use idempotency where supported. If a timeout or ambiguous result occurs, inspect supported readback before retrying to avoid duplicate publication. If readback is unavailable, report outcome unconfirmed and stop blind retries. Report the resulting post URL/identifier and tool confirmation when available; distinguish tool-confirmed from readback-confirmed. Do not require unrelated browser tests for this transaction confirmation.

If publishing access is absent, keep the final approved text ready for manual posting and report blocked access, not failed content generation. Offer separate integration setup only if needed; don't invent access or create a scheduled/background workflow as part of skill invocation.

## Current setup evidence

Resolve the active private profile and relevant capabilities.md and publishing-access-history.md entries. Historical access denials apply to their specific routes; do not bypass them. A separate supported provider can have different permissions. Discover tools at use time; account/channel reads never prove publishing.
