# Coverage audit — 27 September 2026

This audit inventories retained evidence and adds missing regression assets. It is not a claim that every skill or reference has undergone a full semantic/code-smell review. The user authorised creating tests/fixes and then explicitly authorised local offline tests only. No model evaluations, live providers, installation, private-data access, index/cache refresh or background activity is authorised.

## What was already tested

Evidence source: the checkout's `docs/roadmap/demir-bot-master-roadmap.md`, sections “Retained assessment and installation evidence”, “Structural correction and test record”, “Execution Details and structural acceptance” and “Behavioral regression and manual evaluation”. These are retained historical summaries; original temporary reports and screenshots were not recovered or regraded in this audit.

| Area | Retained result | Scope and limit |
|---|---|---|
| Initial package | 31 grouped structural assertions; 12 sampled synthetic responses; source reviewer read skill bodies | Historical snapshot, selective references; not current acceptance or full workflow execution |
| Focused corrections | 9/9 source assertions, 17 links, six synthetic responses | Historical focused scope; not universal reliability |
| Structural validator | Corrected 24/24 suite, followed by assignment and Execution Details updates | Latest recorded pass: 145 files, 26 skills, snapshot `e0dd26073391a5fd15d4f26857d04a9c3878c97845529420ff6137d9b3e38be0`; later A2 edits are outside that result |
| Manual behavior | Ten distinct tagged cases accepted by the user | Arithmetic, bounded patch, evidence-limited comparison, publication boundaries, confidentiality, hostile source text, fictional email, CI uncertainty, honest claims and response-only preferences; no per-domain blanket acceptance |
| A2 001–039 | Saved instructions and source readback | No retained functional model runs or real project/provider validation for this batch |
| Code quality | Historical scoped source review and structural checks | No retained comprehensive current code-smell assessment, mutation score or runtime quality result |

All 26 skill owners are listed in `checks/inventory.json`. [Core reviewer cases](core-cases.json) now map one scenario to every owner, including assignment and Execution Details skills. [A2 reviewer cases](a2-cases.json) map every item 001–039 to its actual source. Each case has a separate synthetic input and expected outcome. These maps provide explicit missing-coverage inventory, not a claim that one case exhausts a skill. Existing [B086 cases](cases.md) remain unchanged and reusable for cross-cutting negative paths. Optional/deferred roadmap items are not marked implemented merely because a route mentions them.

## Changes and quality findings

- Fixed three source-supported validator crash paths: unreadable directory enumeration, malformed URL parsing and an anchor pointing to non-UTF-8 Markdown. They now produce findings rather than uncaught exceptions. Added three synthetic regression tests in `test_structural.py`; execution remains blocked below.
- Corrected stale evidence wording: the structural README no longer denies the historical pinned-environment run; the behavioral README no longer calls the corrected run merely planned; the manual 32-response proposal is explicitly historical and does not reopen the accepted ten-case scope.
- Added 39 A2 and 26 core reviewer cases, with all statuses `not_run`. Expected outcomes emphasize useful completion, uncertainty, permission boundaries and avoiding unsupported claims. They are not keyword tests against instruction wording.
- Added dependency-free integrity tests for complete IDs/owners, package-contained existing source paths, unique inputs and honest execution labels. These do not grade semantic behavior.

Remaining quality concerns: several skill entrypoints have accumulated lengthy conditional guidance and repeated restrictions during A2. This audit does not infer functional failure from length or perform a broad rewrite without behavioral evidence. Source-only API/platform guidance must still be checked against actual project versions. No current reference library, all-provider integration or technical advice corpus has been certified correct by the structural suite.

## Observed local runs

Interpreter: bundled CPython 3.12 environment at the host's workspace-dependency runtime; not the historical pinned CPython 3.11.11 environment. No packages were installed.

1. Existing `python -m unittest -v test_structural`: failed at import with `ModuleNotFoundError: yaml`; no structural test body executed. Do not count this as one failed product case or a pass. The historical environment was not found in the inspected runtime locations.
2. First integrity-suite invocation used the repository root and failed to find `test_a2_coverage`. Corrected the working directory to `skills/qa-and-test-evidence/checks`; this was invocation recovery, not a hidden assertion retry.
3. A2-only integrity suite: 4/4 passed. After adding core coverage, final `PYTHONDONTWRITEBYTECODE=1 python -m unittest -v test_a2_coverage`: 8/8 passed, exit 0. These results establish only case integrity and source reachability.

The three validator fixes and full current-package structural acceptance remain execution-unverified because the declared parser/validator dependencies are unavailable in the selected environment. No fallback parser or weakened assertion was introduced to make the suite pass. Use an existing correctly provisioned environment or separately authorise dependency provisioning; installation is not implied by offline-test approval.

## Future behavioral execution protocol — not authorised now

If separately authorised, select a bounded subset of new cases for the affected implementation batch, plus relevant existing B086 negative cases. Declare case IDs, exact source snapshot, model/settings, attempt count, no-retry/stop rules and isolation before execution. Do not automatically run all 65 cases. Provide only the input and appropriate candidate source to the subject; keep expected outcomes in the reviewer context. Use synthetic/no-live-action boundaries. Record criterion evidence and forbidden actions separately; text-only outcomes do not establish tool enforcement. Preserve failures and mark setup issues or missing access inconclusive, not passed.

Full functionality and quality acceptance requires relevant behavior evidence; real app/database/signing/release operations additionally require their own named project and authority. The 65 prepared cases, eight local integrity passes and historical ten-case acceptance must never be combined into “75 functional tests passed”.

## Subsequent authorised validation — current status

The user subsequently authorised isolated pinned test dependencies and a 65-case, one-response-per-case, no-retry, current-model, tool-disabled behavioral evaluation. Installation succeeded in a temporary environment with CPython 3.12 and the declared dependency versions. The historical reference interpreter remains 3.11.11; this pass is on 3.12, not proof of cross-version support.

The first full run executed 35 tests: 33 passed and two newly added fixtures failed. Markdown normalised the malformed URL before URL parsing; that case now injects a parser exception to test failure containment, not a proven malformed-URL reproduction. The directory fixture now resolves the macOS temporary path before comparison. Intended assertions were preserved.

Two additional regressions reproduced a symlink-loop crash and a collision between explicit and generated heading anchors. The validator now reports failed path resolution and allocates unique heading suffixes. Final combined result: 37/37 passed (29 structural cases including current-package acceptance, eight reviewer-case integrity cases). Full-package inspection reported zero findings. This supersedes the dependency-blocked status above while preserving the failed-attempt history.

Code review covered the executable validator and local tests for exception handling, filesystem/link boundaries, duplicate metadata handling and heading generation. This is a scoped code-quality review, not certification of every technical instruction or live integration. No code-smell score, coverage percentage or universal correctness claim is made.

Behavioral execution remains blocked before any subject attempt: CLI help, generated protocol schemas and feature controls were inspected, but a supported all-tools-disabled evaluation boundary was not established. Read-only execution is not tool-disabled execution; a no-tools prompt is not enforcement. All 65 cases remain not_run. Approval persists for the bounded campaign, but does not authorise weakening isolation, changing the selected model or using a paid external API. A supported isolated evaluator is still required. Live provider/project functionality additionally needs named targets and supported operation-specific access.

Durable local test output and structural JSON were retained outside the distributable plugin in the companion documentation workspace under `validation/2026-09-27`. No installed-cache/index refresh, cloud sync, model subject call, account change or background automation occurred. Current status: local structural and case-integrity pass; scoped executable-code review completed; full behavioral/live functionality pass not established.
