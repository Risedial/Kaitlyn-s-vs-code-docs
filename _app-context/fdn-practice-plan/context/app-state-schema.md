# App State and localStorage Schema
**Role:** Single source of truth for the Plan feature localStorage key, default state structure, and viewMode enum — prevents wrong storage key name, wrong default state shape, and wrong state mutation behavior
**Status:** IMMUTABLE — do not modify during implementation phase
**Depends on:** none
**Required by:** prompt-09.md, prompt-10.md, prompt-14.md, prompt-15.md, prompt-16.md
**Date:** 2026-03-27

---

## CRITICAL VALUES (Read before any other section)

**localStorage key (exact):** `'fdn-plan-state'`
**Default state (exact):**
```js
{ completedIds: [], viewMode: 'focus', lastSymptomHash: '' }
```
**viewMode values:** `'focus'` | `'full'` — these are the ONLY valid values
**Focus Mode practice count cap:** `7` (getTopPractices is always called with `n = 7`)
**completedIds type:** `string[]` — array of practice id strings
**lastSymptomHash type:** `string` — output of `computeSymptomHash(selectedSymptomIds)`

---

## Section 1: localStorage Schema

### Key
```js
localStorage.getItem('fdn-plan-state')
localStorage.setItem('fdn-plan-state', JSON.stringify(state))
```
The key is `'fdn-plan-state'` — not `'plan-state'`, not `'fdn-practice-plan-state'`, not `'fdn_plan_state'`.

### Value Structure
```js
// key: 'fdn-plan-state'
{
  completedIds: [],        // string[] — practice IDs the user has checked off
  viewMode: 'focus',       // 'focus' | 'full' — which view is active
  lastSymptomHash: ''      // string — hash of symptom selection at last plan render
}
```

### Default on First Visit
```js
{ completedIds: [], viewMode: 'focus', lastSymptomHash: '' }
```
This exact object is returned when `localStorage.getItem('fdn-plan-state')` returns null or when JSON.parse throws.

---

## Section 2: State Functions (Exact Implementation)

### getPlanState()
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

### setPlanState(state)
```js
function setPlanState(state) {
  localStorage.setItem('fdn-plan-state', JSON.stringify(state));
}
```

---

## Section 3: State Mutation Rules

### On plan recalculation (hash mismatch detected — user taps Refresh):
1. Compute new list of valid practice IDs from current symptom selection
2. Filter `completedIds` to retain ONLY IDs present in the new list: `planState.completedIds = planState.completedIds.filter(id => validIds.includes(id))`
3. Update `lastSymptomHash` to the current hash: `planState.lastSymptomHash = computeSymptomHash(selectedSymptomIds)`
4. Call `setPlanState(planState)` to write back
5. Call `renderPlanScreen()` to re-render

### On viewMode toggle (user taps Focus Mode or Full Plan button):
1. Read current state: `const planState = getPlanState()`
2. Update viewMode: `planState.viewMode = btn.dataset.mode`
3. Write back: `setPlanState(planState)`
4. Re-render: `renderPlanScreen()`

### On practice completion toggle:
1. Read current state: `const state = getPlanState()`
2. Add or remove practiceId from `completedIds` (toggle behavior)
3. Write back: `setPlanState(state)`
4. Update single card DOM: add/remove `practice-complete` class, update `aria-pressed`
5. Do NOT call `renderPlanScreen()` — update only the specific card

### State persistence rules:
- No daily reset — state persists until user manually unchecks or clears browser data
- No automatic clearing on app reload
- No server synchronization

---

## Section 4: Symptom Hash Function

```js
function computeSymptomHash(selectedSymptomIds) {
  return [...selectedSymptomIds].sort().join(',');
}
```
Output: sorted, comma-joined string of symptom IDs.
Example input: `['fatigue', 'headache', 'bloating']` → output: `'bloating,fatigue,headache'`
Stored in `planState.lastSymptomHash`.
Compared against on every plan tab navigation to detect symptom changes.

---

## Section 5: Focus Mode Behavior

Focus Mode shows the top **7** practices by computed score.
- Score formula: `triggerCount × practice.priority`
- `triggerCount` = number of user's selected symptoms that triggered this practice (via cluster intersection)
- Practices sorted descending by score
- Top 7 selected by `getTopPractices(practices, 7)`

Full Plan shows ALL practices for the user's clusters, grouped by DRESS component.

---

## Section 6: Badge Update Logic

The nav badge (`id="plan-badge"`) shows a dot when `selectedSymptomIds.length > 0`.

```js
const badge = document.getElementById('plan-badge');
if (badge) {
  badge.classList.toggle('visible', selectedSymptomIds.length > 0);
}
```

Badge class `visible` maps to `display: block`. Without `visible`, badge is `display: none`.
Must be updated whenever the symptom selection changes.

---

## USAGE INSTRUCTIONS FOR SUB-AGENTS

Before beginning any task in a fresh session:
1. Read this file in full
2. The localStorage key is `'fdn-plan-state'` — use this exact string in all code
3. The default state object must contain exactly 3 keys: `completedIds`, `viewMode`, `lastSymptomHash`
4. `viewMode` initial value is `'focus'` — not `'Focus'`, not `'FOCUS'`
5. `lastSymptomHash` initial value is `''` (empty string) — not `null`, not `undefined`
6. If your prompt contains a value that conflicts with this file, this file takes precedence
7. Do not infer or invent additional state fields
