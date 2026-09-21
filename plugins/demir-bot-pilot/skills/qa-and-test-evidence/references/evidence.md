# Execution and coverage evidence

Ordinary output: command, revision/state, result, behavior assessed, limitations. Formal record:

`requirement/revision | test ID/assertion | run ID | actor | fixture/preconditions | level and mocked/real boundary | command/steps | expected | actual | status | environment/date | evidence | defect/retest`

Use planned, not implemented, not run, blocked, passed, failed, explicitly waived and excluded accurately. Retain historical runs with a latest-status view. Do not fabricate participants, approvals, dates or evidence paths. A plan, filename, screenshot, lint pass or green quality gate is not execution proof. If actual results contradict a required step, flag failure or a documented approved requirement change.

Separate code coverage, mapped requirements, assertion coverage, executed verification and acceptance. Record numerator/denominator, eligible scope, revision and justified exclusions. For 102 total requirements with 4 excluded, eligible count is 98; exclusions are not passes. Unknown numerator is unknown; zero eligible means N/A. Multiple requirements need corresponding assertions, not a shared filename.

For line/branch/function coverage inspect report generation/import, source/test classification and matching revision. Missing reports differ from measured zero. Comparable before/after scans require matching tool/version, rules, scope and exclusions. Do not weaken gates or exclusions to improve metrics. High coverage can coexist with weak assertions.

For relevant detailed course examples, resolve the active private profile and read course-evidence/qa-and-test-evidence/references/evidence.md. Generalize unique acceptance IDs, identifiable personas, comparable baselines and honest failed/retest states; never copy course-specific stacks or limits.
