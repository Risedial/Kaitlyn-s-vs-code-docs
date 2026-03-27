# FDN Symptom Navigator — Build Orchestration

**Build target:** `fdn-pwa/` (3 files: index.html, manifest.json, sw.js)
**Total steps:** 40
**State checkpoint:** `connect-da-dots/state.json`

Run each prompt in a **fresh Claude Code session**. Open the prompt file and paste its full contents. Complete the task, update state.json, then close the session before starting the next.

---

## Prompt Index

| # | File | Title | Mode | Prerequisite Flag | Output Flag |
|---|------|-------|------|-------------------|-------------|
| 01 | [prompt-01.md](prompt-01.md) | Initialize Build — Create fdn-pwa/ Directory and File Stubs | SOLO | _(none)_ | `initialized` |
| 02 | [prompt-02.md](prompt-02.md) | Write manifest.json — Full PWA Manifest with Base64 PNG Icons | SOLO | `initialized` | `manifestWritten` |
| 03 | [prompt-03.md](prompt-03.md) | Write sw.js — Cache-First Service Worker | SOLO | `initialized` | `swWritten` |
| 04 | [prompt-04.md](prompt-04.md) | Write index.html — Full HTML Document Shell with All Placeholders | SOLO | `swWritten` | `htmlShellWritten` |
| 05 | [prompt-05.md](prompt-05.md) | Write CSS — Design Tokens (:root custom properties) | SOLO | `htmlShellWritten` | `cssDesignTokens` |
| 06 | [prompt-06.md](prompt-06.md) | Write CSS — Base Reset and Body Styles | SOLO | `cssDesignTokens` | `cssBaseReset` |
| 07 | [prompt-07.md](prompt-07.md) | Write CSS — Layout and App Container | SOLO | `cssBaseReset` | `cssLayout` |
| 08 | [prompt-08.md](prompt-08.md) | Write CSS — Top Header (Frosted Glass) | SOLO | `cssLayout` | `cssHeader` |
| 09 | [prompt-09.md](prompt-09.md) | Write CSS — Bottom Tab Bar | SOLO | `cssHeader` | `cssTabBar` |
| 10 | [prompt-10.md](prompt-10.md) | Write CSS — List Rows and Accordion Sections | SOLO | `cssTabBar` | `cssListRows` |
| 11 | [prompt-11.md](prompt-11.md) | Write CSS — Variable Pills and Cluster Tags | SOLO | `cssListRows` | `cssPillsTags` |
| 12 | [prompt-12.md](prompt-12.md) | Write CSS — Bottom Sheet | SOLO | `cssPillsTags` | `cssBottomSheet` |
| 13 | [prompt-13.md](prompt-13.md) | Write CSS — Alert Banner and Search Bar | SOLO | `cssBottomSheet` | `cssAlertSearch` |
| 14 | [prompt-14.md](prompt-14.md) | Write CSS — Animations and Reduced Motion | SOLO | `cssAlertSearch` | `cssAnimations` |
| 15 | [prompt-15.md](prompt-15.md) | Write JS — DATA Object Skeleton with Nested Placeholders | SOLO | `cssAnimations` | `dataSkeletonWritten` |
| 16 | [prompt-16.md](prompt-16.md) | Write Data — Symptom Batch 1: Energy & Fatigue + Sleep (11 entries) | SOLO | `dataSkeletonWritten` | `symptomsBatch1` |
| 17 | [prompt-17.md](prompt-17.md) | Write Data — Symptom Batch 2: Mood & Emotions (9 entries) | SOLO | `symptomsBatch1` | `symptomsBatch2` |
| 18 | [prompt-18.md](prompt-18.md) | Write Data — Symptom Batch 3: Digestion (10 entries) | SOLO | `symptomsBatch2` | `symptomsBatch3` |
| 19 | [prompt-19.md](prompt-19.md) | Write Data — Symptom Batch 4: Food Reactions + Skin (11 entries) | SOLO | `symptomsBatch3` | `symptomsBatch4` |
| 20 | [prompt-20.md](prompt-20.md) | Write Data — Symptom Batch 5: Immune + Hormonal Female (12 entries) | SOLO | `symptomsBatch4` | `symptomsBatch5` |
| 21 | [prompt-21.md](prompt-21.md) | Write Data — Symptom Batch 6: Hormonal Male + Cardiovascular + Pain (12 entries) | SOLO | `symptomsBatch5` | `symptomsBatch6` |
| 22 | [prompt-22.md](prompt-22.md) | Write Data — Symptom Batch 7: Respiratory + Cognitive + Stress (11 entries) | SOLO | `symptomsBatch6` | `symptomsBatch7` |
| 23 | [prompt-23.md](prompt-23.md) | Write Data — Variable Batch 1: MWP + MBA Panels (6 entries) | SOLO | `symptomsBatch7` | `variablesBatch1` |
| 24 | [prompt-24.md](prompt-24.md) | Write Data — Variable Batch 2: SHP Panel (7 entries) | SOLO | `variablesBatch1` | `variablesBatch2` |
| 25 | [prompt-25.md](prompt-25.md) | Write Data — Variable Batch 3: GI-MAP Panel (10 entries) | SOLO | `variablesBatch2` | `variablesBatch3` |
| 26 | [prompt-26.md](prompt-26.md) | Write Data — Variable Batch 4: Cross-Panel Constructs (5 entries) | SOLO | `variablesBatch3` | `variablesBatch4` |
| 27 | [prompt-27.md](prompt-27.md) | Write Data — All 5 Root Cause Clusters | SOLO | `variablesBatch4` | `clusterData` |
| 28 | [prompt-28.md](prompt-28.md) | Verify Data Integrity — Count 76/28/5, Spot-Check Critical Flags | SOLO | `clusterData` | `dataIntegrityVerified` |
| 29 | [prompt-29.md](prompt-29.md) | Write JS — State Machine Core (state, maps, el/txt helpers, sheet functions) | SOLO | `dataIntegrityVerified` | `stateMachineCore` |
| 30 | [prompt-30.md](prompt-30.md) | Write JS — navigateTab(), renderScreen(), renderClusters() | SOLO | `stateMachineCore` | `navigateFunctions` |
| 31 | [prompt-31.md](prompt-31.md) | Write JS — renderHome() with Category Accordions | SOLO | `navigateFunctions` | `renderHome` |
| 32 | [prompt-32.md](prompt-32.md) | Write JS — renderSymptom() with H. pylori Alert Guard | SOLO | `renderHome` | `renderSymptom` |
| 33 | [prompt-33.md](prompt-33.md) | Write JS — renderVariable() with Medical Referral and Cross-Panel Badges | SOLO | `renderSymptom` | `renderVariable` |
| 34 | [prompt-34.md](prompt-34.md) | Write JS — renderCluster() with Cluster E Referral and Cluster A Priority Blocks | SOLO | `renderVariable` | `renderCluster` |
| 35 | [prompt-35.md](prompt-35.md) | Write JS — renderSearch() with Live Symptom and Variable Search | SOLO | `renderCluster` | `renderSearch` |
| 36 | [prompt-36.md](prompt-36.md) | Write JS — Event Delegation Handler (click + keydown) | SOLO | `renderSearch` | `eventDelegation` |
| 37 | [prompt-37.md](prompt-37.md) | Write JS — Service Worker Registration and init() Function | SOLO | `eventDelegation` | `swRegistrationInit` |
| 38 | [prompt-38.md](prompt-38.md) | Integration Assembly — Verify Zero Placeholders and Script Order | SOLO | `swRegistrationInit` | `integrationAssembly` |
| 39 | [prompt-39.md](prompt-39.md) | Verify manifest.json — Validate PWA Installability Requirements | SOLO | `manifestWritten` | `manifestVerified` |
| 40 | [prompt-40.md](prompt-40.md) | Final PWA Verification Checklist | SOLO | `manifestVerified` | `finalVerification` |

