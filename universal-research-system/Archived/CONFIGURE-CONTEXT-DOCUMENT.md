## SECTION 1 — REQUIRED READING

Read both files completely before doing any work. Do not begin analysis until both are fully read.

@universal-research-system/HOW-THIS-SYSTEM-WORKS.md
@universal-research-system/research-patterns-system-context.md

After reading both files, confirm in two sentences: (1) what the system does, (2) what you are about to change and why.

Then proceed immediately to SECTION 2. No preamble after the confirmation.

---

## SECTION 2 — CONTEXT SNAPSHOT

Critical facts — do not rely on file contents for these. These override anything you read in the files.

**Correct path for north-star.md:**
`universal-research-system/Research system brain/north-star.md`

**Correct path for this document (research-patterns-system-context.md):**
`universal-research-system/research-patterns-system-context.md`

**What changed:** The context document was relocated from `cie-bootstrap-output/ignore-user-notes/research-patterns-system-context.md` to `universal-research-system/research-patterns-system-context.md`. The north-star was also relocated from `starter-cie-system/north-star.md` to `universal-research-system/Research system brain/north-star.md`. Five path references inside `research-patterns-system-context.md` were not updated when the files moved. All five must be corrected.

**All 5 stale references — exact current text and exact replacement:**

STALE-1 — Header Authority line:
- CURRENT: `**Authority:** \`starter-cie-system/north-star.md\` (read at runtime per Rule NSA-2)`
- CORRECT: `**Authority:** \`universal-research-system/Research system brain/north-star.md\` (read at runtime per Rule NSA-2)`

STALE-2 — Mandatory Runtime Instruction block:
- CURRENT: `must read \`starter-cie-system/north-star.md\` in full before proceeding`
- CORRECT: `must read \`universal-research-system/Research system brain/north-star.md\` in full before proceeding`

STALE-3 — Section 5 MSA Layer hierarchy, Layer 0 description:
- CURRENT: `Layer 0: North Star (starter-cie-system/north-star.md)`
- CORRECT: `Layer 0: North Star (universal-research-system/Research system brain/north-star.md)`

STALE-4 — Section 8 file table, three rows:
- Row 1 CURRENT: `` `starter-cie-system/north-star.md` | Governing methodology — read at runtime (Rule NSA-2) | Exists ``
- Row 1 CORRECT: `` `universal-research-system/Research system brain/north-star.md` | Governing methodology — read at runtime (Rule NSA-2) | Exists ``
- Row 4 CURRENT: `` `cie-bootstrap-output/ignore-user-notes/research-patterns-system-context.md` | This document | Exists ``
- Row 4 CORRECT: `` `universal-research-system/research-patterns-system-context.md` | This document | Exists ``
- Row 5 CURRENT: `` `state.json` | System state — must be created on first run | Does not exist yet — WV-1 must be resolved ``
- Row 5 CORRECT: `` `universal-research-system/state.json` | System state — created on first run | Does not exist yet — created by command-01-research.md on first execution ``

STALE-5 — Section 10 SPEC-7, "Files to read at session start" block:
- CURRENT: `- starter-cie-system/north-star.md (Rule NSA-2 — mandatory)`
- CORRECT: `- universal-research-system/Research system brain/north-star.md (Rule NSA-2 — mandatory)`

**What is architecturally correct and must not be touched:**
- Section 1 (HAM extraction): all content correct
- Section 2 (variables): all content correct
- Section 3 (goals): all content correct
- Section 4 (ROE decompositions, System Ideas 1–7): all content correct
- Section 5 (MSA hierarchy): correct EXCEPT the Layer 0 north-star path (STALE-3)
- Section 6 (resolved decisions, WV-1 through WV-13): all content correct
- Section 7 (execution readiness): all content correct
- Section 9 (resolved questions): all content correct
- Section 10 SPEC-1 through SPEC-6 and SPEC-8 through SPEC-9: all content correct
- Section 10 SPEC-7: correct EXCEPT the path in the "Files to read at session start" block (STALE-5)
- All 13 wet variable decisions: correct, do not touch

---

## SECTION 3 — PROBLEM STATEMENTS

