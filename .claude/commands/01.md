# Prompt 01: Initialize State

## Prerequisites

none

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system-orchestration\state.json` in full. Confirm that `completedSteps` is empty, `pendingSteps` contains all 29 step IDs beginning with `"step-01-initialize-state"`, and all flags are `false`. Then update `state.json` by setting `flags.stateInitialized` to `true`, appending `"step-01-initialize-state"` to `completedSteps`, and removing `"step-01-initialize-state"` from `pendingSteps`.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system-orchestration\state.json` exists and is valid JSON
- [ ] `pendingSteps` originally contained all 29 step IDs
- [ ] After update: `completedSteps` contains exactly `["step-01-initialize-state"]`
- [ ] After update: `flags.stateInitialized` is `true`
- [ ] After update: `pendingSteps` contains 28 step IDs (step-02 through step-29)

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `state.json` after all Verification checks pass:

1. Append `"step-01-initialize-state"` to `completedSteps`
2. Remove `"step-01-initialize-state"` from `pendingSteps`
3. Set `flags.stateInitialized` to `true`
