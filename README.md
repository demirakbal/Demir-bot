# Demir Bot

Demir Bot is an instruction-based personal assistant workflow for Codex. It selects relevant skills and available tools for coding, university work, research, writing and LinkedIn. The development plugin bundles 27 skills: one coordinator and 26 specialists. This repository is the development source, with opt-in QA assets and a maintained roadmap. The October implementation refines intent/scope routing, native ChatGPT/Work/Codex capability selection, source ownership, everyday workflows and timed continuous progress. Four optional project-scoped execution profiles reuse the same specialist procedures; they are definitions, not running agents.

It is not an always-running service, a trained model, or an account-access mechanism. Installing it does not install Gmail, Firecrawl, Higgsfield or other external plugins, authenticate accounts, or grant permission to send or publish.

## Guides and source access

The planned distribution is a free GitHub project. See [obtain source and first use](docs/download-and-first-use.md) for the configured repository target and the distinction between source download, supported registration and installation. No new public release/download artifact is claimed here.

| Need | Guide |
|---|---|
| Setup and day-to-day work | [Install](docs/installation.md), [usage](docs/usage.md), [cookbook](docs/cookbook.md), [synthetic examples](examples/README.md) |
| Existing copies or failures | [Update/rollback](docs/update-and-recovery.md), [troubleshoot](docs/troubleshooting.md), [support matrix](docs/support-matrix.md) |
| Repository contributions | [Git recipes](docs/git-recipes.md), [contributor guide](CONTRIBUTING.md), [collaboration](docs/collaboration.md) |
| Release evidence and rights | [Acceptance/recovery](docs/release-acceptance.md), [source review](docs/source-review.md), [licensing](docs/licensing.md), [source records](docs/supply-chain.md), [changelog](CHANGELOG.md) |
| Project participation | [Community](docs/community.md), [conduct](CODE_OF_CONDUCT.md), [security reports](SECURITY.md) |


## Start here

1. Follow [local installation](docs/installation.md) for the existing supported Codex path. Source checkout, installed plugin and fresh-task discovery are separate states.
2. In a task where the bundled coordinator is available, give the outcome, actual source and scope: “Use Demir Bot to revise the paragraph below. Keep the supplied facts and return a draft.” No account connection is needed for this supplied-content example.
3. For code, name the actual checkout/feature and allowed changes. For an assignment, supply the assignment/rubric/starter material and selected part. State test writing and execution separately when wanted; neither is automatic.
4. For a chain, request elapsed time and a change summary after each item, followed by continued work on the next eligible item. The active session does the work; an ended session does not imply a background service.

Expected first-use output is the scoped draft/source change and material missing dependencies, with saved work distinguished from observed runtime results. These examples have not been run as a fresh-install test. Personalization is optional; use only approved facts and the existing private-profile loader. For setup limits see the [support matrix](docs/support-matrix.md); for existing-copy changes see [update/recovery](docs/update-and-recovery.md). There are no verified screenshots, performance badges or all-client claims in this quickstart.

The [local documentation hub source](docs/index.html) provides a searchable guide directory, with a [workflow diagram](docs/how-it-works.md). It has not been previewed or deployed; canonical content remains in the Markdown guides.

## Repository layout

```text
plugins/demir-bot-pilot/
  .codex-plugin/plugin.json     Plugin manifest
  skills/
    demir-bot/                 Coordinator
    <skill-name>/
      SKILL.md                 Skill instructions (the skill's source)
      references/              Supporting guidance and provenance, where present
      agents/openai.yaml       Client metadata, where present
      LICENSE*                 Retained upstream notices, where present
docs/roadmap/                  Current specification, roadmap source and PDF
.codex/agents/                 Four optional project-scoped native Codex profiles
AGENTS.md                      Instructions for working on this repository
RESOURCES.md                   Linked inventory of bundled reference resources
```

Most of the source is Markdown and YAML. The coordinator also includes optional local dashboard, notification-deduplication and source-fingerprint helper source. The QA skill includes opt-in Python structural checks, synthetic tests and a manual evaluation runner, while docs/roadmap contains the PDF renderer. The new legacy-batch helpers/checks have not been run. The existing local publishing runtime, credentials and user records are deliberately not bundled. The `plugins/` directory can hold additional first-party plugins later; unrelated third-party packages should remain external dependencies.

## Included skills

