# Claude Code Methodology: A Practitioner's Reference

> Reconstructed from source artifacts: `/prompt` command, `/refinep` command, `refined-prompt.md`, `meta-prompt.md`, `all-prompt.md`, `nnnn.md`, and the `context/` folder. All inferences are labeled explicitly.

---

## Section 1: Philosophy and Mental Model

### Claude Code as a Deterministic Executor

The methodology treats Claude Code not as a conversational assistant but as a **deterministic executor** whose output quality is a direct function of the information architecture surrounding its inputs. This distinction is foundational: casual prompting asks Claude to infer context it does not have; this methodology pre-supplies that context in structured, retrievable form so that Claude executes with precision rather than approximating from uncertainty.

The author encodes this belief in the `/prompt` command's core directive: `"return a single, perfectly engineered prompt that Claude Code can execute with precision, no ambiguity, and no errors."` Precision is stated as a property of the prompt artifact, not a property of Claude's inference capabilities. The practical consequence of this belief is that the methodology invests as much engineering effort in context files, state schemas, and command chains as in the task instructions themselves.

### What Distinguishes This Usage from Casual Prompting

Three operational differences separate this methodology from ad-hoc Claude Code interaction:

**1. Prompts are engineering artifacts, not natural language requests.**
The `/refinep` command treats every incoming prompt as a software artifact requiring diagnostic analysis, systematic transformation, and verification before deployment. The 6-phase refinement pipeline — diagnostic analysis against 25 criteria, mandatory domain research, technique application from a 25-technique library, self-verification — is the equivalent of a code review and build pipeline applied to prompt text.

**2. Context is pre-written and externalized, not embedded in conversation.**
The author maintains a `context/` folder containing pre-written domain reference documents that sub-agents load before executing tasks. These files exist because Claude cannot reliably reconstruct domain-specific knowledge from a prompt alone. Each context file solves a specific failure mode: the design token file (`design-tokens.css`) prevents color inconsistency; the data inventory (`data-inventory.md`) prevents partial or hallucinated data; the architecture file (`app-architecture.md`) prevents navigation model divergence across implementations.

**3. State is externalized to JSON files, not carried in conversation history.**
Multi-phase work executes across isolated, fresh Claude sessions. Each session reads a `state.json` file at start and writes back to it at end. The `meta-prompt.md` articulates the reason: "fresh chats with a cleared contacts window" eliminate accumulated context noise. The state file is the only thread connecting sessions; conversation memory is explicitly excluded from the architecture.

### Core Beliefs About What Makes a Prompt Succeed or Fail

From the source material, the following beliefs govern all prompt design decisions:

**Precision eliminates ambiguity as a precondition to execution.** The `/prompt` command instructs Claude to analyze both "explicit intent (what they literally asked) and implicit intent (what they actually need to accomplish)." The existence of this two-layer intent analysis signals the author's belief that user inputs routinely express surface-level requests that obscure actual needs.

**Vague language is information destruction.** Rule 7 of the `/prompt` command specifically targets replacement of words like "improve," "fix," and "update" with specific, observable actions. [Inferred: The author treats generic verbs as compression artifacts — they lose the specificity needed for correct execution. Restoring that specificity is not stylistic preference but epistemological necessity.]

**Scope absence is implicit permission for overreach.** Rule 2 of the `/prompt` command requires explicit scope specification. [Inferred: The author treats undefined scope as equivalent to granting the executing agent freedom to operate on any file, directory, or system — a failure mode the author considers worse than scope over-restriction.]

**Context must precede instructions.** The `/refinep` command's Technique A2 (Data-First Ordering) places context and background before instructions, citing "up to 30% improvement in Claude's comprehension on complex inputs" (per Anthropic testing, as cited in the command). The ordering principle is: context → instructions → deliverable specification. Reversing this order degrades output fidelity.

**Negative constraints carry equal weight as positive instructions.** The `/refinep` command dedicates Technique D5 (Negative Constraints) to "Do NOT / Avoid / Never" directives, treating them as a category distinct from positive requirements. The `refined-prompt.md` names the most important negative constraint explicitly as "the cardinal failure mode" — a specific error pattern elevated to prominence because it was identified as the highest-risk failure.

### The Feedback Loop

The methodology's iterative cycle:

```
Raw idea
  → Ideation draft (nnnn.md equivalent: decisions locked, UX/architecture choices made)
  → Initial prompt formulation
  → /prompt command application (8-rule optimization, single output)
  → /refinep command application (6-phase systematic refinement → refined-prompt.md)
  → Orchestration decomposition (meta-prompt strategy: split into 30–45 micro-prompts)
  → Context file preparation (pre-written domain references for each sub-agent)
  → State file initialization (state.json with full pendingSteps array)
  → Sequential execution across isolated sessions (each session reads/writes state)
  → Verification at each step (Verification section + state update protocol)
  → Completion confirmed by state.json (completedSteps = all pendingSteps)
```

Each stage produces an artifact that the next stage consumes. Nothing is carried implicitly — all handoffs are explicit, written, and verifiable.

### Axioms

Three first principles are extractable from the source material:

1. **Complexity requires decomposition.** From `meta-prompt.md`: "The reason behind splitting up this prompt into many microprompts and having sub agents is because this is a large and complex mobile application." Complexity is the direct trigger for decomposition — not preference or style.

2. **Token limits are architectural constraints, not soft targets.** From `meta-prompt.md` and `refined-prompt.md`: the 32,000-token output limit "is a hard constraint that never breaks." This constraint governs all decisions about granularity, splitting, and sub-agent scope.

3. **Sequential isolation improves accuracy.** The explicit use of "fresh chats with a cleared contacts window" for sequential prompt execution encodes the belief that prior conversation context can be noise. Each execution unit is designed to operate without access to other executions' context; all necessary context is loaded explicitly from files.

---

## Section 2: The Ideation-to-Execution Pipeline

The methodology defines a progression from raw idea to executed Claude Code task with distinct artifacts at each stage. Each transition has a condition that must be met before advancing.

### Stage 1: Ideation and Specification Lock

**Artifact produced:** An informal specification document (equivalent to `nnnn.md`).

**What happens:** The author works through the full scope of the task without concern for prompt structure or Claude Code conventions. All major decisions are made: architecture choices, data structures, UX flows, constraints, design values. The language at this stage is informal — domain shorthand, mechanism names, working vocabulary — but the decisions are complete.

**Evidence from source material:** The `nnnn.md` file contains no hedging language, no design questions, no "should we" or "consider" markers. The specification is complete, with exact color codes, pixel values, and data counts. Sub-Agent F determined this represents "pre-execution specification at the threshold of implementation."

**Transition condition:** All design decisions are locked. The specification is complete enough to hand to a developer who could implement it without asking clarifying questions.

**What this stage is NOT:** It is not exploratory or iterative. It is the output of prior thinking, not the process of thinking. This stage begins after the author has already resolved the question of what to build.

### Stage 2: Initial Prompt Formulation

**Artifact produced:** A raw prompt — the initial statement of what Claude Code should do.

**What happens:** The specification from Stage 1 is translated into a prompt. This translation is imperfect — it may contain vague verbs, implicit scope assumptions, missing constraints, or no explicit output specification.

**Transition condition:** A prompt exists that expresses the task. Quality at this stage is deliberately not required; that is the function of the next stages.

### Stage 3: /prompt Command Application

**Artifact produced:** A single optimized prompt in a markdown code block.

**What happens:** The user invokes `/prompt [raw prompt]`. The command applies 8 transformation rules, analyzes explicit and implicit intent, and returns a single code block containing the optimized prompt. No commentary, no explanation — only the transformed prompt.

**Transition condition:** The optimized prompt is precise, scoped, constrained, sequenced, and has a declared output format. It can be executed by Claude Code with minimal ambiguity.

**Decision gate:** This stage is appropriate for prompts that need quick optimization. For production-grade work, Stage 4 (/refinep) follows immediately.

### Stage 4: /refinep Command Application

**Artifact produced:** `refined-prompt.md` — a fully engineered prompt plus a Refinement Report.

