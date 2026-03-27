# Prompt 08: Add Utility Functions to index.html

## Prerequisites

state.json flags that must be true:
- `flags.dataLayerAdded` must be `true` (set by step-07-add-data-layer)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\data-schema.md` (confirms DATA.dressPractices property name and entry structure referenced in utility functions)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Locate the JavaScript section where utility/helper functions are defined (after data declarations, before or alongside render functions — use codebase-patterns.md Section 2 and Section 10 to identify the correct location). Add the following five functions using the Edit tool. Match the existing function naming and coding style (camelCase, same comment style, same indentation) exactly.

Add all five functions together in a single contiguous block:

**Function 1 — getActiveClusters(selectedSymptomIds)**
```js
function getActiveClusters(selectedSymptomIds) {
  const clusters = [];
  selectedSymptomIds.forEach(id => {
    const symptom = DATA.symptoms[id];
    if (symptom && symptom.clusters) {
      symptom.clusters.forEach(c => {
        if (!clusters.includes(c)) clusters.push(c);
      });
    }
  });
  return clusters;
}
```

**Function 2 — getPracticesForClusters(clusters, selectedSymptomIds)**
```js
function getPracticesForClusters(clusters, selectedSymptomIds) {
  const seen = new Set();
  const results = [];
  DATA.dressPractices.forEach(practice => {
    if (practice.clusters.some(c => clusters.includes(c)) && !seen.has(practice.id)) {
      seen.add(practice.id);
      const triggerCount = selectedSymptomIds.filter(id => {
        const symptom = DATA.symptoms[id];
        return symptom && symptom.clusters && symptom.clusters.some(c => practice.clusters.includes(c));
      }).length;
      results.push(Object.assign({}, practice, { score: triggerCount * practice.priority }));
    }
  });
  return results.sort((a, b) => b.score - a.score);
}
```

**Function 3 — getTopPractices(practices, n)**
```js
function getTopPractices(practices, n) {
  return practices.slice(0, n || 7);
}
```

**Function 4 — groupByDressComponent(practices)**
```js
function groupByDressComponent(practices) {
  const order = ['diet', 'rest', 'exercise', 'stress', 'supplement'];
  const map = new Map();
  order.forEach(key => map.set(key, []));
  practices.forEach(p => {
    if (map.has(p.dresComponent)) map.get(p.dresComponent).push(p);
  });
  return map;
}
```

**Function 5 — computeSymptomHash(selectedSymptomIds)**
```js
function computeSymptomHash(selectedSymptomIds) {
  return [...selectedSymptomIds].sort().join(',');
}
```

Do NOT modify any existing function. Do NOT add a new `addEventListener`. Use the Edit tool to insert this block at the identified location.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `fdn-pwa/index.html` contains function `getActiveClusters`
- [ ] `fdn-pwa/index.html` contains function `getPracticesForClusters`
- [ ] `fdn-pwa/index.html` contains function `getTopPractices`
- [ ] `fdn-pwa/index.html` contains function `groupByDressComponent`
- [ ] `fdn-pwa/index.html` contains function `computeSymptomHash`
- [ ] No existing functions were modified

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-08-add-utility-functions"` to `completedSteps`
2. Remove `"step-08-add-utility-functions"` from `pendingSteps`
3. Set `flags.utilityFunctionsAdded` to `true`
