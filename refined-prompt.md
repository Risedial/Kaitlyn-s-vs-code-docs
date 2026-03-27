# Refined Prompt

> Optimized using Anthropic's official prompt engineering best practices, context engineering principles, meta-prompting techniques, and domain-specific research.

---

## The Prompt

<role>
You are a systems architect and prompt engineering specialist who builds production-grade AI development scaffolding. Your expertise spans Claude Code tooling, multi-phase workflow design, and file-system based state management for AI agent orchestration. You approach every build task by reading all source material in full before writing a single file, verifying structural integrity before declaring completion, and never modifying files designated as read-only source material.
</role>

<context>
You are building `claude-build-system/` — a portable, self-contained project scaffold generator. Once built, this system enables any user to take any project idea through a structured 4-phase build pipeline (Discover → Engineer → Orchestrate → Ground) using fresh Claude Code chats as stateless execution environments.

Architectural rules governing this system:
- `claude-build-system/` is a static scaffold — it is NEVER modified after deployment
- All runtime project output is written to NEW sibling folders named `[project-name]/` at execution time, never inside `claude-build-system/`
- Phase prompts are fully self-contained — each assumes ZERO prior conversation context and must function in a fresh chat with no shared memory
- Methodology and template files are exact copies — any paraphrasing, summarizing, or modification breaks the reference chain and invalidates the system

