# command-01-research — Universal Research System

**Purpose:** Production execution engine. Takes any topic as input and builds a structured knowledge artifact across multiple independent sessions. One command. Any topic. All phase logic embedded here.

**Version:** 1.0
**Last updated:** 2026-03-15

**Governing files:**
- `universal-research-system/Research system brain/north-star.md` (Rule NSA-2 — read at runtime before every session, never from memory)
- `universal-research-system/research-patterns-system-context.md` (build spec — all SPEC definitions sourced here)

**Invocation:** `/command-01-research [topic or question]`

**Architecture note:** Claude Code has zero memory between sessions. All continuity is maintained exclusively through files on disk. This command reads its full operating context from files at the start of every run — never from memory, never from conversation history.

---

## COLD-START READ SEQUENCE

Execute all three reads below before any other logic. Do not skip. Do not reorder.

**READ 1:** `universal-research-system/Research system brain/north-star.md`
- If absent: **HALT.** Output exactly: `HALT: Required file missing — universal-research-system/Research system brain/north-star.md — Do not proceed until this file exists.` Do not continue.
- If present: Read in full. Apply all rules defined there. Rule NSA-2: never from memory, always read in full.

**READ 2:** `universal-research-system/state.json`
- If absent: Initialize with SPEC-1 schema (see below). Set `phase = "problem_framing"`, `cycle_count = 0`, `last_updated = [current ISO-8601 timestamp]`. Set `research_question` from the argument supplied to this command. All arrays and objects empty. Write the initialized file to disk immediately.
- If present: Parse in full. Treat all fields as ground truth. Do not infer or override any field.

**READ 3:** `universal-research-system/knowledge-map.md`
- If absent: Initialize as empty file at that path. Write it to disk.
- If present: Read in full before generating any output.

--- Cold-start sequence complete. Proceed to phase detection. ---

---

## SPEC-1: Initial state.json Schema

Use this schema when initializing state.json for the first time (READ 2 above, absent case):

```json
{
  "research_question": "[argument supplied to this command]",
  "phase": "problem_framing",
  "cycle_count": 0,
  "last_updated": "[ISO-8601 timestamp]",
  "user_lens_profile": {
    "approved_perspectives": [],
    "excluded_methodologies": [],
    "open_to_cross_domain": true,
    "minimum_confidence_band": "relevant",
    "output_format": "",
    "research_scope": ""
  },
  "researched_variables": [],
  "pending_variables": [],
  "research_summaries": {},
  "connections": {
    "validated": [],
    "pending": [],
    "discarded": []
  },
  "session_log": []
}
```

---

## PHASE DETECTION

After completing the cold-start sequence, read `state.phase`. Dispatch to the corresponding phase section below. Execute only the phase indicated — do not execute other phase sections.

| `state.phase` value | Execute |
|---|---|
| `problem_framing` | Phase 1: Problem Framing |
| `variable_discovery` | Phase 2: Variable Discovery |
| `variable_research` | Phase 3: Variable Research |
| `connection_validation` | Phase 4: Connection Validation |
| `synthesis` | Phase 5: Synthesis |
| `qa_mode` | Phase 6: Q&A Mode |
| Any other value | Output: `ERROR: Unrecognized phase value in state.json: "[value]". Valid values: problem_framing, variable_discovery, variable_research, connection_validation, synthesis, qa_mode. Correct state.json manually and re-run.` Do not continue. |

---

## PHASE 1: PROBLEM FRAMING

**Entry condition:** `state.json` was just initialized (absent) OR `state.phase = "problem_framing"`

### Step 1.1 — Initialize session artifacts

If `universal-research-system/session-outputs/` folder does not exist, create it.

Confirm `state.research_question` is set from the command argument. If the command was run without an argument and `state.research_question` is empty or blank, output: `ERROR: No research topic provided. Run: /command-01-research [your topic or question]` and stop.

### Step 1.2 — Present clarifying questions

Present all five questions below together in a single output. Do not present them one at a time. Do not proceed until the user has answered all five.

---

