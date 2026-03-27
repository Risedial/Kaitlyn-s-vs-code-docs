# Prompt 10: Add renderPlanScreen() Function to index.html

## Prerequisites

state.json flags that must be true:
- `flags.utilityFunctionsAdded` must be `true` (set by step-08-add-utility-functions)
- `flags.stateFunctionsAdded` must be `true` (set by step-09-add-state-functions)

Files that must exist:
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md` (created by Prompt 01)

Context files to read before beginning (read these BEFORE executing Task):
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\context\codebase-patterns.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\nnnn.md`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json`
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\ui-strings.md` (exact verbatim text for all user-visible strings in renderPlanScreen — mode explainers, labels, section headers)
- `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\context\app-state-schema.md` (exact localStorage key, default state, viewMode values, Focus Mode cap of 7)

---

## Hard Constraints

1. 32,000 token output limit — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. No truncation — When writing data entries, write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. State sync required — Read the state file at the start of every session. Complete the single assigned task. Update the state file to mark that step complete before exiting.
4. No external dependencies — No CDN, no npm, no external URLs in any generated file.
5. File writes only via Write tool — Never use bash heredoc or shell redirection to write application files.

---

## Task

Read `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa\index.html`. Using codebase-patterns.md Section 1 and Section 10, identify where render functions are defined. Add `renderPlanScreen()` immediately after the last existing render function, using the Edit tool.

The function must implement this exact logic:

```js
function renderPlanScreen() {
  // Read state
  const selectedSymptomIds = /* read from app state — use exact property name from codebase-patterns.md Section 6 */;
  const planState = getPlanState();

  // Empty state
  const emptyState = document.getElementById('plan-empty-state');
  const practiceList = document.getElementById('plan-practice-list');
  const referralNotice = document.getElementById('plan-referral-notice');
  const refreshBanner = document.getElementById('plan-refresh-banner');
  const subtitle = document.getElementById('plan-subtitle');
  const modeExplainer = document.getElementById('plan-mode-explainer');

  if (!selectedSymptomIds || selectedSymptomIds.length === 0) {
    if (emptyState) emptyState.hidden = false;
    if (practiceList) practiceList.innerHTML = '';
    if (referralNotice) referralNotice.hidden = true;
    if (refreshBanner) refreshBanner.hidden = true;
    return;
  }

  if (emptyState) emptyState.hidden = true;

  // Compute clusters and practices
  const activeClusters = getActiveClusters(selectedSymptomIds);
  const practices = getPracticesForClusters(activeClusters, selectedSymptomIds);

  // Cluster E referral notice
  if (referralNotice) {
    referralNotice.hidden = !activeClusters.includes('E');
  }

  // Symptom-change banner
  const currentHash = computeSymptomHash(selectedSymptomIds);
  if (refreshBanner) {
    refreshBanner.hidden = (currentHash === planState.lastSymptomHash);
  }

  // Subtitle
  if (subtitle) {
    subtitle.textContent = 'Based on ' + selectedSymptomIds.length + ' symptoms you selected';
  }

  // Mode explainer
  const explainers = {
    focus: 'Focus Mode shows the practices with the broadest impact on your symptoms. Start here.',
    full: 'Full Plan shows every practice recommended for your symptoms, grouped by focus area.'
  };
  if (modeExplainer) {
    modeExplainer.textContent = explainers[planState.viewMode] || explainers.focus;
  }

  // Render practice list
  if (practiceList) {
    if (planState.viewMode === 'focus') {
      const top = getTopPractices(practices, 7);
      practiceList.innerHTML = top.map(p => renderPracticeCard(p, planState.completedIds)).join('');
    } else {
      const groups = groupByDressComponent(practices);
      const displayNames = { diet: 'Diet', rest: 'Rest', exercise: 'Exercise', stress: 'Stress Reduction', supplement: 'Supplementation' };
      let html = '';
      groups.forEach((items, key) => {
        if (items.length === 0) return;
        html += '<details class="dress-section" open>';
        html += '<summary class="dress-section-header">' + displayNames[key] + ' \u2014 ' + items.length + ' practice' + (items.length !== 1 ? 's' : '') + '</summary>';
        html += '<div class="dress-section-body">';
        html += items.map(p => renderPracticeCard(p, planState.completedIds)).join('');
        html += '</div></details>';
      });
      practiceList.innerHTML = html;
    }
  }

  // Mode toggle active state
  document.querySelectorAll('.mode-btn').forEach(btn => {
    const isActive = btn.dataset.mode === planState.viewMode;
    btn.classList.toggle('active', isActive);
    btn.setAttribute('aria-selected', String(isActive));
  });
}

function renderPracticeCard(practice, completedIds) {
  const isComplete = completedIds.includes(practice.id);
  const freqLabel = { daily: 'Daily', weekly: 'Weekly', 'as-needed': 'As needed' }[practice.frequency] || practice.frequency;
  const clusterClass = 'cluster-' + practice.clusters[0];
  return '<div class="practice-card' + (isComplete ? ' practice-complete' : '') + '" data-practice-id="' + practice.id + '" data-expanded="false">' +
    '<div class="practice-card-header" data-action="toggle-practice-expand">' +
    '<span class="cluster-dot ' + clusterClass + '" aria-hidden="true"></span>' +
    '<span class="practice-title">' + practice.title + '</span>' +
    '<span class="frequency-pill frequency-' + practice.frequency + '">' + freqLabel + '</span>' +
    '<button class="practice-checkbox" data-action="toggle-practice-complete" data-practice-id="' + practice.id + '" aria-label="Mark ' + practice.title + ' as complete" aria-pressed="' + isComplete + '">' +
    '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8l3.5 3.5L13 4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
    '</button></div>' +
    '<div class="practice-card-body" hidden>' +
    '<p class="practice-what-label">What to do</p>' +
    '<p class="practice-action">' + practice.action + '</p>' +
    '<p class="practice-why-label">Why this helps</p>' +
    '<p class="practice-why">' + practice.why + '</p>' +
    '</div></div>';
}
```

