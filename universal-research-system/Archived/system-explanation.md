# Universal Research System — Complete Technical Explanation

**Generated:** 2026-03-16
**Source files read:** `.claude/commands/command-01-research.md`, `universal-research-system/Research system brain/north-star.md`

---

## Two-Sentence Confirmation

(1) The Universal Research System is a stateless, file-driven AI pipeline that takes any research question as input and builds a validated knowledge artifact — variables, scored connections, and synthesis — across multiple independent AI sessions with zero shared memory between them.
(2) I read 2 files: `command-01-research.md` (the command and execution engine) and `north-star.md` (the absolute governing document in `universal-research-system/Research system brain/`).

---

## SECTION 1: SYSTEM OVERVIEW

**What this system is:** The Universal Research System is a multi-session research pipeline that runs inside Claude Code (an AI CLI). It takes any topic or question, systematically identifies all relevant variables, researches each one against a rigorous quality gate, validates connections between variables, and synthesizes the result into a structured knowledge artifact — across however many AI sessions the scope requires.

**What problem it solves:** Claude Code has zero memory between sessions. A fresh session cannot remember what a prior session discovered. If a research task exceeds one context window — which deep multi-variable research always does — you need a mechanism to preserve all state externally and restore it exactly at the next session start. This system solves that by writing all state to disk (`state.json`) after every significant action and re-reading those files as the first three operations of every session. The command file itself contains all phase logic; the AI contributes no remembered context — it only follows the instructions in the files it reads.

**Who uses it, when, and why:** A single user invokes the system via `/command-01-research [topic]` in Claude Code. The user interacts at three points only: (1) answering five setup questions in Phase 1 to define research scope and filters, (2) optionally reviewing Borderline-confidence variables flagged for review during variable discovery, and (3) asking questions in Phase 6 (Q&A Mode) after synthesis is complete. Between those interaction points, the system operates autonomously, governed entirely by its files.

**What it produces:** A validated knowledge map (`knowledge-map.md`) containing every researched variable with confidence scores and reasoning chains, plus every validated inter-variable connection with type classification and evidence count. Alongside this: a synthesis conclusion document, dated session output files for every session, and a `next-session.md` handoff file telling the user exactly what to run next.

**The governing philosophy (from `north-star.md`):** "The AI is not the product — the system the AI builds and maintains is the product." This is not a one-shot query tool. It is a system that accumulates structured knowledge incrementally, with quality gates at every step, constrained by a governing document (`north-star.md`) that the command must re-read in full at the start of every session without exception (Rule NSA-2).

---

## SECTION 2: ARCHITECTURE

**Components and roles:**

| Component | Location | Role |
|---|---|---|
| Command engine | `.claude/commands/command-01-research.md` | Complete execution logic — all phase sequencing, decision gates, output specs, constraint enforcement |
| North Star | `universal-research-system/Research system brain/north-star.md` | Absolute authority governing document — 8 CIE frameworks; read-only; read at every session start |
| State file | `universal-research-system/state.json` | Complete external memory — all research state persisted between sessions |
| Knowledge map | `universal-research-system/knowledge-map.md` | Primary deliverable — growing structured artifact written in Phase 5 only |
| Session outputs | `universal-research-system/session-outputs/[dated-files].md` | Dated audit trail of each session's work |
| Handoff file | `universal-research-system/next-session.md` | Session-end directive — tells user exactly what command to run next |

**Dependency graph:**

```
User invokes /command-01-research
        ↓
Command engine reads:
  1. north-star.md          ← READ ONLY — never written
  2. state.json             ← read/write — primary state
  3. knowledge-map.md       ← read/write — Phase 5 only

Command engine writes:
  → state.json              (after every variable, every pair, every phase transition)
  → session-outputs/*.md    (one per session, after state.json is written)
  → next-session.md         (every session end)
  → knowledge-map.md        (Phase 5 only, always read before write)
```

**What depends on what:**
- The command engine depends on `north-star.md` being present — its absence halts the entire system
- The command engine depends on `state.json` for phase detection — its absence triggers Phase 1 initialization
- Phase 6 depends on `knowledge-map.md` as its sole answer source
- `next-session.md` is not read by the command engine — it is for the user only
- Session output files are not read by subsequent sessions — `state.json` is the sole continuity mechanism

---

## SECTION 3: COMPONENT BREAKDOWN

---

