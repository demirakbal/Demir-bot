# Demir Bot — future work roadmap

Updated: 16 October 2026. This roadmap contains **future implementation, work needing verification, public-release work and explicitly deferred items only**. Completed implementation entries and historical execution logs have been removed from this planning document. Retained legacy item numbers are traceability references, not a fresh instruction to implement an entire old catalogue.

**For current features and architecture, read the [Demir Bot website](https://demir-bot-fieldnotes.demirakbal.chatgpt.site). This roadmap is only for future work.** The current-feature, architecture and 062–065 alignment is published as website version 29. Use this Markdown for current planning; publication and installation do not establish runtime behavior.

This Markdown file is the canonical future-work roadmap. Its PDF companion is an older September rendering and is not the current plan; regeneration is a separate future deliverable if requested. Work from the canonical checkout resolved through the active private profile, never an installed cache or archived roadmap.

## Baseline and execution boundaries

The latest authorized local refresh on 16 October 2026 completed successfully: `demir-bot-pilot@personal` version `0.1.1` remains enabled, and all **220 installed package files exactly match canonical source** after the latest refresh, including 063. The earlier refresh matched 219 files. The existing `demir-skills` QMD collection was refreshed after the user expanded the scope: **1 new, 9 updated and 152 unchanged documents**, with **76 chunks embedded across 10 documents**. Final status showed **162 indexed files**, 1089 vectors and no pending embeddings. QMD reported 376 orphaned embedding chunks; cleanup was not performed. Existing collection exclusions remain unchanged, including private proposals. This is indexing and installation evidence, not retrieval-quality, runtime or release acceptance.

Use the existing local personal plugin only. **Cloud sync remains deferred. Do not run tests or builds.** This revision authorizes no helper execution, browser/device checks, linting, model evaluation, worker dispatch, account change, external send, publication, commit/push or background activity. Any future execution must match the user's specific authorization; written checks remain unrun. Continue assigned eligible work with per-item elapsed-time and change summaries, without routine reconfirmation; stop at completion or a real dependency, and do not claim background continuation.

Status meanings: **next** = a future task selected in principle, not automatically executed; **needs verification** = source exists but the stated behavior is unobserved; **needs target/access/decision** = blocked on the named prerequisite; **release preparation** = must be applied to an actual candidate before public release; **deferred** = do not resume unless explicitly requested.

## Next tasks

User decision — 16 October 2026: items **062, 063, 064 and 065 are required implementation**, no longer deferred. That planning change did not activate execution. Item 065’s instruction implementation is now saved in canonical source; its installed-cache refresh is complete; indexing is complete and behavioral verification remains pending. Item 062’s bounded coordination contract is now saved in the shared execution policy and linked from native-profile guidance; no workers or background runtime were activated. Item 064’s monitoring guidance is now saved around the existing diagnostic helpers; no helpers, schedules, state stores, repairs or notifications were activated. Item 063’s selected first phase is now saved as approval-only lesson/proposal and on-demand research guidance, linked from the coordinator and research skill. It reuses existing private owners and defines readable-file memory layers with optional future indexing; the private proposal folder and configuration now exist and were inspected empty with owner-only permissions. No proposal records, database, chat imports or background learner were created. A hypothetical summary was demonstrated without saving or adoption; this is not full lifecycle or fresh-session verification. Item **067 remains deferred**, as do cloud synchronization and university RAG. Item 065 preserves the existing opt-in defaults: implementation does not authorize writing or running tests, builds, browser checks or evaluations. The user does not need to repeat “do not run tests.” After finishing implementation, recommend a scoped testing and verification step, then wait for an explicit request before executing it.

The order below is a recommended dependency order, not an instruction to start an implementation chain or activate background work.

| Recommended order | Item | Implementation scope and remaining decisions |
|---|---|---|
| 1 | **063 — Remaining operational learning scope (inactive)** | The selected lesson/proposal and on-demand research instruction workflow is saved in `learning-proposals.md`. Private persistence location, format and retention are configured. Next: verify a complete synthetic proposal lifecycle in a fresh session under explicit scope, then one selected on-demand research task. Before background activation, select the supported host, allowed sources, budgets, cadence/expiry, notification destination and enforceable stop controls. SQLite indexing is optional only if actual lookup needs justify it; no vector/graph service is required. Background observation, schedules and notifications require separate activation scope under 064 and remain inactive. All adoption stays approval-only; testing/evaluation stays opt-in. No automatic persona mutation or model training. |

Fresh-session installation/profile discovery and the website content update/publication have been completed in this conversation. Runtime behavior, rendering and agent dispatch remain unverified. Website alignment for 062–065 was published as Sites version 29 from source commit `37d4cdda0ad103e3bae8d874a9fae353c7ee5248`; publication succeeded, while rendering remains unverified.

## Verification still needed

| Work | Legacy references | Remaining evidence or prerequisite |
|---|---|---|
| Approval-only lessons and on-demand research | 063 | Source now defines memory layers/ownership, source attribution, temporal validity, proposal fields/states, scoped human approval, release/plugin research, stop conditions, retention/deletion boundaries and opt-in verification. Configuration and permissions were inspected; the private folder remains empty. One hypothetical in-chat summary was shown without persistence/adoption. No full learning cycle, memory capture, database/index or background work ran. Installed cache matches source; the existing QMD collection is refreshed. Fresh-session discovery and an explicitly authorized synthetic save/revise/approval/reject/delete lifecycle remain unverified. |
| Bounded maintenance and monitoring | 064 | Guidance now defines approved resources/helper limits, activation prerequisites, private state and baselines, meaningful-change notifications, explicit repair authority, bounded observation/retries, and pause/disable/resume controls. Existing helper code is unchanged and unrun; no scheduler, store or notification was activated. A selected supported host/runtime and separately authorized execution are still required for operational evidence. Installed cache matches source; the existing QMD collection is refreshed. Website alignment is published in version 29; the PDF remains historical. |
| Bounded native coordination | 062 | Shared execution policy now defines role admission, single-writer ownership, dependencies, finite task/revision limits, budgets, lifecycle transitions, parent integration, stopping/cancellation and opt-in verification. Source guidance only; no workers, background service, tests or evaluations ran. Dispatch/cancellation, budget enforcement and end-to-end behavior need separately authorized observation. Installed cache matches source; the existing QMD collection is refreshed. Website alignment is published in version 29; the PDF remains historical. |
| Post-implementation verification recommendation | 065 | Canonical coordinator, delivery, execution-scope and QA instructions now require a proportionate recommendation while preserving opt-in test creation/execution. Source readback only; fresh-host behavior remains unobserved. Installed plugin cache now matches source; the existing QMD collection is refreshed. Website alignment is published in version 29 and the PDF remains historical. Verify only under a separately requested scope. |
| Everyday routing and policy behavior | P01–P12; 030, 047–052 | Observe real, user-selected coding, assignment, research and writing tasks in a fresh host. Confirm proportional skill selection, scope preservation, context ownership and accurate completion feedback. Inspection alone does not establish behavioral reliability or savings. |
| Optional native profiles and delegation | P06–P07 | The local Codex session exposed all four profiles (Coding, Research, University, Career) on 16 October 2026. Discovery on other hosts, dispatch/cancellation and policy propagation remain unobserved; only exercise them if specifically selected and authorized. Do not invent a coordinator profile or assume a permanent worker service. |
| Local helpers and diagnostics | 003–004, 030–031, 040 | Dashboard, notification ledger, upstream fingerprint and installation doctor have source but have not been run. A future explicitly scoped helper run needs approved inputs/private paths and a defined outcome; notification transport and approval enforcement are separate integrations. |
| Isolated installation and recovery lifecycle | 036, 042, 045–046, 059 | Fresh-install, upgrade, rollback, uninstall and private-profile isolation scenarios remain unobserved in a suitable isolated host. The successful current reinstall/file comparison does not cover the whole lifecycle. |
| Written checks and inactive CI | 005, 033, 042–043, 075 | Requested check source exists but is **not run**; CI is prepared and inactive. No execution, activation or test/build loop unless the user later changes the current restriction. |
| Independent source/candidate review | 032, 075 | A bounded independent review has not been dispatched. Select the actual candidate and review scope first; delegation needs explicit authority. Do not recreate completed source fixes. |
| Documentation and reporting behavior | 054, 057 | Documentation-hub filtering/rendering, diagram presentation and security-report delivery are unverified. Any browser/rendering check or test message requires its own scope. The security contact is already selected in SECURITY.md; do not ask for it again. |

## Future implementation requiring a real target

Reusable guidance for these areas already exists. The remaining work is implementing or applying it to a selected project, service or question; do not create duplicate specialists to satisfy catalogue numbers.

| Area | Legacy references | Required target before implementation |
|---|---|---|
| Data/ML, framework packs, mobile and infrastructure | 001, 006–008 | Named project, actual stack/version, dataset/model or workload, required feature and relevant environment/access. |
| Cross-client continuity and additional client support | 002, 044 | A selected additional client, actual host/storage contracts and approved transfer/privacy boundaries. Do not resume deferred cloud sync or RAG as a substitute. |
| Notification and workspace connectors | 004, 012, 015 | Selected service/account, precise operation, supported provider and operation-specific authority. Local ledger source does not deliver notifications. |
| Marketing, networking, venture documents, specialized research and media | 009–014 | Actual site/account/question/venture brief, evidence, audience, assets and relevant provider access. Existing plans/guidance are not the finished campaign, research result or media. |
| Apple-platform features | 016–026 | Concrete app/action/domain/product/model/media workload and target OS/device/toolchain. Scope includes widgets/live activities, App Intents, background tasks, push, universal links, StoreKit, Core ML, Foundation Models, Vision/Speech, Metal and AVFoundation only when selected. |
| Optional delivery integrations | 027–028 | Fastlane or Xcode Cloud only for an actual app/workflow where selected; account access and any operation effects must be specified. These are optional, not completion requirements for the instruction plugin. |
| Executable action safeguards | 029 | Named custom dispatcher/runtime, authenticated approval channel, precise operation/provider contract and durable reservation/reconciliation boundaries. Instruction policy and the existing ledger are not an enforced runtime guard. |

## Public-release work

Confirmed intent: **free GitHub distribution**, primarily developers/vibe coders, **Netherlands-based release with a global audience**, English only, the project owner as sole maintainer, the existing Demir Bot website and initial YouTube/Instagram channels. These facts are settled; do not reopen them without a change from the user. Public release itself has not occurred in this work.

| Future work | Legacy references | Acceptance still needed |
|---|---|---|
| Select and freeze a release candidate | 037, 041, 059, 075 | Identify the exact source revision/snapshot and distribution contents, reconcile inventory/metadata and decide required versus inapplicable gates for that candidate. A version number alone is not candidate proof. |
| Confidentiality and third-party rights | 035, 037–038 | Inspect actual outgoing source/archive and relevant history for private material; establish exact-source provenance/licence compatibility and the rights owner's licence decision. Existing exclusions/notices do not clear the whole candidate. |
| Download, onboarding and recovery acceptance | 036, 039–042, 045–046, 059, 076 | Prepare the actual usable release asset/links and user-facing support/recovery evidence. Keep unrun lifecycle checks explicit; public support claims must match observed clients. |
| Public documentation/community alignment | 053–055, 057–058, 076–077 | Align actual accessible repository/site/docs links, current features and future work; observe rendering only if authorized. Confirm reporting/moderation arrangements and relevant GitHub settings when selected. English-only documentation and sole-maintainer decisions require no translation or extra owner assignment. |
| Education videos and media library | 077–078 | Select rights-cleared recordings/assets/provider; produce and export actual media, then publish approved videos and add real links to the existing website. Scripts/storyboards are already prepared; no fake players or illustrative outputs presented as recordings. |
| GitHub launch and optional promotion | 079 | Apply the saved adoption/channel drafts to actual approved release URLs/accounts/content. Publishing, uploads, outreach, analytics and recurring promotion need their respective authority; no account changes follow from this roadmap. |
| Candidate-specific legal/data/provider assessment | 080 | Apply `docs/legal-preparation.md`'s Netherlands/EU baseline to the actual candidate, rights, website/security-report data flows and applicable regional provider terms, including currently inaccessible Instagram terms. Prepare notices only from actual facts. Global audience intent is not worldwide legal clearance. |

## Deferred — do not resume

| Legacy item | Deferred work | Resume boundary |
|---|---|---|
| 066 | Cloud synchronization and university RAG | Cloud sync explicitly deferred; university RAG remains deferred until the dashboard is ready and setup is requested. |
| 067 | Training and compute infrastructure | No training, compute setup or spending. |
| 068 | Healthcare and regulated clinical packs | No implementation without a new selected use case and scope. |
| 069 | Crypto, trading and agent payments | No implementation, transactions or account work. |
| 070 | Logistics, manufacturing and enterprise operations | No implementation without a selected project and scope. |
| 071 | Homelab and network administration | No discovery or configuration without a selected environment and scope. |
| 074 | Early-window scheduling idea | Reassess only if explicitly requested; no schedule is active. |

## Historical inspection prompt

The following prompt records the earlier read-only inspection scope. Its background-work deferrals predate the promotion of 062–065 above; it does not override that newer planning decision.

Use **Demir Bot — Private Pilot (`demir-bot-pilot@personal`)** only. Perform a bounded, read-only inspection of the refreshed local Demir Bot installation in this fresh Codex chat. Resolve the canonical parent root and checkout from the active private local setup. Read its AGENTS.md, then the installed coordinator and its relevant profile-loading/scope instructions; resolve the active private profile without printing private content.

Confirm which namespaced Demir Bot skills are actually exposed in this session, whether the local plugin is enabled and whether its installed files still match canonical source. The last observed refresh matched 219 files at version 0.1.1. Inspect only the existing QMD configuration/status if accessible; do not refresh or query/evaluate retrieval. Its last observed state was 161 indexed files with no pending embeddings. Check whether the Coding, Research, University and Career profiles are actually discoverable by this host; source TOML files alone are not discovery proof. If the host exposes no supported discovery evidence, report that boundary without dispatching workers or inventing an agent listing.

Briefly explain the discovered architecture, relevant no-unsolicited-execution boundaries and any missing/stale evidence. Separate source/install/catalogue confirmation from runtime behavior, which this inspection does not establish. Use the current future-work roadmap at `docs/roadmap/demir-bot-master-roadmap.md` in that checkout for remaining work; read the website for current-feature presentation, recognizing that website alignment is still pending. Recommend the next eligible task without executing it.

**Do not run tests, builds, linters, validators, benchmarks, helper programs, browser/device checks or model evaluations. Do not dispatch agents, change files/settings, reinstall/index, contact providers, publish or send anything. Keep cloud sync, RAG, training and background automation deferred.** Report findings inline; no separate report/export. Do not interpret this prompt as a runtime test campaign.
