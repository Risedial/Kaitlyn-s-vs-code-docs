# Prompt 06: Finalize Practices Data

## Prerequisites

state.json flags that must be true:
- `flags.practicesDietRestSupplementDrafted` must be `true` (set by step-04-author-practices-diet-rest-supplement)
- `flags.practicesExerciseStressDrafted` must be `true` (set by step-05-author-practices-exercise-stress)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-diet-rest-supplement.md` (created by Prompt 04)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-exercise-stress.md` (created by Prompt 05)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-diet-rest-supplement.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-exercise-stress.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\data-schema.md` (exact field names, enum values, priority rules, content authoring rules — use for validation checks during finalization)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read both draft files. Apply the following final checks and adjustments to every entry, then write the merged and finalized array to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-final.js`.

**Final checks to apply to every entry before including it:**

1. **Deduplication**: If any `id` appears more than once across both files, keep only the version with the most complete `action` field. Remove the duplicate.

2. **Plain-language test**: Read every `title`, `action`, and `why` as if you are a person with no health background. If any string is unclear, rewrite it for clarity — staying as close to the source module text as possible.

3. **Clinical abbreviation check**: Scan every string for: HPA, HPA-T, GI, SIBO, cortisol, adrenal, dysbiosis, pathogen, liver, detox. For each term found: if it lacks an immediate plain-language definition in parentheses, add one.

4. **Priority consistency check**: Verify that the sleep window entry (10 PM–6 AM) has `priority: 10`, blood sugar stabilization has `priority: 9` or `10`, and no supplementation entry exceeds `priority: 5`.

5. **Supplement safety check**: Confirm no supplementation entry contains a dosage amount, brand name, or lab-dependent protocol. If any does, remove that information and keep only the course-level foundational guidance.

6. **Minimum count check**: The finalized array must contain at least 12 entries. If the combined drafts contain fewer than 12, identify gaps in the required practice areas (see nnnn.md "Course module sourcing by DRESS component") and note which content is missing in a comment at the top of the file.

**Output format** — Write `practices-final.js` as follows:
```js
// DATA.dressPractices — finalized from FDN course modules 09, 10, 11, 12
// Minimum 12 entries required. Each entry verified against its source module.
// All strings plain-language tested. No clinical abbreviations without definitions.

const dressPracticesData = [
  {
    id: '...',
    dresComponent: '...',
    title: '...',
    action: '...',
    why: '...',
    frequency: '...',
    clusters: [...],
    priority: N,
    module: '...'
  },
  // ... all entries
];
```

The array must be named `dressPracticesData` and be a valid JavaScript `const` declaration. All string values use single quotes. All entries are complete — no placeholders.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-final.js` exists
- [ ] File contains `const dressPracticesData = [` at the start of the array declaration
- [ ] Array contains at least 12 complete entries
- [ ] Every entry has all 9 fields: id, dresComponent, title, action, why, frequency, clusters, priority, module
- [ ] No duplicate `id` values exist across all entries
- [ ] Sleep window entry has `priority: 10`
- [ ] No supplementation entry has a dosage, brand name, or lab-dependent instruction
- [ ] No user-visible string contains an unexplained clinical abbreviation

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-06-finalize-practices-data"` to `completedSteps`
2. Remove `"step-06-finalize-practices-data"` from `pendingSteps`
3. Set `flags.practicesDataFinalized` to `true`
4. Increment `artifacts.itemCount` by the total number of entries in `dressPracticesData`
5. Append `"fdn-practice-plan/orchestration/context/practices-final.js"` to `artifacts.filesWritten`
