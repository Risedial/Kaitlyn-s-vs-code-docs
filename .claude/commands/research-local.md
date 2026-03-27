# /research-local-local — Universal Research System
**command-01-research | Version 1.1 | Updated: 2026-03-22**

**Purpose:** Production execution engine. Takes any topic as input and builds a validated knowledge artifact across multiple independent sessions. One command. Any topic. All phase logic embedded here.

**Governing authority:** `universal-research-system/Research system brain/north-star.md` (Rule NSA-2 — read at runtime before every session, never from memory)

**Invocation:** `/research-local [topic or question]`
**Topic provided:** $ARGUMENTS

**Architecture note:** Claude Code has zero memory between sessions. All continuity is maintained exclusively through files on disk. This command reads its full operating context from files at the start of every run — never from memory, never from conversation history.

---

## CRITICAL FAILURE POINTS — READ ALL BEFORE EXECUTING ANY LOGIC

These are the known places where this system fails. Enforce all of them throughout the session, not just at session start.

**FP-1 — Cold-start reads skipped or reordered.** The three reads below are unconditional and sequential. No phase logic runs before all three reads complete. Generating output before reading state.json means executing the wrong phase or using stale state.

**FP-2 — Variable researched twice (MC-5 violation).** Before adding any variable to `pending_variables[]` (Phase 2 Step 2.2): check `state.researched_variables[]`. Before processing any variable in the research loop (Phase 3 Step 3.0): check again. If a variable appears in both lists, remove it from `pending_variables[]` immediately. Never research it again.

**FP-3 — SPEC-5 reasoning chain gate treated as advisory.** The gate is structural. Every finding requires all four fields: Claim, Evidence, Logic, Confidence band. A finding missing any one field is excluded and does not count toward `finding_count`. A variable with fewer than 3 gate-passing findings is not complete. Do not count partial findings.

**FP-4 — state.json written after session output (MC-8 violation).** Write order is non-negotiable: (1) state.json after each variable in Phase 3 and after each pair in Phase 4, (2) then session output file, (3) then next-session.md. If context fills mid-session, state must be preserved. Session outputs may be lost; state.json must not be.

**FP-5 — Session budget exceeded without stopping.** Phase 3: `session_variables_processed × 1,400 ≥ 18,000` → stop immediately. Phase 4: `session_pairs_processed × 500 ≥ 18,000` → stop immediately. After hitting budget: write next-session.md, then stop. Do not process one more variable or pair.

**FP-6 — Connection pairs built from wrong variable list.** Phase 4 Step 4.0: build the pending pair list from `state.researched_variables[]` only. Variables in `state.pending_variables[]` are not yet eligible for connection validation.

**FP-7 — Writing knowledge-map.md without reading it first.** Phase 5 Step 5.1: read `knowledge-map.md` in full before writing anything to it. Non-negotiable. Even if the file is empty, the read must occur before the write.

**FP-8 — Generating new research in Q&A Mode.** Phase 6 answers come exclusively from `knowledge-map.md` and `state.research_summaries`. No new research, no external inference, no speculation. If the knowledge map lacks sufficient information, state this explicitly.

**FP-9 — Missing new variable detection during connection validation.** Phase 4 Step 4.2.4: if a new variable is discovered during connection research, add it to `pending_variables[]`, finish the current pair, set `phase = "variable_research"` in state.json, write state, write next-session.md, and stop. Do not continue validating more pairs in the same session.

**FP-10 — Independence rule violated in connection validation.** Two evidence lines are independent only if derived from different sources, domains, or reasoning paths. Restating the same finding differently does not produce two independent lines. Connections without ≥2 genuinely independent lines at Relevant confidence (60+) go to `connections.discarded[]`.

**FP-11 — Convergence condition checked incorrectly.** Phase 4 Step 4.3: convergence requires both simultaneously: `pending_variables[]` is empty AND `connections.pending[]` is empty. A non-empty `pending_variables[]` sends the system back to `variable_research`, not to synthesis.

**FP-12 — Phase transition not written to state.json before session ends.** Every phase transition must be written to state.json before any session output is generated. The phase value in state.json is ground truth for the next session.

**FP-13 — next-session.md includes topic argument after Phase 1.** After Phase 1, the research question is stored in state.json. The command in next-session.md must be `/research-local` with no argument. Only the very first run (Phase 1 initialization) includes the topic as an argument.

**FP-14 — Writing to the Research system brain/ folder.** This folder is read-only. No phase, error condition, or edge case justifies writing to `universal-research-system/Research system brain/`. Read north-star.md from it. Never write to it.

