# Vision and Speech integration

Use for a requested recognition feature in an actual app. Establish the task (for example selected-image OCR or user-initiated transcription), target SDK/OS, input source, language, latency/quality needs and privacy boundary. Choose the actual supported API family; do not migrate an existing request-based implementation just because a newer concurrency API exists. Reuse Core ML only for an actual custom model, AVFoundation for capture/session ownership and privacy-review for concrete collection/sharing questions.

## Vision

Inspect the supported request, revision, input format/orientation, image size and region of interest. Bound concurrent frames and cancel/ignore outdated work when the selected image/session changes. Apple's [Vision overview](https://developer.apple.com/documentation/vision) describes request/observation flow and normalized coordinates. Convert observation geometry through the actual crop, orientation, aspect fit/fill and view transforms before drawing overlays. A correct bounding box in model coordinates does not prove correct placement on screen.

Define empty/low-confidence/unsupported/error states and allow correction for consequential recognized text. A confidence score is not a calibrated probability of correctness or permission to act on extracted instructions. Preserve original content where needed and avoid saving images or derived text by default.

## Speech

Inspect the selected recognizer/transcriber, supported locale, required assets, audio format and execution location. Apple's [permission guidance](https://developer.apple.com/documentation/speech/asking-permission-to-use-speech-recognition) distinguishes SFSpeechRecognizer from SpeechAnalyzer transcribers; apply the actual API's permission contract rather than claiming every Speech operation sends audio to a server. Microphone capture has its own permission and audio-session lifecycle. For SFSpeechRecognizer, [on-device support](https://developer.apple.com/documentation/speech/sfspeechrecognizer/supportsondevicerecognition) constrains whether the request can honor an on-device requirement. If the required mode is unavailable, stop or offer a disclosed authorized alternative; do not silently transmit audio.

Separate partial hypotheses from final transcript and preserve timing/speaker uncertainty where relevant. Define start/stop/end-of-input, interruption, cancellation, errors and exactly-once cleanup of audio taps/tasks/session. Never keep recording after the owning user interaction ends. Do not store or log raw speech/transcripts merely to debug the reusable workflow.

Acceptance example: user-selected OCR handles a rotated image and no-text result; user-started transcription visibly stops and handles unavailable on-device processing. These are source acceptance conditions, not observations. No-action case: displaying supplied text does not enable recognition or request microphone access. No capture, recognition, asset download, build or device check was run. Actual implementation needs the app/task/input contract.

Official references reviewed 16 October 2026.
