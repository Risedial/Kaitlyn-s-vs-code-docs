# Prompt 13: Add New CSS Classes to index.html

## Prerequisites

state.json flags that must be true:
- `flags.codebasePatternsDocumented` must be `true` (set by step-01-document-codebase-patterns)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md`
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

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Locate the `<style>` block (the embedded stylesheet). Find the end of the existing CSS rules. Add the following CSS block immediately before the closing `</style>` tag, using the Edit tool.

Use ONLY CSS custom properties already documented in codebase-patterns.md Section 7. Do NOT introduce any new `--` custom properties.

```css
/* ─── My Plan Feature ─── */
.practice-card {
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  margin-bottom: var(--space-sm);
  overflow: hidden;
}
.practice-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
  padding: var(--space-md);
  min-height: 44px;
  cursor: pointer;
  user-select: none;
}
.practice-title {
  flex: 1;
  font-weight: 600;
  color: var(--text-primary);
  font-size: var(--text-md);
}
.practice-complete .practice-title { color: var(--text-secondary); }
.practice-complete .practice-card-header { opacity: 0.6; }
.frequency-pill {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  background: var(--bg-primary);
  border-radius: 99px;
  padding: 2px 8px;
  white-space: nowrap;
}
.practice-checkbox {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  min-width: 44px;
  border: none;
  background: transparent;
  cursor: pointer;
  color: var(--text-secondary);
  border-radius: var(--radius-md);
  padding: 0;
}
.practice-card-body {
  padding: 0 var(--space-md) var(--space-md);
  border-top: 1px solid var(--border-subtle);
}
.practice-card-body p {
  color: var(--text-primary);
  font-size: var(--text-sm);
  line-height: 1.5;
  margin-bottom: var(--space-xs);
}
.practice-what-label,
.practice-why-label {
  font-weight: 600;
  color: var(--text-secondary);
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-top: var(--space-sm);
}
.cluster-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.cluster-dot.cluster-A { background: var(--cluster-a); }
.cluster-dot.cluster-B { background: var(--cluster-b); }
.cluster-dot.cluster-C { background: var(--cluster-c); }
.cluster-dot.cluster-D { background: var(--cluster-d); }
.cluster-dot.cluster-E { background: var(--cluster-e); }
@keyframes check-pop {
  0%   { transform: scale(1); opacity: 0; }
  50%  { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}
.practice-checkbox[aria-pressed="true"] svg {
  animation: check-pop 200ms ease-out forwards;
  color: var(--accent);
}
.practice-checkbox[aria-pressed="true"] {
  color: var(--accent);
}
.plan-mode-toggle {
  display: flex;
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  padding: 2px;
  margin-bottom: var(--space-sm);
}
.mode-btn {
  flex: 1;
  padding: var(--space-xs) var(--space-sm);
  border-radius: calc(var(--radius-md) - 2px);
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text-secondary);
  background: transparent;
  border: none;
  cursor: pointer;
  min-height: 44px;
}
.mode-btn.active {
  background: var(--bg-primary);
  color: var(--accent);
  font-weight: 600;
}
.mode-explainer {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  margin-bottom: var(--space-md);
  padding: 0 var(--space-xs);
}
.dress-section { margin-bottom: var(--space-sm); }
.dress-section-header {
  font-weight: 600;
  color: var(--text-primary);
  font-size: var(--text-md);
  padding: var(--space-sm) 0;
  cursor: pointer;
  list-style: none;
}
.dress-section-body { padding-top: var(--space-xs); }
.plan-header { margin-bottom: var(--space-md); }
.plan-header h2 {
  font-size: var(--text-xl);
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--space-xs);
}
.nav-badge {
  display: none;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  position: absolute;
  top: 6px;
  right: 6px;
}
.nav-badge.visible { display: block; }
.alert-referral {
  background: var(--bg-secondary);
  border-left: 3px solid var(--cluster-e);
  border-radius: var(--radius-md);
  padding: var(--space-md);
  margin-bottom: var(--space-md);
  color: var(--text-primary);
  font-size: var(--text-sm);
  line-height: 1.5;
}
.banner-notice {
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  padding: var(--space-sm) var(--space-md);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-md);
  font-size: var(--text-sm);
  color: var(--text-secondary);
}
.practice-list { padding-bottom: var(--space-lg); }
```

**Before adding:** Verify that none of these class names already exist in the stylesheet. If any class already exists, skip adding it (do not duplicate). Add only the classes that are new.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `fdn-pwa/index.html` stylesheet contains `.practice-card` rule
- [ ] `fdn-pwa/index.html` stylesheet contains `.practice-card-header` rule
- [ ] `fdn-pwa/index.html` stylesheet contains `.cluster-dot` rule
- [ ] `fdn-pwa/index.html` stylesheet contains `.plan-mode-toggle` rule
- [ ] `fdn-pwa/index.html` stylesheet contains `.alert-referral` rule
- [ ] `fdn-pwa/index.html` stylesheet contains `.nav-badge` rule
- [ ] `fdn-pwa/index.html` stylesheet contains `@keyframes check-pop`
- [ ] No new CSS custom properties (`--` variables) were introduced — only existing tokens used
- [ ] No existing CSS rules were modified

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-13-add-css-classes"` to `completedSteps`
2. Remove `"step-13-add-css-classes"` from `pendingSteps`
3. Set `flags.cssClassesAdded` to `true`