---

## Execution Order

All prompts are **SOLO** — each must complete fully before the next begins. The dependency chain is linear: each prompt's output flag is the next prompt's prerequisite flag.

**Exception:** Prompt 39 (manifest verification) depends only on `manifestWritten` (set by step 02), so it can technically run after step 02 completes. However, running it last (after step 38) is recommended to confirm no edits broke the manifest.

---

## Data Coverage Summary

| Category | Entries | Prompts |
|----------|---------|---------|
| Symptoms | 76 | 16–22 |
| Variables | 28 | 23–26 |
| Clusters | 5 | 27 |

| Symptom Batch | Categories | Count |
|---------------|-----------|-------|
| Batch 1 | Energy & Fatigue, Sleep | 11 |
| Batch 2 | Mood & Emotions | 9 |
| Batch 3 | Digestion | 10 |
| Batch 4 | Food Reactions, Skin | 11 |
| Batch 5 | Immune System, Hormonal Female | 12 |
| Batch 6 | Hormonal Male & Shared, Cardiovascular, Pain & Inflammation | 12 |
| Batch 7 | Respiratory, Cognitive & Neurological, Stress & Nervous System | 11 |
| **Total** | **14 categories** | **76** |

| Variable Batch | Panel | Count |
|----------------|-------|-------|
| Batch 1 | MWP + MBA | 6 |
| Batch 2 | SHP | 7 |
| Batch 3 | GI-MAP | 10 |
| Batch 4 | Cross-Panel Constructs | 5 |
| **Total** | **5 panels** | **28** |

---

## Critical Business Rules (enforced by JS render functions)

1. **H. pylori alert** — Any symptom with `hpylori` in its `variables` array must show a red destructive alert banner BEFORE variable pills (enforced by `renderSymptom`, step 32).
2. **Medical referral** — Variables with `isMedicalReferral: true` (`calprotectin`, `occult-blood`) must show referral banner (enforced by `renderVariable`, step 33).
3. **Cluster E referral** — Cluster E detail view must show medical referral block at top (enforced by `renderCluster`, step 34).
4. **Cluster A priority** — Cluster A detail view must show priority note "Address Before All Other Clusters" (enforced by `renderCluster`, step 34).
5. **Cross-panel badge** — Variables with `isCrossPanel: true` must show `CROSS-PANEL AMPLIFIER` badge (enforced by `renderVariable`, step 33).
6. **No innerHTML** — All DOM construction uses `el()` and `txt()` helpers only (enforced by step 38 audit).
