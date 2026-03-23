# BUILD-command-01-research.md
## Self-Contained Meta-Prompt for a Fresh Claude Code Session

**Purpose:** Build `universal-research-system/commands/command-01-research.md` — the production execution engine for the Universal Research System.

**Process:** Two-pass. This file feeds both passes.
- **Layer 1** — You generate a Build Prompt from the specs in this file.
- **Layer 2** — You execute that Build Prompt to write the complete command.

**Assumed prior knowledge:** None. This file is fully self-contained.

---

## MANDATORY FIRST ACTIONS

Execute these reads before generating any output. Do not skip. Do not reorder.

**READ 1:** `universal-research-system/Research system brain/north-star.md`
- If absent: HALT. Output the exact missing path. Do not proceed.
- If present: Read in full. Apply all rules defined there.

**READ 2:** `universal-research-system/research-patterns-system-context.md`
- If absent: Proceed using this file as the sole spec source.
- If present: Read in full. It is the authoritative build contract. It supersedes any ambiguity in this file.

Both reads precede any generation. The North Star governs naming conventions and behavioral rules. The context document governs all specification details.

---

## PART 1 — SYSTEM ARCHITECTURE

### 1.1 What the System Is

The Universal Research System is a multi-session, state-managed research tool built on Claude Code. It takes any topic as input and progressively builds a structured knowledge artifact across multiple independent sessions.

Key architectural fact: **Claude Code has zero memory between sessions.** Every session starts cold. All continuity is maintained exclusively through files on disk. The command reads its full operating context from files at the start of every run — never from memory, never from conversation history.

The system has exactly one command: `command-01-research.md`. This file contains all logic for all six research phases. It is the only file the user ever runs.

User invocation:
```
/command-01-research [topic or question]
```

### 1.2 Directory Structure

```
universal-research-system/
│
├── Research system brain/               ← READ-ONLY. Never write here. Ever.
│   └── north-star.md                    ← Governing methodology. Rule NSA-2: read before every session.
│
├── commands/                            ← The command lives here.
│   └── command-01-research.md           ← THE FILE BEING BUILT. All phase logic lives here.
│
├── research-patterns-system-context.md  ← Full executable spec. Authoritative source.
├── HOW-THIS-SYSTEM-WORKS.md             ← System overview documentation.
├── BUILD-command-01-research.md         ← This file.
│
├── state.json                           ← Created by command on first run. External memory.
├── knowledge-map.md                     ← Created by command on first run. Growing research artifact.
├── next-session.md                      ← Written by command at end of every session.
│
└── session-outputs/                     ← Created by command on first run. Per-session artifacts.
    └── [YYYY-MM-DD]-[phase]-[n].md      ← Naming pattern for session output files.
```

**File creation responsibility:**

| File | Created by | When |
|---|---|---|
| `state.json` | command-01-research.md | Session 1, phase 1, if absent |
| `knowledge-map.md` | command-01-research.md | Session 1, if absent — initialized empty |
| `next-session.md` | command-01-research.md | End of every session, every phase |
| `session-outputs/` | command-01-research.md | First run, if folder absent |
| `session-outputs/[file].md` | command-01-research.md | Each session produces one dated file |

**The `Research system brain/` folder is never written to programmatically. It is a read-only instruction layer. Any modification to it is made by the user only.**

### 1.3 The Six Phases

The command executes one phase per session. The active phase is determined by reading `state.phase` from state.json at session start. The command does not infer the phase from any other source.

| # | Phase | `state.phase` value | Exit trigger | Next phase |
|---|---|---|---|---|
| 1 | Problem Framing | `problem_framing` | `user_lens_profile` populated in state.json | `variable_discovery` |
| 2 | Variable Discovery | `variable_discovery` | `pending_variables[]` contains ≥1 item | `variable_research` |
| 3 | Variable Research | `variable_research` | `pending_variables[]` is empty | `connection_validation` |
| 4 | Connection Validation | `connection_validation` | `connections.pending[]` is empty | `synthesis` or back to `variable_research` |
| 5 | Synthesis | `synthesis` | `knowledge-map.md` written + conclusion doc written | `qa_mode` |
| 6 | Q&A Mode | `qa_mode` | User terminates or sends new research topic | `problem_framing` |

