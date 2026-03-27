# Prompt 10: Write CSS — List Rows and Accordion Sections

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:LIST-ROWS */` in `fdn-pwa/index.html` with the list row and accordion section CSS shown below.

Replace `/* PLACEHOLDER:CSS:LIST-ROWS */` with:

```css
.list-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: var(--touch-target);
  min-width: var(--touch-target);
  padding: var(--space-3) var(--space-4);
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--separator);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  transition: background var(--duration-fast) var(--ease-standard),
              transform var(--duration-fast) var(--ease-standard);
}

.list-row:active {
  transform: scale(0.98);
  background: var(--bg-tertiary);
}

.list-row-label {
  font-size: var(--text-base);
  color: var(--text-primary);
  flex: 1;
}

.list-row-chevron {
  color: var(--text-tertiary);
  flex-shrink: 0;
}

.accordion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: var(--touch-target);
  min-width: var(--touch-target);
  width: 100%;
  padding: var(--space-3) var(--space-4);
  background: var(--bg-secondary);
  border: none;
  border-bottom: 1px solid var(--separator);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.accordion-header:active {
  background: var(--bg-tertiary);
}

.accordion-title {
  font-size: var(--text-base);
  font-weight: var(--weight-semibold);
  color: var(--text-primary);
}

.accordion-right {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.accordion-chevron {
  transition: transform var(--duration-normal) var(--ease-snap);
  display: inline-block;
  color: var(--text-tertiary);
}

.accordion-header[aria-expanded="true"] .accordion-chevron {
  transform: rotate(90deg);
}

.accordion-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 20px;
  height: 20px;
  padding: 0 6px;
  border-radius: var(--radius-full);
  background: var(--accent);
  color: #fff;
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
}

.accordion-body {
  display: none;
}

.accordion-body.is-open {
  display: block;
}

.result-group-heading {
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: var(--tracking-caps);
  padding: var(--space-3) var(--space-4) var(--space-1);
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:LIST-ROWS */`
- File now contains `.list-row {`
- File contains `.list-row:active { transform: scale(0.98);`
- File contains `.accordion-header[aria-expanded="true"] .accordion-chevron { transform: rotate(90deg); }`
- File contains `.accordion-body.is-open { display: block; }`
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-10"`
- `pendingSteps`: remove `"step-10"`
- `flags.cssListRows`: set to `true`
