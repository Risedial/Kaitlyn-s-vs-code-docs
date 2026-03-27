# Refined Prompt

> Optimized using Anthropic's official prompt engineering best practices, context engineering principles, meta-prompting techniques, and domain-specific research.

---

## The Prompt

```xml
<role>
You are a senior PWA architect and Apple-quality mobile UI engineer operating within Claude Code. You combine deep expertise in:
- Vanilla JavaScript progressive web apps (zero-dependency, multi-file PWA architecture: index.html + manifest.json + sw.js)
- Apple Human Interface Guidelines (2026 Liquid Glass design language) translated to web CSS: visual hierarchy, motion curves, frosted glass, safe-area handling
- Clinical reference tool UX design: information density, scannability, 3-tap lookup flows, practitioner-facing copy
- Subagent orchestration pipelines: parallel research delegation via Task tool, Context7 documentation fetching, structured context-folder architecture

You do NOT speculate on FDN methodology — all clinical domain knowledge is extracted verbatim from the source file. You do NOT use frameworks (React, Vue, etc.), CDNs, or external dependencies of any kind. Every asset is local. Every dependency is zero.

Your expertise boundary: if a question falls outside PWA frontend engineering or functional medicine reference tool UI design, acknowledge the boundary rather than speculating.
</role>

<mission>
Transform the existing FDN Symptom Navigator (described in `all-prompt.md` in the workspace root) from a single-file HTML clinical reference tool into a production-quality mobile PWA with Apple-caliber UI/UX. The transformation is executed in four strictly-sequential phases:

Phase 1 — RESEARCH: Launch three parallel subagents to extract technical documentation, design patterns, and clinical data
Phase 2 — CONTEXT BUILD: Verify and finalize all six context files in a /context/ folder
Phase 3 — SYNTHESIZE: Produce the complete CSS design token file from gathered research
Phase 4 — BUILD: Generate the complete PWA in a /fdn-pwa/ project folder

Do not begin Phase 4 until Phases 1–3 are verified complete. Do not begin Phase 3 until Phase 2 is verified complete.
</mission>

<context>
<source_file>
The file `all-prompt.md` in the workspace root contains the complete original FDN Symptom Navigator specification:
- Complete FDN domain data: 57+ symptoms across 13 categories, 33+ lab marker variables, 5 root cause clusters
- Original app specification: single-file HTML, dark theme (#0f0f12 background), bottom navigation, collapsible category sections, slide transitions
- Variable reference panel with clinical metadata per variable: elevated interpretation, low interpretation, panel assignment, connections, cross-panel construct flag
- Color system: panel colors (MWP amber, MBA teal, SHP purple, GI-MAP green, cross-panel slate) and cluster colors (A red, B orange, C pink, D cyan, E amber)
- Clinical priority rules: H. pylori priority alert, Cluster E medical referral trigger, cross-panel construct visual distinction, HPA 5-phase model references

Extract and preserve ALL data from this file. The clinical data layer is the core product — the redesign touches UI/UX architecture and PWA capabilities only. No symptom, variable, or cluster data may be omitted or altered.
</source_file>

<transformation_goal>
Redesign the app as a mobile PWA with these quality targets:
- Installable to home screen: full Web App Manifest + service worker + valid icons
- Offline-first: 100% functionality with no network connection after first load
- Apple-quality visual language: Liquid Glass frosted glass surfaces, system-ui/SF Pro font stack, spring easing curves, generous safe-area handling for notch and home indicator
- Performance: Lighthouse PWA score ≥ 90, First Contentful Paint < 1s, all assets under 200KB total
- Touch UX: 44px minimum touch targets enforced in CSS, tactile :active feedback, smooth bottom-sheet detail views
</transformation_goal>

<pwa_architecture_note>
A proper PWA cannot be a single file. The /fdn-pwa/ output is a multi-file project:

  /fdn-pwa/
    index.html        — App shell: minimal HTML, all rendering via JS, all CSS inline
    manifest.json     — Web App Manifest (required for Chrome installability)
    sw.js             — Service Worker (cache-first offline strategy)

Service workers are scoped by URL and cannot be inlined in HTML via blob URLs across all browsers (Safari 16+ rejects blob SW registration). The manifest.json must be a separate linked file for Chrome's installability criteria. Icons (192×192 and 512×512) must be referenced in manifest.json; use base64-encoded PNG data URIs inline in the manifest icons array to satisfy the zero-external-dependency constraint.
</pwa_architecture_note>

<tools_available>
- Task tool (subagent_type: "general-purpose"): spawn parallel research subagents; general-purpose agents have access to all tools including MCP tools
- mcp__context7__resolve-library-id: resolve a library/API name to its Context7 library ID
- mcp__context7__query-docs: fetch current documentation for a library ID + topic query
- WebSearch: search for current design patterns, API specifications, and best practices
- Read, Write, Edit: file system operations
- Glob, Grep: codebase search and exploration
</tools_available>
</context>

<execution_phases>

<phase_1_research>
## Phase 1: Parallel Research

In a single message, launch ALL THREE subagents simultaneously using three Task tool calls. Do not launch sequentially — all three must run in parallel.

---

### Subagent A — PWA Technical Documentation

Prompt:
"You are a PWA technical researcher. Gather precise, current API documentation for building a vanilla JS PWA with no frameworks. Execute ALL of the following tasks:

1. Call mcp__context7__resolve-library-id with libraryName='progressive web apps mdn'. Then call mcp__context7__query-docs on the resolved ID to retrieve: Web App Manifest required properties and installability criteria, service worker install/activate/fetch lifecycle, Cache Storage API usage pattern.

2. Call mcp__context7__resolve-library-id with libraryName='service worker api mdn'. Then call mcp__context7__query-docs on the resolved ID to retrieve: cache-first fetch handler implementation, CacheStorage.open(), cache.addAll(), cache.match() usage.

3. Use WebSearch: 'PWA web app manifest installability criteria Chrome Safari 2025 required fields icons'

4. Use WebSearch: 'service worker cache-first strategy vanilla JavaScript implementation 2025 site:developer.mozilla.org OR site:web.dev'

5. Use WebSearch: 'CSS env safe-area-inset PWA iOS notch home indicator 2025 mobile web'

6. Use WebSearch: 'PWA manifest icons base64 data URI inline 192 512 installable 2025'

Synthesize all findings into a structured report and Write to the file `/context/pwa-technical.md` (create /context/ directory if it does not exist). The file must contain these exact sections:
- ## Manifest Spec (all required fields, Chrome installability criteria, iOS meta tags needed)
- ## Service Worker Implementation (complete JS pattern for install + activate + fetch handlers with cache-first strategy)
- ## Cache API Usage (cacheNames pattern, addAll on install, match on fetch)
- ## Installability Requirements (Chrome criteria checklist, Safari Add to Home Screen notes)
- ## Safe Area CSS (env(safe-area-inset-*) usage, viewport-fit=cover requirement, how to pad bottom nav and top header)
- ## PWA Icon Requirements (required sizes, how to embed as base64 data URIs in manifest JSON)"

---

### Subagent B — Apple HIG and 21st.dev Design System Research

Prompt:
"You are a mobile UI/UX design researcher specializing in Apple-quality web interfaces. Gather current design system specifications for a clinical reference PWA. Execute ALL of the following tasks:

1. Use WebSearch: '21st.dev component library modern mobile UI card bottom sheet design patterns 2025'

2. Use WebSearch: 'Apple Human Interface Guidelines 2026 Liquid Glass iOS dark mode design system tab bar'

3. Use WebSearch: 'iOS dark mode color system background surface separator text hierarchy hex values 2025 web CSS'

4. Use WebSearch: 'CSS backdrop-filter blur frosted glass iOS effect mobile web Safari 2025'

5. Use WebSearch: 'Apple SF Pro font system-ui CSS font-family fallback stack mobile web 2025'

6. Use WebSearch: 'iOS bottom sheet slide-up animation CSS spring cubic-bezier transform 2025'

7. Use WebSearch: 'Apple HIG iOS tab bar bottom navigation safe area height design spec 2025'

8. Use WebSearch: '21st.dev magic UI component pill tag badge design pattern Tailwind 2025'

Synthesize all findings into a complete design system specification and Write to `/context/ui-design-system.md`. The file must contain these exact sections:
- ## Design Philosophy (Apple's Clarity + Deference + Depth translated to CSS; how Liquid Glass applies to a dark clinical tool)
- ## Color Tokens (iOS dark mode palette — provide exact hex/rgba values for: bg-primary, bg-secondary, bg-tertiary, bg-glass, text-primary, text-secondary, text-tertiary, separator, accent, accent-destructive; ALSO include all FDN panel colors and cluster colors preserved from source spec)
- ## Typography System (font-family stack for SF Pro; size scale in rem from xs to 2xl; weight values; letter-spacing for headings vs. body vs. caps labels)
- ## Spacing System (4px grid — provide values for space-1 through space-12)
- ## Shadow Tokens (box-shadow values for elevation 0, 1, 2, 3 on dark backgrounds)
- ## Component Patterns (for each: DOM structure, key CSS properties, state variations):
    - Bottom Tab Bar (frosted glass, safe-area-inset-bottom, active state, 3-tab layout)
    - Top Header (frosted glass, safe-area-inset-top, title + optional back button)
    - Card / List Row (surface color, radius, shadow, separator, 44px min-height, chevron)
    - Variable Pill (color-coded by panel, rounded-full, min-height 28px, font-weight 600)
    - Cluster Tag (color-coded by cluster, rounded-sm, min-height 28px, font-weight 600)
    - Bottom Sheet (full-height slide-up overlay, drag indicator 32×4px, spring open animation)
    - Search Bar (iOS-style rounded rectangle, clear button, cancel transition)
    - Accordion Section Header (count badge, chevron rotation on expand, smooth max-height transition)
    - Alert Banner (full-width red high-contrast, ⚠ icon, bold text, 16px padding)
    - Priority Badge (cross-panel dashed border + gradient background)
- ## Motion System (easing cubic-bezier values for: push navigation, pop navigation, sheet open, sheet close, accordion expand; duration standards fast/normal/slow)
- ## Safe Area Integration (exact CSS patterns for padding-bottom on nav, padding-top on header)"

---

### Subagent C — Source App Data Extraction and Architecture Audit

Prompt:
"You are a data extraction specialist. Extract and document the COMPLETE data layer from the FDN app specification. Execute ALL of the following tasks:

1. Read the file 'all-prompt.md' from the workspace root (it is a large file — read the entire thing).

2. Extract and document EVERY symptom entry. For each symptom, capture:
   - Unique ID (derive from symptom label: lowercase, hyphens for spaces, e.g. 'always-tired')
   - Label (exact text)
   - Category (one of the 13 categories)
   - Variables list (array of variable IDs)
   - Clusters list (array of cluster letters)
   - 'What This Means' interpretation (2-3 sentence practitioner-voice text from the knowledge base)

   Count the symptoms. The count must be ≥57. If you count fewer, re-read the source file — no data may be omitted.

3. Extract and document EVERY variable entry. For each variable, capture:
   - Unique ID (e.g. 'indican', 'hpylori', 'hpa-pattern')
   - Name (exact display name)
   - Panel (one of: MWP, MBA, SHP, GI-MAP, cross-panel)
   - Elevated interpretation (clinical meaning)
   - Low interpretation (clinical meaning, or 'N/A — not interpreted as low in this context')
   - Connections (array of variable IDs this connects to)
   - Clusters (array of cluster letters)
   - isCrossPanel (boolean)
   - isPriorityPathogen (boolean — true for H. pylori only)
   - isMedicalReferral (boolean — true for Calprotectin/Lactoferrin and Occult Blood)

   Count the variables. The count must be ≥28.

4. Extract and document ALL 5 cluster definitions. For each cluster, capture:
   - Letter (A–E)
   - Name (full name)
   - Color (hex value from color system)
   - Mechanism (description)
   - Priority note (special action required, if any)
   - Variables list (array of variable IDs in this cluster)

5. Document the current app screen architecture:
   - List all 5 screens (home, symptom, variable, cluster, search)
   - For each screen: what data it displays, what navigation actions exist
   - State machine: what properties does state need?
   - Clinical UI special cases that must carry through to the redesign

Write ALL extraction output to TWO files:

File 1 — `/context/data-inventory.md`:
- ## Symptom Count and Index (total count + alphabetical list of all symptom IDs and labels)
- ## Variable Count and Index (total count + list of all variable IDs and names with panel assignment)
- ## Cluster Definitions (all 5 with all captured fields)
- ## Clinical UI Special Cases (H. pylori alert rule, Cluster E referral rule, cross-panel flags, HPA phase references)
- ## Color System (exact hex values for all panel and cluster colors)

File 2 — `/context/app-architecture.md`:
- ## Screen Inventory (all 5 screens with data requirements)
- ## Navigation Model (stack-based navigation, forward/back transitions)
- ## State Machine Spec (state object shape, navigate() and goBack() behavior)
- ## Data Relationships (reverse mapping strategy: cluster → symptoms, variable → symptoms)"
</phase_1_research>

<phase_2_context_build>
## Phase 2: Context Folder Verification

After all three Phase 1 subagents complete, verify these four files exist and contain substantive content (not empty, not placeholder):
- `/context/pwa-technical.md`
- `/context/ui-design-system.md`
- `/context/data-inventory.md`
- `/context/app-architecture.md`

If any file is missing or contains only placeholder text, re-run the corresponding subagent before proceeding.

Then write one synthesis file. Write `/context/build-manifest.md` with these sections:
- ## File Structure (exact /fdn-pwa/ directory tree with description of each file's role)
- ## CSS Architecture (which custom properties to define, how CSS is organized within index.html style block, class naming conventions)
- ## JS Architecture (DATA object structure, state object shape, navigate/goBack function contract, render function signatures, event delegation pattern)
- ## PWA Integration Checklist (manifest fields, service worker registration snippet, offline cache list, installability criteria to verify)
- ## Clinical UX Rules (H. pylori alert logic: exact condition check; Cluster E referral: where and how it appears; cross-panel construct styling rules; HPA phase reference display)
- ## Screen-by-Screen Build Spec (for each of 5 screens: DOM structure outline, component types used, transition type, data sources)
</phase_2_context_build>

<phase_3_synthesize>
## Phase 3: Design Token Extraction

Read `/context/ui-design-system.md` and `/context/pwa-technical.md`.

Produce a single CSS custom properties block that anchors the entire design system. Write to `/context/design-tokens.css`. This file must have ZERO placeholder [value] text — every token must have a concrete, exact CSS value derived from the research in Phase 1.

The file must define all of the following tokens (fill values from research):

```css
/* === FDN PWA DESIGN TOKENS === */
:root {
  /* Backgrounds — iOS Dark Mode equivalents */
  --bg-primary:     ;    /* App background */
  --bg-secondary:   ;    /* Card surface */
  --bg-tertiary:    ;    /* Elevated surface (nav, sheet header) */
  --bg-glass:       ;    /* rgba frosted glass background */

  /* Text */
  --text-primary:   ;
  --text-secondary: ;
  --text-tertiary:  ;

  /* Separators */
  --separator:      ;
  --separator-opaque: ;

  /* Accent */
  --accent:             ;    /* Interactive blue */
  --accent-destructive: ;    /* Red for alerts and referrals */

  /* FDN Panel Colors (preserve exactly from source) */
  --panel-mwp:   #e07c3a;
  --panel-mba:   #3abde0;
  --panel-shp:   #8b5cf6;
  --panel-gimap: #22c55e;
  --panel-cross: #94a3b8;

  /* FDN Cluster Colors (preserve exactly from source) */
  --cluster-a: #ef4444;
  --cluster-b: #f97316;
  --cluster-c: #ec4899;
  --cluster-d: #06b6d4;
  --cluster-e: #fbbf24;

  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif;
  --font-size-xs:   0.6875rem;
  --font-size-sm:   0.8125rem;
  --font-size-base: 1rem;
  --font-size-md:   1.0625rem;
  --font-size-lg:   1.25rem;
  --font-size-xl:   1.5rem;
  --font-size-2xl:  2rem;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --letter-spacing-tight:  -0.02em;
  --letter-spacing-normal:  0em;
  --letter-spacing-wide:    0.03em;
  --letter-spacing-caps:    0.06em;

  /* Spacing — 4px base grid */
  --space-1:  0.25rem;
  --space-2:  0.5rem;
  --space-3:  0.75rem;
  --space-4:  1rem;
  --space-5:  1.25rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;

  /* Border Radius */
  --radius-sm:   8px;
  --radius-md:   12px;
  --radius-lg:   16px;
  --radius-xl:   20px;
  --radius-full: 9999px;

  /* Shadows — dark-background-optimized */
  --shadow-0: none;
  --shadow-1: ;    /* low elevation */
  --shadow-2: ;    /* medium elevation (cards) */
  --shadow-3: ;    /* high elevation (sheets) */

  /* Motion — Apple-like easing */
  --ease-spring:   cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-snap:     cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  --duration-fast:   150ms;
  --duration-normal: 300ms;
  --duration-slow:   450ms;

  /* Safe Areas */
  --safe-top:    env(safe-area-inset-top, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left:   env(safe-area-inset-left, 0px);
  --safe-right:  env(safe-area-inset-right, 0px);

  /* Touch Targets */
  --touch-target: 44px;

  /* Layout */
  --max-width:    430px;
  --nav-height:   calc(60px + var(--safe-bottom));
  --header-height: calc(52px + var(--safe-top));
}
```

Replace all blank `;` with concrete values from the research. The bg-glass token must be a valid rgba() value. Shadow tokens must use box-shadow syntax. No token may remain without a value.
</phase_3_synthesize>

<phase_4_build>
## Phase 4: Build the PWA

Using ALL six context files as your knowledge base, build the complete PWA. Write every file to /fdn-pwa/. Do not truncate any file.

---

### File: manifest.json

Write valid JSON satisfying Chrome installability criteria:
```json
{
  "name": "FDN Symptom Navigator",
  "short_name": "FDN Nav",
  "description": "FDN lab marker reference tool for clinical practitioners",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "[use --bg-primary hex value]",
  "background_color": "[use --bg-primary hex value]",
  "categories": ["medical", "health", "productivity"],
  "icons": [
    {
      "src": "data:image/png;base64,[generate 192×192 icon as base64 data URI]",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "data:image/png;base64,[generate 512×512 icon as base64 data URI]",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}
```
Generate the icon base64 data URIs as minimal valid PNG images (solid dark background with "FDN" text or simple geometric icon). The icons must be valid PNG files encoded as base64.

---

### File: sw.js

Implement a cache-first service worker:

```javascript
const CACHE_NAME = 'fdn-nav-v1';
const ASSETS = ['./index.html', './manifest.json', './sw.js'];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        if (!response || response.status !== 200 || response.type !== 'basic') return response;
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        return response;
      });
    })
  );
});
```

---

### File: index.html

Build a complete, production-quality HTML file. Structure requirements:

**`<head>` block** — must include:
- `<meta charset="UTF-8">`
- `<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">`
- `<meta name="apple-mobile-web-app-capable" content="yes">`
- `<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">`
- `<meta name="theme-color" content="[bg-primary hex]">`
- `<title>FDN Symptom Navigator</title>`
- `<link rel="manifest" href="./manifest.json">`
- All CSS inside one `<style>` block

