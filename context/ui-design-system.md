# UI Design System — Clinical Reference PWA
**iOS-Quality Dark Mode Design System**
*Synthesized from Apple HIG, iOS UIColor equivalents, CSS frosted glass specs, and mobile UI patterns — March 2026*

---

## Color Tokens

All tokens are defined as CSS custom properties. The dark mode palette mirrors Apple's iOS UIColor semantic system, translated to exact hex/rgba values for web use.

```css
:root {
  /* ── iOS System Background Equivalents (Dark Mode) ── */
  --bg-primary:       #000000;           /* UIColor.systemBackground (dark) */
  --bg-secondary:     #1C1C1E;           /* UIColor.secondarySystemBackground (dark) */
  --bg-tertiary:      #2C2C2E;           /* UIColor.tertiarySystemBackground (dark) */
  --bg-glass:         rgba(28, 28, 30, 0.72); /* Frosted glass surface — ~72% opacity for Liquid Glass depth */

  /* ── Text / Label Colors ── */
  --text-primary:     rgba(255, 255, 255, 1.0);   /* UIColor.label (dark) */
  --text-secondary:   rgba(255, 255, 255, 0.55);  /* UIColor.secondaryLabel (dark) */
  --text-tertiary:    rgba(255, 255, 255, 0.35);  /* UIColor.tertiaryLabel (dark) */

  /* ── Separators ── */
  --separator:        rgba(255, 255, 255, 0.12);  /* UIColor.separator (dark, translucent) */
  --separator-opaque: #3A3A3C;                    /* UIColor.opaqueSeparator (dark) */

  /* ── Accent / System Colors ── */
  --accent:           #007AFF;   /* UIColor.systemBlue */
  --accent-destructive: #FF3B30; /* UIColor.systemRed */

  /* ── FDN Panel Colors (fixed — do not alter) ── */
  --panel-mwp:    #e07c3a;
  --panel-mba:    #3abde0;
  --panel-shp:    #8b5cf6;
  --panel-gimap:  #22c55e;
  --panel-cross:  #94a3b8;

  /* ── FDN Cluster Colors (fixed — do not alter) ── */
  --cluster-a: #ef4444;
  --cluster-b: #f97316;
  --cluster-c: #ec4899;
  --cluster-d: #06b6d4;
  --cluster-e: #fbbf24;
}
```

### Color Token Reference Table

| Token | Value | iOS Semantic Equivalent |
|---|---|---|
| `--bg-primary` | `#000000` | `systemBackground` (dark) |
| `--bg-secondary` | `#1C1C1E` | `secondarySystemBackground` (dark) |
| `--bg-tertiary` | `#2C2C2E` | `tertiarySystemBackground` (dark) |
| `--bg-glass` | `rgba(28,28,30,0.72)` | Liquid Glass material (dark tint) |
| `--text-primary` | `rgba(255,255,255,1.0)` | `label` (dark) |
| `--text-secondary` | `rgba(255,255,255,0.55)` | `secondaryLabel` (dark) |
| `--text-tertiary` | `rgba(255,255,255,0.35)` | `tertiaryLabel` (dark) |
| `--separator` | `rgba(255,255,255,0.12)` | `separator` (dark, translucent) |
| `--separator-opaque` | `#3A3A3C` | `opaqueSeparator` (dark) |
| `--accent` | `#007AFF` | `systemBlue` |
| `--accent-destructive` | `#FF3B30` | `systemRed` |

---

## Typography

SF Pro is accessed on Apple platforms via `-apple-system` and `BlinkMacSystemFont` — the font name itself is not directly addressable in CSS. The stack below ensures SF Pro on Apple, Segoe UI Variable on Windows 11, and Roboto/Helvetica Neue elsewhere.