PROBLEM 1: Stale north-star path in document header
LOCATION: Document header, "Authority" field — line reads `**Authority:** \`starter-cie-system/north-star.md\` (read at runtime per Rule NSA-2)`
WHY IT MATTERS: Any session that reads this header and attempts to load the governing North Star document will halt on a missing-file error because `starter-cie-system/north-star.md` does not exist in the portable `universal-research-system/` folder — the system cannot execute.
CURRENT TEXT: `**Authority:** \`starter-cie-system/north-star.md\` (read at runtime per Rule NSA-2)`
CORRECT TEXT: `**Authority:** \`universal-research-system/Research system brain/north-star.md\` (read at runtime per Rule NSA-2)`

---

PROBLEM 2: Stale north-star path in Mandatory Runtime Instruction
LOCATION: MANDATORY RUNTIME INSTRUCTION section — the sentence beginning "Any Claude Code session executing from this document must read..."
WHY IT MATTERS: The instruction that enforces Rule NSA-2 points to a nonexistent path, so any session that follows it verbatim will fail to load the North Star and will execute without the governing rules in place.
CURRENT TEXT: `must read \`starter-cie-system/north-star.md\` in full before proceeding`
CORRECT TEXT: `must read \`universal-research-system/Research system brain/north-star.md\` in full before proceeding`

---

PROBLEM 3: Stale north-star path in Section 5 MSA Layer hierarchy
LOCATION: Section 5 "Nested System Hierarchies (MSA Layer Logic)" — the Layer 0 description line inside the code block
WHY IT MATTERS: The MSA layer diagram names an incorrect location for the North Star, causing any session that uses this diagram to understand system architecture to derive the wrong governing document path.
CURRENT TEXT: `Layer 0: North Star (starter-cie-system/north-star.md)`
CORRECT TEXT: `Layer 0: North Star (universal-research-system/Research system brain/north-star.md)`

---

PROBLEM 4: Three stale paths in Section 8 file table
LOCATION: Section 8 "Files Required for Execution" — the table rows for north-star.md (Row 1), this context document (Row 4), and state.json (Row 5)
WHY IT MATTERS: A session using this table to locate required files will attempt to read three files at wrong paths — north-star will not be found, this document's self-reference will be wrong, and state.json's path omits its containing folder, making it unresolvable in a portable deployment.
CURRENT TEXT (Row 1): `` `starter-cie-system/north-star.md` | Governing methodology — read at runtime (Rule NSA-2) | Exists ``
CORRECT TEXT (Row 1): `` `universal-research-system/Research system brain/north-star.md` | Governing methodology — read at runtime (Rule NSA-2) | Exists ``
CURRENT TEXT (Row 4): `` `cie-bootstrap-output/ignore-user-notes/research-patterns-system-context.md` | This document | Exists ``
CORRECT TEXT (Row 4): `` `universal-research-system/research-patterns-system-context.md` | This document | Exists ``
CURRENT TEXT (Row 5): `` `state.json` | System state — must be created on first run | Does not exist yet — WV-1 must be resolved ``
CORRECT TEXT (Row 5): `` `universal-research-system/state.json` | System state — created on first run | Does not exist yet — created by command-01-research.md on first execution ``

---

PROBLEM 5: Stale north-star path in SPEC-7 meta-prompt template
LOCATION: Section 10 SPEC-7 "Meta-Prompt Structure" — the "Files to read at session start" block inside the code block
WHY IT MATTERS: Every overflow meta-prompt generated by the command will instruct the receiving session to read the North Star from a nonexistent path, causing every split execution to fail at the cold-start read sequence.
CURRENT TEXT: `- starter-cie-system/north-star.md (Rule NSA-2 — mandatory)`
CORRECT TEXT: `- universal-research-system/Research system brain/north-star.md (Rule NSA-2 — mandatory)`

---

## SECTION 4 — DESIRED OUTCOME

When the work is complete, all of the following are true about `universal-research-system/research-patterns-system-context.md`:

- Zero occurrences of `starter-cie-system` remain anywhere in the file
- Zero occurrences of `cie-bootstrap-output/ignore-user-notes/research-patterns-system-context.md` remain
- Section 8 file table reflects the actual current file locations: north-star at `universal-research-system/Research system brain/north-star.md`, this document at `universal-research-system/research-patterns-system-context.md`, state.json at `universal-research-system/state.json`
- SPEC-7 "Files to read at session start" block references the correct north-star path
- All other sections (1–4, 6–7, 9, SPEC-1 through SPEC-6, SPEC-8, SPEC-9) are byte-for-byte identical to the pre-edit version
- The document is accurate for a fresh session dropped into any workspace containing `universal-research-system/`
- The document is ready to serve as the build contract for `command-01-research.md`

