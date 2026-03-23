# Research Patterns System — CIE Context Document
**Generated:** 2026-03-15
**Updated:** 2026-03-15 — All 13 wet variables resolved. Decision log: `research-patterns-wet-variable-decisions.md` (same directory).
**Source:** `research-patterns-system-raw-idea.md` (same directory)
**Methodology:** CIE North Star — HAM + ROE + MSA frameworks applied at runtime
**Authority:** `universal-research-system/Research system brain/north-star.md` (read at runtime per Rule NSA-2)
**Downstream use:** `@zzzzzz-alex/universal-feedbackloop-goal-system.md` execution — no additional input required

---

## MANDATORY RUNTIME INSTRUCTION

Any Claude Code session executing from this document must read `universal-research-system/Research system brain/north-star.md` in full before proceeding. This is not optional. Rule NSA-2: never from memory, always read in full.

---

## SECTION 1: HAM EXTRACTION — All Five Abstraction Levels

### Level: meta-meta (WHY this system exists / worldview / identity)

| # | Statement | Type |
|---|---|---|
| MM-1 | Truth is discoverable through systematic, recursive variable mapping | Explicit |
| MM-2 | Seemingly unrelated topics have hidden structural relationships — "Synoptic Cognition / Pattern Weaving" | Explicit |
| MM-3 | The goal is to "zoom out and see systems instead of fragments" — not answer questions but understand systems | Explicit |
| MM-4 | AI must never hallucinate — truth-seeking is paramount; fabrication is a fundamental failure | Explicit |
| MM-5 | Personal worldview filters are real and should be acknowledged — but must not blindly exclude genuinely relevant information | Explicit |
| MM-6 | Research compounds — each cycle discovers more than the last; the system grows without diminishing returns | Explicit |
| MM-7 | The user's cognitive model is one of interconnected systems, not isolated facts | Implicit |
| MM-8 | AI (Claude Code) should do the cognitive heavy lifting; the user architects the conditions | Implicit (from CIE operating mode) |
| MM-9 | Understanding is not a destination — it is an ongoing expanding process | Implicit |

---

### Level: meta (HOW the system is designed to behave)

| # | Statement | Type |
|---|---|---|
| M-1 | Claude Code is the execution engine — each command is a stateless fresh chat | Explicit |
| M-2 | Context is managed via state files — system has no memory except what files contain | Explicit |
| M-3 | The system must handle scaling gracefully — dynamic decomposition when context/output grows | Explicit |
| M-4 | All outputs are written to files before context fills — never after | Explicit |
| M-5 | The CIE north-star is the governing meta-architecture | Explicit |
| M-6 | The universal feedback loop goal system is the governing loop logic | Explicit |
| M-7 | Every run advances research — no redundant work is ever done | Explicit |
| M-8 | Research is filtered through user-approved lens — with confidence scoring on borderline items | Explicit |
| M-9 | The system oscillates between: variable extraction → research → new variable discovery → validation → synthesis | Explicit |
| M-10 | The system must be fully executable from a cold start reading only files | Explicit |
| M-11 | Meta-prompts are generated (not executed manually) when scale exceeds context capacity | Explicit |
| M-12 | Output limit is 32,000 tokens — this is a hard design constraint | Explicit |

---

### Level: macro (WHAT the system produces)

| # | Statement | Type |
|---|---|---|
| MA-1 | A knowledge map: central topic → branches → variable nodes → connection-bubble explanations between each pair | Explicit |
| MA-2 | State files that persist across sessions — the system's external memory | Explicit |
| MA-3 | A structured conclusion document — reliable multi-variable research output for any complex problem | Explicit |
| MA-4 | The ability for a user to ask any question after research completes, answered from the full knowledge map | Explicit |
| MA-5 | Multiple output format options: research document / knowledge map / complex JSON profile / multiple documents | Explicit |
| MA-6 | Clarifying questions output at the start (multiple choice) to establish scope and success criteria | Explicit |
| MA-7 | Meta-prompts for handling scale — generated as artifacts, not inline instructions | Explicit |
| MA-8 | A continuously expanding variable list with connection explanations between every pair | Explicit |
| MA-9 | A reusable protocol — one command, any topic, same system | Implicit |

---

### Level: micro (HOW each component works)

