# North Star: Cognitive Infrastructure Engineering (CIE)
# Permanent Grounding Document — Authority Level: Absolute
# Ambiguity Target: ≤5% — Every judgment call is resolved. No interpretation required.

---

## WHAT THIS DOCUMENT IS

This is the highest-authority source of truth for the CIE system. Every command, every generated file, every decision made by any LLM operating within this system is constrained by the rules in this document. When user feedback conflicts with this document, this document wins at the meta and meta-meta level. User feedback governs micro and macro changes only — see NSA framework for exact drift detection rules.

This document does not describe a philosophy. It encodes operational rules. Every section ends in decision trees or explicit behavioral directives.

---

## CORE PREMISE

Most people use AI transactionally: one input, one output, one task, done. CIE is a different operating mode. The AI is not the product — the system the AI builds and maintains is the product. The user's job is to architect the conditions. The AI's job is to execute within them.

**Behavioral directive**: At no point should any LLM operating in this system ask "what should I do?" The system always tells it what to do next. If it cannot find the answer in this document or the files it has access to, it must flag the gap explicitly rather than guess.

---

## FRAMEWORK 1: Hierarchical Abstraction Mapping (HAM)

### Definition
Every piece of information — in the brain dump, in user feedback, in a task description, in a generated file — exists at one or more of five abstraction levels. All five levels must be extracted before any action is taken.

### The Five Levels

| Level | Captures | Example |
|---|---|---|
| meta-meta | Why the system exists. The worldview, identity, philosophy behind the intent. | "I want systems that scale without requiring me to think each time." |
| meta | How the system is designed to behave. Governing logic, principles, operating mode. | "Fresh chats are stateless execution units. Context is managed externally." |
| macro | What the system produces. Major components, outcomes, relationships between parts. | "The system produces commands, grounding docs, folder architecture, and handoff files." |
| micro | How each component works. Parameters, variables, specific behaviors. | "Each command reads one input file and writes one output file to a dated subfolder." |
| micro-micro | Edge cases, implicit constraints, unstated assumptions, failure modes. | "If the user's input file is missing, the command halts and outputs a specific error message." |

### Extraction Rules

**Rule HAM-1**: Always extract all five levels before taking any action. Never assume a level is empty.

**Rule HAM-2**: Distinguish explicit from implicit at every level.
- Explicit = directly stated in the input.
- Implicit = reliably inferable from context, pattern, or intent. If there is any doubt, mark it as implicit and flag for confirmation.

**Rule HAM-3**: When extracting from a brain dump, treat the brain dump as containing all five levels simultaneously. Do not read it linearly — read it as a multi-dimensional object and map each statement to its level(s).

**Rule HAM-4**: If a statement appears to exist at multiple levels, record it at all applicable levels with a note indicating the relationship.

**Rule HAM-5**: Never compress a higher level into a lower one. "I want this to feel effortless" is a meta-meta statement. It does not get compressed into "make the UX clean." It stays at meta-meta and informs every micro decision.

### Decision Tree: Which Level Is This?

```
Is this about WHY the system exists or the person's worldview?
  YES → meta-meta
  NO ↓
Is this about HOW the system is designed to work in principle?
  YES → meta
  NO ↓
Is this about WHAT the system produces (major components/outcomes)?
  YES → macro
  NO ↓
Is this about HOW a specific component works (parameters/variables)?
  YES → micro
  NO ↓
Default → micro-micro (edge case, constraint, implicit assumption)
```

---

## FRAMEWORK 2: Reverse Outcome Engineering (ROE)

### Definition
Never plan forward from the current state. Always start from the fully realized end state and decompose backwards until you reach atomic actions that fit within a single context window.

### The Process

```
Step 1: Define the end state in full — what exists, what works, how it feels to use it
Step 2: Ask "what must be true for this to exist?" — list all prerequisites
Step 3: For each prerequisite, ask the same question recursively
Step 4: Stop recursing when you reach an action that:
         (a) fits in one context window AND
         (b) has all its dependencies already resolved
Step 5: Order the atomic actions by dependency chain
Step 6: Assign each action to a fresh chat execution unit
Step 7: Design the handoff document between each unit
```

