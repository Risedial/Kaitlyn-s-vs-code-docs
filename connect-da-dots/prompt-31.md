# Prompt 31: Write JS — renderHome() Function (Accordion Symptom List with Search)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:RENDER-HOME` in `fdn-pwa/index.html` with the `renderHome()` function shown below.

**Behavioral requirements**:
- Title: "What are you experiencing?"
- Frosted glass sticky header with search bar below it
- 14 accordion category sections in this exact order: Energy & Fatigue | Sleep | Mood & Emotions | Digestion | Food Reactions | Skin | Immune System | Hormonal (Female) | Hormonal (Male & Shared) | Cardiovascular & Circulatory | Pain & Inflammation | Respiratory | Cognitive & Neurological | Stress & Nervous System
- Category sections collapsed by default; state.expandedCategories tracks open sections
- Real-time search filter at ≥2 characters: matches symptom labels, shows match count badge in accordion header
- Each symptom is a tappable list row with data-action="open-symptom" and data-id set to the symptom ID
- All DOM construction via `el()` and `txt()` — never innerHTML with dynamic strings

Replace `// PLACEHOLDER:JS:RENDER-HOME` with:

```javascript
// ─── Category ordering ────────────────────────────────────────────────────
const CATEGORY_ORDER = [
  'Energy & Fatigue', 'Sleep', 'Mood & Emotions', 'Digestion',
  'Food Reactions', 'Skin', 'Immune System', 'Hormonal (Female)',
  'Hormonal (Male & Shared)', 'Cardiovascular & Circulatory',
  'Pain & Inflammation', 'Respiratory', 'Cognitive & Neurological',
  'Stress & Nervous System'
];

function renderHome(container) {
  // Header
  const header = el('div', { class: 'top-header' }, [
    el('div', { class: 'top-header-inner' }, [
      el('span', { class: 'header-title' }, ['What are you experiencing?'])
    ])
  ]);
  container.appendChild(header);

  // Search bar
  const searchWrap = el('div', { class: 'search-container' });
  const searchBar = el('div', { class: 'search-bar' });
  const searchIcon = el('span', { class: 'search-icon' }, [txt('⌕')]);
  const searchInput = el('input', {
    type: 'text', class: 'search-input', id: 'home-search-input',
    placeholder: 'Search symptoms…', 'aria-label': 'Search symptoms'
  });
  searchInput.addEventListener('input', () => {
    state.searchQuery = searchInput.value;
    refreshAccordions(accordionContainer, searchInput.value.trim());
  });
  searchBar.appendChild(searchIcon);
  searchBar.appendChild(searchInput);
  searchWrap.appendChild(searchBar);
  container.appendChild(searchWrap);

  // Accordion container
  const accordionContainer = el('div', { class: 'section-list', id: 'accordion-container' });
  buildAccordions(accordionContainer, '');
  container.appendChild(accordionContainer);
}

function getSymptomsByCategory() {
  const byCat = {};
  CATEGORY_ORDER.forEach(cat => { byCat[cat] = []; });
  Object.entries(DATA.symptoms).forEach(([id, sym]) => {
    if (byCat[sym.category]) byCat[sym.category].push({ id, ...sym });
  });
  return byCat;
}

function buildAccordions(container, query) {
  clearEl(container);
  const q = query.trim().toLowerCase();
  const isFiltering = q.length >= 2;
  const byCat = getSymptomsByCategory();

  CATEGORY_ORDER.forEach(category => {
    const allSymptoms = byCat[category] || [];
    const symptoms = isFiltering
      ? allSymptoms.filter(s => s.label.toLowerCase().includes(q))
      : allSymptoms;

    if (isFiltering && symptoms.length === 0) return;

    const isExpanded = isFiltering || state.expandedCategories.has(category);
    const section = el('div', { class: 'accordion-section' });

    // Header button
    const headerBtn = el('button', {
      class: 'accordion-header',
      'aria-expanded': String(isExpanded),
      'data-category': category
    });

    const titleSpan = el('span', { class: 'accordion-title' }, [txt(category)]);
    const rightWrap = el('span', { class: 'accordion-right' });

    if (isFiltering && symptoms.length > 0) {
      const badge = el('span', { class: 'accordion-badge' }, [txt(String(symptoms.length))]);
      rightWrap.appendChild(badge);
    }

    const chevron = el('span', { class: 'accordion-chevron' }, [txt('›')]);
    rightWrap.appendChild(chevron);

    headerBtn.appendChild(titleSpan);
    headerBtn.appendChild(rightWrap);
    headerBtn.addEventListener('click', () => toggleAccordion(category, headerBtn, body));
    section.appendChild(headerBtn);

    // Body
    const body = el('div', { class: 'accordion-body' + (isExpanded ? ' is-open' : '') });
    symptoms.forEach(sym => {
      const row = el('button', {
        class: 'list-row',
        'data-action': 'open-symptom',
        'data-id': sym.id
      });
      const label = el('span', { class: 'list-row-label' }, [txt(sym.label)]);
      const chevronRight = el('span', { class: 'list-row-chevron' }, [txt('›')]);
      row.appendChild(label);
      row.appendChild(chevronRight);
      body.appendChild(row);
    });
    section.appendChild(body);
    container.appendChild(section);
  });
}

function refreshAccordions(container, query) {
  buildAccordions(container, query);
}

function toggleAccordion(category, btn, body) {
  const isNowOpen = !body.classList.contains('is-open');
  body.classList.toggle('is-open', isNowOpen);
  btn.setAttribute('aria-expanded', String(isNowOpen));
  if (isNowOpen) state.expandedCategories.add(category);
  else state.expandedCategories.delete(category);
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:RENDER-HOME`
- File now contains `function renderHome(`
- File contains `const CATEGORY_ORDER = [`  with all 14 category names
- File contains `function buildAccordions(`
- File contains `function toggleAccordion(`
- Search input uses `addEventListener('input', ...)` — not `oninput`
- All DOM construction uses `el()` and `txt()` — no innerHTML with dynamic strings
- `data-action="open-symptom"` is set on symptom rows with `data-id` attribute

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-31"`
- `pendingSteps`: remove `"step-31"`
- `flags.renderHome`: set to `true`