**Phase transitions are automatic.** The command detects the exit condition, updates `state.phase` in state.json, and writes `next-session.md`. The user does not manage phase transitions.

---

## PART 2 — COMPLETE VARIABLE AND PARAMETER MAP

### 2.1 state.json Full Schema

```json
{
  "research_question": "string — the topic/question supplied by user in session 1",
  "phase": "problem_framing | variable_discovery | variable_research | connection_validation | synthesis | qa_mode",
  "cycle_count": 0,
  "last_updated": "ISO-8601 timestamp",
  "user_lens_profile": {
    "approved_perspectives": ["array of strings — worldviews/frameworks to apply"],
    "excluded_methodologies": ["array of strings — approaches to exclude"],
    "open_to_cross_domain": true,
    "minimum_confidence_band": "relevant",
    "output_format": "research_document | knowledge_map | json_profile | multiple_documents",
    "research_scope": "broad_survey | deep_specific"
  },
  "researched_variables": ["array of variable name strings — completed research"],
  "pending_variables": ["array of variable name strings — research not yet done"],
  "research_summaries": {
    "<variable_name>": {
      "confidence_band": "core | relevant | borderline | weak | exclude",
      "finding_count": 0,
      "summary": "string",
      "reasoning_chains": [
        {
          "claim": "string",
          "evidence": "string",
          "logic": "string",
          "confidence_band": "core | relevant | borderline | weak | exclude"
        }
      ]
    }
  },
  "connections": {
    "validated": [
      {
        "from": "variable_name",
        "to": "variable_name",
        "type": "causal | analogical | architectural | correlational",
        "explanation": "string",
        "evidence_count": 0
      }
    ],
    "pending": [
      {
        "from": "variable_name",
        "to": "variable_name",
        "evidence_count": 0
      }
    ],
    "discarded": [
      {
        "from": "variable_name",
        "to": "variable_name",
        "reason": "string"
      }
    ]
  },
  "session_log": [
    {
      "date": "ISO-8601",
      "phase_executed": "string",
      "variables_researched": ["array"],
      "connections_validated": ["array of from-to strings"],
      "output_file": "session-outputs/filename.md"
    }
  ]
}
```

### 2.2 Variable Relationships and Data Flow

```
USER INPUT
  └── research question (argument to /command-01-research)
        ↓
  PHASE 1: PROBLEM FRAMING
  └── clarifying questions → user_lens_profile populated
        → user_lens_profile.approved_perspectives[]
        → user_lens_profile.excluded_methodologies[]
        → user_lens_profile.open_to_cross_domain (bool)
        → user_lens_profile.output_format (string)
        → user_lens_profile.research_scope (string)
        → user_lens_profile.minimum_confidence_band (default: "relevant")
      state.research_question = [user input]
      state.phase → "variable_discovery"
        ↓
  PHASE 2: VARIABLE DISCOVERY
  └── research_question + user_lens_profile → variable identification
      → each variable assigned confidence_band (SPEC-4 rubric)
      → added to pending_variables[]
      state.phase → "variable_research"
        ↓
  PHASE 3: VARIABLE RESEARCH
  └── for each item in pending_variables[]:
      → research produces ≥3 findings
      → each finding → reasoning_chain (4 required fields)
      → finding_count increments per finding
      → confidence_band assigned per variable
      → when complete (confidence ≥ Relevant + finding_count ≥ 3):
          → item removed from pending_variables[]
          → item added to researched_variables[]
          → research_summaries[variable_name] populated
      state.phase → "connection_validation" (when pending_variables[] empty)
        ↓
  PHASE 4: CONNECTION VALIDATION (Synoptic Cognition)
  └── for every pair (A, B) in researched_variables[]:
      → classify: causal / analogical / architectural / correlational / none
      → if ≠ none: add to connections.pending[]
      → validate: ≥2 independent evidence lines + confidence ≥ Relevant (60+)
          → if validated: move to connections.validated[] + classify type + write explanation
          → if not: move to connections.discarded[] + write reason
      → if new variables discovered: add to pending_variables[], revert phase to variable_research
      state.phase → "synthesis" (when connections.pending[] empty, no new variables)
                 OR → "variable_research" (if new variables found)
        ↓
  PHASE 5: SYNTHESIS
  └── connections.validated[] evaluated → overall patterns identified
      → conclusion document → session-outputs/[YYYY-MM-DD]-synthesis-[n].md
      → knowledge-map.md written/updated (SPEC-3 format)
      → cycle_count incremented
      state.phase → "qa_mode"
        ↓
  PHASE 6: Q&A MODE
  └── knowledge-map.md read into context
      → user question → route to relevant variable nodes
      → answer synthesized from knowledge map only
      → no new research generated
      → if new research topic: state.phase → "problem_framing"
```