**COMPONENT:** `.claude/commands/command-01-research.md`
**ROLE:** The complete execution engine — contains all phase logic, decision trees, output format specifications, constraint enforcement, and error handling for the entire research pipeline.
**INPUTS:** (1) Topic/question argument on first invocation; (2) `north-star.md` (READ 1); (3) `state.json` (READ 2); (4) `knowledge-map.md` (READ 3); (5) User answers to five setup questions during Phase 1
**OUTPUTS:** Writes `state.json` (every phase, every variable, every pair), `knowledge-map.md` (Phase 5 only), dated session output files (one per session), `next-session.md` (every session end)
**KEY LOGIC:**
- Cold-start sequence: read `north-star.md` → read `state.json` → read `knowledge-map.md` — fixed order, non-negotiable, before any other logic
- Phase detection: reads `state.phase` from `state.json`; dispatches exclusively to the matching phase block
- Phase 1 (*problem_framing*): presents five setup questions as a single output; maps answers to `user_lens_profile` fields; writes `state.json` with `phase="variable_discovery"` before writing session output file
- Phase 2 (*variable_discovery*): identifies variables filtered by `user_lens_profile`; assigns confidence bands (Core/Relevant/Borderline — Weak/Exclude not added); anti-redundancy check against `researched_variables[]`; writes `state.json` with `phase="variable_research"`
- Phase 3 (*variable_research*): session budget check before each variable (`session_variables_processed × 1,400`; stop if ≥18,000); per-finding SPEC-5 reasoning chain gate (all 4 fields required or finding excluded); completion gate requires overall band ≥Relevant AND ≥3 gate-passing findings; writes `state.json` after each variable before proceeding to the next
- Phase 4 (*connection_validation*): builds all pending pairs from `researched_variables[]` if `connections.pending[]` is empty; session budget check before each pair (`session_pairs_processed × 500`; stop if ≥18,000); classifies each pair as causal/analogical/architectural/correlational/none; validates with ≥2 independent evidence lines both ≥Relevant; detects new variables and reverts to variable_research if found; writes `state.json` after each pair
- Phase 5 (*synthesis*): reads `knowledge-map.md` first (mandatory Step 5.1); identifies emergent patterns (chains, clusters, cross-domain bridges); writes conclusion document; writes/updates `knowledge-map.md`; increments `cycle_count`; sets `phase="qa_mode"`
- Phase 6 (*qa_mode*): answers questions from `knowledge-map.md` only — no new research, no external inference, no speculation; resets state on new topic detection

---

**COMPONENT:** `universal-research-system/Research system brain/north-star.md`
**ROLE:** Absolute authority governing document — defines the CIE operating philosophy, 8 frameworks, and all meta/meta-meta level rules; constrains every command that reads it.
**INPUTS:** None — it reads nothing; it is the primary source
**OUTPUTS:** Behavioral constraints applied to every session that reads it (per Rule NSA-2: must be read at runtime, not from memory)
**KEY LOGIC:**
- Framework 1 (HAM — Hierarchical Abstraction Mapping): requires extracting five levels before acting — meta-meta (why), meta (how designed), macro (what produced), micro (how components work), micro-micro (edge cases, failure modes)
- Framework 2 (ROE — Reverse Outcome Engineering): plan from end state backward; context window fit rule: ≤80,000 tokens per fresh chat; handoff documents must contain exactly 6 elements (current state, decisions made, ruled-out options, what comes next, open questions, files to read)
- Framework 3 (PAA — Prompt-as-Architecture): prompt structure must demonstrate the methodology, not describe it; prompts sent to fresh chats must be fully self-contained
- Framework 4 (NSA — North Star Anchoring): user feedback at micro/micro-micro → implement directly; at macro → implement and log; at meta → pause, quote the principle, ask for confirmation; at meta-meta → pause, require explicit written authorization; Rule NSA-3: this document wins at meta/meta-meta; user wins at macro/micro/micro-micro
- Framework 5 (MSA — Meta-System Architecture): 6-layer stack (Layer 0: north star → Layer 1: system built → Layer 2: brand customization → Layer 3: self-iteration command → Layer 4: implementation plan → Layer 5: audit trail); changes propagate downward only; a lower layer cannot redefine a higher one
- Framework 6 (Context-as-Constraint): each fresh chat is a stateless execution unit; never >3 large files (>500 lines) in context simultaneously; external memory is the folder/file audit trail
- Framework 7 (SOC — Separation of Concerns): infrastructure (command logic, folder architecture, handoff format) requires explicit user authorization to change; content (brand voice, copy, outputs) can be changed freely
- Framework 8 (UAL — Universal Achievement Layer): evaluation/feedback layer; 5 system phases (Orientation → Testing → Optimization → Expansion → Self-iteration); binary decision thresholds: below acceptable quality → 8-layer failure diagnostic; on target → continue; no movement → escalate to self-iteration command
- Research Discernment Rule: research required for platform-specific/version-specific/evolving information; internal context sufficient for stable concepts; research scoped precisely with defined question first
- Rule NSA-1: this document cannot be modified by a command — only by direct user edit
- Rule NSA-2: any command referencing this document must read it at runtime, never from memory

