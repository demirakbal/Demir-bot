# Risk-based test design

Inspect applicable normal, boundary, invalid/missing/empty, duplicate/order, error and state-transition behavior. Include action-order regressions, authorization denial, user isolation, transaction rollback, partial success, retries, cancellation and concurrency when relevant.

Unit tests establish local logic. Mocked integration establishes behavior against a model, not the actual dependency. Real integration covers affected mappings, constraints, permissions, transactions, migrations and contracts. E2E covers selected whole workflows. Acceptance evaluates criteria for specified actors; usability observations and formal approval are separate.

Use arrange/act/assert/cleanup, descriptive names, controlled clocks/seeds, stable fixtures and explicit expected values. Clear tests may repeat setup. Avoid broad mocking that removes the behavior being tested. Test public contracts or extract meaningful units rather than making private APIs public solely for tests.

Browser tests: use semantic locators and observable readiness/assertions. Do not universally wait for networkidle or add fixed sleeps. Inspect rendered state when necessary; close resources. Screenshot existence alone is not a successful functional or accessibility check.

Exports: inspect real filenames, bytes, format and meaningful content (CSV rows, XLSX sheets/cells, ZIP members, image dimensions/content). Download callback mocks establish invocation only. Persistence: real write/read and transaction behavior need a controlled real dependency test, not only mocked return values.

Performance requires agreed thresholds, workload, environment and measured results. Security needs applicable negative paths and scoped scans; never claim absence of vulnerabilities. Accessibility needs applicable automated and manual checks; an automated scan alone is not complete conformance.

Property/metamorphic tests suit invariants and calculations; differential tests require a trustworthy reference. Mutation testing can assess assertion weakness when justified. Fuzz/load/fault-injection techniques are optional and risk-scaled. No fixed 70/20/10 test ratio or universal 80/100% coverage threshold. Respect actual project gates.

## Project E2E and accessibility scope

Roadmap item 030. Trigger: explicitly requested project E2E/accessibility work or instruction maintenance. Reuse the parent QA workflow, [execution evidence](evidence.md), [frontend accessibility guidance](../../frontend-quality-and-accessibility/SKILL.md) and the stack-specific selection section below. Existing guidance already covers semantic locators, observable readiness, isolation and accessibility limitations; do not create another testing coordinator or generic browser recipe library.

### Establish the project, access and observable flow

For project work, identify the named project/revision, actual framework/runner/browser versions, target URL/environment, available browser tooling and operation-specific access. Distinguish tool availability from an established browser connection, reachable app and authorised session. Superpowers can structure testing/debugging but supplies none of those facts and does not prove accessibility coverage. Use applicable workflows without activating prohibited tests, reproduction or delegation.

Select concrete user flows from requirements and affected risk, including relevant error paths. Name the actor, owned synthetic preconditions, actions, expected visible outcome and external side effects. A happy-path page load alone does not establish a complete user outcome. Keep real versus mocked network, authentication, persistence and service boundaries explicit; intercepted responses do not prove backend integration. Use the smallest meaningful flow set rather than expanding into a broad browser campaign.

Reuse existing project setup and supported browser tooling when separately authorised. Inspect relevant scripts and configuration before assuming they are safe: starting a server, installing browsers/dependencies, seeding data, logging in and running a test are distinct operations. Do not install providers, change accounts or start services merely to fill a dependency gap. Avoid live purchases, messages, production mutations or private-data capture. No named project, stack, target URL or access is supplied by this roadmap instruction, so do not open a browser or fabricate connection evidence.

### Accessibility evidence has explicit limits

Apply the frontend specialist's semantics, keyboard/focus, forms, responsive states and reduced-motion guidance to the selected flows. Separate source review, automated rule findings and observed manual/browser/assistive-technology results. Report the exact states and methods assessed and what remains unassessed. A scan with no findings does not establish full conformance, and a screenshot cannot prove keyboard behavior, accessible names or screen-reader usability.

