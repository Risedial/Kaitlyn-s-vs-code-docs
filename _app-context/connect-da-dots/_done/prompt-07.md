# Prompt 07: Write CSS — Layout and App Container

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:LAYOUT */` in `fdn-pwa/index.html` with the layout CSS shown below. This section controls the max-width centering, app container structure, screen container, and scroll behavior.

Replace `/* PLACEHOLDER:CSS:LAYOUT */` with:

```css
#app {
  position: relative;
  width: 100%;
  max-width: var(--max-width);
  margin: 0 auto;
  min-height: 100dvh;
  background: var(--bg-primary);
  overflow: hidden;
}

#screen-container {
  position: relative;
  width: 100%;
  min-height: 100dvh;
  padding-bottom: var(--nav-height);
  overflow-y: auto;
  overscroll-behavior: contain;
  -webkit-overflow-scrolling: touch;
}

.screen {
  width: 100%;
  min-height: 100%;
  background: var(--bg-primary);
}

.section-list {
  list-style: none;
}

.section-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-2) var(--space-4);
  background: var(--bg-primary);
}

.section-header-label {
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: var(--tracking-caps);
}

.content-section {
  padding: var(--space-4);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.pill-grid {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--space-12) var(--space-6);
  text-align: center;
  color: var(--text-tertiary);
  font-size: var(--text-sm);
  gap: var(--space-3);
}

.detail-heading {
  font-size: var(--text-xl);
  font-weight: var(--weight-bold);
  color: var(--text-primary);
  letter-spacing: var(--tracking-tight);
  line-height: 1.2;
}

.detail-subheading {
  font-size: var(--text-base);
  font-weight: var(--weight-semibold);
  color: var(--text-secondary);
  margin-top: var(--space-4);
  margin-bottom: var(--space-2);
}

.mechanism-tree {
  font-family: var(--font-family);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.6;
  white-space: pre-line;
  background: var(--bg-tertiary);
  border-radius: var(--radius-md);
  padding: var(--space-4);
}

.interpretation-text {
  font-size: var(--text-base);
  color: var(--text-secondary);
  line-height: 1.6;
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:LAYOUT */`
- File now contains `max-width: var(--max-width);`
- File contains `padding-bottom: var(--nav-height);`
- File contains `.pill-grid {`
- File contains `.mechanism-tree {`
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-07"`
- `pendingSteps`: remove `"step-07"`
- `flags.cssLayout`: set to `true`
