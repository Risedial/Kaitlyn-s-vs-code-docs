# Outcome Registry
**Source:** `00-inventory/system-map.md` + `raw context/claude conversation.md`
**Date:** 2026-03-22

---

## Outcome 01 — Complete FDN Marker Root Cause Visual Map

**Precise Name:** Interactive HTML diagram mapping every FDN lab marker to its upstream root causes, organized by failure category

**Classification:** Deliverable (interactive HTML artifact)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: each marker is a terminal output of a multi-node pathway; root causes must be categorized by mechanism type, not just listed |
| meta | Component roles: FDN markers as terminal outputs; root cause categories as the organizing taxonomy; color-coded pill system for visual scanning; filter logic for cross-cutting patterns |
| macro | Outcome: practitioner can look at any FDN marker and immediately see all plausible upstream failure nodes, organized by category |
| micro | Per-marker: list all root causes; assign each to a category (Nutrient/Mineral, Hormonal/HPA, Neurotransmitter, Microbiome/Gut, Structural/Barrier, Immune, Metabolic); implement in interactive HTML |
| micro-micro | Pill parameters: label text, category color, click behavior; filter parameters: category name, toggle state; marker parameters: name, description, failure node count |

**Dependencies:**
- Requires: Complete FDN marker list (not fully enumerated in conversation — needs external source or practitioner knowledge)
- Requires: Root cause taxonomy (7 categories — defined in conversation)
- Requires: Mechanism research per marker (SIgA and Cortisol/DHEA fully researched; others implied but not detailed)
- Depends on: Outcomes 04 (nodal reasoning) and 05 (upstream stressor maps) to populate remaining markers

**Fresh chat or chain:** FRESH CHAT — context-heavy HTML build; requires complete marker list as input; best executed as dedicated prompt after research is complete

---

## Outcome 02 — Nodal Reasoning Framework

**Precise Name:** Clinical decision framework for localizing dysfunction by reading patterns across multiple FDN markers rather than interpreting each marker in isolation

**Classification:** System (clinical reasoning methodology)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: same marker value (e.g. low SIgA) can originate from different failed nodes with different intervention implications; pattern reading is the diagnostic act, not single-marker reading |
| meta | Components: marker pattern inputs → node probability mapping → ranked intervention targets; the framework must distinguish between markers that share upstream nodes |
| macro | Outcome: practitioner receives a prioritized list of most likely compromised nodes given the full pattern of findings across all markers |
| micro | Per-marker-combination: define which node is most implicated when markers X and Y are both abnormal vs. only X vs. only Y |
| micro-micro | Variables: cortisol level, DHEA level, SIgA level, OAT metabolite levels, sex hormone levels; conditions: "If cortisol high AND DHEA low AND SIgA low → pIgR suppression most likely proximal cause" |

**Dependencies:**
- Requires: Outcome 01 (complete marker-to-root-cause map)
- Requires: Outcome 05 (upstream stressor maps per marker)
- Requires: Logic for node overlap (which nodes are shared across multiple markers)

**Fresh chat or chain:** FRESH CHAT — requires complete marker map as context; decision tree logic is complex enough to warrant dedicated build prompt

---

## Outcome 03 — SIgA Axis Complete Reference

**Precise Name:** Structured reference document for the 7-node SIgA production axis with all upstream variables at each node

**Classification:** System (reference document + educational content)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: SIgA is sensitive but non-specific; the value of the document is in localizing which node is most likely failed given the clinical context |
| meta | Components: node sequence (1–7); upstream vulnerability per node; FDN-relevant stressor mapping per node; clinical pattern matching |
| macro | Outcome: practitioner can trace low SIgA to most probable upstream failure given the full clinical picture |
| micro | Per node: name, function, upstream vulnerabilities, FDN stressor category, clinical indicators, intervention implications |
| micro-micro | Node 6 (pIgR): cortisol threshold for suppression; Node 2 (class switching): retinoic acid, TGF-β, APRIL, BAFF; Node 3 (homing): α4β7, CCR9, retinoic acid dependency; Node 5 (plasma cell output): mitochondrial demand, oxidative stress vulnerability |