| Skill | When to use it |
|---|---|
| [demir-bot](plugins/demir-bot-pilot/skills/demir-bot/SKILL.md) | Coordinate tasks, select specialists and preserve scope and user preferences. |
| [git-and-github-workflow](plugins/demir-bot-pilot/skills/git-and-github-workflow/SKILL.md) | Inspect Git state, make scoped commits/PRs and recover safely within authorization. |
| [context-efficiency](plugins/demir-bot-pilot/skills/context-efficiency/SKILL.md) | Reuse evidence, read selectively and keep tool output focused. |
| [clarify-and-execute](plugins/demir-bot-pilot/skills/clarify-and-execute/SKILL.md) | Resolve material ambiguity through useful choices, then execute. |
| [execution-details](plugins/demir-bot-pilot/skills/execution-details/SKILL.md) | On explicit request, explain recorded actions and results, assess mistakes and propose scoped lessons. |
| [project-requirements-discovery](plugins/demir-bot-pilot/skills/project-requirements-discovery/SKILL.md) | Interview for substantial projects, uncover underlying needs and produce atomic, verifiable requirement bullets; separate from assignment analysis. |
| [requirements-and-traceability](plugins/demir-bot-pilot/skills/requirements-and-traceability/SKILL.md) | Map user jobs, MVP scope, ownership, acceptance criteria and evidence links. |
| [assignment-planning-and-delivery](plugins/demir-bot-pilot/skills/assignment-planning-and-delivery/SKILL.md) | Break down assignments and adapt delivery to staged prompts, guided explanations or authorized implementation. |
| [automated-assignment-completer](plugins/demir-bot-pilot/skills/automated-assignment-completer/SKILL.md) | Execute authorized assignment stages sequentially, followed by final deliverables review. |
| [assignment-deliverables-checker](plugins/demir-bot-pilot/skills/assignment-deliverables-checker/SKILL.md) | Review final work against assignment sources and rubrics; flag gaps and extras for user decisions. |
| [architecture-review](plugins/demir-bot-pilot/skills/architecture-review/SKILL.md) | Orient to repositories and examine boundaries, dependencies and architectural trade-offs. |
| [code-refactoring-refactor-clean](plugins/demir-bot-pilot/skills/code-refactoring-refactor-clean/SKILL.md) | Perform requested or concretely justified behavior-preserving refactoring. |
| [documentation-and-adrs](plugins/demir-bot-pilot/skills/documentation-and-adrs/SKILL.md) | Maintain requested documentation and architectural decisions. |
| [qa-and-test-evidence](plugins/demir-bot-pilot/skills/qa-and-test-evidence/SKILL.md) | Plan, write or run tests only within the explicitly requested scope. |
| [privacy-review](plugins/demir-bot-pilot/skills/privacy-review/SKILL.md) | Review collection, sharing, retention and reuse of personal information. |
| [demir-linkedin](plugins/demir-bot-pilot/skills/demir-linkedin/SKILL.md) | Research and draft posts, improve positioning and prepare networking actions. |
| [personal-writing](plugins/demir-bot-pilot/skills/personal-writing/SKILL.md) | Route writing to the relevant channel tone and approved facts. |
| [linkedin-tone](plugins/demir-bot-pilot/skills/linkedin-tone/SKILL.md) | Apply the user's privately stored LinkedIn calibration. |
| [email-tone](plugins/demir-bot-pilot/skills/email-tone/SKILL.md) | Apply audience-specific email language and approved signatures. |
| [deep-research-and-idea-validation](plugins/demir-bot-pilot/skills/deep-research-and-idea-validation/SKILL.md) | Review academic evidence, alternatives, feasibility and demand. |
| [frontend-quality-and-accessibility](plugins/demir-bot-pilot/skills/frontend-quality-and-accessibility/SKILL.md) | Implement semantic, keyboard-accessible and responsive interfaces. |
| [release-readiness-and-observability](plugins/demir-bot-pilot/skills/release-readiness-and-observability/SKILL.md) | Assess deployment prerequisites, rollback, health signals and recovery. |
| [swiftui-performance-and-concurrency](plugins/demir-bot-pilot/skills/swiftui-performance-and-concurrency/SKILL.md) | Handle SwiftUI state, identity, task lifecycle and actor isolation. |
| [jurisdiction-specific-legal-feasibility](plugins/demir-bot-pilot/skills/jurisdiction-specific-legal-feasibility/SKILL.md) | Research a defined activity, jurisdiction and date using official sources. |
| [agent-configuration-review](plugins/demir-bot-pilot/skills/agent-configuration-review/SKILL.md) | Review agent, skill, hook and MCP configuration within requested scope. |
| [ml-training-specialist](plugins/demir-bot-pilot/skills/ml-training-specialist/SKILL.md) | Assess or implement project-specific ML workflows; distinguish retrieval from training. |
| [youtube-learning](plugins/demir-bot-pilot/skills/youtube-learning/SKILL.md) | Learn from transcript and visual evidence; retry transient retrieval failures, then stop and ask before changing sources or producing substitutes. |

