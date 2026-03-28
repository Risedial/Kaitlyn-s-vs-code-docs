# Orchestration Specification
**Purpose:** How all components connect; sequencing rules; handoff contracts; audit trail conventions
**Date:** 2026-03-22

---

## Component Map

```
bd-extraction/
│
├── 00-inventory/
│   └── system-map.md                    ← Source of truth: all entities, all relationships
│
├── 01-outcomes/
│   ├── outcome-registry.md              ← All outcomes, classified and dependency-mapped
│   └── fresh-chat-vs-chain-map.md       ← Execution routing for each outcome
│
├── 02-reverse-engineered/
│   ├── visual-map-execution-plan.md     ← How to build Outcome 01
│   ├── nodal-reasoning-execution-plan.md← How to build Outcome 02
│   ├── marker-research-execution-plan.md← How to execute Outcome 05 (all clusters)
│   ├── methodology-document-execution-plan.md ← How to build Outcome 08
│   └── [cluster-name]/                  ← Created during Outcome 05 research sessions
│       ├── [marker]-map.md
│       └── cluster-summary.md
│
├── 03-templates/
│   ├── marker-upstream-map-template.md  ← Reusable template for every marker research file
│   ├── fresh-chat-prompt-template.md    ← Reusable template for every fresh chat prompt
│   ├── html-widget-spec-template.md     ← Architecture spec for all HTML widgets
│   └── cluster-research-workflow.md     ← Session protocol for cluster research
│
├── 04-meta-system/
│   ├── approach-selection-decision-tree.md ← How to choose approach for any sub-task
│   ├── parameter-extraction-algorithm.md   ← How to extract parameters at all layers
│   ├── system-integrity-rules.md           ← Non-overridable constraints
│   └── orchestration-spec.md               ← This file
│
└── README.md                            ← Entry point; numbered steps; no interpretation required
```

---

## Sequencing Rules

### Rule S1 — Gate Enforcement

Each phase only begins when its gate condition is met:

| Phase | Gate Condition | Gate File |
|---|---|---|
| Phase 1 Research | system-map.md exists | `00-inventory/system-map.md` |
| Phase 2 Build (Outcome 01) | All upstream maps complete | All cluster summary files exist |
| Phase 3 Synthesis (Outcome 02) | Outcome 01 complete AND node-overlap-matrix.md exists | `deliverables/node-overlap-matrix.md` |
| Capstone (Outcome 08) | All Outcomes 01–07 complete | All deliverable files confirmed |

### Rule S2 — No Forward Skip

Tasks must be completed in dependency order. If Task B depends on Task A, Task B cannot begin regardless of how urgent Task B is.

Exception: CHAIN tasks can run in parallel with each other if they have no shared dependencies.

### Rule S3 — Handoff Contract

Every completed task must produce a file. A task is not complete if it exists only in a conversation. All outputs must be saved as files before the task is marked done.

Handoff format for research tasks:
```
HANDOFF COMPLETE
Task: [Outcome #] — [Name]
Output files: [list exact paths]
Research gaps flagged: [Y/N — if Y, list them]
Next task unlocked: [Outcome # that can now proceed]
```

---

## Handoff Contracts Per Outcome

### Outcome 03 → feeds into Outcome 01 and 05d
- Handoff: `deliverables/siga-axis-reference.md` exists
- Research gaps: resolved or explicitly flagged
- Unlocks: 05d cluster research; SIgA entry in Outcome 01

### Outcome 04 → feeds into Outcome 01 and 05a
- Handoff: `deliverables/cortisol-dhea-reference.md` exists
- Unlocks: 05a cluster research; Cortisol/DHEA entry in Outcome 01

### Outcome 05 (all clusters) → feeds into Outcome 01 and 02
- Handoff: All cluster summary files exist in `02-reverse-engineered/[cluster]/`
- Unlocks: `node-overlap-matrix.md` can be built; Outcome 01 HTML build can be completed

### Outcome 06 → feeds into Outcome 01 and 03
- Handoff: `deliverables/vitamin-a-reference.md` exists
- Unlocks: Vitamin A entries in Outcome 01; Node 2 and Node 3 detail in SIgA reference

### Outcome 07 → feeds into Outcome 01 and 05f
- Handoff: `deliverables/neurotransmitter-rootcause-map.md` exists
- Unlocks: 05f cluster research; OAT neurotransmitter entries in Outcome 01

### Outcome 01 → feeds into Outcome 02
- Handoff: `deliverables/fdn-root-cause-map.html` exists and validated
- Unlocks: Outcome 02 build

### Outcome 02 → feeds into Outcome 08
- Handoff: `deliverables/nodal-reasoning-framework.md` exists and validated (case walkthroughs pass)
- Unlocks: Outcome 08 build

---

## Deliverables Folder

All completed build artifacts go to:
```
bd-extraction/deliverables/
  siga-axis-reference.md
  cortisol-dhea-reference.md
  vitamin-a-reference.md
  neurotransmitter-rootcause-map.md
  fdn-root-cause-map.html
  node-overlap-matrix.md
  nodal-reasoning-framework.md
  methodology-document.md
```

This folder does not exist yet — it is created when the first completed deliverable is saved.

---

## Audit Trail Conventions

### File Status Tracking

Each execution plan file (in `02-reverse-engineered/`) maintains a status header:

```markdown
**Status:** NOT STARTED / IN PROGRESS / BLOCKED (reason) / COMPLETE
**Last updated:** YYYY-MM-DD
**Output files produced:** [list or "none yet"]
**Research gaps open:** [list or "none"]
```

Update this header after each work session.

### Research Gap Registry

Any research gap flagged during any task is added to:
`04-meta-system/research-gap-registry.md`

Format:
```
| Gap ID | Task Source | What Is Missing | Resolution Path | Status |
```

Create this file when the first gap is identified.

---

## Cross-Cluster Link Registry

When a node appears in multiple cluster summaries, add it to:
`04-meta-system/cross-cluster-link-registry.md`

Format:
```
| Node Name | Cluster A | Cluster B | Cluster C | Cross-Cluster Implication |
```

Create this file during Outcome 05 research. It is a required input for Outcome 02.