**What happens:** The user invokes `/refinep [prompt or file path]`. The command executes a 6-phase pipeline: input capture → diagnostic analysis against 25 criteria → mandatory domain research → 25-technique transformation → 15-item self-verification → structured file output. The output is written to `refined-prompt.md` in the workspace root.

**Transition condition:** The refined-prompt.md prompt passes all 15 items of the Phase 5 self-verification checklist. The prompt is self-contained, unambiguous, domain-grounded, and has explicit success criteria.

**Relationship between Stages 3 and 4:** [Inferred from the complementary designs of both commands: `/prompt` is a first-pass optimizer suitable for simpler tasks; `/refinep` applies the full systematic treatment for complex or multi-phase tasks. The two commands are designed to be used in sequence — `/prompt` for initial transformation, `/refinep` for production-grade refinement — though each can be used independently.]

### Stage 5: Orchestration Decomposition

**Artifact produced:** Micro-prompt files in an orchestration directory (e.g., `connect-da-dots/`), a `state.json` state file, and a `README.md` index.

**What happens:** When the refined prompt describes a large, complex task, the author applies the strategy defined in `meta-prompt.md`: decompose the task into 30–45 atomic micro-prompts, initialize a `state.json` file with all step IDs pre-populated in `pendingSteps`, and write a `README.md` index of all prompts with their execution order, prerequisites, and estimated token output.

**Splitting criteria:** Each micro-prompt must do exactly one verifiable unit of work. The 32K token output limit governs the maximum size of any single prompt's output. No task that risks exceeding this limit is permitted in a single prompt.

**Transition condition:** All step IDs are pre-populated in `pendingSteps` (the list must not be empty). Every prompt follows the canonical schema. No prompt references a prerequisite created by a later step.

### Stage 6: Context File Preparation

**Artifact produced:** Pre-written domain reference files stored in a `context/` directory.

**What happens:** Before sequential execution begins, the author writes all context files that sub-agents will need. These files encode domain knowledge, design specifications, data inventories, and technical references that cannot be reliably inferred from prompts alone.

**Transition condition:** Every piece of domain knowledge that a sub-agent would otherwise need to infer, guess, or hallucinate has been pre-written and is accessible as a named file.

### Stage 7: Sequential Execution

**What happens:** Each micro-prompt executes in a fresh Claude Code session. Each session begins by reading `state.json`, executes exactly one atomic task, runs its Verification section, updates `state.json` (completing the current step), and exits.

**Transition condition for each step:** The Verification section's measurable checks pass. The state update completes successfully.

### Stage 8: Completion Verification

**What happens:** When `pendingSteps` is empty and `completedSteps` contains all step IDs, the build is complete. The final chat report enumerates all created artifacts and confirms data integrity counts.

---

## Section 3: The /prompt Command — Full Anatomy

### What the Command Does

The `/prompt` command takes a raw, unoptimized prompt as input and returns a single, perfectly engineered prompt as output. The output is wrapped in a markdown code block with no surrounding commentary. The command analyzes both explicit intent (what the user literally asked) and implicit intent (what the user actually needs to accomplish), then applies 8 transformation rules to produce a prompt that Claude Code can execute with precision.

### Input Expectations

- A raw prompt text passed via the `$ARGUMENTS` placeholder
- The prompt can be at any quality level — vague, partially formed, or mostly complete
- The prompt must contain at least implicit intent (Claude Code must be able to determine the goal)
- No prior state or context files are required; this command is stateless

### Output Guarantees

After the `/prompt` command completes, the following are always true of the output:

- The output is a **single markdown code block** containing only the optimized prompt
- **No text appears outside the code block** — no explanations, no commentary
- The prompt has been analyzed for both explicit and implicit intent
- All 8 transformation rules have been considered and applied where relevant
- The optimized prompt is immediately executable by Claude Code without a clarification loop

### The 8 Optimization Rules

#### Rule 1: Lead with the Outcome

**Purpose:** State what should exist or be true after the task is done — not the intermediate steps.

**Transformation:** Reorder the prompt to front-load the desired end state. Replace process descriptions with state descriptions.

**Before/after example:**
```
BEFORE: "Run the tests on the application and check coverage."
AFTER:  "All tests pass and a coverage report exists at /reports/coverage.html
         showing ≥85% coverage across all modules in /src."
```