### 2.3 Confidence Band Rubric (SPEC-4)

| Band | Score Range | Inclusion Rule | When to Use |
|---|---|---|---|
| Core | 80–100 | Include always | Directly addresses the research question |
| Relevant | 60–79 | Include | Clearly connected to one or more Core variables |
| Borderline | 40–59 | Flag for user review before including | Possible connection — structural basis present but not confirmed |
| Weak | 20–39 | Exclude unless cross-session pattern confirmed | Tenuous — single or indirect link only |
| Exclude | 0–19 | Exclude | No structural connection to research question |

**Minimum threshold for variable completion:** Relevant (60+) AND ≥3 distinct substantive findings
**Minimum threshold for connection validation:** Relevant (60+) AND ≥2 independent lines of evidence

### 2.4 Reasoning Chain Format (SPEC-5)

Every research finding stored in `research_summaries[].reasoning_chains[]` must contain all four fields. Findings missing any field are excluded from knowledge-map.md and logged as unvalidated.

```
Claim: [the specific finding or connection being asserted]
Evidence: [what supports this claim — described in specific terms]
Logic: [the inferential path from evidence to claim]
Confidence band: [Core / Relevant / Borderline / Weak / Exclude]
```

### 2.5 Connection Types

| Type | Definition |
|---|---|
| `causal` | Variable A directly causes or produces Variable B |
| `analogical` | Variables A and B share structural pattern — one domain mirrors the other |
| `architectural` | Variables A and B are components of the same structural system |
| `correlational` | Variables A and B co-occur without an established causal direction |

### 2.6 Convergence Rule

The loop enters Synthesis when **both** conditions are true simultaneously:
1. `pending_variables[]` is empty
2. `connections.pending[]` is empty

No artificial cycle cap. The system completes when the work is complete.

---

## PART 3 — PHASE-BY-PHASE LOGIC SPECIFICATION

### Phase 1: Problem Framing

**Entry condition:** `state.json` absent OR `state.phase = "problem_framing"`

**Session 1 initialization (state.json absent):**
- Create `state.json` with SPEC-1 schema, all arrays empty, `phase = "problem_framing"`, `cycle_count = 0`
- Set `state.research_question` from the user's command argument
- Create `knowledge-map.md` as empty file if absent
- Create `session-outputs/` folder if absent

**Work:**
Ask the user the following five multiple-choice clarifying questions. Present all five before accepting any answers. Wait for the user to answer all five in the same session.

```
Q1 — Output format
What format should the final research output take?
A) Research document — narrative prose with structured sections
B) Knowledge map only — variable nodes and connection explanations
C) JSON profile — machine-readable structured data
D) Multiple documents — all of the above

Q2 — Research lens
What worldview or framework should filter the research?
A) First-principles / systems thinking — structural relationships only
B) Empirical / evidence-based — published research and data
C) Practitioner / applied — what works in real-world application
D) No filter — broadest possible coverage

Q3 — Cross-domain openness
Should the system include findings from unrelated domains if they are structurally relevant?
A) Yes — include cross-domain findings if the structural connection is confirmed
B) No — stay within the research topic's domain only

Q4 — Research scope
How should the system approach depth vs. breadth?
A) Broad survey — identify as many variables as possible
B) Deep specific — fewer variables, exhaustive research on each

Q5 — Exclusions
Are there any methodologies, frameworks, or domains to explicitly exclude?
A) None — include everything above minimum confidence
B) [User specifies — free text answer]
```

