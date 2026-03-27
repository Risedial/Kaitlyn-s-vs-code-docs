# Execution Plan: Nodal Reasoning Framework (Outcome 02)
**Cluster:** Clinical Methodology Build
**Date:** 2026-03-22
**Requires:** Fresh Chat (after Outcome 01 complete)

---

## Minimum Context to Execute

1. Complete upstream maps for all FDN markers (Outcomes 03–07)
2. List of shared nodes across markers (nodes that appear in multiple marker pathways)
3. FDN marker panel organized by clinical cluster

---

## Steps in Order

**Step 1 — Map overlapping nodes**
- Action: For every node in every marker's upstream map, list which OTHER markers share that node
- Example: pIgR suppression by cortisol → appears in SIgA AND (implicitly) gut barrier integrity; cortisol → appears in SIgA, sex hormones, neurotransmitters, thyroid
- Output: `node-overlap-matrix.md` — rows: nodes; columns: markers; cells: Y/N

**Step 2 — Identify high-leverage nodes**
- Definition: Any node that appears in ≥ 3 marker pathways = high-leverage node
- Action: Sort node-overlap matrix by row sum (descending)
- Output: Ranked list of high-leverage nodes

**Step 3 — Build pattern logic**
- For each high-leverage node: define the marker signature that indicates this node is the primary failure point
- Format: "If [Marker A is abnormal] AND [Marker B is abnormal] AND [Marker C is normal] → Node X is most likely compromised"
- Decision: If marker pattern points to two nodes equally → flag as "co-failure" case; note both

**Step 4 — Build the decision framework document**
- Structure:
  1. Single-marker interpretation (baseline — what each marker means in isolation)
  2. Multi-marker pattern rules (when to elevate a node from "possible" to "probable")
  3. High-leverage node profiles (full description of each top-tier node; all markers it affects; intervention implications)
  4. Example case walkthroughs (3 minimum: one clear pattern, one ambiguous, one compound failure)

**Step 5 — Build intervention logic**
- For each high-leverage node: identify the intervention target that most directly addresses it
- Distinguish: proximal intervention (addresses the node directly) vs. upstream intervention (removes the stressor loading that node)
- Output: Per-node intervention profile

**Step 6 — Validate against known cases**
- Action: Run 2–3 hypothetical clinical presentations through the decision framework
- Check: Does the framework route correctly? Are there any false certainties?
- Decision: If framework misfires on a case → identify the rule that failed; revise Step 3 rules

---

## Decision Tree

```
START
  │
  ├── Are all upstream maps complete?
  │     NO → Complete Outcomes 03–07 first
  │     YES → Build node-overlap matrix (Step 1)
  │
  ├── After Step 1: Are there high-leverage nodes with ≥ 5 markers?
  │     YES → These are priority nodes; start case walkthroughs with these first
  │     NO → Proceed with ≥ 3 threshold
  │
  └── Does the framework produce ambiguous patterns for compound failures?
        YES → Flag as "requires clinical judgment"; note the ambiguity explicitly
        NO → Finalize as decision rules
```

---

## Split Points

- Node-overlap matrix is too large for one context → split by node category (hormonal nodes first; then nutritional; then structural)
- Case walkthrough reveals missing research → open new fresh chat to research that gap

---

## Handoff Prompt for Fresh Chat

```
OPERATING CONTRACT: Build a clinical nodal reasoning framework for FDN practitioners.
READ FIRST: [paste all upstream map files — Outcomes 03–07 outputs] and [paste node-overlap-matrix.md]
OUTPUT: nodal-reasoning-framework.md at deliverables/

This framework enables practitioners to read patterns across multiple FDN markers to identify which specific upstream node is most likely compromised — rather than interpreting each marker in isolation.

Build in this order:
1. Identify all nodes that appear in ≥ 3 marker pathways ("high-leverage nodes")
2. For each high-leverage node: define the marker signature that indicates it as the primary failure
3. Build decision rules: "If [marker A abnormal] + [marker B abnormal] + [marker C normal] → Node X probable"
4. For each node: define proximal intervention + upstream stressor intervention
5. Write 3 case walkthroughs to validate the rules

Format: structured markdown with decision tables, not prose paragraphs.
Validate: each case walkthrough must route to a specific node recommendation before marking complete.
```
