# Prompt 12: Add #screen-plan Screen Section HTML to index.html

## Prerequisites

state.json flags that must be true:
- `flags.navTabAdded` must be `true` (set by step-11-add-nav-tab-html)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\ui-strings.md` (exact verbatim text for all screen HTML strings — screen section ID, empty state message, banner text, plan header, element IDs)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Locate the last existing `<section id="screen-*">` element (from codebase-patterns.md Section 8). Add the following HTML as a new screen section, immediately after the last existing screen section. Use the Edit tool.

```html
<section id="screen-plan" class="screen" aria-label="My Plan" hidden>

  <div id="plan-referral-notice" class="alert-referral" hidden>
    <strong>Talk to your doctor first.</strong> One or more of your symptoms may indicate a condition that needs medical evaluation. Please consult a licensed physician before starting any new health practice. The information in this plan is for general wellness support only and is not medical advice.
  </div>

  <div id="plan-refresh-banner" class="banner-notice" hidden>
    <span>Your symptoms have changed. Refresh your plan?</span>
    <button data-action="refresh-plan">Refresh</button>
  </div>

  <header class="plan-header">
    <h2>Your Practice Plan</h2>
    <p id="plan-subtitle" class="text-secondary">Based on 0 symptoms you selected</p>
  </header>

  <div class="plan-mode-toggle" role="tablist" aria-label="Plan view mode">
    <button
      class="mode-btn active"
      data-mode="focus"
      role="tab"
      aria-selected="true"
      data-action="switch-plan-mode"
    >Focus Mode</button>
    <button
      class="mode-btn"
      data-mode="full"
      role="tab"
      aria-selected="false"
      data-action="switch-plan-mode"
    >Full Plan</button>
  </div>

  <p id="plan-mode-explainer" class="mode-explainer text-secondary">Focus Mode shows the practices with the broadest impact on your symptoms. Start here.</p>

  <div id="plan-practice-list" class="practice-list"></div>

  <div id="plan-empty-state" class="empty-state" hidden>
    Select symptoms on the Search tab to see your personalized plan.
  </div>

</section>
```

**Exact locked values** (copy verbatim — do not paraphrase):
- Screen section ID: `screen-plan`
- Empty state message: `"Select symptoms on the Search tab to see your personalized plan."`
- Symptom-change banner text: `"Your symptoms have changed. Refresh your plan?"`
- Plan header: `"Your Practice Plan"`
- Sub-label initial text: `"Based on 0 symptoms you selected"`
- Mode explainer initial text: `"Focus Mode shows the practices with the broadest impact on your symptoms. Start here."`

Do NOT modify any existing screen section. Do NOT add any JavaScript in this step. Use the Edit tool.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `fdn-pwa/index.html` contains `<section id="screen-plan"`
- [ ] Section contains `id="plan-referral-notice"` with `hidden` attribute
- [ ] Section contains `id="plan-refresh-banner"` with `hidden` attribute and a child button with `data-action="refresh-plan"`
- [ ] Section contains `<h2>Your Practice Plan</h2>` (exact text)
- [ ] Section contains `id="plan-subtitle"` with initial text `"Based on 0 symptoms you selected"`
- [ ] Section contains `id="plan-practice-list"`
- [ ] Section contains `id="plan-empty-state"` with `hidden` attribute and the exact empty state message
- [ ] Section contains two `.mode-btn` buttons with `data-action="switch-plan-mode"`
- [ ] No existing screen sections were modified

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-12-add-screen-section-html"` to `completedSteps`
2. Remove `"step-12-add-screen-section-html"` from `pendingSteps`
3. Set `flags.screenSectionAdded` to `true`
