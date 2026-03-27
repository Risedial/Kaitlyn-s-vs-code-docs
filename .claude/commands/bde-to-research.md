# /bde-to-research — BDE Output → Research Argument Generator
**Purpose:** Reads all files produced by /bde at a given folder path and outputs a single, perfectly formed argument for /research.
**Output:** One ready-to-run command string. Nothing else.

**Folder path provided:** $ARGUMENTS

---

## OPERATING CONTRACT

You are synthesizing a brain dump extraction into a research question. You do not summarize the brain dump. You do not describe what the system does. You extract what is NOT yet known — the gap between what the extraction reveals the user wants to achieve and what would need to be true (researched, validated, understood) for them to achieve it. That gap is the research question.

**Output format (final output only):**
```
/research [your precisely formulated research question here]
```

One line. Nothing before it. Nothing after it.

---

## STEP 1 — READ ALL BDE OUTPUT FILES

The folder path is: $ARGUMENTS

Read every file that exists in that folder, in this order. If a file is absent, skip it and continue — do not halt.

**Priority reads (read these first — highest signal):**
1. `$ARGUMENTS/bd-extraction/00-inventory/system-map.md`
2. `$ARGUMENTS/bd-extraction/01-outcomes/outcome-registry.md`
3. `$ARGUMENTS/bd-extraction/04-meta-system/system-integrity-rules.md`
4. `$ARGUMENTS/bd-extraction/04-meta-system/orchestration-spec.md`
5. `$ARGUMENTS/bd-extraction/04-meta-system/approach-selection-decision-tree.md`
6. `$ARGUMENTS/bd-extraction/04-meta-system/parameter-extraction-algorithm.md`

**Secondary reads (read after priority files):**
7. `$ARGUMENTS/bd-extraction/01-outcomes/fresh-chat-vs-chain-map.md`
8. All files in `$ARGUMENTS/bd-extraction/02-reverse-engineered/` (read each)
9. All files in `$ARGUMENTS/bd-extraction/03-templates/` (read each)
10. `$ARGUMENTS/bd-extraction/README.md`

Do not write anything yet. Read everything first.

If $ARGUMENTS is empty or no files are found: output `ERROR: No folder path provided or bd-extraction/ folder not found at "$ARGUMENTS". Run: /bde-to-research [path to folder containing bd-extraction/]` and stop.

---

## STEP 2 — EXTRACT THE FIVE ABSTRACTION LAYERS

After reading all files, extract the following from the BDE output. This is internal analysis — do not output it.

**meta-meta (WHY):** What is the governing intent behind everything in the extraction? What problem in the world is this trying to solve? What does success look like at the highest level of abstraction?

**meta (HOW the system is designed to work):** What are the governing principles, operating modes, and architectural rules that constrain how the goal can be achieved?

**macro (WHAT is being built):** What are the major components, deliverables, and outcomes the extraction maps out?

**micro (HOW each component works):** What specific operations, parameters, and behaviors are defined for each component?

**micro-micro (EDGE CASES):** What constraints, failure modes, implicit assumptions, and unresolved decision points appear in the extraction?

---

## STEP 3 — IDENTIFY THE KNOWLEDGE GAP

Determine what is NOT answered by the BDE output but is required for the user to achieve the meta-meta intent.

Apply this filter in order. Stop at the first gap that is real, specific, and researchable:

**Filter A — Structural unknowns:** Is there a system, mechanism, or causal relationship that the extraction assumes exists but does not explain? (e.g., "the system assumes X works — but HOW does X work, and under what conditions?")

**Filter B — Validation gaps:** Does the extraction define an approach or methodology but lack evidence for why that approach is correct? (e.g., "the plan calls for Y — but what does the evidence actually say about Y's effectiveness?")

**Filter C — Variable discovery gaps:** Does the extraction name key variables but not explain what drives them, what they interact with, or what produces them?

**Filter D — Comparative gaps:** Does the extraction make a choice between approaches without a basis for comparison? (e.g., "approach A was chosen — but what distinguishes high-performing from low-performing implementations of this approach?")

**Filter E — Domain transfer gaps:** Does the extraction draw on principles from one domain that may not transfer cleanly to the user's domain? (e.g., "this principle works in domain X — but does it hold in domain Y, and under what conditions?")

The first real gap you identify becomes the seed of the research question.

---

## STEP 4 — FORMULATE THE RESEARCH QUESTION

Transform the identified gap into a research question that meets ALL of the following criteria. Check each criterion before finalizing.

**Criterion 1 — Investigatable:** The question must have multiple distinct variables that can be researched independently. If the question has only one variable, it is too narrow — broaden it.

**Criterion 2 — Not already answered:** The question must not be answerable from the BDE output files you just read. If the answer is already there, the question is wrong — go back to Step 3.

**Criterion 3 — Actionable:** The research output must directly inform what the user is building. If knowing the answer would not change how the system is designed or executed, the question is too abstract — make it more specific.

**Criterion 4 — Scoped correctly:** The question must be answerable across 3–10 research sessions (not too narrow for one session, not so broad it never converges). If it is too narrow, add a comparative or contextual dimension. If it is too broad, add a scope constraint (domain, condition, context).

**Criterion 5 — Self-contained:** The question must be understandable without reading the BDE output. Someone who has never seen the BDE files must be able to understand what is being researched.

**Criterion 6 — Phrased as a question:** Must end with a question mark. Must begin with "What", "How", "Why", "Under what conditions", "Which", or "To what extent".

---

## STEP 5 — OUTPUT

Output exactly one line:

```
/research [your research question]
```

Do not explain the question. Do not summarize what you read. Do not describe the BDE output. Do not add caveats or alternatives. Output the command string and stop.