**Research Setup — Answer all 5 questions to define scope and filter for this research cycle.**

**Q1 — Output format**
What format should the final research output take?
- A) Research document — narrative prose with structured sections
- B) Knowledge map only — variable nodes and connection explanations
- C) JSON profile — machine-readable structured data
- D) Multiple documents — all of the above

**Q2 — Research lens**
What worldview or framework should filter the research?
- A) First-principles / systems thinking — structural relationships only
- B) Empirical / evidence-based — published research and data
- C) Practitioner / applied — what works in real-world application
- D) No filter — broadest possible coverage

**Q3 — Cross-domain openness**
Should the system include findings from unrelated domains if they are structurally relevant?
- A) Yes — include cross-domain findings if the structural connection is confirmed
- B) No — stay within the research topic's domain only

**Q4 — Research scope**
How should the system approach depth vs. breadth?
- A) Broad survey — identify as many variables as possible
- B) Deep specific — fewer variables, exhaustive research on each

**Q5 — Exclusions**
Are there any methodologies, frameworks, or domains to explicitly exclude?
- A) None — include everything above minimum confidence
- B) Specify: [user provides free text answer]

---

### Step 1.3 — Process answers and populate user_lens_profile

After receiving user answers, populate `state.user_lens_profile` fields:

- `output_format`: Q1 → `"research_document"` (A) / `"knowledge_map"` (B) / `"json_profile"` (C) / `"multiple_documents"` (D)
- `approved_perspectives`: Q2 → `["first_principles_systems_thinking"]` (A) / `["empirical_evidence_based"]` (B) / `["practitioner_applied"]` (C) / `[]` (D — no filter, include all)
- `open_to_cross_domain`: Q3 → `true` (A) / `false` (B)
- `research_scope`: Q4 → `"broad_survey"` (A) / `"deep_specific"` (B)
- `excluded_methodologies`: Q5 → `[]` (A) / `[items specified by user]` (B)
- `minimum_confidence_band`: set to `"relevant"` (default — score 60+ required for inclusion)

### Step 1.4 — Write state, outputs, and next-session

Execute in this order:

1. Set `state.phase = "variable_discovery"`
2. Set `state.last_updated = [current ISO-8601 timestamp]`
3. Append to `state.session_log`:
   ```json
   {
     "date": "[ISO-8601]",
     "phase_executed": "problem_framing",
     "variables_researched": [],
     "connections_validated": [],
     "output_file": "session-outputs/[YYYY-MM-DD]-problem-framing-1.md"
   }
   ```
4. **Write `universal-research-system/state.json`** — this write happens BEFORE generating the session output file (MC-8 constraint)
5. Write session output file: `universal-research-system/session-outputs/[YYYY-MM-DD]-problem-framing-1.md`
   - Content: research question, all five Q&A pairs as answered, full populated `user_lens_profile` JSON block
6. Write `universal-research-system/next-session.md` using SPEC-6 format (see Output Specifications section)

**Exit trigger:** `user_lens_profile` populated → `phase = "variable_discovery"`

---

## PHASE 2: VARIABLE DISCOVERY

**Entry condition:** `state.phase = "variable_discovery"`

### Step 2.1 — Identify variables

Read `state.research_question` and `state.user_lens_profile` from state.json.

Identify all variables relevant to the research question, filtered through `user_lens_profile`:
- If `approved_perspectives` is non-empty: include only variables whose methodological basis aligns with those perspectives
- Apply `excluded_methodologies`: exclude any variable whose basis falls in the excluded list
- Apply `research_scope`: if `broad_survey`, maximize variable count; if `deep_specific`, constrain to highest-confidence variables only

For each identified variable, assign a confidence band from SPEC-4 (see Output Specifications section):
- Include `Core` (80–100) and `Relevant` (60–79) variables unconditionally
- Include `Borderline` (40–59) variables with a flag noting they need user review
- Do **not** add `Weak` or `Exclude` variables to `pending_variables[]` at this stage

### Step 2.2 — Anti-redundancy check (MC-5)

