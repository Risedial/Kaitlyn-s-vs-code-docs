# Template: Interactive HTML Widget Specification
**Version:** 1.0 — 2026-03-22
**Use for:** Any interactive single-file HTML tool in this methodology project

---

## Standard Architecture (apply to all HTML widgets in this project)

### File constraints
- Single `.html` file — no external dependencies, no CDN links
- Works fully offline
- All CSS and JS inline in the file
- No build step required

### Visual design system (consistent across all widgets)

**Color palette:**
```
Background:        #0F1117 (near-black)
Card surface:      #1A1D27
Card border:       #2D3145
Text primary:      #F8F9FA
Text secondary:    #9CA3AF
Text muted:        #4B5563
Accent:            #6366F1 (indigo)

Root cause category colors:
  Nutrient/Mineral:    #F59E0B (amber)
  Hormonal/HPA:        #F43F5E (rose)
  Neurotransmitter:    #8B5CF6 (violet)
  Microbiome/Gut:      #10B981 (emerald)
  Structural/Barrier:  #0EA5E9 (sky)
  Immune:              #6366F1 (indigo)
  Metabolic:           #EA580C (orange)
```

**Typography:**
- Font stack: `system-ui, -apple-system, sans-serif`
- Marker names: 14px, weight 600
- Pill text: 11px, weight 500
- Body text: 13px, weight 400
- Section headers: 16px, weight 700

**Spacing:**
- Card padding: 16px
- Card gap: 12px
- Pill padding: 4px 10px
- Pill border-radius: 12px
- Card border-radius: 8px

---

## Component Specifications

### Marker Card
```
Structure:
  [marker-name]        [panel-badge]
  [1-sentence description]
  [root-cause-pill] [root-cause-pill] [root-cause-pill] ...

States:
  collapsed: shows name + description + pills preview (first 3)
  expanded: shows all pills + mechanism tooltips + clinical note

Interaction:
  click card header → toggle expanded/collapsed
  hover pill → show mechanism tooltip
  click pill → copy "Tell me more about [mechanism] in the context of [marker]" to clipboard
```

### Root Cause Pill
```
Structure:
  [category-colored background] [mechanism label text]

Properties:
  - label: short mechanism name (2–4 words max)
  - category: one of 7 categories (determines color)
  - mechanism: 1-sentence explanation (shown on hover)
  - linked_marker: the marker this pill belongs to (for click action)
```

### Filter Bar
```
Structure:
  [All] [Nutrient/Mineral] [Hormonal/HPA] [Neurotransmitter] [Microbiome/Gut] [Structural/Barrier] [Immune] [Metabolic]

Behavior:
  - Single select: clicking a category shows ONLY markers that have at least one pill in that category
  - [All] resets to show all markers
  - Active filter: button shows colored border matching category color

State management:
  - activeFilter: string — current category name, or "all"
  - filtered markers: computed from activeFilter
```

### Search Bar
```
Structure:
  [🔍 Search markers...]

Behavior:
  - Real-time filter: updates visible markers as user types
  - Searches: marker name + description text
  - Combined with active category filter (AND logic)
```

---

## Data Structure

```javascript
const markers = [
  {
    id: "siga",
    name: "Secretory IgA (SIgA)",
    panel: "Gut/Mucosal",
    description: "Terminal output of the mucosal immune axis; reflects integrity of antigen education, class switching, homing, plasma cell function, and epithelial transport.",
    rootCauses: [
      {
        label: "pIgR suppression",
        category: "Hormonal/HPA",
        mechanism: "Cortisol directly downregulates pIgR expression on epithelial cells, throttling luminal IgA delivery even when plasma cells produce dimeric IgA normally."
      },
      {
        label: "Vitamin A insufficiency",
        category: "Nutrient/Mineral",
        mechanism: "Retinoic acid drives IgA class switching and gut-homing imprinting in Peyer's patch dendritic cells; deficiency causes B cells to class switch to IgG or fail to home to gut."
      },
      {
        label: "Dysbiosis",
        category: "Microbiome/Gut",
        mechanism: "Microbiome is required for GALT maturation; dysbiotic environment degrades antigen education quality and IgA class switching stimulus."
      }
      // ... additional root causes
    ]
  }
  // ... additional markers
];
```

---

## Validation Checklist for Any HTML Widget

Before marking a widget build complete:
- [ ] Opens in browser without errors (check console)
- [ ] All markers render (count matches source data)
- [ ] All pills render with correct colors
- [ ] Filter bar filters correctly (category active → only relevant markers shown)
- [ ] [All] button resets correctly
- [ ] Search filters by name in real time
- [ ] Hover on pill shows tooltip
- [ ] Expand/collapse works on all cards
- [ ] No external requests (check Network tab — should be empty)
- [ ] Works offline (disconnect internet, reload)

---

## Template Usage Instructions

When building a new widget:
1. Copy this spec
2. Fill in the data structure with actual marker data
3. Implement each component per specification above
4. Run validation checklist before submitting
5. If adding new component types: add spec to this template file for reuse
