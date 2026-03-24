# Approach Selection Decision Tree
**Purpose:** Autonomously select the best approach for any sub-task in the FDN methodology project
**Date:** 2026-03-22

---

## Input Variables

Before selecting an approach, identify:

| Variable | Options | How to Determine |
|---|---|---|
| **Task type** | Research / Build / Synthesize / Document | What is the primary activity? |
| **Source availability** | All present / Partial / None | Are all required inputs already in files? |
| **Scope** | Single marker / Cluster / Cross-system / Full framework | How many markers or systems does this task touch? |
| **Context load** | Low (<5 files) / Medium (5–15 files) / High (>15 files) | How many files must be read to execute? |
| **Output format** | HTML / Markdown / Decision framework | What is the target artifact? |
| **Prior work exists?** | Yes / No | Has this or a similar task been partially done? |

---

## Decision Tree

```
START: What is this task?
│
├── RESEARCH (upstream map for a marker or mechanism)
│   │
│   ├── Is all source material present in existing files?
│   │     YES → CHAIN: add to current conversation
│   │     NO  → FRESH CHAT: assemble inputs first
│   │
│   ├── Does this cover ≤ 1 marker cluster?
│   │     YES → Single cluster fresh chat
│   │     NO  → Split: one fresh chat per cluster
│   │
│   └── Does prior research on a related cluster exist?
│         YES → Include that cluster's summary in READ FIRST
│         NO  → Proceed without it
│
├── BUILD (HTML widget, decision framework document)
│   │
│   ├── Is all research complete for this build?
│   │     NO  → DO NOT BUILD YET: complete research first
│   │     YES → Proceed
│   │
│   ├── Is the output a single HTML file?
│   │     YES → Use html-widget-spec-template.md; fresh chat
│   │     NO  → Use fresh-chat-prompt-template.md; fresh chat
│   │
│   └── Is the build context-heavy (>15 input files)?
│         YES → Split: "data layer" chat first, then "render layer" chat
│         NO  → Single fresh chat
│
├── SYNTHESIZE (nodal reasoning, pattern logic, methodology)
│   │
│   ├── Are all input research files complete?
│   │     NO  → DO NOT SYNTHESIZE: complete research first
│   │     YES → Proceed
│   │
│   ├── Does this require reading > 20 input files?
│   │     YES → Build node-overlap-matrix.md first in a separate fresh chat
│   │           Then synthesize in a new fresh chat using the matrix as input
│   │     NO  → Single fresh chat
│   │
│   └── Does the synthesis require external validation (case walkthroughs)?
│         YES → Include 3 validation cases in the same fresh chat
│         NO  → Proceed without cases
│
└── DOCUMENT (reference guides, methodology document)
    │
    ├── Is this a sub-reference (single marker, single mechanism)?
    │     YES → CHAIN: can add to current conversation
    │     NO  → FRESH CHAT
    │
    ├── Is this the capstone methodology document (Outcome 08)?
    │     YES → Gate: all other outcomes must be complete first
    │     NO  → Proceed
    │
    └── Is the audience defined?
          NO  → Resolve audience before writing any content
          YES → Proceed
```

---

## Output Path by Approach

| Approach Selected | Output Location | Template to Use |
|---|---|---|
| Chain research | Current conversation | `marker-upstream-map-template.md` |
| Fresh chat research (single cluster) | `02-reverse-engineered/[cluster]/` | `cluster-research-workflow.md` + `fresh-chat-prompt-template.md` |
| Fresh chat build (HTML) | `deliverables/` | `html-widget-spec-template.md` + `fresh-chat-prompt-template.md` |
| Fresh chat synthesize | `deliverables/` | `fresh-chat-prompt-template.md` |
| Chain document | Current conversation | `marker-upstream-map-template.md` |
| Fresh chat document | `deliverables/` | `fresh-chat-prompt-template.md` |

---

## Override Conditions

The following conditions override the decision tree and require a stop:

| Condition | Action |
|---|---|
| Required input file is missing | STOP. Create the missing file first. Do not proceed with assumptions. |
| Research gap flagged in upstream map | STOP. Resolve gap before building from that map. |
| Audience undefined for a document task | STOP. Clarify audience before writing. |
| Case walkthrough fails validation | STOP. Fix the decision rule. Do not finalize with a known failure. |
| Context window approaching limit mid-task | STOP. Output intermediate artifact. Note resume point. |
