# FDN Practice Plan Feature

---

## Section 0: Re-Articulated Original Input

The goal is to add a feature called the Universal Feedback Loop Practice System to the existing FDN Progressive Web App at `fdn-pwa/`. This feature takes a user's already-selected symptoms and converts them into a clear, ordered daily practice plan they can follow without any prior knowledge of functional diagnostic nutrition or health protocols. The desired experience is zero-jargon and zero-overwhelm.

The build is structured in three mandatory phases. Phase 1 is research and familiarization before any code is written. This requires fully exploring the existing app to understand its structure, state management, routing, and component patterns; reading both knowledge map files (`knowledge-map.md` and `source-content-map.md`); and reading the course content files in `research-source-content/course/` to understand the Universal Feedback Loop methodology, how symptoms map to root causes and actionable practices, what the recommended daily and weekly actions are per symptom cluster, and the language and tone used in the course material. A binding constraint governs all health content in this feature: every practice recommendation, educational explanation, and piece of guidance must originate exclusively from the FDN course content files. Nothing from outside those files is permitted.

Phase 2 requires a written feature specification before any code is written. The spec must cover the data model (how symptom selections map to course-derived practice recommendations), the step-by-step user flow from symptom selection to the personalized plan, and the UI structure identifying which screens and components must be created or modified. The UX principles governing the design are: one clear action per screen at a time; plain language only with no clinical abbreviations unless defined inline; progress visibility throughout the experience; complete clarity on each practice (what to do, when, and for how long); and deliberate simplicity — if the plan feels like too much, it must be simplified further.

Phase 3 is implementation. Functional requirements are: read the user's existing symptom selections from the app's current data layer; map each symptom or symptom cluster to a curated set of course-derived daily and weekly practices; display an ordered, bite-sized personalized plan; include for each practice what to do, why it matters in one plain-language sentence, and how often; allow the user to mark practices as complete using client-side local state only, with no backend; and no third-party API integrations. UI requirements are: match the existing design system exactly by reusing existing CSS variables, component classes, and layout patterns; mobile-first with desktop support; professional, clean, and minimal; a micro-interaction on completion such as a checkmark animation; and progressive disclosure so the full plan is never shown in a way that creates visual overwhelm. Code requirements are: follow existing file structure, naming conventions, and component patterns; avoid new dependencies unless absolutely necessary and justified; and store all course-derived content as structured JavaScript data objects rather than inline hardcoded strings.

Out of scope: any backend, database, user accounts, or authentication; third-party health APIs, tracking services, or analytics; modifications to existing symptom selection or educational features; and any health content not sourced from the course files.

---

## Section 1: Summary

The FDN Practice Plan Feature is a new tab added to an existing Progressive Web App built around the Functional Diagnostic Nutrition methodology. The existing app is a symptom-to-lab-marker educational reference tool: users select symptoms they experience, and the app maps those symptoms to the functional lab markers and metabolic dysfunction patterns (organized into five "clusters") that are likely driving them. The new feature extends this by turning the user's symptom selections into a concrete, personalized daily practice plan — a set of ordered, checkable actions drawn exclusively from the FDN certification course curriculum.

The methodology powering the practice content is the DRESS for Health Success framework from the FDN course: Diet, Rest, Exercise, Stress Reduction, and Supplementation. Each of the five existing symptom clusters (A through E) is already linked in the app's data layer to specific physiological dysfunction patterns, and each of those patterns maps to one or more DRESS components. A user whose symptoms involve Cluster B (HPA axis and hormone disruption), for example, will receive practices from the Rest and Stress Reduction modules of the course — specific sleep window recommendations, sleep sanctuary setup steps, and environmental stressor reduction protocols derived directly from Modules 10 and 12. The feature reads cluster memberships from the existing symptom data, retrieves matching course-derived practices, and presents them as a unified, personalized plan.

The plan interface lives in a dedicated "My Plan" tab added to the app's existing bottom navigation bar. The tab displays practices as expandable cards: each card defaults to showing the practice name and frequency; tapping expands it to reveal exact action steps and one plain-language sentence explaining why it matters for the user's symptoms. This design ensures the plan is manageable at a glance while making full detail available on demand.

