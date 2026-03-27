# Codebase Patterns — FDN Symptom Navigator (fdn-pwa/index.html)

---

## Section 1 — Render Functions

All render functions use the `el()` DOM helper to build nodes and append them to a `container` argument. Screens are dynamically created and destroyed — there is no static screen HTML.

| Function | Signature | Description |
|---|---|---|
| `renderScreen` | `renderScreen(screenName)` | Top-level dispatcher: clears `#screen-container`, creates a `<div class="screen screen-enter">`, then calls the appropriate tab-level render function based on `screenName` ('home', 'search', 'clusters'). |
| `renderHome` | `renderHome(container)` | Renders the Home tab: sticky header ("What are you experiencing?"), live search bar, accordion list of symptoms grouped by category in `CATEGORY_ORDER`. |
| `renderSearch` | `renderSearch(container)` | Renders the Search tab: sticky header ("Browse All"), search bar, and an initial full listing via `renderSearchResults`. Binds `input` listener to re-render results on keypress. |
| `renderSearchResults` | `renderSearchResults(container, query)` | Renders filtered symptom+variable results into a container. Groups results under "Symptoms" and "Variables" headings. Empty state shown when no matches. |
| `renderClusters` | `renderClusters(container)` | Renders the Clusters tab: sticky header ("Root Cause Clusters"), list rows for each `DATA.clusters` entry with color dot, cluster tag, and chevron. |
| `renderSheetContent` | `renderSheetContent(type, id)` | Dispatches detail rendering into the bottom sheet: calls `renderSymptom`, `renderVariable`, or `renderCluster` based on `type`. |
| `renderSymptom` | `renderSymptom(id, container)` | Renders a symptom detail view: back button, symptom label, cluster tags, variable pills, interpretation text, and mechanism tree. |
| `renderVariable` | `renderVariable(id, container)` | Renders a variable detail view: back button, variable name, panel badge, medical-referral alert (if `isMedicalReferral`), priority-pathogen alert (if `isPriorityPathogen`), high/low interpretation, connections pills, and related symptoms list. |
| `renderCluster` | `renderCluster(id, container)` | Renders a cluster detail view: back button, cluster letter tag, full name, mechanism text, priority note block, referral block (for Cluster E), and variables list. |

---

## Section 2 — Event Delegation Handler

**Function name:** `handleClick`

**Exact `addEventListener` call:**
```js
document.addEventListener('click', function handleClick(e) {
```

**Dispatch pattern (switch on `data-action`):**

The handler walks the DOM tree upward from `e.target` to find the nearest ancestor with a `data-action` attribute:

```js
document.addEventListener('click', function handleClick(e) {
  // Walk up the DOM tree to find the element with data-action
  let target = e.target;
  while (target && target !== document.body) {
    const action = target.dataset && target.dataset.action;
    if (action) {
      const id = target.dataset.id;
      switch (action) {
        case 'navigate-tab':
          navigateTab(target.dataset.tab);
          return;
        case 'open-symptom':
          if (!id) return;
          if (state.sheet.isOpen) pushSheet('symptom', id);
          else openSheet('symptom', id);
          return;
        case 'open-variable':
          if (!id) return;
          if (state.sheet.isOpen) pushSheet('variable', id);
          else openSheet('variable', id);
          return;
        case 'open-cluster':
          if (!id) return;
          if (state.sheet.isOpen) pushSheet('cluster', id);
          else openSheet('cluster', id);
          return;
        case 'go-back':
          popSheet();
          return;
        case 'close-sheet':
          closeSheet();
          return;
        default:
          break;
      }
    }
    target = target.parentElement;
  }
});
```

---

## Section 3 — Tab Navigation Logic

Tab activation is handled by `navigateTab(tabName)`:

