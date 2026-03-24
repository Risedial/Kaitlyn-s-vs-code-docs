# Fresh Chat vs. Chain Map
**Source:** `01-outcomes/outcome-registry.md`
**Date:** 2026-03-22

---

## Classification Key

- **FRESH CHAT** — Must start a new conversation. Context load is too heavy, scope is too large, or the outcome requires input that must be assembled first and pasted in.
- **CHAIN** — Can continue in an existing conversation. All source material is present; the task is elaboration or structuring of what was already discussed.

---

## Classifications

### CHAIN — Execute in Current or Resumed Conversation

| Outcome | Reasoning |
|---|---|
| **03 — SIgA Axis Complete Reference** | All 7 nodes fully detailed in conversation. Task is structuring + adding intervention logic. No new research needed. |
| **04 — Cortisol/DHEA Ratio Reference** | Core axis fully present. Two sub-mechanisms (progesterone steal, IDO elaboration) need expansion but can be requested inline. |
| **06 — Vitamin A Axis Reference** | Fully detailed in conversation. Sources, conversion constraints, immune functions all present. Pure structuring task. |

---

### FRESH CHAT — Must Open New Conversation

| Outcome | Reasoning | What Must Be Assembled Before Starting |
|---|---|---|
| **01 — FDN Marker Root Cause Visual Map (Full)** | Requires complete FDN marker panel. HTML build is a large technical task. Combining full research + build in one context is risky. | Complete FDN marker list; upstream maps from Outcome 05; design spec (categories, colors, interactions) |
| **02 — Nodal Reasoning Framework** | Decision tree logic requires all marker maps as input. Cannot reason about cross-marker patterns without complete single-marker maps. | Outcomes 01 and 05 complete; list of overlapping nodes across markers |
| **05 — Full FDN Panel Upstream Maps** | FDN panel not fully enumerated in conversation. Requires external sourcing. Should be split by cluster (see below). | FDN marker list by panel cluster; research context per cluster |
| **07 — Neurotransmitter Root Cause Map** | IDO/kynurenine and HPHPA pathways only stated, not elaborated. Need OAT marker list. Requires dedicated research. | OAT marker list; kynurenine pathway elaboration; HPHPA mechanism detail |
| **08 — Methodology Document** | Capstone. Requires all other outcomes complete. Writing a coherent framework from incomplete parts produces a worse document. | All outcomes 01–07 complete and reviewed |

---

## Split Recommendation for Outcome 05

Outcome 05 (Full FDN Panel Upstream Maps) is too large for one fresh chat. Split by marker cluster:

| Cluster | Markers (typical FDN panel) | Recommended Approach |
|---|---|---|
| **05a — Adrenal** | Cortisol (x4), DHEA | Chain from Outcome 04 conversation |
| **05b — Sex Hormone** | Estrogen, progesterone, testosterone, LH/FSH | Fresh chat; estrobolome + progesterone steal context needed |
| **05c — Thyroid** | TSH, free T4, free T3, reverse T3, TPO antibodies | Fresh chat; thyroid-HPA interaction context |
| **05d — Gut** | SIgA, zonulin, calprotectin, LPS antibodies, candida | Chain from Outcome 03 conversation |
| **05e — Metabolic / Oxidative** | 8-OHdG, lipid peroxides, antioxidant capacity, CBC, metabolic panel | Fresh chat |
| **05f — Neurotransmitter (OAT)** | Kynurenine, HPHPA, serotonin metabolites, dopamine metabolites | Fresh chat; requires Outcome 07 complete first |

---

## Execution Order Recommendation

```
Phase 1 (Chain — can do now):
  → Outcome 06: Vitamin A Reference
  → Outcome 03: SIgA Axis Reference
  → Outcome 04: Cortisol/DHEA Reference
  → Outcome 05a: Adrenal cluster (chain from 04)
  → Outcome 05d: Gut cluster (chain from 03)

Phase 2 (Fresh Chats — need assembly):
  → Outcome 07: Neurotransmitter Map
  → Outcome 05b: Sex Hormone cluster
  → Outcome 05c: Thyroid cluster
  → Outcome 05e: Metabolic/Oxidative cluster
  → Outcome 05f: Neurotransmitter OAT cluster (after 07)

Phase 3 (Final Builds — after all research complete):
  → Outcome 01: Full Visual Map HTML
  → Outcome 02: Nodal Reasoning Framework
  → Outcome 08: Methodology Document
```
