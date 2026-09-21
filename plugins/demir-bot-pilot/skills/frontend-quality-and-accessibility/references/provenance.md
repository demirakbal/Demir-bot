# Adaptation provenance

Adapted 2026-09-21 from the previously Firecrawl-reviewed ECC copy, inspected again for this implementation. Hashes identify reviewed instructions; moving upstream URLs are not version pins or proof of current freshness. No upstream widget code, scripts or dependencies imported.

## accessibility
- Source: https://github.com/affaan-m/ECC/blob/main/skills/accessibility/SKILL.md
- Reviewed SHA-256: d8578fe750e7321658450386e2112a46ea1aedca0235fbf97f3db2457e599b3a

## frontend-a11y
- Source: https://github.com/affaan-m/ECC/blob/main/skills/frontend-a11y/SKILL.md
- Reviewed SHA-256: d09d56424592c2382ca310af0067a6de6b8d098d709ea7e5b60513cffde03756

Borrowed: native semantics, names and descriptions, keyboard operation, focus management, form feedback, meaningful alternatives, reflow and reduced-motion support.
Adapted: framework-neutral implementation that reuses the real project stack; complete interaction requirements instead of copying partial dropdown/modal examples; contextual announcements rather than every error being an alert. Added relevant loading/empty/error/retry states and conditional Figma/Sites routing.
Removed: automatic auditing/verification, blanket checklist assertions, hard-coded standards mappings and native-platform code outside this web skill. Standards-specific claims require current authoritative lookup.
Preserved: opt-in tests, no browser/build loops, no unsolicited reports, no automatic deployment or account linking, scoped source reading and deferred cloud sync.
Maintenance: compare relevant upstream changes with these fingerprints and preserve local adaptations. Saved instructions can be inspected without claiming behavior has been tested.
