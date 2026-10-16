# Coverage and requirement bullets

Use this guide during a substantial project interview. It is a gap prompt, not a compulsory questionnaire or a source of preapproved features.

## Explore only relevant dimensions

- **People and purpose:** primary and secondary users, conflicting needs, current workarounds, frequency, consequences, success, exclusions and decision owner.
- **Journeys:** entry trigger, prerequisites, steps, decisions, completion, interruption/resume, cancellation, undo and recovery; walk one actual example before generalizing.
- **Roles and permissions:** who may view/change/share what, ownership, unauthorized attempts, collaboration and isolation. Do not assume multiple users are needed.
- **Information:** source of truth, required/optional fields, missing versus invalid values, duplicates, editing/deletion, import/export, retention and portability.
- **Time and state:** deadlines and timezones, ordering, status transitions, repeated actions, conflicts, concurrent edits and stale information where relevant.
- **Integrations and availability:** external dependencies, unavailable access, partial failure, retries and offline needs; an installed connector is not evidence of working access.
- **Interaction and accessibility:** device/context, navigation, feedback, mistakes, input needs and concrete user tasks; ask about visual preferences after understanding outcomes.
- **Notifications:** whether needed, trigger, recipient, channel, timing, duplicates, quiet periods, opt-out and failure handling; no messaging is authorized by discussing it.
- **Quality and operations:** privacy/security expectations, performance workload and limits, reliability/recovery, supported environments, cost/capacity and maintenance responsibility. Leave unknown targets open.

For each relevant area distinguish explored, unresolved and deliberately deferred/out-of-scope. A missing answer is not evidence the feature is unnecessary. Revisit earlier decisions when new answers invalidate them; explain the change. Do not produce synthetic precision or completion percentages.

## Atomic bullet form

Use a compact bullet with labelled fields; separate behaviors into separate IDs. The following is a format, not a requirement to fill unknown facts:

- **FR-xxx — [Short label].** When [condition], [actor/system] shall [single behavior] with [observable result]. **Source/rationale:** [user decision or evidence and underlying need]. **Priority/status:** [agreed priority; proposed/confirmed/deferred]. **Acceptance:** [Given/When/Then or input and expected result, including agreed boundary]. **Verification:** [appropriate method]. **Dependencies/open issues:** [IDs/questions, if any].

Keep requirements in bullets even when a separate overview table helps. Do not combine save, notify and synchronize into one obligation. Distinguish an acceptance example from complete boundary coverage. Define terms once and refer back to them. Use quality IDs such as NFR-xxx for measurable quality obligations without forcing a new scheme on an existing project.

Illustrative only, not a confirmed university-hub requirement:

- **FR-012 — Cancel deadline edit.** When a student cancels an unsaved assignment deadline edit, the system shall preserve the previously saved deadline. **Source/rationale:** fictional interview decision; avoid accidental changes. **Priority/status:** proposed, priority unresolved. **Acceptance:** Given saved deadline A, when the student enters B and cancels, reopening the assignment displays A. **Verification:** system/acceptance scenario; unit coverage may support the underlying state behavior. **Open issue:** how navigation away from the form differs from explicit cancellation.

Reuse [requirement quality](../../requirements-and-traceability/references/requirements.md#requirement-quality) for further specification checks and [traceability](../../requirements-and-traceability/references/traceability.md) only when linking actual downstream artifacts. A planned verification method is not an existing test or a passed result.