### Context Window Fit Rule

**Rule ROE-1**: An action fits in one context window if the estimated total tokens (input files + instructions + expected output) is ≤80,000 tokens. If uncertain, split.

**Rule ROE-2**: If splitting is required, the split point must be at a clean output boundary — the first unit produces a complete, standalone artifact that the second unit can consume without needing context from the first unit's reasoning process.

**Rule ROE-3**: The handoff document is not a summary. It is a complete context package. The next fresh chat must be able to operate solely from the handoff document and the files it points to. No shared memory. No assumed context.

### Handoff Document Contract

Every handoff document must contain exactly:
1. **Current state**: What exists right now, with file paths.
2. **What was decided**: Every decision made in the previous step, with rationale.
3. **What was explicitly ruled out**: Rejected options and why.
4. **What comes next**: The exact next action, with the exact command or file to use.
5. **Open questions**: Anything flagged as uncertain, needing user input before proceeding.
6. **Files to read**: Exact paths of every file the next step needs.

**Rule ROE-4**: If a handoff document is missing any of these six elements, it is incomplete. Do not proceed to the next step. Complete the handoff document first.

---

## FRAMEWORK 3: Prompt-as-Architecture (PAA)

### Definition
The structure of a prompt must demonstrate the methodology it wants Claude to follow — not describe it. A prompt that tells Claude to "think recursively" is weaker than a prompt whose sections are structured recursively.

### Rules

**Rule PAA-1**: Never use meta-commentary in prompts. Do not write "you should think about this at multiple levels." Instead, structure the prompt into multiple levels — Claude will follow the structure.

**Rule PAA-2**: The sections of a prompt and their relationships to each other should mirror the cognitive process you want Claude to execute.

**Rule PAA-3**: Every prompt has an implicit architecture. Make it explicit. Before writing any prompt, define: what sections it needs, what order they appear in, and what the relationship between each section is.

**Rule PAA-4**: A prompt that must be sent to a fresh chat must be fully self-contained. It must contain or reference every piece of context the executing Claude needs. Test: can someone with zero knowledge of this conversation execute this prompt correctly? If no, it is incomplete.

**Rule PAA-5**: Generated prompts (prompts that create other prompts) must embed the methodology into their structure, not reference this document. The document should not need to be re-read for the prompt to work.

---

## FRAMEWORK 4: North Star Anchoring (NSA)

### Definition
User feedback operates at the micro and macro level. The north star operates at the meta and meta-meta level. These must never be conflated. This document is the north star. It governs all changes.

### Drift Detection Rule

When any user input arrives, map it to an abstraction level using HAM before implementing anything.

```
User input maps to micro-micro or micro?
  → Implement directly. No confirmation needed.

User input maps to macro?
  → Implement, but log the change as a macro-level modification.
  → Note which macro component was changed and how.

User input maps to meta?
  → PAUSE. Do not implement.
  → Output: "This feedback would change how the system is designed to behave [meta level].
    Current meta principle: [quote the principle].
    Proposed change: [describe what would change].
    Confirm to proceed."

User input maps to meta-meta?
  → PAUSE. Do not implement.
  → Output: "This feedback would change why the system exists [meta-meta level].
    Current north star: [quote the relevant section].
    Proposed change: [describe what would change].
    This requires explicit written authorization before proceeding."
```

**Rule NSA-1**: This document cannot be modified by a command. It can only be modified by the user directly editing the file.

**Rule NSA-2**: Any command that references this document must read it at the start of execution, not from memory.

**Rule NSA-3**: If this document and a user instruction conflict, this document wins at meta and meta-meta. The user wins at macro, micro, and micro-micro.

**Rule NSA-4**: "The self-iteration command" (command-07) must reference this document every time it runs. It is the constraint layer that prevents drift from accumulating across iterations.

---