---

**COMPONENT:** `universal-research-system/state.json`
**ROLE:** The system's complete external memory — persists all research state between sessions so every new session resumes exactly where the previous one stopped.
**INPUTS:** Written by the command engine throughout every session
**OUTPUTS:** Read at cold-start (READ 2) to determine phase and restore all research state
**KEY LOGIC:** Contains these fields per SPEC-1 schema:

| Field | Type | Purpose |
|---|---|---|
| `research_question` | string | The topic being researched |
| `phase` | string enum | Current phase — drives phase detection dispatch |
| `cycle_count` | integer | Number of completed research cycles; incremented in Phase 5 |
| `last_updated` | ISO-8601 | Timestamp of last write |
| `user_lens_profile` | object | output_format, approved_perspectives[], excluded_methodologies[], open_to_cross_domain (bool), minimum_confidence_band, research_scope |
| `researched_variables[]` | array | Completed variable names |
| `pending_variables[]` | array | Variables awaiting research |
| `research_summaries{}` | object | Keyed by variable name; each entry: confidence_band, finding_count, summary (2–4 sentences), reasoning_chains[] (each: claim, evidence, logic, confidence_band) |
| `connections.validated[]` | array | {from, to, type, explanation, evidence_count} |
| `connections.pending[]` | array | {from, to, evidence_count} — pairs awaiting evaluation |
| `connections.discarded[]` | array | {from, to, reason} |
| `session_log[]` | array | Session records: date, phase_executed, variables_researched, connections_validated, output_file |

Write timing (MC-8 constraint): written after each variable in Phase 3; written after each pair in Phase 4; written before any session output file is generated in all phases.

---

**COMPONENT:** `universal-research-system/knowledge-map.md`
**ROLE:** The primary growing deliverable — a human-readable structured document encoding all researched variables and validated connections; the sole answer source in Phase 6.
**INPUTS:** Read at cold-start (READ 3) and as mandatory first action in Phase 5 (Step 5.1); written only in Phase 5
**OUTPUTS:** Answer source for all Phase 6 Q&A responses
**KEY LOGIC:** Structure per SPEC-3:
```
# Knowledge Map — [research_question]
**Last updated:** [timestamp]  **Cycle:** [n]  **Variables mapped:** [count]

## Variable: [Name]
**Confidence band:** Core / Relevant / Borderline
**Summary:** [2–4 sentence synthesis from research_summaries]
**Reasoning chain:** [key evidence and logic condensed, 2–4 sentences]
**Finding count:** [n]

### Connections from [Variable Name]
#### → [Connected Variable Name]
**Type:** causal / analogical / architectural / correlational
**Validated:** yes
**Evidence count:** [n]
**Explanation:** [from connections.validated[]]
```
Every variable in `researched_variables[]` and every connection in `connections.validated[]` is included. Discarded connections are excluded. On cycle > 0: existing sections are preserved; new variable sections are added; connection sections are updated where new validated connections exist.

---

**COMPONENT:** `universal-research-system/session-outputs/[YYYY-MM-DD]-[phase]-[n].md`
**ROLE:** Dated audit trail of each session's work — an immutable record of what was produced in each phase execution.
**INPUTS:** Generated from state.json contents and research performed during the session
**OUTPUTS:** Immutable dated record; not read by subsequent sessions (state.json is the authoritative continuity mechanism)
**KEY LOGIC:**

Naming convention:
```
[YYYY-MM-DD]-problem-framing-1.md
[YYYY-MM-DD]-variable-discovery-[cycle].md
[YYYY-MM-DD]-variable-research-[n].md
[YYYY-MM-DD]-connection-validation-[n].md
[YYYY-MM-DD]-synthesis-[cycle_count].md
```
For [n]: count existing files of that type in session-outputs/ and use the next available number.

