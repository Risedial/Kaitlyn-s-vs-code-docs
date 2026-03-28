# Prompt 39: Verify manifest.json — Validate PWA Installability Requirements

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `manifestWritten`
- Files that MUST already exist: `fdn-pwa/manifest.json`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Validate `fdn-pwa/manifest.json` against the PWA installability requirements and repair any issues found.

**Step 1 — Parse JSON validity.**
```python
import json
with open('fdn-pwa/manifest.json') as f:
    manifest = json.load(f)
print("JSON valid:", True)
print("Keys:", list(manifest.keys()))
```
If this fails with a JSON error, the manifest has a syntax error — use the Write tool to rewrite it correctly per the prompt-02 specification.

**Step 2 — Check required fields.**
Verify all of the following keys exist and have correct values:
- `name` = `"FDN Symptom Navigator"`
- `short_name` = `"FDN Nav"`
- `display` = `"standalone"`
- `start_url` = `"./"`
- `scope` = `"./"`
- `orientation` = `"portrait-primary"`
- `theme_color` = `"#000000"`
- `background_color` = `"#000000"`
- `categories` contains `"medical"`, `"health"`, `"productivity"`
- `icons` is an array with exactly 2 entries

**Step 3 — Validate icons.**
For each icon entry:
- `src` must start with `"data:image/png;base64,"` — NOT a placeholder string
- `sizes` must be `"192x192"` and `"512x512"` respectively
- `type` must be `"image/png"`
- `purpose` must be `"any maskable"`

**Step 4 — Validate icon base64 is a real PNG.**
```python
import base64, struct
for icon in manifest['icons']:
    b64 = icon['src'].split(',', 1)[1]
    data = base64.b64decode(b64)
    assert data[:4] == b'\x89PNG', f"Not a PNG: {icon['sizes']}"
    print(f"Icon {icon['sizes']}: valid PNG ({len(data)} bytes)")
```
If the icons are not valid PNGs, return to prompt-02 and regenerate them using the Python PNG generation script.

**Step 5 — Check for external URLs.**
```bash
grep -n "http" fdn-pwa/manifest.json
```
Expected: 0 matches. No external URLs allowed.

**Step 6 — Report result.**
Output: "manifest.json PASS" or list of failures.

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/manifest.json` parses as valid JSON
- All 10 required fields are present with correct values
- Both icons have valid base64 PNG data URIs (not placeholder text)
- `display` is exactly `"standalone"`
- Zero external URLs in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-39"`
- `pendingSteps`: remove `"step-39"`
- `flags.manifestVerified`: set to `true`
