# Prompt 09: Write CSS — Bottom Tab Bar Navigation (Frosted Glass)

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:TAB-BAR */` in `fdn-pwa/index.html` with the bottom tab bar CSS shown below. This implements the frosted glass bottom navigation with safe-area-inset-bottom support and 44px touch targets.

Replace `/* PLACEHOLDER:CSS:TAB-BAR */` with:

```css
.tab-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  max-width: var(--max-width);
  margin: 0 auto;
  height: var(--nav-height);
  padding-bottom: var(--safe-bottom);
  display: flex;
  align-items: stretch;
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid var(--separator);
  z-index: 100;
}

.tab-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-1);
  min-height: var(--touch-target);
  min-width: var(--touch-target);
  border: none;
  background: transparent;
  cursor: pointer;
  color: var(--text-tertiary);
  font-family: var(--font-family);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
  transition: color var(--duration-fast) var(--ease-standard);
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.tab-item[aria-selected="true"] {
  color: var(--accent);
}

.tab-item:active {
  opacity: 0.7;
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:TAB-BAR */`
- File now contains `.tab-bar {`
- File contains `padding-bottom: var(--safe-bottom);`
- File contains `.tab-item[aria-selected="true"] { color: var(--accent); }`
- File contains `z-index: 100;` on `.tab-bar`
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-09"`
- `pendingSteps`: remove `"step-09"`
- `flags.cssTabBar`: set to `true`