## Working principles

- Implement the requested work; ask questions only when answers materially change the result.
- Testing is opt-in. Writing code does not automatically authorize tests, linting, builds, browser checks or repeated fix loops.
- Keep facts, inference, proposals and executed evidence separate.
- Require approval of the exact external action, content and destination before publishing or sending.
- Preserve rollback and private-data boundaries. No autonomous learning, background automation or cloud synchronization is implied.

## Private personalization

The [profile loader](plugins/demir-bot-pilot/skills/demir-bot/references/profile-loading.md) resolves an explicit profile directory, then `DEMIR_BOT_PROFILE_DIR`, then `demir-bot-private` under `CODEX_HOME` (default `~/.codex`). Personal facts, tone examples, account history and local commands remain there, outside this repository.

Without a profile, use supplied facts and provisional tone; do not assume Demir's identity or accomplishments. Do not commit the private profile, correspondence, CVs, credentials, publishing queue, course documents, index databases or backups. `.gitignore` is a convenience, not a privacy guarantee: inspect staged changes before pushing.

See the [dependency and support matrix](docs/support-matrix.md) for required versus optional components, version/access boundaries and evidence limits.

## Optional external capabilities

Demir Bot can select available Firecrawl, Gmail, GitHub, Figma, Sites, Higgsfield, Visualize, document/PDF tools, Codex Security and other relevant providers. See [provider routes](plugins/demir-bot-pilot/skills/demir-bot/references/plugin-routes.md). Install and authenticate providers separately, only when needed. Availability and permissions differ by client and account.

RTK and QMD are optional local helpers. Neither is included. The plugin contains publishing approval guidance but does not include a Buffer connection or executable publisher. University RAG is a deferred project, not an implemented service in this repository.

The [everyday usage guide](docs/usage.md) gives natural requests, expected boundaries, test permissions and preference/continuation controls.

## First use and optional execution profiles

In an authorized local Codex task with the plugin available, ask naturally for the outcome, project and scope. For example: “Use Demir Bot to revise this supplied professor-email draft. Keep it concise and do not send it.” The expected result is a draft using the existing email tone and supplied facts, not an account connection or research campaign. For coding/assignments, supply the actual checkout or assignment sources and selected part. Tests/builds remain opt-in; say explicitly whether you want test writing, execution or fixes. These examples describe expected behavior, not recorded successful runs.

For an explicitly assigned multi-item chain, request an update after each item with observed elapsed time, changed files and evidence limits, then continued work without acknowledgment. The active Codex task can follow that chain; the plugin itself is not an always-on service. A stopped/suspended session must not claim background progress. Dots are optional, account-dependent infrastructure and are not required for the same source plan.

The repository's `.codex/agents/` defines `demir_coding`, `demir_research`, `demir_university` and `demir_career` using the documented standalone Codex profile format. They inherit the parent model and permissions. Use only when actual human delegation authority and supported host discovery are present; otherwise apply the same procedure inline. No worker was launched to implement this revision. These repository profiles are outside the installed skills package and are not copied globally by plugin installation. See the [role/handoff guide](plugins/demir-bot-pilot/skills/demir-bot/references/agent-profiles.md).

Use the [installation guide](docs/installation.md) for the supported local setup sequence, marketplace prerequisite, discovery boundaries and current help-inspection evidence. Commands below describe the existing configured environment.

## Local installation, updates and scoped recovery

Resolve the configured marketplace and its source pointer before an installation operation; cloning alone does not register a plugin. The existing local installation for this development environment is `demir-bot-pilot@personal`, whose marketplace points to this plugin source. Other users must use their actual configured marketplace, not assume that selector exists. Inspect the current CLI's supported help/catalogue before a requested setup; do not invent installation commands for another host or grant account access through source instructions.