```css
:root {
  /* ── Font Family ── */
  --font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text',
                 'Helvetica Neue', Arial, sans-serif;

  /* ── Size Scale (rem, base = 16px) ── */
  --text-xs:   0.6875rem;  /* 11px — captions, legal */
  --text-sm:   0.8125rem;  /* 13px — secondary labels, footnotes */
  --text-base: 1rem;       /* 16px — body text */
  --text-md:   1.0625rem;  /* 17px — iOS default body size */
  --text-lg:   1.25rem;    /* 20px — subheadings */
  --text-xl:   1.5rem;     /* 24px — section titles */
  --text-2xl:  2rem;       /* 32px — large display */

  /* ── Font Weights ── */
  --weight-regular:  400;
  --weight-medium:   500;
  --weight-semibold: 600;
  --weight-bold:     700;

  /* ── Letter Spacing ── */
  --tracking-tight:  -0.02em;
  --tracking-normal:  0em;
  --tracking-wide:    0.03em;
  --tracking-caps:    0.06em;
}
```

---

## Spacing

4px base grid expressed in rem units.

```css
:root {
  --space-1:  0.25rem;   /*  4px */
  --space-2:  0.5rem;    /*  8px */
  --space-3:  0.75rem;   /* 12px */
  --space-4:  1rem;      /* 16px */
  --space-5:  1.25rem;   /* 20px */
  --space-6:  1.5rem;    /* 24px */
  --space-8:  2rem;      /* 32px */
  --space-10: 2.5rem;    /* 40px */
  --space-12: 3rem;      /* 48px */
}
```

---

## Shadow Tokens

Dark-background-optimized shadows use low-opacity black (avoids halos on dark surfaces). Elevation is expressed through both shadow and background differentiation.

```css
:root {
  --shadow-0: none;

  --shadow-1: 0 1px 2px rgba(0, 0, 0, 0.4),
              0 0px 1px rgba(0, 0, 0, 0.3);
  /* Subtle — inline icons, minor element lift */

  --shadow-2: 0 4px 12px rgba(0, 0, 0, 0.5),
              0 1px 3px  rgba(0, 0, 0, 0.4);
  /* Medium — card elevation, list group containers */

  --shadow-3: 0 16px 40px rgba(0, 0, 0, 0.6),
              0  4px 12px rgba(0, 0, 0, 0.5),
              0  1px  3px rgba(0, 0, 0, 0.4);
  /* High — bottom sheets, modals, floating panels */
}
```

---

## Motion

Cubic-bezier values aligned with iOS UIKit spring physics and navigation transitions.

```css
:root {
  /* ── Easing Functions ── */

  /* iOS spring overshoot — matches UISpringTimingParameters with damping < 1 */
  --ease-spring:   cubic-bezier(0.34, 1.56, 0.64, 1);

  /* iOS navigation push/pop — UIViewAnimationCurveEaseInOut equivalent */
  --ease-snap:     cubic-bezier(0.25, 0.46, 0.45, 0.94);

  /* Material-style standard curve — smooth, no overshoot */
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);

  /* ── Durations ── */
  --duration-fast:   150ms;   /* micro-interactions, icon state changes */
  --duration-normal: 300ms;   /* navigation, sheet open/close */
  --duration-slow:   450ms;   /* bottom sheet with spring overshoot */
}
```

---

## Component Specs

### Bottom Tab Bar

Fixed to the bottom of the viewport, full-bleed frosted glass. Respects the device safe area below the home indicator bar.

**DOM Structure:**
```html
<nav class="tab-bar" role="tablist">
  <button class="tab-item" role="tab" aria-selected="true">
    <span class="tab-icon" aria-hidden="true"><!-- SVG icon --></span>
    <span class="tab-label">Panel 1</span>
  </button>
  <button class="tab-item" role="tab" aria-selected="false">
    <span class="tab-icon" aria-hidden="true"><!-- SVG icon --></span>
    <span class="tab-label">Panel 2</span>
  </button>
  <button class="tab-item" role="tab" aria-selected="false">
    <span class="tab-icon" aria-hidden="true"><!-- SVG icon --></span>
    <span class="tab-label">Panel 3</span>
  </button>
</nav>
```

