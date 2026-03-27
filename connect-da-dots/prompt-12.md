# Prompt 12: Write CSS — Bottom Sheet (Spring Slide-Up)

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `htmlShellWritten`
- Files that MUST already exist: `fdn-pwa/index.html` (shell from step-04)

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:BOTTOM-SHEET */` in `fdn-pwa/index.html` with the bottom sheet CSS shown below. The sheet animates via CSS transform only — no setTimeout, no JS animation.

Replace `/* PLACEHOLDER:CSS:BOTTOM-SHEET */` with:

```css
.bottom-sheet-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 200;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--duration-normal) var(--ease-standard);
}

.bottom-sheet-overlay.is-open {
  opacity: 1;
  pointer-events: auto;
}

.bottom-sheet {
  position: fixed;
  inset: 0;
  top: auto;
  max-height: 92dvh;
  z-index: 201;
  background: var(--bg-secondary);
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  box-shadow: var(--shadow-3);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overscroll-behavior: contain;
  -webkit-overflow-scrolling: touch;
  padding-bottom: var(--safe-bottom);
  transform: translateY(100%);
  transition: transform var(--duration-slow) var(--ease-spring);
  max-width: var(--max-width);
  margin: 0 auto;
  left: 0;
  right: 0;
}

.bottom-sheet.is-open {
  transform: translateY(0);
}

.sheet-drag-indicator {
  width: 36px;
  height: 5px;
  background: var(--separator-opaque);
  border-radius: var(--radius-full);
  margin: var(--space-2) auto var(--space-1);
  flex-shrink: 0;
}

.sheet-content {
  flex: 1;
  padding: var(--space-4);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  overflow-y: auto;
  overscroll-behavior: contain;
  -webkit-overflow-scrolling: touch;
}

.sheet-header {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding-bottom: var(--space-2);
  border-bottom: 1px solid var(--separator);
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:BOTTOM-SHEET */`
- File now contains `.bottom-sheet {`
- File contains `transform: translateY(100%);` on `.bottom-sheet`
- File contains `.bottom-sheet.is-open { transform: translateY(0); }`
- File contains `transition: transform var(--duration-slow) var(--ease-spring);`
- File contains `.sheet-drag-indicator {` with `width: 36px; height: 5px;`
- File contains `.bottom-sheet-overlay {` with z-index 200
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-12"`
- `pendingSteps`: remove `"step-12"`
- `flags.cssBottomSheet`: set to `true`
