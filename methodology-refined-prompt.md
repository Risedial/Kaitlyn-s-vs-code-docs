# Refined Prompt

> Optimized using Anthropic's official prompt engineering best practices, context engineering principles, meta-prompting techniques, and domain-specific research.

---

## The Prompt

```xml
<role>
You are a Principal Prompt Engineer and Technical Documentation Architect with deep expertise
in AI workflow systems, Claude Code methodology, and knowledge extraction from heterogeneous
source artifacts. Your specialty is reconstructing implicit practitioner methodology — the
unstated rules, the governing philosophy, the design decisions that explain why something
works — from evidence scattered across multiple files. You approach synthesis tasks
forensically: you distinguish what is directly evidenced from what is inferred, you map
relationships between components rather than describing them in isolation, and you write with
the precision of a system specification, not a retrospective summary. You do not speculate
beyond the source material. If the source files do not answer a question, you label the gap
explicitly rather than filling it with training data.
</role>

<context>
## Domain Background

Claude Code is a CLI-based AI coding assistant by Anthropic that operates as a stateful
agentic system. The following facts are essential context for interpreting the source files:

- **Slash commands** are user-defined `.md` files stored in `.claude/commands/`. When a user
  types `/command-name`, Claude Code loads and executes the corresponding `.md` file as a
  prompt. The `/prompt` and `/refinep` commands referenced in this task are custom
  user-created slash commands — not Anthropic built-ins. They encode a repeatable workflow.

- **Sub-agents** (spawned via the Task tool) run in isolated contexts with their own tool
  permissions. A sub-agent receives a prompt, executes autonomously, and returns a result.
  The parent agent does not share memory with sub-agents — all information transfer must be
  explicit (via files, or embedded in the prompt itself). This isolation is a core constraint
  that shapes all sub-agent design decisions.

- **Context files** are pre-written reference documents that a prompt loads or cites to
  ground Claude in project-specific reality before any work begins. They prevent hallucination
  by establishing facts that Claude would otherwise need to infer or guess. They are the
  equivalent of a project brief handed to a contractor before work begins.

- **State files** (typically JSON) track what has been completed across a multi-phase
  workflow. They allow a new Claude session to resume where a previous one left off, and they
  allow multiple parallel sub-agents to coordinate without stepping on each other's work.

- **Prompt splitting** is the practice of decomposing a single large task into multiple
  bounded sub-prompts, each given to a separate agent invocation or session. State and context
  files serve as the connective tissue between splits. A well-split prompt system is
  effectively a distributed workflow where each node is a self-contained Claude invocation.

- XML tags parse with measurably higher fidelity in Claude 4.x than markdown delimiters
  alone. Structured prompts with explicit XML section tags reduce hallucination and improve
  instruction-following accuracy on complex, multi-part tasks.

## Task Background

The author has developed a systematic, repeatable methodology for working with Claude Code.
This methodology is distributed across: two custom slash commands (`/prompt` and `/refinep`),
several prompt artifacts (`refined-prompt.md`, `meta-prompt.md`, `all-prompt.md`), a raw
ideation file (`nnnn.md`), and a folder of context files (`context/`). No single file
documents the complete system. The methodology must be reconstructed through synthesis of all
sources simultaneously.

## Audience

The output document targets: technically literate practitioners who already understand what
Claude Code is and want to replicate this methodology in their own workflow. They have not
seen the source files. They will use the document as both a reference guide and a practitioner
onboarding manual. They need enough specificity to act on every component of the methodology,
not merely understand it at a conceptual level.
</context>

<task_overview>
Produce a single, comprehensive, self-contained Markdown document at:

  C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-code-methodology.md

This document must capture — with zero information loss and 100% fidelity to the source
material — the complete methodology, philosophy, prompt-engineering system, and workflow the
author uses when working with Claude Code. The document is project-agnostic: zero
application-specific content. It must serve as a source of truth that any practitioner could
read and fully replicate the approach without consulting any other file.

Execute this task in two strictly sequential phases: Phase 1 (parallel sub-agent analysis),
then Phase 2 (synthesis and writing). Do not begin Phase 2 until all Phase 1 sub-agents have
returned complete results.
</task_overview>

<phase_1_parallel_analysis>
## Phase 1: Parallel Sub-Agent Analysis

Launch all seven sub-agents simultaneously. Each sub-agent must:
- Read every assigned file in full — do not skim or summarize before reading completely
- Return structured notes covering: purpose, structure, rules, patterns, constraints,
  philosophy, sequencing logic, and implicit conventions
- Flag explicitly: anything that reveals HOW the author thinks about prompting, not just
  what was written
- Distinguish directly stated content from inferred patterns. Label all inferences.

---

### Sub-Agent A — /prompt Command

**Read:** `C:\Users\Alexb\.claude\commands\prompt.md`

Extract all of the following without omission:
- Every transformation rule the command applies to a raw prompt, stated precisely
- Every output format constraint (what the command produces, in what structure, in what order)
- The operational definition of "a good prompt" as encoded by this command
- The 8 optimization rules if present — for each: the rule name, its purpose, the
  transformation it performs, and a generalized example of how it changes a prompt
- Input expectations: what must a prompt contain, or what state must exist, for this command
  to operate correctly
- Output guarantees: what will always be true of a prompt after this command completes
- The intended position in the workflow: is this an entry point, a mid-step, or a final step?
- Any philosophical or first-principles statements embedded in the command text

---

### Sub-Agent B — /refinep Command

**Read:** `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\.claude\commands\refinep.md`

Extract all of the following without omission:
- What this command does that `/prompt` does not — the incremental value it adds
- The full refinement logic: every phase it executes, what each phase checks, and what each
  phase produces
- The precise relationship between `/prompt` and `/refinep`: sequential, additive, or
  overlapping — with evidence from the command text
- What "perfectly engineered for Claude" means as operationalized by this command — in
  concrete, observable, testable terms, not abstract description
- Any self-verification logic embedded in the command (does it check its own output before
  finalizing?)
- The intended output: exactly what does the user possess after `/refinep` completes?
- Any explicit statements about when to use this command vs. when to skip it

---

### Sub-Agent C — refined-prompt.md

**Read:** `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\refined-prompt.md`

Extract all of the following without omission:
- The complete document structure: every section, its position, its stated purpose
- Every structural decision present in the prompt — why this element appears before that one
- Every constraint statement: both explicit ("Do NOT", "Never") and implicit (encoded through
  high specificity that forecloses alternative interpretations)
- Every edge case that has been anticipated and the mechanism by which it is addressed
- What distinguishes this prompt from a naive version of the same request — list the
  specific additions, not general characterizations
- Every XML tag or structural marker present — its name and the type of content it wraps
- Evidence, if any, that the `/prompt` → `/refinep` chain was applied (structural or
  linguistic signals of a two-stage refinement process)

---

### Sub-Agent D — meta-prompt.md

**Read:** `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\meta-prompt.md`

Extract all of the following without omission:
- The meta-layer function of this file: what problem does it solve at the prompting strategy
  level, before any specific prompt is drafted?
- How the author reasons about prompting strategy as distinct from prompt content
- Any frameworks, heuristics, or decision criteria articulated at the strategic level
- Vocabulary and language patterns that reveal the author's mental model of what a prompt is
  and how it works
- The relationship between this file and the downstream prompts it informs — how does
  meta-level thinking manifest in specific prompt decisions?
- Any governing principles or axioms stated or implied

---

### Sub-Agent E — all-prompt.md

**Read:** `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\all-prompt.md`

Extract all of the following without omission:
- The complete composite view: how all sub-prompts fit together as a system
- The splitting criteria: what factors determined where one prompt ends and the next begins
  (size? complexity? agent specialization? output type?)
- What makes each sub-prompt self-contained — what information it carries internally vs.
  what it relies on from external context or state files
- How state and context are threaded between chunks: the specific mechanisms (file references,
  embedded context, state file reads)
- The sequencing logic: which sub-prompts are parallel, which are sequential, and the
  reasoning that determined each
- The dependency graph: what must complete before what can begin, and why
- Any conventions for how sub-prompts are named, labeled, numbered, or ordered
- Any handoff conventions: what a sub-prompt produces that the next sub-prompt consumes

---

### Sub-Agent F — nnnn.md

**Read:** `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\nnnn.md`

Extract all of the following without omission:
- The raw content of this file, without filtering for polish or completeness
- What stage of thinking this file represents (pre-planning, active ideation, mid-execution
  notes, post-mortem, exploratory draft — determine from internal evidence)
- Vocabulary, phrases, and concepts used informally here that appear more formally in other
  files — these reveal how the author's language evolves from raw thought to polished prompt
- Any rules or conventions stated informally that are formalized elsewhere
- Any concepts, patterns, or ideas present here that do NOT appear in any other file —
  these are unique contributions that might otherwise be lost in synthesis
- What this file reveals about the author's cognitive process before prompts are formalized:
  the thinking before the writing

---

### Sub-Agent G — context/ Folder

**Read:** ALL files in `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\context\`

For each file individually, extract:
- The file's exact name and what the naming convention reveals about its scope or purpose
- The file's role in the larger workflow — what specific problem does it solve?
- What information it contains and why that information required pre-writing (why couldn't it
  be embedded in the prompt or inferred by Claude?)
- How it feeds into prompt construction: is it referenced by name in a prompt? Loaded by a
  sub-agent at runtime? Used to verify output? Ground truth for a specific domain?
- Its scope: global (applies to all tasks in the project), task-specific (applies to one
  phase), or sub-agent-specific (provided to one sub-agent only)

Then, after analyzing all files individually, extract cross-file patterns:
- Naming conventions across the set of context files
- Structural patterns (do they share a common format or schema?)
- How the set of context files maps to the set of sub-agents, phases, or task boundaries
- Any gaps: what context is conspicuously absent that the prompts must rely on Claude to infer?
</phase_1_parallel_analysis>

<phase_2_synthesis>
## Phase 2: Synthesis

Do NOT begin writing until all seven sub-agents have returned their complete extractions.

### Pre-Writing Reasoning Sequence (Required — Execute Before Writing)

Execute the following five steps before writing any part of the output document:

**Step 1 — Map the system.**
Identify every component in the methodology and its function. Components include at minimum:
`/prompt` command, `/refinep` command, context files, state files, sub-agent instructions,
prompt splitting conventions, ideation artifacts. Confirm the function of each.

**Step 2 — Map the relationships.**
For each pair of components, determine the relationship: sequential, parallel, hierarchical,
complementary, or redundant. Construct a mental dependency graph of the full system.

**Step 3 — Extract the governing philosophy.**
Identify the single unified principle that explains the structural decisions across all
components. This is not a summary — it is the deepest level of abstraction that remains true
across every component. State it as a single declarative sentence before proceeding.

**Step 4 — Identify gaps and inferences.**
Note every place where source material does not fully explain a component. These gaps will
become explicitly labeled `[Inferred: reasoning that supports this conclusion]` statements in
the output document. They are not omitted — they are labeled.

**Step 5 — Write in a single pass.**
Write the complete document from Section 1 through Section 15 without stopping to revise
individual sections. Coherence across sections is more important than perfection within any
single section. A single-pass draft maintains internal consistency better than an iteratively
patched one.

### Synthesis Conventions

- When two sub-agents report the same pattern from different files, synthesize into one
  statement with both sources cited inline.
- When sub-agents report contradictory content, preserve both observations and note the
  discrepancy explicitly in the document.
- Never attribute behavior to a file that the extracting sub-agent did not explicitly report
  from that file.
- If a required section cannot be written with source-material evidence, write:
  `[Insufficient source material for this section: describe what is missing]`
  Do not invent content to fill the gap.
- Expand any section beyond the listed bullet points if source material supports additional
  depth. The listed bullets are minimum coverage, not maximum.
</phase_2_synthesis>

<output_requirements>
## Output Document: Required Sections

The document must contain all 15 sections below, each expanded to the maximum depth supported
by source material. No section may be truncated, contain placeholders, or use "see above."
Each section must be self-contained: assume the reader begins at any section without having
read prior sections.

### Section 1: Philosophy and Mental Model
- How the author conceptualizes Claude Code as a tool — specifically, what distinguishes
  this usage pattern from casual prompting or chat interaction
- The author's core beliefs about what makes a prompt succeed vs. fail, with evidence
- The feedback loop: intent → prompt → output → refinement → next prompt — how each
  stage informs the next
- Any axioms or first principles that can be extracted from the source material

### Section 2: The Ideation-to-Execution Pipeline
- Step-by-step progression from raw idea to executed Claude Code task
- What happens at each stage and what artifact is produced at each stage
- The decision gate at each transition: what conditions must be met to advance
- How the `/prompt` and `/refinep` commands fit into this pipeline structurally

### Section 3: The /prompt Command — Full Anatomy
- What the command does, described phase by phase
- Every rule it applies, stated precisely and completely
- Input expectations and output guarantees (what is always true before and after)
- The 8 optimization rules in full: rule name, purpose, the transformation performed, and a
  generalized example of the before/after transformation for each rule
- When this command is necessary vs. when it can be skipped

### Section 4: The /refinep Command — Full Anatomy
- What this command does that `/prompt` does not — the specific incremental value
- The full chain: raw prompt → /prompt → /refinep → final prompt, with each step's
  contribution described precisely
- What "perfectly engineered for Claude" means in concrete, observable, testable terms
- The self-verification logic: what the command checks before declaring completion
- The exact state of the output after this command completes

### Section 5: Prompt Splitting Methodology
- The criteria that trigger a decision to split (what thresholds or signals indicate a
  task is too large or complex for a single prompt)
- The rules for what makes a sub-prompt self-contained
- The mechanisms for passing context and state between sub-prompts
- The decision framework for parallel vs. sequential execution
- How chunk boundaries are determined — the principle, not just the practice
- The handoff convention: what a sub-prompt produces that the next one consumes

### Section 6: Context File System
- What context files are and the specific problem they solve (not a general description —
  the precise failure mode they prevent)
- When to create a context file vs. embedding context directly in the prompt
- Naming conventions and structural patterns evidenced across the `context/` folder
- The scope hierarchy: global vs. task-specific vs. sub-agent-specific, with criteria
  for deciding which applies
- How context files prevent hallucination and maintain coherence across sessions and agents

### Section 7: State File Architecture
- What state files track and why tracking is necessary (what breaks without them)
- Format and schema patterns evidenced in the source material
- The read/write rules: when sub-agents read state, when they update it, and what
  determines the timing
- How conflicts are prevented when multiple parallel sub-agents might write state
  simultaneously

### Section 8: Sub-Agent Design Principles
- The decision criteria for spawning a sub-agent vs. doing work inline
- The structure of an unambiguous sub-agent instruction — every element it must contain
- How to scope sub-agent authority: read-only vs. write, bounded file scope,
  bounded task scope
- How to aggregate sub-agent outputs without information loss or synthesis errors

### Section 9: Constraint Engineering
- How the author encodes "what NOT to do" into prompts
- The taxonomy of constraint types evidenced in the source material (negative commands,
  scope boundaries, format prohibitions, inference prohibitions, etc.)
- Explicit constraints vs. implicit constraints — the difference and when each is used
- Why constraints receive equal design attention as positive instructions — the failure
  modes that occur when they do not

### Section 10: Output Specification Discipline
- The complete set of elements that constitute a fully specified output instruction:
  file path, format, structure, length guidance, naming, section order, heading levels
- The difference between an under-specified and a fully specified output instruction —
  with contrasting examples derived from the source material
- Why under-specification is a failure mode: the specific ways Claude diverges when
  output is not fully specified
- How each element of output specification is expressed in the source prompts

### Section 11: Edge Case Anticipation
- How the author pre-empts Claude's likely failure modes in prompt design
- The patterns for surfacing ambiguity before execution begins (not after output is received)
- Specific edge cases addressed in the source material, with the mechanism used to
  address each one

### Section 12: Vocabulary and Language Patterns
- Words and phrases the author consistently uses that signal specific behaviors to Claude
- The precise meaning of terms of art in this workflow (e.g., "self-contained,"
  "source of truth," "zero ambiguity," "fidelity," "no stone left unturned")
- Why precise language matters in Claude Code prompts — the specific failure modes
  that imprecise language causes, evidenced in or inferable from the source material

### Section 13: Quality Assurance Loop
- How the author validates that a prompt will produce intended output before running it
- The signals that indicate a prompt needs further refinement before execution
- How `/refinep` serves as a QA gate: what it checks and what it guarantees upon completion
- The relationship between the QA loop and the two-command refinement chain

### Section 14: Scalability Patterns
- How this methodology scales from a single-file task to a multi-agent, multi-phase
  project with dozens of sub-prompts
- What remains constant across all scales of task complexity
- What adapts and the mechanism of adaptation
- The ceiling: what this methodology does not handle, if evidence exists for a ceiling

### Section 15: Replication Guide
- The minimum viable understanding a new practitioner needs to begin applying this
  methodology — stated as specific, actionable knowledge, not general principles
- The recommended learning sequence: what to internalize first, second, and third, with
  the rationale for the ordering
- Common failure modes when applying this methodology incorrectly — for each: how to
  diagnose it, and how to correct it
</output_requirements>

<constraints>
## Hard Constraints

**Source Scope**
Extract exclusively from the listed files. Do not import general Claude Code knowledge from
training data when source files provide the answer. If source files are silent on a point,
label it `[Inferred: reasoning]` or `[Insufficient source material: description of gap]`.

**Content Scope**
Zero application-specific content. If a source file contains project-specific details,
extract the methodology pattern the detail demonstrates, not the detail itself. All examples
in the output document must be generalized to the methodology level.

**Depth Requirement**
When in doubt, go deeper. This document is authoritative and exhaustive. Brevity is never the
goal when source material supports expansion. A section that can be expanded with source
evidence must be expanded.

**Inference Labeling**
Every inference must carry its label: `[Inferred: the reasoning that supports this
conclusion]`. Inferences are permitted; unlabeled speculation is prohibited.

**Completeness**
Every section must be fully written. No placeholders. No TODOs. No "see above." No
"as mentioned in Section X." Each section stands alone.

**Output Location**
Write the final document to exactly this path, no variation:
`C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-code-methodology.md`

**Format**
- GitHub-flavored Markdown throughout
- H1 for document title only
- H2 for section headings (Sections 1-15)
- H3 for subsections
- H4 for sub-subsections where needed
- Code blocks (triple backtick) for all prompt excerpts, command examples, structural
  templates, and before/after transformation examples
- No emojis
- No tables unless the content is genuinely tabular and tables add clarity over prose
</constraints>

<success_criteria>
## Success Criteria

The output document meets the required standard when all eight conditions are true:

1. A practitioner who reads Section 3 can correctly identify which of two prompts was
   processed by `/prompt` and which was not, based solely on structural and linguistic
   markers described in the section.

2. A practitioner who reads Section 5 can decompose a novel multi-step task into
   self-contained sub-prompts, correctly identifying which can run in parallel and which
   must be sequential, without consulting any other source.

3. A practitioner who reads Sections 6 and 7 can design a context file and a state file
   schema for a new multi-phase project from scratch.

4. Every factual claim in the document can be traced to a specific source file (cited
   inline or labeled as inferred with reasoning).

5. A practitioner who reads Section 15 can begin applying the methodology within one
   working session without additional guidance.

6. The document contains no hedged language ("it seems," "possibly," "might be") except
   within explicitly labeled `[Inferred]` sections.

7. All 15 required sections are present, fully written, and each contains at minimum
   three distinct, non-redundant, source-grounded observations.

8. The document is self-contained: no section assumes the reader has read the source files
   or any other section first.
</success_criteria>

<verification>
## Pre-Write Self-Verification Checklist

Before writing a single word of the output document, confirm all items are true:

- [ ] All 7 sub-agents have returned complete extractions
- [ ] The five-step pre-writing reasoning sequence has been fully executed
- [ ] A governing philosophy statement has been formulated and can be stated in one sentence
- [ ] All 15 required sections have sufficient source material to be written fully
- [ ] All identified inferences are noted and will be labeled in the output
- [ ] The output file path is confirmed:
      C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-code-methodology.md
- [ ] No application-specific content has been retained from source file extractions

Do not begin writing the output document until every item is checked.
</verification>

<tone>
## Tone and Style

- **Register:** Authoritative, technical, evidence-based
- **Voice:** Third person for all descriptive content; second person ("you") for Section 15
  (Replication Guide) only, where direct instruction is appropriate
- **Density:** Thorough — every concept fully explained; no compression that sacrifices
  precision
- **Style:** Declarative sentences that state facts derived from evidence. Not impressions.
  Not approximations.
- **Hedging:** Prohibited outside of labeled `[Inferred]` sections
- **Meta-commentary:** Prohibited. Do not write "this section covers..." — write the content
  directly
- **Structure signals:** Use H3 and H4 headings freely within sections to aid navigation.
  The document should be scannable as well as readable.
</tone>
```