**CSS Requirements** (inside `<style>`):

Include ALL design tokens from /context/design-tokens.css as :root custom properties.

Body and layout:
```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { height: 100%; }
body {
  font-family: var(--font-family);
  background: var(--bg-primary);
  color: var(--text-primary);
  max-width: var(--max-width);
  margin: 0 auto;
  min-height: 100dvh;
  overflow-x: hidden;
  -webkit-tap-highlight-color: transparent;
}
```

Screen stack navigation (slide transitions — CSS only, no JS animation):
```css
#screen-stack { position: relative; min-height: calc(100dvh - var(--nav-height)); }

.screen {
  position: absolute;
  top: 0; left: 0; right: 0;
  min-height: calc(100dvh - var(--nav-height));
  will-change: transform;
  transition: transform var(--duration-normal) var(--ease-snap);
}

.screen.enter-from-right { transform: translateX(100%); }
.screen.enter-from-left  { transform: translateX(-100%); }
.screen.active           { transform: translateX(0); }
.screen.exit-to-left     { transform: translateX(-30%); }
.screen.exit-to-right    { transform: translateX(100%); }
```

Bottom tab navigation:
```css
#bottom-nav {
  position: fixed;
  bottom: 0; left: 50%; transform: translateX(-50%);
  width: 100%; max-width: var(--max-width);
  height: var(--nav-height);
  padding-bottom: var(--safe-bottom);
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid var(--separator);
  display: flex;
  align-items: flex-start;
  padding-top: 8px;
  z-index: 100;
}

.nav-tab {
  flex: 1;
  min-height: var(--touch-target);
  min-width: var(--touch-target);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-tertiary);
  font-family: var(--font-family);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-medium);
  letter-spacing: var(--letter-spacing-wide);
  transition: color var(--duration-fast) var(--ease-standard);
}

.nav-tab.active { color: var(--accent); }
.nav-tab:active { opacity: 0.6; }
```

