# Prompt 01: Document Codebase Patterns

## Prerequisites

none

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html` in full. Write `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` containing exactly the following ten sections:

**Section 1 — Render Functions**
List every function named `renderXxxScreen()` or equivalent screen-rendering function. For each: exact function name, signature, brief description of what it renders.

**Section 2 — Event Delegation Handler**
Exact function name of the top-level event delegation handler. The exact `addEventListener` call that registers it. The pattern used to dispatch by `data-action` attribute (show the switch/if-else structure).

**Section 3 — Tab Navigation Logic**
The exact code that runs when a tab is activated: how screens are shown/hidden (e.g., toggling `hidden` attribute, class changes), how the active tab button is marked, and whether any render function is called on tab switch.

**Section 4 — App State Object**
The exact name of the top-level app state variable (e.g., `const state = {...}` or `let appState = {...}`). List every key at the top level of this object.

**Section 5 — DATA.symptoms Cluster Field**
Answer YES or NO: Does each `DATA.symptoms` entry contain a `clusters` property (an array of cluster code strings such as `['A', 'B']`)? Copy one complete example entry verbatim to confirm.

**Section 6 — selectedSymptomIds State**
Answer YES or NO: Does a `selectedSymptomIds` array (or equivalent persistent multi-select selection state) exist in the app state? If YES: state the exact property name and its location in the state object. If NO: state that it is absent.

**Section 7 — CSS Custom Properties**
List every CSS custom property defined in `:root {}`. Format: `--property-name: value`.

**Section 8 — Screen Section IDs**
List every `<section id="screen-*">` or `<div id="screen-*">` element ID that currently exists.

**Section 9 — Physician Referral Pattern**
Does the existing code contain any `isMedicalReferral`, `referral`, or equivalent physician-referral notice logic? If YES: copy the relevant code block verbatim. If NO: write "Not present."

**Section 10 — Function and Naming Patterns**
List the naming convention used for: JavaScript functions (camelCase, PascalCase, etc.), CSS class names (kebab-case, BEM, etc.), data attribute values (e.g., `data-action="navigate-tab"`). Provide one example of each.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] File `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` exists
- [ ] File contains all 10 numbered sections
- [ ] Section 5 contains an explicit YES or NO answer and a verbatim example entry
- [ ] Section 6 contains an explicit YES or NO answer
- [ ] Section 7 lists at least 5 CSS custom properties
- [ ] Section 8 lists at least 3 screen section IDs

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-01-document-codebase-patterns"` to `completedSteps`
2. Remove `"step-01-document-codebase-patterns"` from `pendingSteps`
3. Set `flags.codebasePatternsDocumented` to `true`
4. Append `"fdn-practice-plan/orchestration/context/codebase-patterns.md"` to `artifacts.filesWritten`