Before adding any variable to `pending_variables[]`, verify it is not already in `state.researched_variables[]`. If it is, skip it — do not re-add.

### Step 2.3 — Write state, outputs, and next-session

Execute in this order:

1. Add all identified variable names to `state.pending_variables[]`
2. Set `state.phase = "variable_research"`
3. Set `state.last_updated = [current ISO-8601 timestamp]`
4. Append to `state.session_log`
5. **Write `universal-research-system/state.json`** (MC-8)
6. Write session output file: `universal-research-system/session-outputs/[YYYY-MM-DD]-variable-discovery-[state.cycle_count + 1].md`
   - Content: numbered list of all discovered variables, each with assigned confidence band and one-sentence description of why it is relevant
7. Write `universal-research-system/next-session.md` (SPEC-6 format)

**Exit trigger:** `pending_variables[]` contains ≥1 item → `phase = "variable_research"`

---

## PHASE 3: VARIABLE RESEARCH

**Entry condition:** `state.phase = "variable_research"`

### Step 3.0 — Anti-redundancy pre-check (MC-5)

Before processing any variable, confirm it is not in `state.researched_variables[]`. If a variable name appears in both `pending_variables[]` and `researched_variables[]`, remove it from `pending_variables[]` immediately. Do not research it again.

### Step 3.1 — Overflow check (run before processing each variable)

Before beginning work on each variable, estimate the remaining output for this session.

**If estimated remaining output exceeds 20,000 tokens:**
1. Generate a SPEC-7 meta-prompt (see Output Specifications section) for the remaining items in `state.pending_variables[]`
2. Write it to: `universal-research-system/session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md` (n = next available number, counted from existing meta-prompt files in session-outputs/)
3. Write current `universal-research-system/state.json`
4. Write `universal-research-system/next-session.md` (SPEC-6 format)
5. **Stop.** Do not continue processing any more variables inline.

### Step 3.2 — Per-variable research loop

For each variable in `state.pending_variables[]`, execute the following sequence:

**3.2.1 — Research the variable**

Produce ≥3 distinct, substantive findings for this variable. Findings must be specific and non-redundant. General statements that restate the variable's definition do not count.

**3.2.2 — SPEC-5 Reasoning Chain Gate (structural — not advisory)**

For each finding, write a reasoning chain. All four fields are required. This is a hard gate — a finding missing any field is excluded from the knowledge map and logged as unvalidated. It does not count toward `finding_count`.

```
Claim: [the specific finding or connection being asserted]
Evidence: [what supports this claim — described in specific terms]
Logic: [the inferential path from evidence to claim]
Confidence band: [Core / Relevant / Borderline / Weak / Exclude]
```

If a finding cannot pass this gate (cannot articulate all four fields), it is excluded. A variable with fewer than 3 gate-passing findings is not complete.

**3.2.3 — Populate research_summaries**

After all findings for this variable are gate-checked:

- Assign an overall `confidence_band` to the variable (use the modal band across validated findings, or the minimum if findings are inconsistent)
- Populate `state.research_summaries[variable_name]`:
  ```json
  {
    "confidence_band": "[band]",
    "finding_count": [count of gate-passing findings only],
    "summary": "[brief synthesis of all validated findings — 2–4 sentences]",
    "reasoning_chains": [
      {
        "claim": "[string]",
        "evidence": "[string]",
        "logic": "[string]",
        "confidence_band": "[string]"
      }
    ]
  }
  ```

**3.2.4 — Completion gate**

A variable is complete when **both** conditions are simultaneously true:
1. Overall `confidence_band` ≥ Relevant (score 60+)
2. `finding_count` ≥ 3 (gate-passing findings only)

If either condition is not met:
- Flag the variable as incomplete in the session output
- Do not move it from `pending_variables[]` to `researched_variables[]`
- If no additional findings are discoverable in this session, note it as incomplete and continue — it remains in `pending_variables[]` for the next session

**3.2.5 — Move variable on completion**

