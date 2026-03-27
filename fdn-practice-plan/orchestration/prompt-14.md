# Prompt 14: Add Event Delegation Handlers to index.html

## Prerequisites

state.json flags that must be true:
- `flags.renderFunctionAdded` must be `true` (set by step-10-add-render-function)
- `flags.screenSectionAdded` must be `true` (set by step-12-add-screen-section-html)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\app-state-schema.md` (exact localStorage key and state mutation rules for refresh-plan and switch-plan-mode handlers)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Using codebase-patterns.md Section 2, locate the existing event delegation handler function. Find the existing dispatch structure (switch/if-else on `data-action`). Add the following new cases to this existing handler — do NOT create a new `addEventListener`. Use the Edit tool to insert only the new cases.

**New cases to add:**

**Case: `navigate-tab` with `data-tab="plan"`**
This case may already exist as a generic `navigate-tab` handler for all tabs. If a generic handler already exists: add a call to `renderPlanScreen()` when `event.target.closest('[data-tab]').dataset.tab === 'plan'`. If no generic handler exists, add this case:
```js
case 'navigate-tab':
  // (add to existing navigate-tab handler, or add new case if absent)
  if (action.dataset && action.dataset.tab === 'plan') {
    renderPlanScreen();
  }
  // existing tab navigation logic continues
  break;
```

**Case: `toggle-practice-expand`**
```js
case 'toggle-practice-expand': {
  const card = event.target.closest('.practice-card');
  if (card) {
    const body = card.querySelector('.practice-card-body');
    const isExpanded = card.dataset.expanded === 'true';
    card.dataset.expanded = String(!isExpanded);
    if (body) body.hidden = isExpanded;
  }
  break;
}
```

**Case: `toggle-practice-complete`**
```js
case 'toggle-practice-complete': {
  event.stopPropagation();
  const btn = event.target.closest('[data-practice-id]');
  if (btn && btn.dataset.practiceId) {
    togglePracticeComplete(btn.dataset.practiceId);
  }
  break;
}
```

**Case: `refresh-plan`**
```js
case 'refresh-plan': {
  const planState = getPlanState();
  const selectedSymptomIds = /* read from app state — use exact expression from codebase-patterns.md Section 6 */;
  const activeClusters = getActiveClusters(selectedSymptomIds);
  const practices = getPracticesForClusters(activeClusters, selectedSymptomIds);
  const validIds = practices.map(p => p.id);
  planState.completedIds = planState.completedIds.filter(id => validIds.includes(id));
  planState.lastSymptomHash = computeSymptomHash(selectedSymptomIds);
  setPlanState(planState);
  renderPlanScreen();
  const banner = document.getElementById('plan-refresh-banner');
  if (banner) banner.hidden = true;
  break;
}
```

**Case: `switch-plan-mode`**
```js
case 'switch-plan-mode': {
  const btn = event.target.closest('[data-mode]');
  if (btn && btn.dataset.mode) {
    const planState = getPlanState();
    planState.viewMode = btn.dataset.mode;
    setPlanState(planState);
    renderPlanScreen();
  }
  break;
}
```

**CRITICAL:** Replace all occurrences of `/* read from app state — use exact expression from codebase-patterns.md Section 6 */` with the actual expression to read `selectedSymptomIds` from the app state, using the exact property name and object documented in codebase-patterns.md.

**CRITICAL:** Do NOT add `navigate-tab` as a duplicate case if it already exists. Instead, add the plan-specific call within the existing case. Read the handler carefully before editing.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] The existing event delegation handler in `fdn-pwa/index.html` now handles `toggle-practice-expand`
- [ ] The existing event delegation handler handles `toggle-practice-complete`
- [ ] The existing event delegation handler handles `refresh-plan`
- [ ] The existing event delegation handler handles `switch-plan-mode`
- [ ] `renderPlanScreen()` is called when the plan tab is navigated to
- [ ] No new `addEventListener` calls were added — all new cases are inside the existing handler
- [ ] No existing handler cases were removed or modified (only new cases added)

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-14-add-event-delegation"` to `completedSteps`
2. Remove `"step-14-add-event-delegation"` from `pendingSteps`
3. Set `flags.eventDelegationUpdated` to `true`