**CSS:**
```css
.tab-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  max-width: 430px;
  margin: 0 auto;

  height: calc(60px + var(--safe-bottom));
  padding-bottom: var(--safe-bottom);

  display: flex;
  align-items: stretch;

  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);  /* Safari iOS */

  border-top: 1px solid var(--separator);
  box-sizing: border-box;
  z-index: 100;
}

.tab-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-1);

  min-height: 44px;           /* Apple minimum touch target */
  padding: 0;
  border: none;
  background: transparent;
  cursor: pointer;

  color: var(--text-tertiary);
  font-family: var(--font-family);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-normal);

  transition: color var(--duration-fast) var(--ease-standard);
  -webkit-tap-highlight-color: transparent;
}

.tab-item[aria-selected="true"] {
  color: var(--accent);
}

.tab-icon {
  width: 24px;
  height: 24px;
}
```

---

### Top Header

Sticky frosted glass header with safe-area-inset-top padding for notch/Dynamic Island devices.

**DOM Structure:**
```html
<header class="top-header">
  <div class="top-header-inner">
    <h1 class="header-title">Title</h1>
    <div class="header-actions"><!-- action buttons --></div>
  </div>
</header>
```

**CSS:**
```css
.top-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 90;

  height: calc(52px + var(--safe-top));
  padding-top: var(--safe-top);

  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);

  border-bottom: 1px solid var(--separator);
  box-sizing: border-box;
}

.top-header-inner {
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--space-4);
}

.header-title {
  font-family: var(--font-family);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--text-primary);
  margin: 0;
  letter-spacing: var(--tracking-tight);
}
```

---

### Card / List Row

Standard list row with minimum 44px touch target per Apple HIG.

**DOM Structure:**
```html
<div class="list-row" role="button" tabindex="0">
  <div class="list-row-content">
    <span class="list-row-title">Row Title</span>
    <span class="list-row-subtitle">Secondary text</span>
  </div>
  <span class="list-row-chevron" aria-hidden="true">&#8250;</span>
</div>
```

**CSS:**
```css
.list-row {
  display: flex;
  align-items: center;
  justify-content: space-between;

  min-height: 44px;
  padding: 12px 16px;

  background: var(--bg-secondary);
  border-bottom: 1px solid var(--separator);

  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition: background var(--duration-fast) var(--ease-standard),
              transform var(--duration-fast) var(--ease-standard);
}

.list-row:active {
  transform: scale(0.98);
  background: var(--bg-tertiary);
}

.list-row-content {
  display: flex;
  flex-direction: column;
  gap: 2px;
  flex: 1;
  min-width: 0;
}

.list-row-title {
  font-family: var(--font-family);
  font-size: var(--text-base);
  font-weight: var(--weight-regular);
  color: var(--text-primary);
}

.list-row-subtitle {
  font-family: var(--font-family);
  font-size: var(--text-sm);
  font-weight: var(--weight-regular);
  color: var(--text-secondary);
}

.list-row-chevron {
  font-size: 1.25rem;
  color: var(--text-tertiary);
  margin-left: var(--space-2);
  flex-shrink: 0;
  line-height: 1;
}
```

---

### Variable Pill

Colored rounded pill representing a clinical variable, belonging to a specific panel.

**DOM Structure:**
```html
<!-- Standard panel pill -->
<span class="var-pill" style="--panel-color: var(--panel-mwp);">
  Variable Name
</span>

<!-- Cross-panel variant -->
<span class="var-pill var-pill--cross" style="--panel-color: var(--panel-cross);">
  Cross Variable
</span>
```

**CSS:**
```css
.var-pill {
  display: inline-flex;
  align-items: center;
  justify-content: center;

  min-height: 28px;
  min-width: 44px;        /* touch target via padding */
  padding: 4px 12px;
  border-radius: 9999px;  /* fully rounded */

  background: var(--panel-color);
  color: #000000;         /* dark text on colored background for contrast */

  font-family: var(--font-family);
  font-size: var(--text-sm);    /* 0.8125rem = 13px */
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-normal);
  white-space: nowrap;

  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition: opacity var(--duration-fast) var(--ease-standard),
              transform var(--duration-fast) var(--ease-standard);
}

.var-pill:active {
  opacity: 0.75;
  transform: scale(0.96);
}

/* Cross-panel variant: transparent background, dashed border */
.var-pill--cross {
  background: transparent;
  border: 2px dashed var(--panel-color);
  color: var(--panel-color);  /* text matches panel color */
}
```

---

### Cluster Tag

Identical dimensions to Variable Pill but with square-ish corners, used for diagnostic clusters.