Use actual project requirements and current official standards/tool documentation when a criterion or version-specific API is material. Do not invent conformance levels, audited pages, tested devices or disabled-user participation. For separately authorised assessment, identify meaningful manual gaps such as focus order/restoration, validation announcements, zoom/reflow and screen-reader interaction where relevant; planning those activities is not executing them. Do not turn instruction maintenance into an audit or write checks to demonstrate this prose.

### Add setup, traces or flaky-test detail only for a real gap

First identify the actual project failure or missing practical step and why existing QA/runner guidance is insufficient. Only then add a narrow version-appropriate recipe. No stack-specific setup, trace tooling or recovery script is justified by this roadmap label alone.

For supplied failure evidence, distinguish product behavior, selector/readiness, shared state, environment/access and runner problems; mark causes inferred rather than observed. Reuse semantic locators and observable outcomes, bounded waits and owned cleanup. Do not fix unexplained failures with fixed sleeps, weaker assertions, broader matching or unlimited retries. A later pass does not erase an earlier failure, and retries alone do not diagnose flakiness.

Inspect only relevant supplied trace excerpts or already-authorised artifacts. Traces, videos, screenshots and network payloads can contain tokens, personal data and session state; do not enable recording, read stored credentials or upload artifacts automatically. For separately authorised recording, agree the scope/destination, use synthetic data and retain only necessary evidence under project policy. Do not copy traces into distributable skill files. Link to the actual run/revision and preserve original failure versus retest status without inventing evidence paths.

Any reproduction, fix, rerun or quarantine remains within applicable authority. A justified quarantine needs visible rationale, owner/revisit criteria and a clear coverage gap; it is not a passing result. Do not add quarantine machinery or change CI merely to hide a failure. Missing browser access is reported as blocked/not run, not resolved by installing a provider or silently switching to a different environment.

### Demir Bot regression and acceptance boundaries

Reuse [the existing evaluation reference](demir-bot-evaluation.md) for Demir Bot regressions rather than substituting application E2E results. Relevant regression coverage accompanies implementation batches when its creation/execution is authorised; comprehensive validation belongs to phase C. These roadmap stages are planned validation responsibilities, not standing authority to write cases, run models, delegate or execute checks. Under the present no-check/no-evaluation scope, batch regressions and phase C validation remain unperformed; source inspection is not their replacement.

Prose acceptance examples, not executable cases or fixtures:

- Trigger: a supplied flow loses focus after a recoverable form error. Expected action: trace the actual interaction and define the visible error and focus outcome using frontend guidance. No-action case: browser access or execution is absent; do not claim interactive verification or run the app.
- Trigger: a supplied browser test intermittently fails after navigation. Expected action: inspect relevant evidence for readiness, identity, state and environment causes, retaining uncertainty and failure history. No-action case: no trace or reproduction authority exists; do not record a session, add sleeps or start a retry loop.
- Trigger: an automated accessibility report has no findings. Expected action: state the scanned scope and remaining manual/assistive-technology gaps. No-action case: do not claim complete accessibility or conformance from that result.

Report saved instructions, supplied evidence, observed operations and unverified project behavior separately. This instruction-only change creates no suite, fixture, check, browser setup or trace. No tests, builds, evaluations, benchmarks, delegation, commits/push, installation, publication, spending, account changes or private-data modification. Preserve unrelated work, coordinator routes, installed caches and QMD indexes; keep cloud synchronization, university RAG, training and background automation inactive.

Source basis: roadmap item 030 and existing QA, evaluation and frontend accessibility instructions. No browser access, project setup, accessibility result or flaky-test recovery was verified by this guidance change.

## Stack-specific recipe selection

Roadmap item 029. Trigger: a named project's requested testing task exposes missing practical detail after the QA workflow and relevant guidance above are reused. This section establishes how to select a recipe; it does not create tests, fixtures, a runner or a second testing coordinator. Reuse [Demir Bot evaluation](demir-bot-evaluation.md) only for its separate assistant-evaluation scope. Application tests do not establish assistant routing quality, and an assistant evaluation does not establish application correctness. Reading either reference authorises no execution.

### Establish the project and missing detail

