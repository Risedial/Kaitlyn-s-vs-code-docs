# Parameter Extraction Algorithm
**Purpose:** Universal algorithm for extracting every parameter at every level from any artifact in this project
**Date:** 2026-03-22

---

## What "Parameter" Means in This Project

A parameter is any variable that:
- Controls a behavior, output, or condition
- Can take different values in different instances
- Must be specified before a task can execute correctly

Parameters exist at every layer. Failing to extract micro-micro parameters is the most common source of incomplete work.

---

## Universal Algorithm

### Pass 1 — Structural Scan

Read the artifact once. For each element, record:
1. What it is (component type)
2. What it does (function)
3. What controls it (its inputs)
4. What it produces (its outputs)
5. What it fails to do if missing (failure mode)

**Output:** rough inventory list — not structured yet

---

### Pass 2 — Layer Assignment

For each item from Pass 1, assign it to a layer:

| Layer | Test |
|---|---|
| meta-meta | Does it govern the entire system? Does it constrain other rules? |
| meta | Does it define component roles or inter-component contracts? |
| macro | Does it define a major outcome or cross-file workflow? |
| micro | Does it define what one file or component does? |
| micro-micro | Is it a specific value, variable, condition, or edge case? |

Rule: when uncertain, assign to the lower (more specific) layer.

---

### Pass 3 — Explicit vs. Implicit Extraction

For every item, determine:

**Explicit** — stated directly in the artifact
- Extract verbatim where possible
- Preserve exact values (numbers, names, conditions)

**Implicit** — required but not stated
- Inferred from structure: what must be true for this to work?
- Inferred from relationships: what must the input be for this output to occur?
- Inferred from constraints: what is ruled out by what IS stated?

Rule: implicit parameters are often more important than explicit ones. Do not skip this pass.

---

### Pass 4 — Dependency Mapping

For each parameter:
1. Does it require another parameter to be set first?
2. Does it constrain any other parameters?
3. If it changes, what else must change?

**Output:** dependency chain per parameter

---

### Pass 5 — Edge Case Identification

For each parameter:
- What happens at the boundary values (minimum, maximum, zero, null)?
- What happens if this parameter is set incorrectly?
- Is there a conflict condition (two parameters that cannot be set simultaneously)?

---

### Pass 6 — Validation Rules

For each parameter:
- What is the valid range or set of values?
- What confirms this parameter is set correctly?
- What observable output confirms the parameter is working as intended?

---

## Application to This Project's Artifact Types

### Applying to a Marker Upstream Map
| Layer | What to Extract |
|---|---|
| meta-meta | Governing rule for the marker (e.g., "SIgA is sensitive but non-specific") |
| meta | The node sequence; the relationship between nodes |
| macro | The clinical outcome of the full map |
| micro | Per-node: name, function, upstream vulnerabilities |
| micro-micro | Per-vulnerability: stressor name, mechanism sentence, root cause category, FDN marker correlate, BCMO1/bile/etc. modifiers |

### Applying to an HTML Widget
| Layer | What to Extract |
|---|---|
| meta-meta | Design constraints that must hold across all states |
| meta | Component architecture; state management contract |
| macro | User interaction flow; what the user can accomplish |
| micro | Per-component: structure, states, interactions |
| micro-micro | Color hex values; font sizes; border-radius values; filter logic operators; tooltip trigger conditions |

### Applying to a Clinical Decision Framework
| Layer | What to Extract |
|---|---|
| meta-meta | What makes this framework valid (e.g., "every claim must trace to a mechanism") |
| meta | Decision tree structure; input → output contract |
| macro | Outcome categories (proximal failure, upstream failure, compound failure) |
| micro | Per-rule: condition(s), consequence, intervention |
| micro-micro | Exact marker thresholds; OR vs. AND logic between conditions; null condition handling |

---

## Algorithm Output Format

After all 6 passes, produce a parameter table:

| Parameter Name | Layer | Type (Explicit/Implicit) | Value or Range | Dependencies | Edge Cases | Validation Rule |
|---|---|---|---|---|---|---|
| [Name] | [Layer] | E / I | [Value] | [Deps] | [Cases] | [Rule] |
