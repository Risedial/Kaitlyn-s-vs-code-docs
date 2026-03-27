# Prompt 29: Verify Complete claude-build-system/ Structure

## Prerequisites

State file: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system-orchestration\state.json`

state.json flags that must be true:
- `flags.stateInitialized` must be `true` (set by step-01-initialize-state)
- `flags.methodologyFilesWritten` must be `true` (set by step-18-copy-methodology-universal-feedback-system)
- `flags.templateFilesWritten` must be `true` (set by step-23-copy-template-prompt-engineering-checklist)
- `flags.phasePromptsWritten` must be `true` (set by step-27-write-phase-04-ground)
- `flags.readmeWritten` must be `true` (set by step-28-write-readme)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Verify that the complete `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\` structure exists and is correct by checking every item in the Verification section below. Do not write any files. Do not modify any files. Report pass or fail for each item.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `claude-build-system\README.md` exists and contains exactly 14 numbered steps
- [ ] `claude-build-system\README.md` contains binary decision points at step 11 and step 13
- [ ] `claude-build-system\phases\01-discover.md` exists
- [ ] `claude-build-system\phases\02-engineer.md` exists
- [ ] `claude-build-system\phases\03-orchestrate.md` exists
- [ ] `claude-build-system\phases\04-ground.md` exists
- [ ] `phases\01-discover.md` does NOT contain the line `**USER ACTION REQUIRED BEFORE PASTING:**` (confirming no pre-paste replacement is required by the user)
- [ ] `phases\02-engineer.md` contains the string `[PROJECT_FOLDER_PATH]`
- [ ] `phases\03-orchestrate.md` contains the string `[PROJECT_FOLDER_PATH]`
- [ ] `phases\04-ground.md` contains the string `[PROJECT_FOLDER_PATH]`
- [ ] `claude-build-system\methodology\README.md` exists
- [ ] `claude-build-system\methodology\00-inventory\system-map.md` exists
- [ ] `claude-build-system\methodology\01-outcomes\outcome-registry.md` exists
- [ ] `claude-build-system\methodology\01-outcomes\fresh-chat-vs-chain-map.md` exists
- [ ] `claude-build-system\methodology\02-reverse-engineered\prompt-engineering-pipeline-execution-plan.md` exists
- [ ] `claude-build-system\methodology\02-reverse-engineered\orchestration-decomposition-execution-plan.md` exists
- [ ] `claude-build-system\methodology\02-reverse-engineered\context-state-system-execution-plan.md` exists
- [ ] `claude-build-system\methodology\03-templates\sub-prompt-schema-template.md` exists
- [ ] `claude-build-system\methodology\03-templates\state-schema-template.md` exists
- [ ] `claude-build-system\methodology\03-templates\context-file-template.md` exists
- [ ] `claude-build-system\methodology\03-templates\readme-index-template.md` exists
- [ ] `claude-build-system\methodology\03-templates\prompt-engineering-checklist.md` exists
- [ ] `claude-build-system\methodology\04-meta-system\approach-selection-decision-tree.md` exists
- [ ] `claude-build-system\methodology\04-meta-system\system-integrity-rules.md` exists
- [ ] `claude-build-system\methodology\04-meta-system\orchestration-spec.md` exists
- [ ] `claude-build-system\methodology\04-meta-system\parameter-extraction-algorithm.md` exists
- [ ] `claude-build-system\methodology\Universal feedback system\universal-feedbackloop-goal-system.md` exists
- [ ] `claude-build-system\templates\sub-prompt-schema-template.md` exists
- [ ] `claude-build-system\templates\state-schema-template.md` exists
- [ ] `claude-build-system\templates\context-file-template.md` exists
- [ ] `claude-build-system\templates\readme-index-template.md` exists
- [ ] `claude-build-system\templates\prompt-engineering-checklist.md` exists
- [ ] No file in `bd-extraction\` was modified (spot-check 3 files — confirm content matches original)
- [ ] No `[project-name]\` project folder was created inside `claude-build-system\`

If any check fails: identify which step is responsible, re-run that step's prompt in a fresh chat, then re-run this verification prompt.

---

## State Update

Perform these exact mutations to `state.json` after all Verification checks pass:

1. Append `"step-29-verify-complete-structure"` to `completedSteps`
2. Remove `"step-29-verify-complete-structure"` from `pendingSteps`