**After user answers:**
- Populate `state.user_lens_profile` from answers
- Set `state.phase = "variable_discovery"`
- Write `state.json`
- Write `next-session.md` (SPEC-6 format)
- Write session output file: `session-outputs/[YYYY-MM-DD]-problem-framing-1.md`

**Exit trigger:** `user_lens_profile` populated → `phase = "variable_discovery"`

---

### Phase 2: Variable Discovery

**Entry condition:** `state.phase = "variable_discovery"`

**Work:**
1. Read `state.research_question` and `state.user_lens_profile`
2. Identify all variables relevant to the research question, filtered through user_lens_profile
3. For each variable:
   - Assign confidence_band (SPEC-4 rubric — Core/Relevant/Borderline only; Weak/Exclude variables omitted at this stage)
   - Add variable name to `pending_variables[]`
4. Write `state.json` with updated `pending_variables[]`
5. Set `state.phase = "variable_research"`
6. Write `state.json`
7. Write `next-session.md` (SPEC-6 format)
8. Write session output file: `session-outputs/[YYYY-MM-DD]-variable-discovery-[cycle_count+1].md` — list all discovered variables with their confidence bands

**Exit trigger:** `pending_variables[]` contains ≥1 item → `phase = "variable_research"`

---

### Phase 3: Variable Research

**Entry condition:** `state.phase = "variable_research"`

**Overflow check (run before processing each variable):**
If estimated remaining output for this session exceeds 20,000 tokens:
- Generate SPEC-7 meta-prompt for remaining `pending_variables[]`
- Write meta-prompt to `session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md`
- Write `state.json` (current state)
- Write `next-session.md`
- Stop processing. Do not continue inline.

**Work (per variable in `pending_variables[]`):**
1. Research the variable — produce ≥3 distinct substantive findings
2. For each finding, write a reasoning chain (SPEC-5 format — all 4 fields required)
3. Assign `confidence_band` to the variable overall
4. Populate `research_summaries[variable_name]`:
   - `confidence_band` — assessed band
   - `finding_count` — count of validated findings
   - `summary` — brief synthesis of all findings
   - `reasoning_chains[]` — array of all SPEC-5 reasoning chain objects
5. **Gate:** If `confidence_band < Relevant` (score < 60) OR `finding_count < 3`: do not mark complete. Flag in output. Continue researching or note as incomplete.
6. When complete (confidence ≥ Relevant AND finding_count ≥ 3):
   - Remove variable name from `pending_variables[]`
   - Add variable name to `researched_variables[]`
7. **Write `state.json` after completing each variable** — before generating next variable's research output (MC-8 constraint — state written before context fills)

**After all pending_variables[] processed:**
- Set `state.phase = "connection_validation"`
- Write `state.json`
- Write `next-session.md` (SPEC-6 format)
- Write session output file: `session-outputs/[YYYY-MM-DD]-variable-research-[n].md` — all variables researched this session with reasoning chains

**Exit trigger:** `pending_variables[]` is empty → `phase = "connection_validation"`

---

### Phase 4: Connection Validation

**Entry condition:** `state.phase = "connection_validation"`

**Overflow check (run before processing each pair):**
If estimated remaining output for this session exceeds 20,000 tokens:
- Generate SPEC-7 meta-prompt for remaining `connections.pending[]` items
- Write meta-prompt to `session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md`
- Write `state.json` (current state)
- Write `next-session.md`
- Stop processing.

**Work — Synoptic Cognition Protocol (SPEC-9):**

For every pair (Variable A, Variable B) in `researched_variables[]`:

1. **Classify** the relationship type:
   - `causal` — A directly causes or produces B
   - `analogical` — A and B share structural pattern
   - `architectural` — A and B are components of the same structural system
   - `correlational` — A and B co-occur without established causal direction
   - `none` — no structural connection found

2. **If type ≠ `none`:** write explanation + add pair to `connections.pending[]` with `evidence_count = 0`

3. **Validate:** Gather ≥2 independent lines of evidence for the connection. Both must score ≥ Relevant (60+) on the confidence rubric.
   - If validated: move pair from `connections.pending[]` to `connections.validated[]` with type + explanation + evidence_count
   - If not validated: move pair from `connections.pending[]` to `connections.discarded[]` with reason

4. **New variable detection:** If researching connections reveals a variable not yet in `researched_variables[]` or `pending_variables[]`:
   - Add new variable to `pending_variables[]`
   - After finishing current pair: write `state.json` with `phase = "variable_research"`, write `next-session.md`, stop current session. New variable research happens before connection validation continues.

5. **Write `state.json` after completing each pair** (MC-8)

**After all connections.pending[] processed and no new variables found:**
- Evaluate convergence: Is `pending_variables[]` empty AND `connections.pending[]` empty?
  - YES → set `state.phase = "synthesis"`
  - NO (pending_variables[] gained new items) → set `state.phase = "variable_research"`
- Write `state.json`
- Write `next-session.md` (SPEC-6 format)
- Write session output file: `session-outputs/[YYYY-MM-DD]-connection-validation-[n].md` — all connections evaluated this session

**Exit trigger:** `connections.pending[]` is empty → `phase = "synthesis"` or `phase = "variable_research"`

---

### Phase 5: Synthesis

**Entry condition:** `state.phase = "synthesis"`

**Work:**
1. Read `state.connections.validated[]` — all validated connections
2. Read `knowledge-map.md` in full before writing anything to it
3. Evaluate all validated connections for emergent patterns — connections that form chains, clusters, or hierarchies across multiple variable pairs
4. Write conclusion document to `session-outputs/[YYYY-MM-DD]-synthesis-[cycle_count].md`:
   - Research question
   - All validated variables with confidence bands
   - All validated connections with types and explanations
   - Emergent patterns and cross-domain insights identified
   - Summary conclusion
5. Write/update `knowledge-map.md` (SPEC-3 format — full structure below)
6. Increment `state.cycle_count`
7. Set `state.phase = "qa_mode"`
8. Write `state.json`
9. Write `next-session.md` (SPEC-6 format)

**Exit trigger:** `knowledge-map.md` written + conclusion doc written → `phase = "qa_mode"`

---

### Phase 6: Q&A Mode

**Entry condition:** `state.phase = "qa_mode"`

**Work:**
1. Read `knowledge-map.md` in full
2. Read `state.json` — all `research_summaries`, `connections.validated[]`
3. Receive user's question
4. Route question to relevant variable nodes:
   - Match question keywords to variable names and connection types
   - Identify which variables and connections directly address the question
5. Synthesize answer from knowledge map content only — no new research, no external inference
6. New topic detection: If user's message is a new research question (not a question about current research):
   - Set `state.research_question` = new topic
   - Set `state.phase = "problem_framing"`
   - Write `state.json`
   - Write `next-session.md` instructing user to clear chat and run command with new topic

**Exit trigger:** User terminates OR new research topic detected → `phase = "problem_framing"`

---

## PART 4 — OUTPUT FORMAT SPECIFICATIONS

### 4.1 knowledge-map.md Structure (SPEC-3)

```markdown
# Knowledge Map — [research_question]
**Last updated:** [ISO-8601 timestamp]  **Cycle:** [cycle_count]  **Variables mapped:** [count]

---

## Variable: [Variable Name]
**Confidence band:** Core / Relevant / Borderline
**Summary:** [research summary text from research_summaries[].summary]
**Reasoning chain:** [key evidence + logical path supporting this variable's inclusion]
**Finding count:** [finding_count]

### Connections from [Variable Name]

#### → [Connected Variable Name]
**Type:** causal / analogical / architectural / correlational
**Validated:** yes / pending
**Evidence count:** [evidence_count]
**Explanation:** [why/how these two variables connect — from connections.validated[].explanation]

#### → [Next Connected Variable Name]
[repeat structure]

---

## Variable: [Next Variable Name]
[repeat full structure]
```

