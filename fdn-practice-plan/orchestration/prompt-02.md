# Prompt 02: Verify Clusters Field in DATA.symptoms

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

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` Section 5.

**If Section 5 says YES** (clusters field already exists on all DATA.symptoms entries): this step is a no-op. Write a single-line confirmation file at `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\cluster-verification.md` with the text: `clusters[] field confirmed present on DATA.symptoms entries. No modification required.`

**If Section 5 says NO** (clusters field absent): This is a blocking prerequisite gap. The feature cannot be built without cluster assignments on symptom data, and these assignments are health-domain content that must not be synthesized. Write `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\cluster-verification.md` with the following message:

```
BLOCKING GAP: clusters[] field is absent from DATA.symptoms entries.

Required action before proceeding with this build:
Each DATA.symptoms entry must have a `clusters: []` array field populated with the correct cluster codes ('A', 'B', 'C', 'D', 'E') for that symptom.

This assignment requires reading the FDN course module files to determine which symptoms belong to which clusters. Cluster assignments are health-domain content and must be sourced from named course files — they cannot be synthesized.

Source files for cluster assignments:
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\research-source-content\course\module-09\
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\research-source-content\course\module-10\
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\research-source-content\course\module-11\
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\research-source-content\course\module-12\

Do NOT proceed with steps 07–16 until clusters[] arrays are present and verified on all DATA.symptoms entries.
```

Do NOT attempt to add cluster assignments to index.html in this step.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\cluster-verification.md` exists
- [ ] File contains either a confirmation message (YES path) or the BLOCKING GAP message (NO path)
- [ ] If YES path: the confirmation message explicitly states the field is present

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-02-verify-clusters-field"` to `completedSteps`
2. Remove `"step-02-verify-clusters-field"` from `pendingSteps`
3. Set `flags.clustersFieldVerified` to `true`
4. Append `"fdn-practice-plan/orchestration/context/cluster-verification.md"` to `artifacts.filesWritten`
