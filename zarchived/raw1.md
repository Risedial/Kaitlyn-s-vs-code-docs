## Goal

Produce a single, comprehensive, self-contained markdown document at `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-code-methodology.md` that captures — with zero ambiguity and 95–100% fidelity — the complete methodology, philosophy, prompt-engineering system, and workflow used by the author when working with Claude Code. This document is project-agnostic (no application-specific content) and must serve as a source-of-truth that any reader could use to fully understand, internalize, and replicate the approach.

---

## Phase 1 — Parallel Sub-Agent Analysis (run all simultaneously)

Launch one Explore sub-agent per source below. Each sub-agent must:
- Read every file in its assigned scope in full
- Extract and return structured notes covering: purpose, structure, rules, patterns, constraints, philosophy, variables/parameters, sequencing logic, and any implicit conventions
- Flag anything that reveals HOW the author thinks about prompting, not just what was written

### Sub-Agent Assignments

**Agent A — `/prompt` command**
Read: `C:\Users\Alexb\.claude\commands\prompt.md`
Extract: Every rule, heuristic, transformation step, output format constraint, and the underlying philosophy of what "a good prompt" means in this system.

**Agent B — `/refinep` command**
Read: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\.claude\commands\refinep.md`
Extract: The full refinement logic — what it does to a prompt, what it checks for, what it produces, how it differs from `/prompt`, and how the two commands are intended to be chained.

**Agent C — `refined-prompt.md`**
Read: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\refined-prompt.md`
Extract: The final polished prompt as a worked example. Identify every structural decision, ordering choice, constraint statement, and edge-case anticipation present. Note what was changed vs. a naive version.

**Agent D — `meta-prompt.md`**
Read: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\meta-prompt.md`
Extract: The meta-layer thinking — what this file reveals about how the author reasons about prompting strategy before writing any prompt.

**Agent E — `all-prompt.md`**
Read: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\all-prompt.md`
Extract: The full composite view. Identify: how prompts are split into sub-prompts, what makes each chunk self-contained, what state/context is threaded between chunks, and the sequencing/dependency logic.

**Agent F — `nnnn.md`**
Read: `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\nnnn.md`
Extract: Whatever this file contains — treat it as a raw ideation artifact. Extract thinking patterns, vocabulary, early-stage concepts, and any process signals.

**Agent G — `context/` folder**
Read: ALL files in `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\context\`
Extract: For each file — its role in the larger workflow, what problem it solves, how it feeds into prompt construction, and any patterns in how context files are named, scoped, or structured.

---

## Phase 2 — Synthesis

After all sub-agents return, synthesize their outputs into a single document. Do NOT write the document incrementally — fully analyze all agent outputs first, then write the complete document in one pass.

---

## Document Structure Requirements

The output document must include ALL of the following sections. Expand each to maximum useful depth. Do not truncate. Do not summarize where specifics exist.

### 1. Philosophy & Mental Model
- How the author thinks about Claude Code as a tool (not just a chat interface)
- The author's core beliefs about what makes a prompt succeed or fail
- The relationship between intent → prompt → output → refinement

### 2. The Ideation-to-Execution Pipeline
- Step-by-step: from raw idea to executed Claude Code task
- What happens at each stage (thinking, drafting, refining, splitting, executing)
- Decision criteria at each stage gate

### 3. The `/prompt` Command — Full Anatomy
- What it does, line by line if needed
- Every rule it applies and why
- Input expectations and output guarantees
- The 8 optimization rules it follows (lead with outcome, scope, constraints, sequencing, edge cases, conventions, no vagueness, output format) — explained with examples derived from the actual files
- When to use it vs. not

### 4. The `/refinep` Command — Full Anatomy
- What it does after `/prompt` has run
- How it differs from and extends `/prompt`
- The chain: raw prompt → `/prompt` → `/refinep` → final prompt
- What "perfectly engineered for Claude" means in concrete, observable terms

### 5. Prompt Splitting Methodology
- How a large task is decomposed into sub-prompts
- Rules for what makes a sub-prompt self-contained
- How state is passed between sub-prompts (state files, context files, handoff conventions)
- Parallel vs. sequential sub-prompt execution decisions
- How to determine chunk boundaries and ordering

### 6. Context File System
- What context files are, why they exist, and when to create them
- Naming conventions and structural patterns
- How context files are scoped (global vs. task-specific vs. sub-agent-specific)
- How they prevent hallucination and ensure coherence across a long multi-agent task

### 7. State File Architecture
- What state files track and why
- Format and schema patterns
- When to read vs. write state
- How sub-agents consume and update state without conflicts

### 8. Sub-Agent Design Principles
- When to use sub-agents vs. inline work
- How to write a sub-agent instruction that is unambiguous
- How to scope a sub-agent's authority (read-only vs. write, bounded scope)
- How to aggregate sub-agent outputs without loss

### 9. Constraint Engineering
- How the author encodes "what NOT to do" into prompts
- Explicit vs. implicit constraints
- Why constraints are as important as instructions

### 10. Output Specification Discipline
- How to specify exactly what Claude should produce
- File path, format, length, structure, naming — how each is specified
- The difference between "create a document" and a fully specified output instruction

### 11. Edge Case Anticipation
- How the author pre-empts Claude's likely failure modes in prompt design
- Patterns for surfacing ambiguity before execution begins

### 12. Vocabulary & Language Patterns
- Words and phrases the author consistently uses that signal specific behaviors
- Terms of art in this workflow (e.g., "self-contained," "source of truth," "no stone left unturned")
- Why precise language matters in Claude Code prompts

### 13. Quality Assurance Loop
- How the author validates that a prompt will produce what they intended before running it
- Signals that a prompt needs further refinement
- How `/refinep` serves as a QA gate

### 14. Scalability Patterns
- How this methodology scales from a single-file task to a multi-agent, multi-phase project
- What stays constant and what adapts as complexity grows

### 15. Replication Guide (Conceptual, Not Prescriptive)
- The minimum viable understanding a new user needs to apply this methodology
- The sequence of learning: what to internalize first, second, third
- Common failure modes when applying this methodology incorrectly

---

## Hard Constraints

- **Scope:** Extract only from the listed files/folder. Do not invent methodology not evidenced in the source material.
- **Application content:** Zero references to what the application does. All examples must be generalized to the methodology level.
- **Depth over brevity:** When in doubt, go deeper. This document should be exhaustive.
- **No hedging:** Do not write "it seems like" or "possibly." State what the evidence shows. If something is inferred, label it as inferred and explain the reasoning.
- **No truncation:** Every section must be fully written. Do not leave placeholders or TODOs.
- **Output location:** Write the final document to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-code-methodology.md`
- **Format:** GitHub-flavored Markdown, headers H1–H4, code blocks for any prompt excerpts or examples, no emojis.