**DOM Structure:**
```html
<span class="cluster-tag" style="--cluster-color: var(--cluster-a);">
  Cluster A
</span>
```

**CSS:**
```css
.cluster-tag {
  display: inline-flex;
  align-items: center;
  justify-content: center;

  min-height: 28px;
  min-width: 44px;
  padding: 4px 12px;
  border-radius: 8px;     /* square-ish, not fully rounded */

  background: var(--cluster-color);
  color: #000000;

  font-family: var(--font-family);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-normal);
  white-space: nowrap;

  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition: opacity var(--duration-fast) var(--ease-standard);
}

.cluster-tag:active {
  opacity: 0.75;
}
```

---

### Bottom Sheet

Full-screen overlay sheet that slides up from the bottom with an iOS spring animation. Drag indicator centered at top.

**DOM Structure:**
```html
<div class="sheet-backdrop" aria-hidden="true"></div>
<div class="bottom-sheet" role="dialog" aria-modal="true" aria-label="Sheet Title">
  <div class="sheet-drag-indicator" aria-hidden="true"></div>
  <div class="sheet-header">
    <h2 class="sheet-title">Sheet Title</h2>
    <button class="sheet-close" aria-label="Close">&#x2715;</button>
  </div>
  <div class="sheet-body">
    <!-- scrollable content -->
  </div>
</div>
```

**CSS:**
```css
.sheet-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 200;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--duration-normal) var(--ease-standard);
}

.sheet-backdrop.is-open {
  opacity: 1;
  pointer-events: auto;
}

.bottom-sheet {
  position: fixed;
  inset: 0;
  top: auto;               /* anchor to bottom */
  max-height: 92dvh;
  z-index: 201;

  background: var(--bg-secondary);
  border-radius: 16px 16px 0 0;
  box-shadow: var(--shadow-3);

  display: flex;
  flex-direction: column;

  overflow-y: auto;
  overscroll-behavior: contain;
  -webkit-overflow-scrolling: touch;

  /* Closed state */
  transform: translateY(100%);
  transition: transform var(--duration-slow) var(--ease-spring);

  /* Safe area at bottom */
  padding-bottom: var(--safe-bottom);
}

.bottom-sheet.is-open {
  transform: translateY(0);
}

.sheet-drag-indicator {
  width: 36px;
  height: 5px;
  background: var(--separator-opaque);
  border-radius: 9999px;
  margin: 8px auto 4px;
  flex-shrink: 0;
}

.sheet-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--separator);
  flex-shrink: 0;
}

.sheet-title {
  font-family: var(--font-family);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--text-primary);
  margin: 0;
}

.sheet-close {
  width: 28px;
  height: 28px;
  border-radius: 9999px;
  border: none;
  background: var(--bg-tertiary);
  color: var(--text-secondary);
  font-size: var(--text-base);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.sheet-body {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-4);
  overscroll-behavior: contain;
}
```

---

### Search Bar

iOS-style full-radius rounded search input, no visible border.

**DOM Structure:**
```html
<div class="search-bar-wrapper">
  <label class="search-bar">
    <span class="search-icon" aria-hidden="true">
      <!-- magnifying glass SVG -->
    </span>
    <input
      class="search-input"
      type="search"
      placeholder="Search..."
      autocomplete="off"
      autocorrect="off"
      spellcheck="false"
    />
  </label>
</div>
```

**CSS:**
```css
.search-bar-wrapper {
  padding: var(--space-2) var(--space-4);
}

.search-bar {
  display: flex;
  align-items: center;
  gap: var(--space-2);

  background: var(--bg-tertiary);
  border-radius: 9999px;    /* full pill shape */
  min-height: 44px;
  padding: 8px 16px;
  box-sizing: border-box;

  /* No visible border in default state */
  border: 1px solid transparent;
  transition: border-color var(--duration-fast) var(--ease-standard);
}

.search-bar:focus-within {
  border-color: var(--separator-opaque);
}

.search-icon {
  color: var(--text-tertiary);
  flex-shrink: 0;
  width: 18px;
  height: 18px;
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);

  font-family: var(--font-family);
  font-size: var(--text-base);     /* 1rem */
  font-weight: var(--weight-regular);

  /* Remove iOS input styling */
  -webkit-appearance: none;
  appearance: none;
}

.search-input::placeholder {
  color: var(--text-tertiary);
}

/* Remove Safari search cancel button if desired */
.search-input::-webkit-search-cancel-button {
  -webkit-appearance: none;
}
```