1. **Save scroll position:** `state.scrollPositions.set(state.activeTab, document.getElementById('screen-container').scrollTop)`
2. **Close open sheet:** if `state.sheet.isOpen`, calls `closeSheet()`
3. **Update state:** `state.activeTab = tabName; state.screen = tabName;`
4. **Mark active tab button:** iterates `document.querySelectorAll('.tab-item')`, sets `aria-selected` to `"true"` on the matching button and `"false"` on all others — no class changes, only ARIA attribute toggling
5. **Render new screen:** calls `renderScreen(tabName)`, which clears `#screen-container` completely and re-renders the new screen from scratch (no `hidden` attribute or class toggling — full DOM replacement)
6. **Restore scroll:** `requestAnimationFrame(() => { document.getElementById('screen-container').scrollTop = savedScroll; })`

```js
function navigateTab(tabName) {
  if (state.activeTab) {
    state.scrollPositions.set(state.activeTab, document.getElementById('screen-container').scrollTop);
  }
  if (state.sheet.isOpen) closeSheet();
  state.activeTab = tabName;
  state.screen = tabName;
  document.querySelectorAll('.tab-item').forEach(btn => {
    const isActive = btn.dataset.tab === tabName;
    btn.setAttribute('aria-selected', String(isActive));
  });
  renderScreen(tabName);
  requestAnimationFrame(() => {
    const savedScroll = state.scrollPositions.get(tabName) || 0;
    document.getElementById('screen-container').scrollTop = savedScroll;
  });
}
```

---

## Section 4 — App State Object

**Variable name:** `const state`

**Declaration (line 1834):**
```js
const state = {
  screen: 'home',
  activeTab: 'home',
  sheet: {
    isOpen: false,
    type: null,
    id: null,
    stack: [],
  },
  searchQuery: '',
  expandedCategories: new Set(),
  scrollPositions: new Map(),
};
```

**Top-level keys:**

| Key | Type | Notes |
|---|---|---|
| `screen` | string | Current screen name: `'home'` \| `'search'` \| `'clusters'` |
| `activeTab` | string | Tracks which tab button is selected (same values as `screen`) |
| `sheet` | object | Nested: `isOpen` (bool), `type` (string\|null), `id` (string\|null), `stack` (array of `{type, id, scrollY}`) |
| `searchQuery` | string | Current search bar input value for the Home screen search |
| `expandedCategories` | Set | Set of category-name strings currently expanded in the accordion |
| `scrollPositions` | Map | Maps tab name → scrollY value for scroll position restoration |

---

## Section 5 — DATA.symptoms Cluster Field

**YES.** Every `DATA.symptoms` entry contains a `clusters` property — an array of cluster code strings (e.g., `['A', 'B']`).

**Verbatim example entry (`'always-tired'`):**
```js
'always-tired': {
  label: 'Always tired',
  category: 'Energy & Fatigue',
  variables: ['cortisol-diurnal', 'dhea', 'hpa-axis', 'sigas-shp', 'indican', 'ohdg', 'hepatic-detox'],
  clusters: ['A', 'B'],
  interpretation: 'Persistent fatigue without a clear cause reflects convergence of HPA dysregulation depleting cortisol reserve, GI-driven amino acid theft reducing neurotransmitter production, and accumulated oxidative damage impairing mitochondrial ATP output. This is the signature multi-system presentation in functional exhaustion. The practitioner should map which driver is upstream by examining cortisol diurnal pattern shape alongside Indican and 8-OHdG values together.',
  mechanismTree: 'HPA Dysregulation (Cortisol Diurnal Pattern flat or inverted)\n└─ Pregnenolone Steal → DHEA depletion\n   └─ Anabolic collapse → exercise intolerance, motivational fatigue\nGI Dysbiosis (Indican elevation)\n└─ Tryptophan theft by bacteria → serotonin/melatonin deficit\n   └─ Neurotransmitter depletion → non-restorative sleep, mood-fatigue loop\nOxidative Burden (8-OHdG)\n└─ Mitochondrial DNA damage\n   └─ Reduced ATP synthesis → cellular energy deficit'
},
```