**FP-15 — Phase 0 skipped when source-content-map.md is absent.** If `universal-research-system/source-content-map.md` does not exist on cold-start, Phase 0 runs unconditionally before phase detection. No phase logic — including Phase 1 — runs before Phase 0 completes and source-content-map.md is written to disk. The presence of the file is the only valid signal that Phase 0 is complete.

---

## COLD-START READ SEQUENCE

Execute all three reads below before any other logic. Do not skip. Do not reorder.

**READ 1:** `universal-research-system/Research system brain/north-star.md`
- If absent: **HALT.** Output exactly: `HALT: Required file missing — universal-research-system/Research system brain/north-star.md — Do not proceed until this file exists.` Do not continue.
- If present: Read in full. Apply all rules defined there. Rule NSA-2: never from memory, always read in full.

**READ 2:** `universal-research-system/state.json`
- If absent: Initialize with SPEC-1 schema (see below). Set `phase = "problem_framing"`, `cycle_count = 0`, `last_updated = [current ISO-8601 timestamp]`. Set `research_question` from the argument supplied to this command (`$ARGUMENTS`). All arrays and objects empty. Write the initialized file to disk immediately.
- If present: Parse in full. Treat all fields as ground truth. Do not infer or override any field.

**READ 3:** `universal-research-system/knowledge-map.md`
- If absent: Initialize as empty file at that path. Write it to disk.
- If present: Read in full before generating any output.

**READ 4:** `universal-research-system/source-content-map.md`
- If absent: Run Phase 0 (Source Content Mapping) before proceeding to phase detection. Do not skip. Phase 0 writes the map and updates state.json, then returns here.
- If present: Read in full. This map is active context for all research phases, especially Phase 3.

--- Cold-start sequence complete (all four reads done or Phase 0 run). Proceed to phase detection. ---

---

## SPEC-1: Initial state.json Schema

Use this schema when initializing state.json for the first time (READ 2 above, absent case):

```json
{
  "research_question": "[argument supplied to this command]",
  "phase": "problem_framing",
  "cycle_count": 0,
  "source_content_map_built": false,
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

## PHASE 0: SOURCE CONTENT MAPPING

**Entry condition:** `universal-research-system/source-content-map.md` does not exist on cold-start (READ 4 above, absent case).

This phase runs once, before phase detection. It is not pointed to by `state.phase`. It is triggered exclusively by the absence of `source-content-map.md`. After completing, execution returns to the cold-start sequence — READ 4 is now satisfied — and phase detection proceeds normally.

### Step 0.1 — Enumerate source content

Use the Glob tool with pattern `universal-research-system/research-local-source-content/**/*` to list all files recursively.

If no files are found: write `universal-research-system/source-content-map.md` with the following content, then proceed to Step 0.4:

```markdown
# Source Content Map
**Built:** [ISO-8601 timestamp]
**Total files mapped:** 0

No files found in research-source-content/. Add .md or .txt files to that folder and delete source-content-map.md to trigger a rebuild.
```

### Step 0.2 — Generate file summaries

For each file returned by Glob:
1. Use the Read tool to read the file (default settings — first 2000 lines or full file, whichever is smaller)
2. Generate a 1–3 sentence summary of the file's content: what topic(s) it covers, what kind of information it contains, and any notable structure
3. Record: relative path from project root, file extension, summary

Organize entries by folder hierarchy.

### Step 0.3 — Write source-content-map.md

Write `universal-research-system/source-content-map.md` using this structure exactly:

```markdown
# Source Content Map
**Built:** [ISO-8601 timestamp]
**Total files mapped:** [n]

---

## [folder-name]/

### [folder-name]/filename.md
**Type:** .md
**Summary:** [1–3 sentence description of what this file contains and what topics it covers]

### [folder-name]/filename2.txt
**Type:** .txt
**Summary:** [1–3 sentence description]

---

## [another-folder]/

### [another-folder]/filename.md
**Type:** .md
**Summary:** [1–3 sentence description]
```

If files exist at the root of `research-source-content/` (not in any subfolder), list them under a `## research-source-content/ (root)` heading.

### Step 0.4 — Update state.json

1. Set `state.source_content_map_built = true`
2. Set `state.last_updated = [current ISO-8601 timestamp]`
3. Write `universal-research-system/state.json` immediately (MC-8)

Phase 0 does not produce a session output file and does not write next-session.md. After writing source-content-map.md and state.json, return to the cold-start sequence: READ 4 is now satisfied. Proceed to phase detection.