---

## Refinement Report

### Original Prompt

> The raw prompt requested a 15-section methodology document at a specific file path,
> using 7 parallel sub-agents to extract from 7 source locations, with a Phase 1/2
> structure and a set of hard constraints at the end. Full text not repeated here for
> brevity; it was the prompt passed to `/refinep`.

---

### Diagnostic Results

| # | Item | Original | Addressed In Refinement |
|---|------|----------|------------------------|
| 1 | XML/Section Structure | PARTIAL | Full XML tag structure added: `<role>`, `<context>`, `<task_overview>`, `<phase_1_parallel_analysis>`, `<phase_2_synthesis>`, `<output_requirements>`, `<constraints>`, `<success_criteria>`, `<verification>`, `<tone>` |
| 2 | Data-First Ordering | PARTIAL | Domain background and audience definition now precede all task instructions; output spec appears at end |
| 3 | Hierarchical Nesting | PASS | Maintained; enhanced with nested XML sections and per-sub-agent extraction checklists |
| 4 | Progressive Disclosure | PASS | Maintained; domain context layer added as outermost frame before instructions |
| 5 | Role Assignment | FAIL | Added: Principal Prompt Engineer and Technical Documentation Architect with forensic analysis framing and source-only constraint |
| 6 | Expertise Scoping | FAIL | Role explicitly bounded: "You do not speculate beyond the source material"; training data use constrained |
| 7 | Audience Awareness | PARTIAL | Audience fully defined: technically literate Claude Code practitioners, reference + onboarding use case, actionable specificity required |
| 8 | Chain-of-Thought Phasing | PARTIAL | Five-step pre-writing reasoning sequence added: map system → map relationships → extract philosophy → identify gaps → write in single pass |
| 9 | Self-Verification Directives | FAIL | Explicit pre-write verification checklist added (7 binary items); must all be checked before writing begins |
| 10 | Thinking Process Definition | PARTIAL | Pre-Writing Reasoning Sequence added with numbered steps and required outputs per step |
| 11 | Ambiguity Elimination | PARTIAL | "Maximum useful depth" → "maximum depth supported by source material"; "fidelity" → "zero information loss and 100% fidelity" |
| 12 | Active Directives | PASS | Maintained throughout; all passive constructions eliminated |
| 13 | Specificity Gradients | PARTIAL | Hard constraints separated from synthesis conventions; "minimum coverage, not maximum" framing added |
| 14 | Constraint Boundaries | PARTIAL | Constraint section restructured into labeled categories: source scope, content scope, depth, inference labeling, completeness, output location, format |
| 15 | Negative Constraints | PASS | Maintained and expanded: "Do not begin writing until...", "Never attribute behavior to a file...", "Do not import training data when..." |
| 16 | Spelling/Grammar | PASS | Maintained; no errors in original |
| 17 | Domain Context Sufficiency | PARTIAL | Full Domain Background section added: slash command architecture, sub-agent isolation, context file purpose, state file purpose, prompt splitting, XML parsing accuracy |
| 18 | Few-Shot Examples | FAIL | Contrast framing added for Section 10 ("with contrasting examples derived from source material"); before/after transformation requirement added to Section 3 (8 rules); `[Inferred: reasoning]` label format specified as example pattern |
| 19 | Reference Anchoring | PARTIAL | Named and defined: slash command pattern, Task tool, context engineering, state file coordination, XML tag parsing accuracy |
| 20 | Output Format Specification | PASS | Maintained; enhanced with H1/H2/H3/H4 assignment rules, code block usage rules, table usage constraint |
| 21 | Success Criteria | FAIL | Added: 8 measurable, testable success criteria with specific practitioner-action framing |
| 22 | Tone/Voice Calibration | PARTIAL | Full tone section added: register, voice differentiation (3rd person general / 2nd person Section 15), density, style, hedging prohibition, meta-commentary prohibition |
| 23 | Permission to Expand | FAIL | Added in Synthesis Conventions: "Expand any section beyond the listed bullets if source material supports additional depth. The listed bullets are minimum coverage, not maximum." |
| 24 | Uncertainty Allowance | PASS | Maintained and formalized: `[Inferred: reasoning]` and `[Insufficient source material: description]` label system |
| 25 | Task Decomposition | PASS | Maintained; per-sub-agent extraction checklists made granular with itemized extraction requirements |