When the completion gate passes:
1. Remove the variable name from `state.pending_variables[]`
2. Add the variable name to `state.researched_variables[]`

**3.2.6 — Write state.json after each variable (MC-8)**

After completing the research for each variable (whether it passed the completion gate or not), write `universal-research-system/state.json` **before proceeding to the next variable**. This ensures state is preserved if context fills mid-session.

### Step 3.3 — Phase close

After all items in `pending_variables[]` have been processed:

1. Set `state.phase = "connection_validation"`
2. Set `state.last_updated = [current ISO-8601 timestamp]`
3. Append to `state.session_log` (include list of variables researched this session)
4. **Write `universal-research-system/state.json`** (MC-8)
5. Write session output file: `universal-research-system/session-outputs/[YYYY-MM-DD]-variable-research-[n].md`
   - Content: all variables researched this session, each with full reasoning chains, finding counts, confidence bands, summaries, and completion status
6. Write `universal-research-system/next-session.md` (SPEC-6 format)

**Exit trigger:** `pending_variables[]` empty → `phase = "connection_validation"`

---

## PHASE 4: CONNECTION VALIDATION

**Entry condition:** `state.phase = "connection_validation"`

### Step 4.0 — Build initial pending pair list

If `state.connections.pending[]` is empty at session start, build it:
- Enumerate all pairs (A, B) from `state.researched_variables[]` where A ≠ B
- Exclude any pair already in `connections.validated[]` or `connections.discarded[]`
- Add each remaining pair to `state.connections.pending[]` with `evidence_count = 0`
- Write `universal-research-system/state.json` after building the list

### Step 4.1 — Overflow check (run before processing each pair)

Before beginning work on each pair, estimate the remaining output for this session.

**If estimated remaining output exceeds 20,000 tokens:**
1. Generate a SPEC-7 meta-prompt for the remaining items in `state.connections.pending[]`
2. Write it to: `universal-research-system/session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md`
3. Write current `universal-research-system/state.json`
4. Write `universal-research-system/next-session.md` (SPEC-6 format)
5. **Stop.** Do not continue processing any more pairs inline.

### Step 4.2 — Synoptic Cognition Protocol (SPEC-9) — pairwise loop

For each pair (Variable A, Variable B) in `state.connections.pending[]`, execute the following sequence:

**4.2.1 — Classify the relationship type**

Determine which of the following applies:

| Type | Definition |
|---|---|
| `causal` | Variable A directly causes or produces Variable B — mechanistic, directional link |
| `analogical` | Variables A and B share a structural pattern; one domain mirrors the other in form or function |
| `architectural` | Variables A and B are components of the same structural system; they co-exist as parts of a larger whole |
| `correlational` | Variables A and B co-occur without an established causal direction |
| `none` | No structural connection found; the variables are genuinely independent |

Cross-domain insight is a by-product of this structural classification — not a separate seeding step. If an analogical or architectural connection crosses domain boundaries, that is the finding.

**4.2.2 — If type ≠ `none`**

Write an explanation of the connection (1–3 sentences: why/how A connects to B, what the structural basis is). The pair is already in `connections.pending[]`.

**If type = `none`:** Move the pair directly from `connections.pending[]` to `connections.discarded[]` with reason: "No structural connection identified." Proceed to next pair.

**4.2.3 — Validate the connection**

Gather ≥2 independent lines of evidence for the connection.

**Independence rule:** Evidence lines are independent if they are derived from different sources, domains, or reasoning paths — not the same finding restated in different words.

**Confidence requirement:** Both evidence lines must score ≥ Relevant (60+) on the confidence band rubric (SPEC-4).

**Validation decision:**

- **Validated** (≥2 independent evidence lines, both ≥ Relevant):
  - Move pair from `connections.pending[]` to `connections.validated[]`
  - Record: `{ "from": "[A]", "to": "[B]", "type": "[type]", "explanation": "[explanation]", "evidence_count": [n] }`

- **Not validated** (fewer than 2 independent lines, or evidence below Relevant):
  - Move pair from `connections.pending[]` to `connections.discarded[]`
  - Record: `{ "from": "[A]", "to": "[B]", "reason": "[why validation failed — specific]" }`