| # | Statement | Type |
|---|---|---|
| MI-1 | Command: user types command + argument (concern / interest / problem / objective) | Explicit |
| MI-2 | Clarifying questions: multiple choice, establishes research scope + success definition + user preference filter | Explicit |
| MI-3 | User clears chat after clarification → sends same command → system moves to next phase | Explicit |
| MI-4 | State file tracks: current phase, researched variables, pending variables, connections found | Explicit |
| MI-5 | Each session: read state → determine phase → execute phase work → update state → write outputs | Explicit |
| MI-6 | Sessions alternate phases: variable research → connection validation → synthesis → new variable discovery | Explicit |
| MI-7 | Confidence scoring on research relevance to user lens (not binary include/exclude) | Explicit |
| MI-8 | Dynamic decomposition: system detects overflow risk and generates meta-prompts to split work | Explicit |
| MI-9 | Knowledge map node structure: variable in center bubble + connection-explanation bubble between every connected pair | Explicit |
| MI-10 | Problem framing is Step 1: define the research question precisely before any variable extraction | Explicit (from ROE decomposition in source) |
| MI-11 | Known variable extraction precedes unknown variable research | Explicit |
| MI-12 | Hypothesis testing (if X then Y) precedes synthesis | Explicit |
| MI-13 | Connection validation is its own discrete step — not merged with research | Explicit |

---

### Level: micro-micro (Edge cases / constraints / failure modes / implicit assumptions)

| # | Statement | Type |
|---|---|---|
| MC-1 | Must never hallucinate — validation step is load-bearing; hallucination = system failure | Explicit |
| MC-2 | Cannot exceed 32,000 token output limit — hard constraint | Explicit |
| MC-3 | Context window must never become bloated — progressive state files, not growing inline context | Explicit |
| MC-4 | Must handle cold start — stateless session reads only files; no assumed prior context | Explicit |
| MC-5 | Must not do redundant research across sessions — state file must track what has been done | Explicit |
| MC-6 | User preference filter must use confidence scoring on borderline items — not hard exclusion | Explicit |
| MC-7 | Example edge case: dentistry ≠ hormone research unless genuinely relevant — relevance is structurally determined, not topically | Explicit |
| MC-8 | State file must be written BEFORE context fills — not after. Critical execution order constraint | Explicit |
| MC-9 | "cloud code" in source = Claude Code (Anthropic CLI) — confirmed | Resolved ambiguity |
| MC-10 | The system itself is an instance of the CIE system it references — meta-system building a research system | Implicit |
| MC-11 | Phase logic must include exit triggers — otherwise phases blur into each other | Implicit |
| MC-12 | The knowledge map is a persistent file artifact, not a chat output — it survives session boundaries | Implicit |
| MC-13 | When the universal feedback loop goal system executes this, it will need the state file schema defined before execution begins | Implicit — critical for execution |

---

## SECTION 2: All Extracted Variables

### Explicit Variables

| # | Variable | Description |
|---|---|---|
| EV-1 | Research question / problem frame | The core user input — what is being researched |
| EV-2 | User objective | What the user wants to understand or achieve |
| EV-3 | User worldview / filter preferences | Approved perspectives, excluded methodologies, worldview constraints |
| EV-4 | Variable list (known) | All variables identified at any point in the research cycle |
| EV-5 | Unknown variable list | Variables identified as relevant but not yet researched |
| EV-6 | Connection map | Relationships between variables, with explanation per pair |
| EV-7 | State file | Current system state — phase, researched/pending/completed work |
| EV-8 | Current phase | Which step in the research cycle the system is currently executing |
| EV-9 | Confidence level | Per-finding relevance score relative to user lens |
| EV-10 | Output format preference | Research doc / knowledge map / JSON profile / multiple documents |
| EV-11 | Context window budget | Available token capacity for current session |
| EV-12 | Output token limit | Hard cap: 32,000 tokens per output |
| EV-13 | Research cycle count | How many full loops the system has completed |
| EV-14 | Meta-prompts | Generated sub-prompts for executing work that overflows current context |

### Implicit Variables