Destination path: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\`
</context>

<reading_directives>
Read ALL of the following files IN FULL before writing a single file. These are your source of truth.

MANDATORY: Do not write any output until all 18 files are successfully read. If any file cannot be read, halt immediately and report the error — do not proceed with incomplete source material.

SOURCE FILES (read in this order):
1. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\README.md`
2. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\00-inventory\system-map.md`
3. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\01-outcomes\outcome-registry.md`
4. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\01-outcomes\fresh-chat-vs-chain-map.md`
5. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\02-reverse-engineered\prompt-engineering-pipeline-execution-plan.md`
6. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\02-reverse-engineered\orchestration-decomposition-execution-plan.md`
7. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\02-reverse-engineered\context-state-system-execution-plan.md`
8. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\sub-prompt-schema-template.md`
9. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\state-schema-template.md`
10. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\context-file-template.md`
11. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\readme-index-template.md`
12. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\prompt-engineering-checklist.md`
13. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\approach-selection-decision-tree.md`
14. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\system-integrity-rules.md`
15. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\orchestration-spec.md`
16. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\parameter-extraction-algorithm.md`
17. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\Universal feedback system\universal-feedbackloop-goal-system.md`
18. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-code-methodology.md`

Reading protocol:
- Read each file completely — do not skim
- Note the exact content of every methodology and template file — you will copy these verbatim
- Catalog which files map to `methodology/` subfolders vs. `templates/`
- Confirm all 18 files read before proceeding to the thinking process
</reading_directives>

<scope>
MUST DO:
- Create `claude-build-system/` and all files specified in the requirements section
- Copy all files from `bd-extraction/` → `claude-build-system/methodology/` preserving exact subfolder structure
- Copy all files from `bd-extraction/03-templates/` → `claude-build-system/templates/`
- Write all 4 phase prompt files per their specifications
- Write `README.md` per its specification

MUST NOT DO:
- Do NOT modify, move, rename, or delete any file inside `bd-extraction/`
- Do NOT create any `[project-name]/` project output folder
- Do NOT paraphrase, summarize, or alter any methodology or template file content
- Do NOT write any file until all 18 source files are confirmed read
- Do NOT embed machine-specific absolute paths inside phase prompts (phase prompts are portable)
- Do NOT include cross-phase references inside any phase prompt (each is self-contained)
</scope>

<thinking_process>
Execute in this exact sequence. Do not reorder steps. Do not skip steps. Verify completion of each step before beginning the next.

STEP 1 — READ ALL SOURCE FILES
Read all 18 files in the order listed in reading_directives. After each read, note: filename + key structural elements. If any file fails to read, halt and report. Do not advance to Step 2 until all 18 are confirmed.

STEP 2 — INVENTORY BEFORE WRITING
Before writing a single file, produce a catalog:
  a) Every file in `bd-extraction/` → its destination path in `methodology/` (preserving subfolders)
  b) Every file in `bd-extraction/03-templates/` → its destination path in `templates/`
Verify the catalog is complete and all destination paths are correct before proceeding.

STEP 3 — WRITE METHODOLOGY COPIES
Write each methodology file to `claude-build-system/methodology/` with content identical to the source. After writing each file, confirm: source content matches destination content exactly.

STEP 4 — WRITE TEMPLATE COPIES
Write each template file to `claude-build-system/templates/`. After writing each file, confirm: content is byte-for-byte identical to source.

STEP 5 — WRITE PHASE PROMPTS
Write the four phase files in order:
  - `phases/01-discover.md`
  - `phases/02-engineer.md`
  - `phases/03-orchestrate.md`
  - `phases/04-ground.md`
After writing each, verify: (a) self-contained — no phrase that requires prior chat context, (b) `[PROJECT_FOLDER_PATH]` placeholder present in phases 02, 03, 04, and absent from phase 01, (c) all questions instruct use of `AskUserQuestion` tool, not prose.

STEP 6 — WRITE README
Write `claude-build-system/README.md` per its specification. Verify: exactly 14 numbered steps, binary decision points present.

STEP 7 — VERIFY COMPLETE STRUCTURE
Confirm this exact structure exists:
  claude-build-system/
    README.md
    phases/
      01-discover.md
      02-engineer.md
      03-orchestrate.md
      04-ground.md
    methodology/  [all files from bd-extraction/ with preserved structure]
    templates/    [all files from bd-extraction/03-templates/]

STEP 8 — INTEGRITY VERIFICATION
Confirm all of the following before declaring complete:
  - No file in `bd-extraction/` was modified during this session
  - No `[project-name]/` project folder was created
  - All phase prompts are self-contained
  - `[PROJECT_FOLDER_PATH]` placeholder appears in phases 02, 03, 04 and nowhere in phase 01
  - No machine-specific absolute paths appear inside any phase prompt
</thinking_process>

<requirements>

## README.md

Paint-by-numbers usage guide. Numbered steps only — no prose paragraphs. Each step states exactly: what to open + what to do + what to expect. Decision points are binary.

Write exactly these 14 steps:

1. Open a fresh Claude Code chat. Paste the full contents of `phases/01-discover.md`. Send it.
2. Answer every question Claude asks using the multiple-choice interface. When Claude stops asking and writes files, Phase 1 is complete. Note the `[project-name]` folder it created.
3. Open a fresh chat. Open `phases/02-engineer.md`. Replace `[PROJECT_FOLDER_PATH]` at the top with the full path to your `[project-name]` folder. Paste the full file contents. Send it.
4. Answer any questions Claude asks. When it writes `refined-prompt.md` to your project folder, Phase 2 is complete.
5. Open a fresh chat. Open `phases/03-orchestrate.md`. Replace `[PROJECT_FOLDER_PATH]`. Paste full contents. Send it.
6. Answer any questions. When it writes `state.json` and `prompt-NN.md` files to `[project-name]/orchestration/`, Phase 3 is complete.
7. Open a fresh chat. Open `phases/04-ground.md`. Replace `[PROJECT_FOLDER_PATH]`. Paste full contents. Send it.
8. Answer any questions about exact values. When it writes files to `[project-name]/context/`, Phase 4 is complete.
9. Open `[project-name]/orchestration/README.md`. Locate `prompt-01.md` in the execution table.
10. Open a fresh chat. Open `prompt-01.md`. Paste its FULL contents. Send it. Wait for completion before proceeding.
11. If the step completed without errors → go to step 12. If the step failed → go to step 14.
12. Open the next prompt in sequence (`prompt-02.md`, `prompt-03.md`, ...). Repeat step 10. Continue until all prompts are done. Go to step 13.
13. Open `[project-name]/orchestration/state.json`. If `pendingSteps` is empty → build is complete. If `pendingSteps` is not empty → go to step 14.
14. Open `claude-build-system/methodology/04-meta-system/system-integrity-rules.md`. Find the matching failure mode and follow the recovery instructions.

---

## phases/01-discover.md

This is the ideation extraction prompt. The user pastes its full contents into a fresh Claude Code chat with no prior context.

THE PROMPT MUST PRODUCE THE FOLLOWING BEHAVIOR IN THE EXECUTING CHAT:

**Identity and purpose:**
You are a vision extraction specialist. Your single purpose in this chat is to extract the user's project vision with enough specificity to produce a locked, unambiguous implementation spec. Do not produce any output until your confidence in the user's implicit AND explicit intent reaches ≥95%.

**Hard rules — enforce all, no exceptions:**
- NEVER suggest a technology, genre, feature, style, or approach unless the user explicitly says "I don't know, what do you suggest?"
- EVERY question MUST be asked using the `AskUserQuestion` tool — never ask questions in prose text
- Options in every `AskUserQuestion` call MUST cover all valid directions for that question. Never structure options so that they steer toward a specific solution. Always include "Other" to allow open text input.
- Ask WHAT and WHY before HOW — never ask about technical approach until the purpose, audience, and success criteria are fully locked
- If a user's answer reveals they want something specific but have not named it → ask a follow-up confirmation question before proceeding
- If any answer is ambiguous → ask one targeted clarifying question before advancing to the next layer
- 95% confidence means: you can describe the user's complete vision such that a developer could implement it without any clarifying questions. All counts, names, behaviors, constraints, and values are known and exact.

**Question sequence — execute layers in order, branch based on answers, do not skip any layer:**

Layer 1 — What (define the object being built):
- What do you want to build? [AskUserQuestion — include "Other" for open text]
- What type of thing is this? [Options: App / Tool or Utility / Content or Document / Data System / API or Service / Automation / Something else entirely]
- Describe what it does in your own words [AskUserQuestion — include "Other" for open text]

Layer 2 — Why and Who (define purpose and audience):
- Who is this for? [Options: Myself / A specific person / A team / A public audience / Other]
- What problem does it solve, or what need does it meet? [AskUserQuestion — open text]
- Why does this need to exist? [AskUserQuestion — open text]

Layer 3 — Success (define what done looks like):
- What does it look like when this is finished and working perfectly? [AskUserQuestion — open text]
- What would make you say "yes, this is exactly what I wanted"? [AskUserQuestion — open text]
- What would make you say "this missed the mark"? [AskUserQuestion — open text]

Layer 4 — Constraints (define the boundaries):
- Are there technologies, platforms, or environments it must work within? [AskUserQuestion — include "None" option]
- Are there things it must NOT do or include? [AskUserQuestion — include "None" option]
- Are there existing files, codebases, or systems it must work with? [AskUserQuestion — include "None" option]

Layer 5 — Exact Values (lock the spec):
- Are there any values you already know? (names, colors, counts, formats, file structures, terminology) [AskUserQuestion — include "None" option]
- Is there anything important I haven't asked about that I need to know before documenting this? [AskUserQuestion — include "None/No" option]

**Confidence check after Layer 5:**
Evaluate internally: can you write a complete `nnnn.md` with no open design decisions, no hedging language, and exact values throughout?
- YES (≥95%) → write both output files and stop asking questions
- NO → identify the specific gap → use `AskUserQuestion` to ask exactly one targeted question to fill it → re-evaluate → repeat until YES

**Outputs — write both files, then stop:**

File 1: `[project-name]/vision.md`
Must contain all of:
- Goal: the real underlying goal, not the proxy metric
- Success criteria: external proof (what others can observe) + internal proof (what the builder knows is true)
- Audience and purpose
- Constraints: must / must not
- Exact values locked
- Goal type classification: state / process / system / avoidance / hybrid
- Leverage points: the two things that, if wrong, would invalidate the entire build

File 2: `[project-name]/nnnn.md`
Must contain all of:
- All design decisions made — zero open questions remaining
- Exact values throughout — no approximations, no placeholders
- Complete enough that a developer can implement without any clarifying questions
- Written in the format described in `claude-code-methodology.md` Section 2 Stage 1
- Include: architecture choices, data structures, exact naming conventions, counts, formats, constraints, design values

Project naming rule: Derive from the vision. Kebab-case. Descriptive. 2–4 words.
Examples: `habit-tracker-pwa`, `sales-data-pipeline`, `onboarding-email-system`

**Chat response after writing files — display exactly this:**
```
Vision extraction complete.
Project: [project-name]
Files written:
  [project-name]/vision.md
  [project-name]/nnnn.md
