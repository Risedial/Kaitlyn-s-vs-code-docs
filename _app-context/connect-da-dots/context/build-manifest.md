# Build Manifest — FDN Symptom Navigator PWA
*Synthesized from /context/pwa-technical.md, /context/ui-design-system.md, /context/data-inventory.md, /context/app-architecture.md*

---

## PWA File Structure

```
/fdn-pwa/
  index.html      — App shell: <head> meta + <style> block + <body> skeleton + <script> with DATA, state, render functions
  manifest.json   — Web App Manifest: name, icons (192+512), display: standalone, theme_color, start_url, scope
  sw.js           — Service Worker: cache-first strategy, install/activate/fetch handlers
```

**Why three files (not one):**
- Service workers must be served at a real URL with their own scope; blob: URLs are not accepted by Safari or Chrome for SW registration
- The manifest must be fetched as a separate HTTP resource by Chrome's installability checker; data: URI manifests are not reliably supported
- Icon assets can be embedded as base64 data URIs inside manifest.json to avoid external hosting while remaining installable

---

## CSS Architecture

All CSS lives in a single `<style>` block inside `index.html`.

**Organization order inside `<style>`:**
1. `:root {}` — all custom properties from `/context/design-tokens.css` (copy verbatim)
2. Reset: `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }`
3. Base: `html`, `body`, `-webkit-tap-highlight-color: transparent`
4. Layout: `#app`, `.screen-stack`, `.screen`
5. Navigation: `.tab-bar`, `.tab-item`, `.tab-item[aria-selected="true"]`
6. Header: `.top-header`, `.top-header-inner`, `.header-title`, `.back-btn`
7. Home screen: `.search-bar-wrapper`, `.search-bar`, `.search-input`, `.accordion-header`, `.accordion-body`, `.list-row`, `.list-row-chevron`
8. Detail screens: `.bottom-sheet`, `.sheet-drag-indicator`, `.sheet-header`, `.sheet-body`
9. Components: `.var-pill`, `.var-pill--cross`, `.cluster-tag`
10. Alerts: `.alert-banner`, `.alert-banner--destructive`, `.referral-banner`
11. Utility: `.section-label`, `.mechanism-tree`, `.pill-grid`, `.tag-grid`

**Class naming convention:** BEM-lite — block (`.bottom-sheet`), modifier (`--cross`, `--destructive`), state (`.is-open`, `[aria-selected]`, `[aria-expanded]`)

**CSS transition rule:** All animations use `transition` on CSS properties only. No `setTimeout`, no JS animation loops, no requestAnimationFrame for visual state.

---

## JS Architecture

All JS lives in a single `<script>` block inside `index.html`, organized in this exact order:

### 1. DATA object
```javascript
const DATA = {
  symptoms: {
    'always-tired': {
      label: 'Always tired',
      category: 'Energy & Fatigue',
      variables: ['cortisol-pattern', 'dhea', 'hpa-pattern', 'siga-shp', 'indican', '8-ohdg', 'hepatic-detox'],
      clusters: ['A', 'B'],
      interpretation: '...',    // 2-3 sentence practitioner-voice text
      mechanismTree: '...'      // └─ indented text (3+ levels)
    }
    // 76 total symptoms — all categories fully written out
  },
  variables: {
    'indican': {
      name: 'Indican',
      panel: 'MWP',
      panelColor: 'var(--panel-mwp)',
      elevated: '...',
      low: 'N/A — not interpreted as low in this context',
      connections: ['urinary-bile-acids', '8-ohdg', 'zonulin', 'histamine-mba', 'dao', 'siga-shp'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    }
    // 28 total variables
  },
  clusters: {
    'A': {
      letter: 'A',
      name: 'GI Ecosystem Collapse',
      fullName: 'Cluster A — GI Ecosystem Collapse (Primary Driver)',
      color: 'var(--cluster-a)',
      mechanism: '...',
      priorityNote: 'Address before all others — GI dysfunction drives all downstream clusters.',
      variables: ['indican', 'urinary-bile-acids', ...]
    }
    // 5 total clusters
  }
};
```

**DATA counts (from data-inventory.md):**
- `DATA.symptoms`: 76 entries across 14 categories
- `DATA.variables`: 28 entries across 5 panels (MWP: 3, MBA: 3, SHP: 7, GI-MAP: 10, cross-panel: 5)
- `DATA.clusters`: 5 entries (A, B, C, D, E)

### 2. Service Worker registration
```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js').catch(console.error);
}
```

### 3. State object
```javascript
const state = {
  screen: 'home',          // 'home' | 'symptom' | 'variable' | 'cluster' | 'search'
  item: null,              // { type: string, id: string } | null
  stack: [],               // Array<{ screen, item }> — back navigation stack
  searchQuery: '',         // current search string
  expandedCategories: new Set(), // Set<string> — category names currently expanded
  scrollPositions: new Map()     // Map<key, number> — saved scroll positions
};
```