Content by phase:
- *problem-framing*: research question, all five Q&A pairs as answered, full populated `user_lens_profile` JSON block
- *variable-discovery*: numbered list of all discovered variables, each with confidence band and one-sentence relevance description
- *variable-research*: all variables researched that session — full reasoning chains, finding counts, confidence bands, summaries, completion status
- *connection-validation*: all pairs evaluated — validated connections with types/explanations/evidence counts; discarded connections with reasons
- *synthesis*: complete synthesis document (research question, validated variables, validated connections, emergent patterns, conclusion)

---

**COMPONENT:** `universal-research-system/next-session.md`
**ROLE:** Session-end handoff directive — tells the user exactly what command to run next and what the system will execute; written at the end of every session.
**INPUTS:** Written by the command engine at every session end (every phase)
**OUTPUTS:** Read by the user only — not consumed by subsequent command executions
**KEY LOGIC:** Per SPEC-6 format:
```
# Next Session — [YYYY-MM-DD]

## Status
Phase completed: [phase just executed]
Current phase: [state.phase after transition]
Variables researched this session: [n]
Variables remaining: [count of pending_variables[]]
Connections validated this session: [n]

## Command to Send
/command-01-research

## What happens next
[One sentence — what the next session will execute]
```
"Current phase" reflects the value `state.phase` is set to AFTER the transition, not the phase that just ran. "Command to Send" is `/command-01-research` with no argument for all phases after Phase 1. The research question is stored in `state.json`. The topic argument is only included on the very first invocation when `state.json` does not yet exist. Overwritten each session — not appended.

---

## SECTION 4: EXECUTION FLOW

**Step 1 — Invocation**
User runs `/command-01-research [topic]` in Claude Code. The command engine at `.claude/commands/command-01-research.md` is loaded. State: either `state.json` does not exist (first run) or it exists from a prior session.

**Step 2 — READ 1: north-star.md (cold-start, mandatory)**
Command reads `universal-research-system/Research system brain/north-star.md` in full.
→ If absent: output `HALT: Required file missing — universal-research-system/Research system brain/north-star.md — Do not proceed until this file exists.` Stop entirely.
→ If present: apply all rules. Rule NSA-2 enforces that this read cannot be skipped or substituted from memory.

**Step 3 — READ 2: state.json (cold-start, mandatory)**
Command reads `universal-research-system/state.json`.
→ If absent: initialize with SPEC-1 schema; set `phase="problem_framing"`, `cycle_count=0`, `last_updated=[ISO-8601]`, `research_question=[command argument]`; all arrays and objects empty; write to disk immediately.
→ If present: parse in full; all fields treated as ground truth; no overriding or inferring.

**Step 4 — READ 3: knowledge-map.md (cold-start, mandatory)**
Command reads `universal-research-system/knowledge-map.md`.
→ If absent: initialize as empty file; write to disk; output `WARNING: knowledge-map.md was not found. Initialized as empty.`; continue.
→ If present: read in full before generating any output.

**Step 5 — Phase detection**
Command reads `state.phase`. Dispatches to exactly one phase block.
→ If value is unrecognized: output `ERROR: Unrecognized phase value in state.json: "[value]". Valid values: problem_framing, variable_discovery, variable_research, connection_validation, synthesis, qa_mode. Correct state.json manually and re-run.` Stop.

---

### PHASE 1 — problem_framing (Steps 6–9)

**Step 6 — Initialize artifacts**
Create `session-outputs/` folder if absent. Confirm `research_question` is set; if empty: output `ERROR: No research topic provided.` and stop.

**Step 7 — Present setup questions**
Output all five questions together in a single block. Do not present them sequentially. Do not proceed until all five are answered.
- Q1 → maps to `output_format`: A=research_document, B=knowledge_map, C=json_profile, D=multiple_documents
- Q2 → maps to `approved_perspectives[]`: A=first_principles_systems_thinking, B=empirical_evidence_based, C=practitioner_applied, D=empty array (no filter)
- Q3 → maps to `open_to_cross_domain`: A=true, B=false
- Q4 → maps to `research_scope`: A=broad_survey, B=deep_specific
- Q5 → maps to `excluded_methodologies[]`: A=empty, B=user-specified list