**CRITICAL:** Replace the comment `/* read from app state — use exact property name from codebase-patterns.md Section 6 */` with the actual expression to read `selectedSymptomIds` from the app state object. Use the exact property name and state object name documented in codebase-patterns.md Sections 4 and 6.

Do NOT add a new `addEventListener`. Do NOT modify existing render functions. Use the Edit tool.

---

## Verification

Before updating state.json, confirm ALL of the following:

- [ ] `fdn-pwa/index.html` contains function `renderPlanScreen`
- [ ] `fdn-pwa/index.html` contains function `renderPracticeCard`
- [ ] `renderPlanScreen` references `getPlanState`, `getActiveClusters`, `getPracticesForClusters`, `computeSymptomHash`, `getTopPractices`, `groupByDressComponent`, `renderPracticeCard`
- [ ] `renderPlanScreen` handles the empty state (zero selectedSymptomIds) by showing `#plan-empty-state` and returning early
- [ ] `renderPlanScreen` shows `#plan-referral-notice` when Cluster E is active
- [ ] The focus mode explainer string is exactly: `"Focus Mode shows the practices with the broadest impact on your symptoms. Start here."`
- [ ] The full plan explainer string is exactly: `"Full Plan shows every practice recommended for your symptoms, grouped by focus area."`
- [ ] No existing functions were modified

If any check fails: fix the issue, then re-run ALL verification checks before proceeding.

---

## State Update

Perform these exact mutations to `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-practice-plan\orchestration\state.json` after all Verification checks pass:

1. Append `"step-10-add-render-function"` to `completedSteps`
2. Remove `"step-10-add-render-function"` from `pendingSteps`
3. Set `flags.renderFunctionAdded` to `true`
