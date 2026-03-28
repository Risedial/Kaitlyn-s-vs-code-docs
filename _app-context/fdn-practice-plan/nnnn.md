# FDN Practice Plan Feature — Implementation Specification

---

## Architecture

**Target file:** `fdn-pwa/index.html` — all new code added here, no new files created.

**Pattern:** Single-file PWA with embedded CSS and JavaScript. New code follows the existing event-delegation routing model, screen section pattern, and data object structure already present in the codebase.

**Prerequisites before coding:**
1. Verify that `DATA.symptoms[id].clusters[]` arrays exist in the current data layer
2. Verify that a persistent multi-select symptom selection state (array of currently selected symptom IDs accessible across screens) exists or confirm it must be added
3. If the persistent selection state does not exist, add a `selectedSymptomIds: []` array to the app's top-level state before implementing the Plan feature
4. Read all course content files in `research-source-content/course/` — all `DATA.dressPractices` content must be authored from these files before writing code

---

## Data Layer

### DATA.dressPractices

Add alongside `DATA.symptoms` and `DATA.variables` in the JavaScript data layer.

Structure — each entry:
```js
{
  id: 'string',            // kebab-case unique identifier, e.g. 'sleep-window-10pm'
  dresComponent: 'string', // one of: 'diet' | 'rest' | 'exercise' | 'stress' | 'supplement'
  title: 'string',         // plain-language practice name, shown collapsed, no clinical terms
  action: 'string',        // exact step-by-step instructions from course module
  why: 'string',           // one plain-language sentence: why this helps their symptoms
  frequency: 'string',     // one of: 'daily' | 'weekly' | 'as-needed'
  clusters: ['A'],         // array of cluster codes that trigger this practice
  priority: 7,             // integer 1–10, inherent importance independent of symptom count
  module: '10'             // non-displayed; FDN course module number for content audit
}
```

**Content rules enforced during data construction:**
- Every `action` and `why` value authored directly from the named `module` file in `research-source-content/course/`
- No clinical abbreviations in `title`, `action`, or `why` without immediate plain-language definition
- Supplementation entries limited to foundational course-level guidance only — no dosages, brands, or lab-dependent protocols
- `why` sentences use first-person framing: "This helps your body..." not "Studies show..."

### Cluster-to-DRESS mapping

| Cluster | Maps to DRESS components |
|---|---|
| A | diet, stress |
| B | rest, stress, exercise |
| C | diet, stress |
| D | diet, stress |
| E | rest, stress + referral notice |

### Course module sourcing by DRESS component

| Component | Source modules |
|---|---|
| Diet | Module 09: blood sugar stabilization, eliminate refined carbs for 90-day reset, fiber + protein + fat at every meal, track satiety and energy response |
| Rest | Module 10: consistent 10 PM–6 AM sleep window, blackout/cool/quiet sleep environment, no screens 2 hours before bed, small protein + low-glycemic carb snack before sleep |
| Exercise | Module 11: mobility work and active recovery first; progress to resistance training and HIIT as recovery improves |
| Stress Reduction | Module 12: half ounce water per pound of body weight daily, minimum one bowel movement per day, reduce environmental toxin exposure (organic produce, water filtration, avoid nonstick cookware), deliberate daily laughter |
| Supplementation | Module 10: foundational mineral support before sleep — no dosages, no brands |

---

## Mapping and Calculation Functions

### getActiveClusters(selectedSymptomIds)
- Input: array of selected symptom ID strings
- Process: for each ID, read `DATA.symptoms[id].clusters[]`; flatten all arrays into one; deduplicate
- Output: deduplicated array of cluster code strings, e.g. `['A', 'B']`

### getPracticesForClusters(clusters)
- Input: active cluster array from `getActiveClusters`
- Process: filter `DATA.dressPractices` where `practice.clusters` intersects with active clusters; deduplicate by `id`; compute priority score for each: `(count of user's active symptom entries that triggered this practice) × practice.priority`
- Output: array of practice objects with a computed `score` property, sorted by `score` descending

### getTopPractices(practices, n)
- Input: sorted practice array from `getPracticesForClusters`, `n` = 7
- Output: first `n` items (Focus Mode)

### groupByDressComponent(practices)
- Input: practice array
- Output: Map with keys `'diet' | 'rest' | 'exercise' | 'stress' | 'supplement'`, each value = array of practices for that component, sorted by score descending

