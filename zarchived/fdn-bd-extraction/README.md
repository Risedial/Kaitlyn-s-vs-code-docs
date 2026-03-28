# FDN Methodology — Brain Dump Extraction
**Source:** `raw context/claude conversation.md`
**Created:** 2026-03-22

---

## What This Folder Is

This folder contains the complete operationalized extraction of a Claude conversation about building an FDN-based health transformation methodology. Every file here was built by following the BDE protocol on that conversation.

**End goal:** A complete practitioner methodology with an interactive visual diagram, a nodal reasoning framework, and a written document — all grounded in specific mechanisms, not generalizations.

---

## Start Here

**Step 1.** Open [00-inventory/system-map.md](00-inventory/system-map.md) and read Section 1 through Section 3.
This is the source-of-truth map of everything in the brain dump. Read it before touching anything else.

**Step 2.** Open [01-outcomes/outcome-registry.md](01-outcomes/outcome-registry.md) and identify which outcome you want to work on next.
Each outcome has a classification, a dependency list, and a "Fresh Chat or Chain" indicator.

**Step 3.** Check the outcome's dependencies.
If an outcome shows "Depends on: Outcomes X, Y" → confirm those are complete before proceeding. If NOT complete → go to Step 2 and work on those first.

**Step 4.** Open [01-outcomes/fresh-chat-vs-chain-map.md](01-outcomes/fresh-chat-vs-chain-map.md) and find your outcome.
If it says CHAIN → continue in this conversation or the conversation where the source research happened. If it says FRESH CHAT → go to Step 5.

**Step 5 (Fresh Chat only).** Open [02-reverse-engineered/](02-reverse-engineered/) and find the execution plan for your outcome.
The execution plan tells you the exact steps, decision tree, and handoff prompt to use.

**Step 6 (Fresh Chat only).** Open [03-templates/fresh-chat-prompt-template.md](03-templates/fresh-chat-prompt-template.md).
Fill in the template using the handoff prompt at the bottom of the execution plan from Step 5. Paste the assembled prompt into a new conversation.

**Step 7 (Research tasks).** For any marker research task, open [03-templates/marker-upstream-map-template.md](03-templates/marker-upstream-map-template.md).
Use this template for every marker file produced. Do not skip the validation checklist at the bottom.

**Step 8 (Build tasks — HTML).** For any HTML widget build, open [03-templates/html-widget-spec-template.md](03-templates/html-widget-spec-template.md).
Use the design system and component specs defined there. All HTML widgets must follow this spec.

**Step 9.** When a task produces output files, save them to the correct location.
If it's a research file → `02-reverse-engineered/[cluster-name]/`. If it's a completed deliverable → `bd-extraction/deliverables/` (create this folder when needed).

**Step 10.** Update the status header in the execution plan file for the outcome you just completed.
Change `NOT STARTED` to `COMPLETE` and list the output files produced.

---

## Decision Points

**The output file I need doesn't exist yet.**
→ Go to Step 2. Find what produces that file. Work on that outcome first.

**I'm not sure which outcome to work on next.**
→ Open [01-outcomes/fresh-chat-vs-chain-map.md](01-outcomes/fresh-chat-vs-chain-map.md) and follow the "Execution Order Recommendation" at the bottom of that file. Phase 1 items can be started immediately.

**The research for a marker cluster is too large for one chat.**
→ Open [02-reverse-engineered/marker-research-execution-plan.md](02-reverse-engineered/marker-research-execution-plan.md) and find the cluster split table. Use one fresh chat per cluster row.

**I found a mechanism I'm not sure about.**
→ Do NOT guess. Flag it as a research gap. Open [04-meta-system/system-integrity-rules.md](04-meta-system/system-integrity-rules.md) Rule 05 for the exact protocol.

**I want to build the HTML visual map but not all marker research is done.**
→ Stop. Open [04-meta-system/orchestration-spec.md](04-meta-system/orchestration-spec.md) Rule S1. The HTML build is gated on all upstream maps being complete. Complete the research first.

**I want to understand how all the files connect.**
→ Open [04-meta-system/orchestration-spec.md](04-meta-system/orchestration-spec.md) and read the Component Map and Sequencing Rules sections.

---

## Recommended First Session (Phase 1)

These three outcomes can be completed by chaining from the existing conversation — no new research needed:

1. **Outcome 06 — Vitamin A Axis Reference** → chain from existing conversation → save to `deliverables/vitamin-a-reference.md`
2. **Outcome 03 — SIgA Axis Reference** → chain from existing conversation → save to `deliverables/siga-axis-reference.md`
3. **Outcome 04 — Cortisol/DHEA Reference** → chain from existing conversation → save to `deliverables/cortisol-dhea-reference.md`

After these three are complete, Phase 1 research is done and Phase 2 (fresh chats for remaining clusters) can begin.

---

## Folder Index

| Folder / File | What It Contains |
|---|---|
| [00-inventory/system-map.md](00-inventory/system-map.md) | Complete inventory of all entities, mechanisms, and relationships in the brain dump |
| [01-outcomes/outcome-registry.md](01-outcomes/outcome-registry.md) | All 8 outcomes with classifications, layers, and dependency maps |
| [01-outcomes/fresh-chat-vs-chain-map.md](01-outcomes/fresh-chat-vs-chain-map.md) | Routing decision for each outcome + execution order recommendation |
| [02-reverse-engineered/visual-map-execution-plan.md](02-reverse-engineered/visual-map-execution-plan.md) | Step-by-step plan for building the HTML visual map |
| [02-reverse-engineered/nodal-reasoning-execution-plan.md](02-reverse-engineered/nodal-reasoning-execution-plan.md) | Step-by-step plan for building the nodal reasoning framework |
| [02-reverse-engineered/marker-research-execution-plan.md](02-reverse-engineered/marker-research-execution-plan.md) | Step-by-step plan for all marker cluster research (6 clusters) |
| [02-reverse-engineered/methodology-document-execution-plan.md](02-reverse-engineered/methodology-document-execution-plan.md) | Step-by-step plan for the capstone methodology document |
| [03-templates/marker-upstream-map-template.md](03-templates/marker-upstream-map-template.md) | Template for every marker research file |
| [03-templates/fresh-chat-prompt-template.md](03-templates/fresh-chat-prompt-template.md) | Template for every fresh chat prompt |
| [03-templates/html-widget-spec-template.md](03-templates/html-widget-spec-template.md) | Design system and component specs for all HTML widgets |
| [03-templates/cluster-research-workflow.md](03-templates/cluster-research-workflow.md) | Session protocol for marker cluster research |
| [04-meta-system/approach-selection-decision-tree.md](04-meta-system/approach-selection-decision-tree.md) | How to select the right approach for any sub-task |
| [04-meta-system/parameter-extraction-algorithm.md](04-meta-system/parameter-extraction-algorithm.md) | Universal algorithm for extracting parameters at all layers |
| [04-meta-system/system-integrity-rules.md](04-meta-system/system-integrity-rules.md) | Non-overridable constraints for this project |
| [04-meta-system/orchestration-spec.md](04-meta-system/orchestration-spec.md) | How all components connect; sequencing rules; handoff contracts |