| # | Variable | Description | Why Implicit |
|---|---|---|---|
| IV-1 | Research depth threshold | When is a variable "sufficiently" researched? | Never stated — decision point |
| IV-2 | Connection validation criteria | What makes a connection validated vs. hallucinated? | Described in concept only, not defined |
| IV-3 | Minimum confidence threshold | Numeric floor for including borderline items | Described qualitatively only |
| IV-4 | State file schema | What fields, what structure, what format | Referenced but not designed |
| IV-5 | Phase exit triggers | When does each phase end and the next begin? | UAL template exists but application is undefined |
| IV-6 | Fresh chat trigger mechanism | How does user know when to clear and resend? | Manual described, but automatic not ruled out |
| IV-7 | Knowledge map rendering format | Visual vs. text vs. JSON vs. nested markdown | Described visually in prose, no format specified |
| IV-8 | Hallucination prevention mechanism | Specific technique — cross-reference? Source validation? | Required but not designed |
| IV-9 | Session resume logic | Exact cold-start reconstruction process | Implied by stateless design, not specified |
| IV-10 | Synthesis quality criteria | What makes a synthesis "correct"? | Not defined |
| IV-11 | Maximum loop iterations | Is the loop truly unbounded or does it converge? | Described as perpetual, no exit defined |
| IV-12 | Knowledge map file format | .json / .md / .csv / custom schema | Not specified |

---

## SECTION 3: All Goals

### Explicit Goals

| # | Goal | Abstraction Level |
|---|---|---|
| EG-1 | Build a universal research system applicable to any topic or problem | meta |
| EG-2 | Map all variables related to a research topic | macro |
| EG-3 | Research unknown variables | macro |
| EG-4 | Validate connections between variables | macro |
| EG-5 | Produce a structured conclusion document | macro |
| EG-6 | Make research compound across sessions — no redundant work | meta |
| EG-7 | Enable user to ask any question after research completes | macro |
| EG-8 | Handle scale gracefully without context overflow | meta |
| EG-9 | Filter research through user worldview lens while maintaining truth-seeking | meta |
| EG-10 | Connect seemingly unrelated topics (Synoptic Cognition / Pattern Weaving) | meta-meta |

### Implicit Goals

| # | Goal | Abstraction Level | Inference Source |
|---|---|---|---|
| IG-1 | Preserve user's time — system does cognitive work autonomously | meta-meta | CIE operating mode |
| IG-2 | Build a reusable protocol any user can apply to any problem | meta | "universally for anything" |
| IG-3 | Create a persistent growing knowledge base — not one-shot outputs | meta | "expand more and more" |
| IG-4 | Produce the full knowledge map as a permanent file artifact | macro | visual description in source |
| IG-5 | Make the research system self-directing — finds its own next steps | meta | oscillating cycle description |
| IG-6 | Achieve understanding at the level of interconnected systems, not isolated facts | meta-meta | "zoom out and see systems" |
| IG-7 | Apply CIE north-star methodology to the domain of research | meta | explicit CIE references in source |

---

## SECTION 4: System Ideas — ROE Decompositions

### System Idea 1: Universal Research Orchestrator

**End state:** A Claude Code command that can take any topic and produce a fully mapped, validated knowledge graph of all relevant variables and their connections.

```
End state: Complete knowledge graph for any topic
  ↑ Requires: Synthesis layer — evaluate evidence, state connections, produce conclusion doc
    ↑ Requires: Connection validation layer — confirm each variable relationship with research
      ↑ Requires: Variable research layer — deep research on each variable in the list
        ↑ Requires: Variable discovery layer — identify what variables exist and are relevant
          ↑ Requires: Problem framing layer — define the research question precisely
            → Atomic action 1: clarifying question session (multiple choice)
            → Atomic action 2: initialize state.json with research question + user lens profile
```

**Phase exits:** Problem Framing → Variable Discovery (state: research question confirmed) → Variable Research (state: variable list populated) → Connection Validation (state: all variables researched) → Synthesis (state: all connections validated) → Q&A mode (state: synthesis complete)

---

### System Idea 2: State-Managed Research Loop

**End state:** A stateful, session-persistent research loop that never repeats work and always advances on every execution.