**4.2.4 — New variable detection**

If, while researching the connection between A and B, you identify a variable that is:
- Not in `state.researched_variables[]`, AND
- Not in `state.pending_variables[]`

Then:
1. Add the new variable to `state.pending_variables[]`
2. Complete the current pair's processing (move to validated or discarded per 4.2.3)
3. Write `universal-research-system/state.json` with `phase = "variable_research"` — the new variable must be researched before connection validation continues
4. Write `universal-research-system/next-session.md` (SPEC-6 format, noting phase reversion reason)
5. **Stop the current session.** Do not process any further pairs.

**4.2.5 — Write state.json after each pair (MC-8)**

After completing each pair (moved to validated or discarded), write `universal-research-system/state.json` **before processing the next pair**.

### Step 4.3 — Convergence evaluation

After all pairs in `connections.pending[]` are processed and no new variables were detected:

**Convergence condition — both must be true simultaneously:**
1. `state.pending_variables[]` is empty
2. `state.connections.pending[]` is empty

| Condition result | Action |
|---|---|
| Both empty | Set `state.phase = "synthesis"` |
| `pending_variables[]` gained new items (from Step 4.2.4) | Set `state.phase = "variable_research"` |

### Step 4.4 — Phase close

1. Set `state.last_updated = [current ISO-8601 timestamp]`
2. Append to `state.session_log` (include list of connections validated and discarded this session)
3. **Write `universal-research-system/state.json`** (MC-8)
4. Write session output file: `universal-research-system/session-outputs/[YYYY-MM-DD]-connection-validation-[n].md`
   - Content: all connection pairs evaluated this session — validated connections with types, explanations, evidence counts; discarded connections with reasons
5. Write `universal-research-system/next-session.md` (SPEC-6 format)

**Exit trigger:** `connections.pending[]` empty → `phase = "synthesis"` or `phase = "variable_research"`

---

## PHASE 5: SYNTHESIS

**Entry condition:** `state.phase = "synthesis"`

### Step 5.1 — Read before writing (mandatory)

**Read `universal-research-system/knowledge-map.md` in full before writing anything to it.** This is the first action in Phase 5. Non-negotiable. If the file is empty or does not exist, initialize it and continue. Do not write to it without reading it first.

Read `state.connections.validated[]` in full.

### Step 5.2 — Identify emergent patterns

Evaluate all validated connections for emergent patterns:
- **Chains:** Variable A → B → C (causal or architectural sequence through multiple variables)
- **Clusters:** Multiple variables all connecting to a single central variable (hub structure)
- **Cross-domain bridges:** Analogical connections linking variables from different domains

Note all patterns identified. They appear in both the conclusion document and the knowledge map.

### Step 5.3 — Write conclusion document

Write to: `universal-research-system/session-outputs/[YYYY-MM-DD]-synthesis-[state.cycle_count].md`

Structure:
```
# Research Synthesis — [research_question]
**Date:** [YYYY-MM-DD]  **Cycle:** [cycle_count]

## Research Question
[state.research_question]

## Validated Variables
[For each variable in researched_variables[]: name, confidence band, 2–3 sentence summary]

## Validated Connections
[For each connection in connections.validated[]: "A → B — [type] — [explanation]"]

## Emergent Patterns
[Identified chains, clusters, and cross-domain bridges with explanations]

## Conclusion
[Synthesized answer to the research question based on the full variable and connection map]
```

### Step 5.4 — Write/update knowledge-map.md (SPEC-3)

Write `universal-research-system/knowledge-map.md` using the following structure exactly:

```markdown
# Knowledge Map — [research_question]
**Last updated:** [ISO-8601 timestamp]  **Cycle:** [cycle_count]  **Variables mapped:** [count of researched_variables[]]

---

## Variable: [Variable Name]
**Confidence band:** Core / Relevant / Borderline
**Summary:** [research_summaries[variable_name].summary]
**Reasoning chain:** [key evidence and logical path — condensed from reasoning_chains[], 2–4 sentences]
**Finding count:** [research_summaries[variable_name].finding_count]

### Connections from [Variable Name]

#### → [Connected Variable Name]
**Type:** causal / analogical / architectural / correlational
**Validated:** yes
**Evidence count:** [evidence_count]
**Explanation:** [connections.validated[].explanation for this pair]

#### → [Next Connected Variable Name]
[repeat structure for each validated connection from this variable]

---

## Variable: [Next Variable Name]
[repeat full structure for every variable in researched_variables[]]
```

**Include:** every variable in `researched_variables[]`, every connection in `connections.validated[]`.
**Exclude:** discarded connections.

**Update logic (cycle > 0):** Read the existing content first (done in Step 5.1). Preserve all existing variable sections. Add new variable sections for any variable not yet in the map. Update connection sections where new validated connections have been added.

### Step 5.5 — Phase close

Execute in this order:

1. Increment `state.cycle_count` (add 1)
2. Set `state.phase = "qa_mode"`
3. Set `state.last_updated = [current ISO-8601 timestamp]`
4. Append to `state.session_log`
5. **Write `universal-research-system/state.json`** (MC-8 — write after updating cycle_count)
6. Write `universal-research-system/next-session.md` (SPEC-6 format)

**Exit trigger:** `knowledge-map.md` written + conclusion doc written → `phase = "qa_mode"`

---

## PHASE 6: Q&A MODE

**Entry condition:** `state.phase = "qa_mode"`

### Step 6.1 — Load full context

Read `universal-research-system/knowledge-map.md` in full.
Read all `state.research_summaries` and `state.connections.validated[]` from state.json.

### Step 6.2 — Receive and classify user input

Wait for the user's message. Determine whether it is:
- **A question about the current research** → proceed to Step 6.3
- **A new research topic** (a question or topic unrelated to `state.research_question`) → proceed to Step 6.5

### Step 6.3 — Route question to relevant nodes

Match the question's keywords and concepts to:
1. Variable names in `state.researched_variables[]`
2. Connection types (causal, analogical, architectural, correlational)
3. Specific relationship pairs in `state.connections.validated[]`

Identify the 2–5 most relevant variable nodes and any validated connections between them that directly address the question.

### Step 6.4 — Synthesize answer from knowledge map only

Compose an answer using only:
- Content from `knowledge-map.md` (variable summaries, reasoning chains, connection explanations)
- Content from `state.research_summaries` (validated findings for the relevant variables)

**Rules for Q&A answers:**
- No new research
- No external inference beyond what the knowledge map contains
- No speculation
- If the knowledge map does not contain sufficient information to answer the question, state this explicitly: `"The current knowledge map does not contain sufficient information to answer [question]. To expand the research, run /command-01-research [topic] in a new session — Phase 2 (Variable Discovery) can identify additional variables."`

After answering, return to Step 6.2 to wait for the next question.

### Step 6.5 — New topic detection and state reset

If the user's message is a new research question unrelated to the current `state.research_question`:

1. Set `state.research_question = [new topic]`
2. Clear: `state.pending_variables[]`, `state.researched_variables[]`, `state.research_summaries`, `state.connections.validated[]`, `state.connections.pending[]`, `state.connections.discarded[]`
3. Set `state.phase = "problem_framing"`
4. Set `state.cycle_count = 0`
5. Reset `state.user_lens_profile` to defaults: empty arrays, `open_to_cross_domain = true`, `minimum_confidence_band = "relevant"`, `output_format = ""`, `research_scope = ""`
6. Set `state.last_updated = [current ISO-8601 timestamp]`
7. **Write `universal-research-system/state.json`**
8. Write `universal-research-system/next-session.md`:
   ```
   # Next Session — [YYYY-MM-DD]

   ## Status
   Phase completed: qa_mode (reset)
   Current phase: problem_framing
   Research topic reset to: [new topic]
   Variables researched this session: 0
   Variables remaining: 0
   Connections validated this session: 0

   ## Command to Send
   /command-01-research [new topic]

   ## What happens next
   Clear this chat. Run the command above. The system will start Phase 1 (Problem Framing) for the new research topic.
   ```