The `clusters` array is used at runtime by `buildMaps()` to populate `maps.symptomsByCluster` (a reverse-lookup map from cluster letter to array of symptom IDs).

---

## Section 6 — selectedSymptomIds State

**NO.** There is no `selectedSymptomIds` array or equivalent persistent multi-select selection state in the app state object.

The `state` object contains no property tracking selected symptoms. The Home screen accordion allows expanding/collapsing categories (tracked in `state.expandedCategories`), but there is no symptom-selection or multi-select UI — tapping a symptom immediately opens the bottom-sheet detail view rather than toggling a selection.

---

## Section 7 — CSS Custom Properties

All defined in `:root {}` (lines 13–108):

```css
--safe-top:    env(safe-area-inset-top, 0px)
--safe-right:  env(safe-area-inset-right, 0px)
--safe-bottom: env(safe-area-inset-bottom, 0px)
--safe-left:   env(safe-area-inset-left, 0px)
--bg-primary:   #000000
--bg-secondary: #1C1C1E
--bg-tertiary:  #2C2C2E
--bg-glass:     rgba(28, 28, 30, 0.72)
--text-primary:   rgba(255, 255, 255, 1.0)
--text-secondary: rgba(255, 255, 255, 0.55)
--text-tertiary:  rgba(255, 255, 255, 0.35)
--separator:        rgba(255, 255, 255, 0.12)
--separator-opaque: #3A3A3C
--accent:             #007AFF
--accent-destructive: #FF3B30
--panel-mwp:   #e07c3a
--panel-mba:   #3abde0
--panel-shp:   #8b5cf6
--panel-gimap: #22c55e
--panel-cross: #94a3b8
--cluster-a: #ef4444
--cluster-b: #f97316
--cluster-c: #ec4899
--cluster-d: #06b6d4
--cluster-e: #fbbf24
--font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif
--text-xs:   0.6875rem
--text-sm:   0.8125rem
--text-base: 1rem
--text-md:   1.0625rem
--text-lg:   1.25rem
--text-xl:   1.5rem
--text-2xl:  2rem
--weight-regular:  400
--weight-medium:   500
--weight-semibold: 600
--weight-bold:     700
--tracking-tight:  -0.02em
--tracking-normal:  0em
--tracking-wide:    0.03em
--tracking-caps:    0.06em
--space-1:  0.25rem
--space-2:  0.5rem
--space-3:  0.75rem
--space-4:  1rem
--space-5:  1.25rem
--space-6:  1.5rem
--space-8:  2rem
--space-10: 2.5rem
--space-12: 3rem
--radius-sm:   8px
--radius-md:   12px
--radius-lg:   16px
--radius-xl:   20px
--radius-full: 9999px
--shadow-0: none
--shadow-1: 0 1px 2px rgba(0,0,0,0.4), 0 0px 1px rgba(0,0,0,0.3)
--shadow-2: 0 4px 12px rgba(0,0,0,0.5), 0 1px 3px rgba(0,0,0,0.4)
--shadow-3: 0 16px 40px rgba(0,0,0,0.6), 0 4px 12px rgba(0,0,0,0.5), 0 1px 3px rgba(0,0,0,0.4)
--ease-spring:   cubic-bezier(0.34, 1.56, 0.64, 1)
--ease-snap:     cubic-bezier(0.25, 0.46, 0.45, 0.94)
--ease-standard: cubic-bezier(0.4, 0, 0.2, 1)
--duration-fast:   150ms
--duration-normal: 300ms
--duration-slow:   450ms
--touch-target:  44px
--max-width:    430px
--nav-height:   calc(60px + var(--safe-bottom))
--header-height: calc(52px + var(--safe-top))
```

---

## Section 8 — Screen Section IDs

