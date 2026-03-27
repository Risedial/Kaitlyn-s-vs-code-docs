## The Prompt

<role>
You are a senior frontend developer implementing a new feature in an existing production Progressive Web App (PWA). Your expertise covers vanilla JavaScript, CSS custom property systems, localStorage state management, and event-delegation routing patterns. You have zero knowledge of functional medicine — every health claim, action step, and "why" sentence you write MUST be sourced word-for-word or closely paraphrased from the course module files provided. You do not supplement from memory or training knowledge.
</role>

<context>
The FDN (Functional Diagnostic Nutrition) PWA is a single-file app at `fdn-pwa/index.html`. It currently allows users to select symptoms from a searchable list, view cluster assignments, and read educational content. The app uses:
- Vanilla JavaScript with event delegation (one top-level listener on `document`, dispatching by `data-action` attribute)
- A `DATA` object containing `DATA.symptoms` and `DATA.variables`
- Screen sections toggled via `#screen-[name]` IDs and a `data-tab` routing pattern
- CSS custom property tokens (`--bg-primary`, `--bg-secondary`, `--text-primary`, `--text-secondary`, `--accent`, `--radius-md`, `--space-sm/md/lg`, `--text-xs/sm/md/xl`, `--border-subtle`, `--cluster-a` through `--cluster-e`)
- `localStorage` for all persistence; no backend, no server calls
- A service worker enabling full offline operation

The feature to add is called "My Plan" — a fifth navigation tab and a `#screen-plan` section that converts the user's selected symptoms into a personalized, actionable daily and weekly practice plan based on the DRESS protocol (Diet, Rest, Exercise, Stress Reduction, Supplementation) from the FDN certification course.

**Critical architectural risk:** The entire feature depends on `DATA.symptoms[id].clusters[]` arrays existing in the current data layer AND a persistent `selectedSymptomIds` array being accessible across screens. Verify both exist before writing any feature code.
</context>

<prerequisites>
Complete all steps in PHASE 0 and PHASE 1 in order. Do not begin Phase 2 implementation until Phase 1 is fully verified.

**PHASE 0 — Prerequisite Verification**

Step 1: Read `fdn-pwa/index.html` in full.

Step 2: Verify that `DATA.symptoms` entries each contain a `clusters` array field. If this field does not exist on symptom entries, add `clusters: []` arrays to all symptom entries with the correct cluster assignments as a prerequisite step before proceeding.

Step 3: Verify that a `selectedSymptomIds` array (or equivalent persistent multi-select selection state) is accessible across screens from app state. If it does not exist, add `selectedSymptomIds: []` to the top-level app state object before proceeding.

Step 4: Record the exact names of the existing render functions (e.g., `renderXxxScreen()`), the event delegation handler function, and the tab navigation logic so you can match their naming and coding patterns exactly.

**PHASE 1 — Content Authoring (MUST be complete before Phase 2)**

Step 5: Read every course file in `research-source-content/course/` that maps to a DRESS component:
- Diet content → Module 09: blood sugar stabilization, eliminate refined carbs for 90-day reset, fiber + protein + fat at every meal, track satiety and energy response
- Rest content → Module 10: consistent 10 PM–6 AM sleep window, blackout/cool/quiet sleep environment, no screens 2 hours before bed, small protein + low-glycemic carb snack before sleep
- Exercise content → Module 11: mobility work and active recovery first; progress to resistance training and HIIT as recovery improves
- Stress Reduction content → Module 12: half ounce water per pound of body weight daily, minimum one bowel movement per day, reduce environmental toxin exposure, deliberate daily laughter
- Supplementation content → Module 10: foundational mineral support before sleep — foundational guidance only

Step 6: Author all `DATA.dressPractices` entries. For every entry:
- Write `action` directly from the course module text — no synthesis, no paraphrase from training memory
- Write `why` as one plain-language sentence sourced from the module — use first-person framing: "This helps your body..." not "Studies show..."
- Set `module` to the specific module number used (e.g., `"09"`, `"10"`)
- Apply the plain-language test to every string: can a person with no health background read it and immediately understand what to do? If NO, rewrite.
- Confirm no clinical abbreviations (HPA, HPA-T, GI, SIBO, etc.) appear without an immediate plain-language definition in parentheses