### 4.2 next-session.md Structure (SPEC-6)

Written at the end of every session, every phase, before context fills.

```markdown
# Next Session — [YYYY-MM-DD]

## Status
Phase completed: [phase just executed]
Current phase: [next phase — what state.phase is now set to]
Variables researched this session: [n]
Variables remaining: [count of pending_variables[]]
Connections validated this session: [n]

## Command to Send
/command-01-research [original research question]

## What happens next
[One sentence describing what the next session will execute]
```

### 4.3 Meta-Prompt Structure — Overflow Split (SPEC-7)

Generated when estimated session output exceeds 20,000 tokens. All fields derived from state.json at generation time.

```markdown
# Meta-Prompt — Overflow Split [YYYY-MM-DD]

## Context (from state.json)
Research question: [state.research_question]
Current phase: [state.phase]
Cycle: [state.cycle_count]

## Pending work for this split
Variables to research: [subset of state.pending_variables[]]
Connections to validate: [subset of state.connections.pending[]]

## Execution instruction
Read state.json and knowledge-map.md. Execute ONLY the pending work listed above.
Write results to state.json and knowledge-map.md before context fills.
Write next-session.md on completion.

## Files to read at session start
- universal-research-system/state.json
- universal-research-system/knowledge-map.md
- universal-research-system/Research system brain/north-star.md (Rule NSA-2 — mandatory)
```

### 4.4 Session Output File Naming

```
session-outputs/[YYYY-MM-DD]-problem-framing-1.md
session-outputs/[YYYY-MM-DD]-variable-discovery-[cycle].md
session-outputs/[YYYY-MM-DD]-variable-research-[n].md
session-outputs/[YYYY-MM-DD]-connection-validation-[n].md
session-outputs/[YYYY-MM-DD]-synthesis-[cycle].md
session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md
```

---

## PART 5 — SYSTEM CONSTRAINTS

| Constraint ID | Rule | Enforcement Point |
|---|---|---|
| NSA-2 | North Star read before every session — never from memory | Top of command — cold-start READ 1 |
| MC-8 | state.json written BEFORE context fills — never after | After every completed variable or pair, in every research phase |
| MC-5 | No variable researched twice | Check `researched_variables[]` before starting research on any variable |
| MC-1 | No hallucination — every finding requires SPEC-5 reasoning chain | Gate in Phase 3 and Phase 4 — finding without all 4 fields is excluded |
| M-12 | Output token hard cap: 32,000 tokens per output | Overflow detection check before each processing batch |
| M-3 | Dynamic decomposition at 20,000 token estimated output | SPEC-7 meta-prompt generation in Phases 3 and 4 |
| Read-only | Never write to `Research system brain/` folder | No write operation targets that path, ever |
| MC-3 | Context window never grows with inline history | All history lives in state.json and knowledge-map.md — never accumulated inline |

---

## PART 6 — SESSION EXECUTION ORDER (SPEC-8)

Every session, every phase, in this exact order:

```
1. READ   → north-star.md (cold-start READ 1)
2. READ   → state.json (cold-start READ 2) — determine phase
3. READ   → knowledge-map.md (cold-start READ 3)
             ↓
4. DETECT → state.phase → dispatch to phase logic
             ↓
5. EXECUTE → phase work per PART 3 specification
             ↓
6. VALIDATE → all findings include SPEC-5 reasoning chains (4 fields)
             ↓
7. WRITE  → state.json updated (BEFORE generating session output)
8. UPDATE → knowledge-map.md (if phase touches it)
             ↓
9. PRODUCE → session output artifact → session-outputs/[dated file]
             ↓
10. WRITE → next-session.md (SPEC-6 format)
             ↓
11. EVALUATE → convergence: pending_variables[] empty AND connections.pending[] empty?
               YES → state.phase = "synthesis"
               NO  → loop continues; next session picks up from state
```