The app uses **fully dynamic rendering** — there are no static `<section id="screen-*">` or `<div id="screen-*">` elements in the HTML beyond the single mount point container.

**Static HTML element IDs:**

| ID | Element | Purpose |
|---|---|---|
| `screen-container` | `<div>` | Mount point; screens are rendered into this element dynamically |

**Dynamically rendered screens** (created as `<div class="screen screen-enter">` inside `#screen-container`; no individual IDs):

| Screen name | Render function | Triggered by |
|---|---|---|
| `home` | `renderHome(container)` | `navigateTab('home')` / app init |
| `search` | `renderSearch(container)` | `navigateTab('search')` |
| `clusters` | `renderClusters(container)` | `navigateTab('clusters')` |

**Note for future development:** When adding a new screen (e.g., a "Practices" tab), follow the same pattern: add a `data-tab="practices"` button to `.tab-bar`, add a `case 'practices'` branch in `renderScreen()`, and write a `renderPractices(container)` function. No static HTML screen section needed.

---

## Section 9 — Physician Referral Pattern

**YES.** The codebase contains `isMedicalReferral` logic in two places:

### 1. DATA.variables — per-variable flag

Each variable entry in `DATA.variables` carries an `isMedicalReferral: boolean` field. Two variables have it set to `true` (Calprotectin/Lactoferrin at line 1661, and Occult Blood at line 1713). Example from data:

```js
isMedicalReferral: true
```

### 2. renderVariable() — conditional alert banner (lines 2187–2199)

```js
// ── Medical Referral Alert ─────────────────────────────────────────────
if (variable.isMedicalReferral) {
  const alert = el('div', { class: 'alert-banner alert-banner--destructive', role: 'alert' });
  const alertIcon = el('span', { class: 'alert-icon' }, [txt('⚕')]);
  const alertBody = el('div', { class: 'alert-body' });
  alertBody.appendChild(el('p', { class: 'alert-title' },
    [txt('MEDICAL REFERRAL REQUIRED')]));
  alertBody.appendChild(el('p', { class: 'alert-description' },
    [txt('Refer to physician before FDN interventions proceed. This finding indicates structural pathology requiring medical evaluation.')]));
  alert.appendChild(alertIcon);
  alert.appendChild(alertBody);
  container.appendChild(alert);
}
```

### 3. CSS — `.referral-block` class (lines 741–750)

A separate `.referral-block` CSS class (amber/yellow styling) is also defined and used inside `renderCluster()` for Cluster E's priority note:

```css
.referral-block {
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: rgba(251, 191, 36, 0.12);
  border: 1px solid var(--cluster-e);
  color: var(--cluster-e);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  line-height: 1.5;
}
```

---

## Section 10 — Function and Naming Patterns

| Category | Convention | Example |
|---|---|---|
| JavaScript functions | camelCase | `renderHome`, `navigateTab`, `buildMaps`, `openSheet`, `closeSheet`, `pushSheet`, `popSheet`, `clearEl` |
| CSS class names | kebab-case (utility/BEM-lite) | `top-header`, `tab-item`, `list-row`, `accordion-body`, `is-open`, `screen-enter`, `alert-banner--destructive` |
| `data-action` values | kebab-case, verb-noun | `navigate-tab`, `open-symptom`, `open-variable`, `open-cluster`, `go-back`, `close-sheet` |
| `data-tab` values | lowercase single word | `home`, `search`, `clusters` |
| `data-id` values | kebab-case | `always-tired`, `cortisol-diurnal`, `cluster-A` |
| CSS custom property names | kebab-case with `--` prefix, semantic grouping | `--bg-primary`, `--text-secondary`, `--panel-mwp`, `--cluster-a`, `--space-4` |
| DATA object keys | kebab-case strings | `'always-tired'`, `'cortisol-diurnal'`, `'hpa-axis'` |
| Modifier CSS classes | `is-*` prefix for state | `is-open`, `is-visible` |
