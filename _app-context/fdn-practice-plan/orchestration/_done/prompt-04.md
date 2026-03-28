# Prompt 04: Author Diet, Rest, and Supplement Practices from Modules 09 and 10

## Prerequisites

state.json flags that must be true:
- `flags.codebasePatternsDocumented` must be `true` (set by step-01-document-codebase-patterns)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md` (implementation specification — data entry field definitions and content rules)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\data-schema.md` (exact field names, enum values, cluster codes, priority calibration — authoritative reference for all DATA.dressPractices entries)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read ALL files in these two directories before authoring any practice entries:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\research-source-content\course\module-09\` (Diet content)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\research-source-content\course\module-10\` (Rest and Supplementation content)

After reading, author all Diet, Rest, and Supplementation practice entries. Write them to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-diet-rest-supplement.md`.

**Content authoring rules (apply to every entry):**
- `action`: Write the exact step-by-step instructions sourced from the module text. No synthesis from training memory. Paraphrase is permitted only when the source text is not user-readable as-is — stay as close to the source as possible.
- `why`: One sentence in first-person framing: "This helps your body..." sourced from the module. Not "Studies show..."
- `module`: Set to the exact module number the content was sourced from (e.g., `"09"` or `"10"`)
- `title`: Plain-language name for the practice. No clinical abbreviations. No jargon.
- Apply the plain-language test: a person with no health background must be able to read every string and immediately understand what to do and why.
- No clinical abbreviations (HPA, GI, SIBO, etc.) without an immediate plain-language definition in parentheses.

**Diet practices to author** (source: module-09):
- Blood sugar stabilization: eat protein, fat, and fiber at every meal to keep energy stable
- Eliminate refined carbohydrates for a 90-day reset
- Track satiety and energy response after meals

**Rest practices to author** (source: module-10):
- Consistent sleep window: go to bed by 10 PM and wake at 6 AM
- Sleep environment: blackout curtains, cool room, no noise
- No screens 2 hours before bed
- Small protein + low-glycemic carb snack before sleep

**Supplementation practices to author** (source: module-10):
- Foundational mineral support before sleep (no dosages, no brands — course-level guidance only)

**Required fields for each entry** (from nnnn.md):
```
id: 'kebab-case-unique-id'
dresComponent: 'diet' | 'rest' | 'supplement'
title: 'Plain-language name'
action: 'Exact instructions from module'
why: 'One sentence, first-person framing'
frequency: 'daily' | 'weekly' | 'as-needed'
clusters: ['A', 'B', 'C', 'D', 'E']  // use correct cluster codes per cluster-to-DRESS mapping
priority: 1–10  // see calibration below
module: '09' or '10'
```

**Priority calibration:**
- 9–10: Sleep window (10 PM–6 AM) and blood sugar stabilization — highest impact
- 7–8: Broadly foundational practices applicable across multiple clusters
- 4–6: Component-specific practices with moderate cluster overlap
- 3–5: Supplementation entries

**Cluster assignments for DRESS components:**
- Diet → Clusters A, C, D (also include E for universal baseline practices)
- Rest → Clusters B, E (also include A, C, D for universal sleep practices)
- Supplement → Clusters B, E

Format the output file as valid JavaScript object literals (not wrapped in an array — that comes in Prompt 06). Each entry should be a full JS object starting with `{` and ending with `},` on its own line, like:
```js
{
  id: 'sleep-window-10pm',
  dresComponent: 'rest',
  title: 'Set a consistent sleep window',
  action: '...',
  why: '...',
  frequency: 'daily',
  clusters: ['A', 'B', 'C', 'D', 'E'],
  priority: 10,
  module: '10'
},
```

After every entry, include a one-line comment: `// Source: Module [N], [brief topic]`

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\practices-diet-rest-supplement.md` exists
- [ ] File contains at least 8 practice entries covering diet (3+), rest (4+), and supplement (1+) components
- [ ] Every entry contains all 9 required fields: id, dresComponent, title, action, why, frequency, clusters, priority, module
- [ ] Every entry includes a `// Source: Module [N]` comment
- [ ] No entry contains clinical abbreviations without plain-language definitions in parentheses
- [ ] No entry `why` field uses "Studies show..." framing — all use first-person "This helps your body..." framing
- [ ] `dresComponent` values are exactly `'diet'`, `'rest'`, or `'supplement'` — no other values
- [ ] `module` values are `"09"` or `"10"` only

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-04-author-practices-diet-rest-supplement"` to `completedSteps`
2. Remove `"step-04-author-practices-diet-rest-supplement"` from `pendingSteps`
3. Set `flags.practicesDietRestSupplementDrafted` to `true`
4. Append `"fdn-practice-plan/orchestration/context/practices-diet-rest-supplement.md"` to `artifacts.filesWritten`
5. Set `dataChunks.practicesDraft.dietRestSupplement` to `"complete"`
