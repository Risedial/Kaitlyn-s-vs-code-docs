You are executing a production-grade application audit. Two directory paths have been provided as arguments to this command:
- Argument 1 = CONTEXT_FOLDER_PATH (read-only domain knowledge, specs, schemas, requirements)
- Argument 2 = APP_FOLDER_PATH (application source code to audit and fix)

If either path was not provided as an argument, use AskUserQuestion to ask for both before proceeding. Do not guess paths.

---

## PRE-FLIGHT: Read Methodology

Before any other action, read the following files in order:
1. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\methodology\README.md`
2. `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\claude-build-system\methodology\system-integrity-rules.md`

Follow the README's START HERE steps to confirm this is a full pipeline (Stages 1–8) task. Apply system-integrity-rules.md as a standing constraint throughout all phases.

---

## PHASE 1: FULL ASSET INVENTORY

Execute steps 1a–1d sequentially. Write nothing to disk during this phase — read and record only.

**1a. Read all files in CONTEXT_FOLDER_PATH.**
For each file, record: filename, type, purpose, all locked design decisions, canonical values, and constraints.

**1b. Read all files in APP_FOLDER_PATH recursively.**
Use Glob to enumerate every file. For each file, record:
- Relative path from APP_FOLDER_PATH
- Type: component / utility / style / config / test / asset / data / script
- Role in the application
- All imports and external dependencies declared

**1c. Build a dependency graph.**
For every file in APP_FOLDER_PATH: list which files it imports, and which files import it. Identify the full downstream impact surface of each file.

**1d. Lock the technology stack.**
From the files read, identify and record as immutable locked values: framework, language, build tool, styling system, state management library, routing library, data layer, testing framework, deployment target.

---

## PHASE 2: EXHAUSTIVE MULTI-DIMENSIONAL AUDIT

Apply all 18 audit dimensions below to every file and to the application as a whole. Do NOT skip any dimension — if no flaws are found in a dimension, record it explicitly as "CONFIRMED CLEAN."

For each flaw found, record these exact fields:
- **FLAW_ID**: sequential integer starting at 1
- **FILE**: exact relative path from APP_FOLDER_PATH
- **LINE_RANGE**: start–end line numbers, or "global" for app-wide issues
- **DIMENSION**: the audit dimension number and name
- **SEVERITY**: CRITICAL / HIGH / MEDIUM / LOW
- **DESCRIPTION**: the exact observable broken condition (no "improve" or "fix" language — describe what IS wrong as a fact)
- **BILLION_DOLLAR_CRITERION**: which criterion(a) below this violates
- **CASCADING_RISK**: every other file and line affected when this flaw is corrected

**Audit Dimensions:**
1. FUNCTIONAL CORRECTNESS — logic errors, off-by-one, null/undefined dereferences, incorrect conditionals, missing return values, wrong data transformations
2. USER EXPERIENCE — flow breaks, unclear affordances, missing loading/error/empty states, inconsistent interaction patterns, missing feedback on user actions
3. VISUAL FIDELITY — layout breaks at any viewport, spacing inconsistency, color/contrast violations, font rendering issues, z-index conflicts, overflow/clip errors
4. ACCESSIBILITY — WCAG 2.1 AA violations: missing aria-labels, non-keyboard-navigable interactions, missing focus indicators, color-only information encoding, missing alt text, improper heading hierarchy, missing form labels
5. PERFORMANCE — unnecessary re-renders, blocking operations on main thread, unoptimized assets, missing lazy loading, memory leaks, excessive bundle size contributors, N+1 query patterns
6. SECURITY — XSS vectors, injection vulnerabilities, unvalidated input at system boundaries, exposed secrets or API keys, insecure data storage, CSRF exposure, missing Content-Security-Policy, auth bypass conditions
7. ERROR HANDLING — unhandled promise rejections, missing try/catch at I/O boundaries, missing error boundaries in component trees, silent failures, cryptic error messages shown to users
8. DATA INTEGRITY — race conditions, optimistic update without rollback, stale cache serving wrong data, missing data validation before persistence, type coercion errors
9. STATE MANAGEMENT — impossible states representable in the state model, state mutations that bypass the single source of truth, missing cleanup on unmount, subscriptions not unsubscribed
10. ARCHITECTURE — circular dependencies, god components/modules, missing separation of concerns, hardcoded values that should be configurable, vendor lock-in risks
11. CODE QUALITY — dead code, duplicate logic that should be unified, commented-out code, misleading variable/function names, inconsistent naming conventions
12. TESTING GAPS — untested critical paths, missing edge case coverage, tests that don't actually verify the described behavior
13. SEO & METADATA — missing meta tags, incorrect Open Graph data, missing structured data, non-indexable routes, missing canonical URLs
14. CROSS-BROWSER/DEVICE COMPATIBILITY — CSS properties without vendor prefixes, APIs not available in all target environments, missing polyfills for declared targets
15. INTERNATIONALIZATION — hardcoded strings that should be translatable, date/number/currency format assumptions, LTR-only layout assumptions
16. LEGAL/COMPLIANCE — missing required disclosures, cookie consent violations, GDPR/CCPA data handling gaps, missing privacy policy links
17. BUILD & DEPLOYMENT — broken build configs, missing environment variable documentation, hardcoded dev URLs in production code, missing .gitignore entries for sensitive files
18. DOCUMENTATION GAPS — missing JSDoc on public APIs, undocumented non-obvious behavior, missing README instructions

**Billion-Dollar Success Criteria** (every flaw must map to one or more):
- **RELIABILITY**: The app never shows a broken state to any user under any circumstance
- **PERFORMANCE**: Every interaction responds within 100ms perceived; first meaningful paint <1.5s on 4G
- **ACCESSIBILITY**: Any user, regardless of ability, can complete every primary user flow
- **SECURITY**: No user data can be compromised by any known attack vector
- **CORRECTNESS**: Every operation produces the mathematically/logically correct result
- **POLISH**: Every visual and interaction detail is intentional, consistent, and refined
- **TRUST**: The app communicates clearly, never misleads, and handles every failure gracefully
- **SCALABILITY**: No architectural decision creates a ceiling below 10M users

---

## PHASE 3: CASCADING CHANGE IMPACT ANALYSIS

For every flaw in the audit registry, complete steps 3a–3d before writing the plan:

**3a.** Trace full downstream impact: which files import the affected file, which components render the affected component, which tests must update, which types/interfaces change.

**3b.** Group flaws into CHANGE CLUSTERS — sets of flaws whose fixes must be applied simultaneously because fixing one creates a broken intermediate state if the others are not applied at the same time.

**3c.** Identify SAFE INDEPENDENT FIXES — flaws whose corrections have zero downstream effect on any other flaw and can be applied in any order.

**3d.** Produce a dependency-ordered fix sequence. Rule: no fix may depend on a fix that appears after it in the sequence. Fixes with no prerequisites come first.

---

## PHASE 4: WRITE IMPLEMENTATION_PLAN.md

Write the complete plan as a single file to: `APP_FOLDER_PATH/IMPLEMENTATION_PLAN.md`

Use the Write tool to create this file. The file must contain every section below in this exact order, with no sections omitted.

```
# Application Implementation Plan
Generated by Universal Audit Methodology
Date: [today's date in YYYY-MM-DD format]
App: [APP_FOLDER_PATH]
Context: [CONTEXT_FOLDER_PATH]

## Summary
- Total flaws found: [N]
- CRITICAL: [N] | HIGH: [N] | MEDIUM: [N] | LOW: [N]
- Change clusters: [N]
- Safe independent fixes: [N]
- Estimated files modified: [N]

## Technology Stack
[All locked values from Phase 1d]

## Fix Execution Order
[Numbered list of FLAW_IDs in dependency-ordered sequence from Phase 3d]

## Fixes
[One entry per flaw, in execution order — see template below]

## Verification Checklist
[One binary pass/fail check per fix that confirms the fix was applied correctly]

## Regression Risk Register
[For every fix with SEVERITY ≥ HIGH: the specific regression it could introduce and the exact file:line to inspect after applying it]
```

**Fix Entry Template** (repeat exactly for every flaw):

```
---
### FIX [FLAW_ID]: [SEVERITY] — [one sentence: the exact observable broken condition]
**File:** `[exact/relative/path/to/file.ext]`
**Lines:** [start]–[end]  (alternatives: "ADD AFTER line [N]" / "ADD AT TOP OF FILE" / "NEW FILE")
**Dimension:** [dimension number and name]
**Criterion violated:** [billion-dollar criterion name(s)]
**Cascading files affected:** [list of files, or "none"]

**Current code (exact):**
[language]
[verbatim copy of the current lines — no paraphrasing, no summarizing]


**Replace with (exact):**
[language]
[complete, executable replacement — no placeholders, no "[existing code]" shorthand, no "[add your value here]"]


**Why this fixes it:** [one sentence: the observable condition that will be true after this fix]

**Cascading change required in [filename]:**
- Lines [start]–[end]: [exact change required — fully specified, no forward references]

**Do NOT:** [one specific anti-pattern to avoid when applying this fix]
---
```

---

## HARD CONSTRAINTS

**STOP and use AskUserQuestion before proceeding if:**
- You cannot determine the exact replacement code for any "Replace with" block
- A cascading change exists but you cannot fully specify it
- A fix conflicts with another fix in the same change cluster and the conflict cannot be resolved automatically

**NEVER:**
- Omit a dimension from the audit because the app appears clean — confirm clean explicitly
- Write "improve [X]" or "refactor [X]" — state the exact broken condition and the exact fixed condition
- Combine two independent flaws into one Fix entry
- Include any placeholder text in a "Replace with" block
- Reference "see Fix N" for cascading changes — every cascading change must be fully specified in the Fix entry where it was discovered
- Apply fixes in an order that violates the dependency DAG

**Change cluster labeling:** Fixes belonging to the same cluster must appear sequentially and be labeled: `[CLUSTER N — Part X of Y]`

**New file requirement:** If a fix requires a new file, specify in that Fix entry: (1) the complete file path, (2) the complete file contents, (3) which existing file must import it and the exact import line to add.

**Dependency installation requirement:** If a fix requires a new package, specify: the exact package name, the exact version constraint, and the exact line to add in the relevant manifest file.

---

## OUTPUT

After successfully writing IMPLEMENTATION_PLAN.md, output exactly one line to the chat:

`PLAN WRITTEN: [total fix count] fixes across [file count] files. CRITICAL: [N]. Clusters: [N]. Plan at: [full absolute path to IMPLEMENTATION_PLAN.md]`

Write nothing else to the chat.