### renderPlanScreen()
- Reads current `selectedSymptomIds` from app state
- Reads `localStorage` `'fdn-plan-state'` (or initializes defaults)
- Calls `getActiveClusters` → `getPracticesForClusters`
- Detects Cluster E presence for referral notice
- Checks `lastSymptomHash` against current hash; shows banner if mismatch
- Renders screen based on `viewMode` (`'focus'` or `'full'`)
- Pattern: consistent with existing `renderXxxScreen()` functions in the codebase

### togglePracticeComplete(practiceId)
- Reads `fdn-plan-state` from `localStorage`
- Adds or removes `practiceId` from `completedIds`
- Writes back to `localStorage`
- Triggers visual update on the target card (no full re-render)

### computeSymptomHash(selectedSymptomIds)
- Input: array of selected symptom IDs
- Process: sort IDs, join with `','`, produce a simple string hash
- Output: string used as `lastSymptomHash` in storage state

---

## State Management

### localStorage schema
```js
// key: 'fdn-plan-state'
{
  completedIds: [],         // string[] of practice IDs the user has checked
  viewMode: 'focus',        // 'focus' | 'full'
  lastSymptomHash: ''       // hash of symptom selection at last plan render
}
```

**Default on first visit:** `{ completedIds: [], viewMode: 'focus', lastSymptomHash: '' }`

**On plan recalculation (symptom hash mismatch):** Filter `completedIds` to retain only IDs present in the new practice list. Silently drop the rest. Update `lastSymptomHash`.

**State reset:** No daily reset. No automatic clearing. Persists until the user manually unchecks items or clears browser data.

---

## HTML Structure

### Bottom navigation — fifth tab (add after existing four tabs)
```html
<button
  class="nav-tab"
  data-tab="plan"
  data-action="navigate-tab"
  aria-label="My Plan"
>
  <!-- SVG checklist icon, matching existing tab icon dimensions -->
  <span class="nav-label">My Plan</span>
  <span class="nav-badge" id="plan-badge" aria-hidden="true"></span>
</button>
```

Badge visibility: show `.nav-badge` when `selectedSymptomIds.length > 0`. Badge is a small filled dot using `--accent`.

### Plan screen section (add alongside existing screen sections)
```html
<section id="screen-plan" class="screen" aria-label="My Plan" hidden>

  <!-- Cluster E referral notice — rendered conditionally above all cards -->
  <div id="plan-referral-notice" class="alert-referral" hidden>
    <!-- Plain-language physician referral notice, matching existing isMedicalReferral pattern -->
  </div>

  <!-- Symptom-change banner — rendered conditionally -->
  <div id="plan-refresh-banner" class="banner-notice" hidden>
    Your symptoms have changed. Refresh your plan?
    <button data-action="refresh-plan">Refresh</button>
  </div>

  <!-- Plan header -->
  <header class="plan-header">
    <h2>Your Practice Plan</h2>
    <p id="plan-subtitle" class="text-secondary">Based on 0 symptoms you selected</p>
  </header>

  <!-- Mode toggle -->
  <div class="plan-mode-toggle" role="tablist" aria-label="Plan view mode">
    <button
      class="mode-btn active"
      data-mode="focus"
      role="tab"
      aria-selected="true"
    >Focus Mode</button>
    <button
      class="mode-btn"
      data-mode="full"
      role="tab"
      aria-selected="false"
    >Full Plan</button>
  </div>

  <!-- Mode explainer — collapsible one-line, toggles per active mode -->
  <p id="plan-mode-explainer" class="mode-explainer text-secondary"></p>

  <!-- Practice list container — populated by renderPlanScreen() -->
  <div id="plan-practice-list" class="practice-list"></div>

  <!-- Empty state — shown when no symptoms selected -->
  <div id="plan-empty-state" class="empty-state" hidden>
    Select symptoms on the Search tab to see your personalized plan.
  </div>

</section>
```

---

## Practice Card HTML Pattern

