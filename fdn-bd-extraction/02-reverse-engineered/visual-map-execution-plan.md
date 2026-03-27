# Execution Plan: FDN Marker Root Cause Visual Map (Outcome 01)
**Cluster:** Visual Artifact Build
**Date:** 2026-03-22
**Requires:** Fresh Chat

---

## Minimum Context to Execute

1. Complete FDN lab marker list (all panels)
2. Root cause taxonomy (7 categories — defined)
3. Per-marker upstream maps (Outcomes 03–07 complete)
4. Design spec (this document)
5. Completed HTML from prior conversation (if extending rather than rebuilding)

---

## Steps in Order

**Step 1 — Source the complete FDN marker list**
- Action: List every marker in standard FDN lab panels (DUTCH, GI Map, OAT, metabolic, immune)
- Decision: If list exceeds 40 markers → group into clusters; if ≤ 40 → handle all in one pass
- Output: `fdn-marker-list.md` in this folder

**Step 2 — Research pass for unresearched markers**
- Action: For each marker NOT covered by Outcomes 03–07, run the upstream map protocol (see `03-templates/marker-upstream-map-template.md`)
- Decision: If a marker's axis is straightforward (one-node) → note it as simple; if multi-node → apply full template
- Output: Individual research files per marker cluster

**Step 3 — Define HTML architecture**
- Structure: Single-file HTML; no external dependencies; works offline
- Components: Marker card grid; expandable detail panels per marker; color-coded root cause pills by category; filter bar (filter by root cause category); search bar
- Color map:
  - Nutrient/Mineral → amber (#F59E0B)
  - Hormonal/HPA → rose (#F43F5E)
  - Neurotransmitter → violet (#8B5CF6)
  - Microbiome/Gut → emerald (#10B981)
  - Structural/Barrier → sky (#0EA5E9)
  - Immune → indigo (#6366F1)
  - Metabolic → orange (#EA580C)

**Step 4 — Build HTML: marker card layer**
- For each marker: name, brief description (1 sentence), count of root cause nodes
- Interaction: click to expand detail panel

**Step 5 — Build HTML: detail panel layer**
- For each expanded marker: root cause pills organized by category; each pill contains mechanism label; hover tooltip with 1-sentence mechanism explanation
- Interaction: clicking a pill fires a question to Claude (format: pre-populated text block)

**Step 6 — Build HTML: filter and search layer**
- Filter bar: toggle buttons per category; active state styling; filtering updates visible markers and pills
- Search bar: filters markers by name

**Step 7 — Validate and export**
- Validator: open in browser; test filter logic; test expansion; test search; confirm all markers present
- Output: single `.html` file in `deliverables/` folder

---

## Decision Tree

```
START
  │
  ├── Do all marker upstream maps exist?
  │     NO → Run Outcomes 03–07 first; return here when complete
  │     YES → Proceed to Step 3
  │
  ├── Is the marker count ≤ 40?
  │     YES → Single HTML build
  │     NO → Group into panels; build expandable panel-level navigation first
  │
  └── Is the prior HTML widget (from conversation) to be extended?
        YES → Load prior HTML; add missing markers; refactor as needed
        NO → Build from scratch using this spec
```

---

## Split Points

- Context limit reached during marker research: split into per-cluster fresh chats (see `01-outcomes/fresh-chat-vs-chain-map.md`)
- Context limit reached during HTML build: split into "data layer" chat (produce JSON data structure) and "render layer" chat (HTML + CSS + JS consuming JSON)

---

## Handoff Prompt for Fresh Chat

```
OPERATING CONTRACT: Build an interactive single-file HTML tool mapping FDN lab markers to upstream root causes.
READ FIRST: [paste contents of fdn-marker-list.md] and [paste all upstream map files]
OUTPUT: A single self-contained HTML file at deliverables/fdn-root-cause-map.html

Architecture:
- Marker card grid with expandable detail panels
- Root cause pills colored by category (7 categories — see color map below)
- Filter bar by category; search bar by marker name
- No external dependencies; works offline

Color map:
- Nutrient/Mineral: #F59E0B
- Hormonal/HPA: #F43F5E
- Neurotransmitter: #8B5CF6
- Microbiome/Gut: #10B981
- Structural/Barrier: #0EA5E9
- Immune: #6366F1
- Metabolic: #EA580C

For each marker provide: name, 1-sentence description, all root cause nodes as pills, category assignment per pill, mechanism tooltip per pill.

Validate: open in browser and confirm all markers, all filters, and all pills render correctly before completing.
```
