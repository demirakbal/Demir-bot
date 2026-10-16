# Versioning and private release management

Use the canonical development source, stable plugin identity `demir-bot-pilot` and the existing selected registration. Both manifests currently declare 0.1.1. Do not create a second plugin to publish an update, patch an installed cache or treat a local refresh as a public release. The roadmap owns item-by-item scope/evidence; CHANGELOG.md summarizes user-visible source changes.

## Version decision

For an authorized release, choose a version from the actual compatibility impact: major for deliberately incompatible user/setup contracts, minor for compatible capability additions, patch for compatible corrections. While the private pilot remains pre-1.0, explicitly describe breaking changes rather than assuming a 0.x label makes them harmless. A host-specific cachebuster identifies a refresh only where its supported flow requires one; it is not a substitute for user-facing release notes or behavioral proof. Update corresponding manifest versions consistently when a version change is actually authorized.

Keep the current batch under Unreleased until an actual candidate/version is selected. Record exact source revision or snapshot, package identity, applicable host/support envelope, changed behavior, known limitations, migration/recovery implications and evidence states. Distinguish source prepared, candidate packaged, locally installed, newly discovered, indexed, operation-observed and publicly released. Do not create a tag or release date for an unperformed publication.

## Candidate, migration and recovery

Freeze the selected scope and artifact identity before acceptance review. Preserve a usable prior source/artifact locator and existing configuration/profile ownership. Inspect changed loader paths, routes, metadata, dependency contracts and supported host behavior; prefer a documented narrow migration over silently resetting settings. Never bundle a private profile as a migration convenience. Required unrun gates leave the candidate unconfirmed, not accepted.

Local rollback reverses only the implicated source/version change while preserving subsequent work; installed-cache rollback needs its own supported refresh and evidence. QMD entries, native project profiles, cloud copies, website and exported PDF have independent states. Do not infer that reverting Git changes an index or remote distribution. Preserve uncertain external outcomes; a local failure cannot prove an upload was rejected. Public rollout, tagging, uploading, spending and account changes require their actual operation scope.

## Release-note content and issue triage

Use: version/candidate/date state; concrete user-visible changes; required compatibility/migration actions; evidence performed versus unrun; known issues/blockers; precise install/rollback pointers. Link the relevant roadmap record instead of copying all item text. A useful issue names host/version/candidate, expected versus actual outcome, minimal sanitized reproduction and evidence. Do not request credentials, private profiles, full transcripts or raw account data. Security reports follow the selected private reporting policy; no public contact is invented here.

Acceptance example: a later approved candidate references the exact package and unrun runtime gates, offers a compatible update path and does not claim “released” from a saved changelog. No-action case: writing release guidance does not bump versions, reinstall, push, tag or publish. This policy and the Unreleased notes are source deliverables only; no release candidate or migration was executed.