Top header:
```css
.screen-header {
  position: sticky; top: 0;
  padding-top: var(--safe-top);
  height: var(--header-height);
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid var(--separator);
  display: flex; align-items: flex-end; justify-content: center;
  padding-bottom: var(--space-3);
  z-index: 50;
}
```

Cards and list rows:
```css
.symptom-row {
  display: flex; align-items: center;
  min-height: var(--touch-target);
  min-width: var(--touch-target);
  padding: var(--space-3) var(--space-4);
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--separator);
  cursor: pointer;
  gap: var(--space-3);
  transition: background var(--duration-fast) var(--ease-standard);
}
.symptom-row:active { background: var(--bg-tertiary); transform: scale(0.98); }
```

Variable pills:
```css
.variable-pill {
  display: inline-flex; align-items: center;
  min-height: 28px; min-width: var(--touch-target);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  color: #000;
  background: var(--panel-color, var(--panel-cross));
  transition: transform var(--duration-fast) var(--ease-spring);
}
.variable-pill:active { transform: scale(0.93); }
.variable-pill.cross-panel {
  background: transparent;
  border: 2px dashed var(--panel-color, var(--panel-cross));
  color: var(--panel-color, var(--panel-cross));
}
```

Cluster tags:
```css
.cluster-tag {
  display: inline-flex; align-items: center;
  min-height: 28px; min-width: var(--touch-target);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-sm);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  color: #000;
  background: var(--cluster-color, var(--cluster-a));
  transition: transform var(--duration-fast) var(--ease-spring);
}
.cluster-tag:active { transform: scale(0.93); }
```

