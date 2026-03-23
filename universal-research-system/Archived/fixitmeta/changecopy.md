Read these two files before doing anything:

1. @universal-research-system/Archived/index.html
2. @universal-research-system/Archived/landing-page-copy.md

Use all content that currently exists in `landing-page-copy.md`. Do not stall if it is incomplete or empty — convert exactly what is there. If the file is empty, the Overview `<main>` gets: `<p><em>Content coming soon.</em></p>`

---

## GOAL

Produce `universal-research-system/Archived/landing.html` — a single self-contained HTML file with two tabs:

| Tab | Content source |
|-----|----------------|
| Overview | `landing-page-copy.md` converted to HTML |
| Documentation | Inner HTML of `<main>` from `index.html`, extracted verbatim |

No external requests. No CDN. No Google Fonts. No remote images. Works via `file://` protocol. One `<style>` block in `<head>`. One `<script>` at end of `<body>`. Dark mode is the default.

---

## BUILD STRATEGY — 4 SEQUENTIAL STEPS

Write the file using Write once, then Edit three times. Never output raw HTML in chat. Use only tool calls. Complete each step fully before starting the next.

---

### STEP 1 — Write skeleton

Use the **Write tool** to create `universal-research-system/Archived/landing.html`.

**A. HTML tag:** `<html lang="en" class="dark">`

**B. `<head>` block:** Copy verbatim from `index.html` (every meta tag, every attribute). Set `<title>` to the text of the first `#` heading in `landing-page-copy.md`. If no `#` heading exists, use: `Universal Research System`.

**C. `<style>` block:** Copy the **complete** `<style>` block from `index.html` verbatim — every CSS variable, every rule, every media query, nothing omitted. Then, **inside the same `<style>` block**, append these additional rules after all existing content:

```css
/* Tab bar — mobile first */
.tab-bar {
  display: flex;
  background: var(--background);
  border-bottom: 2px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 20;
}
.tab-btn {
  flex: 1;
  padding: 0.75rem 0.5rem;
  background: none;
  border: none;
  border-bottom: 3px solid transparent;
  color: var(--muted-foreground);
  font-family: var(--font-sans, sans-serif);
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: color 0.15s, border-color 0.15s;
}
.tab-btn.active { color: var(--primary); border-bottom-color: var(--primary); }
.tab-btn:hover:not(.active) { color: var(--foreground); }
.tab-panel.hidden { display: none; }
/* Section nav wraps on narrow screens */
nav.sections {
  white-space: normal;
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem 0;
}
nav.sections a { white-space: nowrap; }
/* Tables scroll horizontally on mobile */
main table {
  display: block;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  max-width: 100%;
}
```

**D. Body structure** — write exactly as shown. The placeholder HTML comments must appear exactly as written (capitalized, underscored). Do not omit or rename them:

```html
<body>
  <header class="attribution">
    <span>Built and designed by Alex Bitar &mdash; <a href="https://www.threads.com/@alexbitar" target="_blank" rel="noopener">@alexbitar on Threads</a></span>
    <button id="theme-toggle">Light Mode</button>
  </header>

  <nav class="tab-bar" role="tablist" aria-label="Page sections">
    <button class="tab-btn active" id="btn-overview" role="tab" aria-selected="true" aria-controls="tab-overview">Overview</button>
    <button class="tab-btn" id="btn-docs" role="tab" aria-selected="false" aria-controls="tab-docs">Documentation</button>
  </nav>

  <div id="tab-overview" class="tab-panel" role="tabpanel" aria-labelledby="btn-overview">
    <nav class="sections" aria-label="Overview sections">
      <!-- OVERVIEW_NAV -->
    </nav>
    <main>
      <!-- OVERVIEW_MAIN -->
    </main>
  </div>

  <div id="tab-docs" class="tab-panel hidden" role="tabpanel" aria-labelledby="btn-docs">
    <nav class="sections" aria-label="Documentation sections">
      <!-- DOCS_NAV -->
    </nav>
    <main>
      <!-- DOCS_MAIN -->
    </main>
  </div>

  <script>
// SCRIPT_PLACEHOLDER
  </script>
</body>
</html>
```

---

### STEP 2 — Edit: Overview nav and main content

#### 2A — Replace `<!-- OVERVIEW_NAV -->`

Scan `landing-page-copy.md` for all `##` headings (second-level only — not `#`, not `###`). For each heading generate:

```html
<a href="#[slug]">[heading text]</a>
```