Step 7: Calibrate `priority` integers (1–10):
- 9–10: Sleep window (10 PM–6 AM) and blood sugar stabilization — highest impact, most broadly applicable
- 7–8: Broadly foundational course-level practices applicable across multiple clusters
- 4–6: Component-specific practices with moderate cluster overlap
- 3–5: Supplementation entries

Step 8: Verify content integrity — for each practice entry, you MUST be able to state the exact module number and the passage from which `action` and `why` were derived. If you cannot trace a string to a specific module, delete it and rewrite from the source text.
</prerequisites>

<task>
After completing all prerequisite phases, implement the "My Plan" feature by modifying `fdn-pwa/index.html` only. No new files. No new dependencies.

Implement in this exact order:

**1. Data layer** — Add `DATA.dressPractices` array to the JavaScript data object alongside `DATA.symptoms` and `DATA.variables`. Each entry structure:
```js
{
  id: 'string',            // kebab-case unique identifier, e.g. 'sleep-window-10pm'
  dresComponent: 'string', // one of: 'diet' | 'rest' | 'exercise' | 'stress' | 'supplement'
  title: 'string',         // plain-language practice name, shown collapsed, no clinical terms
  action: 'string',        // exact step-by-step instructions from course module
  why: 'string',           // one plain-language sentence: why this helps their symptoms
  frequency: 'string',     // one of: 'daily' | 'weekly' | 'as-needed'
  clusters: ['A'],         // array of cluster codes that trigger this practice
  priority: 7,             // integer 1–10
  module: '10'             // non-displayed; FDN course module number for content audit
}
```

**2. Utility functions** — Add to the JavaScript section:
- `getActiveClusters(selectedSymptomIds)` — for each ID, read `DATA.symptoms[id].clusters[]`; flatten all arrays; deduplicate; return array of cluster code strings (e.g., `['A', 'B']`)
- `getPracticesForClusters(clusters)` — filter `DATA.dressPractices` where `practice.clusters` intersects with active clusters; deduplicate by `id`; compute score per practice: `(count of user's active symptom entries that triggered this practice) × practice.priority`; sort by score descending; return array with computed `score` property
- `getTopPractices(practices, n=7)` — return first `n` items (Focus Mode list)
- `groupByDressComponent(practices)` — return Map with keys `'diet' | 'rest' | 'exercise' | 'stress' | 'supplement'`, each value an array of practices sorted by score descending
- `computeSymptomHash(selectedSymptomIds)` — sort IDs, join with `','`, return as string

**3. State management functions** — Add:
- `getPlanState()` — reads `localStorage['fdn-plan-state']`; returns parsed JSON; if absent, returns default: `{ completedIds: [], viewMode: 'focus', lastSymptomHash: '' }`
- `setPlanState(state)` — serializes with `JSON.stringify` and writes to `localStorage['fdn-plan-state']`
- `togglePracticeComplete(practiceId)` — reads state; toggles `practiceId` in `completedIds` (add if absent, remove if present); calls `setPlanState`; applies or removes `practice-complete` class and updates `aria-pressed` on the target card directly (no full re-render)

**4. Render function** — Add `renderPlanScreen()`, consistent with existing `renderXxxScreen()` naming and pattern:
- Reads `selectedSymptomIds` from app state
- Reads plan state via `getPlanState()`
- Calls `getActiveClusters` → `getPracticesForClusters`
- If `selectedSymptomIds.length === 0`: shows `#plan-empty-state`, hides all other plan content, stops
- Detects Cluster E in active clusters — if present, removes `hidden` from `#plan-referral-notice`
- Calls `computeSymptomHash(selectedSymptomIds)` — if result !== `planState.lastSymptomHash`, removes `hidden` from `#plan-refresh-banner`; does NOT auto-recalculate
- Updates `#plan-subtitle` text: `"Based on [N] symptoms you selected"`
- Updates `#plan-mode-explainer` text to the exact string for the active mode
- Renders practice list in `#plan-practice-list` based on `planState.viewMode`:
  - `'focus'`: flat list of `getTopPractices(practices, 7)`
  - `'full'`: `<details>` sections from `groupByDressComponent(practices)`