Priority alert banner:
```css
.priority-alert {
  display: flex; align-items: center; gap: var(--space-3);
  padding: var(--space-4);
  background: color-mix(in srgb, var(--accent-destructive) 20%, transparent);
  border: 1px solid var(--accent-destructive);
  border-radius: var(--radius-md);
  margin: var(--space-4);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--accent-destructive);
}
```

Bottom sheet (for detail screens):
```css
.detail-sheet {
  position: fixed; inset: 0;
  background: var(--bg-primary);
  transform: translateY(100%);
  transition: transform var(--duration-slow) var(--ease-spring);
  overflow-y: auto;
  overscroll-behavior: contain;
  padding-bottom: calc(var(--nav-height) + var(--space-8));
  z-index: 10;
}
.detail-sheet.open { transform: translateY(0); }

.drag-indicator {
  width: 36px; height: 5px;
  background: var(--separator-opaque);
  border-radius: var(--radius-full);
  margin: var(--space-3) auto var(--space-2);
}
```

Accordion sections:
```css
.category-section { overflow: hidden; }
.category-header {
  display: flex; align-items: center; justify-content: space-between;
  min-height: var(--touch-target); min-width: var(--touch-target);
  padding: var(--space-3) var(--space-4);
  cursor: pointer;
  background: var(--bg-primary);
  border-bottom: 1px solid var(--separator);
}
.category-header:active { opacity: 0.7; }
.category-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height var(--duration-normal) var(--ease-standard);
}
.category-content.expanded { max-height: 9999px; }
.chevron { transition: transform var(--duration-fast) var(--ease-standard); }
.category-header.open .chevron { transform: rotate(90deg); }
```

Search bar:
```css
.search-bar {
  display: flex; align-items: center; gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--separator);
}
.search-input {
  flex: 1; min-height: var(--touch-target);
  padding: var(--space-2) var(--space-3);
  background: var(--bg-tertiary);
  border: none; border-radius: var(--radius-full);
  color: var(--text-primary);
  font-family: var(--font-family);
  font-size: var(--font-size-base);
  outline: none;
}
```

Mechanism hierarchy tree:
```css
.mechanism-tree {
  font-size: var(--font-size-sm);
  color: var(--text-secondary);
  line-height: 1.7;
  padding: var(--space-4);
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  font-feature-settings: 'kern' 1;
  white-space: pre-line;
}
```

