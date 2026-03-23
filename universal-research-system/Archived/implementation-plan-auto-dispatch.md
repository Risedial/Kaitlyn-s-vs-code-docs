# Implementation Plan: Auto-Dispatch Session Management
# Self-Contained Execution Prompt — Paste into a fresh Claude Code chat to execute

---

## YOUR TASK

Modify the Universal Research System command so that the user never needs to manually copy-paste meta-prompts. After this change, the user only ever runs `/command-01-research` in a fresh chat. The command reads state.json, resumes where it left off, works through as much as the session budget allows, saves state, and stops cleanly. The next session picks up automatically.

**You are modifying one file:**
`c:\Users\Alexb\Documents\Alex's Applications\video-transcriber\universal-research-system\commands\command-01-research.md`

**Before making any changes, read these files in full:**
1. `c:\Users\Alexb\Documents\Alex's Applications\video-transcriber\universal-research-system\commands\command-01-research.md`
2. `c:\Users\Alexb\Documents\Alex's Applications\video-transcriber\universal-research-system\state.json`

---

## PROBLEM BEING SOLVED

The current overflow logic (Phase 3 Step 3.1 and Phase 4 Step 4.1) estimates **all remaining output** for the entire pending list before processing any item. With 37 variables × ~1,400 tokens each = ~50,000 tokens, this triggers immediately on variable 1 of every session — generating a meta-prompt file that requires the user to manually copy-paste into a fresh chat. The system never makes progress automatically.

---

## SOLUTION ARCHITECTURE

Replace the "estimate remaining" overflow model with a **session budget tracker**:

- Each session starts a local counter: `session_items_processed = 0`
- Before each item: check if `session_items_processed × estimated_tokens_per_item >= 18,000`
- If YES → save state, write next-session.md, stop
- If NO → process the item, increment counter, continue

This means each session processes approximately 12–14 variables (or 25+ connection pairs), then stops cleanly. The next `/command-01-research` run reads state.json, finds the remaining pending items, and continues from exactly where the previous session ended. No meta-prompts. No manual copy-paste. No changes to state.json schema.

---

## EXACT CHANGES TO MAKE

Make exactly 5 targeted edits to `command-01-research.md`. Use the exact old text below to locate each section, then replace with the new text.

---

### CHANGE 1 — Phase 3, Step 3.1: Replace overflow check with session budget check

**FIND this exact text (Step 3.1 header and body):**

```
### Step 3.1 — Overflow check (run before processing each variable)

Before beginning work on each variable, estimate the remaining output for this session.

**If estimated remaining output exceeds 20,000 tokens:**
1. Generate a SPEC-7 meta-prompt (see Output Specifications section) for the remaining items in `state.pending_variables[]`
2. Write it to: `universal-research-system/session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md` (n = next available number, counted from existing meta-prompt files in session-outputs/)
3. Write current `universal-research-system/state.json`
4. Write `universal-research-system/next-session.md` (SPEC-6 format)
5. **Stop.** Do not continue processing any more variables inline.
```

**REPLACE WITH:**

```
### Step 3.1 — Session budget check (run before processing each variable)

Maintain a session-local counter: `session_variables_processed` — starts at 0 when this command runs, increments by 1 after each variable is completed (pass or fail the completion gate).

**Before beginning work on each variable:**
Calculate: `session_variables_processed × 1,400`

**If result ≥ 18,000:**
1. `state.json` is already current (MC-8 wrote it after the last variable)
2. Write `universal-research-system/next-session.md` (SPEC-6 format — set "Variables remaining" to count of `pending_variables[]`)
3. **Stop.** Do not process any more variables this session.

**If result < 18,000:** Proceed to research this variable.
```

---

### CHANGE 2 — Phase 4, Step 4.1: Replace overflow check with session budget check

**FIND this exact text (Step 4.1 header and body):**

```
### Step 4.1 — Overflow check (run before processing each pair)

Before beginning work on each pair, estimate the remaining output for this session.

**If estimated remaining output exceeds 20,000 tokens:**
1. Generate a SPEC-7 meta-prompt for the remaining items in `state.connections.pending[]`
2. Write it to: `universal-research-system/session-outputs/[YYYY-MM-DD]-meta-prompt-[n].md`
3. Write current `universal-research-system/state.json`
4. Write `universal-research-system/next-session.md` (SPEC-6 format)
5. **Stop.** Do not continue processing any more pairs inline.
```

**REPLACE WITH:**

```
### Step 4.1 — Session budget check (run before processing each pair)

Maintain a session-local counter: `session_pairs_processed` — starts at 0 when this command runs, increments by 1 after each pair is moved to validated or discarded.

**Before beginning work on each pair:**
Calculate: `session_pairs_processed × 500`

**If result ≥ 18,000:**
1. `state.json` is already current (MC-8 wrote it after the last pair)
2. Write `universal-research-system/next-session.md` (SPEC-6 format — set "Connections remaining" to count of `connections.pending[]`)
3. **Stop.** Do not process any more pairs this session.

**If result < 18,000:** Proceed to evaluate this pair.
```

