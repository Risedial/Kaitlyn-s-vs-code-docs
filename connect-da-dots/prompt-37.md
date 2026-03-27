# Prompt 37: Write JS — Service Worker Registration and init() Function

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `eventDelegation`
- Files that MUST already exist: `fdn-pwa/index.html`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace TWO placeholder comments in `fdn-pwa/index.html`:

**1.** Replace `// PLACEHOLDER:JS:SW-REGISTRATION` with the Service Worker registration snippet:

```javascript
// ─── Service Worker Registration ──────────────────────────────────────────
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js').catch(console.error);
}
```

**2.** Replace `// PLACEHOLDER:JS:INIT` with the initialization function:

```javascript
// ─── Application Initialization ───────────────────────────────────────────
function init() {
  buildMaps();
  navigateTab('home');
}

document.addEventListener('DOMContentLoaded', init);
```

These two Edit operations must both be completed in this step. Use the Edit tool twice — once for each placeholder.

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:SW-REGISTRATION`
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:INIT`
- File now contains `if ('serviceWorker' in navigator) {`
- File contains `navigator.serviceWorker.register('./sw.js')`
- File contains `function init() {`
- File contains `buildMaps();` inside init()
- File contains `navigateTab('home');` inside init()
- File contains `document.addEventListener('DOMContentLoaded', init);`
- No remaining `// PLACEHOLDER:JS:` comments in the file (all 11 JS placeholders replaced)

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-37"`
- `pendingSteps`: remove `"step-37"`
- `flags.swRegistrationInit`: set to `true`
