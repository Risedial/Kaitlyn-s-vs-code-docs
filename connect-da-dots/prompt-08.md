# Prompt 08: Write CSS — Top Header (Frosted Glass, Safe-Area-Aware)

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:HEADER */` in `fdn-pwa/index.html` with the top header CSS shown below. This implements the frosted glass sticky header with safe-area-inset-top support.

Replace `/* PLACEHOLDER:CSS:HEADER */` with:

```css
.top-header {
  position: sticky;
  top: 0;
  z-index: 90;
  height: var(--header-height);
  padding-top: var(--safe-top);
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid var(--separator);
}

.top-header-inner {
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--space-4);
}

.header-title {
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--text-primary);
  letter-spacing: var(--tracking-tight);
}

.header-back-btn {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  min-height: var(--touch-target);
  min-width: var(--touch-target);
  padding: 0 var(--space-2);
  color: var(--accent);
  font-size: var(--text-base);
  font-weight: var(--weight-regular);
  background: none;
  border: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.header-back-btn:active {
  opacity: 0.6;
}

.search-container {
  padding: var(--space-2) var(--space-4);
  background: var(--bg-primary);
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:HEADER */`
- File now contains `.top-header {`
- File contains `backdrop-filter: blur(20px) saturate(180%);`
- File contains `-webkit-backdrop-filter: blur(20px) saturate(180%);`
- File contains `padding-top: var(--safe-top);`
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-08"`
- `pendingSteps`: remove `"step-08"`
- `flags.cssHeader`: set to `true`
