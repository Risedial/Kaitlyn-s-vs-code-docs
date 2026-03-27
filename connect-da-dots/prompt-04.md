# Prompt 04: Write HTML Document Shell — DOCTYPE, Head, Body Skeleton with All Placeholders

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `initialized`
- Files that MUST already exist: `fdn-pwa/index.html` (stub from step-01)

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Write tool to overwrite `fdn-pwa/index.html` with the complete HTML document shell shown below. This shell contains NO real CSS or JavaScript — only the structural skeleton with uniquely-named PLACEHOLDER comments. Subsequent prompts (05–37) will use the Edit tool to replace each placeholder with its actual content.

**CRITICAL**: Every placeholder comment string must appear EXACTLY ONCE in the file and must match the text used in subsequent prompts. Do not rename, reorder, or duplicate any placeholder.

Write this exact file content to `fdn-pwa/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="FDN Nav">
  <meta name="theme-color" content="#000000">
  <title>FDN Symptom Navigator</title>
  <link rel="manifest" href="./manifest.json">
  <style>
/* PLACEHOLDER:CSS:DESIGN-TOKENS */
/* PLACEHOLDER:CSS:BASE-RESET */
/* PLACEHOLDER:CSS:LAYOUT */
/* PLACEHOLDER:CSS:HEADER */
/* PLACEHOLDER:CSS:TAB-BAR */
/* PLACEHOLDER:CSS:LIST-ROWS */
/* PLACEHOLDER:CSS:PILLS-TAGS */
/* PLACEHOLDER:CSS:BOTTOM-SHEET */
/* PLACEHOLDER:CSS:ALERT-SEARCH */
/* PLACEHOLDER:CSS:ANIMATIONS */
  </style>
</head>
<body>
  <div id="app">
    <div id="screen-container"></div>
    <nav class="tab-bar" role="tablist" aria-label="Main navigation">
      <button class="tab-item" role="tab" aria-selected="true" data-action="navigate-tab" data-tab="home">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
        <span>Home</span>
      </button>
      <button class="tab-item" role="tab" aria-selected="false" data-action="navigate-tab" data-tab="search">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
        <span>Search</span>
      </button>
      <button class="tab-item" role="tab" aria-selected="false" data-action="navigate-tab" data-tab="clusters">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
        <span>Clusters</span>
      </button>
    </nav>
    <div id="bottom-sheet-overlay" class="bottom-sheet-overlay" data-action="close-sheet" aria-hidden="true"></div>
    <div id="bottom-sheet" class="bottom-sheet" role="dialog" aria-modal="true" aria-label="Detail view" aria-hidden="true">
      <div class="sheet-drag-indicator" aria-hidden="true"></div>
      <div id="sheet-content" class="sheet-content"></div>
    </div>
  </div>
  <script>
// PLACEHOLDER:JS:DATA-SKELETON
// PLACEHOLDER:JS:SW-REGISTRATION
// PLACEHOLDER:JS:STATE-MACHINE
// PLACEHOLDER:JS:NAVIGATE
// PLACEHOLDER:JS:RENDER-HOME
// PLACEHOLDER:JS:RENDER-SYMPTOM
// PLACEHOLDER:JS:RENDER-VARIABLE
// PLACEHOLDER:JS:RENDER-CLUSTER
// PLACEHOLDER:JS:RENDER-SEARCH
// PLACEHOLDER:JS:EVENT-DELEGATION
// PLACEHOLDER:JS:INIT
  </script>
</body>
</html>
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` contains `<!DOCTYPE html>`
- File contains `<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">`
- File contains `<link rel="manifest" href="./manifest.json">`
- File contains all 10 CSS placeholder comments: `PLACEHOLDER:CSS:DESIGN-TOKENS` through `PLACEHOLDER:CSS:ANIMATIONS`
- File contains all 11 JS placeholder comments: `PLACEHOLDER:JS:DATA-SKELETON` through `PLACEHOLDER:JS:INIT`
- File contains the `<nav class="tab-bar">` with exactly 3 tab buttons
- File contains `<div id="bottom-sheet"` with the `bottom-sheet` class

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-04"`
- `pendingSteps`: remove `"step-04"`
- `flags.htmlShellWritten`: set to `true`