## FRAMEWORK 5: Meta-System Architecture (MSA)

### Definition
This system is built in layers. Each layer governs the layer below it. Changes propagate downward only. A lower layer cannot redefine a higher layer.

### The Layer Stack

```
Layer 0: North Star (this document)
          — The philosophy and rules. Never changes except by direct user edit.

Layer 1: The system being built (the product — e.g., autonomous-business)
          — The actual deliverable. Constrained by Layer 0.

Layer 2: Brand/ICP customization layer
          — Makes Layer 1 adaptable to any brand. Does not change Layer 1's architecture.

Layer 3: Self-iteration command
          — Improves Layer 2 outputs safely. References Layer 0 before every run.

Layer 4: Implementation plan generator
          — Executes Layer 3 outputs. Produces dated, numbered artifacts.

Layer 5: Folder/file audit trail
          — Makes Layer 4 repeatable and scalable. Contains no logic — only state.
```

**Rule MSA-1**: A change at Layer N must be evaluated against Layer N-1 before implementation.

**Rule MSA-2**: If a change at Layer N would break Layer N-1's constraints, the change is rejected and reformulated at a lower scope.

**Rule MSA-3**: Infrastructure (command files, folder architecture, handoff formats, workflow logic) lives at Layers 1-3. Content (brand voice, ICP, copy, specific outputs) lives at Layers 2-4. When unsure which category something belongs to: if removing it would break the system's ability to function for ANY brand, it is infrastructure. If removing it would only affect one brand's outputs, it is content.

---

## FRAMEWORK 6: Context-as-Constraint

### Definition
The context window is not an inconvenience. It is a design parameter. Every architecture decision is made with context limits as a first-class constraint. This produces better systems, not worse ones — it forces decomposition, which produces clarity.

### Rules

**Rule CTX-1**: Each fresh chat is a stateless execution unit. It has no memory of previous chats. It can only know what its input documents tell it.

**Rule CTX-2**: Every fresh chat unit has exactly: one trigger (the command or prompt), one or more input files (listed explicitly), one deliverable to produce, and one handoff document to generate.

**Rule CTX-3**: A fresh chat must not be asked to hold more than three large files in context simultaneously. "Large" = >500 lines. If more context is needed, split the task further.

**Rule CTX-4**: The folder/file audit trail (Layer 5) is the system's external memory. What would normally be "remembered" across a long conversation is instead written to dated files and read by subsequent fresh chats.

**Rule CTX-5**: Token budget awareness — when generating prompts, estimate the token cost of the expected output. If the output is likely to exceed 4,000 tokens, design the prompt to produce a structured output with clear stopping points so partial results are still useful.

### Fresh Chat Execution Unit Template

Every command file in this system follows this template:

```
1. READ: [exact file paths to read before doing anything]
2. APPLY: [which CIE frameworks apply to this task]
3. RESEARCH CHECK: [apply Research Discernment Rule — see below]
4. EXECUTE: [the task, structured per PAA rules]
5. OUTPUT: [exact file path and format of deliverable]
6. HANDOFF: [generate handoff document at exact path]
7. NEXT STEP: [tell user exactly what to do next]
```

---

## FRAMEWORK 7: Separation of Concerns

### Definition
Infrastructure and content are never mixed. Infrastructure changes require explicit authorization. Content changes can be made freely.

### Classification Rules

**Infrastructure** = anything that, if changed, would affect the system's ability to function for any user, brand, or objective:
- Command file logic and structure
- Folder architecture and naming conventions
- Handoff document format
- Fresh-chat sequencing logic
- This north star document

**Content** = anything that only affects outputs for a specific brand, ICP, or objective:
- Brand voice guides
- ICP documents
- Copy files (VSL scripts, landing pages, etc.)
- Product-specific configurations
- Platform-specific content (Threads posts, Gumroad copy, etc.)

**Rule SOC-1**: When modifying the system, classify every proposed change as infrastructure or content before implementing it.

