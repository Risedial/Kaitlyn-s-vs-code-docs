# Prompt 33: Write JS — renderVariable(id, container) Function

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:RENDER-VARIABLE` in `fdn-pwa/index.html` with the `renderVariable()` function shown below.

**Critical requirements**:
1. Panel badge: colored by `variable.panelColor` with panel name as text
2. CROSS-PANEL AMPLIFIER badge: render if `variable.isCrossPanel === true`
3. Medical referral alert: render `.alert-banner--destructive` if `variable.isMedicalReferral === true`
4. Priority pathogen alert: render `.alert-banner--destructive` if `variable.isPriorityPathogen === true`
5. "When Elevated" and "When Low / Deficient" sections
6. Connected Variables: tappable `.var-pill` grid
7. Root Cause Clusters: tappable `.cluster-tag` grid

Replace `// PLACEHOLDER:JS:RENDER-VARIABLE` with:

```javascript
function renderVariable(id, container) {
  const variable = DATA.variables[id];
  if (!variable) return;

  // Back button
  const backRow = el('div', { class: 'sheet-header' }, [
    el('button', { class: 'header-back-btn', 'data-action': 'go-back',
      'aria-label': 'Go back' }, [txt('‹ Back')])
  ]);
  container.appendChild(backRow);

  // Variable name heading
  container.appendChild(el('h1', { class: 'detail-heading' }, [txt(variable.name)]));

  // Panel badge row
  const badgeRow = el('div', { class: 'pill-grid', style: { marginTop: '8px' } });
  const panelBadge = el('span', { class: 'panel-badge',
    style: { '--panel-color': variable.panelColor } }, [txt(variable.panel)]);
  badgeRow.appendChild(panelBadge);

  if (variable.isCrossPanel) {
    const crossBadge = el('span', { class: 'cross-panel-badge' },
      [txt('CROSS-PANEL AMPLIFIER')]);
    badgeRow.appendChild(crossBadge);
  }
  container.appendChild(badgeRow);

  // Description
  if (variable.description) {
    container.appendChild(el('p', { class: 'interpretation-text',
      style: { marginTop: '8px', color: 'var(--text-secondary)' } },
      [txt(variable.description)]));
  }

  // ── Medical Referral Alert ─────────────────────────────────────────────
  if (variable.isMedicalReferral) {
    const alert = el('div', { class: 'alert-banner alert-banner--destructive', role: 'alert' });
    const alertIcon = el('span', { class: 'alert-icon' }, [txt('⚕')]);
    const alertBody = el('div', { class: 'alert-body' });
    alertBody.appendChild(el('p', { class: 'alert-title' },
      [txt('MEDICAL REFERRAL REQUIRED')]));
    alertBody.appendChild(el('p', { class: 'alert-description' },
      [txt('Refer to physician before FDN interventions proceed. This finding indicates structural pathology requiring medical evaluation.')]) );
    alert.appendChild(alertIcon);
    alert.appendChild(alertBody);
    container.appendChild(alert);
  }

  // ── Priority Pathogen Alert ────────────────────────────────────────────
  if (variable.isPriorityPathogen) {
    const alert = el('div', { class: 'alert-banner alert-banner--destructive', role: 'alert' });
    const alertIcon = el('span', { class: 'alert-icon' }, [txt('⚠')]);
    const alertBody = el('div', { class: 'alert-body' });
    alertBody.appendChild(el('p', { class: 'alert-title' },
      [txt('Priority Pathogen — treat H. pylori before all other GI findings')]));
    alertBody.appendChild(el('p', { class: 'alert-description' },
      [txt('H. pylori disrupts gastric acid, collapses colonization resistance, and impairs interpretation of all other GI-MAP results. Clear H. pylori first.')]));
    alert.appendChild(alertIcon);
    alert.appendChild(alertBody);
    container.appendChild(alert);
  }

  // ── When Elevated ──────────────────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('When Elevated')]));
  container.appendChild(el('p', { class: 'interpretation-text' }, [txt(variable.elevated)]));

  // ── When Low / Deficient ───────────────────────────────────────────────
  container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('When Low / Deficient')]));
  container.appendChild(el('p', { class: 'interpretation-text' }, [txt(variable.low)]));

  // ── Connected Variables ────────────────────────────────────────────────
  if (variable.connections && variable.connections.length > 0) {
    container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('Connected Variables')]));
    const connGrid = el('div', { class: 'pill-grid' });
    variable.connections.forEach(connId => {
      const conn = DATA.variables[connId];
      if (!conn) return;
      const pill = el('button', {
        class: 'var-pill' + (conn.isCrossPanel ? ' var-pill--cross' : ''),
        style: { '--panel-color': conn.panelColor },
        'data-action': 'open-variable',
        'data-id': connId,
        'aria-label': conn.name
      }, [txt(conn.name)]);
      connGrid.appendChild(pill);
    });
    container.appendChild(connGrid);
  }

  // ── Root Cause Clusters ────────────────────────────────────────────────
  if (variable.clusters && variable.clusters.length > 0) {
    container.appendChild(el('h2', { class: 'detail-subheading' }, [txt('Root Cause Clusters')]));
    const clusterGrid = el('div', { class: 'pill-grid' });
    variable.clusters.forEach(letter => {
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
  }
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:RENDER-VARIABLE`
- File now contains `function renderVariable(`
- File contains `variable.isMedicalReferral` check with `alert-banner--destructive`
- File contains `variable.isPriorityPathogen` check with `alert-banner--destructive`
- File contains `variable.isCrossPanel` check rendering `cross-panel-badge`
- Medical referral alert text includes `'MEDICAL REFERRAL REQUIRED'`
- Priority pathogen alert text includes `'Priority Pathogen'`
- Connected variables grid uses `data-action: 'open-variable'`
- Cluster tags grid uses `data-action: 'open-cluster'`
- No innerHTML with dynamic strings

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-33"`
- `pendingSteps`: remove `"step-33"`
- `flags.renderVariable`: set to `true`
