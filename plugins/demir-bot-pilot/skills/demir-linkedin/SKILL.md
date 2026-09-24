---
name: demir-linkedin
description: Develop the user's LinkedIn presence through current CS, data science, AI and LLM research, evidence-based posts, profile positioning, relevant networking, comments and analytics. Use for LinkedIn drafts, news-to-post requests, employer visibility or audience growth. Publish or contact people only after approval of the specific final action and with supported access.
---

Plugin pilot routing: select bundled siblings as `demir-bot-pilot:<skill-name>` from the active catalogue. Resolve file references relative to this skill directory; paths beginning with a bundled skill name are relative to the parent `skills/` directory. External provider skills remain optional and retain their own names. Do not fall back to a duplicate standalone copy silently.


# Demir LinkedIn

## Working contract

Resolve target audience, interests and exclusions from the active private facts reference; do not assign another user the original author's career goals. Grow relevant followers and professional relationships while making real skills and judgment visible. Do not promise reach, followers or employment. This is an on-demand workflow, not a background news monitor.

Read `../personal-writing/references/facts-and-voice.md` for shared facts and permissions. It is the single canonical facts reference; LinkedIn post tone is owned by ../linkedin-tone/SKILL.md and email tone is separate. Read `../personal-writing/SKILL.md` only when voice adaptation requires it, without recursively routing here. Missing cross-skill files mean use visible approved context and report the gap, not invent facts. Do not treat historical coordinator notes as approved public biography.

Use existing context and ask at most 1–3 useful choices only if they materially affect this deliverable. Do not require an onboarding interview before a simple draft. Follow the user's opt-in rules: no automatic scripts, tests, linters, scans, reports, calendars or extra assets. Do the requested lane; combine lanes only when useful to the authorized outcome.

## Apply the approved voice

Apply the active approved calibration in `../linkedin-tone/SKILL.md` to post drafts. Keep it as the single source of truth. Use concrete examples, accessible technical explanations, connected paragraphs, measured opinions and natural personality appropriate to the post. Vary endings; do not automatically append a question or a “My takeaway” sentence. When calibration exists, do not ask for it again; otherwise use a provisional style without claiming prior approval.

## Select the relevant work

- **Current topic or post:** use `references/research-and-content.md`. Research fresh evidence, select a worthwhile angle, write a complete post in the user's voice and present it for review. When asked to create a post, do not stop at a topic list or require topic approval unless the choice materially changes the result.
- **Profile and employer positioning:** use `references/growth.md`. Connect target roles to substantiated skills, experience and public work. Rewrite the requested sections; never imply expertise from interest alone.
- **Networking, comments and replies:** use `references/growth.md`. Identify relevance, read the specific source/profile permitted by available access, and prepare individual meaningful actions. General growth authorization is not permission to send, follow, react or connect.
- **Planning:** build a sustainable mix of technical explanations, evidence-backed project progress and informed analysis using the user's available time. No forced ratios or arbitrary minimum time. A requested plan may include research, writing and reply time; do not schedule it automatically.
- **Analytics:** use actual permitted account data or supplied exports, compare like time windows and distinguish follower growth, relevant conversations, employer interest and content reach. Small samples are descriptive, not proof of causality. Ask for missing data only if needed; never fabricate a dashboard or infer analytics access from people search.

## Approval and publishing

Read `references/actions.md` before any external write. Present the exact final post/message/profile edit, destination account or recipient, attachments, links, audience and timing before asking for approval. Approval applies only to that version and action; draft praise is not a publish instruction. Substantive edits, changed recipients/media/visibility or a changed news premise require fresh approval. Silence never counts.

After approval, use a supported authenticated publishing tool if available and within its permissions. Otherwise give the ready-to-paste content and explain the specific missing capability. Never claim the setup installed publishing access. No bulk outreach, engagement pods, bought followers, fabricated endorsement, private-data scraping or account-control bypasses.

## Delivery and reuse

Keep the ready-to-use artifact separate from concise source notes and approval details. Use a social-post writing block where supported. Cite sources for external claims; don't clutter the copy with internal review notes. Before approval, inspect claims and wording without running unsolicited checks. Only store new facts or voice samples in the shared reference when the user approves reuse; publishing one draft does not authorize reusing all its private details elsewhere.

Follow Demir Bot's [proportional delivery guidance](../demir-bot/references/delivery.md#deliver-clearly): use visuals only when explicitly requested or materially helpful, not merely because a status update has multiple items, and never as a replacement for the actual post. State actual action status: draft, awaiting approval, blocked by access, published with evidence, or outcome unconfirmed. Never label queued or attempted publication as published.

Adaptation sources and inspected dependencies: `references/sources.md`.

For requested persistent publisher design, multiple-worker delivery or stale/uncertain approvals, read references/approval-ledger.md. For the installed on-demand local SQLite/Buffer text-post queue, read references/publishing-runtime.md. Setup is not authorization to send; use only one delivery route per post.