**Dependencies:**
- Requires: Conversation content (fully present)
- Depends on: Outcome 06 (Vitamin A reference) for Node 2 and Node 3 detail
- Depends on: Outcome 07 (HPA/cortisol reference) for Node 6 detail

**Fresh chat or chain:** CAN CHAIN — all source material present in conversation

---

## Outcome 04 — Cortisol/DHEA Ratio Complete Reference

**Precise Name:** Structured reference for the cortisol/DHEA ratio — upstream inputs, HPA mechanics, three ratio patterns, downstream consequences, and intervention differentiation logic

**Classification:** System (reference document + intervention logic)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: ratio must be interpreted by pattern (which component is elevated/depleted) not just as a single number; same ratio value can require opposite interventions |
| meta | Components: upstream stressor inputs (7+ categories) → HPA axis mechanics → three ratio patterns → downstream consequence cascade → intervention logic per pattern |
| macro | Outcome: practitioner can read the ratio pattern and reason toward both proximal mechanism AND upstream stressor cluster |
| micro | Three patterns: (1) high cortisol/low DHEA → load reduction + adrenal support; (2) low cortisol/low DHEA → cautious approach, feedback suppressed; (3) oscillating → pattern instability, may indicate phase transition |
| micro-micro | Feedback loops: gut permeability → HPA load; blood sugar instability → HPA load; neurotransmitter depletion → stress resilience impairment → HPA load; progesterone steal → sex hormone cascade disruption |

**Dependencies:**
- Requires: Conversation content (substantially present)
- Requires: Progesterone steal mechanism detail (stated but not fully elaborated)
- Requires: IDO → kynurenine shunting detail (stated, needs expansion)

**Fresh chat or chain:** CAN CHAIN — core content present; elaboration needed on two sub-mechanisms

---

## Outcome 05 — Upstream Stressor Map Per FDN Marker (Full Panel)

**Precise Name:** Exhaustive upstream stressor maps for the complete FDN lab marker panel, covering markers not yet detailed in the conversation

**Classification:** System (research + documentation set)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: each marker gets the same treatment as SIgA — a multi-node pathway analysis, not a simple list of causes |
| meta | Components: complete FDN marker list (to be sourced); research protocol per marker; root cause taxonomy applied consistently |
| macro | Outcome: every FDN marker has a structured upstream map; collective maps populate Outcome 01 |
| micro | Per marker: identify all nodes in the production/regulation pathway; identify which nodes are vulnerable to which FDN-relevant stressors; map to root cause categories |
| micro-micro | For each node: upstream inputs; stressor threshold (when does this node fail?); FDN marker correlates; intervention implications |

**Dependencies:**
- Requires: Complete FDN marker panel list (NOT fully present in conversation — needs sourcing)
- Builds on: SIgA and Cortisol/DHEA as templates
- Feeds into: Outcome 01 and Outcome 02

**Fresh chat or chain:** FRESH CHAT — requires external FDN marker list; large scope; best split by marker cluster (adrenal panel, sex hormone panel, thyroid panel, gut panel, metabolic panel, neurotransmitter panel)

---

## Outcome 06 — Vitamin A Axis Reference

**Precise Name:** Reference document for vitamin A's role as a cross-systemic immune regulator — sources, conversion constraints, failure modes, and intervention logic

**Classification:** Process (sub-reference feeding into Outcomes 01, 03, 05)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: vitamin A deficiency is immune disorganization, not simple immunosuppression; effects are bidirectional (suppression + inappropriate activation) |
| meta | Components: retinol sources → absorption pathway → conversion pathway → active form (retinoic acid) → five immune functions → hidden deficiency risk factors |
| macro | Outcome: practitioner can identify hidden vitamin A insufficiency and understand its multi-system immune consequences |
| micro | Five functions: (1) epithelial barrier, (2) IgA class switching + homing, (3) Treg induction, (4) Th1/Th17 balance, (5) innate immune maturation |
| micro-micro | BCMO1 polymorphism impact; bile/lipase absorption dependency; self-reinforcing deficiency loop; animal vs. plant source comparison; food list with relative potency |