A key interaction is the plan scope toggle. Because different users respond differently to volume, the plan offers two modes with a clear, plain-language explanation of each trade-off: Focus Mode, which surfaces the five to seven highest-priority practices ranked by how broadly they apply across the user's active clusters; and Full Plan mode, which displays all relevant practices organized into collapsible sections by DRESS category. Both modes are always accessible, the user can switch between them at any time, and the app remembers their last-used preference.

Completion state is persistent and non-punitive. When a user checks a practice as done, that check remains until they intentionally remove it. No daily reset occurs. The model treats the plan as a living reference the user builds consistency against over time, not a daily checklist that resets every morning. All state is stored locally in the browser's `localStorage` — no backend, no account, no synchronization.

The entire feature is implemented within the existing single-file app architecture (`index.html` with embedded CSS and JavaScript), following the established data object patterns, CSS variable tokens, component class conventions, and event-delegation routing model already present in the codebase. No new JavaScript dependencies are introduced. The course-derived practice content is stored as a structured `DATA.dressPractices` array, parallel in design to the existing `DATA.symptoms` and `DATA.variables` objects. Every piece of health guidance in the feature traces to a specific FDN course module — nothing is synthesized from outside sources.

---

## Section 2: Key Points

## Feature Purpose and Position
- Adds a "My Plan" tab to the existing bottom navigation without modifying any current tab, screen, or content
- Converts the app from a diagnostic reference tool into a complete loop: understand symptoms → take daily action on them
- Targets a user with no prior FDN knowledge — every string visible to the user must be immediately understandable without background
- Reads from the existing symptom data layer but never modifies or overwrites it

## Content Source Rules
- All practice recommendations, "why" explanations, and educational language derive exclusively from the FDN certification course modules — no external health content permitted under any circumstance
- Course practices are extracted and stored in a structured `DATA.dressPractices` array — not hardcoded inline text
- Each practice entry includes a `module` source field (non-displayed) that traces it to a specific course module for audit purposes
- Supplementation practices are limited to foundational course-level guidance only — no specific dosing, brands, or lab-dependent protocols

