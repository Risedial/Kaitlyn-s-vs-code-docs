# Template: Marker Cluster Research Workflow
**Version:** 1.0 — 2026-03-22
**Use for:** Any FDN marker cluster research session (Outcome 05 sub-clusters)

---

## Pre-Session Setup Checklist

Before opening any chat for cluster research:
- [ ] `03-templates/marker-upstream-map-template.md` — open and ready to paste
- [ ] `00-inventory/system-map.md` Section 2F (root cause categories) — open and ready to paste
- [ ] Prior related cluster summary — open if cross-linking is expected (e.g., adrenal summary before sex hormone session)
- [ ] Cluster marker list confirmed — all markers identified before starting

---

## Session Protocol

**Opening the chat:**
1. Use `03-templates/fresh-chat-prompt-template.md`
2. Fill in: cluster name, marker list, READ FIRST files (template + taxonomy + prior cluster summaries)
3. Paste assembled prompt into new conversation

**During the session:**
- After each marker file is output, confirm: template validation checklist passes
- Flag any "requires additional research" entries immediately — do not defer
- After all markers complete: request cluster summary file

**Closing the session:**
- Confirm all output files exist
- Note any research gaps identified
- Update `01-outcomes/outcome-registry.md` Outcome 05 status for this cluster

---

## Output File Naming Convention

```
02-reverse-engineered/
  [cluster-name]/
    [marker-abbreviation]-map.md          e.g., siga-map.md, TSH-map.md
    cluster-summary.md
```

**Cluster name options:** `adrenal` | `gut-mucosal` | `sex-hormone` | `thyroid` | `metabolic-oxidative` | `neurotransmitter-oat`

---

## Cluster Summary Format

Each cluster summary must include:

```markdown
# [Cluster Name] Cluster Summary

## Shared Nodes Within Cluster
| Node | Appears In Markers | Significance |
|---|---|---|

## Cross-Cluster Links
| Node | Also in Cluster | Marker(s) |
|---|---|---|

## Top 3 High-Leverage Nodes
1. [Node] — affects [# markers] in this cluster + [# markers] across clusters
2. [Node] — [same]
3. [Node] — [same]

## Key Clinical Patterns
| Pattern | Likely Node | Confirming Markers |
|---|---|---|

## Research Gaps
| Gap | What's Missing | Resolution Path |
|---|---|---|
```

---

## Cross-Cluster Link Tracking

When a node appears in markers from two or more clusters, create an entry in:
`04-meta-system/cross-cluster-link-registry.md`

Format:
```
| Node Name | Cluster A | Cluster B | Cluster C | Intervention Implication |
```

This registry feeds directly into Outcome 02 (Nodal Reasoning Framework).