**Constraint:** `research-source-content/` is read-only from this system's perspective. Files are only read during this phase — never written to. Only `source-content-map.md` and `state.json` are written during Phase 0.

---

## PHASE 1: PROBLEM FRAMING

**Entry condition:** `state.json` was just initialized (absent) OR `state.phase = "problem_framing"`

### Step 1.1 — Initialize session artifacts

If `universal-research-system/session-outputs/` folder does not exist, create it.

Confirm `state.research_question` is set from the command argument. If the command was run without an argument and `state.research_question` is empty or blank, output: `ERROR: No research topic provided. Run: /research-local [your topic or question]` and stop.

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

### Step 3.1 — Session budget check (run before processing each variable)

Maintain a session-local counter: `session_variables_processed` — starts at 0 when this command runs, increments by 1 after each variable is completed (pass or fail the completion gate).

**Before beginning work on each variable:**
Calculate: `session_variables_processed × 1,400`

**If result ≥ 18,000:**
1. `state.json` is already current (MC-8 wrote it after the last variable)
2. Write `universal-research-system/next-session.md` (SPEC-6 format — set "Variables remaining" to count of `pending_variables[]`)
3. **Stop.** Do not process any more variables this session.

**If result < 18,000:** Proceed to research this variable.

### Step 3.2 — Per-variable research loop

For each variable in `state.pending_variables[]`, execute the following sequence:

**3.2.1 — Research the variable from local source content**

Source-content-map.md is in active context from the cold-start READ 4. Use the following navigation strategy:

**Step A — Map inference**
Read source-content-map.md. Reason about which files are most likely to contain information relevant to this variable. Consider: file names, folder organization, and the 1–3 sentence summaries. Select 2–5 candidate files.

**Step B — Grep confirmation**
Generate 2–4 keyword variants derived from this variable's name (synonyms, related terms, domain-specific phrasing). Run Grep across `universal-research-system/research-local-source-content/` for each keyword.

Cross-reference Grep results with map inference candidates:
- Files that appear in both: read in full (or by targeted line range — see Step C)
- Files selected by map inference but not hit by Grep: include only if high-confidence based on summary
- Files hit by Grep but not selected by map inference: include if Grep match appears substantively relevant
- Files in neither category: do not read

If Grep returns no hits for any keyword variant across any file: rely on map inference candidates only. If map inference also identifies no candidates, skip directly to the web fallback below.

**Step C — Targeted file reading**
Read each file on the confirmed read list using the Read tool.
- For small files: read in full (no offset/limit needed)
- For large files: use Grep match line numbers to identify relevant sections; use offset and limit parameters in Read to fetch those sections (read ±50 lines around each match)
- Do not read files outside the confirmed read list

**Step D — Finding extraction**
Extract specific, substantive findings from the content read. Findings must be specific, non-redundant, and traceable to a specific passage in a specific file. General statements that restate the variable's definition do not count. The Evidence field in the SPEC-5 reasoning chain must name the source file: `Evidence: [specific content from research-source-content/path/to/file.md — describe the relevant passage]`

**Web fallback (conditional)**
After completing Steps A–D: if gate-passing finding count is fewer than 3, supplement with web research.
- Label all web-sourced findings: `Evidence: [web fallback — [n] local files checked, [n] gate-passing findings found locally — web source: describe the source]`
- Web-sourced findings still require all four SPEC-5 fields
- The session output for this variable must note: "Web fallback triggered — [n] local files checked, [n] gate-passing findings from local content"

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

### Step 4.1 — Session budget check (run before processing each pair)

Maintain a session-local counter: `session_pairs_processed` — starts at 0 when this command runs, increments by 1 after each pair is moved to validated or discarded.

**Before beginning work on each pair:**
Calculate: `session_pairs_processed × 500`

**If result ≥ 18,000:**
1. `state.json` is already current (MC-8 wrote it after the last pair)
2. Write `universal-research-system/next-session.md` (SPEC-6 format — set "Connections remaining" to count of `connections.pending[]`)
3. **Stop.** Do not process any more pairs this session.

**If result < 18,000:** Proceed to evaluate this pair.

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
- If the knowledge map does not contain sufficient information to answer the question, state this explicitly: `"The current knowledge map does not contain sufficient information to answer [question]. To expand the research, run /research-local [topic] in a new session — Phase 2 (Variable Discovery) can identify additional variables."`

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
   /research-local [new topic]

   ## What happens next
   Clear this chat. Run the command above. The system will start Phase 1 (Problem Framing) for the new research topic.
   ```
9. Output to user: `Research topic reset. Clear this chat and run: /research-local [new topic]`

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
/research-local

(No argument needed after Phase 1 — the research question is stored in state.json. Only include the research question as an argument when state.json does not yet exist.)

## What happens next
[One sentence describing what the next session will execute]
```