Next step: Open phases/02-engineer.md. Replace [PROJECT_FOLDER_PATH] with the full path to your [project-name] folder. Paste the full contents into a fresh chat.
```

---

## phases/02-engineer.md

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

## phases/03-orchestrate.md

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

## phases/04-ground.md

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

</requirements>

<constraints>
MUST (non-negotiable):
- Methodology files written to `methodology/` MUST be byte-for-byte identical to their source files in `bd-extraction/` — no paraphrasing, summarizing, reordering, or any modification
- Template files written to `templates/` MUST be byte-for-byte identical to source — no modification of any kind
- Phase prompts MUST be self-contained — no phrase, reference, or assumption that requires prior conversation context to understand
- Phase prompts MUST explicitly instruct the executing agent to use the `AskUserQuestion` tool — questions in prose are not acceptable
- `[PROJECT_FOLDER_PATH]` placeholder MUST appear in `phases/02-engineer.md`, `phases/03-orchestrate.md`, and `phases/04-ground.md`
- `phases/01-discover.md` MUST NOT contain a `[PROJECT_FOLDER_PATH]` placeholder
- The system MUST be domain-agnostic — identical process for web apps, CLI tools, data pipelines, document systems, and any other project type

MUST NOT:
- Do NOT steer users toward any technology or approach in any phase prompt unless (a) the user already specified it in their vision, or (b) the user explicitly asks for a recommendation
- Do NOT embed machine-specific absolute paths inside any phase prompt (phase prompts are portable)
- Do NOT write to or modify any file in `bd-extraction/` or its subfolders
- Do NOT create any `[project-name]/` project output folder during this build
- Do NOT include cross-prompt or cross-phase references inside phase prompts (each is fully self-contained)
</constraints>

<success_criteria>
The build is complete and correct when ALL of the following are true:

1. `claude-build-system/README.md` exists and contains exactly 14 numbered steps with binary decision points at steps 11 and 13
2. All 4 phase files exist in `claude-build-system/phases/` and are fully self-contained — each can be pasted into a fresh chat with zero prior context and executed correctly
3. Every file from `bd-extraction/` has a corresponding file in `claude-build-system/methodology/` with content identical to the source
4. Every file from `bd-extraction/03-templates/` has a corresponding file in `claude-build-system/templates/` with content identical to the source
5. `phases/02-engineer.md`, `phases/03-orchestrate.md`, and `phases/04-ground.md` each contain the `[PROJECT_FOLDER_PATH]` placeholder
6. `phases/01-discover.md` does NOT contain a `[PROJECT_FOLDER_PATH]` placeholder
7. No file in `bd-extraction/` was modified, moved, renamed, or deleted during execution
8. No `[project-name]/` project folder was created
9. Every phase prompt uses `AskUserQuestion` for all user-facing questions — no prose questions
10. Phase prompts contain no machine-specific absolute paths — they are portable to any environment
</success_criteria>

<output_format>
After all files are written and Step 8 of the thinking process is verified complete, display exactly this block and nothing else. Do not narrate your process. Do not summarize what you did. Do not add commentary.

```
claude-build-system/ created at C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\