---

## SECTION 5 — CONSTRAINTS

- Must not modify any content in Section 10 SPEC-1, SPEC-2, SPEC-3, SPEC-4, SPEC-5, SPEC-6, SPEC-8, SPEC-9
- Must not modify any resolved wet variable decisions (Section 6, WV-1 through WV-13)
- Must not modify any HAM content (Section 1), variable lists (Section 2), goals (Section 3), or ROE decompositions (Section 4)
- Must not build `command-01-research.md`
- Must not restructure, rename, or reorder any sections
- Must not add new sections
- Must not remove any content — only update the specific text identified in the problem statements

---

## SECTION 6 — IMPLEMENTATION PLAN

STEP 1: Fix header Authority line
NAVIGATE TO: Document header (top of file, before MANDATORY RUNTIME INSTRUCTION)
FIND: `**Authority:** \`starter-cie-system/north-star.md\` (read at runtime per Rule NSA-2)`
REPLACE WITH: `**Authority:** \`universal-research-system/Research system brain/north-star.md\` (read at runtime per Rule NSA-2)`

---

STEP 2: Fix Mandatory Runtime Instruction
NAVIGATE TO: MANDATORY RUNTIME INSTRUCTION section
FIND: `must read \`starter-cie-system/north-star.md\` in full before proceeding`
REPLACE WITH: `must read \`universal-research-system/Research system brain/north-star.md\` in full before proceeding`

---

STEP 3: Fix Section 5 Layer 0 description
NAVIGATE TO: SECTION 5 "Nested System Hierarchies (MSA Layer Logic)" — the code block beginning with "Layer 0:"
FIND: `Layer 0: North Star (starter-cie-system/north-star.md)`
REPLACE WITH: `Layer 0: North Star (universal-research-system/Research system brain/north-star.md)`

---

STEP 4: Fix Section 8 file table — three rows
NAVIGATE TO: SECTION 8 "Files Required for Execution" — the markdown table

Row 1:
FIND: `` `starter-cie-system/north-star.md` | Governing methodology — read at runtime (Rule NSA-2) | Exists ``
REPLACE WITH: `` `universal-research-system/Research system brain/north-star.md` | Governing methodology — read at runtime (Rule NSA-2) | Exists ``

Row 4:
FIND: `` `cie-bootstrap-output/ignore-user-notes/research-patterns-system-context.md` | This document | Exists ``
REPLACE WITH: `` `universal-research-system/research-patterns-system-context.md` | This document | Exists ``

Row 5:
FIND: `` `state.json` | System state — must be created on first run | Does not exist yet — WV-1 must be resolved ``
REPLACE WITH: `` `universal-research-system/state.json` | System state — created on first run | Does not exist yet — created by command-01-research.md on first execution ``

---

STEP 5: Fix SPEC-7 Files to read block
NAVIGATE TO: SECTION 10 SPEC-7 "Meta-Prompt Structure" — the code block, under the "## Files to read at session start" heading
FIND: `- starter-cie-system/north-star.md (Rule NSA-2 — mandatory)`
REPLACE WITH: `- universal-research-system/Research system brain/north-star.md (Rule NSA-2 — mandatory)`

---

STEP 6: Verify
Search the updated file for `starter-cie-system` — zero occurrences should remain.
Search the updated file for `cie-bootstrap-output/ignore-user-notes/research-patterns-system-context.md` — zero occurrences should remain.
Confirm Section 8 file table Row 1 shows `universal-research-system/Research system brain/north-star.md`.
Confirm Section 8 file table Row 4 shows `universal-research-system/research-patterns-system-context.md`.
Confirm Section 8 file table Row 5 shows `universal-research-system/state.json`.
Confirm SPEC-7 "Files to read at session start" block shows `universal-research-system/Research system brain/north-star.md`.

---

## SECTION 7 — WHAT THIS DOCUMENT IS NOT

This document configures the context file only. It does not build the command. Building `command-01-research.md` is a separate step that uses the corrected `research-patterns-system-context.md` as its build contract — that session reads the corrected spec and implements exactly what is specified there. Do not build the command in the same session as the configuration fix.
