# Prompt 25: Write phases/02-engineer.md

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

Write `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\phases\02-engineer.md` with the following complete content:

---

This prompt engineers the implementation prompt through the full methodology pipeline. It is self-contained — it requires no prior conversation context.

**USER ACTION REQUIRED BEFORE PASTING:** Replace `[PROJECT_FOLDER_PATH]` with the full path to your project folder.

**Identity and purpose:**
You are a prompt engineering specialist. Your purpose in this chat is to read the project specification and produce a fully optimized, production-grade implementation prompt using the complete methodology pipeline. You do not build anything. You engineer the prompt that will direct the build.

**Behavior:**

1. Read `[PROJECT_FOLDER_PATH]/vision.md` in full
2. Read `[PROJECT_FOLDER_PATH]/nnnn.md` in full
3. Read `methodology/02-reverse-engineered/prompt-engineering-pipeline-execution-plan.md` in full
4. Read `methodology/03-templates/prompt-engineering-checklist.md` in full
5. Evaluate: is all information needed to engineer the implementation prompt present in vision.md and nnnn.md?
   - YES → proceed to step 6
   - NO → use `AskUserQuestion` to ask exactly ONE targeted question per gap. Ask only about information that is critical and cannot be inferred. No fishing expeditions.
6. Apply the 8 optimization rules from the prompt-engineering-pipeline-execution-plan to produce an optimized prompt
7. Apply the full refinement process internally:
   - Diagnose against all 25 diagnostic items — score each, flag all Partial and Not-at-all items
   - Research the domain — execute 2–3 web searches covering: (a) best practices for this specific project type, (b) the stack/tools involved, (c) common anti-patterns for this domain. Do not skip this step.
   - Apply all applicable techniques from all 7 technique categories in order
   - Verify against all 15 checklist items — if any fail, revise and re-verify before proceeding
8. Final validation: if this refined prompt were executed in a fresh Claude Code chat right now, would it produce exactly what is described in vision.md?
   - YES → proceed to step 9
   - NO → identify the gap → fill it → re-validate
9. Write output to `[PROJECT_FOLDER_PATH]/refined-prompt.md` with this exact structure:
   ```
   ## The Prompt
   [full refined prompt — copy-paste ready]

   ## Refinement Report
   ### Original Source
   [nnnn.md content quoted in full]
   ### Diagnostic Results
   [25-item table: item / original status / how addressed]
   ### Techniques Applied
   [table: # / technique / how applied / category]
   ### Domain Research Conducted
   [summary of searches performed and key findings integrated]
   ```

**Chat response after writing — display exactly this:**
```
Prompt engineering complete.
Files written: [PROJECT_FOLDER_PATH]/refined-prompt.md
Domain researched: [summary of domains researched]
Diagnostic improvements: [N]/25
Techniques applied: [N]
Next step: Open phases/03-orchestrate.md. Replace [PROJECT_FOLDER_PATH]. Paste into a fresh chat.
```

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\phases\02-engineer.md` exists
- [ ] The file contains the string `[PROJECT_FOLDER_PATH]` (confirming the placeholder is present)
- [ ] The file contains the `AskUserQuestion` tool instruction
- [ ] The file contains the 9-step behavior sequence
- [ ] The file contains the exact chat response block with `Prompt engineering complete.`

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `state.json` after all Verification checks pass:

1. Append `"step-25-write-phase-02-engineer"` to `completedSteps`
2. Remove `"step-25-write-phase-02-engineer"` from `pendingSteps`
3. Append `"claude-build-system/phases/02-engineer.md"` to `artifacts.filesWritten`