### 4. Navigation functions
```javascript
function navigate(screen, item = null) {
  // Save current scroll position
  const key = state.screen + (state.item?.id ?? '');
  state.scrollPositions.set(key, window.scrollY);
  // Push current location to stack
  state.stack.push({ screen: state.screen, item: state.item });
  // Transition
  state.screen = screen;
  state.item = item;
  render();
}

function goBack() {
  if (!state.stack.length) return;
  const prev = state.stack.pop();
  state.screen = prev.screen;
  state.item = prev.item;
  render();
  // Restore scroll after render
  requestAnimationFrame(() => {
    const key = state.screen + (state.item?.id ?? '');
    const saved = state.scrollPositions.get(key);
    if (saved !== undefined) window.scrollTo(0, saved);
  });
}
```

### 5. Render functions (one per screen)
- `renderHome()` — search bar + 14 accordion category sections + symptom list rows
- `renderSymptom(id)` — back btn + name + optional H. pylori alert + variable pills + cluster tags + interpretation + mechanism tree
- `renderVariable(id)` — back btn + name + panel badge + optional banners (referral/pathogen) + elevated/low + connected pills + cluster tags
- `renderCluster(id)` — back btn + name + mechanism + priority note + variable pills + reverse-mapped symptom rows
- `renderSearch()` — full-screen search input + grouped results (Symptoms / Variables)

**DOM construction rule:** Use `createElement` and `textContent` only. Never `innerHTML` with dynamically-constructed strings.

### 6. Event delegation
```javascript
document.addEventListener('click', e => {
  const el = e.target.closest('[data-action]');
  if (!el) return;
  const { action, id } = el.dataset;
  const handlers = {
    'nav-symptom':   () => navigate('symptom',  { type: 'symptom',  id }),
    'nav-variable':  () => navigate('variable', { type: 'variable', id }),
    'nav-cluster':   () => navigate('cluster',  { type: 'cluster',  id }),
    'nav-tab':       () => switchTab(id),
    'go-back':       () => goBack(),
    'toggle-cat':    () => toggleCategory(id)
  };
  handlers[action]?.();
});
```

### 7. init()
```javascript
function init() { render(); }
init();
```

---

## Clinical UX Rules

### H. pylori Priority Alert
**Condition:** `DATA.symptoms[id].variables.includes('hpylori')`
**Placement:** Rendered BEFORE the variable pills section — never after
**Exact wording:** "⚠ Treat H. pylori before addressing other findings"
**Visual:** `.alert-banner.alert-banner--destructive` — red border, red text, rgba red background

### Cluster E Medical Referral
**Trigger 1:** `renderCluster('E')` — display prominent MEDICAL REFERRAL REQUIRED block at top of cluster detail
**Trigger 2:** Any variable with `isMedicalReferral: true` (Calprotectin/Lactoferrin, Occult Blood) — display referral banner in variable detail
**Exact wording:** "⚕ MEDICAL REFERRAL REQUIRED — Refer to physician before FDN interventions"
**Visual:** Same `.alert-banner--destructive` component, or distinct amber `.alert-banner--warning` for Cluster E header

