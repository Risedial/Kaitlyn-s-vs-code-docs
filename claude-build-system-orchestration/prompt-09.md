# Prompt 09: Copy Methodology File — 03-templates/sub-prompt-schema-template.md

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

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\sub-prompt-schema-template.md` in full. Write its complete content verbatim to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\methodology\03-templates\sub-prompt-schema-template.md`. Do not paraphrase, summarize, or modify any content.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\methodology\03-templates\sub-prompt-schema-template.md` exists
- [ ] Its content is identical to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\sub-prompt-schema-template.md`
- [ ] No content was paraphrased, summarized, or modified

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `state.json` after all Verification checks pass:

1. Append `"step-09-copy-methodology-sub-prompt-schema-template"` to `completedSteps`
2. Remove `"step-09-copy-methodology-sub-prompt-schema-template"` from `pendingSteps`
3. Append `"claude-build-system/methodology/03-templates/sub-prompt-schema-template.md"` to `artifacts.filesWritten`