System files:
  README.md
  phases/01-discover.md
  phases/02-engineer.md
  phases/03-orchestrate.md
  phases/04-ground.md
  methodology/ — [N] files (preserving bd-extraction/ subfolder structure)
  templates/ — [N] files

Integrity check:
  bd-extraction/ — unmodified ✓
  No project output created ✓
  All phase prompts self-contained ✓
  [PROJECT_FOLDER_PATH] placeholders in phases 02/03/04 ✓

To build your first project: paste the contents of phases/01-discover.md into a fresh chat.
```
</output_format>

---

## Refinement Report

### Original Prompt

> Read ALL files listed below before writing anything. They are your source of truth.
>
> SOURCE FILES TO READ FIRST:
> [18 file paths listed]
>
> OUTCOME: After execution, a fully operational folder `claude-build-system/` exists at:
> `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\`
>
> [Full original prompt — see command args for complete text]

### Diagnostic Results

| # | Item | Original Status | How Addressed |
|---|------|----------------|---------------|
| 1 | XML/Section Structure | Partial | Added full XML sectioning: `<role>`, `<context>`, `<reading_directives>`, `<scope>`, `<thinking_process>`, `<requirements>`, `<constraints>`, `<success_criteria>`, `<output_format>` |
| 2 | Data-First Ordering | Partial | Restructured: context → reading directives → scope → thinking process → requirements → constraints → success criteria → output spec |
| 3 | Hierarchical Nesting | Partial | Phase requirements nested under `<requirements>`; constraints split into MUST / MUST NOT; behavior steps numbered with sub-bullets |
| 4 | Progressive Disclosure | Pass | Maintained and strengthened with context section establishing architecture rules first |
| 5 | Role Assignment | Fail | Added `<role>` defining systems architect and prompt engineering specialist with bounded expertise |
| 6 | Expertise Scoping | Fail | Role scoped to Claude Code tooling, multi-phase workflow design, file-system state management |
| 7 | Audience Awareness | Fail | Each phase prompt now includes an identity/purpose section defining the agent's role and what it does NOT do in that chat |
| 8 | Chain-of-Thought Phasing | Partial | Added explicit 8-step `<thinking_process>` with verification gates between steps |
| 9 | Self-Verification Directives | Fail | Added Step 7 (verify complete structure) and Step 8 (integrity verification) with explicit checklist |
| 10 | Thinking Process Definition | Fail | Added `<thinking_process>` with sequential steps, verification conditions, and halt-on-failure logic |
| 11 | Ambiguity Elimination | Partial | "Exact copies" → "byte-for-byte identical"; vague "do not modify" → explicit prohibition list; "outputs" → specific display format |
| 12 | Active Directives | Partial | All passive/descriptive language converted to imperative commands throughout |
| 13 | Specificity Gradients | Fail | Added MUST / MUST NOT structure in both `<scope>` and `<constraints>` sections |
| 14 | Constraint Boundaries | Pass | Strengthened IN/NOT IN SCOPE into MUST DO / MUST NOT DO format |
| 15 | Negative Constraints | Partial | Added 6 explicit MUST NOT directives covering all identified failure modes |
| 16 | Spelling/Grammar | Pass | Maintained; domain terminology standardized throughout |
| 17 | Domain Context Sufficiency | Partial | Added `<context>` section with 4 architectural rules explaining why the system works this way |
| 18 | Few-Shot Examples | Partial | Added example decision question in phase 03 spec; project naming examples maintained; phase prompt identity/purpose patterns added |
| 19 | Reference Anchoring | Pass | All methodology file references maintained with explicit "read in full" instruction |
| 20 | Output Format Specification | Pass | Strengthened with explicit "display nothing else" instruction and integrity check block |
| 21 | Success Criteria | Partial | Added 10 measurable, testable success criteria as explicit assertions |
| 22 | Tone/Voice Calibration | Fail | Output format section instructs: no narration, no summary, no commentary — display output block only |
| 23 | Permission to Expand | Fail | N/A for this prompt type — agent MUST NOT expand beyond spec; addressed via MUST NOT constraints |
| 24 | Uncertainty Allowance | Fail | Added explicit halt-and-report instruction in reading_directives for unreadable files |
| 25 | Task Decomposition | Partial | Added 8-step `<thinking_process>` decomposing the build into discrete verifiable phases |

**Original score: ~10/25 items fully addressed**
**Refined score: 25/25 items addressed**

### Techniques Applied

| # | Technique | How Applied | Category |
|---|-----------|-------------|----------|
| 1 | A1 — XML Tag Sectioning | 9 XML sections added: role, context, reading_directives, scope, thinking_process, requirements, constraints, success_criteria, output_format | Structural |
| 2 | A2 — Data-First / Query-Last | Reordered: context + reading directives (data) → requirements (instructions) → success criteria + output format (deliverable) | Structural |
| 3 | A3 — Hierarchical Nesting | Phase specs nested under requirements; MUST/MUST NOT split in scope and constraints; behavior steps with sub-conditions | Structural |
| 4 | A4 — Progressive Disclosure | Maintained existing flow; strengthened with context section establishing rules before instructions | Structural |
| 5 | B1 — Role Assignment | `<role>` added: systems architect + prompt engineering specialist with three named expertise domains | Role & Identity |
| 6 | B2 — Expertise Scoping | Role bounded to Claude Code tooling, multi-phase workflow design, file-system state management | Role & Identity |
| 7 | B3 — Audience Awareness | Each phase prompt includes identity/purpose defining agent role and what it does NOT do in that phase | Role & Identity |
| 8 | C1 — Chain-of-Thought Phasing | 8-step thinking_process with named steps: READ → INVENTORY → WRITE METHODOLOGY → WRITE TEMPLATES → WRITE PHASES → WRITE README → VERIFY STRUCTURE → VERIFY INTEGRITY | Reasoning |
| 9 | C2 — Self-Verification Directives | Steps 7 and 8 in thinking_process are pure verification steps; each write step includes post-write confirmation instruction | Reasoning |
| 10 | C3 — Thinking Process Definition | thinking_process defines exact execution sequence with verification gates and halt conditions | Reasoning |
| 11 | D1 — Ambiguity Elimination | "exact copies" → "byte-for-byte identical"; "do not modify" → explicit 6-item prohibition list; "output format" → display block with fill-in slots | Clarity |
| 12 | D2 — Active Directives | All passive/descriptive language converted to imperative: "Read X in full", "Write Y", "Confirm Z", "Halt and report" | Clarity |
| 13 | D3 — Specificity Gradients | MUST DO / MUST NOT DO in scope; MUST / MUST NOT in constraints | Clarity |
| 14 | D4 — Constraint Boundaries | Explicit "this is a static scaffold, not a project output" established in context; MUST NOT create project folders | Clarity |
| 15 | D5 — Negative Constraints | 6 MUST NOT directives: no bd-extraction modification, no project folders, no paraphrasing, no writing before reading, no machine paths in phase prompts, no cross-phase references | Clarity |
| 16 | E1 — Domain Research Integration | Fresh chat isolation pattern formalized; halt-on-unreadable-file from orchestration failure mode research; portable path warning from multi-environment deployment pattern | Context |
| 17 | F1 — Output Format Specification | Exact display block specified with fill-in slots; "display exactly this block and nothing else" instruction added | Output Control |
| 18 | F2 — Success Criteria | 10 measurable success criteria written as testable assertions | Output Control |
| 19 | F3 — Tone/Voice Calibration | output_format section: no narration, no summary, no commentary — display output block only | Output Control |
| 20 | G2 — Uncertainty Allowance | "If any file cannot be read, halt immediately and report the error — do not proceed with incomplete source material" | Meta |
| 21 | G3 — Task Decomposition | 8 named steps in thinking_process; each phase prompt's behavior decomposed into numbered steps with decision branches | Meta |

**Total: 21 techniques applied**

### Domain Research Conducted

**Domain identified:** AI-assisted software development scaffolding — specifically multi-phase Claude Code workflow systems with fresh-chat isolation and file-system state management.

**Key findings integrated:**

1. **Fresh-chat isolation pattern:** Each phase prompt must function as a completely independent document with zero reliance on conversation memory. This strengthened the self-containment requirements and added explicit "no cross-phase references" constraint. Each phase prompt now includes an identity/purpose section that establishes context from scratch.

2. **Halt-on-incomplete-read pattern:** In orchestration systems where subsequent writes depend on source file content, partial reads produce silently incorrect output (wrong content copied, structure mismatched). Added explicit halt-and-report instruction for unreadable files rather than allowing the agent to proceed.

3. **Portable path anti-pattern:** Phase prompts that embed machine-specific absolute paths fail when the `claude-build-system/` folder is copied to a different machine or location. Added explicit MUST NOT constraint prohibiting machine-specific paths inside phase prompts.

4. **AskUserQuestion enforcement:** In Claude Code, prose questions are frequently processed as rhetorical or skipped. The `AskUserQuestion` tool creates a mandatory UI interaction gate. Strengthened from "include explicit instructions" to "EVERY question MUST use the AskUserQuestion tool — questions in prose are not acceptable."

5. **Verification gate pattern:** Orchestration systems without intermediate verification steps fail silently — a wrong copy propagates through all downstream phases. Added post-write confirmation instruction for every methodology and template file, and two dedicated verification steps (Steps 7 and 8) at the end of the thinking process.
