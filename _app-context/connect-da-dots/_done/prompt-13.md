# Prompt 13: Write CSS — Alert Banner and Search Bar

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:ALERT-SEARCH */` in `fdn-pwa/index.html` with the alert banner and search bar CSS shown below.

Replace `/* PLACEHOLDER:CSS:ALERT-SEARCH */` with:

```css
.alert-banner {
  width: 100%;
  padding: var(--space-4);
  border-radius: var(--radius-md);
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
}

.alert-banner--destructive {
  background: rgba(255, 59, 48, 0.15);
  border: 1px solid #FF3B30;
  color: #FF3B30;
}

.alert-banner--warning {
  background: rgba(255, 204, 0, 0.12);
  border: 1px solid #FFCC00;
  color: #FFCC00;
}

.alert-icon {
  font-size: var(--text-lg);
  flex-shrink: 0;
  line-height: 1;
}

.alert-body {
  flex: 1;
}

.alert-title {
  font-weight: var(--weight-semibold);
  font-size: var(--text-base);
  line-height: 1.3;
}

.alert-description {
  font-size: var(--text-sm);
  margin-top: var(--space-1);
  opacity: 0.85;
  line-height: 1.5;
}

.search-bar {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  background: var(--bg-tertiary);
  border-radius: var(--radius-full);
  min-height: var(--touch-target);
  padding: var(--space-2) var(--space-4);
  border: 1px solid transparent;
  transition: border-color var(--duration-fast);
}

.search-bar:focus-within {
  border-color: var(--separator-opaque);
}

.search-icon {
  color: var(--text-tertiary);
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-family: var(--font-family);
  font-size: var(--text-base);
  -webkit-appearance: none;
  appearance: none;
}

.search-input::placeholder {
  color: var(--text-tertiary);
}

.search-clear {
  display: none;
  background: none;
  border: none;
  color: var(--text-tertiary);
  cursor: pointer;
  padding: var(--space-1);
  border-radius: var(--radius-full);
  min-height: var(--touch-target);
  min-width: var(--touch-target);
  align-items: center;
  justify-content: center;
  -webkit-tap-highlight-color: transparent;
}

.search-clear.is-visible {
  display: flex;
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:ALERT-SEARCH */`
- File now contains `.alert-banner {`
- File contains `.alert-banner--destructive {` with `border: 1px solid #FF3B30`
- File contains `.search-bar {`
- File contains `border-radius: var(--radius-full)` on `.search-bar`
- File contains `.search-input::placeholder { color: var(--text-tertiary); }`
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-13"`
- `pendingSteps`: remove `"step-13"`
- `flags.cssAlertSearch`: set to `true`