**Step 8 — Populate user_lens_profile**
Set `minimum_confidence_band="relevant"` (default — not from user input). Populate all other fields from user answers. Write into `state.user_lens_profile`.

**Step 9 — Write sequence (MC-8 ordering enforced)**
1. Set `state.phase="variable_discovery"`; set `last_updated`
2. Append to `session_log`
3. **Write `state.json`** — this write occurs before the session output file
4. Write `session-outputs/[YYYY-MM-DD]-problem-framing-1.md`
5. Write `next-session.md` (SPEC-6 format)

---

### PHASE 2 — variable_discovery (Steps 10–13)

**Step 10 — Load filters**
Read `research_question` and `user_lens_profile` from `state.json`.

**Step 11 — Identify variables**
Generate all candidate variables relevant to the research question, applying:
- `approved_perspectives`: if non-empty, include only variables whose methodological basis aligns with listed perspectives
- `excluded_methodologies`: exclude any variable whose basis falls in the excluded list
- `research_scope`: if `broad_survey`, maximize variable count; if `deep_specific`, constrain to highest-confidence variables only
Assign a confidence band to each: Core (80–100), Relevant (60–79), Borderline (40–59, flagged for user review). Do **not** add Weak or Exclude variables.

**Step 12 — Anti-redundancy check (MC-5)**
Before adding any variable to `pending_variables[]`, verify it is not already in `researched_variables[]`. Skip if present.

**Step 13 — Write sequence**
1. Add all identified variable names to `state.pending_variables[]`
2. Set `state.phase="variable_research"`; set `last_updated`
3. Append to `session_log`
4. Write `state.json`
5. Write `session-outputs/[YYYY-MM-DD]-variable-discovery-[cycle_count+1].md`
6. Write `next-session.md`

---

### PHASE 3 — variable_research (Steps 14–22)

**Step 14 — Pre-check (MC-5)**
Remove from `pending_variables[]` any variable name that also appears in `researched_variables[]`.

**Step 15 — Initialize session counter**
`session_variables_processed = 0` (session-local, starts fresh each invocation).

**Step 16 — Session budget check (before each variable)**
Calculate: `session_variables_processed × 1,400`
→ If ≥ 18,000: write `next-session.md` (note variables remaining = count of `pending_variables[]`); **stop** — do not process further variables.
→ If < 18,000: proceed.

**Step 17 — Research the variable**
Produce ≥3 distinct, substantive, non-redundant findings. General statements that restate the variable's definition do not qualify.

**Step 18 — SPEC-5 reasoning chain gate (MC-1 — structural, not advisory)**
For each finding, write all four fields:
```
Claim: [the specific finding or connection being asserted]
Evidence: [what supports this claim — described in specific terms]
Logic: [the inferential path from evidence to claim]
Confidence band: [Core / Relevant / Borderline / Weak / Exclude]
```
A finding missing any field is excluded from the knowledge map and logged as unvalidated. It does **not** count toward `finding_count`.

**Step 19 — Populate research_summaries**
Assign overall `confidence_band` (modal band across validated findings, or minimum if inconsistent). Populate `state.research_summaries[variable_name]` with: confidence_band, finding_count (gate-passing only), summary (2–4 sentence synthesis), reasoning_chains[] array.

**Step 20 — Completion gate**
Both conditions must be simultaneously true:
1. Overall `confidence_band` ≥ Relevant (score 60+)
2. `finding_count` ≥ 3 (gate-passing findings only)
→ Gate passes: remove variable from `pending_variables[]`; add to `researched_variables[]`
→ Gate fails: flag as incomplete in session output; leave in `pending_variables[]`; continue to next variable

**Step 21 — Write state.json (MC-8)**
Write `state.json` immediately after completing each variable — before moving to the next. Increment `session_variables_processed`.

**Step 22 — Phase close (after all pending_variables[] processed)**
1. Set `state.phase="connection_validation"`; set `last_updated`
2. Append to `session_log` (list variables researched this session)
3. Write `state.json`
4. Write `session-outputs/[YYYY-MM-DD]-variable-research-[n].md`
5. Write `next-session.md`

---

### PHASE 4 — connection_validation (Steps 23–32)

**Step 23 — Build pending pair list (if connections.pending[] is empty)**
Enumerate all pairs (A, B) from `researched_variables[]` where A ≠ B. Exclude any pair already in `connections.validated[]` or `connections.discarded[]`. Add remaining pairs to `connections.pending[]` with `evidence_count=0`. Write `state.json` after building the list.