When explicitly authorized to refresh this existing local installation, the supported operation observed in this environment is `codex plugin add demir-bot-pilot@personal --json`. Inspect its returned version/path and compare saved source with that installed copy; a successful install response alone does not prove current behavior. Start a fresh task/reload the supported client to discover changed instructions. If the host requires a version/cachebuster update, make it in development source through the supported flow, never patch generated caches. The October source batch kept manifest version 0.1.1; a subsequent separately authorized refresh installed that source as recorded in Current status below.

Uninstall only the exact human-selected registration through the supported host operation; the local CLI exposes `codex plugin remove demir-bot-pilot@personal --json` for this selector. This example is documentation, not an uninstall request. Local and account-hosted plugins can have the same display name yet distinct identities. Inspect those identities before removal; do not delete the development checkout, marketplace, owned cloud definition or private profile as incidental cleanup.

For rollback, compare current files with the scoped pre-edit copies/version evidence and reverse only the implicated change, preserving subsequent user work. Source rollback is not installed-cache rollback, cloud rollback or proof of uninstall/profile isolation. Refresh only when separately authorized. QMD likewise needs exact current collection/update authority; keep private profile data and rollback copies outside the index. No dependency install, index rebuild, cloud sync or tests follow from these instructions.

If a skill is missing, distinguish registration, stale installed source, fresh-task discovery and missing client support. If an operation fails, distinguish unavailable tools, authentication, missing files/projects and permission denial; never bypass a denial or retry unchanged failures. Share only scoped source/version/error evidence with secrets redacted. The native [routing/fallback](plugins/demir-bot-pilot/skills/demir-bot/references/plugin-routes.md) and [handoff](plugins/demir-bot-pilot/skills/demir-bot/references/agent-profiles.md) references own detailed recovery boundaries. An optional [read-only installation doctor](plugins/demir-bot-pilot/skills/demir-bot/references/installation-doctor.md) now has saved source; it has not been run and does not repair installations or establish native discovery/account access.

For scoped updates, exact-registration removal and rollback, use [update and recovery](docs/update-and-recovery.md). Source, installation, index, private profile and cloud recovery remain distinct.

For duplicate entries, stale skills, unavailable files/tools, index gaps or permission errors, use [troubleshooting](docs/troubleshooting.md). Preserve exact identity and failure evidence before any scoped repair.

## Development workflow

1. Clone this repository and open that checkout as the Codex project. Use its `AGENTS.md` instructions.
2. Inspect branch, remote, upstream and local edits first. Fetch/integrate only within the requested scope, choosing an explicit strategy after reviewing divergence. Use the bundled Git workflow guidance and a focused branch when appropriate.
3. Edit `plugins/demir-bot-pilot/skills/<name>/` and relevant references. Keep the plugin ID stable to preserve existing skill names.
4. Inspect the diff and staged files. Run tests or evaluations only when explicitly requested. Retain upstream notices and provenance.
5. Review affected documentation against the outgoing source and evidence, resolving mismatches under the Git skill’s documentation-alignment rule. Commit, push and create or merge pull requests only within the task's authorization. Inspect focused staged changes and the full outgoing range; preserve unrelated work. Ordinary edits do not authorize publication or history rewriting.
6. Updating repository files does not automatically update an installed plugin cache. Use the current supported plugin installation/update workflow to point the local marketplace at this checkout, then reinstall the local plugin and verify the client catalogue. Do not edit cache files directly or reinstall standalone duplicates.

Resolve the actual marketplace source before refreshing an installation; do not assume that cloning alone changes that pointer. The supported update flow preserves plugin identity and reinstalls from the confirmed local marketplace, updating a source manifest cachebuster only when required by that host/workflow. Keep private profile paths outside the checkout and preserve rollback during that transition. QMD collection paths, if used, need an explicit scoped update; do not index private data or Git history.

## Current status and limitations

Source status — 16 October 2026:

- **Current development package:** 27 instruction skills (one coordinator and 26 specialists), four optional native project profiles, and 223 package files at version 0.1.1. Project Requirements Discovery and its coordinator/requirements routes are saved in source; interview behavior is unverified. The supported personal-plugin refresh installed and enabled version 0.1.1; all 223 installed package files match canonical source byte-for-byte. QMD now includes the new skill in the existing collection. Start a fresh session to discover the updated catalogue; cloud sync remains deferred.
- **062–065:** bounded coordination, maintenance/monitoring guidance, approval-only lessons and on-demand research, and post-implementation verification recommendations are saved. Tests remain opt-in. No workers, diagnostic helpers, schedules or background learning were activated.
- **Private proposal setup:** an empty private folder and configuration exist outside this repository, with owner-only permissions. A disposable manual lifecycle observed save/readback, revision, simulated rejection, explicit revision-specific approval, application/readback, byte-matching rollback and cleanup. An official Codex memory-docs comparison found no change needed to the recall-versus-approval boundary. Automated enforcement and broader cross-session behavior remain unverified; no chats were imported.
- **QMD:** the latest authorized existing-collection refresh indexed 2 new and 4 updated documents, with 158 unchanged; 28 chunks were embedded across 6 documents. Final status: 164 indexed files, 1117 vectors and no pending embeddings. Only the new project-discovery skill was added to the existing folder selection; private proposals remain excluded. The 398 reported orphaned embedding chunks were not cleaned up. Indexing does not establish retrieval quality.
- **Documentation/site:** the master Markdown is current planning; the September PDF is historical. The existing website remains published as Sites version 29. Its separate local source now includes Project Requirements Discovery and the completed 063 evidence; this content update is not published. Design and animation files are unchanged; rendering was not checked.
- **Release preparation:** guides, examples, helper/check source and inactive CI templates are prepared. Public source availability is distinct from a reviewed release asset, licence clearance, lifecycle acceptance or measured effectiveness. See the roadmap for remaining requirements.
- **Inactive/deferred:** cloud sync, university RAG, training, automatic maintenance and background learning. No tests, builds, model evaluations or live-provider behavior checks ran in this update.

Historical status recorded on 28 September 2026 (not current-source execution evidence):

- **Source:** 26 instruction skills, one coordinator and 25 specialists; A2 items 001–039 have saved guidance. The remaining roadmap is renumbered 001–080.
- **Installed:** version `0.1.0+codex.20260928130840` was installed from the development source on 28 September 2026; all 178 source files matched the installed copy. This includes bounded transcript recovery and the requirement to ask before substituting sources. Start a new Codex task to load the refreshed plugin; this installation does not establish behavioral test results.
- **QA evidence:** the latest recorded offline run passed 51/51 tests on CPython 3.12. This is a historical tested snapshot; no tests were rerun for these documentation changes. The earlier ten-case manual scope was accepted; the 65 prepared core/A2 behavioral cases remain unrun and deferred.
- **Evaluation runner:** the free [manual runner](plugins/demir-bot-pilot/skills/qa-and-test-evidence/runner/README.md) manages packets, responses and human grades. It makes no model/API calls and cannot enforce tool isolation or establish full functionality.
- **Git workflow:** review affected docs before pushing; when a material mismatch exists without authorization to fix it, ask whether to update the docs or push as-is. This is skill guidance, not a Git hook.
- **Remaining limits:** no full behavioral/live-provider pass or measured cost/reliability gain. CI, cloud synchronization, university RAG, training and background services remain inactive.

Use the [current Markdown roadmap](docs/roadmap/demir-bot-master-roadmap.md) for remaining implementation, verification, release preparation and explicit deferrals. Its [September PDF snapshot](docs/roadmap/demir-bot-master-roadmap.pdf) predates the October plan and implementation. Source completion, operational acceptance and public release remain separate. Older source item labels retain historical identity; they do not reset execution order.

The [structural-check guide](plugins/demir-bot-pilot/skills/qa-and-test-evidence/checks/README.md), [behavioral cases](plugins/demir-bot-pilot/skills/qa-and-test-evidence/behavioral/cases.md) and [comparison guidance](plugins/demir-bot-pilot/skills/qa-and-test-evidence/references/demir-bot-evaluation.md) describe distinct evidence methods. Their presence does not authorize execution, and the accepted manual scope does not require rerunning the larger prepared suite.

## Website

The [Demir Bot website](https://demir-bot-fieldnotes.demirakbal.chatgpt.site) presents the skill catalogue and current evidence. Its local `website/` checkout is a separate Sites source repository, excluded from this repository; publishing and access settings are managed through Sites.

## Sources and licensing

See [RESOURCES.md](RESOURCES.md) for the bundled references and notices, and [upstream adaptations](plugins/demir-bot-pilot/skills/demir-bot/references/upstream-adaptations.md) for source URLs, reviewed versions where recorded, borrowed guidance and intentional omissions.

Existing upstream licence files are preserved in their skill directories. This repository does not assign a blanket licence to material with differing or unassessed provenance. Public distribution requires checking the applicable permissions and attribution; a private repository is not a licence grant.