## Data Model and Mapping Architecture
- Existing `DATA.symptoms[id].clusters[]` arrays already contain the cluster memberships (A–E) that serve as the bridge from symptoms to practices
- Five clusters map to DRESS components: A → Diet + Stress Reduction; B → Rest + Stress Reduction + Exercise; C/D → Diet; E → Stress Reduction + medical referral notice
- Each `DATA.dressPractices` entry contains: `id`, `dresComponent`, `title`, `action`, `why`, `frequency`, `clusters[]`, `priority`, `module`
- Practices triggered by multiple symptoms are deduplicated by `id` — each appears once in the rendered plan regardless of how many clusters activate it
- Priority score at render time: (count of user's active symptoms that trigger the practice) × practice `priority` integer

## Navigation and Entry Point
- A fifth tab labeled "My Plan" with a checklist-style icon is added to the bottom navigation bar alongside the existing four tabs
- A small badge or indicator dot appears on the Plan tab when symptoms are currently selected, drawing attention without forcing navigation
- Empty state (no symptoms selected): clear, friendly message directing the user to the Search tab — no broken or error appearance

## Plan View Modes
- Two modes available via a two-segment toggle below the plan header: Focus Mode and Full Plan
- Focus Mode shows the top 5–7 practices ranked by priority score — the highest-leverage starting point for the user's specific cluster profile
- Full Plan shows all relevant practices grouped into collapsible accordion sections by DRESS category (Diet, Rest, Exercise, Stress Reduction, Supplementation)
- Each mode includes a collapsible two-line plain-language explanation of its trade-off (brevity vs. completeness) so users can choose confidently
- The user's last-used mode is stored in `localStorage` and restored on each visit

## Practice Card Design
- Collapsed default: practice title (bold, plain language), frequency badge pill ("Daily" / "Weekly"), completion checkbox on the right
- Tapping the card body (anywhere except checkbox) expands it to reveal: exact action steps ("What to do") and a one-sentence explanation ("Why this helps your symptoms")
- Expanded state uses the existing `.accordion-header` animation pattern — smooth, consistent with the rest of the app
- No clinical abbreviations appear in card titles or expanded text without an inline plain-language definition

## Completion and State Persistence
- Checkmarks persist in `localStorage` under key `'fdn-plan-state'` until the user manually unchecks them — no daily reset
- Checked cards receive a muted visual treatment (secondary text color, reduced opacity) but remain in their original position — no reordering or removal
- Checkmark tap triggers a CSS scale + opacity animation on the check icon as a micro-interaction
- `localStorage` object structure: `{ completedIds: [], viewMode: 'focus'|'full', lastSymptomHash: string }`

## Technical Implementation
- All new code is added to the existing `index.html` — no new files introduced, consistent with the single-file PWA architecture
- CSS uses existing design system variables exclusively: `--bg-secondary` for card surfaces, `--accent` for interactive elements, `--text-secondary` for muted states, cluster color variables for category indicators
- No new JavaScript dependencies — all logic is vanilla JS consistent with the existing codebase
- Plan recalculation is triggered when the `lastSymptomHash` in storage differs from a hash of the current symptom selection; a non-blocking notification prompts the user to refresh

---

## Section 3: Structured Summary

## Feature Overview

### Purpose and Gap Being Filled
- The existing app answers "what might be wrong?" — this feature answers "what do I do about it today?"
- Without this feature, a user who has selected symptoms has an educational understanding of underlying dysfunction but no actionable path forward
- The feature closes the loop: symptoms selected in the existing app are immediately converted into a concrete daily practice plan

### Design Philosophy
- The DRESS framework is non-specific by design in the FDN methodology — it addresses the body's metabolic systems holistically, not individual symptoms in isolation
- Practices are ordered by cross-symptom relevance, not by DRESS component priority, ensuring the plan feels personal rather than generic
- The feature does not tell users they are sick, deficient, or broken — it tells them what simple daily practices the course recommends for their symptom pattern

### Target User Profile
- Has no prior knowledge of FDN, functional medicine, or health protocols
- Finds conventional health advice overwhelming, contradictory, or inaccessible
- Wants to know exactly what to do, not why the science works at a biochemical level
- Has already engaged with the symptom selection feature of the existing app

## Content Foundation

### The DRESS Framework
- DRESS = Diet, Rest, Exercise, Stress Reduction, Supplementation — the FDN practitioner's primary intervention framework, introduced in Module 01 and developed through Modules 08–13B
- The framework is intentionally non-diagnostic: it supports the body's natural systems regardless of which specific dysfunction is present
- All five components have interdependent effects — improvements in rest support hormone balance; improvements in diet support gut integrity; improvements in stress reduction support detoxification

### Course-Sourced Practice Content
- Diet practices derive from Module 09: blood sugar stabilization, eliminating refined carbohydrates for a 90-day reset, including fiber + protein + fat at every meal, tracking satiety and energy response after eating
- Rest practices derive from Module 10: consistent 10 PM–6 AM sleep window, blackout/cool/quiet sleep environment, no screens 2 hours before bed, small protein + low-glycemic carb snack before sleep
- Exercise practices derive from Module 11: mobility work and active recovery as the starting point for users with fatigue or HPA axis symptoms, progressing to resistance training and HIIT as recovery improves
- Stress Reduction practices derive from Module 12: daily water intake (half ounce per pound of body weight), minimum one bowel movement per day supported by dietary fiber, reducing environmental toxin exposure (organic produce, water filtration, avoiding nonstick cookware), deliberate daily laughter and humor

### Language and Tone Standards
- Course language is evidence-based but accessible — metaphors and practical checklists are used alongside physiological explanations
- This feature translates all content one step further: practitioner-level language is simplified to plain speech without losing accuracy
- "Why" sentences use first-person framing (e.g., "This helps your body clear stress hormones while you sleep") rather than third-person clinical description
- No terms from the course appear in user-facing text unless they are immediately defined or replaced with everyday equivalents

## Data Architecture

### DATA.dressPractices Object Design
- Structured as an array of practice objects stored in the JavaScript data layer alongside `DATA.symptoms` and `DATA.variables`
- Each entry: `{ id, dresComponent, title, action, why, frequency, clusters, priority, module }`
- `dresComponent`: one of `'diet'`, `'rest'`, `'exercise'`, `'stress'`, `'supplement'`
- `frequency`: `'daily'`, `'weekly'`, or `'as-needed'`
- `clusters`: array of cluster codes that trigger this practice (e.g., `['A', 'B']`)
- `priority`: integer 1–10 representing inherent practice importance independent of symptom count
- `module`: non-displayed field for content audit traceability (e.g., `'10'`)

### Mapping Logic
- `getActiveClusters(selectedSymptomIds)`: reads the `clusters` arrays from each selected symptom in `DATA.symptoms`, flattens and deduplicates them into a single active cluster array
- `getPracticesForClusters(clusters)`: filters `DATA.dressPractices` for entries where the practice's `clusters` array intersects with the active cluster array, then deduplicates by `id`
- Priority score computation: for each practice, count how many of the user's selected symptom entries contain a cluster that triggered this practice; multiply by `practice.priority`
- `getTopPractices(practices, n)`: returns the top `n` practices sorted by priority score descending (used for Focus Mode)
- `groupByDressComponent(practices)`: returns a Map of DRESS component → sorted practice array (used for Full Plan mode)

### State Storage
- `localStorage` key: `'fdn-plan-state'`
- Stored JSON: `{ completedIds: string[], viewMode: 'focus'|'full', lastSymptomHash: string }`
- `lastSymptomHash`: a simple hash (e.g., sorted symptom IDs joined and hashed) of the current symptom selection — used to detect when the plan needs recalculation
- On plan recalculation, `completedIds` is filtered to retain only IDs that still exist in the new practice list; removed practices are silently dropped from state

## Symptom-to-Practice Mapping by Cluster

### Cluster A (GI Dysbiosis and Detoxification)
- Maps to Diet: blood sugar stabilization, eliminating refined carbohydrates, including fiber at every meal to support bowel regularity
- Maps to Stress Reduction: daily water intake protocol, minimum daily bowel movements, reducing dietary toxin exposure through organic produce and clean cookware choices
- Symptoms triggering Cluster A include: digestive discomfort, bloating, fatigue, food cravings, brain fog, skin reactions

### Cluster B (HPA Axis and Steroidogenesis Disruption)
- Maps to Rest: consistent sleep window (10 PM–6 AM), full sleep sanctuary setup, pre-bed snack for overnight blood sugar stability
- Maps to Stress Reduction: deliberate daily laughter practices, environmental stressor reduction, mindset practices around symptoms as signals rather than diagnoses
- Maps to Exercise: mobility work and gentle active recovery as the primary starting point; high-intensity work is deferred until recovery capacity is established
- Symptoms triggering Cluster B include: always tired, waking at 2–3 AM, anxiety, low libido, mood instability, difficulty recovering from exertion

### Cluster C and D (Estrogen Recycling and Histamine-DAO Imbalance)
- Maps to Diet: foundational blood sugar and elimination practices; dietary fiber to support estrogen metabolism and elimination via bowel regularity
- Maps to Stress Reduction: hydration protocol, daily bowel movements, reducing high-toxin-load food sources
- Symptoms triggering these clusters include: hormonal symptoms, histamine-type reactions, food sensitivities, mood cycling

### Cluster E (Acute Inflammation and Medical Referral)
- Any selection of Cluster E symptoms triggers a physician referral notice rendered as the first and most prominent element on the Plan screen
- Basic rest and stress reduction practices from the course are still displayed below the notice as universal foundational support
- The referral notice uses the same visual pattern as the existing `isMedicalReferral` alert in the app — plain language, non-alarming tone, clear direction

## User Interface Design

### Navigation Integration
- A fifth tab is added to the existing bottom navigation bar: icon (checklist or similar), label "My Plan"
- Badge indicator (small filled dot using `--accent` color) on the Plan tab when symptoms are selected — passive, not intrusive
- Tab follows the same `data-tab`, `data-action="navigate-tab"`, and `aria-label` pattern as all existing tabs

### Plan Screen Layout
- Header section: title "Your Practice Plan", sub-label "Based on [N] symptoms you selected"
- Mode toggle: two-segment toggle control directly below the header, followed by a collapsible one-line trade-off explanation for each mode
- Content area: full-height scrollable list of practice cards with adequate bottom padding to clear the fixed navigation bar
- Referral notice (Cluster E): rendered above all practice cards when active

### Visual Design System Compliance
- Card backgrounds: `--bg-secondary`; screen background: `--bg-primary`
- Title text: `--text-primary`; metadata (frequency, DRESS label): `--text-secondary`
- Active toggle segment and checkmark fill: `--accent` (#007AFF)
- Cluster color dots (small indicator on each card showing which cluster triggered this practice): `--cluster-a` through `--cluster-e`
- Spacing, border radius, and font sizes: strict adherence to existing CSS variable scale
- Touch targets: minimum 44px per existing standard

## Plan View Modes

### Focus Mode Behavior
- Default mode on first visit; restores to last-used mode on subsequent visits
- Shows top 5–7 practices by priority score
- Header sub-label in Focus Mode: "Showing your highest-impact practices"
- Collapsible explainer line: "Focus Mode shows the practices with the broadest impact on your symptoms. Start here."
- Link at bottom of list: "See all practices →" transitions to Full Plan mode

### Full Plan Mode Behavior
- All deduped practices organized into accordion sections by DRESS component
- Section header: plain-language DRESS component name + count label (e.g., "Rest — 3 practices")
- Sections default to expanded on first render; user collapse state is not persisted (re-expands on next visit)
- Collapsible explainer line: "Full Plan shows every practice recommended for your symptoms, grouped by focus area."
- Weekly practices visually distinguished from Daily practices by a labeled frequency pill

## Practice Card Interaction

### Collapsed Default State
- Shows: practice title (bold, one line), frequency badge pill, checkbox control (right edge)
- Tapping card body (anywhere except checkbox): smooth expand animation revealing action and why sections
- No chevron icon needed — the expand behavior is established by existing `.accordion-header` pattern

### Expanded State Content
- "What to do" section: exact, step-by-step action instructions from the course — concrete, specific, no vagueness
- "Why this helps" section: one plain-language sentence connecting the practice to the user's symptoms (written during data construction, not dynamically generated)
- Collapse: second tap on card body; smooth collapse animation

### Completion Interaction
- Tapping checkbox: CSS scale animation on checkmark SVG, card title shifts to `--text-secondary`, card background softens
- Checked state is immediately written to `localStorage`
- Tapping again: reverses all visual changes, removes ID from `completedIds` in storage
- No reordering of cards after completion — position stability prevents disorientation

## Completion and State Management

### Storage Model
- `localStorage` key: `'fdn-plan-state'`
- Stored as JSON: `{ completedIds: ['practice-id-1', 'practice-id-2'], viewMode: 'focus'|'full', lastSymptomHash: string }`
- `lastSymptomHash` is a hash of the user's current symptom selection — used to detect when the plan should be recalculated due to symptom changes

### Plan Recalculation
- When the app detects that the user's current symptom selection differs from the `lastSymptomHash`, a notice appears at the top of the Plan tab: "Your symptom selection has changed. Tap to refresh your plan."
- Refreshing recalculates the practice list but preserves completion state for practices that persist in the new plan
- Practices removed from the plan (because their symptoms were deselected) are silently dropped from the completion state

### State Scope
- State is local only — no synchronization, no server storage, no account association
- `localStorage` is used directly via `JSON.parse`/`JSON.stringify` — no abstraction layer needed
- State resets when the user clears browser/PWA data (acknowledged limitation; no recovery mechanism required)

## Technical Implementation

### Architecture Fit
- All new code is added to the existing `index.html` — no new files; consistent with the single-file PWA pattern already in use
- New data object `DATA.dressPractices` added in the JavaScript data layer adjacent to `DATA.symptoms` and `DATA.variables`
- New screen section `#screen-plan` added alongside existing screen sections (Home, Search, Clusters)
- New tab button added to the bottom navigation HTML with matching `data-tab` attribute and `aria-label`

### New Functions Required
- `getActiveClusters(selectedSymptomIds)`: returns deduplicated array of cluster codes from user's current symptom selection
- `getPracticesForClusters(clusters)`: returns filtered, deduped, and sorted practice array from `DATA.dressPractices`
- `getTopPractices(practices, n)`: returns top n practices by priority score (Focus Mode)
- `renderPlanScreen()`: full plan screen render function, consistent with existing screen render pattern
- `togglePracticeComplete(practiceId)`: updates localStorage state and re-renders completion visual

### No New Dependencies
- No npm packages, CDN imports, or external scripts introduced
- All animations achieved via CSS transitions using existing animation patterns from the design system
- No icon font additions — use existing SVG icon patterns from the codebase

## Safety and Content Integrity

### Medical Referral Handling
- Any symptom in Cluster E (Calprotectin-triggered acute inflammation) causes a physician referral notice to appear at the top of the plan
- The referral notice matches the tone and style of the existing `isMedicalReferral` alert patterns in the app
- Referral notice does not block access to other practices but maintains visual prominence throughout the session

### Content Audit Trail
- Each practice in `DATA.dressPractices` includes a `module` field referencing the specific module number (e.g., `"module": "10"`) from which the recommendation was derived
- This field is not displayed to users but exists for maintainability and future content audits
- Before implementation, all practice content must be verified against the specific module files

---

## Section 4: Complete Vision Expansion

### Explicit Non-Goals

- The feature does not display or recommend specific supplement brands, dosages, or products — only foundational supplementation principles taught in the course.
- The feature does not track symptom progression, health outcomes, or improvement over time — it is a practice guide, not a health tracker.
- The feature does not replace or compete with the existing symptom-to-marker educational content — it reads from that layer but does not modify it.
- The feature does not provide diagnostic information or imply health conditions — it presents lifestyle practices only.
- The feature does not synchronize, backup, or share data — all state is local-only.
- The feature does not adapt or personalize practices based on metabolic type — it delivers cluster-mapped practices without the metabolic typing assessment that would be needed for full metabolic type individualization.
- The feature does not include push notifications, reminders, or scheduled alerts.
- The feature does not gamify completion — no streaks, scores, badges, or leaderboards are included.

### Edge Case Handling

**No symptoms selected:** The Plan tab renders a clean empty state with the message "Select symptoms on the Search tab to see your personalized plan." No error styling, broken layout, or empty lists — just a calm, clear prompt.

**All symptoms selected simultaneously:** The deduplication logic still produces a manageable practice list. Focus Mode enforces the 5–7 cap regardless of symptom volume. Full Plan renders a longer but grouped, collapsible list that remains navigable. The plan does not appear broken or unmanageable.

**Only Cluster E symptoms selected:** The referral notice is the first and most prominent element. Basic rest and stress reduction practices from the course appear below it. The notice communicates clearly and without alarm that the user should consult a physician, using plain language consistent with the app's existing medical referral pattern.

**User changes symptom selection mid-session:** The `lastSymptomHash` comparison detects the divergence on next Plan tab visit. A non-blocking banner appears at the top of the Plan screen: "Your symptoms have changed. Refresh your plan?" One-tap refresh recalculates the practice list, retains valid completion state, and drops practices no longer relevant. No data is lost; the user is always in control.

**Single symptom selected:** The plan may contain two to three practices. This is correct behavior — a short, focused plan is the intended outcome. Focus Mode and Full Plan may look nearly identical at this scale, which is acceptable; the toggle is still present for UX consistency.

**Practice belongs to multiple clusters, triggered by many symptoms:** The practice appears once (deduplicated by `id`) and naturally rises to the top of Focus Mode due to its high priority score. This is the intended behavior — broadly relevant practices surface first.

**App used offline:** All plan functionality works offline. Practice data is embedded in the JavaScript layer (no API calls required), and `localStorage` persists across offline sessions. The service worker cache-first strategy already covers `index.html` — no additional caching configuration is needed.

**User has practices checked from a previous symptom selection that no longer apply:** On plan refresh, the `completedIds` array is filtered against the new practice list. IDs no longer in the plan are silently removed from storage. The user only sees completion state for currently relevant practices.

### Key Design Principles

1. **Course Content Is the Exclusive Source** — No practice, explanation, or health claim appears in this feature unless it can be directly traced to a specific FDN course module. This rule has no exceptions and cannot be relaxed during implementation. The `module` field on every `DATA.dressPractices` entry exists to enforce this auditability.

2. **Clarity Over Completeness** — When a user has many symptoms and the full practice list is long, the design defaults to Focus Mode. Progressive disclosure (expandable cards, collapsible sections, the Focus/Full toggle) is the structural answer to volume — never truncation, never omission, always user-controlled depth.

3. **Persistent, Not Punitive** — Completion state persists across sessions without resetting. The model is: the user is building consistency over time, not passing a daily test. A missed practice is handled by an unchecked box, not a broken streak or a punishing empty state.

4. **No Clinical Language at the Surface** — Every user-visible string (labels, card titles, mode descriptions, empty states, referral notices, frequency badges) passes a plain-language test: a person with no health background can read it and immediately understand what is being communicated. Terms like "HPA dysregulation" or "hepatic congestion" do not appear in user-facing text.

5. **Architectural Continuity** — The feature is built as though it were part of the original app. It introduces no new patterns, conventions, or dependencies that diverge from the existing codebase. A developer encountering the code for the first time should not be able to identify where the original code ends and the new code begins.

### Component or Document Relationships

```
User selects symptoms (Search tab / existing feature)
          │
          ▼
DATA.symptoms[id].clusters[]  →  Active clusters: ['A', 'B', ...]
          │
          ▼
getActiveClusters(selectedIds)
          │
          ▼
getPracticesForClusters(clusters)  ←  DATA.dressPractices[]
          │  (filtered, deduped, priority-scored)
          ▼
┌─────────────────────┐    ┌──────────────────────────────────────┐
│   Focus Mode        │    │   Full Plan Mode                     │
│   getTopPractices(7)│    │   groupByDressComponent()            │
│   → top 5-7 cards   │    │   → Diet / Rest / Exercise /         │
│                     │    │     Stress / Supplement sections      │
└─────────────────────┘    └──────────────────────────────────────┘
          │                           │
          └────────────┬──────────────┘
                       ▼
          Practice Cards (expandable)
          ┌──────────────────────────────┐
          │ [collapsed] title + freq + ☐ │
          │ [expanded]  + action + why   │
          └──────────────────────────────┘
                       │
                       ▼
          togglePracticeComplete(id)
                       │
                       ▼
          localStorage 'fdn-plan-state'
          { completedIds[], viewMode, lastSymptomHash }
                       │
                       ▼
          Visual: checked = muted styling + checkmark animation

Cluster E symptom present?
          │ Yes
          ▼
Referral Notice Card (rendered above practice cards)

Symptom selection changed?
          │ Yes (lastSymptomHash mismatch)
          ▼
Non-blocking banner → "Refresh your plan" → recalculate
```

### Success Criteria

- The feature is successful when a user with no prior health knowledge can navigate to the Plan tab and immediately understand what to do, when to do it, and why — without needing to look anything up or interpret anything.
- The data model is successful when every practice in `DATA.dressPractices` can be traced to a specific FDN course module via its `module` field, and no practice contains content that originates outside the course.
- Focus Mode is successful when users with five or more selected symptoms see a plan of five to seven items that represent the highest-leverage practices for their specific cluster profile — not a generic starter list.
- Full Plan mode is successful when all relevant practices are visible, grouped into clearly labeled sections by DRESS area, and the user can collapse completed sections without losing information.
- The mode toggle is successful when the two-line trade-off explanation beside each mode is sufficient for any user to confidently choose between them on their first visit.
- Completion state is successful when checked items persist across app restarts and are displayed in their original position with consistent muted styling when the user reopens the app.
- Plan recalculation is successful when the user is notified of symptom changes on their next Plan tab visit and can refresh their plan in one tap while retaining valid prior completion state.
- Medical referral handling is successful when any Cluster E symptom selection causes the referral notice to render as the first visible element on the Plan screen, above all practice cards, on every session where that symptom remains selected.
- Technical implementation is successful when the new code in `index.html` is indistinguishable in style, convention, and approach from the existing codebase — no divergent patterns, no new dependencies.
- Content integrity is successful when a full review of all `DATA.dressPractices` entries confirms every `action` and `why` field traces to a specific FDN course module without exception.

### Open Questions and Assumptions

1. **Symptom Selection Persistence:** The current app's `DATA.symptoms` structure and Search screen are well-documented, but the research did not confirm whether a persistent multi-select state (a list of "currently selected symptom IDs" available across screens) exists in the codebase. The Plan feature requires this as a foundation. **Assumption:** this state exists or will be added as a prerequisite. **Flag: if not already present, adding a global symptom selection array is an architectural prerequisite — not a minor addition — and the implementation estimate must account for it.**

2. **Fifth Tab Bar Fit:** The existing bottom navigation has four tabs (Home, Search, Clusters, and possibly one more). Adding a fifth may create crowding on 320px-width screens. **Assumption:** the tab bar accommodates five tabs by reducing label text size, switching to icon-only, or allowing horizontal scroll — the specific approach should be validated against the actual rendered tab bar width before coding the navigation change.

3. **Metabolic Type Individualization:** The FDN Diet component (Module 09) specifies that dietary recommendations must be tailored by metabolic type (fast vs. slow oxidizer, autonomic dominance). This assessment is not available in the current app. **Assumption:** Diet practices in this feature are limited to universally applicable foundational guidance — blood sugar stabilization, eliminating refined carbohydrates, including fiber/protein/fat at each meal — without type-specific variations. **Flag: if metabolic type data is added to the app in the future, the diet practice layer will require substantial extension.**

4. **Supplementation Content Depth:** The FDN "S" (Supplementation) component in the course is closely tied to lab results and specific protocols. Without labs, only foundational course-level guidance is applicable. **Assumption:** Supplementation practices are limited to a small number of foundational recommendations the course presents independently of lab context (e.g., multi-mineral support before sleep from Module 10). These should be conservative and explicitly framed as foundational support, not targeted protocols.

5. **"Why" Sentence Construction:** Every practice requires one user-facing sentence explaining why it matters for the user's symptoms, written in plain language. These sentences require human authorship during the data construction phase. **Assumption:** "why" sentences are written and reviewed against specific course module text before implementation begins — they are content deliverables that precede the code deliverable.

6. **Priority Integer Calibration:** The `priority` integer (1–10) on each practice entry determines ranking within Focus Mode. The specific calibration of these values requires editorial judgment. **Assumption:** priority values are assigned based on how broadly a practice is recommended across clusters and how foundational it is in the course's framing (e.g., sleep and blood sugar stabilization rank highest as they are described as foundational to all other DRESS components). A first-pass calibration can be refined after user testing.

7. **Cluster E Baseline Practices:** When a user's symptoms map exclusively to Cluster E, the plan could theoretically show only a referral notice with no actionable practices. **Assumption:** a small set of universal "baseline" practices — drawn from the course's foundational Rest and Stress Reduction guidance — are always included in any plan regardless of cluster, representing the FDN course's entry-level "do no harm" starting point.