- Applies `practice-complete` class and `aria-pressed="true"` to cards whose IDs are in `completedIds`

**5. HTML — Navigation tab** — Add as the fifth `<button class="nav-tab">` in the bottom navigation:
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

**6. HTML — Plan screen section** — Add `<section id="screen-plan" class="screen" aria-label="My Plan" hidden>` alongside existing screen sections, containing exactly:
```html
<section id="screen-plan" class="screen" aria-label="My Plan" hidden>

  <div id="plan-referral-notice" class="alert-referral" hidden>
    <!-- Plain-language physician referral notice -->
  </div>

  <div id="plan-refresh-banner" class="banner-notice" hidden>
    Your symptoms have changed. Refresh your plan?
    <button data-action="refresh-plan">Refresh</button>
  </div>

  <header class="plan-header">
    <h2>Your Practice Plan</h2>
    <p id="plan-subtitle" class="text-secondary">Based on 0 symptoms you selected</p>
  </header>

  <div class="plan-mode-toggle" role="tablist" aria-label="Plan view mode">
    <button class="mode-btn active" data-mode="focus" role="tab" aria-selected="true">Focus Mode</button>
    <button class="mode-btn" data-mode="full" role="tab" aria-selected="false">Full Plan</button>
  </div>

  <p id="plan-mode-explainer" class="mode-explainer text-secondary"></p>

  <div id="plan-practice-list" class="practice-list"></div>

  <div id="plan-empty-state" class="empty-state" hidden>
    Select symptoms on the Search tab to see your personalized plan.
  </div>

</section>
```

**7. Practice card HTML pattern** — Use this pattern when rendering each card in `#plan-practice-list`:
```html
<div class="practice-card" data-practice-id="[id]" data-expanded="false">
  <div class="practice-card-header" data-action="toggle-practice-expand">
    <span class="cluster-dot cluster-[X]" aria-hidden="true"></span>
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

**8. Full Plan `<details>` section pattern** — Use for each DRESS component group:
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
DRESS display names: `'diet'` → "Diet", `'rest'` → "Rest", `'exercise'` → "Exercise", `'stress'` → "Stress Reduction", `'supplement'` → "Supplementation". Sections default to `open` on every render; collapse state is not persisted.

**9. CSS** — Add all new classes in the existing stylesheet. Use existing CSS variable tokens only — no new custom properties. Add:
```css
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
.practice-complete .practice-title { color: var(--text-secondary); }
.practice-complete .practice-card-header { opacity: 0.6; }
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
@keyframes check-pop {
  0%   { transform: scale(1); opacity: 0; }
  50%  { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}
.practice-checkbox[aria-pressed="true"] svg {
  animation: check-pop 200ms ease-out forwards;
  color: var(--accent);
}
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
.mode-explainer {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  margin-bottom: var(--space-md);
  padding: 0 var(--space-xs);
}
.dress-section { margin-bottom: var(--space-sm); }
.dress-section-header {
  font-weight: 600;
  color: var(--text-primary);
  font-size: var(--text-md);
  padding: var(--space-sm) 0;
  cursor: pointer;
  list-style: none;
}
.plan-header { margin-bottom: var(--space-md); }
.plan-header h2 {
  font-size: var(--text-xl);
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--space-xs);
}
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
.nav-badge.visible { display: block; }
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

**10. Event delegation — new actions** — Register in the existing delegation handler only. Do not add new `addEventListener()` calls:

| `data-action` value | Handler behavior |
|---|---|
| `navigate-tab` with `data-tab="plan"` | Navigate to `#screen-plan`; call `renderPlanScreen()`; toggle `visible` on `#plan-badge` based on `selectedSymptomIds.length > 0` |
| `toggle-practice-expand` | Use `event.target.closest('.practice-card')` to find the card; toggle `data-expanded`; toggle `hidden` on `.practice-card-body` |
| `toggle-practice-complete` | Use `event.target.closest('[data-practice-id]').dataset.practiceId`; call `togglePracticeComplete(id)` |
| `refresh-plan` | Recalculate: call `renderPlanScreen()` with forced recalculation; filter `completedIds` to retain only IDs present in new practice list; call `computeSymptomHash` and update `lastSymptomHash`; hide `#plan-refresh-banner` |
| Mode toggle button clicked | Update `planState.viewMode`; call `setPlanState`; update `aria-selected` and `active` class on both buttons; update `#plan-mode-explainer` text; re-render `#plan-practice-list` only |

