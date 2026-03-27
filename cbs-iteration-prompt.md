```markdown
<role>
You are an orchestration architect specializing in the Claude Code Build Methodology. Your expertise is applying Stage 5 orchestration decomposition to monolithic build prompts — converting them into atomic sub-prompt packages that satisfy all six Tier 1 system integrity rules.
</role>

<context>
You are iterating on `CBS-prompt.md`, an existing build prompt with a critical structural problem: it violates multiple Tier 1 architectural constraints from the same methodology it is designed to implement.

THE VIOLATIONS IN CBS-PROMPT.MD:

Violation 1 — Rule 4 (Cardinal Failure Mode — One Atomic Task Per Prompt):
CBS-prompt.md is a single monolithic prompt that simultaneously asks: read 18 source files + copy 18 methodology files + copy 5 template files + write 4 phase prompt files + write 1 README + run verification. That is 29+ discrete verifiable units bundled into one prompt. The methodology names this the cardinal failure mode.

Violation 2 — Rule 2 (pendingSteps Fully Populated at Initialization):
CBS-prompt.md has no state.json. No step registry exists. No orchestration tracking exists.

Violation 3 — Rule 1 (Fresh Chat for Every Sub-Prompt Execution):
CBS-prompt.md executes all 29+ units in a single session. The methodology requires each unit to run in its own fresh chat.

Violation 4 — Rule 3 (Hard Constraints Verbatim in Every Prompt):
CBS-prompt.md contains none of the five required hard constraints.

Violation 5 — Rule 6 (State Update Before Session Exit):
No state.json means no state updates. Build progress cannot be tracked or resumed.

YOUR TASK: Apply Stage 5 orchestration decomposition to CBS-prompt.md and produce a fully methodology-compliant orchestration package that accomplishes the exact same build outcome.
</context>

<reading_directives>
Read ALL of the following files IN FULL before writing a single file. If any file cannot be read, halt immediately and report the error. Do not proceed with incomplete source material.

FILES TO READ (in this order):
1. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\CBS-prompt.md`
   Purpose: Extract the complete build task — all file contents to write, all source paths to copy from, all structural requirements
2. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\02-reverse-engineered\orchestration-decomposition-execution-plan.md`
   Purpose: The 9-step decomposition process you must follow exactly
3. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\sub-prompt-schema-template.md`
   Purpose: The exact template every prompt-NN.md must follow — copy hard constraints verbatim from here
4. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\state-schema-template.md`
   Purpose: The exact template for state.json initialization
5. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\readme-index-template.md`
   Purpose: The exact template for the orchestration README.md
6. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\system-integrity-rules.md`
   Purpose: The six Tier 1 rules every prompt-NN.md must satisfy
</reading_directives>

<thinking_process>
Execute in this exact sequence. Do not reorder. Do not skip steps. Verify each step before proceeding to the next.

STEP 1 — READ ALL 6 FILES
Read each file completely. Confirm all 6 are read before advancing.

STEP 2 — CATALOG ALL ATOMIC UNITS (orchestration-decomposition-execution-plan.md Step 1)
From CBS-prompt.md, enumerate every discrete unit of work. Apply the atomicity test to each: "Can this be completed and verified independently?" If NO → subdivide.

Expected categories:
- 1 initialization unit (write state.json)
- N methodology file copy units — one per file in bd-extraction/ (each file = one unit)
- 5 template file copy units — one per file in bd-extraction/03-templates/
- 4 phase prompt write units — one per phases/NN-*.md
- 1 README.md write unit
- 1 final verification unit

Document the complete catalog before writing any file.

STEP 3 — ESTABLISH EXECUTION ORDER (Step 3)
Order all units into a dependency sequence where no unit references files not yet created by a prior unit. Methodology and template copies are independent — order them logically (e.g., by subfolder). Phase prompts are independent of each other. README.md must come after all other files exist.

STEP 4 — DESIGN STATE.JSON SCHEMA (Step 5)
Before writing any file, finalize ALL step IDs:
- Format: step-NN-descriptive-name (zero-padded, kebab-case)
- Identify flags: at minimum methodologyFilesWritten, templateFilesWritten, phasePromptsWritten
- Set buildTarget: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\`
ALL step IDs must be locked here. Never add step IDs after state.json is written.

STEP 5 — WRITE ORCHESTRATION PACKAGE (Steps 6, 7, 8)
Write all files to: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system-orchestration\`

Order:
  a) Write state.json first — all step IDs in pendingSteps per state-schema-template.md
  b) Write README.md — execution index table per readme-index-template.md
  c) Write all prompt-NN.md files in sequence

For every prompt-NN.md:
  - Five hard constraints VERBATIM — copy word-for-word from sub-prompt-schema-template.md
  - One atomic task per file — no compound tasks
  - Verification section: measurable binary checks (yes/no), not subjective
  - State Update section: exact mutations listed

STEP 6 — VERIFY COMPLETE PACKAGE (Step 9)
Run all checks before declaring complete:
  - state.json has ALL step IDs in pendingSteps
  - README.md has one row per prompt
  - Every prompt-NN.md exists (count matches pendingSteps count)
  - Every prompt has all 5 required sections
  - No prerequisite references a file created by a later prompt
  - Five hard constraints are verbatim in every prompt (spot-check at least 3)
  - Every Task section contains exactly ONE verifiable unit
  - Phase prompt Task sections embed full content (no references to CBS-prompt.md)
</thinking_process>

<requirements>

## Content Rules for Each Prompt Category

### Methodology File Copy Prompts
Task format:
  "Read `[exact source path in bd-extraction/]` in full. Write its complete content verbatim to `[destination path in claude-build-system/methodology/]`. Do not paraphrase, summarize, or modify any content."
Verification:
  "File `[destination path]` exists. Its content is identical to `[source path]`."
State Update:
  Append step ID to completedSteps, remove from pendingSteps, append destination path to artifacts.filesWritten.

### Template File Copy Prompts
Task format:
  "Read `[exact source path in bd-extraction/03-templates/]` in full. Write its complete content verbatim to `[destination path in claude-build-system/templates/]`. Do not modify any content."
Verification:
  "File `[destination path]` exists. Its content is identical to `[source path]`."
State Update:
  Same pattern as methodology copies.

### Phase Prompt Write Prompts (01-discover, 02-engineer, 03-orchestrate, 04-ground)
CRITICAL RULE: The full specification for each phase prompt is in CBS-prompt.md's requirements section. That specification MUST be embedded verbatim in the Task section of the corresponding prompt-NN.md. Do not reference CBS-prompt.md in the task — the executing agent will have no access to it.

Task format:
  "Write `claude-build-system/phases/[NN]-[name].md` with the following complete content:
  [EMBED THE FULL PHASE SPECIFICATION FROM CBS-PROMPT.MD HERE — every word, every rule, every behavior instruction, every output specification]"

Verification:
  "File `claude-build-system/phases/[NN]-[name].md` exists and contains [specific verifiable element unique to that phase, e.g., 'the AskUserQuestion rule', 'the [PROJECT_FOLDER_PATH] placeholder', 'the 5-layer question sequence']."

### README.md Write Prompt
CRITICAL RULE: The full 14-step README content from CBS-prompt.md MUST be embedded verbatim in the Task section.

Task format:
  "Write `claude-build-system/README.md` with the following complete content:
  [EMBED THE EXACT 14-STEP README CONTENT FROM CBS-PROMPT.MD HERE]"

Verification:
  "File `claude-build-system/README.md` exists and contains exactly 14 numbered steps with binary decision points at steps 11 and 13."

### Final Verification Prompt
Task:
  "Verify that the complete claude-build-system/ structure exists and is correct."
Verification items (all must pass):
  - claude-build-system/README.md exists and contains 14 steps
  - All 4 phase files exist in claude-build-system/phases/
  - All methodology files exist in claude-build-system/methodology/ with preserved subfolder structure
  - All template files exist in claude-build-system/templates/
  - No file in bd-extraction/ was modified
  - No [project-name]/ project folder was created
  - phases/01-discover.md does NOT contain [PROJECT_FOLDER_PATH]
  - phases/02-engineer.md, 03-orchestrate.md, 04-ground.md each contain [PROJECT_FOLDER_PATH]

</requirements>

<constraints>
MUST:
- Five hard constraints MUST appear verbatim in every prompt-NN.md — copy from sub-prompt-schema-template.md exactly as written
- state.json MUST be written first with ALL step IDs in pendingSteps
- Phase prompt and README content MUST be embedded in Task sections — self-contained, no external references
- Every prompt MUST have exactly one atomic task

MUST NOT:
- Do NOT write to or modify any file in bd-extraction/ or in the CBS-prompt.md source location
- Do NOT create claude-build-system/ directly — the orchestration prompts do that at runtime
- Do NOT paraphrase the five hard constraints in any prompt file
- Do NOT bundle multiple file operations into one prompt unless they share a single verifiable completion condition
- Do NOT reference CBS-prompt.md inside any prompt-NN.md Task section
</constraints>

<success_criteria>
The iteration is complete and correct when ALL of the following are true:
1. `claude-build-system-orchestration/state.json` exists with all step IDs in pendingSteps and completedSteps empty
2. `claude-build-system-orchestration/README.md` exists with one row per prompt
3. All prompt-NN.md files exist — count matches pendingSteps array length exactly
4. Every prompt-NN.md has exactly 5 sections: Prerequisites, Hard Constraints, Task, Verification, State Update
5. Five hard constraints appear verbatim in every prompt (verified by spot-checking minimum 3 prompts)
6. Every Task section contains exactly ONE verifiable unit of work
7. No Prerequisites section references a file or flag created by a later-numbered prompt
8. Phase prompt Task sections embed complete phase content — no reference to CBS-prompt.md or any file not available in a fresh chat
9. Executing all prompts in order in fresh chats will produce an identical claude-build-system/ to what CBS-prompt.md described
</success_criteria>

<output_format>
After all files are written and Step 6 verification passes, display exactly this block and nothing else. Do not narrate your process. Do not summarize. Do not add commentary.

claude-build-system-orchestration/ created at C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system-orchestration\

Orchestration package:
  state.json — [N] steps in pendingSteps
  README.md — [N] rows
  prompt-01.md through prompt-[NN].md

Step breakdown:
  Prompts 01: Initialize state
  Prompts 02–[N]: Copy methodology files (bd-extraction/ → methodology/)
  Prompts [N+1]–[N+5]: Copy template files (bd-extraction/03-templates/ → templates/)
  Prompts [N+6]–[N+9]: Write phase prompts (phases/01 through 04)
  Prompt [N+10]: Write README.md
  Prompt [N+11]: Final verification

Integrity check:
  Rule 1 (fresh chat isolation): each prompt runs independently ✓
  Rule 2 (pendingSteps full): all [N] steps registered at init ✓
  Rule 3 (verbatim constraints): present in all [N] prompts ✓
  Rule 4 (one atomic task): one unit per prompt ✓
  Rule 6 (state update): every prompt has State Update section ✓

To execute: open claude-build-system-orchestration/README.md. Start with prompt-01.md in a fresh chat.
</output_format>
```
