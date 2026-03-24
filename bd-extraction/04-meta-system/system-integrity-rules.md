# System Integrity Rules
**Purpose:** Constraints that survive all future user instructions; enforcement logic; compliance-while-responsive pattern
**Date:** 2026-03-22

---

## What Are Integrity Rules?

These are constraints that CANNOT be overridden even if a future instruction, prompt, or convenience argument suggests doing so. They exist because violating them produces work that is wrong in ways that may not be immediately visible.

---

## Rule 01 — No Claim Without a Mechanism

**Rule:** Every assertion about how a stressor affects a marker must include a specific mechanism — not a generalization.

**Violation example:**
> "Stress weakens immunity and can lower SIgA."

**Compliant example:**
> "Cortisol directly downregulates pIgR expression on mucosal epithelial cells, reducing luminal SIgA delivery independent of plasma cell output."

**Enforcement:** Before any document or diagram is finalized, scan for vague causal language ("weakens," "affects," "disrupts," "impacts"). Replace each with a specific mechanism or flag as a research gap.

---

## Rule 02 — Same Marker, Different Nodes = Different Interventions

**Rule:** Low [marker X] is NOT a single clinical entity. It must always be interpreted in context of which node is most likely failed.

**Violation example:**
> "Low SIgA → support gut immune function."

**Compliant example:**
> "Low SIgA + elevated cortisol + normal microbiome markers → pIgR suppression most probable; intervention: HPA load reduction and cortisol support, not generic immune supplementation."

**Enforcement:** Any intervention recommendation must include the node identification step. Strip any recommendation that skips directly from marker to intervention.

---

## Rule 03 — No Missing Node Documentation

**Rule:** Every node in a marker's pathway must be documented before that marker is considered researched. Partial maps cannot be used to build the visual diagram or the nodal reasoning framework.

**Violation:** Using a marker with 2 documented nodes (missing Node 4 because it's harder to research).

**Enforcement:** Template validation checklist is mandatory and non-skippable. Any file with fewer than the required nodes is marked "incomplete" and excluded from builds.

---

## Rule 04 — No Speculative Cross-Cluster Links

**Rule:** Cross-cluster node overlap claims must be supported by a specific mechanism. Do not assert that "cortisol affects X" unless the specific mechanism for that marker has been researched.

**Violation:** Adding cortisol as an upstream stressor for every marker because cortisol is generally immunosuppressive.

**Enforcement:** Cross-cluster link registry entries require a mechanism citation. Generic "cortisol suppresses" entries are rejected.

---

## Rule 05 — Research Gaps Are Flagged, Not Filled

**Rule:** If the mechanism for a node is uncertain or not yet researched, it must be labeled as a research gap — never filled with a plausible guess.

**Violation:** Writing a mechanism sentence for HPHPA/dopamine interference without having researched the specific enzyme competition mechanism.

**Enforcement:** Every upstream map file contains a Research Gaps section. Incomplete research generates an entry there. Downstream builds (HTML, nodal reasoning) are blocked by any unfilled research gap in their input files.

---

## Rule 06 — Audience Must Be Defined Before Writing

**Rule:** No practitioner-facing document may be written without explicit audience definition. Mechanism depth, language register, and example complexity all depend on who will use it.

**Enforcement:** Methodology document (Outcome 08) execution plan includes an explicit audience gate step that cannot be skipped.

---

## Rule 07 — Validation Is Non-Skippable

**Rule:** Every fresh chat prompt must include a validation gate. The task is not complete until that gate is passed. This applies to both technical outputs (HTML must render) and research outputs (minimum node counts must be met).

**Enforcement:** Prompts built with `fresh-chat-prompt-template.md` include the validation gate section as a required field. Any prompt missing this field is malformed.

---

## Rule 08 — Context Limits Are Managed, Not Ignored

**Rule:** If context is approaching a limit during a task, stop and output an intermediate artifact rather than rushing to complete and producing incomplete work.

**Enforcement:** Every fresh chat prompt includes a SPLIT INSTRUCTIONS section. The instruction is: "If you reach [condition], stop, output [intermediate artifact], and note 'Resume from [point]'."

---

## Compliance-While-Responsive Pattern

The integrity rules above may sometimes appear to conflict with a user request for speed or simplicity. The correct response is:

1. **Complete the user's immediate request** to the extent that integrity rules permit
2. **Flag the constraint** that prevents full compliance: "I can complete [X] but [Y] requires [missing input] before it can be done correctly"
3. **Offer the path forward**: "To complete [Y], the next step is [specific action]"

This is NOT:
- Refusing the task entirely
- Producing work that violates the rules while noting the violation
- Deferring the task indefinitely without a forward path

---

## Integrity Rule Conflict Resolution

If two rules appear to conflict:

| Rule Priority | Example |
|---|---|
| Rule 05 (no speculation) > Rule 03 (all nodes documented) | Better to flag a gap than to fill it with a guess |
| Rule 01 (specific mechanism) > Rule 06 (audience language) | Mechanism must be correct even if simplified for audience |
| Rule 04 (no speculative cross-links) > Rule 02 (node interpretation) | Don't identify a node if the cross-link that suggests it is speculative |
