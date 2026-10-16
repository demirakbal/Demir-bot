# Target-specific mobile extension contract

Use for a named Android, React Native, Flutter, Compose Multiplatform or Apple app feature. Inspect actual repository targets/manifests/dependency locks and supported OS/device matrix first; framework presence does not prove native capability parity. Do not migrate a SwiftUI app or create a second app just to use this guide.

| Target | Establish before implementation | Preserve and return |
| --- | --- | --- |
| Android/native Compose | Actual app/modules, Android/plugin/Kotlin/dependency versions, lifecycle and permission requirements | State/lifecycle ownership, process death/restoration, navigation, persistence and cancellation; actual device/runtime evidence separately. |
| React Native | Actual framework/native module versions, platform targets and JS/native bridge ownership | Platform-specific permissions, async/event/subscription cleanup, error/cancellation and native fallback; no assumption every dependency works on both OSes. |
| Flutter | Actual SDK/platform targets, package versions and plugin support | Widget/state/disposal and async ownership, native plugin boundary, accessibility and fallback behavior. |
| Compose Multiplatform | Actual shared/platform source sets and supported toolchain/targets | Shared business/data contracts versus platform lifecycle/permissions/interop; no blanket Android/iOS parity claim. |
| SwiftUI/Apple | Actual Xcode/Swift/OS targets, app/extensions, persistence and concurrency settings | Reuse existing SwiftUI, navigation, persistence/migration, privacy and QA references; do not duplicate them here. |
| On-device models | Actual model license/artifact, OS/device support, preprocessing and task need | Availability/resource/privacy constraints and disclosed fallback; training, downloads and provider setup remain separate. |

For the selected feature, trace user action and data across UI/state, domain/data boundary and native platform APIs. Define supported input/output and error states, cancellation, background/foreground transitions, resource/session disposal, offline behavior and durable-state migration only where the real requirement needs them. Private data and permission prompts stay with the platform/account owner. Avoid storing tokens/raw personal data in sample logs or committing target credentials.

Select the existing stack's official versioned documentation for changed APIs. Implement only the actual target and necessary compatibility adapter; document unsupported platforms or missing native plugins rather than inventing behavior. Shared UI or a successful build on one platform is not evidence for every target. Testing/device launches/builds remain separately scoped; platform instructions do not trigger them.

Expected example, not a run: a selected cross-platform sensor feature declares each native permission and subscription lifecycle, handles unavailable sensors, and returns a disclosed unsupported state on an unimplemented target. No-action case: an existing SwiftUI navigation fix does not create Android/Flutter apps. No mobile app/target was selected by this item; reusable procedure is saved, project implementation and device proof remain pending.
