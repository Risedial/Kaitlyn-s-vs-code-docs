# Template: Fresh Chat Prompt
**Version:** 1.0 — 2026-03-22
**Use for:** Any task that requires a new conversation (see `01-outcomes/fresh-chat-vs-chain-map.md`)

---

## Instructions

Replace all `[BRACKETED PLACEHOLDERS]` with task-specific content.
This template satisfies all Prompt Engineering Gates from the BDE operating contract.

---

## TEMPLATE

```
OPERATING CONTRACT: [State the task in 1–2 sentences. What is being built? What is the output?]
This prompt is self-contained. Read every file listed below before acting.

READ FIRST (in this order):
1. [File path or pasted content — label clearly]
2. [File path or pasted content]
3. [File path or pasted content]
[Add as many as needed — do not proceed if any file is missing]

TASK:
[Describe the task with enough specificity that zero interpretation is required.
Use numbered steps if the task has sequence.
Use decision rules if the task involves branching logic.]

OUTPUT FILES (create exactly these, no more, no less):
- [exact/path/filename.md] — [what this file contains]
- [exact/path/filename.html] — [what this file contains]
[List every output artifact]

CONSTRAINTS:
- [Any non-negotiable rules — format, style, length, dependencies]
- [Any content that must NOT be included]
- [Any validation steps that must run before completion]

VALIDATION GATE (non-skippable):
[Describe the check that must pass before this task is marked complete.
Example: "Open HTML in browser and confirm all markers, all filters, and all pills render before submitting."]

SPLIT INSTRUCTIONS (if context limits apply):
[If this task may exceed one context window, describe where to split:
"If you reach [condition], stop, output [intermediate artifact], and note where to resume."]
```

---

## Prompt Engineering Gates Checklist

Verify before sending any fresh chat prompt:

- [ ] **Self-contained** — zero dependency on prior chat context; all necessary context embedded
- [ ] **Front-loaded** — operating contract stated in first 3 lines
- [ ] **Context-declared** — explicitly lists every file to read before acting
- [ ] **Token-efficient** — no meta-commentary; no re-explanation of what the prompt does
- [ ] **Output-specified** — exact file paths and formats for every output artifact
- [ ] **Split-aware** — if the task exceeds one context window, the prompt includes its own split instructions
- [ ] **Validation-gated** — includes a mandatory non-skippable validation step

---

## Example (Completed)

```
OPERATING CONTRACT: Build the upstream root cause map for the FDN thyroid marker cluster.
This prompt is self-contained. Read every file listed below before acting.

READ FIRST (in this order):
1. [Paste contents of 03-templates/marker-upstream-map-template.md]
2. [Paste the 7-category root cause taxonomy from 00-inventory/system-map.md, Section 2F]
3. [Paste the adrenal cluster summary from 02-reverse-engineered/adrenal/cluster-summary.md — needed for thyroid-HPA crosslinks]

TASK:
1. For each marker in this list [TSH, free T4, free T3, reverse T3, T3/rT3 ratio, TPO antibodies, TG antibodies]:
   a. Identify the full production/regulation pathway as numbered nodes
   b. At each node: list all upstream FDN-relevant vulnerabilities; assign each to a root cause category
   c. Flag any nodes shared with markers from other panels
2. Write one file per marker using the template format
3. Write a cluster summary file covering: shared nodes, cross-panel links, top 3 high-leverage nodes

OUTPUT FILES:
- 02-reverse-engineered/thyroid/TSH-map.md
- 02-reverse-engineered/thyroid/freeT4-map.md
- 02-reverse-engineered/thyroid/freeT3-map.md
- 02-reverse-engineered/thyroid/rT3-map.md
- 02-reverse-engineered/thyroid/T3-rT3-ratio-map.md
- 02-reverse-engineered/thyroid/TPO-antibodies-map.md
- 02-reverse-engineered/thyroid/TG-antibodies-map.md
- 02-reverse-engineered/thyroid/cluster-summary.md

CONSTRAINTS:
- Tables and bullet lists only — no prose paragraphs
- Every marker must have ≥ 3 distinct root cause nodes
- Every upstream stressor must be assigned to one of the 7 root cause categories
- If a node has fewer than 3 traceable stressors, flag as "requires additional research"

VALIDATION GATE (non-skippable):
Before submitting, run the template validation checklist on each marker file. Confirm every checkbox passes. If any file fails, revise before completing.

SPLIT INSTRUCTIONS:
If you complete 4 markers and context is filling, stop, output those 4 files, and note "Resume from marker [name]" — do not attempt all 7 in one pass if context is constrained.
```
