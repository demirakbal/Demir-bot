# Provider routes and current setup

## Optional visual analysis: Higgsfield

Potential operations include video_analysis_create, video_analysis_status and video_analysis_jobs. Discover current tools and schemas before use. This package neither installs Higgsfield nor establishes authentication, availability or pricing.

For a requested public YouTube analysis, video_analysis_create accepts `youtube_url`; provide exactly one source, never both youtube_url and video_input_id. An existing local upload uses the provider's supported media_upload_and_confirm workflow and returned video_input_id; do not invent IDs or upload private files under unrelated authorization. Do not route ordinary analysis into video generation or presets.

Tell the user before submitting that longer videos yield less reliable scene-by-scene analysis and short clips are more reliable (provider-required notice). The currently discovered tool does not document a clip-range input: do not invent start/end fields or claim URL timestamps restrict processing. Prefer a genuinely short supplied clip where needed.

Keep the returned analysis ID. Poll video_analysis_status with `video_analyze_id` about every 30–60 seconds, keeping the user informed; stop on completed/failed. Typical documented duration is 3–5 minutes, not a guarantee. For unusually prolonged or unchanged progress, report pending status and retain the ID rather than submitting duplicates or polling forever. On an ambiguous submission, inspect the narrow relevant existing job evidence before any retry. Do not enumerate the whole media library unnecessarily.

Inspect actual returned scenes/fields before reasoning. No assumed timestamps, full transcription, OCR fidelity or frame URLs: the scene payload schema is not fixed in the exposed description. If frames are supplied and inspectable, inspect the relevant ones. If only scene descriptions are returned, label conclusions as provider analysis. Missing speech detail needs a transcript; missing visuals cannot be repaired by a fabricated scene description.

## Spoken content: captions/transcript

Prefer a currently available supported transcript tool or the public video's Show transcript interface through available browser controls when relevant. Caption retrieval is task work, not a browser test campaign. Discover actual controls/API before acting; follow tool instructions. Firecrawl is appropriate for source discovery and accessible public page text, but a successful YouTube page scrape is not evidence it returned captions. Match third-party transcripts to video identity and disclose provenance; third-party summaries remain secondary evidence.

If captions are absent/blocked, state it. Use an already available and authorized transcription/video route only when it actually exposes speech, or ask for the transcript/clip. Do not install or run a spoofed private API client, proxy rotation, cookie extraction or an unreviewed downloader to get around denial. A supplied transcript is sufficient for speech-only analysis; label it transcript-based.

## Not bundled

Watch Skill/DeepWatch, its frame/OCR/Whisper/index runtimes, TranscriptAPI account, and youtube-digest extraction script. Use existing Higgsfield tooling only when available and authorized. Local-only full video perception is not implemented; do not claim offline watching. A future request specifically needing local processing would require scoped dependency/data-flow assessment and setup. No default server, watcher, browser capture or self-correction loop.
