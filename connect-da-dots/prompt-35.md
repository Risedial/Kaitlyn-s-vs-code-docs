# Prompt 35: Write JS — renderSearch() Function (Full-Screen Search Screen)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:RENDER-SEARCH` in `fdn-pwa/index.html` with the `renderSearch()` function shown below.

**Behavioral requirements**:
- Full-screen search input, auto-focused when the Search tab is activated
- Real-time search at ≥2 characters across both symptom labels AND variable names
- Results grouped under "Symptoms" and "Variables" headings
- Empty state (< 2 chars): "Start typing to search symptoms and variables"
- No-results state: `No matches for '[query]'`
- Each symptom result opens the symptom detail sheet; each variable result opens the variable detail sheet
- All DOM construction via `el()` and `txt()` — no innerHTML with dynamic strings

Replace `// PLACEHOLDER:JS:RENDER-SEARCH` with:

```javascript
function renderSearch(container) {
  // Header
  const header = el('div', { class: 'top-header' }, [
    el('div', { class: 'top-header-inner' }, [
      el('span', { class: 'header-title' }, ['Search'])
    ])
  ]);
  container.appendChild(header);

  // Search bar (full-width, auto-focus)
  const searchWrap = el('div', { class: 'search-container' });
  const searchBar = el('div', { class: 'search-bar' });
  const searchIcon = el('span', { class: 'search-icon' }, [txt('⌕')]);
  const searchInput = el('input', {
    type: 'search', class: 'search-input', id: 'search-screen-input',
    placeholder: 'Search symptoms and variables…', 'aria-label': 'Search'
  });

  const resultsContainer = el('div', { id: 'search-results' });
  renderSearchResults(resultsContainer, '');

  searchInput.addEventListener('input', () => {
    renderSearchResults(resultsContainer, searchInput.value);
  });

  searchBar.appendChild(searchIcon);
  searchBar.appendChild(searchInput);
  searchWrap.appendChild(searchBar);
  container.appendChild(searchWrap);
  container.appendChild(resultsContainer);

  // Auto-focus search input after render
  requestAnimationFrame(() => {
    const input = document.getElementById('search-screen-input');
    if (input) input.focus();
  });
}

function renderSearchResults(container, query) {
  clearEl(container);
  const q = query.trim().toLowerCase();

  if (q.length < 2) {
    container.appendChild(el('div', { class: 'empty-state' }, [
      el('p', {}, [txt('Start typing to search symptoms and variables')])
    ]));
    return;
  }

  // Search symptoms
  const matchedSymptoms = Object.entries(DATA.symptoms).filter(([, sym]) =>
    sym.label.toLowerCase().includes(q)
  );

  // Search variables
  const matchedVariables = Object.entries(DATA.variables).filter(([, v]) =>
    v.name.toLowerCase().includes(q)
  );

  if (matchedSymptoms.length === 0 && matchedVariables.length === 0) {
    const noMatch = el('div', { class: 'empty-state' });
    const msg = el('p', {});
    msg.appendChild(txt('No matches for \u201c'));
    msg.appendChild(txt(query.trim()));
    msg.appendChild(txt('\u201d'));
    noMatch.appendChild(msg);
    container.appendChild(noMatch);
    return;
  }

  // Render symptom results
  if (matchedSymptoms.length > 0) {
    container.appendChild(el('p', { class: 'result-group-heading' },
      [txt('Symptoms (' + matchedSymptoms.length + ')')]));
    matchedSymptoms.forEach(([id, sym]) => {
      const row = el('button', {
        class: 'list-row',
        'data-action': 'open-symptom',
        'data-id': id
      });
      const labelWrap = el('span', { class: 'list-row-label' });
      labelWrap.appendChild(el('span', {}, [txt(sym.label)]));
      labelWrap.appendChild(el('span', {
        style: { display: 'block', fontSize: 'var(--text-xs)',
          color: 'var(--text-tertiary)', marginTop: '2px' } },
        [txt(sym.category)]));
      row.appendChild(labelWrap);
      row.appendChild(el('span', { class: 'list-row-chevron' }, [txt('›')]));
      container.appendChild(row);
    });
  }

  // Render variable results
  if (matchedVariables.length > 0) {
    container.appendChild(el('p', { class: 'result-group-heading' },
      [txt('Variables (' + matchedVariables.length + ')')]));
    matchedVariables.forEach(([id, variable]) => {
      const row = el('button', {
        class: 'list-row',
        'data-action': 'open-variable',
        'data-id': id
      });
      const labelWrap = el('span', { class: 'list-row-label' });
      labelWrap.appendChild(el('span', {}, [txt(variable.name)]));
      const panelSpan = el('span', {
        class: 'var-pill',
        style: { '--panel-color': variable.panelColor,
          minWidth: 'unset', minHeight: 'unset', padding: '2px 8px',
          fontSize: 'var(--text-xs)', marginTop: '4px', cursor: 'default',
          display: 'inline-flex' } },
        [txt(variable.panel)]);
      labelWrap.appendChild(panelSpan);
      row.appendChild(labelWrap);
      row.appendChild(el('span', { class: 'list-row-chevron' }, [txt('›')]));
      container.appendChild(row);
    });
  }
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:RENDER-SEARCH`
- File now contains `function renderSearch(`
- File contains `function renderSearchResults(`
- Search activates at ≥2 characters (`q.length < 2` returns empty state)
- Empty state text: `'Start typing to search symptoms and variables'`
- No-results uses `'No matches for'` with the query (no innerHTML — uses txt() nodes)
- Symptom results have `data-action: 'open-symptom'`
- Variable results have `data-action: 'open-variable'`
- Auto-focus uses `requestAnimationFrame` — no setTimeout
- No innerHTML with dynamic strings

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-35"`
- `pendingSteps`: remove `"step-35"`
- `flags.renderSearch`: set to `true`