Identify the actual language/runtime, framework, test runner and relevant plugin versions from supplied evidence and project configuration. Inspect existing adjacent tests, configured commands, discovery rules, environment and requirements only within the requested scope. Do not infer pytest from Python, a particular JavaScript runner from TypeScript, or a browser environment from React. Existing package scripts may contain builds, network work or other side effects; their presence does not authorise invoking them.

State the missing practical detail with a source locator or supplied failure, the observable behavior at risk and why existing guidance is insufficient. Reuse applicable Superpowers testing/debugging methodology for the actual task, without assuming it supplies every framework API. Do not activate a red/green loop, reproduction, delegation or evaluation merely to maintain instructions. Test creation, execution, fixes and reruns retain their explicit boundaries; omitted execution is reported, not implied by a written recipe.

No named project, versions or failure evidence is supplied by this roadmap item. Save this selection guidance without inventing a project gap or adding speculative pytest, JavaScript/TypeScript or React recipes. Obtain current official runner/framework documentation before prescribing version-sensitive fixtures, async behavior, mocking, timers or rendering APIs in a later project task.

### Add only the needed recipe when justified

For separately authorised guidance or implementation, keep one focused recipe with its trigger, supported project/version context, requirement-derived expected outcome, setup/cleanup ownership and limitations. Prefer the existing test structure and dependencies; do not install a runner, migrate frameworks or replace a working suite for novelty. Illustrative prose is not permission to create executable examples or fixtures.

Investigate only relevant project details:

- Python/pytest: actual discovery and fixture scope, owned resources and cleanup, existing async plugin/event-loop conventions and isolation. Do not assume a plugin or run collection as harmless discovery; importing tests can execute code.
- JavaScript/TypeScript: the actual runner, module/transformation configuration, runtime environment, async completion, mock restoration and timer ownership. Transpilation and type checking are different claims; neither replaces a behavioral assertion. Do not mix APIs from different runners based on similar syntax.
- React: the project's rendering and interaction tools, observable user behavior, async states, semantics and focus. Reuse frontend-quality-and-accessibility rather than asserting component internals or treating a simulated DOM as evidence of real layout, browser or assistive-technology behavior.

Keep expected results independent of implementation internals. Use the smallest meaningful scope that exposes the requirement or regression, preserving failure paths and resource ownership. Do not add assertions that merely mirror the code or snapshots that replace a meaningful outcome assertion. Mocked boundaries must remain explicit; neither a mock nor a fixture proves a real service, store or browser integration.

Respect existing approved project gates without inventing universal coverage thresholds or asserting that high coverage guarantees correctness. Explain the affected behavior and remaining gaps; do not weaken assertions, delete failures or increase retry counts to satisfy a number. Missing project dependencies or unavailable access are named limitations, not permission to fetch tools or contact services.

### Acceptance examples and reporting

These are prose examples, not executable cases or fixtures:

- Trigger: supplied pytest evidence shows state shared across tests. Expected action: inspect the actual fixture/resource ownership and project conventions, adding only missing lifecycle guidance if needed. No-action case: no project evidence or execution authority exists; do not generate a fixture, collect tests or reproduce the failure.
- Trigger: an identified React test asserts success before the required async UI state. Expected action: consult the actual runner/rendering tools and define an observable outcome with appropriate lifecycle handling. No-action case: versions or the component contract are unknown; do not guess APIs, install a framework or launch a browser.
- Trigger: a request seeks a universal coverage percentage. Expected action: connect meaningful confidence to actual risks and approved project gates. No-action case: no approved threshold exists; do not manufacture one or imply coverage is proof of correctness.

Report saved guidance separately from authored tests, supplied evidence, observed runs and unverified behavior. A saved recipe is not a passing test. Under this roadmap scope, create no checks, suites or fixtures; run no tests, builds, evaluations or benchmarks. Keep unrelated work/private data intact, coordinator routes unchanged, and installed caches and QMD indexes untouched. No delegation, commits/push, provider installation, publication, spending or account changes. Cloud synchronization, university RAG, training and background automation remain inactive.

Source basis: roadmap item 029 and existing QA/test-design/evaluation instructions. No project-specific recipe, framework compatibility or execution result was verified by this instruction change.
