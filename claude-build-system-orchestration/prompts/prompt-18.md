# Prompt 18: Copy Methodology File — Universal feedback system/universal-feedbackloop-goal-system.md

## Prerequisites

State file: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system-orchestration\state.json`

state.json flags that must be true:
- `flags.stateInitialized` must be `true` (set by step-01-initialize-state)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\Universal feedback system\universal-feedbackloop-goal-system.md` in full. Write its complete content verbatim to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\methodology\Universal feedback system\universal-feedbackloop-goal-system.md`. Do not paraphrase, summarize, or modify any content. This is the final methodology file. After writing it, set `flags.methodologyFilesWritten` to `true` in state.json.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\methodology\Universal feedback system\universal-feedbackloop-goal-system.md` exists
- [ ] Its content is identical to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\Universal feedback system\universal-feedbackloop-goal-system.md`
- [ ] No content was paraphrased, summarized, or modified
- [ ] All 17 methodology files now exist in `claude-build-system\methodology\`

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `state.json` after all Verification checks pass:

1. Append `"step-18-copy-methodology-universal-feedback-system"` to `completedSteps`
2. Remove `"step-18-copy-methodology-universal-feedback-system"` from `pendingSteps`
3. Set `flags.methodologyFilesWritten` to `true`
4. Append `"claude-build-system/methodology/Universal feedback system/universal-feedbackloop-goal-system.md"` to `artifacts.filesWritten`