**Rule SOC-2**: Infrastructure changes require the user to have explicitly authorized the change (either in the original instruction or by confirming a flag).

**Rule SOC-3**: Content can be regenerated from scratch without breaking the system. Infrastructure cannot. When in doubt, classify as infrastructure.

---

## FRAMEWORK 8: Universal Achievement Layer (UAL)

### 8.1 — Purpose

UAL answers the question CIE does not answer — "Is this system achieving its goal and at what rate?" UAL operates as an evaluation and feedback layer within CIE. It does not change how systems are built. It governs how systems are measured, iterated, and diagnosed.

### 8.2 — What UAL adds to existing CIE frameworks

| Framework | Enhancement | Detail |
|---|---|---|
| ROE | Leverage Point Discovery | Only decompose along variables that move the result disproportionately — apply the 7 leverage filters from UCLAD before finalizing the decomposition sequence |
| NSA | Failure Diagnostics | When drift is detected, run the 8-layer failure diagnostic before deciding what to change: Goal coherence → Metric validity → Variable map → Leverage accuracy → Controllability → Adherence → Cadence → Hidden bottleneck |
| MSA | Phase Logic | Each MSA layer has a phase; correct actions become incorrect when applied in the wrong layer/phase; define phase exit triggers for each layer |
| CTX (Context-as-Constraint) | Cadence | The review cadence for the system maps to: real-time = within a fresh chat, daily = per session, weekly = per iteration cycle, monthly = per self-iteration command run |
| SOC | Control Surface distinction | Infrastructure variables = directly controllable; content variables = indirectly influenceable; background constraints = do not build execution around these |

### 8.3 — UAL Success Criteria Rule

Every system CIE builds must have two kinds of success criteria defined during Step 2 (command-02-ux.md):
- **External proof**: observable from outside (outputs, metrics, behaviors, third-party response)
- **Internal proof**: confirmed from within (felt progress, reduced friction, clarity)

If a system has only internal proof, it is drift-prone. If only external, it becomes empty. Both are required. This is a hard constraint — command-02-ux.md must surface both.

### 8.4 — UAL Binary Decision Rule

Every command in any system CIE builds must include at minimum these binary decision thresholds in its execution logic:
- If output is below acceptable quality → diagnose using 8-layer failure tree before retrying
- If output is on target → continue
- If no movement over review window → escalate to self-iteration command
- If drift detected → apply NSA drift detection first, then UAL failure diagnostics second

### 8.5 — UAL Phase Logic for CIE Systems

All systems built by CIE pass through phases. Each phase defines what matters now, what to ignore, and what triggers the next phase. The default phases for any CIE-built system are:
- **Phase 1 (Orientation)**: establish north star, UX profile, command set. Ignore output quality. Exit trigger: all commands exist.
- **Phase 2 (Testing)**: run commands, collect feedback. Ignore scale. Exit trigger: consistent output quality across 3+ runs.
- **Phase 3 (Optimization)**: improve individual commands. Ignore new features. Exit trigger: no recurring failure modes.
- **Phase 4 (Expansion)**: add new commands, new domains. Exit trigger: user-defined.
- **Phase 5 (Self-iteration)**: system improves itself. No exit — this is the operating state.

### 8.6 — What UAL does NOT do

UAL does not change the meta or meta-meta levels of CIE. UAL does not make UCLAD's Layer III template the default output format. UAL does not add the full 13-step UCLAD sequence to any command. UAL does not override any existing CIE framework rule. If UAL and any existing CIE rule conflict, the existing CIE rule wins.

---

## RESEARCH DISCERNMENT RULE

### When to Research vs. Use Internal Context

This rule applies any time a command needs information that may be factual, technical, or platform-specific.

```
Does this information involve:
  - Specific software versions, APIs, or platform behavior?
  - Best practices that evolve over time (e.g., Claude Code command architecture)?
  - Platform algorithms or ranking factors (e.g., Threads algorithm)?
  - Limitations or capabilities of a tool the system will use?
    YES → Research required. Do not rely on internal context.

Is this information:
  - A stable programming concept (e.g., what a loop is)?
  - Internal project knowledge (files in this repo)?
  - General reasoning, logic, or strategy?
  - Something Claude has high confidence in AND that doesn't change with versions?
    YES → Internal context sufficient. Do not research.
```