**11. Badge** — After any symptom selection change (wherever selections are modified), show class `visible` on `#plan-badge` when `selectedSymptomIds.length > 0`; remove `visible` when `0`.
</task>

<constraints>

**IS — This implementation:**
- Modifies only `fdn-pwa/index.html` — all new code in this single file
- Uses vanilla JavaScript only — no new library imports, no CDN references
- Stores all plan state in `localStorage` under key `'fdn-plan-state'` only
- Sources all health content from `research-source-content/course/` module files exclusively
- Matches existing CSS custom property tokens, component class naming, and event-delegation routing model
- Works fully offline — no API calls, no network requests

**IS NOT — This implementation does NOT:**
- Create any new files
- Modify any existing tab, screen, component, data structure, or function
- Include push notifications, reminders, daily resets, streaks, scores, badges, or gamification
- Store or transmit user data to any server
- Display supplement dosages, brand recommendations, or lab-dependent protocols
- Import, infer, or use any health content from outside the course files
- Show clinical abbreviations or practitioner-level terminology without inline plain-language definition

**MUST (non-negotiable):**
- Cluster E presence MUST trigger physician referral notice rendered as the first visible element above all practice cards
- Every `action` and `why` field MUST be traceable to a named course module
- Focus Mode MUST cap at 7 practices (top by priority score)
- Minimum touch target MUST be 44px for all interactive elements
- `localStorage` schema MUST exactly match: `{ completedIds: string[], viewMode: 'focus'|'full', lastSymptomHash: string }`

**MUST NOT (critical failure modes):**
- Do NOT synthesize, infer, or generate any health claim from training knowledge — only use text directly from course module files. Factual incorrectness is the primary failure mode in health apps; the only prevention is strict source-grounding to named files.
- Do NOT add any new `addEventListener()` calls — all interactions go through the existing event delegation handler
- Do NOT modify existing tab IDs, screen IDs, function names, or data structures
- Do NOT add any new CSS custom properties — use only existing `--` tokens
- Do NOT implement daily reset, scoring, or gamification logic
- Do NOT display any clinical abbreviation without an immediate plain-language definition in parentheses

**Exact locked values (use verbatim):**

