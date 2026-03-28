# Prompt 14: Write CSS — Screen Transitions and Animations

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:ANIMATIONS */` in `fdn-pwa/index.html` with the animation and transition CSS shown below. All animations use CSS transitions and keyframes only — no setTimeout or setInterval.

Replace `/* PLACEHOLDER:CSS:ANIMATIONS */` with:

```css
@keyframes fade-in {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes scale-in {
  from { opacity: 0; transform: scale(0.95); }
  to   { opacity: 1; transform: scale(1); }
}

.animate-fade-in {
  animation: fade-in var(--duration-normal) var(--ease-snap) forwards;
}

.animate-scale-in {
  animation: scale-in var(--duration-fast) var(--ease-spring) forwards;
}

.screen-enter {
  animation: fade-in var(--duration-normal) var(--ease-snap) forwards;
}

.priority-block {
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: rgba(239, 68, 68, 0.12);
  border: 1px solid var(--cluster-a);
  color: var(--cluster-a);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  line-height: 1.5;
}

.referral-block {
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: rgba(251, 191, 36, 0.12);
  border: 1px solid var(--cluster-e);
  color: var(--cluster-e);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  line-height: 1.5;
}

.divider {
  height: 1px;
  background: var(--separator);
  margin: 0 var(--space-4);
}

.spacer-sm { height: var(--space-2); }
.spacer-md { height: var(--space-4); }
.spacer-lg { height: var(--space-8); }

.text-accent { color: var(--accent); }
.text-destructive { color: var(--accent-destructive); }
.text-secondary { color: var(--text-secondary); }
.text-tertiary { color: var(--text-tertiary); }
.font-semibold { font-weight: var(--weight-semibold); }
.font-bold { font-weight: var(--weight-bold); }
.text-sm { font-size: var(--text-sm); }
.text-xs { font-size: var(--text-xs); }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:ANIMATIONS */`
- File now contains `@keyframes fade-in {`
- File contains `.screen-enter {`
- File contains `@media (prefers-reduced-motion: reduce) {`
- File contains `.priority-block {` and `.referral-block {`
- All 10 CSS placeholder comments are now replaced (none remain in the style block as `PLACEHOLDER:CSS:*`)

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-14"`
- `pendingSteps`: remove `"step-14"`
- `flags.cssAnimations`: set to `true`
