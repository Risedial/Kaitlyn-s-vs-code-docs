# Execution Plan: Methodology Document (Outcome 08)
**Cluster:** Capstone Deliverable
**Date:** 2026-03-22
**Requires:** Fresh Chat — ALL prior outcomes complete

---

## Gate Condition

Do not begin this execution plan until:
- [ ] Outcome 01 (Visual Map HTML) — complete
- [ ] Outcome 02 (Nodal Reasoning Framework) — complete
- [ ] Outcome 03 (SIgA Reference) — complete
- [ ] Outcome 04 (Cortisol/DHEA Reference) — complete
- [ ] Outcome 05a–f (All cluster maps) — complete
- [ ] Outcome 06 (Vitamin A Reference) — complete
- [ ] Outcome 07 (Neurotransmitter Map) — complete

---

## Minimum Context to Execute

1. All research outputs (Outcomes 03–07)
2. Nodal reasoning framework (Outcome 02)
3. Visual map (Outcome 01) — as reference, not embedded
4. Clarity on: audience (practitioners? clients? trainees?), format (PDF? web? course module?), length constraints

---

## Steps in Order

**Step 1 — Define audience and format (MUST resolve before writing)**
- Questions to answer:
  - Is this for FDN-certified practitioners, FDN students, or clients?
  - Is the format a reference guide, a course module, or a written methodology paper?
  - Is there a length target?
- Decision: If audience = practitioners → technical language acceptable; If audience = clients → translate to accessible language; If both → write practitioner version first, then create translated version

**Step 2 — Outline the methodology structure**
- Proposed structure:
  1. The FDN Foundation (what FDN already does well; metabolic chaos concept; HIDDEN stressors)
  2. The Extension Problem (what standard FDN doesn't do — nodal reasoning; why same marker can require different interventions)
  3. The Nodal Reasoning Layer (how to read marker patterns; the decision framework)
  4. The Mechanistic Reference Library (how to use the marker maps; organized by system)
  5. The Visual Tool (how to use the HTML map; filter patterns worth knowing)
  6. Clinical Examples (3 case walkthroughs showing the full methodology in action)
  7. Implementation Guide (how to integrate into FDN practice; what requires additional testing; limitations)

**Step 3 — Write each section**
- One section at a time; review before proceeding
- Decision: If a section requires information not in the reference library → flag it; do not guess; note as "research gap"

**Step 4 — Integrate case walkthroughs**
- Minimum 3 cases: one predominantly adrenal, one predominantly gut/mucosal, one compound multi-system
- Each case: presenting markers → pattern reading → node identification → intervention logic → expected trajectory
- Validate: each case must demonstrate the methodology working; not just illustrating what markers are elevated

**Step 5 — Write implementation guide**
- How does a practitioner add this layer to their existing FDN workflow?
- What additional testing does nodal reasoning require vs. standard FDN panel?
- What are the limitations of the framework?

**Step 6 — Review and finalize**
- Check: Is every claim traceable to a mechanism in the reference library?
- Check: Are there any vague generalizations that need to be replaced with specific mechanisms?
- Check: Is the methodology extensible (can a practitioner add new markers and apply the same logic)?

---

## Decision Tree

```
START
  │
  ├── Is audience defined?
  │     NO → Resolve before writing any content
  │     YES → Proceed to outline
  │
  ├── At Step 3: Is there a research gap in any section?
  │     YES → Stop; note the gap; do not fill with speculation
  │     NO → Continue writing
  │
  └── At Step 4: Do case walkthroughs validate the methodology?
        YES → Finalize
        NO → Identify which rule in Outcome 02 failed; revise; rerun cases
```

---

## Handoff Prompt for Fresh Chat

```
OPERATING CONTRACT: Write the health transformation methodology document integrating FDN with mechanistic physiology.
READ FIRST: [paste Outcome 02 nodal reasoning framework] and [paste all cluster summaries from Outcome 05] and [paste Outcomes 03, 04, 06, 07 references]
OUTPUT: methodology-document.md at deliverables/

Audience: [SPECIFY — practitioner / student / client]
Format: [SPECIFY — reference guide / course module / paper]

Structure:
1. FDN Foundation (what it does; metabolic chaos; HIDDEN stressors)
2. The Extension Problem (why nodal reasoning adds value over single-marker reading)
3. Nodal Reasoning Layer (decision framework from Outcome 02)
4. Mechanistic Reference Library (organized by system; reference to marker maps)
5. Visual Tool Usage Guide (how to use the HTML map)
6. Clinical Case Walkthroughs (3 cases; each demonstrating full methodology)
7. Implementation Guide (workflow integration; limitations)

Rules:
- Every claim must trace to a mechanism in the reference library; flag any gaps rather than filling them
- No vague generalizations; replace all "stress weakens immunity" language with specific mechanisms
- Case walkthroughs must demonstrate the methodology working, not just describe what markers mean

Validate: run all 3 cases through Outcome 02 decision framework before finalizing; confirm they route correctly.
```