**"Current phase"** must reflect the value `state.phase` is set to AFTER the phase transition — not the phase that just ran.
**"Command to Send"** is `/research-local` with no argument for all phases after problem_framing. The research question is read from state.json. Only include the question as an argument on the very first run when state.json does not exist.

### SPEC-7: Meta-Prompt Structure (Deprecated — not used in execution path)

This format is no longer generated automatically. Session management is handled by the session budget check in Phase 3 Step 3.1 and Phase 4 Step 4.1. SPEC-7 is retained for reference only.

### Session Output File Naming Convention

```
session-outputs/[YYYY-MM-DD]-problem-framing-1.md
session-outputs/[YYYY-MM-DD]-variable-discovery-[cycle].md
session-outputs/[YYYY-MM-DD]-variable-research-[n].md
session-outputs/[YYYY-MM-DD]-connection-validation-[n].md
session-outputs/[YYYY-MM-DD]-synthesis-[cycle].md
```

For `[n]`: count existing files of that type in session-outputs/ and use the next available number.

---

## CONSTRAINT ENFORCEMENT

| Constraint ID | Rule | Where enforced |
|---|---|---|
| NSA-2 | Read north-star.md before every session — never from memory | Cold-start READ 1 — unconditional, first block in this file |
| MC-8 | state.json written BEFORE context fills — never after | Phase 3: after each variable (Step 3.2.6); Phase 4: after each pair (Step 4.2.5); all phases: before writing session output |
| MC-5 | No variable researched twice | Phase 2 Step 2.2 (before adding to pending_variables[]); Phase 3 Step 3.0 (pre-check before loop) |
| MC-1 | No hallucination — every finding requires SPEC-5 reasoning chain | Phase 3 Step 3.2.2: per-finding field gate (structural, not advisory); Phase 4 Step 4.2.3: ≥2 independent evidence lines required |
| M-12 | Output token hard cap: 32,000 tokens per output | Overflow detection in Phase 3 (Step 3.1) and Phase 4 (Step 4.1) |
| M-3 | Session budget cap: stop at 18,000 estimated tokens used per session | Phase 3 Step 3.1 and Phase 4 Step 4.1 — session counters enforce per-session budget |
| Read-only | Never write to `Research system brain/` folder | No write operation in any phase targets that directory |
| Read-only (source) | Never write to `research-source-content/` folder | Phase 0: only writes source-content-map.md and state.json — never writes files inside research-source-content/ |
| MC-3 | Context window never grows with inline history | All state in state.json and knowledge-map.md — no inline history accumulated across sessions |

---

## ERROR HANDLING

| Error condition | Output |
|---|---|
| `north-star.md` absent | `HALT: Required file missing — universal-research-system/Research system brain/north-star.md — Do not proceed until this file exists.` |
| `state.json` malformed (cannot parse) | `ERROR: state.json could not be parsed. Inspect the file manually at universal-research-system/state.json. If irreparable, delete it and re-run to reinitialize — note: this will reset all research state to Phase 1.` |
| `knowledge-map.md` absent on non-Phase-1 run | Initialize as empty file and continue. Output: `WARNING: knowledge-map.md was not found. Initialized as empty. If prior research exists, verify the file is present at universal-research-system/knowledge-map.md.` |
| Unrecognized phase value in state.json | `ERROR: Unrecognized phase value in state.json: "[value]". Valid values: problem_framing, variable_discovery, variable_research, connection_validation, synthesis, qa_mode. Correct state.json manually and re-run.` |
| Command run without argument (Phase 1, research_question empty) | `ERROR: No research topic provided. Run: /research-local [your topic or question]` |

---

## SESSION EXECUTION ORDER (every session, every phase)

```
1. READ   → north-star.md (cold-start READ 1 — unconditional)
2. READ   → state.json (cold-start READ 2 — determine phase)
3. READ   → knowledge-map.md (cold-start READ 3)
3a. CHECK → source-content-map.md (cold-start READ 4)
            IF absent → run Phase 0 (Source Content Mapping) → write map + state.json → return here
            IF present → read in full
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

*All state lives in `universal-research-system/state.json`. All research artifacts live in `universal-research-system/knowledge-map.md` and `universal-research-system/session-outputs/`. The `Research system brain/` folder is never written to programmatically — it is a read-only instruction layer modified only by the user.*