### Collapsed (default) state
```html
<div
  class="practice-card"
  data-practice-id="[id]"
  data-expanded="false"
>
  <div class="practice-card-header" data-action="toggle-practice-expand">
    <span class="cluster-dot cluster-[x]" aria-hidden="true"></span>
    <span class="practice-title">[title]</span>
    <span class="frequency-pill frequency-[daily|weekly|as-needed]">[Daily|Weekly|As needed]</span>
    <button
      class="practice-checkbox"
      data-action="toggle-practice-complete"
      data-practice-id="[id]"
      aria-label="Mark [title] as complete"
      aria-pressed="false"
    >
      <!-- SVG checkmark icon -->
    </button>
  </div>
  <div class="practice-card-body" hidden>
    <p class="practice-what-label">What to do</p>
    <p class="practice-action">[action]</p>
    <p class="practice-why-label">Why this helps</p>
    <p class="practice-why">[why]</p>
  </div>
</div>
```

### Expanded state
- Set `data-expanded="true"` on `.practice-card`
- Remove `hidden` from `.practice-card-body`
- Apply smooth CSS transition (match existing `.accordion-header` animation pattern)

### Completed state
- Set `aria-pressed="true"` on `.practice-checkbox`
- Add class `practice-complete` to `.practice-card`
- `.practice-complete .practice-title` → color: `var(--text-secondary)`
- `.practice-complete .practice-card-header` → opacity: 0.6
- CSS animation on checkmark SVG: scale 1 → 1.3 → 1, opacity 0 → 1, duration 200ms

---

## Full Plan Mode — Section HTML Pattern

```html
<details class="dress-section" open>
  <summary class="dress-section-header">
    [Plain-language component name] — [N] practices
  </summary>
  <div class="dress-section-body">
    <!-- practice cards for this component -->
  </div>
</details>
```

DRESS component display names:
- `'diet'` → "Diet"
- `'rest'` → "Rest"
- `'exercise'` → "Exercise"
- `'stress'` → "Stress Reduction"
- `'supplement'` → "Supplementation"

Sections default to `open` on every render. Section collapse state is not persisted.

---

## CSS — New Classes

All new classes use existing CSS variable tokens exclusively. No new custom properties introduced.

```css
/* Practice card */
.practice-card {
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  margin-bottom: var(--space-sm);
  overflow: hidden;
}

.practice-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
  padding: var(--space-md);
  min-height: 44px;
  cursor: pointer;
  user-select: none;
}

.practice-title {
  flex: 1;
  font-weight: 600;
  color: var(--text-primary);
  font-size: var(--text-md);
}

.practice-complete .practice-title {
  color: var(--text-secondary);
}

.practice-complete .practice-card-header {
  opacity: 0.6;
}

.frequency-pill {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  background: var(--bg-primary);
  border-radius: 99px;
  padding: 2px 8px;
  white-space: nowrap;
}

.practice-card-body {
  padding: 0 var(--space-md) var(--space-md);
  border-top: 1px solid var(--border-subtle);
}

.practice-card-body p {
  color: var(--text-primary);
  font-size: var(--text-sm);
  line-height: 1.5;
  margin-bottom: var(--space-xs);
}

.practice-what-label,
.practice-why-label {
  font-weight: 600;
  color: var(--text-secondary);
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-top: var(--space-sm);
}

/* Cluster dot indicator */
.cluster-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.cluster-dot.cluster-A { background: var(--cluster-a); }
.cluster-dot.cluster-B { background: var(--cluster-b); }
.cluster-dot.cluster-C { background: var(--cluster-c); }
.cluster-dot.cluster-D { background: var(--cluster-d); }
.cluster-dot.cluster-E { background: var(--cluster-e); }

/* Completion checkmark animation */
@keyframes check-pop {
  0%   { transform: scale(1); opacity: 0; }
  50%  { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}
.practice-checkbox[aria-pressed="true"] svg {
  animation: check-pop 200ms ease-out forwards;
  color: var(--accent);
}

/* Mode toggle */
.plan-mode-toggle {
  display: flex;
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  padding: 2px;
  margin-bottom: var(--space-sm);
}
.mode-btn {
  flex: 1;
  padding: var(--space-xs) var(--space-sm);
  border-radius: calc(var(--radius-md) - 2px);
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text-secondary);
  background: transparent;
  border: none;
  cursor: pointer;
  min-height: 44px;
}
.mode-btn.active {
  background: var(--bg-primary);
  color: var(--accent);
  font-weight: 600;
}

/* Mode explainer */
.mode-explainer {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  margin-bottom: var(--space-md);
  padding: 0 var(--space-xs);
}

/* DRESS section (Full Plan) */
.dress-section {
  margin-bottom: var(--space-sm);
}
.dress-section-header {
  font-weight: 600;
  color: var(--text-primary);
  font-size: var(--text-md);
  padding: var(--space-sm) 0;
  cursor: pointer;
  list-style: none;
}

/* Plan header */
.plan-header {
  margin-bottom: var(--space-md);
}
.plan-header h2 {
  font-size: var(--text-xl);
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--space-xs);
}

/* Nav badge */
.nav-badge {
  display: none;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  position: absolute;
  top: 6px;
  right: 6px;
}
.nav-badge.visible {
  display: block;
}

/* Referral notice */
.alert-referral {
  background: var(--bg-secondary);
  border-left: 3px solid var(--cluster-e);
  border-radius: var(--radius-md);
  padding: var(--space-md);
  margin-bottom: var(--space-md);
  color: var(--text-primary);
  font-size: var(--text-sm);
  line-height: 1.5;
}

/* Refresh banner */
.banner-notice {
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  padding: var(--space-sm) var(--space-md);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-md);
  font-size: var(--text-sm);
  color: var(--text-secondary);
}
```

