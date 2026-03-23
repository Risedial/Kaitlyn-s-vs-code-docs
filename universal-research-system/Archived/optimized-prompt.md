# Optimized Prompt — Universal Research System HTML Page Builder
# Execute this prompt in a fresh Claude Code session from the project root.

---

<required_reading>
Read both files completely before doing anything else:

@universal-research-system/Archived/system-explanation.md
@universal-research-system/Archived/style.css

After reading both files, confirm in exactly two sentences:
(1) What is the hex value of `--primary` in light mode in style.css?
(2) How many `##` top-level sections does system-explanation.md contain, and what is the last one titled?
Then proceed immediately to the task. No preamble.
</required_reading>

---

<role>
You are a front-end engineer delivering a polished static page as a finished client artifact. This file ships in one write operation — no follow-up, no revisions. Your frame: "Would I hand this to the client as a finished deliverable right now?" If the page is hard to navigate on mobile, cluttered, or missing any content from the source document, that is your failure to own.
</role>

---

<context_snapshot>
Critical facts — do not infer or guess these:

- Output file path: `C:\Users\Alexb\Documents\Alex's Applications\video-transcriber\universal-research-system\Archived\index.html`
- Attribution text: "Built and designed by Alex Bitar"
- Attribution URL: https://www.threads.com/@alexbitar
- Attribution must appear at the absolute top of the page, visually distinct, above all navigation and content
- The page must work when opened as a local file in a browser (file:// protocol — zero external requests: no CDN, no Google Fonts import, no remote images, no external scripts)
- All CSS goes in a single `<style>` block in `<head>`. All JS goes in a single `<script>` block at the end of `<body>`.
- Preserve every word of system-explanation.md — no summarizing, no paraphrasing, no truncation
</context_snapshot>

---

<task>
Complete in this exact order. Finish each step fully before starting the next.

1. Map the document structure of system-explanation.md. Identify every `##` section, `###` subsection, table, code block, and inline callout. You will replicate this hierarchy exactly in HTML using semantic elements.

2. Build the complete index.html file meeting all of these requirements:

   2a. Document head:
   - `<!DOCTYPE html>`, `<html lang="en">`, `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
   - `<title>Universal Research System</title>`
   - Single `<style>` block containing:
     - The full contents of style.css (all CSS variables for `:root` and `.dark`, plus the `@theme inline` block) — embed verbatim
     - Body base: `body { font-family: var(--font-sans, sans-serif); background: var(--background); color: var(--foreground); margin: 0; padding: 0; }`
     - Layout: `main { max-width: 800px; margin: 0 auto; padding: 1rem; }` — add `padding: 2rem` at `min-width: 640px`
     - Typography: `h1 { font-size: 1.75rem; }`, `h2 { font-size: 1.4rem; border-bottom: 2px solid var(--border); padding-bottom: 0.4rem; margin-top: 2.5rem; }`, `h3 { font-size: 1.1rem; margin-top: 1.75rem; }`, `p { line-height: 1.7; }`, `code { font-family: var(--font-mono, monospace); background: var(--muted); padding: 0.15em 0.35em; border-radius: 3px; font-size: 0.9em; }`, `pre code { display: block; overflow-x: auto; padding: 1rem; line-height: 1.6; }`
     - Tables: `table { width: 100%; border-collapse: collapse; margin: 1.25rem 0; font-size: 0.92em; }`, `th { background: var(--muted); text-align: left; padding: 0.5rem 0.75rem; border: 1px solid var(--border); }`, `td { padding: 0.5rem 0.75rem; border: 1px solid var(--border); vertical-align: top; }`, `tbody tr:nth-child(even) { background: color-mix(in srgb, var(--muted) 40%, transparent); }`
     - Attribution header: `header.attribution { background: var(--primary); color: var(--primary-foreground); padding: 0.75rem 1rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; font-size: 0.9rem; }`, `header.attribution a { color: var(--primary-foreground); font-weight: 600; }`
     - Sticky nav: `nav.sections { position: sticky; top: 0; background: var(--background); border-bottom: 1px solid var(--border); padding: 0.5rem 1rem; overflow-x: auto; white-space: nowrap; z-index: 10; font-size: 0.85rem; }`, `nav.sections a { margin-right: 1rem; color: var(--primary); text-decoration: none; }`, `nav.sections a:hover { text-decoration: underline; }`
     - Dark mode toggle button: `button#theme-toggle { background: transparent; border: 1px solid var(--primary-foreground); color: var(--primary-foreground); padding: 0.25rem 0.6rem; border-radius: var(--radius); cursor: pointer; font-size: 0.85rem; }`

   2b. Body structure:
   - `<header class="attribution">` containing: the text "Built and designed by Alex Bitar" and `<a href="https://www.threads.com/@alexbitar" target="_blank" rel="noopener">@alexbitar on Threads</a>`, plus `<button id="theme-toggle">Dark Mode</button>`
   - `<nav class="sections">` containing anchor links to each `<h2>` section — use the section title as link text and a slug derived from the title as the `href` (e.g., `#section-1-system-overview`)
   - `<main>` containing the full converted content from system-explanation.md

   2c. Content conversion rules — apply to every element in system-explanation.md:
   - `## Heading` → `<h2 id="[slug]">Heading</h2>` where slug = lowercase, spaces to hyphens, special chars removed
   - `### Heading` → `<h3 id="[slug]">Heading</h3>`
   - Fenced code blocks (` ``` ... ``` `) → `<pre><code>[content with HTML entities escaped: < → &lt;  > → &gt;  & → &amp;]</code></pre>`
   - Markdown tables (`| col |`) → `<table>` with `<thead>` for the header row and `<tbody>` for data rows
   - `**bold**` → `<strong>`
   - `` `inline code` `` → `<code>`
   - Blank-line-separated paragraphs → `<p>`
   - Horizontal rules `---` → `<hr>`
   - AMBIGUITY callout paragraphs → `<p>` — no special treatment needed

   2d. Dark mode script at end of `<body>`:
   ```
   <script>
     const toggle = document.getElementById('theme-toggle');
     const html = document.documentElement;
     if (localStorage.getItem('theme') === 'dark') { html.classList.add('dark'); toggle.textContent = 'Light Mode'; }
     toggle.addEventListener('click', () => {
       html.classList.toggle('dark');
       const isDark = html.classList.contains('dark');
       toggle.textContent = isDark ? 'Light Mode' : 'Dark Mode';
       localStorage.setItem('theme', isDark ? 'dark' : 'light');
     });
   </script>
   ```

3. Write the complete file to `C:\Users\Alexb\Documents\Alex's Applications\video-transcriber\universal-research-system\Archived\index.html` using the Write tool. Write the entire file in one operation. Do not output the HTML in the chat.

4. Confirm the write succeeded by stating the file path written and the approximate line count.
</task>

---

<constraints>
- Zero external requests — the page must work fully offline. No `<link>` to Google Fonts, no CDN script tags, no remote image src. Font fallbacks (`sans-serif`, `monospace`) are acceptable.
- Preserve all content from system-explanation.md exactly. Every word, every code block, every table row must appear in the output HTML.
- Do not output the HTML in the chat — write directly to the file using the Write tool.
- Do not add features not specified: no search, no sidebar, no additional pages, no animations.
- Start the Write tool call immediately after step 2 is complete. No preamble, no summary before the file write.
</constraints>

---

<fallback>
If the Write tool fails due to a path or permission error: write the file as `index.html` in the current working directory and add this HTML comment at line 2: `<!-- INTENDED PATH: C:\Users\Alexb\Documents\Alex's Applications\video-transcriber\universal-research-system\Archived\index.html -->`.

If system-explanation.md content is too large to embed completely in one Write call: write the file in two sequential Write calls — first pass covers everything through SECTION 3, second pass overwrites with the complete file including SECTIONS 4 and 5. Do not ask for input between the two writes.

If a markdown construct in system-explanation.md has no direct HTML equivalent: wrap it in `<div style="border-left: 3px solid var(--primary); padding: 0.5rem 1rem; margin: 1rem 0; background: color-mix(in srgb, var(--primary) 10%, transparent);">` — do not stop or ask for clarification.
</fallback>
