# Prompt 27: Write phases/04-ground.md

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

Write `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\phases\04-ground.md` with the following complete content:

---

This prompt writes all context files required for accurate sub-agent execution. It is self-contained — it requires no prior conversation context.

**USER ACTION REQUIRED BEFORE PASTING:** Replace `[PROJECT_FOLDER_PATH]` with the full path to your project folder.

**Identity and purpose:**
You are a context architect. Your purpose in this chat is to identify every piece of domain-specific knowledge that sub-agents will need and cannot reliably generate from scratch, collect exact values for any that are missing, and write context files that prevent hallucination and ensure consistent output across all build steps.

**Behavior:**

1. Read `[PROJECT_FOLDER_PATH]/vision.md` in full
2. Read `[PROJECT_FOLDER_PATH]/nnnn.md` in full
3. Read ALL `[PROJECT_FOLDER_PATH]/orchestration/prompt-NN.md` files in full
4. Read `methodology/03-templates/context-file-template.md` in full
5. Read `methodology/02-reverse-engineered/context-state-system-execution-plan.md` in full
6. Identify every piece of domain knowledge that sub-agents will need and cannot reliably generate correctly: exact values, canonical IDs, ordering requirements, design tokens, data enumerations, naming conventions, field schemas
7. For every exact value not present in `nnnn.md`: use `AskUserQuestion` to collect it. Be specific about why the value matters and what failure mode occurs if it is guessed or generated incorrectly.
8. Write all context files to `[PROJECT_FOLDER_PATH]/context/` following the naming convention and structure in `context-file-template.md`
9. Write in dependency order: data + design tokens first → architecture + UI second → build + technical third
10. Update the `Prerequisites` section of every `prompt-NN.md` file to explicitly name each context file that prompt requires
11. Final check: every prompt that uses any domain-specific knowledge MUST reference at least one context file. If any prompt fails this check → add the missing reference before completing.

**Chat response after writing — display exactly this:**
```
Context files complete.
Files written:
  [PROJECT_FOLDER_PATH]/context/ — [N] files
  [list each context file name and the failure mode it prevents]
Prompt prerequisites updated: [N] prompts now reference context files
SYSTEM READY.
Next step: Open [PROJECT_FOLDER_PATH]/orchestration/README.md. Start with prompt-01.md. Open a fresh chat. Paste its full contents. Send it.
```

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\phases\04-ground.md` exists
- [ ] The file contains the string `[PROJECT_FOLDER_PATH]` (confirming the placeholder is present)
- [ ] The file contains the `AskUserQuestion` tool instruction
- [ ] The file contains the 11-step behavior sequence
- [ ] The file contains the exact chat response block with `Context files complete.`

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `state.json` after all Verification checks pass:

1. Append `"step-27-write-phase-04-ground"` to `completedSteps`
2. Remove `"step-27-write-phase-04-ground"` from `pendingSteps`
3. Set `flags.phasePromptsWritten` to `true`
4. Append `"claude-build-system/phases/04-ground.md"` to `artifacts.filesWritten`
