# Prompt 03: Verify selectedSymptomIds in App State

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

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` Section 6.

**If Section 6 says YES** (selectedSymptomIds or equivalent already exists in app state): this step is a no-op. The existing field name and location are sufficient; no modification to `fdn-pwa/index.html` is needed. Record the exact property name and location in `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\state-verification.md` with this format:

```
selectedSymptomIds: PRESENT
Exact property name: [name from codebase-patterns.md Section 6]
Location in state object: [location from codebase-patterns.md Section 6]
No modification to index.html required.
```

**If Section 6 says NO** (selectedSymptomIds is absent): Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Locate the top-level app state object identified in codebase-patterns.md Section 4. Add `selectedSymptomIds: []` as a new property on that state object. Use the Edit tool to make this targeted change only — do not modify any other part of the file. Then write `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\state-verification.md` with this format:

```
selectedSymptomIds: ADDED
Property name: selectedSymptomIds
Location: [state object name] in fdn-pwa/index.html
Modification made: added selectedSymptomIds: [] to [state object name]
```

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\state-verification.md` exists
- [ ] File contains either PRESENT or ADDED status
- [ ] If ADDED path: `fdn-pwa/index.html` contains `selectedSymptomIds: []` in the app state object
- [ ] No other modifications were made to `fdn-pwa/index.html` beyond the single property addition

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-03-verify-selected-symptoms-state"` to `completedSteps`
2. Remove `"step-03-verify-selected-symptoms-state"` from `pendingSteps`
3. Set `flags.selectedSymptomsStateVerified` to `true`
4. Append `"fdn-practice-plan/orchestration/context/state-verification.md"` to `artifacts.filesWritten`
