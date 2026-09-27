# XCTest patterns

Original roadmap item 019 guidance. Use for explicit XCTest instruction work, a requested test review or separately authorised test creation. Reuse the parent QA workflow and [SwiftUI specialist](../../swiftui-performance-and-concurrency/SKILL.md) for isolation, state ownership and task lifetime. Do not migrate frameworks, add a new test runner or duplicate general QA guidance.

## Establish scope and the contract

Inspect relevant requirements, existing XCTest targets, source boundaries and supplied toolchain/settings. Identify unit versus integration/UI scope, real versus substituted dependencies and the behavior being asserted. Follow actual project conventions and deployment support. A request to improve this reference does not authorise creating test files, fixtures or examples that execute.

Use current official Apple documentation before prescribing version-sensitive XCTest or concurrency APIs. Without a named project or diagnostics, save reusable guidance and leave app-specific choices unresolved. Missing access does not justify running discovery builds or invoking the test runner.

## Fixture ownership and cleanup

When test creation is separately authorised, use the smallest synthetic state that exposes the requirement. Give each test a clear owner for mutable models, clocks, service substitutes and temporary resources. Avoid production credentials, shared user defaults, live Keychain, real stores or account-backed containers. An in-memory substitute does not prove disk persistence or migration behavior.

Separate per-test setup from truly immutable shared setup. Do not rely on method order, another test's cleanup or a global singleton reset that can interfere with parallel execution. Use existing injection boundaries rather than adding protocols or changing public APIs solely for convenient mocking.

Follow Apple's [setup and teardown lifecycle](https://developer.apple.com/documentation/xctest/set-up-and-tear-down-state-in-your-tests). Register scoped cleanup when acquiring a resource so a later assertion failure does not skip intended teardown. Account for partial setup, retained observers, subscriptions and tasks; teardown is not a substitute for an operation's own cancellation contract. Do not promise cleanup after process termination or delete outside the fixture's owned scope.

Keep randomness, time and external responses controlled through existing seams when they affect the contract. Preserve informative fixture names and expected values derived from requirements, not serialized private data or a copy of the implementation's calculation. This guidance describes fixtures; it creates none.

## Asynchronous behavior

Apple's [asynchronous test guidance](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations) distinguishes async test methods from expectation-based callback/delegate work. Await the operation's actual completion where supported; launching a Task and returning from the test can leave assertions or failures outside the intended lifetime.

Use expectations for a concrete observable event when required by the API. Register observation before triggering the event. Choose bounded timeouts from the operation's contract/environment, not arbitrary sleeps intended to make scheduling work. Specify expected fulfillment count and ordering only when those properties are requirements. Fulfillment alone is not proof that returned data is correct.

For async contexts, use the supported asynchronous expectation-waiting API where appropriate rather than blocking the executor needed by the callback. Consult [XCTestCase](https://developer.apple.com/documentation/xctest/xctestcase) for the actual toolchain's API contract. Apply actor isolation to the relevant test operation based on the subject's requirements; do not silence compiler errors with blanket unsafe annotations or assume every test belongs on MainActor.

For cancellation and out-of-order results, use controlled completion boundaries if authorised rather than timing races. Assert the intended state after cancellation or a newer request, and finish/cancel owned work before teardown. Cover genuine failure separately from cancellation; do not turn either into apparent success. No test code or execution is implied by describing these cases.

An inverted expectation establishes non-occurrence only during its observation window. A timeout may reflect infrastructure, missing observation or product behavior; preserve the evidence and do not simply increase timeouts, retry until green or weaken assertions. Race freedom is not proved by one passing schedule.

## Meaningful assertions

Assert the observable result or state transition specified by the requirement, including relevant error semantics and preserved data. Distinguish valid empty results, failures and unknown completion using the existing app contract. Do not merely assert non-nil, no crash or that a mock was called when the requirement concerns actual contents or side effects.

For an expected error, establish that the operation failed and that the error has the required meaning; a catch that accepts any failure can hide an unrelated defect. For unexpected errors, let the test report failure rather than swallowing them with try?. Where assertions need awaited values, obtain those values through supported async APIs before applying synchronous assertion forms as required by the actual toolchain.

Avoid overspecifying internal call order, private fields or incidental formatting unless they are contractual. Use tolerances only where the domain permits approximation and explain them. A substitute can establish consumer behavior under its scripted response, not a real server, database, security boundary or UI interaction. Keep those claims separate.

## Acceptance and reporting

Illustrative acceptance examples, not executable checks:

- **Async result:** an existing test starts callback work but returns before checking it. Identify the missing lifetime/completion boundary and required result assertion without writing or running a replacement under instruction-only scope.
- **Fixture isolation:** two tests mutate the same global service. Identify the shared ownership risk and reuse existing dependency injection for a scoped alternative; do not reset live application state.
- **Error assertion:** a test passes for any thrown error although the requirement concerns access denial. Explain the missing semantic assertion without claiming the product is broken.
- **No-action case:** existing focused tests already assert the requested contract with isolated state. Do not add redundant tests, fixtures or a framework migration to satisfy a pattern label.

Report saved instruction changes separately from any later authorised test creation and execution. Not run means not run; a source review does not establish discovery, compilation, passing assertions or regression coverage. Do not create an extra test report by default.

Source basis: official Apple resources linked above, consulted 27 September 2026. Original instructions only; no test suite, fixture or executable example imported.

Preserve instruction-only restrictions: no tests/fixtures/check creation or execution, builds, apps/simulators, profiling, benchmarks, scans, evaluations, delegation, commits, installations, package operations, cache deletion, index refreshes or background activity. Do not access accounts/credentials, alter containers, enable sync or open/copy/migrate real databases. Leave private data, installed plugin, cloud skill sync, university RAG and training unchanged.
