# Prompt 34: Write JS — renderCluster(id, container) Function

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:RENDER-CLUSTER` in `fdn-pwa/index.html` with the `renderCluster()` function shown below.

**Critical requirements**:
1. If `cluster.letter === 'E'` (Cluster E): render MEDICAL REFERRAL REQUIRED block at the TOP before anything else (after back button)
2. If `cluster.letter === 'A'` (Cluster A): render priority block "Address before all others — GI dysfunction drives all downstream clusters."
3. Variables in cluster: tappable `.var-pill` grid
4. Symptoms associated: reverse-mapped from `maps.symptomsByCluster[letter]` — render as tappable list rows
5. All DOM construction via `el()` and `txt()` — no innerHTML with dynamic strings

Replace `// PLACEHOLDER:JS:RENDER-CLUSTER` with:

```javascript
function renderCluster(id, container) {
  const cluster = DATA.clusters[id];
  if (!cluster) return;

  // Back button
  const backRow = el('div', { class: 'sheet-header' }, [
    el('button', { class: 'header-back-btn', 'data-action': 'go-back',
      'aria-label': 'Go back' }, [txt('‹ Back')])
  ]);
  container.appendChild(backRow);

  // Cluster heading colored by cluster color
  const heading = el('h1', { class: 'detail-heading',
    style: { color: cluster.color } }, [txt(cluster.fullName)]);
  container.appendChild(heading);

  // ── Cluster E: Medical Referral Block ──────────────────────────────────
  if (id === 'E') {
    const referral = el('div', { class: 'alert-banner alert-banner--destructive', role: 'alert' });
    const icon = el('span', { class: 'alert-icon' }, [txt('⚕')]);
    const body = el('div', { class: 'alert-body' });
    body.appendChild(el('p', { class: 'alert-title' },
      [txt('MEDICAL REFERRAL REQUIRED')]));
    body.appendChild(el('p', { class: 'alert-description' },
      [txt('Elevated Calprotectin/Lactoferrin or Occult Blood >10 µg/g indicates structural GI pathology. Refer to physician before any FDN interventions. This is a referral trigger, not an FDN intervention trigger.')]));
    referral.appendChild(icon);
    referral.appendChild(body);
    container.appendChild(referral);
  }

  // ── Cluster A: Priority Block ──────────────────────────────────────────
  if (id === 'A') {
    const priority = el('div', { class: 'priority-block', role: 'note' });
    priority.appendChild(el('p', { style: { fontWeight: 'var(--weight-semibold)' } },
      [txt('⬆ Primary Driver — Address Before All Other Clusters')]));
    priority.appendChild(el('p', { style: { marginTop: '4px', fontSize: 'var(--text-sm)' } },
      [txt('GI dysfunction is the upstream driver of systemic dysfunction in the FDN model. H. pylori must be treated first if positive.')]));
    container.appendChild(priority);
  }

  // ── Mechanism Description ──────────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('Mechanism')]));
  container.appendChild(el('p', { class: 'interpretation-text' }, [txt(cluster.mechanism)]));

  // ── Variables in This Cluster ──────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' },
    [txt('Variables in This Cluster')]));
  const varGrid = el('div', { class: 'pill-grid' });
  (cluster.variables || []).forEach(varId => {
    const variable = DATA.variables[varId];
    if (!variable) return;
    const pill = el('button', {
      class: 'var-pill' + (variable.isCrossPanel ? ' var-pill--cross' : ''),
      style: { '--panel-color': variable.panelColor },
      'data-action': 'open-variable',
      'data-id': varId,
      'aria-label': variable.name
    }, [txt(variable.name)]);
    varGrid.appendChild(pill);
  });
  container.appendChild(varGrid);

  // ── Associated Symptoms (reverse map) ─────────────────────────────────
  const associatedIds = maps.symptomsByCluster[id] || [];
  if (associatedIds.length > 0) {
    container.appendChild(el('h2', { class: 'detail-subheading' },
      [txt('Symptoms Associated with This Cluster')]));
    const symptomList = el('div', { class: 'section-list' });
    associatedIds.forEach(symId => {
      const sym = DATA.symptoms[symId];
      if (!sym) return;
      const row = el('button', {
        class: 'list-row',
        'data-action': 'open-symptom',
        'data-id': symId
      });
      row.appendChild(el('span', { class: 'list-row-label' }, [txt(sym.label)]));
      row.appendChild(el('span', { class: 'list-row-chevron' }, [txt('›')]));
      symptomList.appendChild(row);
    });
    container.appendChild(symptomList);
  }
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:RENDER-CLUSTER`
- File now contains `function renderCluster(`
- File contains `if (id === 'E') {` rendering the medical referral block
- File contains `if (id === 'A') {` rendering the priority block
- Medical referral block uses class `alert-banner alert-banner--destructive`
- Priority block uses class `priority-block`
- Cluster heading uses `style: { color: cluster.color }` — colored by cluster color
- Associated symptoms uses `maps.symptomsByCluster[id]` (reverse map from step-29)
- Symptom rows have `data-action: 'open-symptom'`
- Variable pills have `data-action: 'open-variable'`

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-34"`
- `pendingSteps`: remove `"step-34"`
- `flags.renderCluster`: set to `true`
