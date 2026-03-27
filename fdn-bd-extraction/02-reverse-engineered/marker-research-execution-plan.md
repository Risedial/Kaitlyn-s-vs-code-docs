# Execution Plan: Full FDN Panel Upstream Maps (Outcome 05)
**Cluster:** Research — Per Marker Cluster
**Date:** 2026-03-22
**Requires:** Fresh Chat per cluster (6 clusters)

---

## Minimum Context to Execute Per Cluster

1. The marker upstream map template (`03-templates/marker-upstream-map-template.md`)
2. The FDN marker list for that specific cluster
3. The 7-category root cause taxonomy
4. Any prior research outputs that inform this cluster (e.g., HPA research for sex hormone cluster)

---

## Cluster Sequence and Dependencies

```
Cluster 05a (Adrenal)
  └── Source: Chain from Outcome 04 conversation
  └── Markers: Cortisol x4 (CAR, morning, afternoon, evening), DHEA
  └── Dependencies: None (core content already present in conversation)

Cluster 05d (Gut/Mucosal)
  └── Source: Chain from Outcome 03 conversation
  └── Markers: SIgA, zonulin, calprotectin, LPS/endotoxin antibodies, candida antibodies, beta-glucuronidase
  └── Dependencies: SIgA research complete; others need fresh research

Cluster 05b (Sex Hormone)
  └── Source: Fresh chat
  └── Markers: Estradiol, progesterone, testosterone, SHBG, LH, FSH, DHT (if measured)
  └── Dependencies: Needs progesterone steal mechanism; estrobolome reference; aromatase pathway

Cluster 05c (Thyroid)
  └── Source: Fresh chat
  └── Markers: TSH, free T4, free T3, reverse T3, T3/rT3 ratio, TPO antibodies, TG antibodies
  └── Dependencies: Needs thyroid-HPA crosstalk; selenium/iodine/zinc roles; autoimmune triggers

Cluster 05e (Metabolic/Oxidative)
  └── Source: Fresh chat
  └── Markers: 8-OHdG, lipid peroxides, total antioxidant capacity, CRP, homocysteine, fasting glucose, insulin, HbA1c
  └── Dependencies: Needs mitochondrial function context; blood sugar-HPA axis; methylation

Cluster 05f (Neurotransmitter/OAT)
  └── Source: Fresh chat (after Outcome 07 complete)
  └── Markers: Kynurenate, quinolinate, serotonin metabolites (5-HIAA), dopamine metabolites (HVA, VMA), HPHPA, markers of B6 status (xanthurenate)
  └── Dependencies: Outcome 07 (IDO/kynurenine + HPHPA pathways) must be complete first
```

---

## Steps Per Cluster (Universal Protocol)

**Step 1 — List all markers in this cluster**
- Output: Numbered list with marker name, what it measures, normal range reference

**Step 2 — For each marker: identify the production/regulation pathway**
- Map each marker as a terminal output of a sequence of nodes
- Identify each node's function and its upstream dependencies

**Step 3 — For each node: identify upstream vulnerabilities**
- What FDN-relevant stressor degrades this node?
- Assign to root cause category (7 categories)
- Note: Is this a primary vulnerability or a secondary/contributory one?

**Step 4 — Identify cross-marker shared nodes**
- Which nodes appear in multiple markers within this cluster?
- Which nodes appear in markers from OTHER clusters (cross-cluster links)?
- Flag all cross-cluster links for Outcome 02 (nodal reasoning)

**Step 5 — Write structured upstream map per marker**
- Format: use `03-templates/marker-upstream-map-template.md`
- One file per marker

**Step 6 — Write cluster summary**
- Shared nodes within cluster
- Cross-cluster links
- Top 3 high-leverage nodes in this cluster
- Key clinical patterns (what combinations of markers in this cluster suggest what?)

---

## Decision Tree

```
START
  │
  ├── Is this cluster 05a or 05d?
  │     YES → Chain from existing conversation; skip to Step 2
  │     NO → Open fresh chat with template + marker list
  │
  ├── At Step 2: Is the pathway multi-node (≥ 3 nodes)?
  │     YES → Apply full template
  │     NO → Simplified template; note as straightforward marker
  │
  └── At Step 4: Do cross-cluster links exceed 3?
        YES → Create a cross-cluster link file for that cluster pair
        NO → Note inline in cluster summary
```

---

## Handoff Prompt Template for Cluster Fresh Chats

```
OPERATING CONTRACT: Research and document the upstream root cause map for the FDN [CLUSTER NAME] marker cluster.
READ FIRST: [paste marker-upstream-map-template.md] and [paste 7-category root cause taxonomy]
OUTPUT: One structured markdown file per marker at 02-reverse-engineered/[cluster-name]/[marker-name]-map.md
        One cluster summary at 02-reverse-engineered/[cluster-name]/cluster-summary.md

Markers to cover: [LIST MARKERS]

For each marker:
1. Identify the full production/regulation pathway as a numbered node sequence
2. At each node: list all upstream FDN-relevant vulnerabilities; assign each to a root cause category
3. Flag any nodes shared with markers in other FDN panels
4. Write the output in the template format — no prose paragraphs; tables and bullet lists only

Validate: every marker must have at least 3 distinct root cause nodes before marking complete.
If a marker has fewer than 3 traceable nodes, flag it as "requires additional research" and note what's missing.
```
