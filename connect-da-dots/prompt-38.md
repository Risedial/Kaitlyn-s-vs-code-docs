# Prompt 38: Integration Assembly — Final index.html Verification and Cleanup

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `swRegistrationInit`
- Files that MUST already exist: `fdn-pwa/index.html`, `fdn-pwa/manifest.json`, `fdn-pwa/sw.js`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Perform a comprehensive final assembly check on `fdn-pwa/index.html` to verify all sections are correctly integrated.

**Step 1 — Check for any remaining placeholder strings.**
Use the Bash tool:
```bash
grep -c "PLACEHOLDER:" fdn-pwa/index.html
```
Expected result: **0**. If any PLACEHOLDER strings remain, identify which prompt step was skipped and return to run it.

**Step 2 — Verify all required HTML structure elements.**
Confirm the following are present in `fdn-pwa/index.html`:
- `<!DOCTYPE html>` — line 1
- `<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">`
- `<meta name="apple-mobile-web-app-capable" content="yes">`
- `<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">`
- `<link rel="manifest" href="./manifest.json">`
- `<style>` block containing `:root {`
- `<nav class="tab-bar"` with 3 tab buttons
- `<div id="bottom-sheet"` with class `bottom-sheet`
- `<script>` block containing `const DATA = {`
- `if ('serviceWorker' in navigator) {`
- `function init() {`
- `document.addEventListener('DOMContentLoaded', init);`

**Step 3 — Verify script order.**
The script block must have content in this exact order:
1. `const DATA = {` (DATA object)
2. `if ('serviceWorker' in navigator)` (SW registration)
3. `const state = {` (state object)
4. `function buildMaps()` (maps builder)
5. `function el(` (DOM helper)
6. `function openSheet(` / `closeSheet(` / `pushSheet(` / `popSheet(` (sheet management)
7. `const CATEGORY_ORDER` and `function renderHome(`
8. `function renderSymptom(`
9. `function renderVariable(`
10. `function renderCluster(`
11. `function renderSearch(`
12. `function navigateTab(` and `function renderScreen(`
13. `document.addEventListener('click',` (event delegation)
14. `function init(` and `document.addEventListener('DOMContentLoaded', init)`

If the order is incorrect (e.g., a render function references `el()` before it is defined), use the Edit tool to reorder the sections in the script block.

**Step 4 — Run a syntax check.**
Use the Bash tool to run Python to check for obvious JS syntax errors (mismatched braces):
```python
import re
content = open('fdn-pwa/index.html').read()
# Extract script content
script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if script_match:
    script = script_match.group(1)
    opens = script.count('{')
    closes = script.count('}')
    print(f"Open braces: {opens}, Close braces: {closes}, Balance: {opens - closes}")
```
If the brace count is significantly imbalanced (more than ±5), there may be a truncation error in one of the data batches.

**Step 5 — Check for innerHTML with dynamic strings.**
```bash
grep -n "innerHTML" fdn-pwa/index.html
```
Expected: 0 matches. If innerHTML is found, identify the location and refactor to use `el()` and `txt()`.

## Verification
Before updating state.json, Claude MUST confirm:
- Zero PLACEHOLDER strings remain in `fdn-pwa/index.html`
- All 12 required HTML structure elements are present
- Script block order is correct (DATA → SW registration → state → helpers → renders → events → init)
- JavaScript brace balance is within ±5 (near-zero imbalance)
- Zero `innerHTML` with dynamic string construction

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-38"`
- `pendingSteps`: remove `"step-38"`
- `flags.integrationAssembly`: set to `true`
