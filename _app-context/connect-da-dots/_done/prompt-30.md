# Prompt 30: Write JS — navigate() and goBack() Screen Navigation Functions

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `stateMachineCore`
- Files that MUST already exist: `fdn-pwa/index.html`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:NAVIGATE` in `fdn-pwa/index.html` with the screen navigation functions shown below.

The navigation system controls:
1. Tab-level navigation (Home / Search / Clusters tabs)
2. Screen rendering dispatching to the correct render function
3. Tab bar active state management
4. Scroll position save/restore for tab switching

All navigation uses CSS transitions via class toggling — no setTimeout, no JS animation.

Replace `// PLACEHOLDER:JS:NAVIGATE` with:

```javascript
// ─── Tab Navigation ───────────────────────────────────────────────────────
function navigateTab(tabName) {
  // Save current scroll position
  if (state.activeTab) {
    state.scrollPositions.set(state.activeTab, document.getElementById('screen-container').scrollTop);
  }

  // Close any open sheet when switching tabs
  if (state.sheet.isOpen) closeSheet();

  state.activeTab = tabName;
  state.screen = tabName;

  // Update tab bar aria-selected states
  document.querySelectorAll('.tab-item').forEach(btn => {
    const isActive = btn.dataset.tab === tabName;
    btn.setAttribute('aria-selected', String(isActive));
  });

  // Render the new screen
  renderScreen(tabName);

  // Restore scroll position for this tab
  requestAnimationFrame(() => {
    const savedScroll = state.scrollPositions.get(tabName) || 0;
    document.getElementById('screen-container').scrollTop = savedScroll;
  });
}

function renderScreen(screenName) {
  const container = document.getElementById('screen-container');
  clearEl(container);
  const screenDiv = el('div', { class: 'screen screen-enter' });
  if (screenName === 'home') renderHome(screenDiv);
  else if (screenName === 'search') renderSearch(screenDiv);
  else if (screenName === 'clusters') renderClusters(screenDiv);
  container.appendChild(screenDiv);
}

function renderClusters(container) {
  const header = el('div', { class: 'top-header' }, [
    el('div', { class: 'top-header-inner' }, [
      el('span', { class: 'header-title' }, ['Root Cause Clusters'])
    ])
  ]);
  container.appendChild(header);

  const list = el('div', { class: 'section-list' });

  Object.entries(DATA.clusters).forEach(([letter, cluster]) => {
    const row = el('button', {
      class: 'list-row',
      'data-action': 'open-cluster',
      'data-id': letter
    });

    const colorDot = el('span', {
      style: { width: '12px', height: '12px', borderRadius: '50%',
               backgroundColor: cluster.color, flexShrink: '0',
               display: 'inline-block', marginRight: '12px' }
    });

    const labelWrap = el('span', { class: 'list-row-label' });
    const clusterTag = el('span', {
      class: 'cluster-tag',
      style: { '--cluster-color': cluster.color }
    }, [txt(letter + ': ' + cluster.name)]);
    labelWrap.appendChild(clusterTag);

    if (cluster.priorityNote) {
      const note = el('span', { style: { display: 'block', fontSize: 'var(--text-xs)',
        color: 'var(--text-secondary)', marginTop: '4px' } },
        [txt(cluster.priorityNote.substring(0, 60) + (cluster.priorityNote.length > 60 ? '...' : ''))]);
      labelWrap.appendChild(note);
    }

    const chevron = el('span', { class: 'list-row-chevron' }, [txt('›')]);
    row.appendChild(colorDot);
    row.appendChild(labelWrap);
    row.appendChild(chevron);
    list.appendChild(row);
  });

  container.appendChild(list);
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:NAVIGATE`
- File now contains `function navigateTab(`
- File contains `function renderScreen(`
- File contains `function renderClusters(`
- `navigateTab` saves scroll position and restores it via `requestAnimationFrame`
- `renderScreen` calls `clearEl(container)` before rendering (no innerHTML)
- No `setTimeout` or `setInterval` used for any animation
- All DOM construction uses `el()` and `txt()` helpers

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-30"`
- `pendingSteps`: remove `"step-30"`
- `flags.navigateFunctions`: set to `true`