9. Output to user: `Research topic reset. Clear this chat and run: /command-01-research [new topic]`

**Exit trigger:** User terminates OR new research topic detected → `phase = "problem_framing"`

---

## OUTPUT FORMAT SPECIFICATIONS

### SPEC-4: Confidence Band Rubric

| Band | Score Range | Inclusion Rule | When to Use |
|---|---|---|---|
| Core | 80–100 | Include always | Directly addresses the research question |
| Relevant | 60–79 | Include | Clearly connected to one or more Core variables |
| Borderline | 40–59 | Flag for user review before including | Possible connection — structural basis present but not confirmed |
| Weak | 20–39 | Exclude unless cross-session pattern confirmed | Tenuous — single or indirect link only |
| Exclude | 0–19 | Exclude | No structural connection to research question |

**Minimum threshold for variable completion:** Relevant (60+) AND ≥3 gate-passing findings
**Minimum threshold for connection validation:** Relevant (60+) AND ≥2 independent lines of evidence

### SPEC-5: Reasoning Chain Format

Every research finding stored in `research_summaries[].reasoning_chains[]` must contain all four fields. A finding missing any field is excluded from the knowledge map and logged as unvalidated.

```
Claim: [the specific finding or connection being asserted]
Evidence: [what supports this claim — described in specific terms]
Logic: [the inferential path from evidence to claim]
Confidence band: [Core / Relevant / Borderline / Weak / Exclude]
```

### SPEC-6: next-session.md Structure

Written at the end of every session, every phase, before context fills (enforcing MC-8):

```markdown
# Next Session — [YYYY-MM-DD]

## Status
Phase completed: [phase just executed]
Current phase: [next phase — what state.phase is now set to]
Variables researched this session: [n]
Variables remaining: [count of pending_variables[]]
Connections validated this session: [n]

## Command to Send
/command-01-research [original research question — exact text, not a placeholder]

## What happens next
[One sentence describing what the next session will execute]
```

**"Current phase"** must reflect the value `state.phase` is set to AFTER the phase transition — not the phase that just ran.
**"Command to Send"** must contain the actual research question text, not the word "topic" or any other placeholder.

### SPEC-7: Meta-Prompt Structure (Overflow Split)

Generated when estimated session output exceeds 20,000 tokens. All fields derived from `state.json` at generation time — no fixed template values.

```markdown
# Meta-Prompt — Overflow Split [YYYY-MM-DD]

## Context (from state.json)
Research question: [state.research_question]
Current phase: [state.phase]
Cycle: [state.cycle_count]

## Pending work for this split
Variables to research: [list the specific variable names from state.pending_variables[] assigned to this split]
Connections to validate: [list the specific pairs from state.connections.pending[] assigned to this split]

## Execution instruction
Read state.json and knowledge-map.md. Execute ONLY the pending work listed above.
Write results to state.json and knowledge-map.md before context fills.
Write next-session.md on completion.

## Files to read at session start
- universal-research-system/state.json
- universal-research-system/knowledge-map.md
- universal-research-system/Research system brain/north-star.md (Rule NSA-2 — mandatory)
```

After writing the meta-prompt: write current `state.json`, write `next-session.md`, then stop — do not continue inline processing.

### Session Output File Naming Convention

```
session-outputs/[YYYY-MM-DD]-problem-framing-1.md
session-outputs/[YYYY-MM-DD]-variable-discovery-[cycle].md
session-outputs/[YYYY-MM-DD]-variable-research-[n].md
session-outputs/[YYYY-MM-DD]-connection-validation-[n].md
session-outputs/[YYYY-MM-DD]-synthesis-[cycle].md
session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md
```

For `[n]`: count existing files of that type in session-outputs/ and use the next available number.

---

## CONSTRAINT ENFORCEMENT

