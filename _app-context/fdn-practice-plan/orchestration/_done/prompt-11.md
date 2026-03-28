# Prompt 11: Add My Plan Nav Tab HTML to index.html

## Prerequisites

state.json flags that must be true:
- `flags.codebasePatternsDocumented` must be `true` (set by step-01-document-codebase-patterns)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Locate the bottom navigation bar (the element containing the existing tab buttons with `class="nav-tab"`). Identify the last existing `<button class="nav-tab">` element. Add the following HTML as the fifth tab, immediately after the last existing nav tab button. Use the Edit tool to insert this at exactly that location.

```html
<button
  class="nav-tab"
  data-tab="plan"
  data-action="navigate-tab"
  aria-label="My Plan"
  style="position: relative;"
>
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true">
    <rect x="4" y="3" width="16" height="18" rx="2" stroke="currentColor" stroke-width="1.5"/>
    <path d="M8 8h8M8 12h8M8 16h5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
    <circle cx="6" cy="8" r="0.75" fill="currentColor"/>
    <circle cx="6" cy="12" r="0.75" fill="currentColor"/>
    <circle cx="6" cy="16" r="0.75" fill="currentColor"/>
  </svg>
  <span class="nav-label">My Plan</span>
  <span class="nav-badge" id="plan-badge" aria-hidden="true"></span>
</button>
```

**Exact locked values:**
- Tab label: `"My Plan"` (exactly this text in `<span class="nav-label">`)
- Tab badge ID: `plan-badge`
- `data-tab` value: `"plan"`
- `data-action` value: `"navigate-tab"`

Match the SVG dimensions and class names of existing tab icons in the nav bar. If the existing tabs do not use inline `style="position: relative;"`, remove that attribute — match the existing tab button structure exactly.

Do NOT modify any existing tab button. Do NOT add any JavaScript in this step. Use the Edit tool.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `fdn-pwa/index.html` contains `<button class="nav-tab"` with `data-tab="plan"`
- [ ] The button contains `<span class="nav-label">My Plan</span>` (exact text)
- [ ] The button contains `<span class="nav-badge" id="plan-badge"`
- [ ] The button has `data-action="navigate-tab"`
- [ ] The button has `aria-label="My Plan"`
- [ ] No existing nav tab buttons were modified

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-11-add-nav-tab-html"` to `completedSteps`
2. Remove `"step-11-add-nav-tab-html"` from `pendingSteps`
3. Set `flags.navTabAdded` to `true`