**Dependencies:**
- Fully present in conversation
- Feeds into: Outcome 01, 03, 05

**Fresh chat or chain:** CAN CHAIN

---

## Outcome 07 — Neurotransmitter Root Cause Map (IDO/Kynurenine + HPHPA/Dopamine)

**Precise Name:** Reference document for the two key microbially-mediated neurotransmitter disruption pathways identified in the conversation

**Classification:** System (mechanistic reference)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: these are mechanistically specific pathways, not metaphorical "gut-brain connections" — microbial metabolites compete at enzyme level |
| meta | Components: IDO pathway (cortisol-driven); Clostridia/HPHPA pathway (dysbiosis-driven); convergence with FDN neurotransmitter markers (OAT) |
| macro | Outcome: practitioner understands how gut status and HPA status directly produce neurotransmitter dysfunction |
| micro | IDO: cortisol → IDO activation → tryptophan → kynurenine (not serotonin) → neuroinflammatory metabolites; HPHPA: Clostridia overgrowth → HPHPA → dopamine pathway enzyme competition |
| micro-micro | OAT markers that reflect each pathway; intervention targets per pathway; distinguishing features (which pattern predominates?) |

**Dependencies:**
- Partially present in conversation (stated but not elaborated)
- Requires: OAT marker list for kynurenine and HPHPA — needs sourcing or elaboration
- Feeds into: Outcome 01, 05

**Fresh chat or chain:** FRESH CHAT — needs elaboration beyond what's in conversation

---

## Outcome 08 — Methodology Document (Integration Layer)

**Precise Name:** Written methodology for the health transformation framework — how FDN's multi-marker approach, the nodal reasoning layer, and the mechanistic physiology integrate into a coherent practitioner tool

**Classification:** Deliverable (written framework document)

**Five Layers:**
| Layer | Content |
|---|---|
| meta-meta | Governing rule: the methodology must be both mechanistically credible and practically executable; it extends FDN rather than replacing it |
| meta | Components: FDN foundation (markers + HIDDEN stressors) + nodal reasoning layer (Outcome 02) + mechanistic reference library (Outcomes 03–07) + visual tool (Outcome 01) |
| macro | Outcome: complete practitioner-facing methodology document |
| micro | Sections: FDN baseline, what's missing, the nodal reasoning extension, how to use the visual map, marker pattern examples, intervention logic |
| micro-micro | Audience: FDN-trained practitioners; tone: clinically precise; format: TBD (written document, course module, reference guide?) |

**Dependencies:**
- Requires: All other outcomes complete
- Requires: Clarity on audience and format (not specified in conversation)

**Fresh chat or chain:** FRESH CHAT — capstone deliverable; all inputs must exist first

---

## Outcome Summary Table

| # | Name | Type | Fresh Chat? | Deps |
|---|---|---|---|---|
| 01 | FDN Marker Root Cause Visual Map | Deliverable (HTML) | YES | 04, 05 |
| 02 | Nodal Reasoning Framework | System | YES | 01, 05 |
| 03 | SIgA Axis Complete Reference | System | NO (chain) | 06, 07 |
| 04 | Cortisol/DHEA Ratio Reference | System | NO (chain) | — |
| 05 | Full FDN Panel Upstream Maps | System | YES (by cluster) | External FDN marker list |
| 06 | Vitamin A Axis Reference | Process | NO (chain) | — |
| 07 | Neurotransmitter Root Cause Map | System | YES | OAT marker list |
| 08 | Methodology Document | Deliverable (written) | YES | 01–07 all complete |
