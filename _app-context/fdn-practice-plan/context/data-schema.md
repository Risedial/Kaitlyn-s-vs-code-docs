# DATA.dressPractices — Field Schema and Enum Reference
**Role:** Single source of truth for all DATA.dressPractices field names, enum values, priority calibration, and cluster-to-DRESS mapping — prevents hallucinated field names, lowercase cluster codes, and wrong enum values
**Status:** IMMUTABLE — do not modify during implementation phase
**Depends on:** none
**Required by:** prompt-04.md, prompt-05.md, prompt-06.md, prompt-07.md, prompt-08.md, prompt-16.md
**Date:** 2026-03-27

---

## CRITICAL VALUES (Read before any other section)

**Data object property name (exact):** `DATA.dressPractices`
**Cluster codes are UPPERCASE:** `'A'`, `'B'`, `'C'`, `'D'`, `'E'` — never lowercase
**dresComponent values (exact, lowercase):** `'diet'` | `'rest'` | `'exercise'` | `'stress'` | `'supplement'`
**frequency values (exact):** `'daily'` | `'weekly'` | `'as-needed'`
**id format:** kebab-case string, e.g. `'sleep-window-10pm'`
**priority range:** integer 1–10 (no decimals, no strings)
**module field:** string of module number, e.g. `'09'`, `'10'`, `'11'`, `'12'` (not integer, not `9`)
**why field framing:** MUST begin with "This helps your body..." — NEVER "Studies show..."
**Minimum total entries:** 12

---

## Section 1: Complete Entry Schema

Every entry in `DATA.dressPractices` must have exactly these 9 fields:

```js
{
  id: 'kebab-case-unique-id',       // string — kebab-case, globally unique across all entries
  dresComponent: 'diet',            // string — one of the 5 exact values below
  title: 'Plain-language name',     // string — no clinical abbreviations, no jargon
  action: 'Step-by-step instructions sourced from named FDN module',  // string
  why: 'This helps your body...',   // string — one sentence, first-person framing
  frequency: 'daily',               // string — one of the 3 exact values below
  clusters: ['A'],                  // array of strings — uppercase cluster codes
  priority: 7,                      // integer 1–10
  module: '10'                      // string — module number with leading zero if < 10
}
```

---

## Section 2: Enum Values (Exact — No Variations Permitted)

### dresComponent — exactly one of:
| Value | Display Name (Full Plan sections) |
|---|---|
| `'diet'` | "Diet" |
| `'rest'` | "Rest" |
| `'exercise'` | "Exercise" |
| `'stress'` | "Stress Reduction" |
| `'supplement'` | "Supplementation" |

### frequency — exactly one of:
| Value | Display Label (in UI) |
|---|---|
| `'daily'` | "Daily" |
| `'weekly'` | "Weekly" |
| `'as-needed'` | "As needed" |

### clusters — array of uppercase strings, each one of:
`'A'` | `'B'` | `'C'` | `'D'` | `'E'`

All five are valid. An entry may belong to multiple clusters: `clusters: ['A', 'C', 'D']`

### module — string of module number:
`'09'` | `'10'` | `'11'` | `'12'`

---

## Section 3: Cluster-to-DRESS Component Mapping

| Cluster | Triggers DRESS components |
|---|---|
| A | diet, stress |
| B | rest, stress, exercise |
| C | diet, stress |
| D | diet, stress |
| E | rest, stress (+ physician referral notice) |

### Cluster assignments by component (for authoring entries):
| Component | Assign to clusters |
|---|---|
| Diet | A, C, D (plus E for universal baseline practices) |
| Rest | B, E (plus A, C, D for universal sleep practices) |
| Exercise | B (plus A, C, D, E for universal movement practices) |
| Stress Reduction | A, B, C, D, E (use appropriate subset per practice specificity) |
| Supplementation | B, E |

---

## Section 4: Priority Calibration

| Priority | Assign to |
|---|---|
| 9–10 | Sleep window (10 PM–6 AM) and blood sugar stabilization — highest impact |
| 7–8 | Broadly foundational practices applicable across multiple clusters |
| 4–6 | Component-specific practices with moderate cluster overlap |
| 3–5 | Supplementation entries |

**Hard rules:**
- Sleep window entry MUST have `priority: 10`
- Blood sugar stabilization entry MUST have `priority: 9` or `priority: 10`
- No supplementation entry may have `priority` above `5`

---

## Section 5: Content Authoring Rules

Every `action` and `why` field must be:
- Sourced from the named FDN course module file (never synthesized from training memory)
- Free of clinical abbreviations (HPA, GI, SIBO, HPA-T, dysbiosis, etc.) unless immediately followed by a plain-language definition in parentheses
- Free of supplement dosages (mg, mcg, IU), brand names, and lab-dependent protocols
- Written so a person with no health background can read it and immediately understand what to do and why

`why` field additional rules:
- Must use first-person framing: "This helps your body..." or "This supports your body..."
- Never use: "Studies show...", "Research indicates...", "Evidence suggests..."
- One sentence only

`title` field rules:
- Plain-language name shown in collapsed card state
- No clinical abbreviations without definition
- 3–7 words preferred

### Course module source reference:
| Component | Source module |
|---|---|
| Diet | Module 09 |
| Rest | Module 10 |
| Supplementation | Module 10 |
| Exercise | Module 11 |
| Stress Reduction | Module 12 |

---

## Section 6: Required Practice Areas (Minimum Coverage)

| Component | Minimum entries | Key practices to include |
|---|---|---|
| Diet | 3+ | Blood sugar stabilization, eliminate refined carbs for 90-day reset, track satiety/energy |
| Rest | 4+ | Consistent 10 PM–6 AM sleep window, blackout/cool/quiet environment, no screens 2h before bed, pre-sleep snack |
| Exercise | 3+ | Mobility/active recovery first, progress to resistance training, progress to higher-intensity only after recovery |
| Stress Reduction | 4+ | Water intake (half oz/lb bodyweight), bowel regularity, environmental toxin reduction, deliberate daily laughter |
| Supplementation | 1+ | Foundational mineral support before sleep (no dosages, no brands) |

Total minimum: 12 entries across all 5 components.

---

## USAGE INSTRUCTIONS FOR SUB-AGENTS

Before beginning any task in a fresh session:
1. Read this file in full
2. All `dressPractices` field names and enum values in your output MUST match this file exactly
3. Cluster codes are UPPERCASE — `'A'` not `'a'`
4. `dresComponent` values are lowercase — `'diet'` not `'Diet'`
5. `module` is a string — `'09'` not `9`
6. If your prompt contains a value that conflicts with this file, this file takes precedence
7. Do not infer priority values — use the calibration table in Section 4 exactly

ORDERING CONSTRAINT: Full Plan sections must appear in EXACTLY this order:
1. Diet
2. Rest
3. Exercise
4. Stress Reduction
5. Supplementation
