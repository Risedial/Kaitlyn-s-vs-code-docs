# Prompt 36: Write JS — Event Delegation Handler

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `renderHome`, `renderSymptom`, `renderVariable`, `renderCluster`, `renderSearch`
- Files that MUST already exist: `fdn-pwa/index.html`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:EVENT-DELEGATION` in `fdn-pwa/index.html` with the event delegation handler shown below.

The event delegation pattern uses a single `click` listener on `document` that reads `data-action` attributes from event targets. This is the ONLY click binding mechanism — no individual element click handlers outside of the search input listeners already added by render functions.

**Actions handled**:
- `navigate-tab`: calls `navigateTab(btn.dataset.tab)`
- `open-symptom`: calls `pushSheet('symptom', btn.dataset.id)` or `openSheet` if sheet is not open
- `open-variable`: calls `pushSheet('variable', btn.dataset.id)` or `openSheet`
- `open-cluster`: calls `pushSheet('cluster', btn.dataset.id)` or `openSheet`
- `go-back`: calls `popSheet()`
- `close-sheet`: calls `closeSheet()`

Replace `// PLACEHOLDER:JS:EVENT-DELEGATION` with:

```javascript
// ─── Event Delegation ─────────────────────────────────────────────────────
document.addEventListener('click', function handleClick(e) {
  // Walk up the DOM tree to find the element with data-action
  let target = e.target;
  while (target && target !== document.body) {
    const action = target.dataset && target.dataset.action;
    if (action) {
      const id = target.dataset.id;
      switch (action) {
        case 'navigate-tab':
          navigateTab(target.dataset.tab);
          return;
        case 'open-symptom':
          if (!id) return;
          if (state.sheet.isOpen) pushSheet('symptom', id);
          else openSheet('symptom', id);
          return;
        case 'open-variable':
          if (!id) return;
          if (state.sheet.isOpen) pushSheet('variable', id);
          else openSheet('variable', id);
          return;
        case 'open-cluster':
          if (!id) return;
          if (state.sheet.isOpen) pushSheet('cluster', id);
          else openSheet('cluster', id);
          return;
        case 'go-back':
          popSheet();
          return;
        case 'close-sheet':
          closeSheet();
          return;
        default:
          break;
      }
    }
    target = target.parentElement;
  }
});

// Close sheet on Escape key
document.addEventListener('keydown', function handleKeydown(e) {
  if (e.key === 'Escape' && state.sheet.isOpen) {
    closeSheet();
  }
});
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:EVENT-DELEGATION`
- File now contains `document.addEventListener('click', function handleClick`
- File contains `switch (action) {` with all 6 case handlers
- File contains `case 'navigate-tab':`, `case 'open-symptom':`, `case 'open-variable':`, `case 'open-cluster':`, `case 'go-back':`, `case 'close-sheet':`
- File contains the DOM tree walk: `while (target && target !== document.body)`
- File contains keyboard `Escape` handler for closing sheet
- No individual click event listeners on specific elements (besides search input listeners in render functions)

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-36"`
- `pendingSteps`: remove `"step-36"`
- `flags.eventDelegation`: set to `true`
