# Vision: FDN Practice Plan Feature

---

## Goal

The real underlying goal is to close the loop the existing FDN PWA opens but never completes: a user who has selected their symptoms and understood what metabolic systems are likely affected now has a concrete, ordered set of daily actions they can follow without any prior knowledge of functional diagnostic nutrition.

The proxy metric (a "My Plan" tab) exists only in service of this goal. The feature succeeds when a user with no health background can act — not just understand.

---

## Goal Type Classification

**Hybrid: State + Process**

- *State*: The user has a persistent, personalized practice plan they can reference at any time
- *Process*: The user follows a daily and weekly practice rhythm derived from their symptom profile

---

## Audience and Purpose

**Primary user:** A person with no prior FDN, functional medicine, or clinical health knowledge who has already used the FDN app's symptom selection feature. They are overwhelmed by conventional health information, want clear and specific actions, and are not interested in biochemical explanations.

**Purpose:** Convert the app from a diagnostic reference tool into a complete, actionable feedback loop. The existing app answers "what might be wrong?" This feature answers "what do I do about it today?"

---

## Success Criteria

### External proof (what others can observe)
- A user who has never heard of FDN navigates to the Plan tab and within 60 seconds identifies exactly what they should do today, when to do it, and why it matters for their symptoms
- Every practice visible to the user can be traced to a specific FDN course module by a reviewer with access to the course files
- A reviewer comparing the new code to the existing `index.html` cannot identify a stylistic or structural boundary between old and new code

### Internal proof (what the builder knows is true)
- Every string in `DATA.dressPractices[].action` and `DATA.dressPractices[].why` is sourced from and verified against a named FDN course module
- The `module` field on every practice entry references the specific module from which the content was derived
- No clinical abbreviation, practitioner-level term, or unexplained jargon appears in any user-visible string
- The feature works fully offline with no API calls

---

## Constraints

### Must
- All new code is added to the existing `index.html` — no new files
- All practice content (action steps and "why" sentences) derives exclusively from the FDN certification course module files in `research-source-content/course/`
- Match the existing design system: CSS variables, component classes, layout patterns, event-delegation routing model
- Vanilla JavaScript only — no new dependencies
- Mobile-first with desktop support
- All state stored in `localStorage` only — no backend, no server calls
- Cluster E symptoms must trigger a physician referral notice rendered as the first visible element on the Plan screen

### Must not
- Import, infer, or use any health content from outside the FDN course files
- Modify any existing tab, screen, component, or data structure
- Include push notifications, reminders, daily resets, streaks, scores, badges, or gamification
- Store or transmit user data to any server
- Display supplement dosages, brand recommendations, or lab-dependent protocols
- Show clinical abbreviations or practitioner-level terminology without inline plain-language definition

---

## Exact Values Locked

| Value | Definition |
|---|---|
| `localStorage` key | `'fdn-plan-state'` |
| Storage JSON structure | `{ completedIds: string[], viewMode: 'focus'\|'full', lastSymptomHash: string }` |
| Focus Mode count | Top 5–7 practices by priority score |
| Data object name | `DATA.dressPractices` |
| Practice entry fields | `id`, `dresComponent`, `title`, `action`, `why`, `frequency`, `clusters`, `priority`, `module` |
| `dresComponent` values | `'diet'`, `'rest'`, `'exercise'`, `'stress'`, `'supplement'` |
| `frequency` values | `'daily'`, `'weekly'`, `'as-needed'` |
| `clusters` values | `'A'`, `'B'`, `'C'`, `'D'`, `'E'` |
| `priority` range | Integer 1–10 |
| Tab label | "My Plan" |
| Tab badge color | `--accent` (#007AFF) |
| Card background | `--bg-secondary` |
| Screen background | `--bg-primary` |
| Active toggle / checkmark | `--accent` |
| Muted/completed text | `--text-secondary` |
| Cluster indicators | `--cluster-a` through `--cluster-e` |
| Minimum touch target | 44px |
| New screen section ID | `#screen-plan` |
| Referral notice trigger | Any symptom in Cluster E |
| Empty state message | "Select symptoms on the Search tab to see your personalized plan." |
| Symptom-change banner | "Your symptoms have changed. Refresh your plan?" |
| Focus Mode sub-label | "Showing your highest-impact practices" |
| Focus Mode explainer | "Focus Mode shows the practices with the broadest impact on your symptoms. Start here." |
| Full Plan explainer | "Full Plan shows every practice recommended for your symptoms, grouped by focus area." |
| Plan header | "Your Practice Plan" |
| Plan sub-label format | "Based on [N] symptoms you selected" |

---

## Leverage Points

These are the two things that, if wrong, invalidate the entire build:

**1. Content integrity — course sourcing.**
If any practice content is synthesized, inferred, or sourced outside the FDN course module files, the feature violates its foundational promise. Every `action` and `why` field must be authored directly from the course. This is not a style preference — it is the non-negotiable constraint that makes the feature trustworthy. A build that gets the UI perfect but has one hallucinated health claim is a failed build.

**2. Symptom-to-cluster bridge.**
The entire data flow depends on `DATA.symptoms[id].clusters[]` arrays existing in the current app and being accessible as a persistent multi-select selection state across screens. If this bridge does not exist in the current codebase, it must be built as an explicit prerequisite before any plan feature work begins. This is the highest-risk architectural assumption. Treating it as a given without verification will cause the feature to fail at the data layer.
