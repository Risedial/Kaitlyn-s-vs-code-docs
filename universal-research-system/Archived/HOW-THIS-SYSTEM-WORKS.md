# HOW THIS SYSTEM WORKS
**System:** Universal Research System
**Command:** `command-01-research.md`
**Governed by:** `universal-research-system/Research system brain/north-star.md`

---

## SECTION 1 — WHAT THIS SYSTEM IS

This is the Universal Research System — a Claude Code slash-command-driven research tool that accepts a topic argument and progressively builds a structured knowledge artifact about that topic across multiple sessions.

The system is portable. The entire `universal-research-system/` folder can be dropped into any workspace and will function without modification, provided the North Star document is present at `universal-research-system/Research system brain/north-star.md`.

The system has one command: `command-01-research.md`. This command contains all logic for all six research phases. It is the only file the user ever runs.

The system is governed by the CIE North Star document located at:
`universal-research-system/Research system brain/north-star.md`

The North Star defines all naming conventions, command file structure, behavioral rules, and failure modes. Any executing instance of Claude Code must read the North Star at the start of every session — never from memory, always from the file. This is Rule NSA-2 and it is non-negotiable.

The fully resolved specification for this system is at:
`universal-research-system/research-patterns-system-context.md`

All architectural decisions have been made. All specs are written in that document. When building `command-01-research.md`, Claude Code reads `research-patterns-system-context.md` as the build contract and implements exactly what is specified there — no interpretation, no gap-filling.

---

## SECTION 2 — WHAT GETS BUILT AND WHERE

**The execution engine:**
`universal-research-system/commands/command-01-research.md`

This file contains the full phase logic for all six research phases. It is the execution engine for the entire system — the only file the user ever runs.

**What the command initializes on first run (if not already present):**

| File | Purpose | Created by |
|---|---|---|
| `universal-research-system/state.json` | External memory — tracks current phase, session count, confirmed variables, research completion, connection status | Command, on first run |
| `universal-research-system/knowledge-map.md` | The growing research artifact — nested markdown, accumulates structured knowledge across sessions | Command, on first run |
| `universal-research-system/session-outputs/` | Folder for per-session output files, dated and numbered | Command, on first run |
| `universal-research-system/next-session.md` | Written at the end of every session — tells user exactly what to type to begin the next session | Command, at end of every session |

**The static layer (never modified programmatically):**

`universal-research-system/Research system brain/` is a read-only subfolder. Claude Code never writes to it, never modifies it, and never deletes anything in it. It exists to provide read-only instruction and context. Currently it contains `north-star.md`, placed there manually. Any future additions to this folder are made by the user manually.

**The specification document:**

`universal-research-system/research-patterns-system-context.md` is the fully resolved build spec. It contains:
- All extracted system variables (explicit and implicit)
- All system goals (explicit and implicit)
- ROE decompositions for all 7 sub-systems
- MSA layer hierarchy (Layers 0–5)
- All 13 resolved wet variable decisions
- 9 executable specifications (state.json schema, phase definitions, knowledge-map structure, confidence rubric, reasoning chain format, next-session.md format, meta-prompt structure, feedback loop integration map, Synoptic Cognition protocol)

This document is the authoritative source. When any ambiguity arises during implementation, the answer is in this file.

---

## SECTION 3 — HOW THE USER OPERATES THIS SYSTEM

**Starting a research session:**

The user types a slash command followed by a topic:

```
/command-01-research [topic or question]
```

Example:
```
/command-01-research What makes high-performance teams different from average ones?
```

**Session 1 — Problem Framing:**

The command asks the user approximately five multiple-choice clarifying questions to establish:
- What output format is desired (research document / knowledge map / JSON profile / multiple documents)
- What lens or worldview the research should be filtered through
- Whether cross-domain findings are welcome if structurally relevant
- The research scope (broad survey vs. deep specific investigation)

The user answers all questions in the same session. The command then initializes `state.json` with the user's lens profile and sets phase to `variable_discovery`. The command writes `next-session.md` and the session ends.

**All subsequent sessions — the only workflow:**

1. User reads `next-session.md` (it contains the exact command to type)
2. User clears the chat (starts a fresh Claude Code session — no memory carries over)
3. User types the exact command shown in `next-session.md`
4. Claude Code executes the appropriate phase, writes outputs, writes the next `next-session.md`
5. Repeat from step 1

There is no other workflow. The user does not decide what happens next. The command reads `state.json`, determines the phase, and executes it. The user's only input is the topic (once, in session 1) and the session trigger (every session after).

**The six phases in sequence:**

