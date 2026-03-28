# FDN Symptom Navigator — App Architecture Specification

---

## Screen Inventory

### Screen 1: Home (`screen: 'home'`)

**Data Displayed:**
- Title: "What are you experiencing?"
- Search input bar (pinned at top; activates filtering at 2+ characters typed)
- All 14 symptom categories as collapsible accordion sections, in the canonical order (see Category Order section below)
- Each category header shows the category name; when search is active and filtered, shows match count: e.g., "Digestion (3)"
- Within each expanded category: list of symptom cards, each showing the symptom label
- All categories collapsed by default on first load

**Navigation Actions:**
- Tap a symptom card → navigate('symptom', { type: 'symptom', id: symptomSlug })
- Tap a category header → toggle that category's expanded/collapsed state in state.expandedCategories
- Type in search bar (2+ chars) → transition to search screen OR filter in-place (see requirements: search bar on home activates Search screen)
- Tap bottom nav "Search" tab → navigate('search', null)
- Tap bottom nav "Clusters" tab → navigate('cluster-list', null) [cluster list view]

**Components Used:**
- Search input (pinned header)
- Category accordion (header button + collapsible list)
- Symptom card (tappable, min 44px height)
- Bottom navigation bar (3 tabs: Home | Search | Clusters)

---

### Screen 2: Symptom Detail (`screen: 'symptom'`)

**Data Displayed:**
- Back button (returns to exact previous screen)
- Symptom label as heading (from DATA.symptoms[id].label)
- PRIORITY ALERT (conditional): If H. pylori appears in this symptom's variables array → display high-contrast red banner: "⚠ Treat H. pylori before addressing other findings"
- Section "Variables Involved": each variable rendered as a tappable pill, color-coded by the variable's panel color (from DATA.variables[varId].panel → panel color map), labeled with the variable display name
- Section "Root Cause Clusters": each cluster in this symptom's clusters array rendered as a colored tappable tag with the format "A: GI Ecosystem Collapse" (letter prefix + full name), colored by cluster color
- Section "What This Means": 2–3 sentence plain-language mechanistic interpretation in practitioner voice
- Section "Mechanism Hierarchy": text-tree using └─ indentation, minimum 3 levels: SURFACE SYMPTOM → Immediate mechanism variable → Root driver → Deepest upstream cause. No canvas or SVG — plain text only.

**Navigation Actions:**
- Tap back button → goBack() (restores previous screen and scroll position)
- Tap a variable pill → navigate('variable', { type: 'variable', id: variableSlug })
- Tap a cluster tag → navigate('cluster', { type: 'cluster', id: clusterLetter })

**Components Used:**
- Back button (min 44px)
- Priority alert banner (red, conditional on H. pylori presence)
- Variable pill (tappable, color-coded left border or dot, min 44px height)
- Cluster tag (tappable, color-coded, letter-prefixed)
- Mechanism hierarchy text block

---

### Screen 3: Variable Detail (`screen: 'variable'`)

