Read ALL files listed below before writing anything. They are your source of truth.

SOURCE FILES TO READ FIRST:
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\README.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\00-inventory\system-map.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\01-outcomes\outcome-registry.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\01-outcomes\fresh-chat-vs-chain-map.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\02-reverse-engineered\prompt-engineering-pipeline-execution-plan.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\02-reverse-engineered\orchestration-decomposition-execution-plan.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\02-reverse-engineered\context-state-system-execution-plan.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\sub-prompt-schema-template.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\state-schema-template.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\context-file-template.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\readme-index-template.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\03-templates\prompt-engineering-checklist.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\approach-selection-decision-tree.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\system-integrity-rules.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\orchestration-spec.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\04-meta-system\parameter-extraction-algorithm.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\bd-extraction\Universal feedback system\universal-feedbackloop-goal-system.md
- C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-code-methodology.md

---

OUTCOME: After execution, a fully operational folder `claude-build-system/` exists at:
`C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\`

This folder is a portable, self-contained project scaffold generator. It can be copied to any location and used to build any project. It is never modified after deployment. All project-specific output is always written to a NEW sibling folder `[project-name]/` that is created at runtime — never inside `claude-build-system/` itself.

---

SCOPE:
- IN SCOPE: Create claude-build-system/ and all files within it as specified below
- IN SCOPE: Copy all methodology reference files from bd-extraction/ into claude-build-system/methodology/
- IN SCOPE: Copy all template files from bd-extraction/03-templates/ into claude-build-system/templates/
- NOT IN SCOPE: Modify, move, or delete any file in bd-extraction/
- NOT IN SCOPE: Create any project-specific output (that is the system's job at runtime)

---

FOLDER STRUCTURE TO CREATE:

claude-build-system/
  README.md
  phases/
    01-discover.md
    02-engineer.md
    03-orchestrate.md
    04-ground.md
  methodology/
    [exact copies of all files from bd-extraction/, preserving subfolder structure]
  templates/
    [exact copies of all files from bd-extraction/03-templates/]

---

FILE SPECIFICATIONS:

## README.md

Paint-by-numbers usage guide. Numbered steps only — no prose paragraphs. Each step states: what to open + what to do + what to expect. Decision points are binary (If X → go to step N. If Y → go to step M).

Must cover exactly:
1. To start a new project: open a fresh Claude Code chat. Paste the full contents of phases/01-discover.md into the chat. Send it.
2. Answer every question Claude asks. When it stops asking and writes files, Phase 1 is complete. Note the [project-name] folder it created.
3. Open a fresh chat. Open phases/02-engineer.md. At the top, replace [PROJECT_FOLDER_PATH] with the full path to your [project-name] folder. Paste the full contents. Send it.
4. Answer any questions Claude asks. When it writes refined-prompt.md to your project folder, Phase 2 is complete.
5. Open a fresh chat. Open phases/03-orchestrate.md. Replace [PROJECT_FOLDER_PATH]. Paste full contents. Send it.
6. Answer any questions. When it writes state.json and prompt files to [project-name]/orchestration/, Phase 3 is complete.
7. Open a fresh chat. Open phases/04-ground.md. Replace [PROJECT_FOLDER_PATH]. Paste full contents. Send it.
8. Answer any questions about exact values. When it writes files to [project-name]/context/, Phase 4 is complete.
9. Open [project-name]/orchestration/README.md. Find prompt-01.md in the table.
10. Open a fresh chat. Paste the full contents of prompt-01.md. Send it. Wait for completion.
11. Repeat step 10 for each prompt in order (prompt-02.md, prompt-03.md, ...) until all are done.
12. To check progress: open [project-name]/orchestration/state.json. If pendingSteps is empty → build complete.
13. If any step fails: open bd-extraction/04-meta-system/system-integrity-rules.md and find the matching failure mode.

---

## phases/01-discover.md

This is the ideation extraction prompt. The user pastes its contents into a fresh chat.

BEHAVIOR THIS PROMPT MUST PRODUCE IN THE EXECUTING CHAT:

Purpose: Extract the user's vision with enough specificity to produce a locked implementation spec (nnnn.md). Do not proceed to output until confidence in the user's implicit AND explicit intent is ≥95%.

RULES (enforce all):
- Never suggest a technology, genre, feature, style, or approach unless the user explicitly says "I don't know, what do you suggest?"
- Every question uses the AskUserQuestion tool — never ask in prose
- Options in AskUserQuestion must never exclude valid creative directions. Always include sufficient options + "Other" for open input
- Never ask a question whose answer would push the user toward a specific technical solution. Ask about WHAT and WHY before asking about HOW
- If the user's answer reveals they want something specific but hasn't named it, ask a follow-up to confirm — do not assume
- If any answer is ambiguous, ask a targeted clarifying question before continuing
- 95% confidence means: you can describe the user's vision back to them with enough specificity that a developer could implement it without asking any clarifying questions. Exact counts, names, behaviors, constraints all known.

QUESTION SEQUENCE (branch based on answers, do not skip layers):

Layer 1 — What (understand the object being built):
- What do you want to build? [open text via Other option]
- What type of thing is this? [options: App / Tool or Utility / Content or Document / Data System / API or Service / Automation / Something else entirely]
- Describe what it does in your own words [open text]

Layer 2 — Why and Who (understand purpose and audience):
- Who is this for? [options: Myself / A specific person / A team / A public audience / Other]
- What problem does it solve or what need does it meet?
- Why does this need to exist?

Layer 3 — Success (understand the completion target):
- What does it look like when this is finished and working perfectly?
- What would make you say "yes, this is exactly what I wanted"?
- What would make you say "this missed the mark"?

Layer 4 — Constraints (understand the boundaries):
- Are there any technologies, platforms, or environments it must work with or within?
- Are there things it must NOT do or include?
- Are there existing files, codebases, or systems it must work with?

Layer 5 — Exact Values (lock the spec):
- Are there any specific values you already know? (names, colors, counts, formats, file structures, terminology)
- Is there anything I haven't asked about that is important for me to know before I document this?

CONFIDENCE CHECK (after Layer 5):
Evaluate: can you write a complete nnnn.md with no open design decisions, no hedging language, and exact values throughout?
- YES (≥95% confidence) → produce outputs and stop asking
- NO → identify the specific gap → ask one targeted question to fill it → re-evaluate

OUTPUTS (write these files, then stop):
1. [project-name]/vision.md — the full extracted vision:
   - Goal (the real goal, not the proxy)
   - Success criteria: external proof + internal proof
   - Audience and purpose
   - Constraints (must/must not)
   - Exact values locked
   - Goal type classification (state / process / system / avoidance / hybrid)
   - Leverage points: what two things, if wrong, would invalidate the entire build
   
2. [project-name]/nnnn.md — the locked implementation spec:
   - All design decisions made — no open questions
   - Exact values throughout (no approximations)
   - Complete enough that a developer can build without asking clarifying questions
   - Written in the same style as the nnnn.md described in claude-code-methodology.md Section 2 Stage 1
   - Include: architecture choices, data structures, exact naming, counts, formats, constraints, design values

Project-name rule: derive from the vision. Kebab-case. Descriptive. 2–4 words. Example: "habit-tracker-pwa", "sales-data-pipeline", "onboarding-email-system"

Chat response after writing files:
  Vision extraction complete.
  Project: [project-name]
  Files written:
    [project-name]/vision.md
    [project-name]/nnnn.md
  Next step: Open phases/02-engineer.md. Replace [PROJECT_FOLDER_PATH] with [full path to project-name folder]. Paste into a fresh chat.

---

## phases/02-engineer.md

This prompt reads the project folder and engineers the implementation prompt through the full methodology pipeline.

Contains a [PROJECT_FOLDER_PATH] placeholder that the user replaces before pasting.

BEHAVIOR:

1. Read [PROJECT_FOLDER_PATH]/vision.md and [PROJECT_FOLDER_PATH]/nnnn.md in full
2. Read methodology/02-reverse-engineered/prompt-engineering-pipeline-execution-plan.md
3. Read methodology/03-templates/prompt-engineering-checklist.md
4. Use AskUserQuestion if any critical information needed to engineer the prompt is missing from vision.md or nnnn.md — ask exactly one targeted question per gap, no fishing expeditions
5. Apply the 8 optimization rules from the prompt engineering pipeline to produce an optimized prompt
6. Apply the full /refinep 6-phase process internally:
   - Phase 2: Diagnose against 25 items — score each, flag all Partial/Not at all
   - Phase 3: Research the domain — 2–3 web searches (best practices + stack/tools + anti-patterns for this specific project type). Do not skip this phase.
   - Phase 4: Apply applicable techniques from all 7 categories (A→G) in order
   - Phase 5: Verify against all 15 checklist items — if any fail, revise and re-verify before proceeding
7. Validate: will this prompt, if executed, produce the thing described in vision.md? If NO → identify the gap → fill it before writing
8. Write output to [PROJECT_FOLDER_PATH]/refined-prompt.md in the standard structure:
   ## The Prompt [full refined prompt — copy-paste ready]
   ## Refinement Report
   ### Original Source [nnnn.md quoted]
   ### Diagnostic Results [25-item table]
   ### Techniques Applied [table]
   ### Domain Research Conducted [summary]

Chat response after writing:
  Prompt engineering complete.
  Files written: [PROJECT_FOLDER_PATH]/refined-prompt.md
  Domain researched: [summary]
  Diagnostic improvements: [N]/25
  Techniques applied: [N]
  Next step: Open phases/03-orchestrate.md. Replace [PROJECT_FOLDER_PATH]. Paste into a fresh chat.

---

## phases/03-orchestrate.md

This prompt reads the project folder and produces the complete orchestration package.

Contains a [PROJECT_FOLDER_PATH] placeholder.

BEHAVIOR:

1. Read [PROJECT_FOLDER_PATH]/vision.md, nnnn.md, and refined-prompt.md in full
2. Read methodology/02-reverse-engineered/orchestration-decomposition-execution-plan.md
3. Read methodology/03-templates/sub-prompt-schema-template.md
4. Read methodology/03-templates/state-schema-template.md
5. Read methodology/03-templates/readme-index-template.md
6. Read methodology/04-meta-system/approach-selection-decision-tree.md
7. Determine scale: SMALL (1–5 steps) / MEDIUM (10–30) / LARGE (30–45+)
8. MANDATORY PRE-WRITE: Catalog every discrete verifiable unit of work before creating any files. Apply the atomicity test to each unit: "Can this be completed and verified independently?" If NO → subdivide.
9. Spawn sub-agents to research: domain-specific build order, standard file structures for this project type, common implementation patterns — use findings to inform decomposition
10. Use AskUserQuestion if any decision about decomposition requires knowing something about the user's preferences that isn't in the spec (e.g., "The spec mentions authentication — should this use sessions or tokens?")
11. DO NOT make technical decisions that belong to the user. Surface them as questions.
12. Order units into dependency sequence — validate no forward references
13. Write [PROJECT_FOLDER_PATH]/orchestration/state.json — all step IDs in pendingSteps, fully populated
14. Write [PROJECT_FOLDER_PATH]/orchestration/README.md — execution index table with all required columns
15. Write all [PROJECT_FOLDER_PATH]/orchestration/prompt-NN.md files — following sub-prompt-schema-template.md exactly. Five hard constraints verbatim in every file. One atomic task per file.
16. Run Checklist D (from prompt-engineering-checklist.md) on the full package before declaring complete

Chat response after writing:
  Orchestration complete.
  Project: [project-name]
  Scale: [SMALL/MEDIUM/LARGE]
  Files written:
    [PROJECT_FOLDER_PATH]/orchestration/state.json — [N] steps
    [PROJECT_FOLDER_PATH]/orchestration/README.md
    [PROJECT_FOLDER_PATH]/orchestration/prompt-01.md through prompt-[NN].md
  Step breakdown: [category breakdown of what each group of prompts does]
  Next step: Open phases/04-ground.md. Replace [PROJECT_FOLDER_PATH]. Paste into a fresh chat.

---

## phases/04-ground.md

This prompt reads the full orchestration package and writes all required context files.

Contains a [PROJECT_FOLDER_PATH] placeholder.

BEHAVIOR:

1. Read [PROJECT_FOLDER_PATH]/vision.md, nnnn.md, and all orchestration/prompt-NN.md files
2. Read methodology/03-templates/context-file-template.md
3. Read methodology/02-reverse-engineered/context-state-system-execution-plan.md
4. Identify every piece of domain knowledge that sub-agents will need and cannot reliably generate correctly (exact values, canonical IDs, ordering requirements, design tokens, data enumerations)
5. For any exact values not present in nnnn.md, use AskUserQuestion to collect them — be specific about why each value matters and what goes wrong if it's guessed
6. Write context files to [PROJECT_FOLDER_PATH]/context/ using the naming convention and structure from context-file-template.md
7. Write in dependency order: data + design tokens first → architecture + UI second → build + technical third
8. Update every prompt-NN.md Prerequisites section to explicitly name each context file that prompt needs
9. Verify: every prompt that uses domain-specific knowledge references at least one context file

Chat response after writing:
  Context files complete.
  Files written:
    [PROJECT_FOLDER_PATH]/context/ — [N] files
    [list each context file and what failure mode it prevents]
  Prompt prerequisites updated: [N] prompts now reference context files
  SYSTEM READY.
  Next step: Open [PROJECT_FOLDER_PATH]/orchestration/README.md. Start with prompt-01.md. Open a fresh chat. Paste its full contents. Send it.

---

CONSTRAINTS:
- methodology/ files must be exact copies — no paraphrasing, no summarizing, no modification
- templates/ files must be exact copies — no modification
- Phase prompts must be self-contained — no references to prior conversation context, everything needed embedded
- The system must be domain-agnostic — identical process whether the project is a web app, CLI tool, data pipeline, or document system
- Phase prompts must include explicit instructions to use AskUserQuestion (not prose questions)
- No phase prompt may steer the user toward any specific technology or approach unless (a) the user already specified it in their vision, or (b) the user explicitly asks for a recommendation
- The [PROJECT_FOLDER_PATH] placeholder must appear in phases/02-engineer.md, 03-orchestrate.md, and 04-ground.md — user replaces before pasting

OUTPUT FORMAT:
After all files are written, display:
  claude-build-system/ created at [full path]

  System files:
    README.md
    phases/01-discover.md
    phases/02-engineer.md
    phases/03-orchestrate.md
    phases/04-ground.md
    methodology/ — [N] files
    templates/ — [N] files

  To build your first project: paste the contents of phases/01-discover.md into a fresh chat.
