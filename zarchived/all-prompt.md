# FDN Symptom Navigator — Mobile PWA Build Prompt

> Refined with Apple HIG 2026 Liquid Glass design language, iOS dark mode design tokens, PWA technical architecture, and complete FDN clinical data layer. Research files in /context/ folder.

---

```xml
<role>
You are a senior PWA architect and Apple-quality mobile UI engineer specializing in zero-dependency multi-file progressive web apps optimized for mobile clinical reference use. You combine deep expertise in:
- Vanilla JavaScript PWA architecture: Web App Manifest, Service Worker lifecycle, Cache Storage API, offline-first cache-first strategy
- Apple Human Interface Guidelines (2026 Liquid Glass design language): frosted glass surfaces, SF Pro system font, spring easing curves, safe-area insets, 44px touch targets, bottom sheet patterns, tab bar conventions
- Clinical reference tool UX: information density, 3-tap lookup flows, practitioner-facing copy, symptom-to-root-cause tracing
- FDN (Functional Diagnostic Nutrition) methodology: lab panel relationships, cross-panel constructs, HPA Axis 5-phase model, root cause cluster logic

Your expertise is bounded to: PWA frontend engineering for zero-dependency multi-file tools, and functional medicine reference tool design. If the task veers outside these domains, acknowledge the boundary rather than speculating.
</role>

<context>
## Project Brief
Build a multi-file progressive web app (PWA) — installable, offline-first, Apple-quality mobile UI — for an FDN (Functional Diagnostic Nutrition) practitioner knowledge system. All data is provided in the knowledge base below: 76 validated symptom entries across 14 categories, 28 lab marker variables, 5 root cause clusters, and their interconnections. The app must install to a phone's home screen and function completely offline after first load.

## Target Audience
FDN practitioners and trained health coaches using this tool during active client sessions. They are NOT patients — they already know what Cortisol Diurnal Pattern, Beta-glucuronidase, and HPA Axis Dysregulation mean. Their workflow: a client describes a symptom → practitioner opens tool → taps symptom → sees variable-cluster map → drills into specific variables for mechanistic detail. The entire lookup must complete in 3 taps or fewer.

## FDN Methodology Context
Encode this understanding into the tool's logic and copy:
- **Pattern over individual markers**: Convey marker relationships, not just flat lists. The tool must make cross-variable connections visually obvious.
- **HPA Axis Dysregulation has 5 progressive phases**: Alarm → Resistance → Exhaustion → Collapse → Recovery. Reference these phase names when displaying HPA-related symptoms and variables.
- **Pregnenolone Steal is a downstream mechanism**, not a direct lab value. Its variable card must reflect this distinction explicitly.
- **Cross-panel constructs** (Systemic Oxidative Stress Cascade, Hepatic Detoxification Impairment, Histamine-DAO Regulatory System, HPA Axis Dysregulation Pattern, Pregnenolone Steal and Steroidogenesis Disruption) amplify all other dysfunction simultaneously. Visually distinguish them with dashed borders and the CROSS-PANEL AMPLIFIER badge.
- **H. pylori is the highest-priority pathogen**: Any symptom screen listing H. pylori must surface a prominent red alert banner: "⚠ Treat H. pylori before addressing other findings."
- **Cluster E requires immediate medical referral**: Calprotectin/Lactoferrin elevation and Occult Blood >10 µg/g are referral triggers, not FDN intervention triggers.

## Technical Mandate
Multi-file PWA in a /fdn-pwa/ output folder. Three required files: index.html (app shell + all inline CSS + all JS + embedded DATA object), manifest.json (Web App Manifest for installability), sw.js (Service Worker for offline cache-first operation). No external dependencies, no CDN, no frameworks, no fetch calls to APIs. Max-width 430px, centered on desktop. All FDN data embedded as a JS DATA object in the script tag. Loads instantly. Works fully offline after first load. Lighthouse PWA score target >= 90.
</context>

<design_system>
## Design Philosophy
Apply Apple's three core principles to this dark clinical tool:
- **Clarity**: Every element has a clear purpose. Panel colors and cluster colors are not decorative — they encode clinical identity and must always be present on pills and tags.
- **Deference**: The UI recedes so clinical data leads. Surfaces use translucent frosted glass rather than opaque competing backgrounds. Typography hierarchy directs the eye.
- **Depth**: Bottom sheets create a sense of layered navigation. The home screen recedes behind detail screens. Motion communicates hierarchy.

## CSS Design Tokens
Embed these custom properties verbatim in the :root {} block at the top of the style block in index.html. Do not alter any value.

```css
:root {
  /* Safe Areas */
  --safe-top:    env(safe-area-inset-top, 0px);
  --safe-right:  env(safe-area-inset-right, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left:   env(safe-area-inset-left, 0px);

  /* Backgrounds - iOS UIColor dark mode equivalents */
  --bg-primary:   #000000;
  --bg-secondary: #1C1C1E;
  --bg-tertiary:  #2C2C2E;
  --bg-glass:     rgba(28, 28, 30, 0.72);

  /* Text */
  --text-primary:   rgba(255, 255, 255, 1.0);
  --text-secondary: rgba(255, 255, 255, 0.55);
  --text-tertiary:  rgba(255, 255, 255, 0.35);

  /* Separators */
  --separator:        rgba(255, 255, 255, 0.12);
  --separator-opaque: #3A3A3C;

  /* Accent */
  --accent:             #007AFF;
  --accent-destructive: #FF3B30;

  /* FDN Panel Colors - preserve exactly */
  --panel-mwp:   #e07c3a;
  --panel-mba:   #3abde0;
  --panel-shp:   #8b5cf6;
  --panel-gimap: #22c55e;
  --panel-cross: #94a3b8;

  /* FDN Cluster Colors - preserve exactly */
  --cluster-a: #ef4444;
  --cluster-b: #f97316;
  --cluster-c: #ec4899;
  --cluster-d: #06b6d4;
  --cluster-e: #fbbf24;

  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif;
  --text-xs:   0.6875rem;
  --text-sm:   0.8125rem;
  --text-base: 1rem;
  --text-md:   1.0625rem;
  --text-lg:   1.25rem;
  --text-xl:   1.5rem;
  --text-2xl:  2rem;
  --weight-regular:  400;
  --weight-medium:   500;
  --weight-semibold: 600;
  --weight-bold:     700;
  --tracking-tight:  -0.02em;
  --tracking-normal:  0em;
  --tracking-wide:    0.03em;
  --tracking-caps:    0.06em;

  /* Spacing - 4px base grid */
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

  /* Shadows - dark-background-optimized */
  --shadow-0: none;
  --shadow-1: 0 1px 2px rgba(0,0,0,0.4), 0 0px 1px rgba(0,0,0,0.3);
  --shadow-2: 0 4px 12px rgba(0,0,0,0.5), 0 1px 3px rgba(0,0,0,0.4);
  --shadow-3: 0 16px 40px rgba(0,0,0,0.6), 0 4px 12px rgba(0,0,0,0.5), 0 1px 3px rgba(0,0,0,0.4);

  /* Motion */
  --ease-spring:   cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-snap:     cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  --duration-fast:   150ms;
  --duration-normal: 300ms;
  --duration-slow:   450ms;

  /* Layout */
  --touch-target:  44px;
  --max-width:    430px;
  --nav-height:   calc(60px + var(--safe-bottom));
  --header-height: calc(52px + var(--safe-top));
}
```

## Component CSS Specifications

### Bottom Tab Bar (Frosted Glass)
```css
.tab-bar {
  position: fixed; bottom: 0; left: 0; right: 0;
  max-width: var(--max-width); margin: 0 auto;
  height: var(--nav-height); padding-bottom: var(--safe-bottom);
  display: flex; align-items: stretch;
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid var(--separator); z-index: 100;
}
.tab-item {
  flex: 1; display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: var(--space-1);
  min-height: var(--touch-target); min-width: var(--touch-target);
  border: none; background: transparent; cursor: pointer;
  color: var(--text-tertiary);
  font-family: var(--font-family); font-size: var(--text-xs); font-weight: var(--weight-medium);
  transition: color var(--duration-fast) var(--ease-standard);
  -webkit-tap-highlight-color: transparent;
}
.tab-item[aria-selected="true"] { color: var(--accent); }
```

### Top Header (Frosted Glass, Safe-Area-Aware)
```css
.top-header {
  position: sticky; top: 0; z-index: 90;
  height: var(--header-height); padding-top: var(--safe-top);
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid var(--separator);
}
.top-header-inner {
  height: 52px; display: flex; align-items: center;
  justify-content: space-between; padding: 0 var(--space-4);
}
.header-title {
  font-size: var(--text-lg); font-weight: var(--weight-semibold);
  color: var(--text-primary); letter-spacing: var(--tracking-tight);
}
```

### Bottom Sheet (Spring Slide-Up)
```css
.bottom-sheet {
  position: fixed; inset: 0; top: auto;
  max-height: 92dvh; z-index: 201;
  background: var(--bg-secondary);
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  box-shadow: var(--shadow-3);
  display: flex; flex-direction: column;
  overflow-y: auto; overscroll-behavior: contain;
  -webkit-overflow-scrolling: touch;
  padding-bottom: var(--safe-bottom);
  transform: translateY(100%);
  transition: transform var(--duration-slow) var(--ease-spring);
}
.bottom-sheet.is-open { transform: translateY(0); }
.sheet-drag-indicator {
  width: 36px; height: 5px;
  background: var(--separator-opaque); border-radius: var(--radius-full);
  margin: var(--space-2) auto var(--space-1); flex-shrink: 0;
}
```

### List Row (Symptom / Result)
```css
.list-row {
  display: flex; align-items: center; justify-content: space-between;
  min-height: var(--touch-target); min-width: var(--touch-target);
  padding: var(--space-3) var(--space-4);
  background: var(--bg-secondary); border-bottom: 1px solid var(--separator);
  cursor: pointer; -webkit-tap-highlight-color: transparent;
  transition: background var(--duration-fast) var(--ease-standard),
              transform var(--duration-fast) var(--ease-standard);
}
.list-row:active { transform: scale(0.98); background: var(--bg-tertiary); }
```

### Variable Pill (Panel-Colored)
```css
.var-pill {
  display: inline-flex; align-items: center; justify-content: center;
  min-height: 28px; min-width: var(--touch-target);
  padding: var(--space-1) var(--space-3); border-radius: var(--radius-full);
  background: var(--panel-color); color: #000000;
  font-family: var(--font-family); font-size: var(--text-sm);
  font-weight: var(--weight-semibold); white-space: nowrap;
  cursor: pointer; -webkit-tap-highlight-color: transparent;
  transition: opacity var(--duration-fast), transform var(--duration-fast) var(--ease-spring);
}
.var-pill:active { opacity: 0.75; transform: scale(0.96); }
.var-pill--cross {
  background: transparent; border: 2px dashed var(--panel-color); color: var(--panel-color);
}
```

### Cluster Tag
```css
.cluster-tag {
  display: inline-flex; align-items: center; justify-content: center;
  min-height: 28px; min-width: var(--touch-target);
  padding: var(--space-1) var(--space-3); border-radius: var(--radius-sm);
  background: var(--cluster-color); color: #000000;
  font-family: var(--font-family); font-size: var(--text-sm);
  font-weight: var(--weight-semibold); white-space: nowrap;
  cursor: pointer; -webkit-tap-highlight-color: transparent;
  transition: opacity var(--duration-fast);
}
.cluster-tag:active { opacity: 0.75; }
```

### Alert Banner (H. pylori / Medical Referral)
```css
.alert-banner {
  width: 100%; padding: var(--space-4); border-radius: var(--radius-md);
  display: flex; align-items: flex-start; gap: var(--space-3);
}
.alert-banner--destructive {
  background: rgba(255, 59, 48, 0.15); border: 1px solid #FF3B30; color: #FF3B30;
}
.alert-title { font-weight: var(--weight-semibold); font-size: var(--text-base); }
```

### Accordion Section Header
```css
.accordion-header {
  display: flex; align-items: center; justify-content: space-between;
  min-height: var(--touch-target); min-width: var(--touch-target);
  width: 100%; padding: var(--space-3) var(--space-4);
  background: var(--bg-secondary); border: none;
  border-bottom: 1px solid var(--separator); cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}
.accordion-title { font-size: var(--text-base); font-weight: var(--weight-semibold); color: var(--text-primary); }
.accordion-chevron {
  transition: transform var(--duration-normal) var(--ease-snap);
  display: inline-block; color: var(--text-tertiary);
}
.accordion-header[aria-expanded="true"] .accordion-chevron { transform: rotate(90deg); }
.accordion-badge {
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 20px; height: 20px; padding: 0 6px; border-radius: var(--radius-full);
  background: var(--accent); color: #fff; font-size: var(--text-xs); font-weight: var(--weight-semibold);
}
```

### Search Bar (iOS Style)
```css
.search-bar {
  display: flex; align-items: center; gap: var(--space-2);
  background: var(--bg-tertiary); border-radius: var(--radius-full);
  min-height: var(--touch-target); padding: var(--space-2) var(--space-4);
  border: 1px solid transparent; transition: border-color var(--duration-fast);
}
.search-bar:focus-within { border-color: var(--separator-opaque); }
.search-input {
  flex: 1; background: transparent; border: none; outline: none;
  color: var(--text-primary); font-family: var(--font-family); font-size: var(--text-base);
  -webkit-appearance: none; appearance: none;
}
.search-input::placeholder { color: var(--text-tertiary); }
```
</design_system>

<pwa_architecture>
## Why Three Files (Not One)
A true PWA cannot be a single HTML file:
- **Service Workers** must be registered at a real URL with their own HTTP scope. Blob: URL service workers are not accepted by Safari 16+ or Chrome and do not persist across sessions.
- **Web App Manifest** must be fetched as a separate HTTP resource by Chrome's installability checker. Data: URI manifests are not reliably supported.
- **Minimum viable PWA**: index.html + manifest.json + sw.js

Icons can be embedded as base64 data URIs inside manifest.json to satisfy zero-external-dependency constraint while remaining installable.

## manifest.json Requirements
```json
{
  "name": "FDN Symptom Navigator",
  "short_name": "FDN Nav",
  "description": "FDN lab marker reference tool for clinical practitioners",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "#000000",
  "background_color": "#000000",
  "categories": ["medical", "health", "productivity"],
  "icons": [
    { "src": "data:image/png;base64,[192x192 valid base64 PNG]", "sizes": "192x192", "type": "image/png", "purpose": "any maskable" },
    { "src": "data:image/png;base64,[512x512 valid base64 PNG]", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }
  ]
}
```
Generate actual valid PNG base64 strings for icons. A simple dark background with "FDN" text is acceptable.

## sw.js Pattern
```javascript
const CACHE_NAME = 'fdn-nav-v1';
const ASSETS = ['./index.html', './manifest.json', './sw.js'];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)));
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
  if (event.request.method !== 'GET') return;
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

