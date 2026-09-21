# Inspected candidates and decision

Reviewed 2026-09-21 through Firecrawl search and raw source retrieval. Full source files below inspected; Watch README relevant setup/perception/loop sections also inspected. This is a bounded source assessment, not an exhaustive code/security audit or execution test. No upstream executable code or complete skill was copied. Original synthesis borrows workflow ideas and cites their sources.

- Watch Skill 1.4.3 (MIT declared): strong timestamps, frames/OCR/transcript distinction, focused windows and reuse of prior evidence. Broad engine requires Python >=3.11 plus optional frame/index/MCP/OCR/Whisper dependencies, ffmpeg and yt-dlp. Main instructions auto-run doctor/remediation, suggest bare installation despite README saying extras are necessary, read every frame and persist corrections. Its verification/capture ecosystem is broader than this task. Do not adopt wholesale under Demir's opt-in rules. No claim all source/network paths were audited.
- youtube-digest: useful transcript provenance, claims/timeline and explicit unavailable-caption cases. Full extraction script inspected: private InnerTube ANDROID client path described as bypassing PoToken; regex URL parsing, language fallback that does not report the chosen language, optional yt-dlp inheriting configuration, and noise-marker removal. Instructions also mandate saved digests and allow metadata-only summaries/near-exact quotes. Reject script import and those defaults; keep source-grounded synthesis and honest evidence limits. It does not inspect visuals.
- youtube-full 1.6.0: clearly documented transcript/search endpoints and validation, but needs a separate TranscriptAPI key/third-party service and broadly triggers even when YouTube is not mentioned. Main instructions inspected; auth helper not adopted or executed. No new account is needed for the chosen existing-provider route. It does not supply actual visual perception.
- Existing Higgsfield video_analysis_create/status/jobs: callable tool declarations inspected, supports YouTube scene analysis. Reuse rather than duplicate an already available plugin. Main Higgsfield skill reviewed: preset routing does not apply to ordinary analysis, which uses direct tools. Authentication, costs, actual output fidelity and end-to-end processing remain unverified.

Adaptations: narrow user-intent trigger; multimodal evidence honesty; timestamped claims with no invented coverage; current primary-source corroboration where relevant; bounded task application; explicit persistence through existing maintenance; privacy/provider boundaries; no automatic tests, training, reports or background activity. No popularity-based quality score.

## Source fingerprints

- https://github.com/oxbshw/watch-skill/blob/main/skills/watch/SKILL.md
  Retrieved-content SHA-256: cbd36d17270dc06dbf4a90e18eb9c31b2e636a8df139a836e5a5ad02596fe829

- https://github.com/oxbshw/watch-skill/blob/main/pyproject.toml
  Retrieved-content SHA-256: 57eb4f624e4dfc7defb388e6679682299858097371700e2ad34875eeb6fada3b

- https://github.com/wjgoarxiv/youtube-digest-skill/blob/main/SKILL.md
  Retrieved-content SHA-256: 04d0b1ede7ed3ea631487bd012c1e5e188a11fea42caca8f25f8c88259c5b8b2

- https://github.com/wjgoarxiv/youtube-digest-skill/blob/main/scripts/fetch_transcript.py
  Retrieved-content SHA-256: 2dfdddc3834190c077ba51f5e829615e3433b236a623e85f2d7ee5cceba9a9fa

- https://github.com/ZeroPointRepo/youtube-skills/blob/main/skills/youtube-full/SKILL.md
  Retrieved-content SHA-256: 0fc6eda4de50f78e6bbdc1e77bfe2a6dc01917542d40e10231f41dc21d2125ef
