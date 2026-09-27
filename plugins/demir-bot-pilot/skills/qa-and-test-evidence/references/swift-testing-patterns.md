# Swift Testing patterns

Original roadmap item 020 guidance. Use for explicit Swift Testing instruction work or authorised work in a project that supports it. Reuse [XCTest patterns](xctest-patterns.md) for requirement-derived assertions, isolated synthetic state, cleanup ownership and honest evidence; translate concepts rather than copying XCTest lifecycle APIs into another framework. Reuse the [SwiftUI specialist](../../swiftui-performance-and-concurrency/SKILL.md) for actual actor isolation and task lifetime.

## Establish compatibility and value

Inspect the existing test target, imports, toolchain, deployment settings and relevant test conventions as source. Distinguish installed compiler support from the project's actual runner/discovery and CI configuration. Do not invoke builds or runner discovery merely to establish support. If evidence is missing, name it and keep the implementation recommendation provisional.

Preserve working XCTest coverage. Choose Swift Testing for a concrete benefit in the requested scope, not novelty. Consult Apple's current [migration guidance](https://developer.apple.com/documentation/testing/migratingfromxctest) before mixing assertions, lifecycle assumptions or interoperability features; their availability is toolchain-dependent. Do not imply that translating macros preserves fixture lifecycle, scheduling or test discovery. Retain existing framework-specific UI/performance workflows unless replacement is separately requested and supported.

## Parameterisation

Use [parameterised tests](https://developer.apple.com/documentation/testing/parameterizedtesting) when several inputs exercise the same behavioral contract. Each case needs a meaningful input and independently derived expected outcome; avoid a loop that conceals which case failed. Keep distinct behaviors separate when one parameterised function would require unrelated branches.

Decide whether multiple collections represent every combination or intentionally paired inputs. Check the actual API's combination semantics before choosing the argument representation; do not accidentally multiply cases or silently truncate paired data. Keep argument construction deterministic, bounded and free of network, database or credential access. Discovery should not create live resources as a side effect.

Preserve case identity and useful diagnostic descriptions without exposing secrets. An empty argument collection is not evidence of coverage. Parameterisation reduces repetition, not the need for meaningful boundaries, invalid inputs and justified expected results. This instruction task creates no case data or fixtures.

## Traits and assertions

Use supported [traits](https://developer.apple.com/documentation/testing/traits) for an explicit purpose: grouping, relevant conditions, known constraints or bounded execution. A disabled/skipped test is not passing coverage. Record the reason and unresolved requirement; do not disable a failing test or mark a real regression expected merely to produce a green result. Distinguish a runtime condition from compile-time availability requirements.

Choose #expect for an observable condition and #require when continuing without the prerequisite would be meaningless or unsafe, using the supported API contract. Apple's [expectation guidance](https://developer.apple.com/documentation/testing/expectations) distinguishes continued execution from a thrown requirement failure. Preserve error semantics and data assertions; do not replace a precise XCTest assertion with a weaker non-nil or any-error condition during an authorised conversion.

Time limits bound execution, not prove performance. Tags, issue references and traits do not themselves establish test quality or CI selection. Do not install a helper library merely because an example uses it.

## Concurrency and lifecycle

Apple documents [parallel execution by default](https://developer.apple.com/documentation/testing/parallelization). Treat mutable global state, shared files, service singletons and process-wide settings as potential cross-case interference. Use independently owned state and the existing dependency-injection boundaries. A separate suite instance does not isolate a global dependency.

The serialized trait controls the relevant suite's contained tests or a parameterised function's cases; it does not exclude unrelated tests. Do not treat it as a process-wide lock or promise a fixed execution order. Prefer removing unjustified sharing; use serialisation only for a demonstrated requirement with its remaining scope limits explicit.

Await the real asynchronous operation and preserve its actor requirements. Do not use arbitrary sleeps, block an executor waiting for its own callback, or spawn unowned work that outlives the test. An actor-isolated test is not automatically a serial suite across suspension points. Do not add blanket MainActor or unsafe annotations merely to silence diagnostics.

For event/callback assertions, consult the actual supported confirmation or async API contract. Do not mechanically translate XCTest expectations: determine whether the selected API waits or checks events within an awaited scope. Ensure the operation's lifecycle includes the event being assessed, with explicit count/order only where contractual. Reuse cancellation and stale-result principles without launching races to discover behavior.

Use supported suite initialisation and explicitly owned cleanup rather than assuming XCTest setUp/tearDown methods run. Account for failed setup, thrown requirements and asynchronous resource release. A synchronous destructor or defer cannot be assumed to perform awaited cleanup. Do not migrate live stores, alter global account state or create fixtures under instruction-only authority.

## Acceptance and reporting

Illustrative acceptance examples, not executable checks:

- **Parameterisation:** repeated examples share a contract but have paired expected values. Propose identifiable bounded cases that preserve pairing, not an unintended Cartesian product.
- **Concurrency:** a serialized suite and an unrelated suite both mutate a singleton. Explain the remaining shared-state risk; do not claim the trait guarantees global isolation.
- **Traits:** an existing test is disabled without an applicable requirement. Describe the lost coverage and missing rationale; do not quietly count it as passed or change it under review-only scope.
- **No-action case:** existing XCTest coverage is adequate and the project has no supported migration need. Retain it; do not introduce Swift Testing merely because it exists.

Report saved instructions separately from test creation, discovery, compilation and execution evidence. A source review or trait declaration does not prove passing tests, race freedom or preserved coverage. No extra test report is implied.

Source basis: official Apple resources linked above, consulted 27 September 2026. Original guidance; no test suite, fixture or executable sample imported.

Preserve instruction-only restrictions: no test suites, fixtures, checks, tests, builds, apps/simulators, profiling, benchmarks, scans, evaluations, delegation, commits, package operations, installations, cache deletion, index refreshes or background activity. Do not access accounts/credentials, alter containers, enable sync or open/copy/migrate real databases. Leave private data, installed plugin, cloud skill sync, university RAG and training unchanged.