## index.html Head Requirements
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="FDN Nav">
  <meta name="theme-color" content="#000000">
  <title>FDN Symptom Navigator</title>
  <link rel="manifest" href="./manifest.json">
  <style>/* All CSS here */</style>
</head>
```

## Service Worker Registration
Place immediately after the DATA object, before state definition:
```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js').catch(console.error);
}
```
</pwa_architecture>

<knowledge_base>
## KNOWLEDGE SYSTEM OVERVIEW

76 FDN symptom entries across 14 categories. 28 lab marker variables organized across 5 panels:
- MWP (Metabolic Wellness Panel): Indican, Urinary Bile Acids, 8-OHdG
- MBA (Mucosal Barrier Assessment): Histamine-MBA, DAO, Zonulin
- SHP (Stress Hormone Panel): Cortisol Diurnal Pattern, DHEA, Testosterone, Estradiol, Progesterone, Melatonin, sIgA-SHP
- GI-MAP: H. pylori, Candida, Parasites, Dysbiotic Bacteria, Commensal Bacteria, Calprotectin/Lactoferrin, Beta-glucuronidase, Anti-gliadin IgA, sIgA-GI, Occult Blood
- Cross-panel constructs: Systemic Oxidative Stress Cascade, Hepatic Detoxification Impairment, Histamine-DAO Regulatory System, HPA Axis Dysregulation Pattern, Pregnenolone Steal and Steroidogenesis Disruption

Five root cause clusters:
- Cluster A — GI Ecosystem Collapse (Primary Driver)
- Cluster B — HPA-Immune Loop (Amplifier)
- Cluster C — Estrogen Recycling Loop (Cross-Panel)
- Cluster D — Mucosal Barrier Breakdown (Histamine)
- Cluster E — Structural GI Pathology (Medical Referral)

---

## SYMPTOM-TO-VARIABLE MAPPING

Encode the following symptom library exactly. Each symptom links to every variable that can produce it and every root cause cluster involved.

### ENERGY & FATIGUE
- "Always tired" → Cortisol Diurnal Pattern, DHEA, HPA Axis Dysregulation, sIgA-SHP, Indican, 8-OHdG, Hepatic Detox Impairment | Clusters A, B
- "Afternoon energy crash" → Cortisol Diurnal Pattern, Blood Glucose Dysregulation, Indican | Cluster B
- "Can't get out of bed in the morning" → Cortisol Diurnal Pattern, DHEA, Melatonin | Cluster B
- "Wired but tired" → Cortisol Diurnal Pattern, HPA Axis Dysregulation, Melatonin | Cluster B
- "Exercise makes me worse" → 8-OHdG, Systemic Oxidative Stress Cascade, DHEA, Cortisol | Clusters A, B
- "No motivation or drive" → DHEA, Testosterone, HPA Axis Dysregulation, Indican (neurotransmitter depletion) | Clusters A, B

### SLEEP
- "Can't fall asleep" → Melatonin, Cortisol Diurnal Pattern, HPA Axis Dysregulation, Histamine-MBA | Clusters B, D
- "Wake up between 1-3am" → Cortisol Diurnal Pattern, Blood Glucose Dysregulation, Hepatic Detox Impairment | Clusters A, B
- "Never feel rested" → Melatonin, Cortisol Diurnal Pattern, 8-OHdG, Histamine-MBA | Clusters B, D
- "Vivid dreams or nightmares" → HPA Axis Dysregulation, Cortisol Diurnal Pattern | Cluster B
- "Need 10+ hours and still tired" → HPA Axis Dysregulation Exhaustion Phase, DHEA, sIgA-SHP | Cluster B

### MOOD & EMOTIONS
- "Anxiety" → Histamine-MBA, DAO, HPA Axis Dysregulation, Indican (tryptophan depletion → serotonin deficit), Zonulin (LPS-driven neuroinflammation), Cortisol | Clusters A, B, D
- "Depression" → Indican (neurotransmitter depletion via tryptophan theft), HPA Axis Dysregulation, DHEA, Testosterone, 8-OHdG, Systemic Oxidative Stress Cascade | Clusters A, B
- "Irritability / short fuse" → Histamine-MBA, Cortisol Diurnal Pattern, Blood Glucose Dysregulation, HPA Axis Dysregulation | Clusters B, D
- "Emotional numbness" → HPA Axis Dysregulation Exhaustion Phase, DHEA, Cortisol (flat pattern) | Cluster B
- "Overwhelm / can't cope with stress" → HPA Axis Dysregulation, sIgA-SHP, Cortisol:DHEA ratio, Pregnenolone Steal | Cluster B
- "Mood swings" → Estradiol, Progesterone, Cortisol Diurnal Pattern, Histamine-MBA, Blood Glucose Dysregulation | Clusters B, C, D
- "Brain fog" → Zonulin (LPS translocation), Indican (amino acid depletion), 8-OHdG, Hepatic Detox Impairment, Histamine-MBA, DAO | Clusters A, B, D
- "Poor memory" → Indican (tryptophan/neurotransmitter depletion), 8-OHdG, Systemic Oxidative Stress Cascade, HPA Axis Dysregulation | Clusters A, B
- "Feeling disconnected from yourself" → HPA Axis Dysregulation Collapse Phase, sIgA-SHP, Cortisol flat pattern | Cluster B

### DIGESTION
- "Bloating" → Indican (SIBO/dysbiosis), H. pylori, Candida, Dysbiotic Bacteria, DAO-low, Histamine-MBA, Anti-gliadin IgA, sIgA-GI | Clusters A, D
- "Gas / flatulence (especially foul-smelling)" → Indican (putrefactive dysbiosis), H. pylori, Dysbiotic Bacteria, Parasites | Cluster A
- "Constipation" → Indican (hypomotility signal), Urinary Bile Acids (low = poor bile flow), Dysbiotic Bacteria, Cortisol | Clusters A, B
- "Diarrhea" → H. pylori, Parasites, Candida, Calprotectin/Lactoferrin, Zonulin, sIgA-GI | Clusters A, D, E
- "Alternating constipation and diarrhea" → H. pylori, Dysbiotic Bacteria, Zonulin, sIgA-GI, Indican | Clusters A, D
- "Heartburn / reflux" → H. pylori (disrupts gastric acid), Indican (hypochlorhydria signal), Urinary Bile Acids | Cluster A
- "Nausea" → H. pylori, Parasites, Histamine-MBA, Urinary Bile Acids (high) | Clusters A, D
- "Food feels like it just sits there" → Indican (hypomotility), H. pylori, Urinary Bile Acids (low bile flow) | Cluster A
- "Stomach pain / cramping" → H. pylori, Parasites, Calprotectin/Lactoferrin, Histamine-MBA, Zonulin | Clusters A, D, E
- "Can't eat without feeling sick" → H. pylori, Anti-gliadin IgA, Zonulin, DAO-low, Histamine load | Clusters A, D

### FOOD REACTIONS
- "Reactions to many foods" → Zonulin (leaky gut → systemic antigen load), DAO-low, Histamine-MBA, Anti-gliadin IgA, sIgA-GI, MRT reactive foods | Clusters A, D
- "Gluten sensitivity" → Anti-gliadin IgA, Zonulin, sIgA-GI (interpretation dependency), Histamine-MBA | Clusters A, D
- "Dairy reactions" → Anti-gliadin IgA (cross-reactive: dairy shares gliadin homology), Zonulin, DAO | Clusters A, D
- "Histamine-rich food reactions (wine, aged cheese, fermented foods)" → Histamine-MBA, DAO, Histamine-DAO Regulatory System | Cluster D
- "Getting worse after eating fermented foods or probiotics" → Histamine-MBA, DAO-low, SIBO (Indican) | Cluster D

### SKIN
- "Hives / urticaria" → Histamine-MBA, DAO-low, Zonulin, Histamine-DAO Regulatory System | Cluster D
- "Eczema / rashes" → Histamine-MBA, Zonulin (leaky gut antigen load), Anti-gliadin IgA, sIgA-GI | Clusters A, D
- "Flushing / redness (especially face)" → Histamine-MBA, DAO-low, Estradiol | Clusters C, D
- "Itching (no visible rash)" → Histamine-MBA, DAO, Urinary Bile Acids (high — bile salt itch) | Clusters A, D
- "Acne" → Estradiol (elevated), Progesterone (low), Beta-glucuronidase, HPA Axis Dysregulation, Hepatic Detox Impairment | Clusters B, C
- "Skin that ages fast" → 8-OHdG, Systemic Oxidative Stress Cascade | Clusters A, B

### IMMUNE SYSTEM
- "Get sick constantly" → sIgA-SHP (low), sIgA-GI (low), HPA Axis Dysregulation, Cortisol (immune suppression) | Clusters A, B
- "Take forever to recover from illness" → sIgA-SHP, DHEA, Systemic Oxidative Stress Cascade, Hepatic Detox Impairment | Clusters A, B
- "Allergies getting worse over time" → sIgA-GI, Zonulin, Histamine-MBA, DAO | Clusters A, D
- "Autoimmune condition or suspicion" → Zonulin (sustained TJ disassembly → antigen translocation → autoimmune activation), 8-OHdG, Systemic Oxidative Stress Cascade | Clusters A, B
- "Frequent UTIs, yeast infections, or infections" → Candida, sIgA-GI (low), HPA Axis Dysregulation, Cortisol | Clusters A, B

### HORMONAL (FEMALE)
- "PMS / PMDD" → Estradiol (elevated), Progesterone (low), Beta-glucuronidase (recycling estrogen), HPA Axis Dysregulation, Cortisol:DHEA ratio | Clusters B, C
- "Irregular periods" → Estradiol, Progesterone, Cortisol, HPA Axis Dysregulation, Pregnenolone Steal | Clusters B, C
- "Heavy periods" → Estradiol (elevated), Progesterone (low), Beta-glucuronidase | Cluster C
- "Low libido" → Testosterone (low), DHEA, HPA Axis Dysregulation, Pregnenolone Steal, Indican (amino acid depletion) | Clusters A, B
- "Hot flashes" → Estradiol dysregulation, Histamine-MBA (histamine triggers vasodilation), Progesterone (low), HPA Axis Dysregulation | Clusters B, C, D
- "Infertility or difficulty conceiving" → Progesterone (low), Estradiol imbalance, HPA Axis Dysregulation, Pregnenolone Steal, Beta-glucuronidase | Clusters B, C
- "Estrogen dominance symptoms (weight in hips, painful breasts, water retention)" → Estradiol (elevated), Beta-glucuronidase (recycling), Progesterone (low), Hepatic Detox Impairment | Cluster C

### HORMONAL (MALE & SHARED)
- "Low testosterone symptoms (low drive, muscle loss, fatigue)" → Testosterone (low), DHEA, HPA Axis Dysregulation, Pregnenolone Steal, Indican | Clusters A, B
- "Can't build or maintain muscle" → Testosterone (low), DHEA, Cortisol (catabolic), HPA Axis Dysregulation | Cluster B
- "Weight gain despite diet/exercise" → Cortisol (elevated, promotes fat storage), Estradiol (elevated via B-GUS recycling), Indican (metabolic disruption), Urinary Bile Acids | Clusters A, B, C

### CARDIOVASCULAR & CIRCULATORY
- "Heart palpitations / racing heart" → Histamine-MBA (cardiac H2 receptor activation), DAO-low, Cortisol, HPA Axis Dysregulation | Clusters B, D
- "Low blood pressure / dizziness on standing" → HPA Axis Dysregulation Exhaustion Phase, DHEA (low), Cortisol (flat) | Cluster B
- "High blood pressure" → Cortisol (elevated), Histamine-MBA (vasoconstriction paradox), Systemic Oxidative Stress Cascade | Clusters B, D

### PAIN & INFLAMMATION
- "Joint pain" → Zonulin (antigen translocation → immune complex deposition), 8-OHdG, Systemic Oxidative Stress Cascade, DAO-low | Clusters A, D
- "Muscle aches without exertion" → Systemic Oxidative Stress Cascade, 8-OHdG, HPA Axis Dysregulation, Cortisol (catabolic) | Clusters A, B
- "Headaches" → Histamine-MBA (vasodilation), DAO-low, Zonulin, Indican (neurotransmitter depletion), Cortisol | Clusters A, B, D
- "Migraines" → Histamine-MBA, DAO-low, Estradiol (hormonal trigger), HPA Axis Dysregulation, Zonulin | Clusters B, C, D
- "Fibromyalgia-like symptoms" → 8-OHdG, Systemic Oxidative Stress Cascade, HPA Axis Dysregulation, Indican (amino acid depletion) | Clusters A, B
- "Chronic pain" → Systemic Oxidative Stress Cascade, 8-OHdG, Zonulin, HPA Axis Dysregulation | Clusters A, B

### RESPIRATORY
- "Stuffy nose / runny nose (not seasonal)" → Histamine-MBA, DAO-low, Zonulin (antigen translocation), Anti-gliadin IgA | Clusters A, D
- "Asthma-like symptoms" → Histamine-MBA (H1 bronchospasm), DAO-low, Zonulin | Cluster D
- "Post-nasal drip" → Histamine-MBA, DAO, Zonulin | Cluster D

### COGNITIVE & NEUROLOGICAL
- "Difficulty concentrating" → Indican (tryptophan/neurotransmitter depletion), 8-OHdG, Histamine-MBA, Zonulin (LPS neuroinflammation) | Clusters A, D
- "Word-finding problems" → 8-OHdG, Systemic Oxidative Stress Cascade, Indican, Zonulin | Clusters A, B
- "Sensitivity to light or sound" → Histamine-MBA, DAO-low, HPA Axis Dysregulation | Clusters B, D
- "Tingling or numbness" → 8-OHdG (nerve oxidative damage), Systemic Oxidative Stress Cascade | Cluster A

### STRESS & NERVOUS SYSTEM
- "Can't handle stress the way I used to" → HPA Axis Dysregulation (Phase 3+ Exhaustion), Cortisol:DHEA ratio, sIgA-SHP, DHEA (low) | Cluster B
- "Burnout" → HPA Axis Dysregulation Exhaustion/Collapse Phase, Cortisol (flat), DHEA, sIgA-SHP | Cluster B
- "Panic attacks" → Histamine-MBA (acute vasoactive release), HPA Axis Dysregulation, Cortisol | Clusters B, D
- "Feel like I can't relax" → HPA Axis Dysregulation, Cortisol (elevated), Histamine-MBA, Melatonin (low) | Clusters B, D

---

## VARIABLE REFERENCE PANEL

Build the following variable detail cards with exact data:

Indican | Signals SIBO, dysbiosis, protein maldigestion | High: bacterial overgrowth stealing tryptophan, liver burden | Low: n/a | Clusters A | Connects to: Urinary Bile Acids, 8-OHdG, Zonulin, Histamine-MBA, DAO, sIgA-SHP

Urinary Bile Acids | Liver detoxification throughput marker | High: liver congestion, toxin overload | Low: poor bile flow, gallbladder dysfunction, IBD | Cluster A | Connects to: Hepatic Detoxification Impairment

8-OHdG | DNA oxidative damage biomarker | High: oxidative stress exceeding repair = accelerated aging, cancer risk | Low: n/a | Cluster A | Connects to: Systemic Oxidative Stress Cascade

Zonulin | Intestinal tight junction regulator | High: leaky gut, antigen translocation, autoimmune risk | Low: n/a | Clusters A, D | Connects to: Histamine-MBA, DAO, sIgA-SHP, 8-OHdG

Histamine-MBA | Biogenic amine: immune, vascular, neural functions | High: excess production or impaired degradation | Low: n/a | Cluster D | Connects to: DAO, Zonulin, Histamine-DAO Regulatory System

DAO | Histamine-degrading enzyme, mucosal integrity proxy | High: early injury compensatory upregulation | Low: chronic mucosal destruction, IBD | Cluster D | Connects to: Histamine-DAO Regulatory System

sIgA-SHP | Salivary mucosal immune defense | High: active acute immune challenge | Low: cortisol suppression, chronic stress, immune collapse | Cluster B | Connects to: HPA Axis Dysregulation Pattern

HPA Axis Dysregulation Pattern | Adrenal stress response cascade — 5 phases: Alarm, Resistance, Exhaustion, Collapse, Recovery | Active/all phases: progressive cortisol dysregulation driving downstream immune, sex hormone, sleep deficits | Low: n/a (phase-dependent interpretation) | Cluster B | Connects to: Cortisol Diurnal Pattern, DHEA, sIgA-SHP, Pregnenolone Steal and Steroidogenesis Disruption | CROSS-PANEL CONSTRUCT

Pregnenolone Steal and Steroidogenesis Disruption | Downstream mechanism (not a direct lab value) — cortisol demand diverts pregnenolone away from DHEA and sex hormone synthesis | Active: DHEA, testosterone, and progesterone suppressed while cortisol is elevated | Low: n/a | Cluster B | Connects to: DHEA, Testosterone, Estradiol, Progesterone | CROSS-PANEL CONSTRUCT

Cortisol Diurnal Pattern | 4-point salivary cortisol arc measuring diurnal rhythm integrity | Flat: exhaustion/collapse | Elevated overall: acute/compensatory stress | Low overall: adrenal exhaustion | Cluster B

DHEA | Anabolic counterbalance to cortisol | High: n/a clinically significant | Low: catabolic dominance, immune suppression, aging acceleration | Cluster B

Testosterone | Anabolic hormone (male primary, female secondary role) | High: n/a in FDN context | Low: fatigue, low libido, muscle loss, depression | Cluster B

Estradiol | Primary estrogen | High: Cluster C estrogen recycling via elevated Beta-glucuronidase | Low: menopause, HPA-driven suppression | Cluster C

Progesterone | Anti-estrogenic, calming hormone | High: n/a | Low: anxiety, poor sleep, heavy periods, infertility | Cluster C

Melatonin | Circadian rhythm hormone | High (noon elevation): GI dysbiosis signal | Low: insomnia, poor antioxidant capacity | Cluster B

H. pylori | Ulcerogenic gastric pathogen — PRIORITY PATHOGEN | Positive: treat first — disrupts all other colonization resistance and gastric acid integrity | Negative: n/a | Cluster A

Candida | Opportunistic yeast | High/Elevated: dysbiosis, immune suppression | Low: n/a | Cluster A

Parasites | GI parasitic load | Positive: immune activation, barrier disruption | Negative: n/a | Cluster A

Dysbiotic Bacteria | Pathobiont bacterial overgrowth | Elevated: drives Indican production, Beta-glucuronidase activity, histamine excess | Low: n/a | Cluster A

Commensal Bacteria | Beneficial microbiome composition | High: n/a | Low: SCFA deficit, sIgA suppression, immune dysregulation | Cluster A

Calprotectin/Lactoferrin | Neutrophil-derived GI inflammation marker | Elevated: active IBD — distinguish from functional GI disorders; MEDICAL REFERRAL REQUIRED | Low: n/a | Cluster E

Beta-glucuronidase | Bacterial enzyme deconjugating Phase II estrogen metabolites | Elevated: estrogen recycling loop, hormone disruption, toxic recirculation | Low: n/a | Cluster C | Connects to: Estradiol, Hepatic Detoxification Impairment

Anti-gliadin IgA | Local mucosal immune response to gliadin | Elevated: gluten/cross-reactive food reactivity | Low with concurrent low sIgA-GI: likely false negative — interpret with caution | Cluster A | Connects to: sIgA-GI

sIgA-GI | Stool mucosal immune defense | High: acute immune challenge | Low: chronic pathogen load, dysbiosis, immune collapse | Clusters A, B

Occult Blood | Fecal hemoglobin — structural mucosal bleeding marker | >10 ug/g: MEDICAL REFERRAL REQUIRED IMMEDIATELY before FDN intervention | Low: n/a | Cluster E

Systemic Oxidative Stress Cascade | Overarching amplifier of all dysfunction across all panels | Active: accelerates every other dysregulation simultaneously | Low: n/a | All clusters | CROSS-PANEL CONSTRUCT

Hepatic Detoxification Impairment | Liver Phase I/II/III overwhelm | Active: toxin and hormone recirculation, bile acid spillover into systemic circulation | Low: n/a | Clusters A, C | CROSS-PANEL CONSTRUCT

Histamine-DAO Regulatory System | Functional balance of histamine load vs. DAO degradation capacity | Disrupted: histamine intolerance — interpret using Histamine:DAO ratio | Low: n/a | Cluster D | CROSS-PANEL CONSTRUCT

---

## ROOT CAUSE CLUSTER DEFINITIONS

Cluster A — GI Ecosystem Collapse (Primary Driver)
- Priority: Treat before all other clusters. GI dysfunction is the upstream driver of systemic dysfunction in the FDN model.
- Variables: Indican, Urinary Bile Acids, 8-OHdG, Zonulin, H. pylori, Candida, Parasites, Dysbiotic Bacteria, Commensal Bacteria, Anti-gliadin IgA, sIgA-GI, Hepatic Detoxification Impairment, Systemic Oxidative Stress Cascade
- Mechanism: Pathogenic overgrowth collapses colonization resistance → drives intestinal permeability (Zonulin) → antigen translocation → systemic immune activation + toxin recirculation → amplifies all downstream clusters

Cluster B — HPA-Immune Loop (Amplifier)
- Variables: Cortisol Diurnal Pattern, DHEA, Testosterone, Melatonin, sIgA-SHP, HPA Axis Dysregulation Pattern, Pregnenolone Steal and Steroidogenesis Disruption, sIgA-GI
- Mechanism: Chronic stress → cortisol dysregulation (5-phase HPA model) → immune suppression (down-sIgA) + sex hormone depletion via Pregnenolone Steal + circadian disruption (down-Melatonin) → self-perpetuating loop

Cluster C — Estrogen Recycling Loop (Cross-Panel)
- Variables: Estradiol, Progesterone, Beta-glucuronidase, Hepatic Detoxification Impairment
- Mechanism: Elevated Beta-glucuronidase → deconjugates Phase II estrogen metabolites in gut → estrogens re-enter circulation → estrogen dominance symptoms despite potentially normal production levels

Cluster D — Mucosal Barrier Breakdown (Histamine)
- Variables: Histamine-MBA, DAO, Zonulin, Histamine-DAO Regulatory System
- Mechanism: Mucosal destruction → DAO enzyme loss → histamine accumulates unmetabolized → vasoactive and neuroactive symptoms across cardiovascular, neurological, respiratory, and skin systems

Cluster E — Structural GI Pathology (Medical Referral)
- Variables: Calprotectin/Lactoferrin, Occult Blood
- Priority: MEDICAL REFERRAL REQUIRED. Elevated Calprotectin/Lactoferrin or Occult Blood >10 ug/g indicates structural GI pathology (IBD, bleeding lesion) that must be evaluated by a physician before FDN interventions proceed.

---

## COLOR SYSTEM

Panel colors (use for variable pills and panel badges):
- MWP (Metabolic Wellness Panel): #e07c3a (amber)
- MBA (Mucosal Barrier Assessment): #3abde0 (teal)
- SHP (Stress Hormone Panel): #8b5cf6 (purple)
- GI-MAP: #22c55e (green)
- Cross-panel constructs: #94a3b8 (slate)

Cluster tag colors:
- Cluster A: #ef4444 (red)
- Cluster B: #f97316 (orange)
- Cluster C: #ec4899 (pink)
- Cluster D: #06b6d4 (cyan)
- Cluster E: #fbbf24 (amber/warning)

App background: #000000 (iOS system background dark)
</knowledge_base>

<thinking_process>
Work through these phases in order before writing any files:

**Phase 1 — Data Architecture**
Design the complete JS DATA object structure:
- DATA.symptoms: keyed by slug ID → { label, category, variables: [ids], clusters: [letters], interpretation, mechanismTree }
- DATA.variables: keyed by slug ID → { name, panel, panelColor, elevated, low, connections: [ids], clusters: [letters], isCrossPanel, isPriorityPathogen, isMedicalReferral }
- DATA.clusters: keyed by cluster letter → { letter, name, fullName, color, mechanism, priorityNote, variables: [ids] }
- Build reverse maps programmatically from DATA.symptoms — do NOT hardcode

**Phase 2 — PWA File Architecture**
Confirm the 3-file structure before any DOM work. Verify manifest.json fields, sw.js pattern, index.html head block requirements from the pwa_architecture section above.

**Phase 3 — State Machine**
Define the complete app state before any rendering:
- state.screen: 'home' | 'symptom' | 'variable' | 'cluster' | 'search'
- state.item: { type: string, id: string } | null
- state.stack: Array for multi-level back navigation with scroll position restoration
- state.searchQuery: string
- state.expandedCategories: Set of category names
- state.scrollPositions: Map of keys to scrollY values

**Phase 4 — Screen Architecture**
Define the DOM structure for each of the 5 screens before writing render functions. Reference the component CSS specs in the design_system section for exact CSS class names and properties.

**Phase 5 — Build and Verify**
Write all three files. Run the verification checklist before finalizing.
</thinking_process>

<requirements>
<must>
**manifest.json**
- Valid JSON: name, short_name, display: standalone, theme_color: #000000, background_color: #000000, start_url: ./, scope: ./, orientation: portrait-primary
- Two icons with valid base64 data URI src values (not placeholder strings), sizes 192x192 and 512x512, purpose: any maskable

**sw.js**
- Install handler caches all 3 app assets, calls self.skipWaiting()
- Activate handler deletes old caches, calls self.clients.claim()
- Fetch handler: GET-only, cache-first, falls back to network, caches new responses

**index.html — Head**
- viewport meta with viewport-fit=cover
- apple-mobile-web-app-capable, apple-mobile-web-app-status-bar-style: black-translucent
- theme-color: #000000
- link rel="manifest" href="./manifest.json"
- All CSS in one style block with design tokens (verbatim from design_system section) first

**Screen: Home**
- Title: "What are you experiencing?"
- Frosted glass sticky header (backdrop-filter: blur(20px) saturate(180%), -webkit-backdrop-filter same)
- iOS-style search bar: border-radius: 9999px, background: var(--bg-tertiary), min-height: 44px — real-time filter at >=2 characters
- 14 accordion category sections in exact order: Energy & Fatigue | Sleep | Mood & Emotions | Digestion | Food Reactions | Skin | Immune System | Hormonal (Female) | Hormonal (Male & Shared) | Cardiovascular & Circulatory | Pain & Inflammation | Respiratory | Cognitive & Neurological | Stress & Nervous System
- Category sections collapsed by default; tapping expands with chevron rotation
- Each symptom: tappable list row, min-height 44px, chevron right side, :active scale(0.98)
- Body padding-bottom = var(--nav-height) to clear tab bar
- Bottom nav: 3 tabs (Home | Search | Clusters), frosted glass, always visible, safe-area-aware

**Screen: Symptom Detail (Bottom Sheet)**
- Spring slide-up: transform translateY(100%) to translateY(0), var(--duration-slow) var(--ease-spring)
- Drag indicator: 36x5px centered pill
- Back button top-left, data-action="go-back"
- Symptom name heading (var(--text-xl), var(--weight-bold))
- H. PYLORI CHECK: if 'hpylori' in symptom.variables → render .alert-banner--destructive BEFORE variable pills: "⚠ Treat H. pylori before addressing other findings"
- Section "Variables Involved": .var-pill grid, --panel-color set per pill, cross-panel use .var-pill--cross, tappable
- Section "Root Cause Clusters": .cluster-tag grid, colored, tappable, prefix "A: GI Ecosystem Collapse" format
- Section "What This Means": 2-3 sentence practitioner-voice interpretation
- Section "Mechanism Hierarchy": text-tree using └─ indentation, minimum 3 levels, no canvas/SVG

**Screen: Variable Detail (Bottom Sheet)**
- Back button
- Variable name heading
- Panel badge: colored by panel, panel name as text
- CROSS-PANEL AMPLIFIER badge if isCrossPanel (dashed border variant)
- If isMedicalReferral: .alert-banner--destructive "⚕ MEDICAL REFERRAL REQUIRED — Refer to physician before FDN interventions"
- If isPriorityPathogen: .alert-banner--destructive "⚠ Priority Pathogen — treat H. pylori before all other GI findings"
- "When Elevated" section
- "When Low / Deficient" section or "N/A — not interpreted as low in this context"
- "Connected Variables": tappable .var-pill grid
- "Root Cause Clusters": tappable .cluster-tag grid

**Screen: Cluster Detail (Bottom Sheet)**
- Back button
- Cluster letter + full name heading, colored per cluster color
- If cluster E: MEDICAL REFERRAL REQUIRED block at top
- If cluster A: "Address before all others — GI dysfunction drives all downstream clusters." priority block
- Mechanism description
- "Variables in This Cluster": tappable .var-pill grid
- "Symptoms Associated": reverse-mapped symptoms (all symptoms.clusters.includes(id)) as tappable list rows

**Screen: Search**
- Full-screen search input, auto-focused on activation
- Real-time at >=2 characters across symptom labels AND variable names
- Results grouped: "Symptoms" and "Variables" headings
- Empty state: "Start typing to search symptoms and variables"
- No-results: "No matches for '[query]'"

**Navigation**
- JS-stack-based: navigate() pushes state, goBack() pops and restores scrollY
- Slide-left forward / slide-right back via CSS transform transitions only — no setTimeout, no JS animation
- Active tab highlighted with var(--accent)
- All interactive elements: min-height var(--touch-target), min-width var(--touch-target) in CSS

**Data**
- DATA.symptoms: all 76 entries, fully written — no placeholder comments
- DATA.variables: all 28 entries, fully written — no placeholder comments
- DATA.clusters: all 5 entries, fully written — no placeholder comments
- Use textContent and createElement for all dynamic DOM — never innerHTML with dynamic strings
</must>

<should>
- :active feedback on all tappable elements via CSS :active pseudo-class (scale or opacity)
- Search active: show match count badge in accordion section header
- Frosted glass uses both -webkit-backdrop-filter and backdrop-filter for Safari + Chrome compatibility
- Cluster tags prefixed with letter for fast scanning: "A: GI Ecosystem Collapse"
</should>

<may>
- Variables in 5+ symptoms may display "High-frequency marker" indicator on variable detail card
- Cross-panel constructs may render with gradient accent to further distinguish from panel-specific variables
- Category sections may remember expanded/collapsed state across navigation via state.expandedCategories
</may>
</requirements>

<constraints>
**This IS:**
- A clinical practitioner reference tool for FDN-trained professionals
- A multi-file offline-first PWA installable to a phone home screen
- A symptom-to-root-cause tracing tool for active client sessions

**This is NOT:**
- A patient-facing app — no patient language ("you might have...", "try taking...")
- A treatment engine — no supplement dosages, protocols, or interventions
- A data visualization app — no chart libraries, canvas, or SVG graphs
- A networked app — no API fetch calls, no localStorage, no external CDN

**Do NOT:**
- Reference external URLs, CDNs, fonts, or images in any file
- Use innerHTML with dynamically-constructed strings — use textContent and createElement
- Truncate DATA — all 76 symptoms, 28 variables, 5 clusters fully written; no "// ... more" comments
- Use setTimeout or setInterval for animations — CSS transitions only
- Write patient-facing copy anywhere in the UI
- Add treatment protocols, supplement names, or dosage recommendations
- Use more than 3 bottom navigation tabs
- Omit color coding from variable pills or cluster tags
- Omit H. pylori alert from renderSymptom()
- Omit Cluster E referral language from renderCluster() and isMedicalReferral variable cards
</constraints>

<output_format>
Deliver a /fdn-pwa/ folder with exactly three files:

1. manifest.json — Valid Web App Manifest with base64 icon data URIs
2. sw.js — Service worker with cache-first strategy
3. index.html — Complete app shell structured as:
   - DOCTYPE + html lang="en"
   - head: charset, viewport (viewport-fit=cover), PWA meta tags, title, manifest link, all CSS in style block
   - body: app container + bottom nav
   - One script block in this order:
     1. const DATA = {} — fully populated (76 symptoms, 28 variables, 5 clusters)
     2. Service worker registration
     3. const state = {}
     4. navigate() and goBack()
     5. renderHome(), renderSymptom(id), renderVariable(id), renderCluster(id), renderSearch()
     6. Event delegation on document using data-action and data-id
     7. init() called at bottom

All three files must render in Chrome and Safari with no console errors and no external network requests after service worker install.
</output_format>

<success_criteria>
Complete and correct when ALL of the following are true:

1. **Data completeness**: DATA.symptoms = 76 entries; DATA.variables = 28 entries; DATA.clusters = 5 entries
2. **PWA installability**: manifest.json has required fields + two valid base64 icons; Chrome shows "Installable" in DevTools Application tab
3. **Offline operation**: All screens navigable with DevTools Network set to Offline after first load
4. **Lighthouse PWA score**: >= 90
5. **Apple-quality UI**: Frosted glass tab bar and header; spring bottom-sheet transitions; SF Pro font stack; 4px grid spacing
6. **3-tap navigation**: Symptom → Variable → Connected Variable in <=3 taps, no dead ends
7. **H. pylori alert**: Every symptom with H. pylori in variables shows red banner BEFORE variable pills
8. **Cluster E referral**: Cluster E detail shows MEDICAL REFERRAL REQUIRED; Occult Blood and Calprotectin/Lactoferrin cards show referral banner
9. **Search**: Typing "histamine" returns all symptoms with Histamine-MBA, plus Histamine-MBA card, plus Histamine-DAO Regulatory System card
10. **Back navigation**: goBack() returns to exact previous screen with scroll position restored
11. **Zero external dependencies**: No external src, href, or url() references in any file
12. **Touch targets**: All interactive elements have min-height: var(--touch-target) and min-width: var(--touch-target) in CSS
13. **No truncation**: DATA contains complete written-out entries — no placeholder comments
</success_criteria>

<verification>
Before finalizing any file, complete this checklist:

manifest.json:
- [ ] Valid JSON, no syntax errors
- [ ] name, short_name, display: standalone, theme_color, background_color, start_url, scope, orientation present
- [ ] 2 icons with valid base64 data URI src (not placeholder text), purpose: any maskable

sw.js:
- [ ] Install: caches ASSETS array, self.skipWaiting()
- [ ] Activate: deletes old caches, self.clients.claim()
- [ ] Fetch: GET-only guard, cache-first, network fallback, caches new responses

index.html:
- [ ] viewport meta includes viewport-fit=cover
- [ ] apple-mobile-web-app-capable and apple-mobile-web-app-status-bar-style present
- [ ] link rel="manifest" href="./manifest.json" present
- [ ] All design tokens from design_system section present in :root {} verbatim
- [ ] Service worker registration after DATA object
- [ ] DATA.symptoms count = 76
- [ ] DATA.variables count = 28
- [ ] DATA.clusters count = 5
- [ ] renderSymptom() checks symptom.variables.includes('hpylori') and renders alert BEFORE variable pills
- [ ] renderCluster('E') renders MEDICAL REFERRAL REQUIRED block
- [ ] Calprotectin/Lactoferrin and Occult Blood variable cards render referral banner
- [ ] No external URL in any file
- [ ] All interactive CSS: min-height: var(--touch-target), min-width: var(--touch-target)
- [ ] No innerHTML with dynamic string construction
- [ ] No setTimeout/setInterval for animations

Mental walkthrough:
Tap "Bloating" → bottom sheet slides up with spring → H. pylori alert appears above variable pills → tap H. pylori pill → variable detail opens with priority pathogen + referral banners → tap back → Bloating detail returns with scroll restored → tap Cluster A tag → Cluster A detail shows "Address before all others" + mechanism + reverse-mapped symptoms including Bloating → tap back → Bloating detail restored
</verification>
```