| Phase | What happens | Session ends when |
|---|---|---|
| 1 — Problem Framing | Clarifying questions. User lens profile captured. state.json initialized. | User has answered all clarifying questions |
| 2 — Variable Discovery | System identifies all variables relevant to the research topic. Assigns confidence bands. Populates pending_variables[]. | All identified variables listed in state.json |
| 3 — Variable Research | Deep research on each variable. Reasoning chains written. Confidence scored. Variables moved from pending to researched when done (≥3 findings + confidence ≥ Relevant). | pending_variables[] is empty |
| 4 — Connection Validation | All variable pairs tested for structural relationships (causal / analogical / architectural / correlational). Connections validated when ≥2 independent evidence lines above Relevant confidence. | connections.pending[] is empty |
| 5 — Synthesis | All validated connections evaluated. Conclusion document produced. knowledge-map.md finalized. | knowledge-map.md written and conclusion document written |
| 6 — Q&A Mode | User asks any question. Command reads knowledge-map.md and answers from it. No new research runs. | User terminates or starts a new research topic |

**Phase transitions are automatic.** The command detects when the exit condition for the current phase is met, updates `state.json`, and the next session begins at the next phase. The user does not manage this.

**Between sessions, the user can:**
- Read `knowledge-map.md` to see research progress
- Read `session-outputs/` for dated session artifacts
- Read `next-session.md` to see what comes next

---

## SECTION 4 — THE COLD-START READ SEQUENCE

### Why It Exists: Stateless Execution and State Continuity

Claude Code has no memory between sessions. Every session starts cold. There is no shared context, no conversation history, no implicit knowledge of what happened in previous sessions.

The entire continuity of this system depends on a single mechanism: the command file reading external state from disk at the start of every run, before doing anything else. If the command executes any logic before completing the cold-start read sequence, the system operates on invented or stale state — and every output it produces from that point forward is potentially wrong.

This is not a hypothetical edge case. It is the default failure mode of any multi-session, stateless system. The only protection is strict, unconditional enforcement of the read sequence at the top of the command file.

### The Required Cold-Start Reading Sequence

The following three reads must occur in this exact order, before any other logic executes:

**Read 1: `universal-research-system/Research system brain/north-star.md`**

Purpose: Establish naming conventions, behavioral rules, command file structure, and failure mode handling. The North Star governs how the command interprets everything that comes after it.

Why first: The North Star defines the rules used to interpret state.json and knowledge-map.md. Reading state.json before the North Star means operating without the rules that define what the state fields mean and how they should be used.

If absent: Halt. Output the exact path that is missing. Do not proceed. Do not attempt to reconstruct the North Star from memory.

**Read 2: `universal-research-system/state.json`**

Purpose: Establish ground truth for the current phase, session number, confirmed variables, pending variables, connection status, and user lens profile.

If the file exists: Parse its full contents. Treat every field as authoritative. Do not override any field with an assumption. If `state.phase` says `connection_validation`, the session executes connection validation — regardless of what the command might infer from other context.

If the file does not exist: This is session 1 of phase 1. Initialize state.json with the default schema (specified in `research-patterns-system-context.md` Section 10, SPEC-1) and set `phase` to `problem_framing`. Proceed to the clarifying question session.

**Read 3: `universal-research-system/knowledge-map.md`**

Purpose: Establish what has already been researched and written before generating any new output.

If the file exists: Read its full contents before producing any research output. The command must know what is already in the knowledge map before adding to it. Writing without reading first causes: duplication (variables researched again that are already in the map), contradiction (claims made that conflict with prior findings), and context collapse (connections described that contradict the established variable structure).

If the file does not exist: Initialize it as an empty file. Proceed.

### Why the Ordering Is Architecturally Critical

**North Star before state.json:** The North Star defines the rules for interpreting state.json. Without the North Star, the command does not know the confidence band system, the phase exit triggers, or the connection validation protocol. It would read state.json fields and apply its own interpretation rather than the system's defined interpretation.

**state.json before knowledge-map.md:** state.json tells the command which phase it is in. The phase determines which sections of knowledge-map.md are relevant, whether the command is adding to existing variable summaries or creating new connection entries, and what the output format for this session should be. Reading the knowledge map before knowing the phase means the command cannot correctly interpret what it is reading.

**Both before any execution:** The system's anti-redundancy guarantee — that no variable is researched twice, no connection is validated twice, no work is ever repeated — is only possible if the command knows the complete state before it begins. Any phase logic executed before reading state.json and knowledge-map.md has no access to the history of what has been done and will produce redundant or contradictory work.

### How the Command Enforces This

The command opens with an explicit, unconditional READ block. This block is the first section in the file. It is not nested inside a conditional. It is not optional for certain phases. It runs on every execution, including session 1.

The command opens exactly as follows:

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

After this block and only after this block, the command reads `state.phase` from the parsed state.json and executes the logic for that phase.

### The Failure Mode in Detail

If the cold-start sequence is skipped or reordered, the session will appear to work. Outputs will be generated. The user will see responses. But the system will have operated on assumed or stale state.

The failure is silent and cumulative. Each session that operates on wrong state moves further from the actual research history. By the time the error is visible — typically at synthesis, when the knowledge-map contains contradictions, missing variables, or duplicate entries — multiple sessions of research work must be discarded and repeated from the point of divergence.

There is no recovery mechanism built into this system. There is no error detection that catches mid-stream state corruption. The only protection is prevention: enforce the cold-start read sequence unconditionally at the top of every command execution.

---

This document is read-only. Do not modify it programmatically.