**Rule RES-1**: When research is required, it is done in a dedicated step before the main execution. Research outputs are embedded into the work — not appended as references.

**Rule RES-2**: Research is scoped precisely. Do not research broadly. Define the exact question before searching. Output: a concise factual block embedded in the relevant section of the work.

**Rule RES-3**: Research findings that contradict this document's frameworks are flagged to the user. They do not automatically override this document.

**Rule RES-4**: If research cannot be completed (no tool access, no web access), the command notes what was assumed and marks it as unverified.

---

## FOLDER AND FILE NAMING CONVENTIONS

All outputs of this system follow these conventions:

**Folders**: `YYYY-MM-DD-[sequence-number]-[brief-descriptor]/`
Example: `2026-03-10-001-ux-profile/`

**Files**: `[sequence-number]-[descriptor].md`
Example: `001-handoff.md`, `002-ux-profile.md`

**Commands**: `command-[two-digit-number]-[descriptor].md`
Example: `command-02-ux.md`, `command-07-self-iteration.md`

**Rule FILE-1**: Never overwrite an existing numbered artifact. Always increment the sequence number.

**Rule FILE-2**: Every output folder contains at minimum: the deliverable file and a handoff document.

**Rule FILE-3**: The README in every output folder contains only: what was produced, the date, and the next step.

---

## THE SEQUENCE (Steps 1–7)

This is the canonical execution sequence for building any system using CIE.

| Step | Command | Purpose | Input | Output |
|---|---|---|---|---|
| 1 | (manual) | Save north star, create structure | This document | `cie-system/` folder |
| 2 | `command-02-ux.md` | Define ideal user experience via structured questions | User answers | `ux-profile.md` |
| 3 | `command-03-derive-commands.md` | Derive minimum command set from UX | `ux-profile.md` | `command-set.md` |
| 4 | `command-04-grounding-docs.md` | Build grounding document architecture | `command-set.md` | `grounding-doc-architecture.md` |
| 5 | `command-05-folder-architecture.md` | Build external memory layer | `grounding-doc-architecture.md` | `folder-architecture.md` |
| 6 | `command-06-build-commands.md` | Build all commands | All prior outputs | Full command set |
| 7 | `command-07-self-iteration.md` | Build self-iteration command | All prior outputs + north-star.md | `self-iteration-command.md` |

**Rule SEQ-1**: Steps must be executed in order. No step can be skipped.

**Rule SEQ-2**: Each step is a fresh chat. Never chain steps in one chat unless a step's output is trivially small (<200 tokens) and explicitly marked as chainable.

**Rule SEQ-3**: Step 7 is always last. It cannot be built until all other steps are complete, because it must protect everything that steps 1–6 created.

---

## FAILURE MODES AND RESPONSES

| Failure Mode | Detection | Response |
|---|---|---|
| Missing input file | Command cannot find referenced file | Halt. Output exact path that is missing. Do not proceed. |
| Ambiguous user instruction | Instruction maps to >1 abstraction level with conflicting implications | Apply drift detection. Flag the conflict. Do not guess. |
| Context overflow risk | Estimated token cost >80k | Split. Define the handoff boundary first, then execute. |
| Research gap | Required information is unavailable | Note the gap explicitly. Proceed with assumption marked [UNVERIFIED]. |
| North star conflict | User instruction would change meta or meta-meta level | Pause. Follow NSA drift detection rule exactly. |
| Circular dependency | Step N requires output of Step M, but Step M requires Step N | Flag to user. Ask which step has priority. Do not attempt to resolve autonomously. |

---

*This document is the north star. It does not change unless the user edits it directly. All commands in this system read this document at runtime. It is never cached, never summarized, always read in full.*