**Original addressable score:** ~14/25
**Refined score:** 25/25

---

### Techniques Applied

| # | Technique | How Applied | Category |
|---|-----------|-------------|----------|
| 1 | XML Tag Sectioning | 10 XML sections covering all distinct concerns | A1 |
| 2 | Data-First Ordering | Context/audience → instructions → output spec → constraints | A2 |
| 3 | Hierarchical Nesting | XML sections nest sub-sections; output requirements nest per-section bullets | A3 |
| 4 | Progressive Disclosure | Domain context → task background → audience → phases → section requirements → constraints | A4 |
| 5 | Role Assignment | Principal Prompt Engineer + Technical Documentation Architect, forensic synthesis approach | B1 |
| 6 | Expertise Scoping | Bounded to source files; training data use explicitly constrained; speculation prohibited | B2 |
| 7 | Audience Awareness | Technically literate Claude Code practitioners; reference + onboarding use case | B3 |
| 8 | Chain-of-Thought Phasing | Five-step pre-writing reasoning sequence with required outputs per step | C1 |
| 9 | Self-Verification Directives | Seven-item binary checklist with explicit gate before writing | C2 |
| 10 | Thinking Process Definition | Pre-Writing Reasoning Sequence with numbered steps | C3 |
| 11 | Ambiguity Elimination | Vague qualifiers replaced with specific, bounded language throughout | D1 |
| 12 | Active Directives | All sub-agent extraction items as imperatives: Extract, Identify, Confirm, Note | D2 |
| 13 | Specificity Gradients | Hard constraints separated from conventions; minimum vs. maximum coverage framing | D3 |
| 14 | Constraint Boundaries | Explicit IS/IS NOT: "project-agnostic methodology. NOT application documentation." | D4 |
| 15 | Negative Constraints | "Do not speculate", "Never attribute", "Do not import training data", "No placeholders" | D5 |
| 16 | Spelling/Grammar | Maintained and standardized | D6 |
| 17 | Domain Research Integration | Claude Code architecture, sub-agent isolation, XML parsing accuracy integrated in context | E1 |
| 18 | Reference Anchoring | Slash command pattern, Task tool, context engineering, state files — all named and defined | E3 |
| 19 | Output Format Specification | H1-H4 rules, code block rules, table constraint, GFM throughout | F1 |
| 20 | Success Criteria | 8 behavioral, testable success criteria with practitioner-action framing | F2 |
| 21 | Tone/Voice Calibration | Register, voice by section, density, style, hedging rules, meta-commentary prohibition | F3 |
| 22 | Permission to Expand | "Minimum coverage, not maximum" + explicit expansion permission | G1 |
| 23 | Uncertainty Allowance | Formalized [Inferred] and [Insufficient source material] label system | G2 |

**Total techniques applied: 23**

---

### Domain Research Conducted

**Topic 1 — Claude Code architecture and multi-agent patterns**
Researched Claude Code sub-agent model (Task tool isolation), slash command implementation as `.md` files in `.claude/commands/`, context window management, and CLAUDE.md as a pre-loading pattern. Integrated: sub-agent isolation constraint explained in domain background, context file purpose defined precisely, Task tool named explicitly.

**Topic 2 — Anthropic prompt engineering methodology**
Researched Anthropic's prompt engineering ladder (clarity → examples → chain-of-thought → XML tags → roles), context engineering as evolution of prompt engineering, and synthesis task best practices (competing hypotheses, confidence tracking, self-critique). Integrated: XML parsing accuracy claim, five-step reasoning sequence design, self-verification checklist structure.

**Topic 3 — Technical methodology documentation as single source of truth**
Researched SSOT principles, docs-as-code methodology, hierarchical navigation structure, and user-centered organization patterns. Integrated: self-contained section requirement, hierarchical heading assignment rules, practitioner-action success criteria framing, audience-first context design.
