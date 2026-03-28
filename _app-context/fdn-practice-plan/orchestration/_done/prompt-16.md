# Prompt 16: Verify Build Against All Success Criteria

## Prerequisites

state.json flags that must be true:
- `flags.badgeLogicAdded` must be `true` (set by step-15-add-badge-logic)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\refined-prompt.md` (success criteria section)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\ui-strings.md` (exact verbatim strings to verify — empty state message, plan header, mode explainers, element IDs)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\app-state-schema.md` (exact localStorage key and default state to verify)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\data-schema.md` (exact field names, enum values, and content authoring rules to verify against every DATA.dressPractices entry)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html` in full. Run every check below against the file. For each check that FAILS: fix the issue in `fdn-pwa/index.html` using the Edit tool before proceeding. Repeat until all checks pass.

**Technical compliance checks:**

- [ ] `DATA.dressPractices` exists as a property on the `DATA` object and contains at least 12 entries
- [ ] Every `DATA.dressPractices` entry has all 9 fields: `id`, `dresComponent`, `title`, `action`, `why`, `frequency`, `clusters`, `priority`, `module`
- [ ] `localStorage` key used in `getPlanState` and `setPlanState` is exactly `'fdn-plan-state'`
- [ ] `getPlanState` default return is exactly `{ completedIds: [], viewMode: 'focus', lastSymptomHash: '' }`
- [ ] Function `renderPlanScreen` exists
- [ ] Function `renderPracticeCard` exists
- [ ] Function `getActiveClusters` exists
- [ ] Function `getPracticesForClusters` exists
- [ ] Function `computeSymptomHash` exists
- [ ] `<section id="screen-plan"` exists in the HTML
- [ ] `<button ... data-tab="plan"` exists in the nav bar HTML
- [ ] `<span id="plan-badge"` exists
- [ ] CSS classes `.practice-card`, `.plan-mode-toggle`, `.alert-referral`, `.nav-badge` all exist in the stylesheet
- [ ] `@keyframes check-pop` exists in the stylesheet
- [ ] No new `addEventListener` calls were added outside the existing delegation handler
- [ ] No new CSS `--` custom properties were introduced (only existing tokens used)
- [ ] No new files were created (all code is in `index.html` only)

**Content integrity checks (read each DATA.dressPractices entry):**

- [ ] No `action` or `why` field contains a clinical abbreviation (HPA, GI, SIBO, dysbiosis, HPA-T) without an immediate plain-language definition in parentheses
- [ ] No `action` or `why` field contains a supplement dosage amount (mg, mcg, IU, etc.)
- [ ] No `action` or `why` field contains a brand name recommendation
- [ ] No `action` or `why` field uses "Studies show..." or third-person framing — all `why` fields use "This helps your body..." or equivalent first-person framing
- [ ] Every `module` field contains a number string (`"09"`, `"10"`, `"11"`, or `"12"`)

**UX completeness checks:**

- [ ] `renderPlanScreen` shows `#plan-empty-state` and returns early when `selectedSymptomIds.length === 0`
- [ ] `renderPlanScreen` removes `hidden` from `#plan-referral-notice` when active clusters include `'E'`
- [ ] `renderPlanScreen` shows `#plan-refresh-banner` when current symptom hash differs from stored `lastSymptomHash`
- [ ] `renderPlanScreen` caps Focus Mode at 7 practices via `getTopPractices(practices, 7)`
- [ ] `.practice-checkbox` button has `min-height: 44px` or equivalent 44px minimum touch target in CSS
- [ ] `.mode-btn` has `min-height: 44px` in CSS
- [ ] Empty state message is exactly: `"Select symptoms on the Search tab to see your personalized plan."`
- [ ] Plan header `<h2>` text is exactly: `"Your Practice Plan"`

**Structural integrity checks:**

- [ ] No existing `DATA.symptoms` entries were removed or modified
- [ ] No existing `DATA.variables` entries were removed or modified
- [ ] No existing render functions were renamed or removed
- [ ] No existing screen section IDs were renamed or removed
- [ ] The file is valid HTML (no unclosed tags, no broken JavaScript — use Grep to scan for obvious syntax markers)

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] Every check above shows PASS
- [ ] No check was skipped or left unresolved
- [ ] If any check required a fix: the fix was applied and the check was re-run

If any check fails and cannot be fixed in this session: document the remaining failures in a new file `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\verification-failures.md` and do NOT mark this step complete until all are resolved.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after ALL verification checks pass (zero failures):

1. Append `"step-16-verify-build"` to `completedSteps`
2. Remove `"step-16-verify-build"` from `pendingSteps`
3. Set `flags.buildVerified` to `true`
4. Append `"fdn-pwa/index.html"` to `artifacts.filesWritten`