**Step 24 — Initialize session counter**
`session_pairs_processed = 0` (session-local).

**Step 25 — Session budget check (before each pair)**
Calculate: `session_pairs_processed × 500`
→ If ≥ 18,000: write `next-session.md`; **stop**.
→ If < 18,000: proceed.

**Step 26 — Classify relationship type**
Determine which type applies:
- `causal`: A directly causes or produces B — mechanistic, directional link
- `analogical`: A and B share a structural pattern; one domain mirrors the other in form or function
- `architectural`: A and B are components of the same structural system; they co-exist as parts of a larger whole
- `correlational`: A and B co-occur without an established causal direction
- `none`: no structural connection found; variables are genuinely independent

**Step 27 — Type = none path**
Move pair from `connections.pending[]` to `connections.discarded[]` with reason: "No structural connection identified." Proceed to next pair.

**Step 28 — Type ≠ none path: validate**
Write 1–3 sentence explanation of the connection (why/how A connects to B, structural basis). Gather ≥2 independent evidence lines. Independence rule: derived from different sources, domains, or reasoning paths — not the same finding restated differently. Both lines must score ≥ Relevant (60+).
→ Validated (≥2 independent lines, both ≥Relevant): move to `connections.validated[]` recording {from, to, type, explanation, evidence_count}
→ Not validated: move to `connections.discarded[]` recording {from, to, reason}

**Step 29 — New variable detection**
If, during pair research, a variable is identified that is not in `researched_variables[]` AND not in `pending_variables[]`:
1. Add to `pending_variables[]`
2. Complete the current pair processing (validated or discarded per Step 28)
3. Write `state.json` with `phase="variable_research"` (phase reversion)
4. Write `next-session.md` noting the reversion reason
5. **Stop** — do not process any further pairs this session

**Step 30 — Write state.json (MC-8)**
Write `state.json` after each pair, before processing the next. Increment `session_pairs_processed`.

**Step 31 — Convergence evaluation (after all pending[] pairs processed)**
Both must be simultaneously true: `pending_variables[]` is empty AND `connections.pending[]` is empty
→ Both empty: set `state.phase="synthesis"`
→ `pending_variables[]` gained new items (from Step 29): `state.phase="variable_research"` (already set in Step 29)

**Step 32 — Phase close**
1. Set `last_updated`
2. Append to `session_log`
3. Write `state.json`
4. Write `session-outputs/[YYYY-MM-DD]-connection-validation-[n].md`
5. Write `next-session.md`

---

### PHASE 5 — synthesis (Steps 33–37)

**Step 33 — Mandatory pre-read**
Read `knowledge-map.md` in full. This is the first action — non-negotiable. Read `connections.validated[]` from `state.json`.

**Step 34 — Identify emergent patterns**
Evaluate all validated connections for:
- **Chains**: Variable A → B → C (causal or architectural sequence through multiple variables)
- **Clusters**: Multiple variables all connecting to a single central variable (hub structure)
- **Cross-domain bridges**: Analogical connections linking variables from different domains

**Step 35 — Write conclusion document**
Write `session-outputs/[YYYY-MM-DD]-synthesis-[state.cycle_count].md` with sections: Research Question, Validated Variables, Validated Connections, Emergent Patterns, Conclusion.

**Step 36 — Write/update knowledge-map.md**
Write the SPEC-3 structure. On cycle > 0: read in Step 33 ensures existing content is preserved; add new variable sections; update connection sections where new validated connections exist.

**Step 37 — Phase close**
1. **Increment `cycle_count`** (add 1)
2. Set `state.phase="qa_mode"`; set `last_updated`
3. Append to `session_log`
4. Write `state.json` (MC-8 — write after updating `cycle_count`)
5. Write `next-session.md`

---

### PHASE 6 — qa_mode (Steps 38–41)

**Step 38 — Load full context**
Read `knowledge-map.md` in full. Read all `research_summaries` and `connections.validated[]` from `state.json`.

**Step 39 — Classify user input**
Determine whether user message is a question about the current research OR a new research topic unrelated to `state.research_question`.