[Inferred: This rule encodes the author's belief that declarative outcomes are more reliable targets for Claude Code than imperative procedures. Stating what should be true after execution is less ambiguous than describing the path to that state.]

#### Rule 2: Specify Scope

**Purpose:** Clarify which files, directories, or systems are explicitly in or out of scope.

**Transformation:** Enumerate scope boundaries as explicit statements. Do not allow scope to be inferred.

**Before/after example:**
```
BEFORE: "Fix the authentication code."
AFTER:  "Fix bugs only in /src/auth/. Do not modify /tests/, /docs/, or any
         file outside /src/auth/."
```

#### Rule 3: Name Constraints Explicitly

**Purpose:** Declare language, framework, style conventions, and what NOT to do.

**Transformation:** Add all constraints as declarative statements — both positive (must use X) and negative (must not use Y).

**Before/after example:**
```
BEFORE: "Write it properly using our standard stack."
AFTER:  "Use Python 3.11+, follow PEP 8, do not use pandas, must be
         compatible with async/await, no global state."
```

#### Rule 4: Break Compound Tasks into Ordered Steps

**Purpose:** If multiple things need to happen, sequence them with clear ordering.

**Transformation:** Decompose into numbered or explicitly sequenced substeps. Each step is one unit of work.

**Before/after example:**
```
BEFORE: "Build and deploy the container."
AFTER:  "1) Build Docker image from /Dockerfile
         2) Run test suite; abort if any test fails
         3) Push image to registry with tag matching current git SHA
         4) Deploy to staging environment
         5) Verify all health check endpoints return 200"
```

#### Rule 5: Anticipate Edge Cases

**Purpose:** Mention likely failure modes or decisions Claude Code will need to make during execution.

**Transformation:** Explicitly state what happens when specific conditions occur. Name the conditions, not just the general category.

**Before/after example:**
```
BEFORE: "Handle errors gracefully."
AFTER:  "If the config file is missing, create it from the template at
         /templates/config.default.json. If the API timeout exceeds 5s,
         retry 3 times with exponential backoff, then log the error to
         /logs/api-errors.log and exit with code 1."
```

#### Rule 6: Use Claude Code Conventions

**Purpose:** Reference file paths, function names, and line numbers where relevant to the Claude Code environment.

**Transformation:** Replace generic references with concrete, addressable identifiers that Claude Code can locate and act on.

**Before/after example:**
```
BEFORE: "Fix the email validation function."
AFTER:  "Fix the validateEmail() function in /src/utils/validation.ts
         (lines 42–67) to accept plus-sign subaddresses (e.g., user+tag@domain.com)."
```

#### Rule 7: Avoid Vagueness

**Purpose:** Replace words like "improve," "fix," "update," "enhance," and "clean up" with specific, observable actions.

**Transformation:** Substitute generic verbs with precise, measurable actions whose completion can be objectively verified.

**Before/after example:**
```
BEFORE: "Improve the performance of the search endpoint."
AFTER:  "Reduce the /api/search endpoint response time from the current average
         of 2.1s to under 500ms by adding Redis caching for query results with
         a 5-minute TTL."
```

#### Rule 8: State the Output Format

**Purpose:** If a file should be created, edited, or returned, declare it explicitly with format and location.

**Transformation:** Add a declaration of the expected output artifact — its type, location, structure, and any format constraints.

**Before/after example:**
```
BEFORE: "Generate a report on the test results."
AFTER:  "Generate a JSON report at /reports/test-results.json with the
         structure: { status: 'pass'|'fail', timestamp: ISO string,
         results: [{ test: string, passed: boolean, duration_ms: number }],
         errors: [string] }"
```

### Intended Position in Workflow

The `/prompt` command is the **entry point** of the prompt engineering workflow. It is designed to take raw user input and produce an immediately actionable prompt. [Inferred: For complex, multi-phase work, the output of `/prompt` serves as the input to `/refinep` rather than being executed directly. For simpler tasks, the `/prompt` output may be used directly.]

### Philosophical Signal in the Command

The requirement to analyze "implicit intent (what they actually need to accomplish)" reveals that the author assumes users do not always ask for what they need. The command's job is to bridge the gap between the user's expressed request and their actual objective — a diagnostic step built into the transformation itself.

---

## Section 4: The /refinep Command — Full Anatomy

### What This Command Does That /prompt Does Not

The `/refinep` command is a **systematic refinement pipeline**, not a simple transformation. Where `/prompt` applies 8 rules to optimize a raw prompt, `/refinep` performs:

- **Diagnostic validation** against 25 structural, clarity, reasoning, and output-control dimensions before any transformation
- **Mandatory domain research** regardless of whether the user asked for it, enriching the prompt with domain-specific best practices, terminology, and anti-patterns the user may not have included
- **Systematic technique application** from a curated 25-technique Master Technique Library, applied in precise category order
- **Self-verification enforcement** against 15 concrete checklist items before the output is finalized
- **Structured output** that includes not just the refined prompt but a complete Refinement Report documenting what was diagnosed, what changed, and why

The `/prompt` command produces a better prompt; the `/refinep` command produces a production-grade prompt with full transparency into its construction.

### Phase 1: Input Capture

The command checks whether `$ARGUMENTS` is empty. If a prompt is provided, it is assigned to `RAW_PROMPT` and Phase 2 begins. If `$ARGUMENTS` is empty, the command triggers an `AskUserQuestion` workflow offering two options: the user types the prompt directly, or provides a file path (which the system reads). The phase completes when `RAW_PROMPT` is established.

### Phase 2: Diagnostic Analysis

`RAW_PROMPT` is evaluated against 25 diagnostic items across 7 categories. Each item is scored as Adequate, Partial, or Not at all. Every item scored as Partial or Not at all is flagged for correction in Phase 4.

**The 25 diagnostic items by category:**

**Structural Quality (4 items):**
- XML/Section Structure — are distinct concerns separated into labeled sections?
- Data-First Ordering — does context appear before instructions?
- Hierarchical Nesting — are related sub-topics logically grouped?
- Progressive Disclosure — does information layer from general to specific?

**Role & Identity (3 items):**
- Role Assignment — is Claude assigned a specific expert persona?
- Expertise Scoping — is the role's knowledge domain bounded to prevent hallucination?
- Audience Awareness — is the intended reader defined by technical level, role, and use case?

**Reasoning & Thinking (3 items):**
- Chain-of-Thought Phasing — are sequential reasoning phases defined?
- Self-Verification Directives — is Claude instructed to check its own output?
- Thinking Process Definition — is HOW to reason specified, not just WHAT to produce?

**Clarity & Precision (6 items):**
- Ambiguity Elimination — are all vague terms replaced with specific, measurable language?
- Active Directives — are all passive/wishful constructions replaced with direct commands?
- Specificity Gradients — are requirements organized by MUST / SHOULD / MAY?
- Constraint Boundaries — are IS and IS NOT statements present?
- Negative Constraints — are Do NOT / Avoid / Never directives present?
- Spelling/Grammar — is terminology correct and consistent?

**Context & Research (3 items):**
- Domain Context Sufficiency — is domain-specific knowledge present?
- Few-Shot Examples — are 1–3 concrete examples provided for format/quality demonstration?
- Reference Anchoring — are frameworks and methodologies named explicitly?

**Output Control (3 items):**
- Output Format Specification — is the exact structure of the expected output defined?
- Success Criteria — are 5–10 measurable completion conditions stated?
- Tone/Voice Calibration — is register, perspective, and density specified?

**Meta-Techniques (3 items):**
- Permission to Expand — is Claude given latitude to add value beyond stated scope?
- Uncertainty Allowance — is Claude permitted to flag gaps rather than invent answers?
- Task Decomposition — are complex tasks broken into named sub-tasks with clear handoffs?

### Phase 3: Domain Research

**This phase is mandatory regardless of whether the user asked for research.** The command identifies the primary domain of `RAW_PROMPT`, then executes 2–3 targeted web searches:
1. Domain best practices and current standards (with the current year in the query)
2. Framework/methodology deep-dive if specific tools are referenced
3. Common pitfalls and anti-patterns

Research findings are synthesized and extracted as: terminology, frameworks, constraints, best practices, and anti-patterns. **Research results are not displayed to the user.** They are integrated directly into the prompt during Phase 4. This phase produces a research-enriched foundation that Phase 4 draws from.

### Phase 4: Technique Application

The command applies all applicable techniques from the Master Technique Library in category order (A → B → C → D → E → F → G). Not every technique is appropriate for every prompt — a simple prompt may use 3–4 sections; a complex prompt may use 8+. The command exercises judgment about which techniques add value.

**Category A — Structural Techniques:**
- **A1: XML Tag Sectioning** — Organizes content into labeled XML sections using canonical tags: `<role>`, `<context>`, `<research_directives>`, `<requirements>`, `<constraints>`, `<thinking_process>`, `<output_format>`, `<success_criteria>`, `<examples>`, `<tone>`
- **A2: Data-First Ordering** — Moves context/background to position 1, instructions to position 2, deliverable specification to position 3
- **A3: Hierarchical Nesting** — Wraps related items in parent tags (e.g., `<core_features>`, `<optional_features>`, `<excluded_features>` within `<requirements>`)
- **A4: Progressive Disclosure** — Layers: high-level goal → key context and constraints → detailed specifications → edge cases

**Category B — Role & Identity:**
- **B1: Role Assignment** — Template: "You are a [ROLE TITLE] specializing in [DOMAIN 1] and [DOMAIN 2]. You combine [SKILL 1] with [SKILL 2] and approach problems through [METHODOLOGY]. Your goal is to [PRIMARY OBJECTIVE]."
- **B2: Expertise Scoping** — Adds: "You are an expert in X, Y, Z. If asked about topics outside [DOMAIN], acknowledge the boundary rather than speculating."
- **B3: Audience Awareness** — Defines intended reader's technical level, role, and use case

**Category C — Reasoning & Thinking:**
- **C1: Chain-of-Thought Phasing** — Common patterns: Research → Analyze → Synthesize → Articulate; Understand → Plan → Execute → Verify
- **C2: Self-Verification Directives** — Adds: "Before finalizing, verify that every [REQUIREMENT] is addressed. Cross-check your output against the success criteria. If you find gaps, revise before presenting the final output."
- **C3: Thinking Process Definition** — Adds: "Consider multiple approaches before committing to one. Weigh trade-offs explicitly when making design decisions. If information is insufficient, flag it rather than assuming."

**Category D — Clarity & Precision:**
- **D1: Ambiguity Elimination** — Converts: "good" → "meets these criteria: [list]"; "fast" → "responds within X seconds"; "user-friendly" → "requires no technical knowledge; all actions achievable in ≤3 clicks"
- **D2: Active Directives** — Converts: "It would be great if..." → "Include [X]."; "Something like..." → "Specifically, [X] with [Y] characteristics."
- **D3: Specificity Gradients** — Labels requirements as: MUST (non-negotiable) / SHOULD (strong preference) / MAY (optional enhancement)
- **D4: Constraint Boundaries** — Adds: "This IS a [vision document / technical spec / analysis]. This is NOT a [implementation plan / tutorial / sales pitch]."
- **D5: Negative Constraints** — Adds: "Do NOT [common mistake].", "Avoid [anti-pattern from research].", "Never [failure mode that would invalidate the output]."
- **D6: Spelling/Grammar Correction** — Applies correct domain terminology discovered during Phase 3

**Category E — Context & Research:**
- **E1: Domain Research Integration** — Weaves Phase 3 research as specific directives, named frameworks, and correct terminology
- **E2: Few-Shot Examples** — Adds 1–3 examples in `<examples>` tags covering simple case, complex case, and edge case
- **E3: Reference Anchoring** — Converts vague framework references to explicit citations with application instructions

**Category F — Output Control:**
- **F1: Output Format Specification** — Declares: section headings and order, content expectations per section, length guidance, format preferences (prose vs. bullets vs. tables)
- **F2: Success Criteria** — Defines 5–10 testable assertions formatted as: "A [TARGET_READER] reading this should be able to [SPECIFIC_ACTION]"
- **F3: Tone/Voice Calibration** — Specifies register (formal / conversational / technical / persuasive), perspective (first / third / imperative), density (concise / thorough / exhaustive)

**Category G — Meta-Techniques:**
- **G1: Permission to Expand** — Adds: "Identify elements I haven't mentioned but that logically belong in this [OUTPUT_TYPE]. If you discover important considerations during research, include them."
- **G2: Uncertainty Allowance** — Adds: "If information is insufficient to make a definitive recommendation, note the uncertainty and provide conditional guidance. Mark assumptions explicitly so they can be validated."
- **G3: Task Decomposition** — Structures as: "First, [SUB_TASK_1] and produce [INTERMEDIATE_OUTPUT_1]. Using [INTERMEDIATE_OUTPUT_1], then [SUB_TASK_2]. Finally, synthesize into [FINAL_DELIVERABLE]."

### Phase 5: Self-Verification

Before the refined prompt is finalized, the command validates it against a 15-item checklist:

```
[ ] Clear <role> with bounded expertise
[ ] XML tags separate distinct concerns
[ ] Context/background appears before instructions (data-first ordering)
[ ] Deliverable specification at end
[ ] All ambiguous phrases replaced with specific language
[ ] All passive/wishful language converted to active directives
[ ] Domain research findings woven naturally
[ ] Explicit success criteria (minimum 5 conditions)
[ ] Defined output format with named sections
[ ] Chain-of-thought phases defined (if multi-step)
[ ] Constraint boundaries clearly state IS and IS NOT
[ ] Negative constraints address common failure modes
[ ] Prompt is self-contained — Claude can execute without additional context
[ ] Spelling, grammar, terminology correct throughout
[ ] Minimum structure needed — no unnecessary complexity
```

**Decision gate:** If any box is unchecked, the prompt is revised and verification re-runs before Phase 6.

### Phase 6: Output

The command writes `refined-prompt.md` to the workspace root. The file contains:

```
# Refined Prompt

> Optimized using Anthropic's official prompt engineering best practices,
> context engineering principles, meta-prompting techniques, and domain-specific research.

## The Prompt
[Full refined prompt — copy-paste ready, immediately executable]

## Refinement Report

### Original Prompt
[RAW_PROMPT quoted in full]

### Diagnostic Results
[Table: Item | Original Status | How Addressed in Refined Version]

### Techniques Applied
[Table: # | Technique | How Applied | Category]

### Domain Research Conducted
[Summary of topics researched and key findings integrated]
```

After writing the file, the command displays a summary in chat: file location, diagnostic improvement count (X/25 items addressed), techniques applied count, domain research summary. The command then stops and outputs nothing further.

### What "Perfectly Engineered for Claude" Means — Operationalized

A "perfectly engineered" prompt, as defined by this command's Phase 5 verification, satisfies all of the following **observable, testable conditions**:

1. It is divided into XML-tagged sections with canonical tag names
2. Context appears before instructions; deliverable specification is last
3. Claude is assigned a named expert role with bounded knowledge domain
4. All reasoning is guided through sequential phases with named goals
5. Every vague term has been replaced with a measurable specific
6. MUST / SHOULD / MAY gradients are applied to requirements
7. IS / IS NOT constraint boundaries are present
8. Do NOT directives address the specific failure modes of this domain
9. Output structure is fully declared: section headings, order, format, length
10. 5+ measurable success criteria are stated as testable assertions
11. The prompt is self-contained — another Claude instance could execute it without additional context

---

## Section 5: Prompt Splitting Methodology

### The Trigger for Splitting

The decision to split a prompt into multiple atomic prompts is triggered by two conditions, either of which is sufficient:

1. **The task risks producing more than 32,000 tokens in a single response.** This is named a "hard constraint that never breaks" — not a guideline or soft limit. Any task that approaches this threshold must be split.

2. **The task involves multiple discrete verifiable units of work.** A "unit of work" is anything that could be completed and verified independently. If a task has N verifiable units, it should produce N prompts.

From the source material, a target range of 30–45 prompts represents a medium-to-large project. [Inferred: Smaller projects may require fewer prompts; the range establishes that the author prefers over-splitting to under-splitting. The instruction to "be obsessive" about decomposition (from `meta-prompt.md`) confirms this bias.]

### The Atomicity Principle

An atomic prompt does exactly **one verifiable unit of work.** Examples of atomic units:

- One CSS section (e.g., `:root {}` design tokens only)
- One JavaScript function or module
- One batch of 15–20 data entries
- One standalone file (e.g., `manifest.json` only)
- One initialization step (e.g., creating the state file)
- One verification pass

Combining two atomic units into a single prompt is explicitly named "the cardinal failure mode." The naming of this failure mode as "cardinal" — rather than as one of several concerns — indicates the author considers it the single highest-risk error in the splitting process.

### What Makes a Sub-Prompt Self-Contained

Each sub-prompt must carry sufficient information that **a fresh Claude Code session with no prior conversation context can execute it correctly without ambiguity.** This self-containment requirement is operationalized through four required sections in the prompt schema:

```markdown
## Prerequisites
[List all flags in state.json that must be true and all files that must
exist before this prompt can execute. If none, state "none" explicitly.]

## Hard Constraints
[The five hard constraints, verbatim, repeated in every prompt:
1. 32,000 token output limit
2. No truncation
3. State sync required
4. No external dependencies
5. Write tool only]

## Task
[A single, unambiguous instruction — one action, stated precisely,
with no compound verbs, no implicit scope, no undefined references.]

## Verification
[Measurable checks that must pass before state.json is updated.]

## State Update
[Exact state.json mutations to perform: completedSteps append,
pendingSteps remove, flags set, artifact counts increment.]
```

### The Five Hard Constraints

Every sub-prompt includes these five constraints verbatim, without paraphrasing, in the Hard Constraints section:

1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

The verbatim inclusion requirement prevents paraphrasing that might soften constraints. [Inferred: The author discovered through prior experience that paraphrased constraints were interpreted as suggestions rather than absolute rules.]

### Sequencing Logic: Parallel vs. Sequential

**Sequential execution** is the default and the rule. Sub-prompts execute one at a time, in fresh sessions, with state.json read at the start of each. Sequential execution prevents context contamination and ensures each step's outputs are available as prerequisites for subsequent steps.

**Parallel execution** is a conditional option for sub-agents spawned within a single prompt execution: "each of the microprompts [can] spin off sub agents to get things done faster if it is going to contribute to better results accurate results" (from `meta-prompt.md`). The README's Sub-Agent Strategy column (SOLO or PARALLEL) designates which prompts may use parallel sub-agents.

**Dependency graph rules:**
- A prompt may only reference prerequisites created by steps that precede it in execution order
- Forward references (depending on a file created by a later step) are forbidden
- The README table encodes the execution order and all prerequisite relationships

### State and Context Threading Between Prompts

Information passes between sub-prompts through three mechanisms:

1. **state.json** — tracks which steps are complete, stores artifact counts and data chunk references, exposes boolean flags that prompts can check as prerequisites
2. **Written files** — files created by one prompt are referenced by name in subsequent prompts' Prerequisites sections
3. **Embedded context in each prompt** — all necessary knowledge is contained within the prompt file itself; no reliance on conversation memory

### File Naming Conventions

```
prompt-01.md
prompt-02.md
...
prompt-NN.md
```

Zero-padded two-digit numbers enforce alphabetical sort order. Prompt titles follow the pattern: `# Prompt [NN]: [Action Title in imperative form]`.

Data batch prompts use category names rather than batch numbers:
```
# Prompt 12: Write Symptom Data: Energy & Fatigue Category
```
not
```
# Prompt 12: Write Symptom Data Batch 3
```

The category-name convention makes prompts self-documenting and eliminates the need to cross-reference a batch-to-category mapping.

---

## Section 6: Context File System

### What Context Files Are and the Problem They Solve

Context files are pre-written domain reference documents that sub-agents load before executing their assigned tasks. The specific failure mode they prevent is **hallucination and inconsistency that results from asking Claude to infer domain knowledge it cannot reliably reconstruct from a prompt alone.**

Examples of knowledge that requires pre-writing:
- Exact color hex codes that encode identity (changing them breaks visual consistency)
- Navigation state machine definitions (the semantics of state fields cannot be inferred)
- Complete data inventories with canonical IDs (Claude would generate plausible-but-incorrect entries)
- CSS architecture ordering requirements (the exact order of 11 CSS sections cannot be guessed)
- Clinical or domain-specific rules with exact wording (paraphrase is clinically or technically incorrect)

Without context files, each prompt must either embed this knowledge inline (making prompts massive) or rely on Claude to infer it (introducing errors). Context files solve the third option: pre-write once, reference repeatedly.

### When to Create a Context File vs. Embedding in the Prompt

[Inferred from the structure of the context/ folder and the content of the prompts that reference it: a context file is warranted when the knowledge it encodes is (a) too large to embed repeatedly in each prompt, (b) immutable during the implementation phase, (c) referenced by multiple prompts or sub-agents, or (d) domain-specific enough that Claude would need to research or infer it. Knowledge that is task-specific and not reused belongs in the prompt itself.]

### Naming Conventions

The context/ folder follows a consistent naming convention: `[domain-prefix]-[descriptor].[type]`

**Domain prefixes observed:**
- `app-` — application-level structural specifications
- `build-` — assembly and construction blueprints
- `data-` — data inventories and enumeration catalogs
- `ui-` — user interface specifications and component libraries
- `pwa-` — progressive web app infrastructure references

**Descriptor types observed:**
- `-architecture` — structural and navigation specifications
- `-manifest` — assembly checklists with ordered build instructions
- `-inventory` — complete enumerations with canonical identifiers
- `-design-system` — component specifications with DOM and CSS
- `-technical` — implementation references with code patterns
- `.css` — raw CSS custom property files ready for copy-paste inclusion

This convention allows files to be sorted and understood at a glance without opening them. A file named `data-inventory.md` is unambiguously a complete data enumeration catalog; a file named `design-tokens.css` is a CSS custom property file intended for direct inclusion.

### Structural Patterns

Across the six context files observed in the source material, shared structural patterns include:

**Copy-paste-ready code blocks.** CSS files and code-heavy markdown files contain blocks intended for direct extraction into implementation files. The design token file is a single `:root {}` block; the architecture file contains JavaScript pseudocode; the build manifest contains HTML, CSS, and JS examples.

**Immutability designation.** All context files are designated immutable during the implementation phase. Changes to any context file require re-evaluation of all components that depend on it.

**Redundancy as insurance for isolated access.** Critical information (e.g., the 14-category order) is repeated across multiple context files. [Inferred: This redundancy is intentional — if a sub-agent loads only one context file, it still has the critical ordering information it needs.]

**Feed-forward dependency graph.** The context files form a directed dependency graph with no cycles:
```
data-inventory.md + design-tokens.css
  → app-architecture.md + ui-design-system.md
    → pwa-technical.md + build-manifest.md
      → implementation
```
Data files are upstream; architecture files consume data and define structure; infrastructure and build files coordinate implementation.

### Scope Hierarchy

**Global scope** (applies to every task in the project): All six context files observed are global in scope. They define the data layer, design language, navigation model, component library, PWA infrastructure, and build order — all of which apply to the complete implementation.

**Task-specific scope** (applies to one phase only): [Inferred: Context files intended for a specific build phase would be scoped accordingly. The source material does not provide examples of task-specific context files, suggesting the author's current practice creates global-scope files exclusively.]

**Sub-agent-specific scope:** [Insufficient source material: no sub-agent-specific context files were observed. Whether the methodology supports this scope level is not evidenced in the source files.]

### What Context Files Prevent

Specific failure modes that each observed file type prevents:

| File Type | Failure Mode Prevented |
|-----------|----------------------|
| Data inventory | Missing entries, incorrect IDs, partial data sets |
| Design tokens | Color inconsistency, incorrect spacing, wrong easing curves |
| Architecture spec | Navigation model divergence, state machine field misinterpretation |
| Build manifest | CSS ordering errors, wrong JS initialization sequence |
| PWA technical ref | Service worker lifecycle errors, manifest installability failures |
| Design system | Component structure inconsistency, wrong touch target sizes |

---

## Section 7: State File Architecture

### Why State Files Are Necessary

Multi-phase work executes across isolated Claude sessions that share no memory. Without an external state mechanism, each session would have no way to know what prior sessions completed, what files exist, or what remains to be done. The state file solves this by externalizing the execution checkpoint system to a persistent JSON file that any session can read.

The `meta-prompt.md` articulates the specific problem: "fresh chats with a cleared contacts window" are the preferred execution model because they eliminate context noise. But this design creates a continuity problem — the state file is the architectural solution to that problem.

Without state files, the following fail:
- Sequential execution chains (no way to determine the next step)
- Resumption after interruption (no way to determine what was completed)
- Parallelization (no way to prevent multiple agents from executing the same step)
- Data integrity verification (no record of how many entries were written)

### Schema

The `state.json` schema contains the following fields:

```json
{
  "version": "1.0.0",
  "buildTarget": "path/to/output/directory/",
  "completedSteps": [],
  "pendingSteps": ["step-01-id", "step-02-id", "...all step IDs"],
  "artifacts": {
    "itemCount": 0,
    "filesWritten": []
  },
  "dataChunks": {
    "category1": {},
    "category2": {}
  },
  "flags": {
    "flagName1": false,
    "flagName2": false
  }
}
```

**Field semantics:**
- `version` — schema version, enables future migration
- `buildTarget` — the output directory path; prevents hardcoding in each prompt
- `completedSteps` — append-only log of completed step IDs; starts empty
- `pendingSteps` — the complete ordered list of all step IDs; **must be fully populated at initialization**; items are removed as steps complete
- `artifacts` — counters and file lists for data integrity verification
- `dataChunks` — tracks which data entries have been written by category/type
- `flags` — boolean toggles that prerequisites use to check if required setup has occurred

### The Read/Write Discipline

**On session start (every session, no exceptions):** Read `state.json` in full. Confirm the assigned step ID is in `pendingSteps`. If it is not, do not execute — the step was already completed or the state is inconsistent.

**On session end (before exiting):** After the Verification section passes:
1. Append the completed step ID to `completedSteps`
2. Remove the completed step ID from `pendingSteps`
3. Set any relevant `flags` to `true`
4. Increment any relevant `artifacts` counters
5. Record data chunk keys if this was a data batch step

**The state update must occur before the session exits.** Performing the task without updating state leaves the state file inconsistent, causing the next session to attempt the same step again.

### Initialization Rule

The `pendingSteps` array must be **fully populated at initialization** with all step IDs in execution order. An empty `pendingSteps` is explicitly forbidden — the initialization step that creates `state.json` must produce a complete list, not a partial one that gets extended later.

This rule ensures that:
- Any session can determine the full scope of remaining work at any time
- The README index and `state.json` are consistent with each other from the start
- No "surprise" steps appear mid-execution

### Conflict Prevention

The sequential execution model is the primary conflict prevention mechanism. Since all prompts execute one at a time in separate sessions, simultaneous writes to `state.json` cannot occur. Parallel sub-agents spawned within a single session should only write to non-overlapping portions of state (separate flags, separate data chunk keys).

---

## Section 8: Sub-Agent Design Principles

### When to Spawn a Sub-Agent vs. Do Work Inline

The criteria from `meta-prompt.md`: spawn a sub-agent "if it is going to contribute to better results, accurate results, [and] get things done faster." Three conditions justify sub-agent spawning:

1. **Parallelization** — multiple independent tasks can execute simultaneously, reducing total execution time
2. **Context isolation** — the sub-task benefits from a fresh context window uncontaminated by prior work
3. **Specialization** — the sub-task requires different expertise or tools from the parent task

A sub-agent should NOT be spawned for work that is simpler to do inline, for tasks that depend on the current session's state (which the sub-agent cannot access unless passed explicitly), or when the coordination overhead exceeds the parallelization benefit.

### Structure of an Unambiguous Sub-Agent Instruction

An unambiguous sub-agent instruction contains:

```
1. A precisely bounded task statement — one action, stated once, in imperative form
2. The complete context needed for execution — no references to "what we discussed"
   or "as above"; everything the sub-agent needs must be in the instruction itself
3. Explicit file access scope — which files the sub-agent may read and which it may write
4. The expected output — format, file path, structure
5. A verification condition — how to know the task is complete
6. Instructions for reporting back — what to return to the parent agent
```

The key constraint on sub-agent instructions: **sub-agents do not share memory with the parent agent.** Everything the sub-agent needs must be explicitly embedded in its instruction. References to prior conversation, other files, or implied context are invisible to the sub-agent and will cause errors or hallucination.

### Scoping Sub-Agent Authority

**Read scope:** Define explicitly which files the sub-agent may read. A sub-agent that reads only its assigned context files cannot accidentally apply knowledge from other sources.

**Write scope:** Define explicitly which files the sub-agent may write. A sub-agent building one CSS section should have no authority to modify the JS logic files.

**Task scope:** The sub-agent's task ends when it produces its specified output. It does not extend to adjacent tasks, cleanup, optimization, or anything not explicitly in its instruction.

### Aggregating Sub-Agent Outputs

When multiple sub-agents execute in parallel and the parent agent must synthesize their results, the aggregation instruction must be explicit about:
- Which sub-agent outputs to collect
- How to combine them (concatenate? merge? synthesize?)
- Conflict resolution — if two sub-agents report different findings for the same item, both are preserved and the discrepancy is noted explicitly (neither is silently dropped)
- Where to write the aggregated result

---

## Section 9: Constraint Engineering

### How Constraints Are Encoded

The methodology uses two types of constraints: **explicit** (directly stated as prohibitions or requirements) and **implicit** (encoded through high specificity that forecloses alternative interpretations).

**Explicit constraints** use language such as:
- "Do NOT [action]"
- "Never [action]"
- "Must [requirement] — no exceptions"
- "This is NOT a [category]"
- "Never use `// ... more`, ellipses, or placeholder comments"

**Implicit constraints** are encoded by specifying the positive requirement so precisely that no deviation is possible. Example: stating "15–20 entries per data batch" constrains batch size without saying "do not write 21 entries." The positive specification leaves no room for a 30-entry batch.

### The Constraint Taxonomy

Six constraint types are evidenced in the source material:

**1. Technical hard limits** — 32K token output; Write tool only; no external URLs. These are architectural constraints with no exceptions.

**2. Data completeness mandates** — "No truncation"; "write ALL entries for that batch"; "no `// ... more`". These prevent the specific failure mode where Claude abbreviates large datasets.

**3. Scope boundaries** — "This IS an orchestration layer. This is NOT the application itself." IS/IS NOT framing explicitly defines both the positive scope and the excluded scope.

**4. Process sequencing constraints** — "Do not begin Phase 2 until Phase 1 is complete." Sequential ordering prevents phase-skipping.

**5. Prerequisite forward-reference prohibition** — "Never reference a prerequisite file or flag created by a later step." This enforces DAG acyclicity in the dependency graph.

**6. Failure mode prohibitions** — "Do NOT combine two atomic tasks into one prompt file — this is the cardinal failure mode." Naming a specific failure mode elevates it above the list of general prohibitions.

### The IS / IS NOT Framing Pattern

The `<constraints>` section of any well-formed prompt uses this structure:

```
This IS:
- [Affirmative statements of what the output is and does]

This is NOT:
- [Explicit exclusions: types of content, actions, or scope that are out of bounds]

Do NOT:
- [Specific prohibited actions, often targeting known failure modes]
```

This three-part structure covers: what to produce, what NOT to produce, and how NOT to behave. The three categories are not redundant — they address different failure modes. "This is NOT" prevents scope creep; "Do NOT" prevents specific execution errors.

### Why Constraints Receive Equal Design Attention

The source material devotes equal structural space to constraints as to positive requirements (a dedicated `<constraints>` section at the same level as `<requirements>`). [Inferred: The author treats constraint absence as equivalent to permission. A prompt without explicit negative constraints implicitly grants Claude freedom to use any approach, any file, any output format — defaults that may be worse than any specific failure mode the author was trying to prevent.]

### Verbatim Constraint Inclusion

The five hard constraints are included verbatim in every sub-prompt, with "no exceptions, no paraphrasing." The verbatim requirement reflects a specific belief: that paraphrased constraints are interpreted as soft suggestions rather than absolute rules. Exact wording preserves the constraint's force.

---

## Section 10: Output Specification Discipline

### The Complete Set of Output Specification Elements

A fully specified output instruction, as evidenced across the source material, contains all of the following:

**1. File path** — Exact, absolute file path. Not "write a markdown file" but "write to `connect-da-dots/prompt-01.md`."

**2. Format** — File format (Markdown, JSON, CSS, HTML) and any format-specific constraints (valid JSON, GFM throughout, triple-backtick code blocks for all examples).

**3. Section structure** — Ordered list of required sections with their heading levels. Not "include a verification section" but:

```
## Prerequisites
## Hard Constraints
## Task
## Verification
## State Update
```

**4. Section content** — What each section must contain. Not "describe the task" but "a single, unambiguous instruction in imperative form."

**5. Naming conventions** — How files are named, how titles are structured, what pattern to follow (`prompt-NN.md`, `# Prompt [NN]: [Action Title in imperative form]`).

**6. Forbidden content** — What may NOT appear in the output: `// ... more`, placeholder comments, truncated data, forward-looking prerequisites.

**7. Chat report format** — After file writes complete, what to display in chat — formatted as a specific markdown structure with exact field names.

**8. Verification checklist** — A pre-delivery executable checklist confirming all output elements are present before declaring completion.

### Under-Specified vs. Fully Specified

**Under-specified output instruction:**
```
"Generate the prompt files for the build pipeline and include a README."
```

This leaves open: how many files, what format, what sections, where to write them, how to name them, what the README must contain, what to report in chat after completion.

**Fully specified output instruction (from the source material):**

```markdown
## Output Format

The output directory (connect-da-dots/) must contain:
1. state.json — initial state file with all pendingSteps populated
2. prompt-01.md through prompt-NN.md — numbered prompt files
3. README.md — index table with columns:
   Prompt # | File | Purpose | Prerequisites | Est. Token Output | Sub-Agent Strategy

After all files are written, display in chat:
  Build orchestration complete.

  connect-da-dots/ contents:
    state.json       — [N] pending steps tracked
    README.md        — [N] prompts indexed
    prompt-01.md     — [title]
    ...

  Prompt breakdown:
    Initialization prompts:  [N]
    [category]: [N]
    Total: [N]

  Data coverage:
    [type1]: [N]/[expected]
    [type2]: [N]/[expected]
```

### Why Under-Specification Is a Failure Mode

Specific divergences that occur when output is under-specified:

- Claude generates files in the current working directory rather than the specified directory
- Claude omits sections it considers optional without being told they are required
- Claude abbreviates large data sets with `// ... more` to manage output length
- Claude uses inconsistent naming conventions across files
- Claude omits the chat report or formats it differently each time
- Claude completes the task without updating state, leaving the pipeline inconsistent

Each of these divergences requires manual intervention to correct. Full output specification eliminates the class of errors rather than fixing instances.

---

## Section 11: Edge Case Anticipation

### Pre-Empting Failure Modes in Prompt Design

The methodology's approach to edge cases is **proactive naming, not reactive correction.** Before execution, the author identifies the most likely failure modes and addresses each with a specific mechanism. The `refined-prompt.md` document contains the most concentrated evidence of this practice.

### Pattern: Explicit Failure Mode Naming

The most dangerous anticipated failure mode is given a name: "the cardinal failure mode." Naming a failure mode serves two purposes: it elevates it above general caution language, and it gives the executing agent a specific pattern to recognize and avoid.

From `refined-prompt.md`: "Do NOT: Combine two atomic tasks into one prompt file — this is the cardinal failure mode." The label "cardinal" signals priority: of all the failure modes listed, this one is the most consequential.

### Edge Cases Addressed in Source Material

| Edge Case | Anticipation Statement | Mechanism |
|-----------|----------------------|-----------|
| Single response exceeds 32K tokens | "If a task risks exceeding this, split it further and stop after the first sub-task completes" | Hard constraint #1, present in every prompt |
| Data entry list abbreviated | "Never use `// ... more`, ellipses, or placeholder comments" | Hard constraint #2; verification checks exact entry counts |
| Prompt references non-existent prerequisite | "Write prompt files that reference a prerequisite created by a later step" (forbidden) | Phase 2 assigns strict execution order; success criterion 9 validates no forward references |
| State.json becomes inconsistent across sessions | "Read state.json at the start of every session. Update state.json before exiting." | Hard constraint #3; state update is the final step before session close |
| Two tasks combined into one prompt | Named as "the cardinal failure mode" | Phase 1 catalogs every discrete unit before writing; verification checks atomic structure |
| Data batch exceeds 20 entries | "Exceed the 20-entry limit for any single data batch prompt" (forbidden) | Phase 1 groups entries into batches ≤20; Phase 6 verifies counts |
| Verification section missing or non-measurable | "Skip the Verification section — every prompt must have measurable checks before state update" (forbidden) | Schema requires Verification section; success criteria check its presence |
| Hard constraints paraphrased or omitted | "Verbatim under a 'Hard Constraints' section — no exceptions, no paraphrasing" | Verification confirms all 5 constraints present verbatim |

### Surfacing Ambiguity Before Execution

The pre-write verification checklist in `refined-prompt.md` represents the methodology's mechanism for surfacing ambiguity before execution begins — not after output is received. The 15-item self-verification checklist (Phase 5 of `/refinep`) and the 10-item success criteria list create two separate gates that must be passed before any prompt is used or any file is delivered.

[Inferred: The author's preference is to invest effort in pre-execution checks rather than post-execution diagnosis. The cost of a failed execution in a multi-prompt sequential pipeline — lost state, potentially corrupted output, manually checking where the build halted — is high enough to justify extensive pre-execution validation.]

---

## Section 12: Vocabulary and Language Patterns

### Terms of Art in the Methodology

The following terms appear consistently and carry specific technical meanings that differ from their general-language use:

**"Atomic"** — A single, bounded, verifiable unit of work that cannot be subdivided without losing the ability to verify completion. Used in: "atomic task," "atomic prompt," "one atomic build step." An atomic task has a binary completion state: done or not done. Compound tasks that have intermediate completion states are not atomic.

**"Self-contained"** — Able to execute correctly in a fresh Claude session with no prior conversation context, relying only on explicitly provided information. A self-contained prompt includes its own context; it does not reference "as discussed above" or "based on the prior analysis."

**"Source of truth"** — A designated file or document that is the authoritative reference for a piece of information. State.json is the source of truth for build progress. Data inventory files are the source of truth for clinical/domain data. When a conflict exists between two sources, the designated source of truth takes precedence.

**"Cardinal failure mode"** — The single most consequential error pattern in the execution context. Named explicitly to elevate it above general caution lists. The use of "cardinal" (meaning primary, most important) signals that this failure mode is architecturally disqualifying, not merely inconvenient.

**"Verbatim"** — Exactly as written, with no paraphrasing, no reordering, no omission. Used for hard constraints that must appear in every sub-prompt. The use of "verbatim" closes the interpretation gap that paraphrase creates.

**"Hard constraint"** — A rule with no exceptions and no conditional relaxation. Distinguished from "should" (strong preference) and "may" (optional). The hard constraint vocabulary maps directly to the MUST / SHOULD / MAY specificity gradient.

**"Zero information loss"** — A completeness standard for synthesis or documentation tasks. The output must contain everything the source material contains — no summarization, no selection, no compression that loses content.

**"Fidelity"** — Accuracy of reproduction relative to source material. "100% fidelity" means the output matches the source without interpretation, paraphrase, or omission.

**"No truncation"** — The prohibition against abbreviating any data set during generation. Specifically targets the failure mode where Claude writes `// ... more entries` or `/* see spec for full list */` to manage output length.

### The MUST / SHOULD / MAY Gradient

The `/refinep` command's Technique D3 codifies a specificity hierarchy that appears in all well-formed prompts:

- **MUST** — non-negotiable; failure to include is a disqualifying error
- **SHOULD** — strong preference; deviation requires explicit justification
- **MAY** — optional enhancement; include only if it adds value without complexity cost

This gradient is not stylistic. It communicates to Claude precisely which requirements are load-bearing and which are aspirational. Without this gradient, Claude must guess which requirements are critical — and that guess may be wrong.

### Why Precise Language Matters

The source material contains specific evidence of how imprecise language causes execution errors:

- **Paraphrased constraints** are interpreted as suggestions rather than absolute rules (evidenced by the verbatim constraint mandate — the requirement for verbatim inclusion exists because paraphrasing was observed to soften constraints)
- **Vague verbs** (improve, fix, update) suppress information about what "done" looks like, making completion verification impossible
- **Implicit scope** is equivalent to unlimited scope; Claude will act on anything it infers as in-scope unless boundaries are explicit
- **"Cardinal failure mode" naming** exists because simply listing the failure mode in a Do NOT list was insufficient — elevation to "cardinal" was required to produce consistent avoidance

---

## Section 13: Quality Assurance Loop

### How the Author Validates a Prompt Before Running It

The methodology embeds QA at three levels:

**Level 1: /refinep Phase 5 self-verification** — Before the refined prompt is written to `refined-prompt.md`, the 15-item verification checklist must pass. Any unchecked item triggers a revision cycle before output. This gate prevents prompts with structural or quality deficiencies from ever reaching execution.

**Level 2: Prompt file schema verification** — Before any sub-prompt is submitted for execution, its structure is verified against the required schema (5 sections: Prerequisites, Hard Constraints, Task, Verification, State Update). Missing sections cause the prompt to fail the success criteria check.

**Level 3: Post-execution state verification** — After each prompt executes, the Verification section's measurable checks must pass before `state.json` is updated. The state update is the final signal that an execution was correct. If verification fails, state remains unchanged — the step can be retried.

### Signals That a Prompt Needs Further Refinement

From the Phase 2 diagnostic in `/refinep`, the following patterns in a raw prompt signal the need for further refinement before execution:

- Vague action verbs (improve, fix, update, enhance) without measurable criteria
- No explicit scope boundaries (no files in scope / no files out of scope)
- No output format declaration (no specification of file path, structure, or format)
- No success criteria (no way to verify that execution was correct)
- No role definition (Claude has no expert persona to anchor its approach)
- Passive or wishful constructions ("it would be great if," "maybe consider")
- No constraint boundaries (no IS / IS NOT statements)
- Missing negative constraints (no Do NOT directives targeting failure modes)

### How /refinep Serves as a QA Gate

The `/refinep` command is structurally positioned as a **pre-execution quality gate.** Its Phase 5 verification checklist is not an audit — it is a release condition. The command will not write `refined-prompt.md` until all 15 verification items pass. This design means that every prompt produced by `/refinep` meets a minimum structural standard before it is available for use.

The Refinement Report included in `refined-prompt.md` provides full transparency: 25 diagnostic items with before/after status, all techniques applied with their specific mechanisms, and domain research conducted. This transparency serves two purposes: it allows the practitioner to understand and learn from each refinement, and it provides a verifiable audit trail for the refinement process.

### The QA Loop's Structure

```
Draft prompt (any quality)
  → /prompt: 8-rule structural optimization
  → /refinep Phase 2: 25-item diagnostic (identify all deficiencies)
  → /refinep Phase 3: domain research (fill knowledge gaps)
  → /refinep Phase 4: technique application (correct all deficiencies)
  → /refinep Phase 5: 15-item self-verification (confirm all corrections)
  → Decision: if any item fails → revise and re-verify
  → Output: refined-prompt.md (guaranteed to pass Phase 5 checklist)
  → Execution: sub-prompt runs in fresh session
  → Verification section: measurable checks pass
  → State update: step marked complete
```

The loop is closed at two points: Phase 5 verification (pre-execution) and the Verification section (post-execution). No step is considered complete without both gates passing.

---

## Section 14: Scalability Patterns

### How the Methodology Scales

The methodology scales from a single-file task to a multi-agent, multi-phase project through a consistent structural approach: everything that changes with complexity (the number of prompts, the number of context files, the number of state fields) is handled by the same mechanisms at all scales. Only the quantity changes, not the mechanism.

**Small task (1–5 prompts):** Apply `/prompt` for quick optimization. If production quality is required, apply `/refinep`. Execute directly. No state file needed.

**Medium task (10–30 prompts):** Initialize a `state.json` with all step IDs. Write context files for domain knowledge that sub-agents will need. Execute sequentially, updating state after each step.

**Large task (30–45+ prompts):** Full orchestration: meta-prompt decomposition strategy → 30–45 atomic prompts → 5–6 context files → complete state.json schema with dataChunks and flags → README index with Sub-Agent Strategy designations → sequential execution with parallel sub-agents where designated.

### What Remains Constant Across All Scales

Three elements remain constant regardless of task complexity:

1. **The atomicity principle** — each prompt does exactly one verifiable unit of work. A 5-prompt project and a 45-prompt project both use atomic prompts; the 45-prompt project simply has more of them.

2. **The self-containment requirement** — every prompt is executable in a fresh session with no prior context. This constraint does not relax at large scale; it becomes more important because more isolated sessions are executing.

3. **The constraint verbatim inclusion** — the five hard constraints appear verbatim in every sub-prompt regardless of scale. Large projects do not relax constraints.

### What Adapts

**Context file granularity.** Small projects may embed context directly in prompts. Medium projects may have 2–3 context files. Large projects may have 6+ context files covering separate domains (architecture, data, design, infrastructure). The number of context files scales with the complexity and specialization requirements of sub-agents.

**State file schema.** Small tasks may use a minimal state schema. Large tasks use the full schema with `completedSteps`, `pendingSteps`, `artifacts`, `dataChunks`, and `flags`. The schema expands as needed to track the project's specific completion signals.

**Parallel sub-agent use.** Small tasks execute sequentially; large tasks designate specific prompts as PARALLEL in the README, allowing sub-agents to parallelize independent work within a single session.

### The Ceiling

[Inferred from the 32K token hard limit and the 30–45 prompt target range: the methodology handles projects up to approximately 45 sequential steps with parallel sub-agent delegation within steps. Projects requiring more than this scale would need additional decomposition layers — meta-orchestration managing multiple sub-orchestration pipelines. The source material does not document this multi-layer orchestration pattern, suggesting it represents the current ceiling of documented methodology.]

---

## Section 15: Replication Guide

This section addresses you directly. To replicate this methodology in your own Claude Code workflow, you need specific, actionable knowledge organized in the recommended learning sequence.

### What to Internalize First: The /prompt Command

Before anything else, internalize the 8 optimization rules and make them a mental checklist you run on every prompt before submitting it. You do not need the command installed to apply these rules — you can apply them manually.

When writing any prompt, ask:
1. Does it lead with the outcome (what should be true after completion)?
2. Is scope explicitly defined (what files and systems are in scope)?
3. Are all constraints named (what cannot be done)?
4. Are compound tasks broken into ordered steps?
5. Are edge cases anticipated with specific handling instructions?
6. Are all references concrete (file paths, function names, line numbers)?
7. Are all vague verbs replaced with observable actions?
8. Is the expected output format declared?

If any answer is no, revise the prompt before submitting. This alone eliminates the majority of ambiguity-driven execution errors.

### What to Internalize Second: The /refinep Command

Once you understand the 8 rules, understand the 25-technique library and 6-phase pipeline. The critical shift is recognizing that refinement is systematic, not creative. The `/refinep` command's value is in its completeness — it checks all 25 diagnostic items regardless of which ones you would have thought to address. Use it for any prompt that will execute complex, multi-step, or multi-file work.

The Phase 5 verification checklist (15 items) is the replication minimum — memorize it. Any prompt that fails one of these 15 items is not production-ready.

### What to Internalize Third: Context Files and State Architecture

Context files and state files are the structural backbone of multi-session work. The key insights:

- **Pre-write your domain knowledge before you start.** Do not rely on Claude to infer it from prompts. Write it out as a reference document — exact values, exact names, exact counts — and load it at the start of each relevant sub-agent.
- **State.json must be fully populated at initialization.** Do not add steps as you go. Every step ID must be in `pendingSteps` before the first session executes.
- **Read state at start, write state before exit.** No exceptions. Any session that does not update state leaves the pipeline inconsistent.

### Common Failure Modes and How to Correct Them

**Failure mode 1: Compound atomic tasks**
*Symptom:* A single prompt attempts to write multiple CSS sections, multiple data categories, or multiple JS modules. The output is either truncated (hits 32K token limit) or partially correct (some sections are complete, others are abbreviated).
*Diagnosis:* The prompt's Task section contains more than one verifiable unit of work.
*Correction:* Split into one prompt per unit. If a data category has 20 entries, it gets its own prompt. Never combine two separable tasks.

**Failure mode 2: Implicit prerequisites**
*Symptom:* A prompt fails because it references a file or flag that doesn't exist yet, even though a prior session was supposed to create it.
*Diagnosis:* The Prerequisites section is empty or says "none" when it should list specific flags/files.
*Correction:* For every resource your prompt references, trace back which step creates it and add that step's completion flag as a prerequisite. Check that no prerequisite comes from a later step.

**Failure mode 3: Paraphrased hard constraints**
*Symptom:* Constraints are present but stated as soft guidelines. Sub-agents deviate from them.
*Diagnosis:* The Hard Constraints section uses paraphrased or summarized versions of the constraints.
*Correction:* Replace with verbatim text. Word-for-word. "Never use `// ... more`, ellipses, or placeholder comments" must be exactly that — not "don't abbreviate data."

**Failure mode 4: Missing output format specification**
*Symptom:* Claude writes files in the wrong directory, omits required sections, or formats output inconsistently across sessions.
*Diagnosis:* The prompt specifies what to produce but not where to put it, what format to use, or what sections it must contain.
*Correction:* Add an explicit output format specification: exact file path, required sections in order, naming convention, and what to report in chat after completion.

**Failure mode 5: State not updated**
*Symptom:* A session executes successfully but the next session attempts the same step again, or the pipeline shows the wrong completion count.
*Diagnosis:* The State Update section was not executed or was skipped when verification failed.
*Correction:* Treat the state update as a mandatory final step — not optional, not conditional on anything except the Verification section passing. If verification fails, fix the issue and re-run verification before updating state. Never skip the state update on a successful execution.

**Failure mode 6: Context not loaded**
*Symptom:* Sub-agent output contains incorrect values, inconsistent naming, or missing data that was specified in a context file.
*Diagnosis:* The sub-agent's prompt does not explicitly reference or load the relevant context file.
*Correction:* Every sub-agent instruction must explicitly reference which context files to read, with the instruction to read them before beginning work. Context files are not automatically available — they must be explicitly loaded.

### The Minimum Viable Starting Point

If you have never applied this methodology before, start here:

1. Take your next Claude Code task and apply the 8 optimization rules from the `/prompt` command manually before submitting.
2. Run `/refinep` on the result. Read the Refinement Report — specifically the Diagnostic Results table and the Techniques Applied table. Study what changed and why.
3. For your next multi-session project, create a `state.json` with `completedSteps: []` and `pendingSteps` containing all step IDs before you run the first session. Read and update it in every session.

The methodology's value compounds with use. The first application will feel procedural; after a dozen applications, the diagnostic framework becomes a natural pre-execution mental checklist.

---

*All inferences in this document are labeled `[Inferred: reasoning]`. All factual claims are traceable to one of the seven source files analyzed in Phase 1. Application-specific content from source files has been generalized to the methodology pattern it demonstrates.*