---

### Accordion Section Header

Expandable section header with animated chevron and match-count badge.

**DOM Structure:**
```html
<button class="accordion-header" aria-expanded="false" aria-controls="section-body">
  <span class="accordion-title">Section Title</span>
  <div class="accordion-meta">
    <span class="accordion-badge">12</span>
    <span class="accordion-chevron" aria-hidden="true">&#8250;</span>
  </div>
</button>
<div class="accordion-body" id="section-body" hidden>
  <!-- content -->
</div>
```

**CSS:**
```css
.accordion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  min-height: 44px;
  width: 100%;
  padding: var(--space-3) var(--space-4);
  box-sizing: border-box;

  background: var(--bg-secondary);
  border: none;
  border-bottom: 1px solid var(--separator);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.accordion-title {
  font-family: var(--font-family);
  font-size: var(--text-base);
  font-weight: var(--weight-semibold);
  color: var(--text-primary);
  text-align: left;
  flex: 1;
}

.accordion-meta {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-shrink: 0;
}

.accordion-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 20px;
  height: 20px;
  padding: 0 6px;
  border-radius: 9999px;

  background: var(--accent);
  color: #ffffff;
  font-family: var(--font-family);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
}

.accordion-chevron {
  font-size: 1.25rem;
  color: var(--text-tertiary);
  transition: transform var(--duration-normal) var(--ease-snap);
  display: inline-block;
  line-height: 1;
}

.accordion-header[aria-expanded="true"] .accordion-chevron {
  transform: rotate(90deg);
}

.accordion-body {
  background: var(--bg-primary);
  padding: var(--space-3) var(--space-4);
}

.accordion-body[hidden] {
  display: none;
}
```

---

### Alert Banner (H. pylori Priority)

High-visibility destructive alert banner.

**DOM Structure:**
```html
<div class="alert-banner alert-banner--destructive" role="alert">
  <span class="alert-icon" aria-hidden="true">&#9888;&#xFE0E;</span>
  <div class="alert-content">
    <p class="alert-title">H. pylori — Priority Finding</p>
    <p class="alert-body">Consider eradication therapy before NSAID use.</p>
  </div>
</div>
```

**CSS:**
```css
.alert-banner {
  width: 100%;
  padding: 16px;
  box-sizing: border-box;
  border-radius: 12px;
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
}

.alert-banner--destructive {
  background: rgba(255, 59, 48, 0.15);
  border: 1px solid #FF3B30;
  color: #FF3B30;
}

.alert-icon {
  font-size: var(--text-lg);
  flex-shrink: 0;
  line-height: 1;
  margin-top: 1px;
}

.alert-content {
  flex: 1;
  min-width: 0;
}

.alert-title {
  font-family: var(--font-family);
  font-size: var(--text-base);
  font-weight: var(--weight-semibold);   /* 600 */
  color: #FF3B30;
  margin: 0 0 4px 0;
}

.alert-body {
  font-family: var(--font-family);
  font-size: var(--text-sm);
  font-weight: var(--weight-regular);
  color: rgba(255, 59, 48, 0.85);
  margin: 0;
  line-height: 1.4;
}
```

---

### Cross-Panel Badge

Pill-shaped badge with dashed border, indicating a variable that appears across multiple panels.

**DOM Structure:**
```html
<span class="var-pill var-pill--cross" style="--panel-color: var(--panel-cross);">
  Cross Badge
</span>
```

**CSS:** Inherits `.var-pill--cross` from the Variable Pill component above.

```css
/* Standalone cross-panel badge (if not using var-pill base) */
.cross-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;

  min-height: 28px;
  min-width: 44px;
  padding: 4px 12px;
  border-radius: 9999px;

  background: transparent;
  border: 2px dashed var(--panel-cross, #94a3b8);
  color: var(--panel-cross, #94a3b8);

  font-family: var(--font-family);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  white-space: nowrap;
}
```