```
End state: Perpetually advancing research — no redundancy, always progress
  ↑ Requires: State file that tracks all completed, in-progress, and pending work
    ↑ Requires: Phase logic — what exact work happens in each phase
      ↑ Requires: Phase transition rules — explicit exit triggers per phase
        ↑ Requires: Cold-start recovery logic — session reads state, resumes from exact position
          ↑ Requires: State file schema designed before first execution
            → Atomic action 1: define state.json schema (fields: phase, researched_variables, pending_variables, connections, cycle_count, last_updated)
            → Atomic action 2: write session-start routine (read state → determine phase → execute)
```

---

### System Idea 3: Dynamic Decomposition Engine

**End state:** A system that detects when output/context will overflow and auto-generates meta-prompts to split work into fresh-chat units without losing continuity.

```
End state: No context overflow, ever, regardless of research volume
  ↑ Requires: Token budget estimator — before execution, predict output size
    ↑ Requires: Split logic — where to split, how to preserve continuity
      ↑ Requires: Meta-prompt generator — writes self-contained fresh-chat execution instructions
        ↑ Requires: Handoff document format — what the next fresh-chat session needs to know
          → Atomic action 1: define split trigger threshold (e.g., estimated output >20,000 tokens)
          → Atomic action 2: define handoff document template (per CIE ROE handoff contract)
          → Atomic action 3: write meta-prompt generator logic
```

---

### System Idea 4: Relevance Filter + Confidence Scorer

**End state:** Research filtered through user worldview lens — does not hard-exclude genuinely relevant cross-domain findings; uses confidence scoring to preserve unexpected connections.

```
End state: Filtered research with preserved cross-domain insights
  ↑ Requires: Confidence scoring system (0–100 relevance to user lens)
    ↑ Requires: User preference profile (what lens to apply)
      ↑ Requires: Preference clarification session (multiple choice questions at start)
        → Atomic action 1: design preference profile format (fields: approved perspectives, excluded methodologies, open to cross-domain Y/N, minimum confidence threshold)
        → Atomic action 2: design confidence scoring rubric (criteria → score mapping)
        → Atomic action 3: design clarifying question set for preference capture
```

---

### System Idea 5: Knowledge Map Builder

**End state:** A complete, growing knowledge map file with variable nodes and connection-bubble explanations between every validated pair.

```
End state: Complete knowledge map file artifact
  ↑ Requires: Connection explanation generator — produces "why/how A connects to B" for every pair
    ↑ Requires: Full validated variable list with research summaries per variable
      ↑ Requires: Pairwise connection analysis — all variable pairs evaluated for relationship
        ↑ Requires: All individual variables researched with confidence scores
          → Atomic action 1: define knowledge map file format (JSON / nested markdown — WET VARIABLE)
          → Atomic action 2: write pairwise analysis routine
          → Atomic action 3: write connection-bubble generator prompt
```

---

### System Idea 6: Q&A Interpreter Layer

**End state:** After research is complete, user asks any question; Claude Code interprets from the full knowledge map without re-running research.

```
End state: Question-answering from complete knowledge map — no redundant research
  ↑ Requires: Complete knowledge map loaded in context
    ↑ Requires: Question routing logic — which variables and connections are relevant to the question
      ↑ Requires: Q&A command that reads state + map files and routes intelligently
        → Atomic action 1: define Q&A command structure (read map file → identify relevant nodes → synthesize answer)
        → Atomic action 2: design question routing criteria (keyword → variable mapping)
```

---

### System Idea 7: Synoptic Cognition Layer

**End state:** The system systematically discovers cross-domain connections — variables that appear unrelated to the research topic but have structural relationships to variables that are related.

```
End state: Cross-domain connection map — insights invisible when looking at subjects in isolation
  ↑ Requires: Cross-domain variable seeding — introducing adjacent/unrelated domains for overlap testing
    ↑ Requires: Structural relationship detection — is the connection architectural, causal, or analogical?
      ↑ Requires: Confidence-gated inclusion — cross-domain findings included if confidence > threshold
        → Atomic action 1: define cross-domain seeding protocol (how to introduce adjacent domains)
        → Atomic action 2: define structural relationship classification (causal / analogical / architectural / correlational)
```

---

## SECTION 5: Nested System Hierarchies (MSA Layer Logic)

