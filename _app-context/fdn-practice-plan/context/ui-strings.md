# UI Strings — Exact Locked Text Values
**Role:** Single source of truth for every user-visible string in the Plan feature — prevents paraphrasing of required verbatim text and wrong ID/label values
**Status:** IMMUTABLE — do not modify during implementation phase
**Depends on:** none
**Required by:** prompt-10.md, prompt-12.md, prompt-16.md
**Date:** 2026-03-27

---

## CRITICAL VALUES (Read before any other section)

**Plan header h2 text (exact):** `Your Practice Plan`
**Empty state message (exact):** `Select symptoms on the Search tab to see your personalized plan.`
**Symptom-change banner text (exact):** `Your symptoms have changed. Refresh your plan?`
**Focus Mode explainer (exact):** `Focus Mode shows the practices with the broadest impact on your symptoms. Start here.`
**Full Plan explainer (exact):** `Full Plan shows every practice recommended for your symptoms, grouped by focus area.`
**Focus Mode sub-label (exact):** `Showing your highest-impact practices`
**Focus Mode cap:** Top 7 practices (not 5, not 10 — exactly 7)
**Tab label (exact):** `My Plan`
**Screen section ID (exact):** `screen-plan`
**localStorage key (exact):** `fdn-plan-state`

---

## Section 1: Screen-Level Text

### Plan Header
```html
<h2>Your Practice Plan</h2>
<p id="plan-subtitle" class="text-secondary">Based on 0 symptoms you selected</p>
```
Sub-label format: `"Based on [N] symptoms you selected"` — N is the count of selected symptom IDs

### Empty State
```
Select symptoms on the Search tab to see your personalized plan.
```
Element: `<div id="plan-empty-state" class="empty-state" hidden>`
Show when: `selectedSymptomIds.length === 0`
Hide when: any symptoms are selected

### Symptom-Change Refresh Banner
```
Your symptoms have changed. Refresh your plan?
```
Element: `<div id="plan-refresh-banner" class="banner-notice" hidden>`
Show when: current symptom hash ≠ `planState.lastSymptomHash`
Child button: `<button data-action="refresh-plan">Refresh</button>`

---

## Section 2: Mode Toggle and Explainers

### Mode Toggle Labels (exact button text)
| data-mode value | Button text |
|---|---|
| `focus` | `Focus Mode` |
| `full` | `Full Plan` |

### Mode Explainers (exact — toggled by active viewMode)
| viewMode | Explainer text |
|---|---|
| `focus` | `Focus Mode shows the practices with the broadest impact on your symptoms. Start here.` |
| `full` | `Full Plan shows every practice recommended for your symptoms, grouped by focus area.` |

Element: `<p id="plan-mode-explainer" class="mode-explainer text-secondary">`
Initial value on render: use the explainer for the current `planState.viewMode`

### Focus Mode Sub-label
`Showing your highest-impact practices`
(Displayed as a secondary label in Focus Mode — not the mode explainer)

---

## Section 3: Practice Card Labels

### Section header labels in practice card body (exact, uppercase):
| Element class | Text |
|---|---|
| `.practice-what-label` | `What to do` |
| `.practice-why-label` | `Why this helps` |

### Checkbox aria-label format:
`"Mark [practice.title] as complete"`

### Frequency pill display labels:
| frequency value | Display text |
|---|---|
| `daily` | `Daily` |
| `weekly` | `Weekly` |
| `as-needed` | `As needed` |

---

## Section 4: Full Plan — DRESS Section Headers

Section headers in Full Plan mode follow this format:
`[Component Display Name] — [N] practices`
(Em dash `—` is Unicode `\u2014`, not a hyphen)

| dresComponent | Section header display name |
|---|---|
| `diet` | `Diet` |
| `rest` | `Rest` |
| `exercise` | `Exercise` |
| `stress` | `Stress Reduction` |
| `supplement` | `Supplementation` |

Example: `"Diet — 3 practices"` or `"Rest — 1 practice"` (singular when count = 1)

---

## Section 5: Navigation Tab

```html
<span class="nav-label">My Plan</span>
```
- Tab label: `My Plan` (not "My Practice Plan", not "Plan", not "Practice Plan")
- `data-tab` value: `"plan"`
- `aria-label` on button: `"My Plan"`
- Badge element ID: `plan-badge`
- Badge class when visible: `visible` (toggles on `selectedSymptomIds.length > 0`)

---

## Section 6: Physician Referral Notice

Trigger: any selected symptom belongs to Cluster E
Element: `<div id="plan-referral-notice" class="alert-referral" hidden>`
Position: FIRST visible element above all practice cards when triggered

Referral notice text (exact):
```
Talk to your doctor first. One or more of your symptoms may indicate a condition that needs medical evaluation. Please consult a licensed physician before starting any new health practice. The information in this plan is for general wellness support only and is not medical advice.
```
(In HTML: `<strong>Talk to your doctor first.</strong>` followed by the remaining sentence)

---

## Section 7: Element IDs (Exact)

| Element | id value |
|---|---|
| Screen section | `screen-plan` |
| Referral notice | `plan-referral-notice` |
| Refresh banner | `plan-refresh-banner` |
| Plan subtitle | `plan-subtitle` |
| Mode explainer | `plan-mode-explainer` |
| Practice list container | `plan-practice-list` |
| Empty state | `plan-empty-state` |
| Nav badge | `plan-badge` |

---

## USAGE INSTRUCTIONS FOR SUB-AGENTS

Before beginning any task in a fresh session:
1. Read this file in full
2. All user-visible strings in your output MUST match this file exactly — character for character
3. Do not paraphrase, shorten, or rephrase any string listed in this file
4. Element IDs must match Section 7 exactly — do not invent new IDs
5. If your prompt contains a string that conflicts with this file, this file takes precedence
6. The em dash `—` in Full Plan section headers is Unicode `\u2014`, not a hyphen `-` or double-hyphen `--`