---

### CHANGE 3 — SPEC-6: Update "Command to Send" instruction

**FIND this exact text (inside the SPEC-6 section):**

```
## Command to Send
/command-01-research [original research question — exact text, not a placeholder]
```

**REPLACE WITH:**

```
## Command to Send
/command-01-research

(No argument needed after Phase 1 — the research question is stored in state.json. Only include the research question as an argument when state.json does not yet exist.)
```

**Also find this line immediately after the SPEC-6 block:**

```
**"Command to Send"** must contain the actual research question text, not the word "topic" or any other placeholder.
```

**REPLACE WITH:**

```
**"Command to Send"** is `/command-01-research` with no argument for all phases after problem_framing. The research question is read from state.json. Only include the question as an argument on the very first run when state.json does not exist.
```

---

### CHANGE 4 — SPEC-7: Mark as deprecated (no longer in execution path)

**FIND this exact text (SPEC-7 header):**

```
### SPEC-7: Meta-Prompt Structure (Overflow Split)

Generated when estimated session output exceeds 20,000 tokens. All fields derived from `state.json` at generation time — no fixed template values.
```

**REPLACE WITH:**

```
### SPEC-7: Meta-Prompt Structure (Deprecated — not used in execution path)

This format is no longer generated automatically. Session management is handled by the session budget check in Phase 3 Step 3.1 and Phase 4 Step 4.1. SPEC-7 is retained for reference only — it may be used for manual session planning if needed, but the command does not generate or consume meta-prompt files.
```

---

### CHANGE 5 — CONSTRAINT ENFORCEMENT table: Update M-3 entry

**FIND this exact text (inside the CONSTRAINT ENFORCEMENT table):**

```
| M-3 | Dynamic decomposition at 20,000 token estimated output | SPEC-7 meta-prompt generation in Phase 3 Step 3.1 and Phase 4 Step 4.1 |
```

**REPLACE WITH:**

```
| M-3 | Session budget cap: stop at 18,000 estimated tokens used per session | Phase 3 Step 3.1 and Phase 4 Step 4.1 — session_variables_processed and session_pairs_processed counters enforce per-session budget |
```

---

## VALIDATION — CHECK THESE AFTER MAKING ALL 5 CHANGES

Read the modified `command-01-research.md` and confirm:

1. **Phase 3 Step 3.1** — No longer mentions "remaining output" or "meta-prompt." Uses `session_variables_processed × 1,400 >= 18,000` as the stop condition.

2. **Phase 4 Step 4.1** — No longer mentions "remaining output" or "meta-prompt." Uses `session_pairs_processed × 500 >= 18,000` as the stop condition.

3. **SPEC-6 "Command to Send"** — Says `/command-01-research` with no argument (and explains why).

4. **SPEC-7** — Marked as deprecated, not referenced anywhere in execution logic.

5. **CONSTRAINT ENFORCEMENT table** — M-3 row describes session budget counter, not meta-prompt generation.

6. **Logic trace — does it work?**
   - Session 1: `session_variables_processed` starts at 0. Check: `0 × 1,400 = 0 < 18,000` → process variable 1. After: counter = 1. Check: `1 × 1,400 = 1,400 < 18,000` → process variable 2. Continue until `13 × 1,400 = 18,200 ≥ 18,000` → stop. 13 variables researched. state.json has them in `researched_variables[]`, 24 remaining in `pending_variables[]`.
   - Session 2: counter resets to 0. Reads state.json. Finds 24 remaining. Starts from first item in `pending_variables[]`. Processes ~12 more. Stops.
   - Session 3: processes remaining 12. `pending_variables[]` is empty. Phase advances to `connection_validation`.
   - All subsequent sessions: same pattern for connection pairs.
   - **Result:** User runs `/command-01-research` each session. Command self-manages. No meta-prompts. ✓

---

## AFTER MAKING CHANGES

1. The existing file `universal-research-system/session-outputs/2026-03-15-meta-prompt-1.md` can be ignored — it was generated under the old logic and is no longer needed.

2. `state.json` is already at `phase = "variable_research"` with 37 variables in `pending_variables[]`. The next `/command-01-research` run will resume Phase 3 automatically and process ~13 variables before stopping.

3. Do not modify `state.json` or any other file — only `command-01-research.md` changes.

4. Report: "Changes complete. command-01-research.md updated with session budget checks. Meta-prompt mechanism removed from execution path. User workflow: clear chat → run /command-01-research → repeat until synthesis."
