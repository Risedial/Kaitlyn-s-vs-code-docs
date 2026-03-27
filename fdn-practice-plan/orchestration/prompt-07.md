# Prompt 07: Add DATA.dressPractices Array to index.html

## Prerequisites

state.json flags that must be true:
- `flags.clustersFieldVerified` must be `true` (set by step-02-verify-clusters-field)
- `flags.selectedSymptomsStateVerified` must be `true` (set by step-03-verify-selected-symptoms-state)
- `flags.practicesDataFinalized` must be `true` (set by step-06-finalize-practices-data)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-final.js` (created by Prompt 06)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-final.js`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\data-schema.md` (confirms the DATA object property name is `DATA.dressPractices` and the correct data structure)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Locate the JavaScript data object (`DATA`) that contains `DATA.symptoms` and `DATA.variables`. Add `DATA.dressPractices` as a new array property on the `DATA` object, immediately after `DATA.variables` (or after whichever existing data property is last).

Use the entries from `practices-final.js` verbatim. The property to add:
```js
DATA.dressPractices = dressPracticesData;
```

**OR**, if the `DATA` object is defined as a single object literal (e.g., `const DATA = { symptoms: [...], variables: [...] }`), add `dressPractices: [...]` as a new key on that object — matching the existing structural pattern exactly.

Do NOT restructure the DATA object. Match the existing pattern exactly as documented in codebase-patterns.md Section 4. Use the Edit tool to make this single targeted addition only.

The `dressPractices` array must contain every entry from `practices-final.js` — all entries, no truncation, no placeholders.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html` contains `dressPractices` as a property
- [ ] The array contains at least 12 entries (same count as practices-final.js)
- [ ] No existing `DATA.symptoms` or `DATA.variables` content was modified
- [ ] The file remains valid HTML (no unclosed tags, no broken JavaScript syntax around the edit)

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-07-add-data-layer"` to `completedSteps`
2. Remove `"step-07-add-data-layer"` from `pendingSteps`
3. Set `flags.dataLayerAdded` to `true`
