# Prompt 11: Write CSS — Variable Pills and Cluster Tags

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:PILLS-TAGS */` in `fdn-pwa/index.html` with the variable pill and cluster tag CSS shown below.

The `.var-pill` element uses a CSS custom property `--panel-color` set inline by JS on each pill element. The `.var-pill--cross` variant uses dashed border with transparent background. The `.cluster-tag` element uses `--cluster-color` set inline by JS.

Replace `/* PLACEHOLDER:CSS:PILLS-TAGS */` with:

```css
.var-pill {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 28px;
  min-width: var(--touch-target);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  background: var(--panel-color, var(--panel-cross));
  color: #000000;
  font-family: var(--font-family);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  white-space: nowrap;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  transition: opacity var(--duration-fast), transform var(--duration-fast) var(--ease-spring);
  border: 2px solid transparent;
}

.var-pill:active {
  opacity: 0.75;
  transform: scale(0.96);
}

.var-pill--cross {
  background: transparent;
  border: 2px dashed var(--panel-color, var(--panel-cross));
  color: var(--panel-color, var(--panel-cross));
}

.cluster-tag {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 28px;
  min-width: var(--touch-target);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-sm);
  background: var(--cluster-color, var(--cluster-a));
  color: #000000;
  font-family: var(--font-family);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  white-space: nowrap;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  transition: opacity var(--duration-fast);
}

.cluster-tag:active {
  opacity: 0.75;
}

.panel-badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  background: var(--panel-color, var(--panel-cross));
  color: #000000;
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
}

.cross-panel-badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  border: 2px dashed var(--panel-cross);
  color: var(--panel-cross);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-caps);
  text-transform: uppercase;
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:PILLS-TAGS */`
- File now contains `.var-pill {`
- File contains `.var-pill--cross {` with `background: transparent` and `border: 2px dashed`
- File contains `.cluster-tag {`
- File contains `color: #000000;` on both `.var-pill` and `.cluster-tag`
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-11"`
- `pendingSteps`: remove `"step-11"`
- `flags.cssPillsTags`: set to `true`
