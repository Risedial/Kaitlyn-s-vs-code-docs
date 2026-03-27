# Prompt 09: Add State Management Functions to index.html

## Prerequisites

state.json flags that must be true:
- `flags.dataLayerAdded` must be `true` (set by step-07-add-data-layer)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\app-state-schema.md` (exact localStorage key, default state structure, and state mutation rules — authoritative reference for getPlanState/setPlanState/togglePracticeComplete)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Locate the correct position for state management functions (alongside or after existing localStorage read/write helpers, if any — use codebase-patterns.md Section 4 to identify the state management pattern). Add the following three functions using the Edit tool. Match existing function style exactly.

Add all three functions together in a single contiguous block, immediately after the utility functions added in Prompt 08:

**Function 1 — getPlanState()**
```js
function getPlanState() {
  try {
    const raw = localStorage.getItem('fdn-plan-state');
    return raw ? JSON.parse(raw) : { completedIds: [], viewMode: 'focus', lastSymptomHash: '' };
  } catch (e) {
    return { completedIds: [], viewMode: 'focus', lastSymptomHash: '' };
  }
}
```

**Function 2 — setPlanState(state)**
```js
function setPlanState(state) {
  localStorage.setItem('fdn-plan-state', JSON.stringify(state));
}
```

**Function 3 — togglePracticeComplete(practiceId)**
```js
function togglePracticeComplete(practiceId) {
  const state = getPlanState();
  const idx = state.completedIds.indexOf(practiceId);
  if (idx === -1) {
    state.completedIds.push(practiceId);
  } else {
    state.completedIds.splice(idx, 1);
  }
  setPlanState(state);
  const card = document.querySelector('.practice-card[data-practice-id="' + practiceId + '"]');
  if (card) {
    const isComplete = state.completedIds.includes(practiceId);
    card.classList.toggle('practice-complete', isComplete);
    const checkbox = card.querySelector('.practice-checkbox');
    if (checkbox) checkbox.setAttribute('aria-pressed', String(isComplete));
  }
}
```

**localStorage key must be exactly:** `'fdn-plan-state'`
**Default state must be exactly:** `{ completedIds: [], viewMode: 'focus', lastSymptomHash: '' }`

Do NOT modify any existing function. Do NOT add a new `addEventListener`. Use the Edit tool.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `fdn-pwa/index.html` contains function `getPlanState`
- [ ] `fdn-pwa/index.html` contains function `setPlanState`
- [ ] `fdn-pwa/index.html` contains function `togglePracticeComplete`
- [ ] `getPlanState` uses `localStorage.getItem('fdn-plan-state')` with exactly that key
- [ ] Default return value includes `completedIds: []`, `viewMode: 'focus'`, `lastSymptomHash: ''`
- [ ] No existing functions were modified

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-09-add-state-functions"` to `completedSteps`
2. Remove `"step-09-add-state-functions"` from `pendingSteps`
3. Set `flags.stateFunctionsAdded` to `true`