**Step 40 — Answer (if question about current research)**
Match question's keywords and concepts to 2–5 most relevant variable nodes and validated connections. Compose answer using only content from `knowledge-map.md` and `state.research_summaries`. Rules: no new research, no external inference beyond the knowledge map, no speculation. If insufficient information: output exactly: `"The current knowledge map does not contain sufficient information to answer [question]. To expand the research, run /command-01-research [topic] in a new session — Phase 2 (Variable Discovery) can identify additional variables."` Return to Step 39.

**Step 41 — Reset (if new research topic)**
1. Set `research_question=[new topic]`
2. Clear: `pending_variables[]`, `researched_variables[]`, `research_summaries`, `connections.validated[]`, `connections.pending[]`, `connections.discarded[]`
3. Set `phase="problem_framing"`, `cycle_count=0`
4. Reset `user_lens_profile`: empty arrays, `open_to_cross_domain=true`, `minimum_confidence_band="relevant"`, `output_format=""`, `research_scope=""`
5. Set `last_updated`
6. Write `state.json`
7. Write `next-session.md` with reset format
8. Output: `Research topic reset. Clear this chat and run: /command-01-research [new topic]`

---

## SECTION 5: MICRO-LEVEL DETAILS

**Session budget arithmetic — Phase 3:**
The counter `session_variables_processed` starts at 0 per session invocation. It increments by 1 after each variable, regardless of whether the variable passed or failed the completion gate. The formula `session_variables_processed × 1,400` compared against threshold 18,000 means: at 12 variables, the result is 16,800 (< 18,000, proceed); at 13 variables, the result is 18,200 (≥ 18,000, stop). Effective maximum per session: 12 variables.

**Session budget arithmetic — Phase 4:**
`session_pairs_processed × 500` compared against 18,000. At 35 pairs: 17,500 (proceed); at 36 pairs: 18,000 (stop). Effective maximum per session: 35 pairs.

**Pair count scaling:**
For N variables, Phase 4 must evaluate up to N×(N-1) ordered pairs. At 12 variables: up to 132 ordered pairs (or 66 unordered). The 35-pair session cap means Phase 4 may require multiple sessions for larger variable sets. Each subsequent session resumes from `connections.pending[]` (unevaluated pairs remain there).

AMBIGUITY: The spec says "Enumerate all pairs (A, B) from `researched_variables[]` where A ≠ B" but does not specify whether (A, B) and (B, A) are treated as the same pair or two distinct pairs. The `connections.validated[]` format records `{from, to}`, which implies directionality — A→B and B→A could both be distinct validated connections. This is unresolved in the files.

**SPEC-5 gate is structural, not advisory:**
The command file explicitly states: "This is a hard gate — a finding missing any field is excluded from the knowledge map and logged as unvalidated. It does not count toward `finding_count`." A variable can generate many findings but still fail the completion gate if fewer than 3 pass the four-field SPEC-5 check. Findings that fail the gate are: not included in `research_summaries[].reasoning_chains[]`, not reflected in `finding_count`, and flagged as unvalidated in session output.

**Completion gate is an AND condition:**
Both: (1) overall `confidence_band` ≥ Relevant AND (2) `finding_count` ≥ 3 — both conditions must be simultaneously true. A variable with 5 findings but a Borderline overall band does not complete. A variable with a Core band but only 2 gate-passing findings does not complete. Incomplete variables remain in `pending_variables[]` for the next session.

**Overall confidence_band assignment:**
"Use the modal band across validated findings, or the minimum if findings are inconsistent." Modal = the most frequently occurring band across the variable's gate-passing findings. If there is no clear mode (e.g., equal counts of Core and Relevant), use the minimum (lower-scoring) band. This makes the overall band conservative when evidence is mixed.

**MC-8 write ordering:**
The invariant is: `state.json` is always written before session output files. If context fills between `state.json` write and session output file write, state is preserved. The session output file is recoverable by re-running; the state is not reconstructable from conversation history alone (the system has no conversation history — Rule CTX-1: each fresh chat is stateless).

**Cycle count naming:**
Phase 5 Step 5.3 names the conclusion document `synthesis-[state.cycle_count].md` before incrementing. Step 5.5 then increments `cycle_count`. On first run: `cycle_count=0`, file is named `synthesis-0.md`, then `cycle_count` becomes 1. On second synthesis: file named `synthesis-1.md`, then `cycle_count` becomes 2. This produces zero-indexed filenames.