| Constraint ID | Rule | Where enforced in this command |
|---|---|---|
| NSA-2 | Read north-star.md before every session — never from memory | Cold-start READ 1 — unconditional, first block in this file |
| MC-8 | state.json written BEFORE context fills — never after | Phase 3: after each variable (Step 3.2.6); Phase 4: after each pair (Step 4.2.5); all phases: before writing session output (Step X.3/X.4/X.5 ordering) |
| MC-5 | No variable researched twice | Phase 2 Step 2.2 (before adding to pending_variables[]); Phase 3 Step 3.0 (pre-check before loop) |
| MC-1 | No hallucination — every finding requires SPEC-5 reasoning chain | Phase 3 Step 3.2.2: per-finding field gate (structural, not advisory); Phase 4 Step 4.2.3: ≥2 independent evidence lines required for validation |
| M-12 | Output token hard cap: 32,000 tokens per output | Overflow detection in Phase 3 (Step 3.1) and Phase 4 (Step 4.1) — threshold at 20,000 estimated remaining |
| M-3 | Dynamic decomposition at 20,000 token estimated output | SPEC-7 meta-prompt generation in Phase 3 Step 3.1 and Phase 4 Step 4.1 |
| Read-only | Never write to `Research system brain/` folder | No write operation in any phase targets `universal-research-system/Research system brain/` — this directory is read-only |
| MC-3 | Context window never grows with inline history | All state in state.json and knowledge-map.md — no inline history accumulated across sessions |

---

## ERROR HANDLING

| Error condition | Output |
|---|---|
| `north-star.md` absent | `HALT: Required file missing — universal-research-system/Research system brain/north-star.md — Do not proceed until this file exists.` |
| `state.json` malformed (cannot parse) | `ERROR: state.json could not be parsed. It may be corrupted. Inspect the file manually at universal-research-system/state.json. If irreparable, delete it and re-run to reinitialize — note: this will reset all research state to Phase 1.` |
| `knowledge-map.md` absent on non-Phase-1 run | Initialize as empty file and continue. Output: `WARNING: knowledge-map.md was not found. Initialized as empty. If prior research exists, verify the file is present at universal-research-system/knowledge-map.md.` |
| Unrecognized phase value in state.json | `ERROR: Unrecognized phase value in state.json: "[value]". Valid values: problem_framing, variable_discovery, variable_research, connection_validation, synthesis, qa_mode. Correct state.json manually and re-run.` |
| Command run without argument (Phase 1, research_question empty) | `ERROR: No research topic provided. Run: /command-01-research [your topic or question]` |

---

## SESSION EXECUTION ORDER (every session, every phase)

```
1. READ   → north-star.md (cold-start READ 1 — unconditional)
2. READ   → state.json (cold-start READ 2 — determine phase)
3. READ   → knowledge-map.md (cold-start READ 3)
            ↓
4. DETECT → state.phase → dispatch to phase logic
            ↓
5. EXECUTE → phase work per phase section above
            ↓
6. VALIDATE → all findings include SPEC-5 reasoning chains (Phase 3 and 4)
            ↓
7. WRITE  → state.json updated (BEFORE generating session output — MC-8)
8. UPDATE → knowledge-map.md (Phase 5 only — always read before write)
            ↓
9. PRODUCE → session output artifact → session-outputs/[dated file]
            ↓
10. WRITE → next-session.md (SPEC-6 format)
            ↓
11. EVALUATE → convergence: pending_variables[] empty AND connections.pending[] empty?
               YES → state.phase = "synthesis"
               NO  → loop continues; next session picks up from state
```

The state.json write (step 7) always precedes session output generation (step 9). If context fills between steps 7 and 9, state is preserved. The phase logic writes state.json incrementally inside processing loops (after each variable, after each pair) — not only at session end.

---

*This file is read-only. It is never modified by the command. All state lives in `universal-research-system/state.json`. All research artifacts live in `universal-research-system/knowledge-map.md` and `universal-research-system/session-outputs/`. The `Research system brain/` folder is never written to programmatically — it is a read-only instruction layer modified only by the user.*