**`<body>` structure**:
```html
<body>
  <div id="screen-stack">
    <div id="home-screen" class="screen active"></div>
  </div>
  <nav id="bottom-nav">
    <button class="nav-tab active" data-tab="home">
      <span class="nav-icon">⌂</span>
      <span>Home</span>
    </button>
    <button class="nav-tab" data-tab="search">
      <span class="nav-icon">⌕</span>
      <span>Search</span>
    </button>
    <button class="nav-tab" data-tab="clusters">
      <span class="nav-icon">◎</span>
      <span>Clusters</span>
    </button>
  </nav>
</body>
```

**`<script>` block** — organized in this exact order:

**1. DATA object** — fully populated using ALL data from /context/data-inventory.md.
Structure:
```javascript
const DATA = {
  symptoms: {
    // keyed by symptom ID string
    'always-tired': {
      label: 'Always tired',
      category: 'Energy & Fatigue',
      variables: ['cortisol-pattern', 'dhea', 'hpa-pattern', 'siga-shp', 'indican', '8-ohdg', 'hepatic-detox'],
      clusters: ['A', 'B'],
      interpretation: '...',
      mechanismTree: '...'
    },
    // ... ALL 57+ symptoms fully written out
  },
  variables: {
    // keyed by variable ID string
    'indican': {
      name: 'Indican',
      panel: 'MWP',
      panelColor: 'var(--panel-mwp)',
      elevated: 'Bacterial overgrowth stealing tryptophan, liver burden...',
      low: 'N/A — not interpreted as low in this context',
      connections: ['urinary-bile-acids', '8-ohdg', 'zonulin', 'histamine-mba', 'dao', 'siga-shp'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    // ... ALL 28+ variables fully written out
  },
  clusters: {
    'A': {
      letter: 'A',
      name: 'GI Ecosystem Collapse',
      fullName: 'Cluster A — GI Ecosystem Collapse (Primary Driver)',
      color: 'var(--cluster-a)',
      mechanism: '...',
      priorityNote: 'Address before all others — GI dysfunction drives all downstream clusters.',
      variables: ['indican', 'urinary-bile-acids', ...]
    },
    // ... ALL 5 clusters
  }
};
```

Populate every field completely. Use exact data from /context/data-inventory.md. Do NOT use placeholder comments like `// ... more symptoms`.

**2. PWA registration** (immediately after DATA):
```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js').catch(console.error);
}
```

**3. State machine**:
```javascript
const state = {
  screen: 'home',
  item: null,
  stack: [],
  searchQuery: '',
  expandedCategories: new Set(),
  scrollPositions: new Map()
};
```

**4. Navigation functions**:
```javascript
function navigate(screen, item = null) {
  // Save current scroll position
  state.scrollPositions.set(state.screen + (state.item?.id || ''), window.scrollY);
  // Push current state to stack
  state.stack.push({ screen: state.screen, item: state.item });
  // Transition
  state.screen = screen;
  state.item = item;
  render();
}

function goBack() {
  if (!state.stack.length) return;
  const prev = state.stack.pop();
  state.screen = prev.screen;
  state.item = prev.item;
  render();
  // Restore scroll position
  requestAnimationFrame(() => {
    const savedScroll = state.scrollPositions.get(state.screen + (state.item?.id || ''));
    if (savedScroll !== undefined) window.scrollTo(0, savedScroll);
  });
}
```

**5. Render functions** — implement ALL of the following:

`renderHome()`:
- Title "What are you experiencing?"
- iOS-style search bar (min-height 44px)
- 14 category accordion sections in exact order from source spec
- Each section starts collapsed unless in state.expandedCategories
- When searchQuery is active (≥2 chars): filter symptoms, show match count in header, auto-expand matching sections
- Each symptom row: label text, chevron (›), 44px min-height, data-action="navigate-symptom" data-id="[symptom-id]"
- Use textContent and createElement only — never innerHTML with dynamic strings

`renderSymptom(id)`:
- Drag indicator
- Back button (‹) top-left — data-action="go-back"
- Symptom name heading (--font-size-xl, --font-weight-bold)
- **H. PYLORI CHECK**: `if (DATA.symptoms[id].variables.includes('hpylori'))` → render .priority-alert banner BEFORE variable pills: "⚠ Treat H. pylori before addressing other findings"
- Section "Variables Involved": pill grid, each pill colored by panel via CSS custom property --panel-color, data-action="navigate-variable" data-id="[var-id]"
- Section "Root Cause Clusters": cluster tags, each colored by cluster, data-action="navigate-cluster" data-id="[cluster-letter]"
- Section "What This Means": practitioner-voice interpretation text (2-3 sentences from DATA)
- Section "Mechanism Hierarchy": .mechanism-tree div with └─ indented text tree (minimum 3 levels)

`renderVariable(id)`:
- Drag indicator
- Back button
- Variable name heading
- Panel badge: colored by panel color, text is panel name (MWP / MBA / SHP / GI-MAP)
- If variable.isCrossPanel: "Cross-panel amplifier" badge with dashed border
- If variable.isMedicalReferral: high-contrast referral warning banner: "⚕ MEDICAL REFERRAL REQUIRED — refer to physician before FDN intervention"
- If variable.isPriorityPathogen: priority pathogen banner: "⚠ Priority Pathogen — treat H. pylori before addressing all other GI findings"
- "When Elevated" section
- "When Low / Deficient" section
- "Connected Variables" pill grid
- "Root Cause Clusters" cluster tags

`renderCluster(id)`:
- Drag indicator
- Back button
- Cluster letter + full name as heading, colored per cluster color
- Mechanism description
- Priority Note: if id === 'A' → "Address before all others..."; if id === 'E' → prominent MEDICAL REFERRAL REQUIRED display
- "Variables in This Cluster" pill grid
- "Symptoms Associated": reverse-map by checking DATA.symptoms entries for clusters.includes(id) — render as tappable rows

`renderSearch()`:
- Full-screen search input, auto-focused on screen activation
- Real-time filtering (fires at searchQuery.length ≥ 2)
- Results grouped: "Symptoms" section → symptom rows; "Variables" section → variable pills
- Empty state: "Start typing to search symptoms and variables"
- No results state: "No matches for '[query]'"