**Phase 4 new variable detection triggers full stop:**
When Step 4.2.4 detects a new variable, the system must complete the current pair evaluation (move to validated or discarded), then immediately set `phase="variable_research"`, write `state.json`, write `next-session.md`, and stop — processing no additional pairs. The next session will execute Phase 3 to research the new variable, then return to Phase 4 (which will pick up remaining `connections.pending[]` pairs).

**State reset in Phase 6 does not clear session_log:**
Step 6.5 explicitly lists the fields to clear: `pending_variables[]`, `researched_variables[]`, `research_summaries`, `connections.validated[]`, `connections.pending[]`, `connections.discarded[]`. `session_log[]` is not listed among the cleared fields. Session history from prior topics persists across resets.

AMBIGUITY: Whether this is intentional (preserving audit history across topics) or an omission is not specified in the files.

**NSA-2 enforcement mechanism:**
The command file makes `north-star.md` READ 1 in an unconditional cold-start sequence. If the file is absent, the system issues a HALT and stops entirely — it does not attempt to proceed from memory. This is the mechanical enforcement of Rule NSA-2 ("never from memory, always read in full"). A command operating from cached rules could drift from the north star; requiring a live file read on every session makes drift physically impossible.

**Connection type "cross-domain" is not a type:**
The command file does not define "cross-domain" as a relationship type. The five types are: causal, analogical, architectural, correlational, none. Cross-domain insight emerges from the `analogical` type: "If an analogical or architectural connection crosses domain boundaries, that is the finding." Cross-domain is a property of certain analogical/architectural connections — not a separate classification.

**Constraint table (complete):**

| Constraint | Rule | Mechanism |
|---|---|---|
| NSA-2 | Read north-star.md before every session — never from memory | Cold-start READ 1 — unconditional, halts if absent |
| MC-8 | state.json written before context fills | Phase 3: after each variable; Phase 4: after each pair; all phases: before session output |
| MC-5 | No variable researched twice | Phase 2 Step 2.2 (before adding to pending[]); Phase 3 Step 3.0 (pre-check before loop) |
| MC-1 | No hallucination — every finding requires SPEC-5 reasoning chain | Phase 3 Step 3.2.2: four-field gate (structural); Phase 4 Step 4.2.3: ≥2 independent evidence lines |
| M-12 | Output token hard cap: 32,000 tokens per output | Overflow detection in Phase 3 and Phase 4 — threshold at 20,000 estimated remaining |
| M-3 | Session budget cap: 18,000 estimated tokens per session | Phase 3: `session_variables_processed × 1,400`; Phase 4: `session_pairs_processed × 500` |
| Read-only | Never write to `Research system brain/` folder | No write operation in any phase targets that directory |
| MC-3 | Context window never grows with inline history | All state in state.json and knowledge-map.md — no inline history accumulated across sessions |

**Error conditions and exact output messages:**

| Error condition | Exact output |
|---|---|
| `north-star.md` absent | `HALT: Required file missing — universal-research-system/Research system brain/north-star.md — Do not proceed until this file exists.` |
| `state.json` malformed | `ERROR: state.json could not be parsed. It may be corrupted. Inspect the file manually at universal-research-system/state.json. If irreparable, delete it and re-run to reinitialize — note: this will reset all research state to Phase 1.` |
| `knowledge-map.md` absent on non-Phase-1 run | Initialize as empty file and output: `WARNING: knowledge-map.md was not found. Initialized as empty. If prior research exists, verify the file is present at universal-research-system/knowledge-map.md.` |
| Unrecognized phase value | `ERROR: Unrecognized phase value in state.json: "[value]". Valid values: problem_framing, variable_discovery, variable_research, connection_validation, synthesis, qa_mode. Correct state.json manually and re-run.` |
| No argument on first run | `ERROR: No research topic provided. Run: /command-01-research [your topic or question]` |

**The governing file listed but not read at runtime:**
The command file header states `universal-research-system/research-patterns-system-context.md` is a "build spec — all SPEC definitions sourced here." However, this file does not appear in the `Research system brain/` directory and is not included in the cold-start read sequence. All SPEC definitions (SPEC-1 through SPEC-6) are defined inline within the command file itself.

AMBIGUITY: Either (a) this file exists elsewhere in the project and was not provided, (b) it has been superseded by the inline SPEC definitions, or (c) it is a dead reference. The command's execution does not depend on it — all SPECs are self-contained within the command file. A developer modifying the system should not expect this file to be authoritative over the inline SPEC definitions.
