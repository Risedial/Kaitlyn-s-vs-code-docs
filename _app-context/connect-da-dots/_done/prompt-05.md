# Prompt 05: Write CSS — Design Tokens (:root Block)

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
Use the Edit tool to replace the placeholder comment `/* PLACEHOLDER:CSS:DESIGN-TOKENS */` in `fdn-pwa/index.html` with the complete `:root {}` CSS custom properties block shown below. Copy this block verbatim — do not alter any value, variable name, or comment.

Replace `/* PLACEHOLDER:CSS:DESIGN-TOKENS */` with:

```css
:root {
  /* Safe Areas */
  --safe-top:    env(safe-area-inset-top, 0px);
  --safe-right:  env(safe-area-inset-right, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left:   env(safe-area-inset-left, 0px);

  /* Backgrounds - iOS UIColor dark mode equivalents */
  --bg-primary:   #000000;
  --bg-secondary: #1C1C1E;
  --bg-tertiary:  #2C2C2E;
  --bg-glass:     rgba(28, 28, 30, 0.72);

  /* Text */
  --text-primary:   rgba(255, 255, 255, 1.0);
  --text-secondary: rgba(255, 255, 255, 0.55);
  --text-tertiary:  rgba(255, 255, 255, 0.35);

  /* Separators */
  --separator:        rgba(255, 255, 255, 0.12);
  --separator-opaque: #3A3A3C;

  /* Accent */
  --accent:             #007AFF;
  --accent-destructive: #FF3B30;

  /* FDN Panel Colors - preserve exactly */
  --panel-mwp:   #e07c3a;
  --panel-mba:   #3abde0;
  --panel-shp:   #8b5cf6;
  --panel-gimap: #22c55e;
  --panel-cross: #94a3b8;

  /* FDN Cluster Colors - preserve exactly */
  --cluster-a: #ef4444;
  --cluster-b: #f97316;
  --cluster-c: #ec4899;
  --cluster-d: #06b6d4;
  --cluster-e: #fbbf24;

  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif;
  --text-xs:   0.6875rem;
  --text-sm:   0.8125rem;
  --text-base: 1rem;
  --text-md:   1.0625rem;
  --text-lg:   1.25rem;
  --text-xl:   1.5rem;
  --text-2xl:  2rem;
  --weight-regular:  400;
  --weight-medium:   500;
  --weight-semibold: 600;
  --weight-bold:     700;
  --tracking-tight:  -0.02em;
  --tracking-normal:  0em;
  --tracking-wide:    0.03em;
  --tracking-caps:    0.06em;

  /* Spacing - 4px base grid */
  --space-1:  0.25rem;
  --space-2:  0.5rem;
  --space-3:  0.75rem;
  --space-4:  1rem;
  --space-5:  1.25rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;

  /* Border Radius */
  --radius-sm:   8px;
  --radius-md:   12px;
  --radius-lg:   16px;
  --radius-xl:   20px;
  --radius-full: 9999px;

  /* Shadows - dark-background-optimized */
  --shadow-0: none;
  --shadow-1: 0 1px 2px rgba(0,0,0,0.4), 0 0px 1px rgba(0,0,0,0.3);
  --shadow-2: 0 4px 12px rgba(0,0,0,0.5), 0 1px 3px rgba(0,0,0,0.4);
  --shadow-3: 0 16px 40px rgba(0,0,0,0.6), 0 4px 12px rgba(0,0,0,0.5), 0 1px 3px rgba(0,0,0,0.4);

  /* Motion */
  --ease-spring:   cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-snap:     cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  --duration-fast:   150ms;
  --duration-normal: 300ms;
  --duration-slow:   450ms;

  /* Layout */
  --touch-target:  44px;
  --max-width:    430px;
  --nav-height:   calc(60px + var(--safe-bottom));
  --header-height: calc(52px + var(--safe-top));
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `/* PLACEHOLDER:CSS:DESIGN-TOKENS */`
- File now contains `:root {` block
- File contains `--panel-mwp: #e07c3a` (FDN panel color, exact value)
- File contains `--cluster-a: #ef4444` (FDN cluster color, exact value)
- File contains `--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1)` (motion token, exact value)
- File contains `--nav-height: calc(60px + var(--safe-bottom))`
- All other 9 CSS placeholder comments (`PLACEHOLDER:CSS:BASE-RESET` through `PLACEHOLDER:CSS:ANIMATIONS`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-05"`
- `pendingSteps`: remove `"step-05"`
- `flags.cssDesignTokens`: set to `true`