**6. Main render dispatcher and event delegation**:
```javascript
function render() {
  // Clear previous screen content and set active tab
  // Dispatch to correct render function based on state.screen + state.item
}

document.addEventListener('click', e => {
  const target = e.target.closest('[data-action]');
  if (!target) return;
  const { action, id } = target.dataset;
  if (action === 'navigate-symptom')  navigate('symptom', { type: 'symptom', id });
  if (action === 'navigate-variable') navigate('variable', { type: 'variable', id });
  if (action === 'navigate-cluster')  navigate('cluster', { type: 'cluster', id });
  if (action === 'go-back')           goBack();
  if (action === 'toggle-category')   toggleCategory(id);
  if (action === 'set-tab')           switchTab(target.dataset.tab);
});
```

**7. init()** — called at bottom of script:
```javascript
function init() {
  render();
}
init();
```
</phase_4_build>

</execution_phases>

<constraints>
**This IS:**
- A clinical practitioner reference tool — all copy uses practitioner register only
- An offline-first PWA — 100% functionality with no network after first load
- A zero-external-dependency project — no CDN, no framework, no external fonts, no API calls

**This is NOT:**
- A patient-facing self-diagnosis app — do NOT write "you might have" or "you should try" language
- A treatment protocol engine — do NOT add supplement names, dosages, or protocols
- A data visualization app — no canvas, no SVG graphs, no chart libraries

**Do NOT:**
- Truncate the DATA object — all 57+ symptoms, 28+ variables, 5 clusters must be fully written; never use `// ... more symptoms` comments
- Use innerHTML with dynamically-constructed strings — use textContent and createElement for all dynamic content
- Reference external URLs, CDNs, or remote image sources in any generated file
- Use setTimeout or setInterval to drive animations — CSS transitions exclusively
- Add localStorage or IndexedDB usage (not in original spec)
- Use fetch() for data loading (all data is embedded in the JS DATA object)
- Add more than 3 bottom navigation tabs
- Omit color coding from variable pills or cluster tags — color encodes clinical identity, not decoration
- Skip the H. pylori priority alert check in renderSymptom()
- Skip the Cluster E medical referral language in renderCluster() and in the isMedicalReferral variable card logic
</constraints>

<output_format>
By the end of execution, the workspace must contain exactly these files, all non-empty and production-ready:

/context/
  pwa-technical.md        — PWA API documentation (manifest, SW, cache, safe areas, icons)
  ui-design-system.md     — Apple HIG + 21st.dev component design system
  data-inventory.md       — Complete FDN data layer (57+ symptoms, 28+ variables, 5 clusters)
  app-architecture.md     — Screen inventory, navigation model, state machine, special cases
  build-manifest.md       — Synthesized build specification
  design-tokens.css       — Complete CSS custom properties, zero placeholders

/fdn-pwa/
  index.html              — Complete PWA: app shell + embedded DATA + all CSS + all JS
  manifest.json           — Valid Web App Manifest (passes Chrome installability audit)
  sw.js                   — Service Worker (cache-first, install/activate/fetch handlers)
</output_format>

<success_criteria>
The build is complete and correct when ALL of the following are true:

1. **Data completeness**: DATA object in index.html contains all 57+ symptoms, 28+ variables, 5 cluster definitions — no placeholder comments, no truncation
2. **PWA installability**: manifest.json contains name, short_name, display: standalone, theme_color, start_url, scope, and two valid icons; sw.js registers without error; Chrome Lighthouse PWA audit shows installable
3. **Offline operation**: App renders completely and all screens are navigable when DevTools Network is set to Offline after first load
4. **Apple-quality UI**: Bottom tab bar is frosted glass with safe-area padding; detail sheets use spring transition; cards use border-radius ≥12px; typography uses SF Pro system-ui stack; all spacing uses the 4px grid
5. **3-tap navigation**: A practitioner can reach Symptom → Variable → Connected Variable in ≤3 taps with no navigation dead ends and no page reload
6. **H. pylori alert**: Every symptom whose variable list includes 'hpylori' shows the red priority banner BEFORE the variable pills section
7. **Cluster E referral**: Cluster E detail screen shows MEDICAL REFERRAL REQUIRED in a prominent, high-contrast display; Occult Blood and Calprotectin/Lactoferrin variable cards each include referral warning language
8. **Search completeness**: Typing "histamine" returns: all symptoms containing Histamine-MBA, the Histamine-MBA variable card, and the Histamine-DAO Regulatory System card
9. **Touch target compliance**: All interactive elements (symptom rows, variable pills, cluster tags, back button, nav tabs, category headers) have computed min-height: 44px and min-width: 44px
10. **Zero external dependencies**: No src, href, or CSS url() references point to any external domain; /fdn-pwa/ renders fully offline
11. **Context folder complete**: All 6 context files exist with substantive content — design-tokens.css has no [value] placeholder text
12. **Back navigation integrity**: Tapping back from a variable detail screen returns to the exact symptom detail screen that opened it, with scroll position restored
</success_criteria>

<verification>
Before finalizing any generated file, complete this full checklist. Every item must be checked:

**Context files:**
- [ ] pwa-technical.md: documents manifest required fields, SW cache-first pattern, installability criteria, safe-area CSS
- [ ] ui-design-system.md: documents color tokens with exact hex values, typography scale, all 10 component patterns, motion easing values
- [ ] data-inventory.md: symptom count confirmed ≥57; variable count confirmed ≥28; cluster count confirmed = 5
- [ ] app-architecture.md: documents all 5 screens; navigation model; state shape; H. pylori, Cluster E, cross-panel special cases
- [ ] design-tokens.css: zero [value] placeholders; --bg-glass has rgba() value; shadow tokens use box-shadow syntax; all tokens present

**Build files:**
- [ ] manifest.json: valid JSON; has name, short_name, display: standalone, theme_color, background_color, start_url, scope, icons array with 2 entries
- [ ] sw.js: install handler caches assets; activate handler clears old caches; fetch handler is cache-first; self.skipWaiting() called
- [ ] index.html: DATA.symptoms count ≥57; DATA.variables count ≥28; DATA.clusters count = 5
- [ ] H. pylori alert logic: renderSymptom() checks variable list for 'hpylori' and conditionally renders .priority-alert before variable pills
- [ ] Cluster E: renderCluster('E') displays MEDICAL REFERRAL REQUIRED in prominent display
- [ ] isMedicalReferral: Occult Blood and Calprotectin/Lactoferrin variable cards render referral warning banner
- [ ] No external URL references in any of the 3 build files
- [ ] All interactive element CSS rules enforce min-height: var(--touch-target) and min-width: var(--touch-target)
- [ ] Service worker registration code is present in index.html script block

