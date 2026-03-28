# FDN Practice Plan — Orchestration Index
**Date:** 2026-03-27
**Total Steps:** 16
**Build Target:** `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`

---

## Execution Index

| Prompt # | File | Purpose | Prerequisites | Est. Token Output | Sub-Agent Strategy |
|---|---|---|---|---|---|
| 01 | prompt-01.md | Read index.html; document codebase patterns to context file | none | ~3,000 | SOLO |
| 02 | prompt-02.md | Verify clusters[] field on DATA.symptoms; add if missing | flags.codebasePatternsDocumented = true; context/codebase-patterns.md exists | ~8,000 | SOLO |
| 03 | prompt-03.md | Verify selectedSymptomIds in app state; add if missing | flags.codebasePatternsDocumented = true; context/codebase-patterns.md exists | ~5,000 | SOLO |
| 04 | prompt-04.md | Author diet, rest, supplement practices from modules 09 and 10 | flags.codebasePatternsDocumented = true | ~8,000 | SOLO |
| 05 | prompt-05.md | Author exercise and stress reduction practices from modules 11 and 12 | flags.codebasePatternsDocumented = true | ~8,000 | SOLO |
| 06 | prompt-06.md | Merge all practice drafts; write finalized DATA.dressPractices JS fragment | flags.practicesDietRestSupplementDrafted = true; flags.practicesExerciseStressDrafted = true; context/practices-diet-rest-supplement.md exists; context/practices-exercise-stress.md exists | ~6,000 | SOLO |
| 07 | prompt-07.md | Add DATA.dressPractices array to index.html | flags.clustersFieldVerified = true; flags.selectedSymptomsStateVerified = true; flags.practicesDataFinalized = true; context/practices-final.js exists | ~10,000 | SOLO |
| 08 | prompt-08.md | Add utility functions to index.html | flags.dataLayerAdded = true; context/codebase-patterns.md exists | ~4,000 | SOLO |
| 09 | prompt-09.md | Add state management functions to index.html | flags.dataLayerAdded = true; context/codebase-patterns.md exists | ~3,000 | SOLO |
| 10 | prompt-10.md | Add renderPlanScreen() function to index.html | flags.utilityFunctionsAdded = true; flags.stateFunctionsAdded = true; context/codebase-patterns.md exists | ~7,000 | SOLO |
| 11 | prompt-11.md | Add My Plan nav tab button HTML to index.html | flags.codebasePatternsDocumented = true; context/codebase-patterns.md exists | ~1,500 | SOLO |
| 12 | prompt-12.md | Add #screen-plan screen section HTML to index.html | flags.navTabAdded = true | ~2,500 | SOLO |
| 13 | prompt-13.md | Add all new CSS classes to index.html stylesheet | flags.codebasePatternsDocumented = true; context/codebase-patterns.md exists | ~4,000 | SOLO |
| 14 | prompt-14.md | Add new event delegation handlers to existing handler in index.html | flags.renderFunctionAdded = true; flags.screenSectionAdded = true; context/codebase-patterns.md exists | ~3,000 | SOLO |
| 15 | prompt-15.md | Add badge visibility update calls to symptom selection change points | flags.eventDelegationUpdated = true; context/codebase-patterns.md exists | ~2,000 | SOLO |
| 16 | prompt-16.md | Run full verification pass against all 10 success criteria | flags.badgeLogicAdded = true | ~2,500 | SOLO |

---

## Context Files

| File | Role | Created By | Required By |
|---|---|---|---|
| context/codebase-patterns.md | Existing render functions, event handler, CSS tokens, screen IDs, DATA.symptoms structure | Prompt 01 | Prompts 02–15 |
| context/practices-diet-rest-supplement.md | Authored diet, rest, supplementation practices (draft) | Prompt 04 | Prompt 06 |
| context/practices-exercise-stress.md | Authored exercise and stress reduction practices (draft) | Prompt 05 | Prompt 06 |
| context/practices-final.js | Complete DATA.dressPractices array ready to paste into index.html | Prompt 06 | Prompt 07 |

---

## Sub-Agent Strategy Reference

**SOLO:** Prompt executes as single task in its session. No sub-agents spawned.
**PARALLEL:** Prompt may spawn sub-agents for independent parallel sub-operations.

All prompts in this build are SOLO — each modifies a single shared file (index.html) and cannot safely parallelize writes.

---

## Step Breakdown by Category

| Category | Prompts | What Accomplished |
|---|---|---|
| Phase 0 — Prerequisite Verification | 01–03 | Codebase documented; clusters field and selectedSymptomIds confirmed or added |
| Phase 1 — Content Authoring | 04–06 | All DATA.dressPractices entries authored from FDN course modules; finalized fragment ready |
| Phase 2A — Data & Logic | 07–10 | Data layer, utility functions, state functions, render function added to index.html |
| Phase 2B — HTML & CSS | 11–13 | Nav tab, screen section, and all CSS classes added to index.html |
| Phase 2C — Interactions | 14–15 | Event delegation and badge logic added to index.html |
| Phase 3 — Verification | 16 | All 10 success criteria verified; build complete |

---

## Progress Tracking

| Step | Status |
|---|---|
| step-01-document-codebase-patterns | pending |
| step-02-verify-clusters-field | pending |
| step-03-verify-selected-symptoms-state | pending |
| step-04-author-practices-diet-rest-supplement | pending |
| step-05-author-practices-exercise-stress | pending |
| step-06-finalize-practices-data | pending |
| step-07-add-data-layer | pending |
| step-08-add-utility-functions | pending |
| step-09-add-state-functions | pending |
| step-10-add-render-function | pending |
| step-11-add-nav-tab-html | pending |
| step-12-add-screen-section-html | pending |
| step-13-add-css-classes | pending |
| step-14-add-event-delegation | pending |
| step-15-add-badge-logic | pending |
| step-16-verify-build | pending |