```
Layer 0: North Star (universal-research-system/Research system brain/north-star.md)
  — Governs all layers below
  — Never changes except by direct user edit
  — Must be read at runtime before any execution

Layer 1: Universal Research System (this system)
  — The product being built
  — Constrained by Layer 0's CIE frameworks
  — Architecture: state-managed, session-persistent, context-aware research loop

  Sub-systems within Layer 1:
    ├── Problem Framing Sub-system        (clarifying questions → research scope → user lens profile)
    ├── Variable Discovery Sub-system     (initial + ongoing variable identification per cycle)
    ├── Variable Research Sub-system      (deep research per variable + confidence scoring)
    ├── Connection Validation Sub-system  (research inter-variable relationships, confirm or discard)
    ├── Dynamic Decomposition Sub-system  (overflow detection → meta-prompt generation → split execution)
    ├── Relevance Filter Sub-system       (user lens application + confidence scoring on borderline items)
    ├── Knowledge Map Sub-system          (builds + updates persistent map artifact across sessions)
    ├── Synoptic Cognition Sub-system     (cross-domain variable seeding + structural relationship detection)
    └── Q&A Interpreter Sub-system        (reads complete map, routes questions, synthesizes answers)

Layer 2: Research Domain Customization
  — User's research question + preference filter profile
  — Makes Layer 1 adaptable to any topic
  — Does not change Layer 1's architecture
  — Stored in state.json (preference profile fields)

Layer 3: Research Loop Self-Iteration
  — Each command run improves the research state
  — Oscillates: variable extraction → research → discovery → validation → synthesis → repeat
  — Governed by UAL phase logic (Phase 1–5 mapped to research phases)
  — References Layer 0 before each run

Layer 4: Session Execution Units (per fresh chat)
  — Reads state → determines phase → executes one phase's work → writes state + outputs
  — Governed by CTX rules: stateless, file-based, single deliverable per unit
  — Trigger: user clears chat and resends same command
  — Each unit operates from cold start on files only

Layer 5: State Files + Output Files (External Memory)
  — state.json: current phase, variable lists, connection map progress
  — knowledge-map.[format]: the growing knowledge artifact
  — session-outputs/: dated, numbered artifacts from each session
  — Contains no logic — only state
  — Layer 5 IS the system's memory across all sessions
```

**Nesting Depth: 3 levels confirmed**
- Layer 1 contains 9 identified sub-systems
- Each sub-system (e.g., Variable Research) contains its own micro-level logic (research protocol, confidence scoring, hallucination prevention)
- The Dynamic Decomposition Sub-system contains a further nested layer: meta-prompt templates that themselves execute fresh-chat units

---

## SECTION 6: Resolved Decisions — Formerly Wet Variables

All 13 variables resolved. Decision log: `research-patterns-wet-variable-decisions.md`.

| # | Variable | Decision | Resolution |
|---|---|---|---|
| WV-1 | State file schema | **B** | Extended schema: `connections{ validated[], pending[], discarded[] }`, `research_summaries{}` keyed by variable (confidence score + summary text), `session_log[]` dated entries |
| WV-2 | Phase definitions + exit triggers | **A** | 6 explicit phases: Problem Framing → Variable Discovery → Variable Research → Connection Validation → Synthesis → Q&A Mode. Each phase exits on a specific state.json field condition. |
| WV-3 | Connection validation protocol | **B** | Multi-source corroboration + confidence threshold: connection is validated when supported by ≥2 independent lines of evidence AND scores above minimum confidence threshold (WV-12). Single-source connections → pending. |
| WV-4 | Research depth threshold per variable | **B** | Confidence floor + finding count: variable is done when confidence score ≥ minimum threshold (WV-12) AND ≥3 distinct substantive findings recorded in research_summaries{}. |
| WV-5 | Knowledge map file format | **B** | Nested markdown: variable sections with connection subsections. Human-readable, directly loadable into Claude Code context without parsing. |
| WV-6 | Output format selection mechanism | **A** | Upfront selection: one of the multiple-choice clarifying questions at session start. Options: research document / knowledge map / JSON profile / multiple documents. |
| WV-7 | Fresh chat trigger | **B** | System writes `next-session.md` at end of each session containing exact command to send + brief status summary. User reads and triggers manually. |
| WV-8 | Synoptic Cognition implementation | **B** | Structural pairwise analysis: during Connection Validation phase, all variable pairs classified by relationship type (causal / analogical / architectural / correlational). Cross-domain insight emerges from classification, not external seeding. |
| WV-9 | Hallucination prevention mechanism | **B** | Reasoning chain requirement: every research finding must include explicit reasoning chain (evidence + logical path). Findings without reasoning chain → excluded from knowledge map until supplied. |
| WV-10 | Universal feedback loop integration points | **A** | Feedback loop governs phase transitions. Each Claude Code session = one feedback loop iteration: reads state.json → determines phase → executes phase work → writes state → produces session output. The loop IS Layer 3. |
| WV-11 | Meta-prompt structure | **B** | State-derived dynamic generation: meta-prompt generated fresh from state.json contents each time. Structure: context summary + exact phase + pending variable list + execution instruction. No fixed template. |
| WV-12 | Confidence scoring rubric | **B** | Named band system: Core (80–100) include always / Relevant (60–79) include / Borderline (40–59) flag for user review / Weak (20–39) exclude unless pattern confirmed / Exclude (0–19) no structural connection. |
| WV-13 | Convergence rule | **A** | Natural convergence: loop enters Synthesis when `pending_variables[]` is empty AND all `connections.pending[]` items moved to `validated[]` or `discarded[]`. No artificial cycle cap. |