Slug rule: lowercase the heading text, replace every space with a hyphen, remove all characters that are not `a-z`, `0-9`, or `-`.

If no `##` headings exist: insert `<!-- no sections -->`.

#### 2B — Replace `<!-- OVERVIEW_MAIN -->`

Convert the full content of `landing-page-copy.md` to HTML. Apply every rule below to every element. Preserve every word — no summarizing, no paraphrasing, no truncation:

| Markdown | HTML |
|----------|------|
| `# Heading` | `<h1>Heading</h1>` |
| `## Heading` | `<h2 id="[slug]">Heading</h2>` — slug must match 2A exactly |
| `### Heading` | `<h3 id="[slug]">Heading</h3>` |
| `**bold**` | `<strong>bold</strong>` |
| `*italic*` or `_italic_` | `<em>italic</em>` |
| `` `inline code` `` | `<code>inline code</code>` |
| Fenced code block (``` ``` ```) | `<pre><code>` — escape `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;` |
| Markdown table | `<table><thead>...<tbody>...` with `<th>` and `<td>` |
| `- item` or `* item` | `<ul><li>item</li></ul>` |
| `1. item` | `<ol><li>item</li></ol>` |
| `---` | `<hr>` |
| Blank-line-separated prose | `<p>` |

**Token limit rule:** If the markdown file is more than 400 lines, perform 2A and 2B as two separate Edit calls — 2A first, then 2B. Never attempt to write more than ~400 lines of converted HTML in a single Edit call. If the converted Overview content would exceed ~400 lines, split it across multiple Edit calls by inserting from the beginning of `<!-- OVERVIEW_MAIN -->` and appending until complete.

---

### STEP 3 — Edit: Documentation nav and main content

#### 3A — Replace `<!-- DOCS_NAV -->`

Open `index.html`. Find `<nav class="sections">`. Copy the inner content (all `<a>` tags) verbatim — every tag, every attribute, every character exactly as it appears. Do not regenerate or modify them.

#### 3B — Replace `<!-- DOCS_MAIN -->`

Open `index.html`. Find `<main>...</main>`. Copy the entire inner HTML verbatim — every tag, every attribute, every entity reference, every character, in order. Do not regenerate, reformat, summarize, or paraphrase any of it.

**Token limit rule:** If the `<main>` inner content is more than 400 lines, perform 3A and 3B as two separate Edit calls — 3A first, then 3B. Never attempt to copy more than ~400 lines of HTML in a single Edit call.

---

### STEP 4 — Edit: Script

Replace `// SCRIPT_PLACEHOLDER` with exactly this JavaScript — no additions, no modifications:

```javascript
// Theme — default dark, persisted
const toggle = document.getElementById('theme-toggle');
const html = document.documentElement;
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') { html.classList.remove('dark'); toggle.textContent = 'Dark Mode'; }
toggle.addEventListener('click', () => {
  html.classList.toggle('dark');
  const isDark = html.classList.contains('dark');
  toggle.textContent = isDark ? 'Light Mode' : 'Dark Mode';
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

// Tab switching with persistence
const tabDefs = [
  { btn: document.getElementById('btn-overview'), panel: document.getElementById('tab-overview'), key: 'overview' },
  { btn: document.getElementById('btn-docs'),     panel: document.getElementById('tab-docs'),     key: 'docs'     }
];
function activateTab(target) {
  tabDefs.forEach(t => {
    const isActive = t === target;
    t.btn.classList.toggle('active', isActive);
    t.btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
    t.panel.classList.toggle('hidden', !isActive);
  });
  localStorage.setItem('activeTab', target.key);
}
tabDefs.forEach(t => t.btn.addEventListener('click', () => activateTab(t)));
const savedTab = localStorage.getItem('activeTab');
if (savedTab) {
  const match = tabDefs.find(t => t.key === savedTab);
  if (match) activateTab(match);
}
```

---

### STEP 5 — Confirm

State: the exact file path written and the approximate total line count.

---

## CONSTRAINTS

- Zero external requests. No CDN. No Google Fonts. No remote images. Works via `file://` protocol.
- All CSS in one `<style>` block. All JS in one `<script>` at end of `<body>`.
- Dark mode is the default: `<html lang="en" class="dark">`. Toggle button initial text is `Light Mode`.
- Do not add features not listed above.
- Do not output any HTML in chat. Use only Write and Edit tool calls to build the file.
- If `landing-page-copy.md` is incomplete, convert exactly what exists and move on.