**The state.json write (step 7) always precedes the session output generation (step 9).** This is non-negotiable. If context fills between steps 7 and 9, the state is preserved. If context fills between steps 5 and 7, work may be lost. Design the phase logic to write state.json incrementally (after each variable, after each pair) — not only at session end.

---

## PART 7 — THE COLD-START READ SEQUENCE

The command file opens with this block. It is unconditional. It is not nested inside any conditional. It is not optional for any phase. It executes on every run, including session 1.

```
## COLD-START READ SEQUENCE
Execute all three reads below before any other logic. Do not skip. Do not reorder.

READ 1: universal-research-system/Research system brain/north-star.md
  → If absent: halt, output path, do not proceed
  → If present: read in full, apply all rules

READ 2: universal-research-system/state.json
  → If absent: initialize with SPEC-1 schema, set phase = problem_framing
  → If present: parse in full, treat all fields as ground truth

READ 3: universal-research-system/knowledge-map.md
  → If absent: initialize as empty file
  → If present: read in full before generating any output

--- Cold-start sequence complete. Proceed to phase detection. ---
```

After this block and only after this block, the command reads `state.phase` and dispatches to the appropriate phase logic.

**Why the order is architecturally critical:**
- North Star before state.json: The North Star defines the rules for interpreting state.json fields. Without it, confidence bands, phase exit triggers, and connection validation protocols have no defined meaning.
- state.json before knowledge-map.md: `state.phase` determines which sections of knowledge-map.md are relevant and whether the command is adding to existing summaries or creating new connection entries. Reading the map before knowing the phase means the command cannot correctly interpret what it reads.
- Both before any execution: The anti-redundancy guarantee — no variable researched twice, no connection validated twice — is only possible if the command knows complete state before it begins.

---

## PART 8 — LAYER 1 INSTRUCTION: GENERATE THE BUILD PROMPT

**You must complete this layer before writing any command code. Do not skip to Layer 2.**

Read Parts 1 through 7 of this file. Then, before writing `command-01-research.md`, produce a **Build Prompt** — a structured specification that explicitly maps every section the command must contain to its exact requirements.

The Build Prompt is a numbered list. Each item corresponds to one discrete section of the command file. Write the Build Prompt as your first output in response to this meta-prompt.

**The Build Prompt must cover these sections, in this order:**

1. **File header** — what the header must identify (system name, purpose, governing files, version)

2. **Cold-start READ block** — exact text of the unconditional read sequence, exact halt condition for missing north-star.md, exact initialization logic for absent state.json (SPEC-1 schema), exact initialization for absent knowledge-map.md

3. **Phase detection block** — how `state.phase` is read, how each of the six values maps to phase logic, what happens if `state.phase` contains an unrecognized value

4. **Phase 1 logic block** (Problem Framing) — exact five questions with options, state.json initialization sequence, user_lens_profile field population, phase transition write, next-session.md write

5. **Phase 2 logic block** (Variable Discovery) — variable identification protocol, confidence band assignment per variable, pending_variables[] population, state write, phase transition, next-session.md write

6. **Phase 3 logic block** (Variable Research) — overflow check position and threshold, per-variable research loop, SPEC-5 reasoning chain gate (field requirements), completion criteria (confidence + finding_count), pending→researched move logic, incremental state write timing, phase transition, next-session.md write

7. **Phase 4 logic block** (Connection Validation) — overflow check position, pairwise loop structure, SPEC-9 Synoptic Cognition classification protocol, all four connection types with definitions, validation criteria (≥2 evidence lines + Relevant band), pending→validated move logic, pending→discarded move logic, new variable detection and phase reversion logic, convergence evaluation, phase transition, next-session.md write

8. **Phase 5 logic block** (Synthesis) — knowledge-map.md read before write, conclusion document structure, knowledge-map.md write using SPEC-3 format, cycle_count increment, phase transition, next-session.md write