---

## SECTION 7: Execution Readiness Assessment

**STATUS: ALL TIERS RESOLVED — System is executable.**

All 13 wet variables have been resolved. The universal feedback loop goal system may proceed to execution without further decision-making. No open decision points remain.

**Tier 1 — RESOLVED:**
1. ~~WV-1 (state.json schema)~~ → **RESOLVED: B** — Extended schema with typed sub-fields
2. ~~WV-2 (phase definitions + exit triggers)~~ → **RESOLVED: A** — 6 explicit phases with state-based exit triggers
3. ~~WV-3 (connection validation protocol)~~ → **RESOLVED: B** — Multi-source corroboration + confidence threshold
4. ~~WV-10 (universal feedback loop integration points)~~ → **RESOLVED: A** — Loop governs phase transitions; each session = one iteration

**Tier 2 — RESOLVED:**
5. ~~WV-4 (research depth threshold)~~ → **RESOLVED: B** — Confidence floor + ≥3 findings
6. ~~WV-5 (knowledge map file format)~~ → **RESOLVED: B** — Nested markdown
7. ~~WV-9 (hallucination prevention mechanism)~~ → **RESOLVED: B** — Reasoning chain requirement
8. ~~WV-11 (meta-prompt structure)~~ → **RESOLVED: B** — State-derived dynamic generation

**Tier 3 — RESOLVED:**
9. ~~WV-6 (output format selection)~~ → **RESOLVED: A** — Upfront clarifying question
10. ~~WV-8 (Synoptic Cognition implementation)~~ → **RESOLVED: B** — Structural pairwise analysis
11. ~~WV-12 (confidence scoring rubric)~~ → **RESOLVED: B** — Named band system
12. ~~WV-7 (fresh chat trigger)~~ → **RESOLVED: B** — Session-end next-session.md artifact
13. ~~WV-13 (convergence rule)~~ → **RESOLVED: A** — Natural convergence on empty pending_variables[]

---

## SECTION 8: Files Required for Execution

Any Claude Code session executing from this context document will need:

| File | Purpose | Status |
|---|---|---|
| `universal-research-system/Research system brain/north-star.md` | Governing methodology — read at runtime (Rule NSA-2) | Exists |
| `zzzzzz-alex/universal-feedbackloop-goal-system.md` | Loop execution logic | Must be read — path confirmed in source |
| `cie-bootstrap-output/ignore-user-notes/research-patterns-system-raw-idea.md` | Original source — available if needed for reference | Exists |
| `universal-research-system/research-patterns-system-context.md` | This document | Exists |
| `universal-research-system/state.json` | System state — created on first run | Does not exist yet — created by command-01-research.md on first execution |

---

## SECTION 9: Resolved Questions (CIE Handoff Contract Item 5)

All open questions answered. No user input required before execution.

1. **WV-1** — state.json schema: **Extended schema adopted.** Fields: `phase`, `researched_variables[]`, `pending_variables[]`, `connections{ validated[], pending[], discarded[] }`, `cycle_count`, `user_lens_profile`, `last_updated`, `research_summaries{}`, `session_log[]`. Full schema in Section 10.

