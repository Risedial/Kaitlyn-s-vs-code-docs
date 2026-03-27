# Prompt 29: Write JS — State Machine Core (state object definition)

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `dataIntegrityVerified`
- Files that MUST already exist: `fdn-pwa/index.html`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:STATE-MACHINE` in `fdn-pwa/index.html` with the application state object and computed reverse maps shown below.

The state machine defines all mutable application state. The reverse map (`symptomsByCluster`) is computed once at initialization from DATA and used by renderCluster() to list associated symptoms without hardcoding.

Replace `// PLACEHOLDER:JS:STATE-MACHINE` with:

```javascript
// ─── Application State ────────────────────────────────────────────────────
const state = {
  screen: 'home',           // 'home' | 'search' | 'clusters'
  activeTab: 'home',        // tracks which tab is selected
  sheet: {
    isOpen: false,
    type: null,             // 'symptom' | 'variable' | 'cluster'
    id: null,               // the DATA key for the current detail view
    stack: [],              // [{type, id, scrollY}] for back navigation within sheet
  },
  searchQuery: '',
  expandedCategories: new Set(),
  scrollPositions: new Map(), // key → scrollY for position restoration
};

// ─── Computed Reverse Maps (built once from DATA at init) ─────────────────
const maps = {
  symptomsByCluster: {},    // 'A' → ['symptom-id-1', ...]
  symptomsByVariable: {},   // 'variable-id' → ['symptom-id-1', ...]
};

function buildMaps() {
  // Build symptomsByCluster
  Object.keys(DATA.clusters).forEach(letter => {
    maps.symptomsByCluster[letter] = [];
  });
  Object.entries(DATA.symptoms).forEach(([id, symptom]) => {
    (symptom.clusters || []).forEach(letter => {
      if (maps.symptomsByCluster[letter]) {
        maps.symptomsByCluster[letter].push(id);
      }
    });
  });

  // Build symptomsByVariable
  Object.entries(DATA.symptoms).forEach(([id, symptom]) => {
    (symptom.variables || []).forEach(varId => {
      if (!maps.symptomsByVariable[varId]) {
        maps.symptomsByVariable[varId] = [];
      }
      maps.symptomsByVariable[varId].push(id);
    });
  });
}

// ─── DOM Helpers ──────────────────────────────────────────────────────────
function el(tag, attrs = {}, children = []) {
  const element = document.createElement(tag);
  Object.entries(attrs).forEach(([k, v]) => {
    if (k === 'class') element.className = v;
    else if (k === 'style') Object.assign(element.style, v);
    else if (k.startsWith('data-')) element.dataset[k.slice(5)] = v;
    else if (k === 'aria-selected' || k === 'aria-expanded' || k === 'aria-label' || k === 'aria-hidden' || k === 'role') element.setAttribute(k, v);
    else element[k] = v;
  });
  children.forEach(child => {
    if (typeof child === 'string') element.appendChild(document.createTextNode(child));
    else if (child) element.appendChild(child);
  });
  return element;
}

function txt(text) {
  return document.createTextNode(String(text));
}

function clearEl(element) {
  while (element.firstChild) element.removeChild(element.firstChild);
}

// ─── Sheet Management ─────────────────────────────────────────────────────
function openSheet(type, id) {
  state.sheet.isOpen = true;
  state.sheet.type = type;
  state.sheet.id = id;
  document.getElementById('bottom-sheet').setAttribute('aria-hidden', 'false');
  document.getElementById('bottom-sheet').classList.add('is-open');
  document.getElementById('bottom-sheet-overlay').classList.add('is-open');
  document.body.style.overflow = 'hidden';
  renderSheetContent(type, id);
  document.getElementById('sheet-content').scrollTop = 0;
}

function closeSheet() {
  state.sheet.isOpen = false;
  state.sheet.stack = [];
  document.getElementById('bottom-sheet').setAttribute('aria-hidden', 'true');
  document.getElementById('bottom-sheet').classList.remove('is-open');
  document.getElementById('bottom-sheet-overlay').classList.remove('is-open');
  document.body.style.overflow = '';
}

function pushSheet(type, id) {
  const current = { type: state.sheet.type, id: state.sheet.id,
    scrollY: document.getElementById('sheet-content').scrollTop };
  state.sheet.stack.push(current);
  state.sheet.type = type;
  state.sheet.id = id;
  renderSheetContent(type, id);
  document.getElementById('sheet-content').scrollTop = 0;
}

function popSheet() {
  if (state.sheet.stack.length === 0) { closeSheet(); return; }
  const prev = state.sheet.stack.pop();
  state.sheet.type = prev.type;
  state.sheet.id = prev.id;
  renderSheetContent(prev.type, prev.id);
  requestAnimationFrame(() => {
    document.getElementById('sheet-content').scrollTop = prev.scrollY;
  });
}

function renderSheetContent(type, id) {
  const content = document.getElementById('sheet-content');
  clearEl(content);
  if (type === 'symptom') renderSymptom(id, content);
  else if (type === 'variable') renderVariable(id, content);
  else if (type === 'cluster') renderCluster(id, content);
}
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:STATE-MACHINE`
- File now contains `const state = {`
- File contains `const maps = {`
- File contains `function buildMaps() {`
- File contains `function el(tag,` (DOM helper)
- File contains `function openSheet(`
- File contains `function pushSheet(`
- File contains `function popSheet(`
- File contains `function renderSheetContent(`
- Uses `document.createTextNode` and `document.createElement` — no innerHTML with dynamic strings

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-29"`
- `pendingSteps`: remove `"step-29"`
- `flags.stateMachineCore`: set to `true`
