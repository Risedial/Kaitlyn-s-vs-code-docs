# Prompt 06: Write CSS — Base Reset and Body Styles

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:BASE-RESET */` in `fdn-pwa/index.html` with the base reset and body CSS shown below. This section resets browser defaults and establishes the iOS-dark-mode base for the app.

Replace `/* PLACEHOLDER:CSS:BASE-RESET */` with:

```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html, body {
  height: 100%;
  overscroll-behavior: none;
  -webkit-overflow-scrolling: touch;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: var(--font-family);
  font-size: var(--text-base);
  font-weight: var(--weight-regular);
  line-height: 1.4;
  letter-spacing: var(--tracking-normal);
}

button {
  font-family: var(--font-family);
  font-size: var(--text-base);
  border: none;
  background: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

input {
  font-family: var(--font-family);
}

svg {
  display: block;
  flex-shrink: 0;
}

p, h1, h2, h3, h4 {
  overflow-wrap: break-word;
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:BASE-RESET */`
- File now contains `*, *::before, *::after {`
- File contains `overscroll-behavior: none;`
- File contains `-webkit-tap-highlight-color: transparent;`
- All remaining CSS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-06"`
- `pendingSteps`: remove `"step-06"`
- `flags.cssBaseReset`: set to `true`
