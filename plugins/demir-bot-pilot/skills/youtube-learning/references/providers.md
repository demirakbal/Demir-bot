# Provider routes and current setup

## Optional visual analysis: Higgsfield

Potential operations include video_analysis_create, video_analysis_status and video_analysis_jobs. Discover current tools and schemas before use. This package neither installs Higgsfield nor establishes authentication, availability or pricing.

For a requested public YouTube analysis, video_analysis_create accepts `youtube_url`; provide exactly one source, never both youtube_url and video_input_id. An existing local upload uses the provider's supported media_upload_and_confirm workflow and returned video_input_id; do not invent IDs or upload private files under unrelated authorization. Do not route ordinary analysis into video generation or presets.

Tell the user before submitting that longer videos yield less reliable scene-by-scene analysis and short clips are more reliable (provider-required notice). The currently discovered tool does not document a clip-range input: do not invent start/end fields or claim URL timestamps restrict processing. Prefer a genuinely short supplied clip where needed.

Keep the returned analysis ID. Poll video_analysis_status with `video_analyze_id` about every 30–60 seconds, keeping the user informed; stop on completed/failed. Typical documented duration is 3–5 minutes, not a guarantee. For unusually prolonged or unchanged progress, report pending status and retain the ID rather than submitting duplicates or polling forever. On an ambiguous submission, inspect the narrow relevant existing job evidence before any retry. Do not enumerate the whole media library unnecessarily.

Inspect actual returned scenes/fields before reasoning. No assumed timestamps, full transcription, OCR fidelity or frame URLs: the scene payload schema is not fixed in the exposed description. If frames are supplied and inspectable, inspect the relevant ones. If only scene descriptions are returned, label conclusions as provider analysis. Missing speech detail needs a transcript; missing visuals cannot be repaired by a fabricated scene description.

## Spoken content: captions/transcript

Prefer a currently available supported transcript tool or the public video's Show transcript interface through available browser controls when relevant. Caption retrieval is task work, not a browser test campaign. Discover actual controls/API before acting; follow tool instructions. Firecrawl is appropriate for source discovery and accessible public page text, but a successful YouTube page scrape is not evidence it returned captions. Match third-party transcripts to video identity and disclose provenance; third-party summaries remain secondary evidence.

### Bounded transcript recovery

For a timeout, empty result, stalled loading panel, or an ambiguous exporter message such as “No transcript is available,” make up to **two recovery attempts after the initial attempt** (three retrieval attempts total for the same video in the current task). Reuse the attempt count across tools and turns; changing routes does not reset it. These are bounded read-only retrieval steps within the video task, not an authorization for browser testing, installation or access changes.

1. **First recovery:** inspect the public page. If Show transcript is available, open it and use the browser’s supported readiness check or a brief bounded wait for caption rows. Retry the supported transcript export, or read the displayed transcript. Discover the actual tool API before calling it; do not assume a method exists.
2. **Second recovery:** if the result is still ambiguous, reload once or open one fresh tab for the same video in the selected browser. Reopen the transcript panel and retry retrieval. Inspect relevant visible errors when available. Do not repeat identical calls without a recovery step, poll a spinner indefinitely, or reset the budget by switching providers.
3. **Stop on success:** confirm nonempty transcript content matches the video, inspect timestamp coverage, and retain returned language and caption-generation metadata. Reuse the retrieved content; do not fetch it again unnecessarily.

Stop early for an explicit access denial, authentication/CAPTCHA barrier, rate limit, or clear page-level confirmation that captions are absent. Do not bypass restrictions or automatically change accounts. A visible Show transcript button conflicts with an exporter’s absence message; treat that combination as unresolved retrieval, not proof of missing captions. The button alone also does not prove that captions have loaded.

After the bounded attempts fail, report “I could not retrieve the transcript in this session,” with the observed failure and attempts made. Claim captions are absent only with supporting source evidence. If captions are confirmed absent or access is blocked, state that specific limitation. Follow the blocked-source choice below instead of producing an alternative deliverable.

### Blocked-source choice

A request for notes from a particular video authorizes notes grounded in that video. When the required speech or visual evidence cannot be obtained, stop drafting or generating the requested artifact. Ask one concise question offering relevant available choices, and wait for the answer before dependent work. If the user has already selected a fallback explicitly, follow that scope without asking again. Silence or elapsed time is not a choice; leave the task blocked rather than creating a substitute.

Possible choices (offer only those relevant to the actual blocker):
- Stop/cancel the task without creating notes.
- Continue once the user supplies the missing transcript or clip.
- Try an available alternative route for the **same video**, such as Firecrawl to locate accessible transcript text, or a speech-capable transcription provider. Explain what the route can actually retrieve; do not promise success or bypass a denial. A user-approved new attempt has a stated bounded scope, not unlimited retries.
- Create **substitute topic notes** from different videos or other sources, but only after the user explicitly chooses that changed scope. Use Firecrawl for source discovery/extraction and `demir-bot-pilot:deep-research-and-idea-validation` when substantial research or corroboration is warranted. Identify the replacement sources and do not attribute their content to the original video.

Firecrawl and the research skill can support YouTube learning, but neither makes a description, search snippet or third-party summary equivalent to the video's transcript. Within the original task, focused source discovery and necessary factual corroboration remain appropriate; they must not turn into an unrequested alternative lesson. After the retrieval stop condition, do not begin new fallback research or provider jobs while waiting for the user's choice. Do not create even a clearly labeled companion PDF, summary or partial substitute merely to return an artifact.

Do not install or run a spoofed private API client, proxy rotation, cookie extraction or an unreviewed downloader to get around denial. A supplied transcript is sufficient for speech-only analysis; label it transcript-based. Visual analysis remains appropriate when the task needs it, but is not an automatic substitute for unavailable speech.

## Not bundled

Watch Skill/DeepWatch, its frame/OCR/Whisper/index runtimes, TranscriptAPI account, and youtube-digest extraction script. Use existing Higgsfield tooling only when available and authorized. Local-only full video perception is not implemented; do not claim offline watching. A future request specifically needing local processing would require scoped dependency/data-flow assessment and setup. No default server, watcher, browser capture or self-correction loop.
