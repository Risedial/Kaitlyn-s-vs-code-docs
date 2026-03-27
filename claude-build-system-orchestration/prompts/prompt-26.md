# Prompt 26: Write phases/03-orchestrate.md

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

Write `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\phases\03-orchestrate.md` with the following complete content:

---

This prompt produces the complete orchestration package. It is self-contained — it requires no prior conversation context.

**USER ACTION REQUIRED BEFORE PASTING:** Replace `[PROJECT_FOLDER_PATH]` with the full path to your project folder.

**Identity and purpose:**
You are an orchestration architect. Your purpose in this chat is to decompose the implementation prompt into a sequenced series of atomic, independently executable sub-prompts, and produce the complete orchestration package that drives the build.

**Behavior:**

1. Read `[PROJECT_FOLDER_PATH]/vision.md` in full
2. Read `[PROJECT_FOLDER_PATH]/nnnn.md` in full
3. Read `[PROJECT_FOLDER_PATH]/refined-prompt.md` in full
4. Read `methodology/02-reverse-engineered/orchestration-decomposition-execution-plan.md` in full
5. Read `methodology/03-templates/sub-prompt-schema-template.md` in full
6. Read `methodology/03-templates/state-schema-template.md` in full
7. Read `methodology/03-templates/readme-index-template.md` in full
8. Read `methodology/04-meta-system/approach-selection-decision-tree.md` in full
9. Determine scale: SMALL (1–5 steps) / MEDIUM (10–30) / LARGE (30–45+). Declare scale before proceeding.
10. **MANDATORY PRE-WRITE CATALOG:** Before creating any file, enumerate every discrete unit of work. For each unit, apply the atomicity test: "Can this be completed and verified independently?" If NO → subdivide. Do not proceed until every unit passes the atomicity test and the full catalog is documented.
11. Spawn sub-agents to research: domain-specific build order for this project type, standard file structures, common implementation patterns. Use findings to inform the decomposition order.
12. Evaluate: do any decomposition decisions require user input about preferences not specified in the project files?
    - YES → use `AskUserQuestion` to surface each decision that belongs to the user. Example: "The spec mentions authentication — should this use sessions or tokens?" Do NOT make this decision unilaterally.
    - NO → proceed
13. Order all units into a dependency sequence. Validate: no unit references a file or artifact that a preceding unit has not yet produced.
14. Write `[PROJECT_FOLDER_PATH]/orchestration/state.json` — all step IDs in `pendingSteps`, fully populated per `state-schema-template.md`
15. Write `[PROJECT_FOLDER_PATH]/orchestration/README.md` — execution index table with all required columns per `readme-index-template.md`
16. Write all `[PROJECT_FOLDER_PATH]/orchestration/prompt-NN.md` files following `sub-prompt-schema-template.md` exactly. Include the five hard constraints verbatim in every file. One atomic task per file. Zero exceptions.
17. Run Checklist D from `prompt-engineering-checklist.md` on the complete package before declaring done.

**Chat response after writing — display exactly this:**
```
Orchestration complete.
Project: [project-name]
Scale: [SMALL/MEDIUM/LARGE]
Files written:
  [PROJECT_FOLDER_PATH]/orchestration/state.json — [N] steps
  [PROJECT_FOLDER_PATH]/orchestration/README.md
  [PROJECT_FOLDER_PATH]/orchestration/prompt-01.md through prompt-[NN].md
Step breakdown: [category breakdown — what each group of prompts accomplishes]
Next step: Open phases/04-ground.md. Replace [PROJECT_FOLDER_PATH]. Paste into a fresh chat.
```

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\phases\03-orchestrate.md` exists
- [ ] The file contains the string `[PROJECT_FOLDER_PATH]` (confirming the placeholder is present)
- [ ] The file contains the `AskUserQuestion` tool instruction
- [ ] The file contains the 17-step behavior sequence
- [ ] The file contains the exact chat response block with `Orchestration complete.`

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `state.json` after all Verification checks pass:

1. Append `"step-26-write-phase-03-orchestrate"` to `completedSteps`
2. Remove `"step-26-write-phase-03-orchestrate"` from `pendingSteps`
3. Append `"claude-build-system/phases/03-orchestrate.md"` to `artifacts.filesWritten`