2. **WV-10** — Feedback loop hook: **As the governing loop itself.** Each Claude Code session = one feedback loop iteration. The loop reads state → determines phase → executes phase work → writes state → produces output artifact. This maps to Layer 3 in the MSA hierarchy.

3. **WV-3** — Hallucination prevention: **Multi-source corroboration + confidence threshold.** A connection is validated when supported by ≥2 independent lines of evidence within the research AND scores above the minimum confidence band (Relevant: 60+). Single-source connections remain pending. All findings must include a reasoning chain (WV-9).

4. **WV-5** — Knowledge map format: **Nested markdown.** Human-readable, directly loadable into Claude Code context without parsing. Variable sections with connection subsections. File: `knowledge-map.md` in the project root.

5. **WV-13** — Convergence condition: **Natural convergence adopted.** Loop enters Synthesis when `pending_variables[]` is empty AND all `connections.pending[]` items are moved to `validated[]` or `discarded[]`. No artificial cycle cap — the system completes when the work is complete.

---

*This document was generated by applying CIE frameworks (HAM + ROE + MSA) to `research-patterns-system-raw-idea.md`. It contains no built systems — only extracted context, identified variables, system ideas, and wet variable decision points. It is designed to be fully sufficient for the universal feedback loop goal system to execute without requiring access to the original source file.*

---

## SECTION 10: Resolved Specifications

Full specifications derived from all 13 resolved decisions. This section is the executable contract — the universal feedback loop goal system reads this as its build spec.

---

### SPEC-1: state.json Full Schema

```json
{
  "phase": "problem_framing | variable_discovery | variable_research | connection_validation | synthesis | qa_mode",
  "cycle_count": 0,
  "last_updated": "ISO-8601 timestamp",
  "user_lens_profile": {
    "approved_perspectives": [],
    "excluded_methodologies": [],
    "open_to_cross_domain": true,
    "minimum_confidence_band": "relevant"
  },
  "researched_variables": [],
  "pending_variables": [],
  "research_summaries": {
    "<variable_name>": {
      "confidence_band": "core | relevant | borderline | weak | exclude",
      "finding_count": 0,
      "summary": "",
      "reasoning_chains": []
    }
  },
  "connections": {
    "validated": [
      { "from": "", "to": "", "type": "causal | analogical | architectural | correlational", "explanation": "", "evidence_count": 0 }
    ],
    "pending": [
      { "from": "", "to": "", "evidence_count": 0 }
    ],
    "discarded": [
      { "from": "", "to": "", "reason": "" }
    ]
  },
  "session_log": [
    { "date": "", "phase_executed": "", "variables_researched": [], "connections_validated": [], "output_file": "" }
  ]
}
```

---

### SPEC-2: Phase Definitions and Exit Triggers

| Phase | Work | Exit Trigger | Next Phase |
|---|---|---|---|
| `problem_framing` | Clarifying question session (multiple choice). Capture: research question, user lens profile, output format preference. Initialize state.json. | `state.user_lens_profile` populated + `state.phase` set | `variable_discovery` |
| `variable_discovery` | Identify all known variables relevant to research question. Populate `pending_variables[]`. Apply confidence band to each. | `pending_variables[]` contains ≥1 item | `variable_research` |
| `variable_research` | Research each variable in `pending_variables[]`. For each: write reasoning chain + ≥3 findings + assign confidence band. Move to `researched_variables[]` when done. | `pending_variables[]` is empty | `connection_validation` |
| `connection_validation` | For every pair in `researched_variables[]`: test for connection. Validate if ≥2 independent evidence lines + confidence ≥ Relevant (60+). Classify type. Move to `validated[]` or `discard[]`. | `connections.pending[]` is empty | `synthesis` (if cycle complete) or `variable_discovery` (if new variables discovered) |
| `synthesis` | Evaluate all validated connections. Produce conclusion document. Write knowledge-map.md. Write next-session.md or close loop. | `knowledge-map.md` written + conclusion doc written | `qa_mode` |
| `qa_mode` | Read knowledge-map.md + state.json. Route question to relevant variable nodes. Synthesize answer. No new research. | User terminates or sends new research question | `problem_framing` (new topic) |

