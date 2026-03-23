# Session Output — Problem Framing
**Date:** 2026-03-22
**Phase:** problem_framing → variable_discovery

---

## Research Question

For every FDN lab marker in the standard panel, what are the complete bidirectional connections — specifically: (1) every symptom that marker's dysfunction produces and the specific physiological mechanism linking them, (2) every upstream root cause that drives that marker abnormal and its mechanism, and (3) every other FDN marker that shares upstream nodes — such that any input combination of symptoms and lab findings can be traced to the most probable root cause cluster?

---

## User Clarification Answers

**Q1 — Output format:** D — Multiple documents (research document + knowledge map + JSON profile)

**Q2 — Research lens:** A — First-principles / systems thinking — structural relationships only

**Q3 — Cross-domain openness:** A — Yes — include cross-domain findings if the structural connection is confirmed

**Q4 — Research scope:** A — Broad survey — identify as many variables as possible

**Q5 — Exclusions:** A — None — include everything above minimum confidence

---

## User Context (Additional)

The research target is a full bidirectional symptom-marker-root-cause web anchored to the FDN lab marker panel. Every node in the web — whether a symptom, an FDN lab marker, a root cause category, or a physiological mechanism — should connect to every other node it has a structural causal relationship with, in any direction.

**A single unit of research output is a node entry with:**
1. Which symptoms this marker produces when abnormal — with the specific mechanism for each
2. Which upstream root causes drive this marker abnormal — with their mechanisms
3. Which other FDN markers share upstream nodes with this one

**End goal — three-layer system:**
1. Reference library of all node entries
2. Clinical reasoning framework where a practitioner can input any combination of symptoms and lab findings and trace to the most probable root cause cluster
3. Interactive visual tool where the user enters multiple symptoms and markers simultaneously and the tool identifies the most probable root cause cluster

**Design constraint:** Every connection must include a specific physiological mechanism — no vague correlations.

---

## Populated user_lens_profile

```json
{
  "approved_perspectives": ["first_principles_systems_thinking"],
  "excluded_methodologies": [],
  "open_to_cross_domain": true,
  "minimum_confidence_band": "relevant",
  "output_format": "multiple_documents",
  "research_scope": "broad_survey"
}
```

---

## Next Phase

Variable Discovery — identify all FDN lab markers (primary nodes), all symptom categories they connect to, all root cause categories that drive them, and any bridging physiological mechanisms that function as independent nodes.