---

## Safe Area Integration

Full viewport-fit implementation for notch, Dynamic Island, and home indicator devices.

### HTML Viewport Meta Tag

```html
<meta name="viewport"
      content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
```

`viewport-fit=cover` is required to allow content to extend under the notch/Dynamic Island and for `env(safe-area-inset-*)` values to be non-zero.

### CSS Custom Properties and Usage

```css
:root {
  --safe-top:    env(safe-area-inset-top, 0px);
  --safe-right:  env(safe-area-inset-right, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left:   env(safe-area-inset-left, 0px);
}

/* Top header — pad above content for Dynamic Island / notch */
.top-header {
  padding-top: var(--safe-top);
  height: calc(52px + var(--safe-top));
}

/* Bottom nav — pad below tabs for home indicator bar */
.tab-bar {
  padding-bottom: var(--safe-bottom);
  height: calc(60px + var(--safe-bottom));
}

/* Main scroll container — ensure content isn't hidden under fixed bars */
.main-content {
  padding-top: calc(52px + var(--safe-top));
  padding-bottom: calc(60px + var(--safe-bottom));
  min-height: 100dvh;      /* dynamic viewport height — excludes browser chrome */
  overflow-y: auto;
  overscroll-behavior-y: contain;
  -webkit-overflow-scrolling: touch;
}

/* Bottom sheets need safe-bottom padding inside scrollable area */
.bottom-sheet {
  padding-bottom: var(--safe-bottom);
}
```

### Frosted Glass Performance Notes (Safari iOS)

Safari iOS fully supports `backdrop-filter` since Safari 14, and the `-webkit-` prefix is still recommended through 2026 for maximum compatibility:

```css
.frosted-element {
  /* Always include both prefixed and standard */
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  backdrop-filter: blur(20px) saturate(180%);

  /* GPU compositing hints for mobile performance */
  will-change: backdrop-filter;
  transform: translateZ(0);

  /* Avoid box-shadow on same element as backdrop-filter in Safari —
     use drop-shadow() inside backdrop-filter instead if needed */
  backdrop-filter: blur(20px) saturate(180%) drop-shadow(0 4px 12px rgba(0,0,0,0.4));
  -webkit-backdrop-filter: blur(20px) saturate(180%) drop-shadow(0 4px 12px rgba(0,0,0,0.4));
}
```

### PWA Manifest Recommendations

```json
{
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#000000",
  "orientation": "portrait"
}
```

### Complete CSS Variables Block (Copy-paste ready)

```css
:root {
  /* Safe areas */
  --safe-top:    env(safe-area-inset-top, 0px);
  --safe-right:  env(safe-area-inset-right, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left:   env(safe-area-inset-left, 0px);

  /* Backgrounds */
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

  /* Accents */
  --accent:            #007AFF;
  --accent-destructive: #FF3B30;

  /* FDN Panels */
  --panel-mwp:   #e07c3a;
  --panel-mba:   #3abde0;
  --panel-shp:   #8b5cf6;
  --panel-gimap: #22c55e;
  --panel-cross: #94a3b8;

  /* FDN Clusters */
  --cluster-a: #ef4444;
  --cluster-b: #f97316;
  --cluster-c: #ec4899;
  --cluster-d: #06b6d4;
  --cluster-e: #fbbf24;

  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text',
                 'Helvetica Neue', Arial, sans-serif;
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

  /* Spacing */
  --space-1:  0.25rem;
  --space-2:  0.5rem;
  --space-3:  0.75rem;
  --space-4:  1rem;
  --space-5:  1.25rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;

  /* Shadows */
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
}
```

---

*Sources synthesized from: Apple Human Interface Guidelines (developer.apple.com), iOS UIColor Dark Mode cheat sheets (sarunw.com, noahgilmore.com), CSS backdrop-filter documentation (MDN, joshwcomeau.com), iOS tab bar specifications (ivomynttinen.com, Apple Developer), iOS spring animation cubic-bezier research (css-tricks.com, pyxofy.com), and mobile UI pattern references (mobbin.com, nngroup.com) — compiled March 2026.*
