# Prompt 32: Write JS — renderSymptom(id, container) Function

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `navigateFunctions`
- Files that MUST already exist: `fdn-pwa/index.html`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:RENDER-SYMPTOM` in `fdn-pwa/index.html` with the `renderSymptom()` function shown below.

**Critical requirements**:
1. **H. pylori check**: If `symptom.variables.includes('hpylori')`, render `.alert-banner--destructive` BEFORE the variables section with the text "⚠ Treat H. pylori before addressing other findings."
2. Variable pills must use the correct panel color via `--panel-color` CSS custom property. Cross-panel variables must use `.var-pill--cross` class.
3. All DOM construction via `el()` and `txt()` — NEVER innerHTML with dynamic strings.
4. Back button at top uses `data-action="go-back"` to trigger `popSheet()`.

Replace `// PLACEHOLDER:JS:RENDER-SYMPTOM` with:

```javascript
function renderSymptom(id, container) {
  const symptom = DATA.symptoms[id];
  if (!symptom) return;

  // Back button row
  const backRow = el('div', { class: 'sheet-header' }, [
    el('button', { class: 'header-back-btn', 'data-action': 'go-back',
      'aria-label': 'Go back' }, [txt('‹ Back')])
  ]);
  container.appendChild(backRow);

  // Symptom heading
  container.appendChild(el('h1', { class: 'detail-heading' }, [txt(symptom.label)]));

  // Category label
  container.appendChild(el('p', { class: 'interpretation-text',
    style: { color: 'var(--text-tertiary)', fontSize: 'var(--text-sm)', marginTop: '4px' } },
    [txt(symptom.category)]));

  // ── H. PYLORI ALERT (MUST appear before variable pills) ────────────────
  if (symptom.variables && symptom.variables.includes('hpylori')) {
    const alert = el('div', { class: 'alert-banner alert-banner--destructive', role: 'alert' });
    const alertIcon = el('span', { class: 'alert-icon' }, [txt('⚠')]);
    const alertBody = el('div', { class: 'alert-body' });
    const alertTitle = el('p', { class: 'alert-title' },
      [txt('Treat H. pylori before addressing other findings')]);
    const alertDesc = el('p', { class: 'alert-description' },
      [txt('H. pylori must be cleared first. All other GI-MAP findings are secondary until H. pylori is negative.')]);
    alertBody.appendChild(alertTitle);
    alertBody.appendChild(alertDesc);
    alert.appendChild(alertIcon);
    alert.appendChild(alertBody);
    container.appendChild(alert);
  }

  // ── Variables Section ──────────────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('Variables Involved')]));
  const pillGrid = el('div', { class: 'pill-grid' });
  (symptom.variables || []).forEach(varId => {
    const variable = DATA.variables[varId];
    if (!variable) return;
    const isCross = variable.isCrossPanel;
    const pill = el('button', {
      class: 'var-pill' + (isCross ? ' var-pill--cross' : ''),
      style: { '--panel-color': variable.panelColor },
      'data-action': 'open-variable',
      'data-id': varId,
      'aria-label': variable.name
    }, [txt(variable.name)]);
    pillGrid.appendChild(pill);
  });
  container.appendChild(pillGrid);

  // ── Cluster Tags ───────────────────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('Root Cause Clusters')]));
  const clusterGrid = el('div', { class: 'pill-grid' });
  (symptom.clusters || []).forEach(letter => {
    const cluster = DATA.clusters[letter];
    if (!cluster) return;
    const tag = el('button', {
      class: 'cluster-tag',
      style: { '--cluster-color': cluster.color },
      'data-action': 'open-cluster',
      'data-id': letter,
      'aria-label': cluster.fullName
    }, [txt(letter + ': ' + cluster.name)]);
    clusterGrid.appendChild(tag);
  });
  container.appendChild(clusterGrid);

  // ── Interpretation ─────────────────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('What This Means')]));
  container.appendChild(el('p', { class: 'interpretation-text' },
    [txt(symptom.interpretation)]));

  // ── Mechanism Tree ─────────────────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('Mechanism Hierarchy')]));
  container.appendChild(el('pre', { class: 'mechanism-tree' },
    [txt(symptom.mechanismTree)]));
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:RENDER-SYMPTOM`
- File now contains `function renderSymptom(`
- File contains the H. pylori check: `symptom.variables.includes('hpylori')`
- H. pylori alert uses class `alert-banner alert-banner--destructive`
- The alert is appended BEFORE the pill grid (before `Variables Involved` section)
- File contains `.var-pill--cross` class assignment for cross-panel variables
- File contains `data-action`: `'open-variable'` on pill buttons and `'open-cluster'` on cluster tags
- File contains `data-action`: `'go-back'` on back button
- No innerHTML with dynamic strings — all uses `el()` and `txt()`

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-32"`
- `pendingSteps`: remove `"step-32"`
- `flags.renderSymptom`: set to `true`