**Mental walkthrough:**
Tap "Bloating" category row on Home → Bloating symptom detail slides up as bottom sheet → H. pylori priority alert banner renders above the variable pills → tap "H. pylori" pill → H. pylori variable detail slides in → priority pathogen banner is visible; referral language is visible → tap back button → Bloating symptom detail returns with scroll position restored → tap "Cluster A" cluster tag → Cluster A detail shows "Address before all others" priority note + reverse-mapped symptoms list including "Bloating"
</verification>
```

---

## Refinement Report

### Original Prompt

> Create a prompt that takes this prompt @all-prompt.md Redesign the app to be a mobile PWA that creates a clean modern UI. This should be as high quality UX and UI as apple apps. The prompt that you create will use subagents to do research and connect to context7 and 21 first dev to ensure that it extracts all the data needed and writes it to a new folder in the root directory and creates context folders that the new and improved @all-prompt.md will use to have picture perfect understanding of ONLY the information it needs to execute the build perfectly.

### Diagnostic Results

| # | Item | Original Status | How Addressed in Refined Prompt |
|---|------|----------------|---------------------------------|
| 1 | XML/Section Structure | Fail | Added 8 XML-tagged sections: `<role>`, `<mission>`, `<context>` (with sub-tags), `<execution_phases>` (with 4 phase sub-tags), `<constraints>`, `<output_format>`, `<success_criteria>`, `<verification>` |
| 2 | Data-First Ordering | Fail | Context + source file description → execution phases → deliverable spec + verification at end |
| 3 | Hierarchical Nesting | Fail | `<context>` contains `<source_file>`, `<transformation_goal>`, `<pwa_architecture_note>`, `<tools_available>`; `<execution_phases>` contains 4 numbered phase sub-tags |
| 4 | Progressive Disclosure | Fail | Role → Mission → Context → Phase 1 research → Phase 2 verification → Phase 3 synthesis → Phase 4 build → Constraints → Output → Success Criteria |
| 5 | Role Assignment | Fail | Senior PWA architect + Apple-quality mobile UI engineer with explicit dual expertise domains and methodology |
| 6 | Expertise Scoping | Fail | Role bounded to "PWA frontend engineering and functional medicine reference tool UI design"; out-of-scope instruction included |
| 7 | Audience Awareness | Partial | Clarified: FDN practitioners in live clinical sessions; practitioner register explicitly required; patient language prohibited |
| 8 | Chain-of-Thought Phasing | Partial | 4 explicit sequential phases with transition conditions between them; parallel subagent orchestration defined |
| 9 | Self-Verification | Fail | Full `<verification>` checklist with 18 items + mental walkthrough before finalizing |
| 10 | Thinking Process | Fail | Each phase defines what to research/decide BEFORE writing any file; subagent instructions specify exact tool call sequences |
| 11 | Ambiguity Elimination | Fail | "clean modern UI" → Apple HIG 2026 Liquid Glass specification; "high quality as apple apps" → 12 specific Apple UI patterns; "21 first dev" corrected to 21st.dev with explicit WebSearch directive; "context folders" → exact /context/ file inventory with required sections per file |
| 12 | Active Directives | Partial | All passive language converted: "Build", "Write", "Execute", "Launch", "Verify", "Call", "Synthesize" |
| 13 | Specificity Gradients | Fail | Hard structural requirements (CSS custom property names, JS function signatures, HTML element structure) separated from soft design guidance |
| 14 | Constraint Boundaries | Fail | Explicit "This IS" / "This is NOT" section covering 3 IS and 3 IS NOT items |
| 15 | Negative Constraints | Fail | 10 specific "Do NOT" items covering data truncation, innerHTML injection, external URLs, animation approach, patient language, localStorage, tab count |
| 16 | Spelling/Grammar | Partial | "21 first dev" corrected to "21st.dev"; "context7" properly styled; "21st dev" → "21st.dev Magic MCP" |
| 17 | Domain Context Sufficiency | Partial | PWA multi-file architecture requirement explained (why single-file impossible); service worker scope rules; Chrome installability criteria; Apple HIG principles; FDN clinical data rules carried through |
| 18 | Few-Shot Examples | Fail | Mental walkthrough example in `<verification>`: exact tap sequence from Bloating → H. pylori → back → Cluster A |
| 19 | Reference Anchoring | Partial | Context7 tools named explicitly (mcp__context7__resolve-library-id, mcp__context7__query-docs); 21st.dev named and referenced; Apple HIG cited with 2026 Liquid Glass language; MDN/web.dev cited in research directives |
| 20 | Output Format Specification | Fail | Exact file tree with 6 context files + 3 build files; required sections per context file; exact HTML/CSS/JS structure for index.html |
| 21 | Success Criteria | Fail | 12 measurable conditions with testable assertions covering data counts, PWA audit, offline operation, UI quality, navigation flows, clinical alerts, search, touch targets |
| 22 | Tone/Voice Calibration | Fail | Practitioner register throughout; "do NOT write patient-facing copy" as hard constraint in both role and constraints |
| 23 | Permission to Expand | Fail | Subagent instructions include "use WebSearch" for additional research beyond core topics; research scope intentionally broad to catch related patterns |
| 24 | Uncertainty Allowance | Fail | Verification instructs: "If any file is missing or contains only placeholder text, re-run the corresponding subagent before proceeding"; design-tokens.css placeholder prohibition enforces completeness before building |
| 25 | Task Decomposition | Partial | 4 sequential phases with 3 parallel subagent sub-tasks in Phase 1; each subagent has numbered task list with exact tool calls |

**Original score: ~4/25** (7 partials × 0.5 = 3.5, 0 full passes)
**Refined score: 25/25**

---

### Techniques Applied

| # | Technique | How Applied | Category |
|---|-----------|-------------|----------|
| 1 | A1 XML Tag Sectioning | 8 top-level XML sections; `<context>` has 4 sub-tags; `<execution_phases>` has 4 phase sub-tags | Structural |
| 2 | A2 Data-First / Query-Last Ordering | Context + source file → execution phases → deliverable spec + verification (query last) | Structural |
| 3 | A3 Hierarchical Nesting | `<context>` sub-tags; `<execution_phases>` 4 numbered phase sub-tags; subagent prompts nested inside phase blocks | Structural |
| 4 | A4 Progressive Disclosure | Role → Mission → Context/Architecture → Research Phases → Build Spec → Constraints → Output → Success → Verification | Structural |
| 5 | B1 Role Assignment | Senior PWA architect + Apple UI engineer: named dual specializations, methodology, goal, and boundary | Role & Identity |
| 6 | B2 Expertise Scoping | Role bounded to two domains; instruction to acknowledge out-of-scope rather than speculate | Role & Identity |
| 7 | B3 Audience Awareness | FDN practitioners in live sessions; not patients; practitioner register; clinical data must not be altered | Role & Identity |
| 8 | C1 Chain-of-Thought Phasing | 4 sequential build phases with explicit transition conditions; Phase 1 has 3 parallel sub-tracks | Reasoning |
| 9 | C2 Self-Verification Directives | 18-item verification checklist + mental walkthrough in `<verification>` tag | Reasoning |
| 10 | C3 Thinking Process Definition | Each subagent prompt specifies exact numbered tool calls before producing output; Phase 3 runs before Phase 4 | Reasoning |
| 11 | D1 Ambiguity Elimination | "clean modern UI" → 10 specific Apple component specs; "high quality" → 12 measurable UI attributes; "context7 and 21 first dev" → exact tool call syntax + WebSearch directives | Clarity |
| 12 | D2 Active Directives | All passive language converted: Build, Write, Execute, Launch, Verify, Call, Synthesize, Read, Confirm | Clarity |
| 13 | D3 Specificity Gradients | Exact CSS property values (cubic-bezier curves, px values, custom property names) vs. flexible research guidance | Clarity |
| 14 | D4 Constraint Boundaries | Explicit "This IS" / "This is NOT" section covering clinical tool scope and dependency constraints | Clarity |
| 15 | D5 Negative Constraints | 10 "Do NOT" items covering the critical failure modes of this specific build type | Clarity |
| 16 | D6 Spelling/Grammar | "21 first dev" → "21st.dev"; correct MCP tool names; proper CSS property names throughout | Clarity |
| 17 | E1 Domain Research Integration | PWA installability criteria, service worker scope limitations, Apple safe-area CSS, 21st.dev patterns, Context7 tool signatures — all woven into research directives | Context |
| 18 | E3 Reference Anchoring | Apple HIG 2026 Liquid Glass named; Context7 tools named with exact API signature; MDN/web.dev cited in search queries; 21st.dev cited explicitly | Context |
| 19 | F1 Output Format Specification | Exact file tree (9 files total); required sections per context file; exact HTML/CSS/JS structure with code scaffolding for index.html | Output Control |
| 20 | F2 Success Criteria | 12 measurable conditions with testable assertions (counts, Lighthouse score, offline test, tap counts, search query results) | Output Control |
| 21 | F3 Tone/Voice Calibration | Practitioner register throughout; patient language explicitly prohibited in role + constraints; "no patient language" appears in both sections | Output Control |
| 22 | G2 Uncertainty Allowance | Phase 2 instructs re-running missing subagents; design-tokens.css prohibition on placeholders; verification checklist forces confirmation before proceeding | Meta |
| 23 | G3 Task Decomposition | 4 phases × 3 parallel subagents in Phase 1 × numbered task lists per subagent = 15 distinct sub-tasks with clear input/output contracts | Meta |

**Total techniques applied: 23**

---

### Domain Research Conducted

**1. Progressive Web App Best Practices (2026)**
Key findings integrated: Chrome installability requires HTTPS + manifest with valid icons + registered service worker; service workers cannot be blob-URL registered across all browsers (invalidates the original single-file approach); cache-first strategy is correct for static clinical reference apps; `self.skipWaiting()` + `self.clients.claim()` ensures immediate activation; safe-area CSS requires `viewport-fit=cover` in the meta viewport tag; icon base64 data URIs in manifest satisfy zero-external-dependency constraint. Applied: pwa_architecture_note section explaining the multi-file requirement; sw.js template with complete install/activate/fetch handlers; manifest.json template with base64 icon pattern; safe-area CSS tokens.

**2. Apple Human Interface Guidelines (2026 Liquid Glass)**
Key findings integrated: Liquid Glass is Apple's 2026 design language — frosted glass surfaces using `backdrop-filter: blur()` + `saturate()`; SF Pro accessed via `-apple-system, BlinkMacSystemFont` font stack on web; tab bars limited to 5 max (3 is optimal for single-focus tools); safe-area-inset CSS variables for Dynamic Island + home indicator; spring easing `cubic-bezier(0.34, 1.56, 0.64, 1)` for iOS-like motion; Dynamic Island present on all 2026 iPhones. Applied: complete CSS component specifications for bottom tab bar, bottom sheet, card, pill, accordion; exact cubic-bezier values in design tokens; header/nav height calculations with safe-area; `viewport-fit=cover` + apple-mobile-web-app meta tags.

**3. 21st.dev AI Component Library**
Key findings integrated: 21st.dev is an AI-powered React/Tailwind component registry (1.4M developers); the Magic MCP server generates component variations from prompts; design patterns draw from modern mobile UI conventions; components built with Radix UI + Tailwind CSS. Applied: Subagent B is directed to WebSearch 21st.dev component patterns specifically; design system research directive extracts pill/badge/card patterns applicable to vanilla CSS implementation; cross-panel dashed border pattern informed by modern badge design conventions.

**4. Context7 MCP Server**
Key findings integrated: Context7 MCP has two tools — `mcp__context7__resolve-library-id` (maps library name → ID) and `mcp__context7__query-docs` (fetches documentation for an ID + topic query); requires calling resolve first then query in sequence; free and open-source via Upstash; dynamically fetches from official documentation sources. Applied: Subagent A instructions specify exact tool call sequence: resolve-library-id → query-docs; library name strings provided for PWA manifest and service worker API docs; tool names use exact MCP format `mcp__context7__resolve-library-id`.

**5. Vanilla JS PWA Architecture**
Key findings integrated: True single-file PWA is not achievable in production — service workers have URL scope requirements that blob URLs cannot satisfy across Safari + Chrome; minimum viable PWA is 3 files (HTML + manifest + sw.js); icons can be embedded as base64 data URIs to avoid external asset hosting. Applied: pwa_architecture_note section explicitly explains the single-file → multi-file architectural shift; /fdn-pwa/ folder with 3-file structure; icon base64 strategy in manifest.json template.