**Data Displayed:**
- Back button (returns to exact calling screen)
- Variable display name as heading (from DATA.variables[id].name)
- Panel badge: colored per panel color system, text = panel name (MWP / MBA / SHP / GI-MAP / cross-panel)
- "Cross-panel amplifier" badge: displayed only if DATA.variables[id].isCrossPanel === true; optional visual treatment: dashed border or gradient badge
- "What It Is": plain-language 1–2 sentence description of what the marker measures
- "When Elevated" section: DATA.variables[id].elevated (clinical meaning)
- "When Low / Deficient" section: DATA.variables[id].low — if not clinically interpreted, display exactly: "N/A — not interpreted as low in this context"
- "Connected Variables": each variable in DATA.variables[id].connections rendered as a tappable pill (color-coded by that variable's panel)
- "Root Cause Clusters": each cluster in DATA.variables[id].clusters rendered as a colored tappable tag (letter-prefixed)
- For H. pylori: isPriorityPathogen badge or note visible
- For Calprotectin/Lactoferrin and Occult Blood: isMedicalReferral flag — referral language displayed prominently

**Navigation Actions:**
- Tap back button → goBack()
- Tap a connected variable pill → navigate('variable', { type: 'variable', id: connectedVariableSlug })
- Tap a cluster tag → navigate('cluster', { type: 'cluster', id: clusterLetter })

**Components Used:**
- Back button (min 44px)
- Panel badge (color-coded)
- Cross-panel amplifier badge (conditional)
- Medical referral badge/banner (conditional)
- Priority pathogen badge (conditional)
- Connected variable pills (tappable, color-coded)
- Cluster tags (tappable, color-coded)

---

### Screen 4: Cluster Detail (`screen: 'cluster'`)

**Data Displayed:**
- Back button
- Cluster letter + full name as heading, styled with cluster color: e.g., "A: GI Ecosystem Collapse"
- Plain-language mechanism description (1–2 sentences from DATA.clusters[id].mechanism)
- Priority Note section:
  - Cluster A: "Address before all others — GI dysfunction drives all downstream clusters."
  - Cluster E: "MEDICAL REFERRAL REQUIRED before FDN interventions. Refer to physician immediately."
  - Clusters B, C, D: no priority note displayed
- "Variables in This Cluster": all variables from DATA.clusters[id].variables rendered as tappable pills (color-coded by each variable's panel)
- "Symptoms Associated": reverse-mapped list — all symptoms whose clusters array includes this cluster letter, each rendered as a tappable card

**Navigation Actions:**
- Tap back button → goBack()
- Tap a variable pill → navigate('variable', { type: 'variable', id: variableSlug })
- Tap a symptom card → navigate('symptom', { type: 'symptom', id: symptomSlug })

**Components Used:**
- Back button (min 44px)
- Cluster heading (color-coded)
- Priority note block (conditional on cluster letter)
- Variable pills (tappable, color-coded)
- Symptom cards (tappable, min 44px height, reverse-mapped from DATA.symptoms)

---

### Screen 5: Search (`screen: 'search'`)

**Data Displayed:**
- Search input (focused on screen entry; real-time filtering at 2+ characters)
- When query is fewer than 2 characters: empty state or prompt
- When query is 2+ characters:
  - "Symptoms" heading + filtered symptom cards (match against DATA.symptoms[id].label)
  - "Variables" heading + filtered variable pills (match against DATA.variables[id].name)
  - Each section only rendered if it has results

**Navigation Actions:**
- Tap a symptom result card → navigate('symptom', { type: 'symptom', id: symptomSlug })
- Tap a variable result pill → navigate('variable', { type: 'variable', id: variableSlug })
- Tap bottom nav "Home" tab → navigate('home', null)
- Tap bottom nav "Clusters" tab → navigate('cluster-list', null)

**Components Used:**
- Search input (focused, controlled)
- Symptoms results section with symptom cards
- Variables results section with variable pills
- Bottom navigation bar

---

## Navigation Model

### Stack-Based Navigation

The app uses a JS array as a history stack. There is no use of the browser History API, no page reloads, and no URL changes.

**navigate(screen, item):**
1. Push the current state snapshot onto state.stack: `{ screen: state.screen, item: state.item, scrollY: currentScrollY }`
2. Set state.screen = screen
3. Set state.item = item
4. Re-render the app from the new state
5. Apply CSS slide-left transition (forward navigation)

**goBack():**
1. If state.stack is empty: no-op (already at root)
2. Pop the last entry from state.stack: `const prev = state.stack.pop()`
3. Set state.screen = prev.screen
4. Set state.item = prev.item
5. Re-render from restored state
6. Restore scroll position: `window.scrollTo(0, prev.scrollY)`
7. Apply CSS slide-right transition (backward navigation)

**Transition Animations:**
- Forward (navigate): CSS transform slide-left — new screen enters from the right, old screen exits to the left
- Back (goBack): CSS transform slide-right — previous screen enters from the left, current screen exits to the right
- Implemented as CSS transitions only (transform + opacity on a wrapper element)
- No setTimeout, no JS animation libraries, no requestAnimationFrame for animation logic

**Bottom Navigation:**
- Always rendered and visible; not part of the scrollable content area
- Active tab is highlighted (CSS class based on state.screen)
- Tapping a bottom nav tab that is already active: no-op or scroll-to-top
- 3 tabs only: Home | Search | Clusters

---

## State Machine Spec

```
state = {
  screen: 'home' | 'symptom' | 'variable' | 'cluster' | 'search',
  item: { type: 'symptom' | 'variable' | 'cluster', id: string } | null,
  stack: Array<{ screen: string, item: object | null, scrollY: number }>,
  searchQuery: string,
  expandedCategories: Set<string>,
  scrollPositions: Map<string, number>
}
```

**Field Semantics:**

- `screen`: The currently rendered screen identifier. Drives the top-level render switch.
- `item`: The currently displayed entity. null on home and search screens. On symptom screen: { type: 'symptom', id: symptomSlugId }. On variable screen: { type: 'variable', id: variableSlugId }. On cluster screen: { type: 'cluster', id: clusterLetter }.
- `stack`: LIFO array of previous { screen, item, scrollY } snapshots. Each navigate() call pushes the current state before transitioning. Each goBack() call pops and restores. The stack enables multi-level back navigation: Variable → Symptom → Home, each goBack() step restoring the correct screen.
- `searchQuery`: The current search input string. Persists across navigate/goBack calls so the search field is not cleared when returning to the search screen.
- `expandedCategories`: A Set of category name strings that are currently expanded in the home screen accordion. Persists through navigation so category expansion state is restored when the user navigates back to home.
- `scrollPositions`: A Map keyed by a unique screen+item string (e.g., 'symptom:bloating') to the last scrollY position on that screen. Used to restore scroll position precisely on goBack(). The stack also captures scrollY at navigate() time for the same purpose.

**Initial State:**
```
state = {
  screen: 'home',
  item: null,
  stack: [],
  searchQuery: '',
  expandedCategories: new Set(),
  scrollPositions: new Map()
}
```

---

## Data Relationships

### Reverse Map: Clusters → Symptoms

The cluster detail screen must display "Symptoms Associated" — all symptoms that belong to a given cluster.

**Do not hardcode this mapping.** Instead, compute it programmatically:

```js
function getSymptomsForCluster(clusterLetter) {
  return Object.entries(DATA.symptoms)
    .filter(([id, symptom]) => symptom.clusters.includes(clusterLetter))
    .map(([id, symptom]) => ({ id, ...symptom }));
}
```

**Why programmatic:** Any future addition or edit to a symptom's clusters array automatically propagates to all cluster detail screens without requiring a separate hardcoded reverse-map to be updated. Single source of truth is DATA.symptoms.

### Reverse Map: Variables → Symptoms

A variable detail screen may need to show "Symptoms that involve this variable" (not currently in the MUST requirements, but supportable).

```js
function getSymptomsForVariable(variableId) {
  // variableId is the display name as used in symptom.variables arrays
  return Object.entries(DATA.symptoms)
    .filter(([id, symptom]) => symptom.variables.includes(variableId))
    .map(([id, symptom]) => ({ id, ...symptom }));
}
```

**Why programmatic:** Same reason — DATA.symptoms is the single source of truth for all symptom-variable associations. Hardcoding a per-variable symptom list would create two places to maintain the same information and introduce drift.

### Variable Name Resolution

Within symptom entries, variables are stored as display name strings (e.g., "Cortisol Diurnal Pattern"). Within DATA.variables, keys are slug IDs (e.g., "cortisol-diurnal-pattern"). A lookup helper is needed:

```js
function getVariableByName(displayName) {
  return Object.entries(DATA.variables)
    .find(([id, v]) => v.name === displayName);
}
```

Alternatively, symptom entries can store variable slug IDs directly (preferred for performance), with display names resolved through DATA.variables[id].name for rendering.

### Panel Color Resolution

Variable pills and badges are colored by panel. The panel-to-color map:

```js
const PANEL_COLORS = {
  'MWP':         '#e07c3a',
  'MBA':         '#3abde0',
  'SHP':         '#8b5cf6',
  'GI-MAP':      '#22c55e',
  'cross-panel': '#94a3b8'
};
```

### Cluster Color Resolution

```js
const CLUSTER_COLORS = {
  A: '#ef4444',
  B: '#f97316',
  C: '#ec4899',
  D: '#06b6d4',
  E: '#fbbf24'
};
```

---

## Category Order

The exact ordered list of all 14 symptom categories as they must appear in the home screen accordion (top to bottom):

1. Energy & Fatigue
2. Sleep
3. Mood & Emotions
4. Digestion
5. Food Reactions
6. Skin
7. Immune System
8. Hormonal (Female)
9. Hormonal (Male & Shared)
10. Cardiovascular & Circulatory
11. Pain & Inflammation
12. Respiratory
13. Cognitive & Neurological
14. Stress & Nervous System

Note: The source knowledge base lists 13 categories in the overview section but 14 are defined in the requirements section. "Hormonal (Female)" and "Hormonal (Male & Shared)" are two separate categories — the "13" figure in the overview was a slight undercount. The canonical 14-category ordered list above reflects the full requirements specification and the actual symptom data.