---

## Event Delegation — New Actions

Register these in the existing event delegation handler (no new event listeners):

| `data-action` value | Handler behavior |
|---|---|
| `navigate-tab` with `data-tab="plan"` | Navigate to `#screen-plan` (reuse existing tab navigation logic) |
| `toggle-practice-expand` | Toggle `data-expanded` on parent `.practice-card`; show/hide `.practice-card-body` |
| `toggle-practice-complete` | Call `togglePracticeComplete(practiceId)` |
| `refresh-plan` | Recalculate plan (call `renderPlanScreen()` with forced recalculation); hide banner |

---

## Edge Cases — Exact Behavior

| Scenario | Behavior |
|---|---|
| No symptoms selected | Hide all practice content; show `#plan-empty-state`; hide badge |
| Cluster E symptom selected | Show `.alert-referral` as first visible element above all cards; still show rest/stress practices below |
| Only Cluster E symptoms selected | Show referral notice + baseline rest/stress practices (universal foundational practices included in `DATA.dressPractices` with `clusters: ['A','B','C','D','E']`) |
| Single symptom selected | Render 2–3 practice cards; Focus and Full Plan may look nearly identical; toggle still rendered |
| All symptoms selected | Focus Mode cap at 7 enforced; Full Plan renders all, grouped in collapsible sections |
| Symptoms changed mid-session | On next Plan tab visit, detect hash mismatch; show `#plan-refresh-banner`; do not auto-recalculate |
| Refresh tapped | Recalculate; filter `completedIds` to retain valid IDs; update `lastSymptomHash`; hide banner |
| App used offline | All functionality works; no API calls; service worker cache covers `index.html` |
| Practice in multiple clusters | Deduplicate by `id`; appears once; rises in Focus Mode naturally via priority score |

---

## Content Integrity Protocol

Before writing a single line of implementation code:

1. Read each module file in `research-source-content/course/` corresponding to the DRESS components
2. Author all `DATA.dressPractices` entries — every `action` and `why` field sourced from named module text
3. Assign `module` field values (e.g., `"10"` for Module 10 rest practices)
4. Calibrate `priority` integers: sleep window and blood sugar stabilization = highest (9–10); broadly foundational course practices = 7–8; component-specific practices = 4–6; supplementation = 3–5
5. Review all user-visible strings against the plain-language test: a person with no health background can read it and immediately understand it
6. Verify no practice entry contains content that cannot be traced to its named module

---

## Non-Goals (Out of Scope — Do Not Implement)

- No backend, database, user accounts, or authentication
- No third-party health APIs, tracking services, or analytics
- No modifications to existing symptom selection, search, cluster, or educational features
- No daily reset of completion state
- No streaks, scores, badges, or gamification
- No push notifications, reminders, or scheduled alerts
- No synchronization across devices or sessions
- No symptom progression or health outcome tracking
- No metabolic type individualization
- No specific supplement dosages, brands, or lab-dependent protocols
- No new JavaScript library imports or CDN dependencies
- No new files — all code in `index.html` only
