```markdown
You are in brain-dump extraction and operationalization mode. Do not orient — execute immediately.

---

## OPERATING CONTRACT

**Output root:** `[OUTPUT_FOLDER]/bd-extraction/`
**Date format:** YYYY-MM-DD
**Folder prefix:** two-digit zero-padded integer (00, 01, 02...)
**Authority:** Full autonomous decision authority over structure, naming, and split logic. Zero authority to skip steps, omit the README, or write any file before reading every source it references.

---

## LAYER EXTRACTION PROTOCOL

Apply to every artifact produced. Do not skip layers. Do not merge layers.

| Layer | Extract |
|---|---|
| **meta-meta** | System's self-referential logic — governing rules, self-knowledge, recursive constraints |
| **meta** | Purpose architecture — component roles, inter-component dependencies, system contracts |
| **macro** | Outcome categories — cross-file workflows, major user-facing deliverables |
| **micro** | Discrete operations — what each file owns, exact operations performed |
| **micro-micro** | All parameters, variables, naming conventions, decision conditions, edge cases |

At every layer: extract **explicit content** (stated directly) AND **implicit content** (required but unstated — inferred from structure, relationships, and constraints).

---

## EXECUTION SEQUENCE

Complete each step fully before beginning the next.

---

### STEP 00 — Inventory Pass
Read every file, folder, tool, command, and external reference mentioned in the brain dump before writing anything.

For each item record:
- Full path or identifier
- Role classification (meta-meta / meta / macro / micro / micro-micro)
- Explicit content summary
- Implicit dependencies and contracts
- All parameters it controls
- All relationships to other items

**Output:** `bd-extraction/00-inventory/system-map.md`

Gate: do not proceed until this file exists.

---

### STEP 01 — Outcome Decomposition
Identify every distinct outcome the brain dump implies — stated or unstated.

For each outcome:
- Name it precisely
- Classify it (deliverable / system / process / command / template)
- Identify all five layers within it
- Map its dependencies on other outcomes
- Flag whether it requires a fresh chat (context-heavy) or can chain

**Output:** `bd-extraction/01-outcomes/`
- `outcome-registry.md` — every outcome, classified, layered, dependency-mapped
- `fresh-chat-vs-chain-map.md` — binary classification for every outcome with reasoning

---

### STEP 02 — Reverse-Engineering Pass
For each outcome in the registry, reverse-engineer the steps required to produce it.

Selection logic — before writing, determine:
1. What is the minimum context needed to execute this outcome?
2. What is the correct sequencing of steps?
3. What is the optimal split point if context limits apply?
4. What decision tree governs approach selection for this outcome?

**Output:** `bd-extraction/02-reverse-engineered/`
- One file per major outcome cluster: `[outcome-name]-execution-plan.md`
- Each file contains: steps in order, decision trees, split points, exact handoff prompts for fresh chats

---

### STEP 03 — Template and System Generation
For every repeatable pattern identified, produce a reusable artifact.

**Output:** `bd-extraction/03-templates/`
- One file per template/system/command/workflow
- Every file is fully parameterized — no hardcoded values that belong to a specific instance
- Every prompt artifact must satisfy the Prompt Engineering Gates below

---

### STEP 04 — Meta-System Architecture
Extract the governing logic that makes every other step coherent and scalable.

**Output:** `bd-extraction/04-meta-system/`
- `approach-selection-decision-tree.md` — how to autonomously select the best approach for any sub-task; all input variables; all branches; all output paths
- `parameter-extraction-algorithm.md` — universal algorithm for extracting every parameter at every level from any artifact type
- `system-integrity-rules.md` — constraints that survive all future user instructions; enforcement logic; compliance-while-responsive pattern
- `orchestration-spec.md` — how all components connect; sequencing rules; handoff contracts; audit trail conventions

---

### STEP 05 — Paint-by-Numbers README

**Non-negotiable rules:**
- Zero interpretation required by the user
- Numbered steps only — no prose paragraphs
- Each step: what to open + what to do + what to expect
- Every reference is an exact relative path from `bd-extraction/`
- Decision points are binary: "If X → go to step N. If Y → go to step M."
- Maximum 2 sentences per step

**Output:** `bd-extraction/README.md`

---

## PROMPT ENGINEERING GATES

Every prompt generated for use in a fresh chat must pass all of the following before being written to a file:

1. **Self-contained** — zero dependency on prior chat context; all necessary context embedded
2. **Front-loaded** — operating contract stated in first 3 lines
3. **Context-declared** — explicitly lists every file to read before acting
4. **Token-efficient** — no meta-commentary; no re-explanation of what the prompt does
5. **Output-specified** — exact file paths and formats for every output artifact
6. **Split-aware** — if the task exceeds one context window, the prompt includes its own split instructions
7. **Validation-gated** — any prompt touching a domain with a defined validator (e.g. a command, framework, or checklist) includes that validator as a mandatory non-skippable step

---

## FOLDER NAMING CONVENTION

```
bd-extraction/
  00-inventory/
  01-outcomes/
  02-reverse-engineered/
  03-templates/
  04-meta-system/
  README.md
```

Numbered subfolders within steps follow the same two-digit prefix convention.
Files that are versioned or iterable include date suffix: `filename-YYYY-MM-DD.md`

---

## START

Begin with Step 00. The brain dump below is your raw material.
```