### Cross-Panel Construct Styling
**Condition:** `variable.isCrossPanel === true`
**Five variables:** Systemic Oxidative Stress Cascade, Hepatic Detoxification Impairment, Histamine-DAO Regulatory System, HPA Axis Dysregulation Pattern, Pregnenolone Steal and Steroidogenesis Disruption
**Visual:** `.var-pill.var-pill--cross` — dashed border in `--panel-cross` (#94a3b8), transparent background, text matches border color
**Badge:** "CROSS-PANEL AMPLIFIER" label on variable detail card

### HPA 5-Phase References
**Phase names in order:** Alarm → Resistance → Exhaustion → Collapse → Recovery
**Usage:** HPA Axis Dysregulation Pattern variable card and any symptom interpretation text referencing HPA phases must use these exact names
**Pregnenolone Steal:** Must include the note "downstream mechanism — not a direct lab value" on its variable detail card

---

## Screen-by-Screen Spec

### Screen 1: Home
**DOM structure:**
```
<div class="screen" id="home-screen">
  <header class="top-header">
    <div class="top-header-inner">
      <h1 class="header-title">What are you experiencing?</h1>
    </div>
  </header>
  <div class="search-bar-wrapper"> ... </div>
  <main class="main-content">
    [14 × accordion section]
    each section:
      <button class="accordion-header" data-action="toggle-cat" data-id="[category]"> ... </button>
      <div class="accordion-body"> [symptom rows] </div>
  </main>
</div>
```
**Components used:** Top Header, Search Bar, Accordion Section Header, List Row
**Transition:** Base screen — no transition; slides left when navigating forward
**Data sources:** `DATA.symptoms` grouped by category; `state.expandedCategories`; `state.searchQuery`
**Search behavior:** Fires at ≥2 chars; filters symptom rows; shows count badge in section header; auto-expands matching sections; collapses non-matching sections

### Screen 2: Symptom Detail
**DOM structure:**
```
<div class="bottom-sheet is-open" id="symptom-sheet">
  <div class="sheet-drag-indicator"></div>
  <div class="sheet-header">
    <button class="back-btn" data-action="go-back">‹ Back</button>
    <h2 class="sheet-title">[symptom.label]</h2>
  </div>
  <div class="sheet-body">
    [conditional: .alert-banner--destructive if hpylori in variables]
    <section class="detail-section"> Variables Involved: [pill grid] </section>
    <section class="detail-section"> Root Cause Clusters: [tag grid] </section>
    <section class="detail-section"> What This Means: [interpretation text] </section>
    <section class="detail-section"> Mechanism Hierarchy: [.mechanism-tree] </section>
  </div>
</div>
```
**Components used:** Bottom Sheet, Alert Banner, Variable Pill, Cluster Tag, Mechanism Tree
**Transition:** Slides up from bottom with var(--ease-spring) 450ms

### Screen 3: Variable Detail
**DOM structure:**
```
<div class="bottom-sheet is-open" id="variable-sheet">
  <div class="sheet-drag-indicator"></div>
  <div class="sheet-header">
    <button class="back-btn" data-action="go-back">‹ Back</button>
    <h2 class="sheet-title">[variable.name]</h2>
  </div>
  <div class="sheet-body">
    <span class="panel-badge" style="--panel-color: [variable.panelColor]">[Panel Name]</span>
    [if isCrossPanel: <span class="cross-badge">CROSS-PANEL AMPLIFIER</span>]
    [if isPriorityPathogen: .alert-banner--destructive "⚠ Priority Pathogen — treat before other GI findings"]
    [if isMedicalReferral: .alert-banner--destructive "⚕ MEDICAL REFERRAL REQUIRED"]
    <section> When Elevated: [elevated text] </section>
    <section> When Low / Deficient: [low text or N/A] </section>
    <section> Connected Variables: [pill grid] </section>
    <section> Root Cause Clusters: [tag grid] </section>
  </div>
</div>
```
**Components used:** Bottom Sheet, Panel Badge, Cross-Panel Badge, Alert Banner, Variable Pill, Cluster Tag

### Screen 4: Cluster Detail
**DOM structure:**
```
<div class="bottom-sheet is-open" id="cluster-sheet">
  <div class="sheet-drag-indicator"></div>
  <div class="sheet-header">
    <button class="back-btn" data-action="go-back">‹ Back</button>
    <h2 class="sheet-title" style="color: [cluster.color]">[cluster.fullName]</h2>
  </div>
  <div class="sheet-body">
    [if id === 'E': prominent MEDICAL REFERRAL REQUIRED block]
    [if id === 'A': "Address before all others" priority block]
    <section> Mechanism: [mechanism text] </section>
    <section> Variables in This Cluster: [pill grid] </section>
    <section> Associated Symptoms: [reverse-mapped list rows] </section>
  </div>
</div>
```
**Reverse map logic:** `Object.entries(DATA.symptoms).filter(([,s]) => s.clusters.includes(id)).map(([sid]) => sid)`
**Components used:** Bottom Sheet, Alert Banner, Variable Pill, List Row

### Screen 5: Search
**DOM structure:**
```
<div class="screen" id="search-screen">
  <header class="top-header"> ... </header>
  <div class="search-bar-wrapper"> [autofocused search input] </div>
  <main class="main-content">
    [if query.length < 2: empty state text]
    [if results:
      <h3>Symptoms</h3> [matching symptom rows]
      <h3>Variables</h3> [matching variable pills]
    ]
    [if no results: "No matches for '[query]'"]
  </main>
</div>
```
**Search scope:** `symptom.label.toLowerCase().includes(query)` + `variable.name.toLowerCase().includes(query)`
**Transition:** Activated by bottom nav "Search" tab; slides in from right

---

## Category Order (14 categories — exact sequence for Home accordion)

1. Energy & Fatigue (6 symptoms)
2. Sleep (5 symptoms)
3. Mood & Emotions (9 symptoms)
4. Digestion (10 symptoms)
5. Food Reactions (5 symptoms)
6. Skin (6 symptoms)
7. Immune System (5 symptoms)
8. Hormonal (Female) (7 symptoms)
9. Hormonal (Male & Shared) (3 symptoms)
10. Cardiovascular & Circulatory (3 symptoms)
11. Pain & Inflammation (6 symptoms)
12. Respiratory (3 symptoms)
13. Cognitive & Neurological (4 symptoms)
14. Stress & Nervous System (4 symptoms)

**Note:** Source prompt states "13 categories" in the overview but the actual symptom data contains 14 distinct category labels. Use 14. Total symptoms: 76.