9. **Phase 6 logic block** (Q&A Mode) — full knowledge map read, question routing logic, answer synthesis rules (knowledge map only, no new research), new topic detection and state reset

10. **knowledge-map.md write routine** — SPEC-3 structure with all required fields per variable and per connection, update logic for adding to existing map vs. creating new map

11. **next-session.md write routine** — SPEC-6 structure with all required fields, what "current phase" field must reflect, exact command format

12. **Meta-prompt generation routine** — when triggered (20,000 token threshold), SPEC-7 structure, state-derived field population, output file path

13. **Constraint enforcement summary** — where in the command each constraint from PART 5 is enforced

14. **Error handling** — what the command outputs when: north-star.md is absent, state.json is malformed, knowledge-map.md is absent on a non-session-1 run, a phase value is unrecognized

Write the Build Prompt now. Number each item. Be specific — not "handle the cold-start" but "open with this exact text block, read north-star.md first, halt with this exact output if absent."

---

## PART 9 — LAYER 2 INSTRUCTION: EXECUTE THE BUILD PROMPT

After producing the Build Prompt from Layer 1, use it to write the complete `command-01-research.md` file.

**Output path:** `universal-research-system/commands/command-01-research.md`

**Requirements the command must satisfy:**

- Opens with the exact COLD-START READ SEQUENCE block from PART 7 — unconditional, not nested in any conditional, runs on every execution
- Phase detection reads `state.phase` exactly — no inference, no fallback to guessing phase from context or conversation
- All six phase logic blocks present, each with: explicit entry condition, all work steps in sequence, incremental state.json writes during research loops, explicit exit trigger that updates state.phase, next-session.md write before session closes
- SPEC-5 reasoning chain gate present in Phase 3 and Phase 4 as a per-finding validation check — not a general reminder but a structural gate that excludes non-compliant findings
- Overflow detection present in Phase 3 (before each variable) and Phase 4 (before each pair) — generates SPEC-7 meta-prompt when threshold exceeded, then halts inline processing
- Convergence evaluation at end of Phase 4 checks both empty conditions (pending_variables[] AND connections.pending[]) before setting phase to synthesis
- knowledge-map.md is read before any write to it, in every phase that touches it
- state.json is written before session output files are generated (MC-8)
- Never writes to `universal-research-system/Research system brain/`
- Session output files follow the naming convention from PART 4.4
- next-session.md contains the exact command the user must type (not a paraphrase)

**Quality gate before submitting:**

After writing the command, verify:
- [ ] Cold-start block is the first thing in the file — nothing precedes it except the header
- [ ] All six phase values (`problem_framing`, `variable_discovery`, `variable_research`, `connection_validation`, `synthesis`, `qa_mode`) have explicit logic blocks
- [ ] Phase 1 contains all five clarifying questions with labeled options
- [ ] Phase 3 contains SPEC-5 field check per finding (Claim, Evidence, Logic, Confidence band)
- [ ] Phase 4 contains all four connection type definitions and SPEC-9 pairwise protocol
- [ ] Phase 5 reads knowledge-map.md before writing it
- [ ] Phase 5 uses SPEC-3 structure for knowledge-map.md output
- [ ] Overflow detection is present in Phase 3 and Phase 4 with the 20,000 token threshold
- [ ] SPEC-7 meta-prompt template is embedded in the overflow generation logic
- [ ] SPEC-6 next-session.md template is used consistently across all six phases
- [ ] No write targets `universal-research-system/Research system brain/`
- [ ] state.json writes occur inside the processing loop (per variable, per pair) not only at session end

Write the complete command. Not a summary. Not a partial draft. The full production-ready file at the correct path.

---

*This file is self-contained. All specifications needed to build `command-01-research.md` are embedded above. Reading `universal-research-system/Research system brain/north-star.md` and `universal-research-system/research-patterns-system-context.md` at session start remains mandatory per Rule NSA-2 and the cold-start sequence — but this file provides sufficient specification to execute both passes without them.*