| Item | Value |
|---|---|
| localStorage key | `'fdn-plan-state'` |
| Tab label | `"My Plan"` |
| Screen section ID | `#screen-plan` |
| Tab badge color | `--accent` (#007AFF) |
| Card background | `--bg-secondary` |
| Screen background | `--bg-primary` |
| Active toggle / checkmark | `--accent` |
| Muted/completed text | `--text-secondary` |
| Focus Mode sub-label | `"Showing your highest-impact practices"` |
| Focus Mode explainer | `"Focus Mode shows the practices with the broadest impact on your symptoms. Start here."` |
| Full Plan explainer | `"Full Plan shows every practice recommended for your symptoms, grouped by focus area."` |
| Plan header | `"Your Practice Plan"` |
| Sub-label format | `"Based on [N] symptoms you selected"` |
| Empty state | `"Select symptoms on the Search tab to see your personalized plan."` |
| Symptom-change banner | `"Your symptoms have changed. Refresh your plan?"` |

</constraints>

<edge-cases>
Handle each scenario exactly as specified:

| Scenario | Required behavior |
|---|---|
| No symptoms selected | Hide all practice content; show `#plan-empty-state`; hide `#plan-badge` |
| Cluster E symptom selected | Show `.alert-referral` as first visible element above all cards; still show rest/stress practices below |
| Only Cluster E symptoms selected | Show referral notice + baseline rest/stress practices (universal entries with `clusters: ['A','B','C','D','E']`) |
| Single symptom selected | Render 2–3 practice cards; Focus and Full Plan may look nearly identical; mode toggle still rendered |
| All symptoms selected | Focus Mode cap at 7 enforced; Full Plan renders all, grouped in collapsible `<details>` sections |
| Symptoms changed mid-session | On next Plan tab visit, detect hash mismatch; show `#plan-refresh-banner`; do NOT auto-recalculate |
| Refresh tapped | Recalculate; filter `completedIds` to retain only IDs still in new practice list; update `lastSymptomHash`; hide banner |
| Practice in multiple clusters | Deduplicate by `id`; appears once; rises in Focus Mode naturally via computed score |
| App used offline | All functionality works; no network requests made; service worker cache covers `index.html` |
</edge-cases>

<success-criteria>
The implementation is complete when ALL of the following are verifiable:

1. A user with no prior FDN knowledge navigates to the Plan tab and within 60 seconds can identify exactly what they should do today, when to do it, and why it matters for their symptoms — without reading any documentation.
2. Every `DATA.dressPractices[].action` and `DATA.dressPractices[].why` string can be traced by a reviewer to a specific named module file in `research-source-content/course/` — no string fails this audit.
3. A reviewer comparing the new code to the existing `index.html` cannot identify a stylistic or structural boundary between old and new code — class names, variable names, function names, and comment style all match existing patterns.
4. The Plan tab functions identically with the device in airplane mode: practices load, completion state persists, and the mode toggle works.
5. Selecting any symptom tagged with Cluster E causes the physician referral notice to appear as the topmost visible element on the Plan screen, above all practice cards.
6. Deselecting all symptoms causes the Plan screen to show only the empty state message and no practice cards.
7. Changing the symptom selection and then visiting the Plan tab triggers the "Your symptoms have changed. Refresh your plan?" banner — and tapping Refresh recalculates the plan.
8. No clinical abbreviation or practitioner-level term appears in any user-visible string without an immediate plain-language definition.
9. The `localStorage` key `'fdn-plan-state'` persists completion state across full page refreshes without data loss.
10. All interactive elements have a minimum touch target of 44px.
</success-criteria>

<deliverable>
Modify `fdn-pwa/index.html` in place. All new code added to this single file only.

Before completing, verify:
- All 10 success criteria above are satisfied
- `DATA.dressPractices` contains a minimum of 12 entries, each with a populated `module` field referencing a real course file
- No new files were created
- No new `addEventListener()` calls exist outside the existing delegation handler
- No new CSS custom properties were introduced (only existing `--` tokens used)
- No health claim exists that cannot be traced to a named course module

Do not create a summary or report. Do not output the modified file contents to chat. Modify the file and stop.
</deliverable>

---

## Refinement Report

### Original Source

```
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

[...full nnnn.md content — see file at fdn-practice-plan/nnnn.md]
```

*(Full nnnn.md is 520 lines; the original specification is the complete content of that file.)*

---

### Diagnostic Results

| # | Diagnostic Item | Category | Original Status | How Addressed |
|---|---|---|---|---|
| 1 | XML/semantic tags separate distinct concerns | Structural | Not at all | Full XML section structure added: `<role>`, `<context>`, `<prerequisites>`, `<task>`, `<constraints>`, `<edge-cases>`, `<success-criteria>`, `<deliverable>` |
| 2 | Data-first ordering (context before instructions) | Structural | Partial | Reordered: context → prerequisites → task → constraints → deliverable |
| 3 | Nested structure for compound tasks | Structural | Partial | Phase 0 / Phase 1 / Task Steps 1–11 in explicit numbered sequence |
| 4 | Progressive disclosure (high-level before detail) | Structural | Adequate | Maintained — critical risk stated early in `<context>` |
| 5 | Role assigned to executor | Role & Identity | Not at all | `<role>` assigns senior frontend developer with bounded expertise; explicitly no health knowledge |
| 6 | Expertise domain bounded | Role & Identity | Not at all | Zero-health-knowledge framing added to role; executor MUST source from files, not memory |
| 7 | Audience awareness in framing | Role & Identity | Partial | All framing addressed to implementer; prescriptive, not descriptive |
| 8 | Chain-of-thought phases defined | Reasoning | Partial | Formal phases: Phase 0 (verification), Phase 1 (content authoring), Task Steps 1–11 (implementation) |
| 9 | Self-verification directives | Reasoning | Partial | Phase 1 Step 8: explicit content integrity check before any coding begins |
| 10 | Decision logic for uncertainty | Reasoning | Not at all | Explicit: if prerequisite missing, add it first; if content untraceable, delete and rewrite |
| 11 | Ambiguity eliminated from all terms | Clarity | Adequate | Maintained — all values were precise in original |
| 12 | Active directive voice throughout | Clarity | Partial | All instructions converted to imperative form: "Read", "Verify", "Add", "Author" |
| 13 | MUST/SHOULD/MAY gradients applied | Clarity | Partial | Explicit MUST block added with 5 non-negotiable requirements |
| 14 | IS/IS NOT constraint boundaries | Clarity | Partial | Dedicated IS / IS NOT sections replace scattered constraint descriptions |
| 15 | Do NOT directives for failure modes | Clarity | Partial | 6 MUST NOT directives added targeting the specific failure modes of this domain |
| 16 | Spelling/grammar/terminology | Clarity | Adequate | Maintained |
| 17 | Domain research integrated | Context & Research | Not at all | (1) Content hallucination prevention: "Factual incorrectness is the primary failure mode in health apps; the only prevention is strict source-grounding"; (2) Event delegation: `event.target.closest()` pattern called out explicitly; (3) localStorage: JSON.stringify/parse, persistence pattern confirmed |
| 18 | Few-shot examples provided | Context & Research | Partial | HTML card pattern, section pattern, and data entry structure all retained and labeled as patterns |
| 19 | Reference anchoring | Context & Research | Partial | All module numbers, function names, exact `data-action` values, and localStorage key specified verbatim |
| 20 | Output format fully declared | Output Control | Partial | `<deliverable>` section added: artifact (`fdn-pwa/index.html`), 6 post-completion verification checks, explicit "stop" instruction |
| 21 | Success criteria — 5+ testable assertions | Output Control | Partial | 10 numbered, binary, testable success criteria added |
| 22 | Tone/voice for user-visible content | Output Control | Partial | Plain-language test, first-person framing rule, no-clinical-abbreviation rule all consolidated |
| 23 | Permission to expand — scope boundary explicit | Meta | Partial | IS NOT section provides explicit non-goal boundary; non-goals list preserved |
| 24 | Uncertainty handling | Meta | Not at all | Both architectural risks addressed with explicit fallback instructions (add missing fields/state before proceeding) |
| 25 | Task decomposition into execution sequence | Meta | Partial | 11 implementation steps in explicit order with prerequisites as gated phases |

**Summary:** 4 Adequate (maintained) / 16 Partial (addressed) / 5 Not at all (addressed) → **21/25 items improved**

---

### Techniques Applied

| # | Technique | How Applied | Category |
|---|---|---|---|
| 1 | XML structural tagging | 8 named XML sections wrapping all major concerns | A — Structural |
| 2 | Data-first ordering | Context and prerequisites placed before task instructions; deliverable last | A — Structural |
| 3 | Phase decomposition nesting | Phase 0 → Phase 1 → Task Steps 1–11 in explicit gated sequence | A — Structural |
| 4 | Progressive disclosure | Critical architectural risk surfaced in `<context>` before any instructions | A — Structural |
| 5 | Role assignment | Named expert role (senior frontend developer) assigned with specific capability profile | B — Role & Identity |
| 6 | Expertise scoping | Explicit "zero knowledge of functional medicine" constraint binds executor to source files | B — Role & Identity |
| 7 | Audience-aware framing | All language addressed to an implementer; removed descriptive/declarative passages | B — Role & Identity |
| 8 | Chain-of-thought phase definition | Three formal phases with named goals before any coding begins | C — Reasoning |
| 9 | Self-verification directive | Phase 1 Step 8: content integrity gate that blocks progression to Phase 2 | C — Reasoning |
| 10 | Uncertainty decision logic | Explicit fallback for each missing prerequisite; explicit delete-and-rewrite for untraceable content | C — Reasoning |
| 11 | Ambiguity elimination | All vague terms (e.g., "match existing patterns") replaced with specific function names and attribute values | D — Clarity |
| 12 | Active directive conversion | All "should be", "is expected to", "will" constructions replaced with imperative ("Read", "Add", "Verify") | D — Clarity |
| 13 | MUST/SHOULD/MAY gradients | 5-item MUST block identifies non-negotiable requirements; MUST NOT block identifies hard prohibitions | D — Clarity |
| 14 | IS/IS NOT constraint boundaries | Explicit parallel IS / IS NOT sections replace scattered constraint list | D — Clarity |
| 15 | Do NOT failure mode directives | 6 MUST NOT directives targeting the 6 most likely failure modes in this specific build | D — Clarity |
| 16 | Domain research integration — health content | Research finding (38% factual incorrectness rate in health apps; source-grounding as mitigation) woven into MUST NOT directive | E — Context & Research |
| 17 | Domain research integration — event delegation | `event.target.closest()` pattern explicitly specified in delegation handler section | E — Context & Research |
| 18 | Domain research integration — localStorage | JSON.stringify/parse, storage event behavior, ~5MB limit context informs schema design validation | E — Context & Research |
| 19 | Few-shot HTML patterns | Practice card, screen section, and details/summary patterns provided as labeled copy-paste templates | E — Context & Research |
| 20 | Reference anchoring | Every module number, function name, data-action value, localStorage key, and CSS token specified verbatim | E — Context & Research |
| 21 | Output format declaration | `<deliverable>` specifies artifact, 6 post-completion verification checks, and explicit termination instruction | F — Output Control |
| 22 | Success criteria — 10 testable assertions | 10 binary testable conditions covering UX, content integrity, offline behavior, and technical compliance | F — Output Control |
| 23 | Voice/framing specification | Plain-language test, first-person "why" framing, and abbreviation rule consolidated in Phase 1 | F — Output Control |
| 24 | Permission-to-expand boundary | IS NOT section provides explicit non-goal boundary; prevents scope creep | G — Meta |
| 25 | Task decomposition with gate conditions | Phases are gated: Phase 1 must complete before Phase 2; content integrity check must pass before coding | G — Meta |

**Total techniques applied: 25**

---

### Domain Research Conducted

**Search 1: Vanilla JS PWA feature addition and event delegation best practices (2026)**

Key findings integrated:
- Event delegation with `event.target.closest()` is the correct traversal pattern for dynamically generated card elements. This is explicitly specified in the task section for `toggle-practice-expand` and `toggle-practice-complete` handlers.
- Non-bubbling events (blur, focus, mouseenter) cannot be delegated — not applicable here but confirmed no new event listeners are needed for this feature.
- Cache-first strategy for static assets is correct pattern for this offline-first app. The existing service worker covers `index.html`.

**Search 2: localStorage state management and hash-based change detection in vanilla JS SPAs**

Key findings integrated:
- All localStorage values MUST be serialized with `JSON.stringify` before write and parsed with `JSON.parse` on read. `getPlanState()` and `setPlanState()` functions specified with these requirements.
- Hash-based change detection (symptom selection hash vs. stored hash) is a standard SPA pattern for detecting stale persisted state. The `computeSymptomHash` → `lastSymptomHash` comparison pattern is validated by this research.
- Batch DOM updates (update card directly in `togglePracticeComplete` without full re-render) minimizes layout thrashing — confirmed in no-full-rerender directive.

**Search 3: Health wellness app content integrity and hallucination prevention**

Key findings integrated:
- Factual incorrectness accounts for 38% of user-reported LLM hallucinations in health apps; fabricated information accounts for 15%. Combined, over half of health content failures are ungrounded claims.
- The primary mitigation: "Please only answer out of the information I provided" — operationalized in this prompt as the zero-health-knowledge role framing + mandatory Phase 1 content authoring from source files + MUST NOT directive.
- Rule-based post-processing validation is the recommended enterprise approach — operationalized here as the 6-item post-completion verification checklist in `<deliverable>` and the 10-item success criteria.
- The content integrity gate (Phase 1 Step 8: every string must be traceable to a module number before any code is written) directly addresses the highest-risk failure mode for this specific domain.
