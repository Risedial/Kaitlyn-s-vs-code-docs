# Prompt 15: Add Badge Visibility Update Logic to index.html

## Prerequisites

state.json flags that must be true:
- `flags.eventDelegationUpdated` must be `true` (set by step-14-add-event-delegation)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\app-state-schema.md` (badge logic — Section 6 — and exact selectedSymptomIds threshold for badge visibility)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Find every location in the JavaScript where symptoms are added to or removed from the selection state (i.e., where `selectedSymptomIds` is modified, or where symptom toggle/selection logic runs). At each such location, add a call to update the badge visibility immediately after the symptom selection change.

The badge update logic to add at each relevant location:
```js
const planBadge = document.getElementById('plan-badge');
if (planBadge) {
  planBadge.classList.toggle('visible', selectedSymptomIds.length > 0);
}
```

Where `selectedSymptomIds` should use the exact property path documented in codebase-patterns.md Section 6.

**If no explicit symptom selection change points are identifiable:** Add a helper function `updatePlanBadge()` immediately after the utility functions from Prompt 08, and add a call to `updatePlanBadge()` in the `renderPlanScreen()` function at the end of the non-empty-state path:

```js
function updatePlanBadge() {
  const selectedSymptomIds = /* exact expression from codebase-patterns.md Section 6 */;
  const badge = document.getElementById('plan-badge');
  if (badge) {
    badge.classList.toggle('visible', selectedSymptomIds.length > 0);
  }
}
```

Then call `updatePlanBadge()` at the end of `renderPlanScreen()` (before the `return` statement) and at each location where the symptom selection changes.

Do NOT modify any existing symptom selection logic — only add the badge update call after it. Use the Edit tool.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `fdn-pwa/index.html` contains badge update logic referencing `plan-badge`
- [ ] Badge logic calls `classList.toggle('visible', ...)` or `classList.add/remove('visible')`
- [ ] Badge visibility is driven by whether `selectedSymptomIds.length > 0`
- [ ] No existing symptom selection logic was removed or restructured

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-15-add-badge-logic"` to `completedSteps`
2. Remove `"step-15-add-badge-logic"` from `pendingSteps`
3. Set `flags.badgeLogicAdded` to `true`