---

### SPEC-3: knowledge-map.md Structure (Nested Markdown)

```markdown
# Knowledge Map — [Research Question]
**Last updated:** [timestamp]  **Cycle:** [n]  **Variables mapped:** [n]

---

## Variable: [Variable Name]
**Confidence band:** Core / Relevant / Borderline
**Summary:** [research summary text]
**Reasoning chain:** [evidence + logical path that supports this variable's inclusion]
**Finding count:** [n]

### Connections from [Variable Name]

#### → [Connected Variable]
**Type:** causal / analogical / architectural / correlational
**Validated:** yes / pending
**Evidence count:** [n]
**Explanation:** [why/how these two variables connect]

#### → [Next Connected Variable]
...

---

## Variable: [Next Variable]
...
```

---

### SPEC-4: Confidence Band Rubric

| Band | Score Range | Inclusion Rule | Use |
|---|---|---|---|
| Core | 80–100 | Include always | Directly addresses research question |
| Relevant | 60–79 | Include | Clearly connected to core variables |
| Borderline | 40–59 | Flag for user review before including | Possible connection — structural basis present |
| Weak | 20–39 | Exclude unless cross-session pattern confirmed | Tenuous — single or indirect link only |
| Exclude | 0–19 | Exclude | No structural connection to research question |

**Minimum threshold for validation:** Relevant (60+)
**Minimum threshold for variable completion (WV-4):** Relevant (60+) AND ≥3 distinct findings

---

### SPEC-5: Reasoning Chain Format

Every research finding stored in `research_summaries[].reasoning_chains[]` must follow this structure:

```
Claim: [the specific finding or connection being asserted]
Evidence: [what supports this claim — described in specific terms]
Logic: [the inferential path from evidence to claim]
Confidence band: [Core / Relevant / Borderline / Weak / Exclude]
```

Findings without all four fields are excluded from the knowledge map and logged as unvalidated.

---

### SPEC-6: next-session.md Structure (Session-End Artifact)

Written at the end of every session before context fills (enforcing MC-8):

```markdown
# Next Session — [date]

## Status
Phase completed: [phase_name]
Current phase: [next_phase_name]
Variables researched this session: [n]
Variables remaining: [n]
Connections validated this session: [n]

## Command to Send
[exact command the user types to resume — same command as previous session]

## What happens next
[one sentence: what the next session will execute]
```

---

### SPEC-7: Meta-Prompt Structure (Dynamic, State-Derived)

Generated when session detects estimated output will exceed 20,000 tokens. Derives all fields from state.json at generation time:

```markdown
# Meta-Prompt — Overflow Split [date]

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
- state.json
- knowledge-map.md
- universal-research-system/Research system brain/north-star.md (Rule NSA-2 — mandatory)
```

---

### SPEC-8: Feedback Loop Integration Map

The universal feedback loop goal system integrates at **Layer 3** (Research Loop Self-Iteration):

```
Each feedback loop iteration = one Claude Code session:
  1. READ: state.json → determine current phase
  2. EXECUTE: phase work per SPEC-2 phase definition
  3. VALIDATE: all outputs meet hallucination prevention (SPEC-5 reasoning chains)
  4. WRITE: update state.json + knowledge-map.md BEFORE context fills (MC-8)
  5. PRODUCE: session output artifact (dated file in session-outputs/)
  6. WRITE: next-session.md (SPEC-6)
  7. EVALUATE: is convergence condition met? (pending_variables[] empty + connections.pending[] empty)
     → YES: advance to synthesis phase
     → NO: loop continues; next session picks up from state
```

---

### SPEC-9: Synoptic Cognition Protocol

Executed during Connection Validation phase for all pairs in `researched_variables[]`:

For each pair (Variable A, Variable B):
1. Classify relationship type: `causal` / `analogical` / `architectural` / `correlational` / `none`
2. If type ≠ `none`: write explanation + add to `connections.pending[]` for validation
3. Validate per SPEC-2 connection validation rule (≥2 evidence lines + Relevant band)
4. Classification note: cross-domain insight is a by-product of structural classification, not a separate seeding step

---

*Updated: 2026-03-15. All 13 wet variables resolved. This document is now a complete, executable specification. No further decisions required before the universal feedback loop goal system begins execution.*
