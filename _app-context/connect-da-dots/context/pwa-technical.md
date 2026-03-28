# PWA Technical Reference — Vanilla JS, No Frameworks

*Compiled 2026-03-26 from MDN, web.dev, Chrome Developers, and CSS-Tricks documentation.*

---

## Manifest Spec

### Required Fields for Chrome Installability

A `manifest.json` file must be served as a separate file (not inline) and linked from every HTML page via:

```html
<link rel="manifest" href="/manifest.json">
```

The following fields are required or functionally required for Chrome's install prompt to trigger:

| Field | Required | Notes |
|---|---|---|
| `name` | Yes (or `short_name`) | Full app name; used in install dialogs and splash screens |
| `short_name` | Recommended | Shown on home screen when space is limited; max ~12 chars |
| `start_url` | Yes | The URL to load when the app is launched; must be within scope |
| `scope` | Recommended | Defines which URLs are "in-app"; defaults to the manifest's own directory |
| `display` | Yes (for standalone feel) | Must be one of `standalone`, `fullscreen`, or `minimal-ui` to suppress browser chrome |
| `theme_color` | Recommended | Colors the browser toolbar and Android task switcher |
| `background_color` | Recommended | Splash screen background before app paint; should match CSS body background |
| `icons` | Yes | Array of icon objects; must include at least 192x192 and 512x512 PNG |
| `prefer_related_applications` | Must be absent or `false` | If `true`, Chrome will not offer the install prompt |

Complete minimal example:

```json
{
  "name": "My Application",
  "short_name": "MyApp",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "theme_color": "#1a1a2e",
  "background_color": "#ffffff",
  "icons": [
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}
```

### Icon Requirements in Detail

- **Minimum sizes**: 192x192 and 512x512 pixels are required by Chromium browsers. Without both, the install criteria fail.
- **Format**: PNG is the universally safe format. SVG is not yet fully supported across all platforms as a manifest icon source.
- **`type` field**: Should be `"image/png"` for PNG files. Required for correct MIME handling.
- **`purpose` field**: Optional but important.
  - `"any"` — standard icon used on home screens, launchers, etc.
  - `"maskable"` — adaptive icon for Android that can be cropped into a circle/squircle. The icon's "safe zone" is a circle with 40% radius centered in the image (so the main visual should stay within that circle).
  - `"any maskable"` — serves both purposes from one image.
- **Recommended additional sizes**: 384x384, 1024x1024 for high-density displays; 180x180 for iOS.
- **Non-transparent background**: Use PNG icons with a solid background color for reliable rendering across platforms that auto-fill transparent areas.

### Chrome's Complete Installability Criteria

All of the following must be true for Chrome's automatic install prompt (`beforeinstallprompt`) to fire:

1. **HTTPS**: The page must be served over `https://`. Exception: `localhost` and `127.0.0.1` work for local development without HTTPS.
2. **Valid manifest**: A `manifest.json` must be linked, parseable, and contain at minimum:
   - `name` or `short_name`
   - `start_url`
   - `icons` with at least 192x192 and 512x512 PNG entries
   - `display` set to `standalone`, `fullscreen`, or `minimal-ui`
   - `prefer_related_applications` absent or `false`
3. **Service worker with fetch handler**: A registered service worker with a `fetch` event listener. (Note: Chrome 108+ mobile and 112+ desktop relaxed the fetch handler requirement for menu-based installation, but the `beforeinstallprompt` install-prompt path still requires it as of early 2025.)
4. **User engagement**: User has interacted with the page (click/tap) and spent at least 30 seconds on it. This gate prevents install spam.
5. **Not already installed**: Chrome will not offer installation if the PWA is already installed.

### iOS-Specific Meta Tags

Safari on iOS uses a combination of the Web App Manifest (iOS 16.4+) and legacy Apple-proprietary meta tags. For maximum backward compatibility across all iOS versions, include both:

```html
<!-- In the <head> of every HTML page -->

<!-- iOS PWA standalone mode (pre-iOS 16.4 requirement) -->
<meta name="apple-mobile-web-app-capable" content="yes">

<!-- Status bar style when running in standalone mode -->
<!-- Options: default | black | black-translucent -->
<!-- black-translucent makes the status bar overlay the app (content goes under it) -->
<!-- Requires env(safe-area-inset-top) to compensate -->
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

<!-- App title shown under the icon on the home screen -->
<meta name="apple-mobile-web-app-title" content="My App">

<!-- The home screen icon for iOS (180x180 recommended for modern iPhones) -->
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">

<!-- Optional: specify size variants -->
<link rel="apple-touch-icon" sizes="180x180" href="/icons/apple-touch-icon-180.png">
<link rel="apple-touch-icon" sizes="152x152" href="/icons/apple-touch-icon-152.png">
```

**Current status note**: As of web.dev guidance (2024-2025), `apple-mobile-web-app-capable` is considered legacy and web.dev recommends relying on the manifest `display` field instead for iOS 16.4+. However, for apps targeting older iOS versions or needing `black-translucent` status bar behavior, including these tags remains necessary.

---

## Service Worker Pattern

### Complete Cache-First Service Worker Implementation

This is a complete, production-ready `sw.js` file implementing the cache-first strategy with proper lifecycle management.

```javascript
// sw.js — Service Worker with Cache-First Strategy

const CACHE_NAME = 'app-cache-v1';

// Files to precache on install — these are served from cache even when offline
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/styles.css',
  '/app.js'
];

// ─── INSTALL ────────────────────────────────────────────────────────────────
// Fires when the browser installs this service worker version for the first time.
// event.waitUntil() keeps the SW alive until all precaching is done.
// self.skipWaiting() forces the new SW to activate immediately without waiting
// for existing tabs using the old SW to close.
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[SW] Precaching app shell');
        return cache.addAll(PRECACHE_URLS);
      })
      .then(() => {
        console.log('[SW] Install complete, skipping waiting');
        return self.skipWaiting();
      })
      .catch((error) => {
        console.error('[SW] Precache failed:', error);
      })
  );
});

// ─── ACTIVATE ───────────────────────────────────────────────────────────────
// Fires after install, once the old SW (if any) has released control.
// Use this phase to delete stale caches from previous versions.
// self.clients.claim() makes this SW take control of all open pages immediately
// (without a reload), so they benefit from the new cache right away.
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames
            .filter((name) => name !== CACHE_NAME)
            .map((staleName) => {
              console.log('[SW] Deleting old cache:', staleName);
              return caches.delete(staleName);
            })
        );
      })
      .then(() => {
        console.log('[SW] Activate complete, claiming clients');
        return self.clients.claim();
      })
  );
});

// ─── FETCH ──────────────────────────────────────────────────────────────────
// Intercepts every network request made by pages this SW controls.
// Strategy: Cache-First
//   1. Look in the cache for a matching response.
//   2. If found in cache → return it immediately (fast, offline-capable).
//   3. If not in cache → fetch from network.
//   4. If network succeeds → clone and store in cache, then return response.
//   5. If network fails and nothing in cache → return a generic error response.
self.addEventListener('fetch', (event) => {
  // Only handle GET requests — let POST/PUT/DELETE pass through to network
  if (event.request.method !== 'GET') {
    return;
  }

  // Only handle same-origin and CDN requests; skip browser-extension requests
  const url = new URL(event.request.url);
  if (url.protocol !== 'https:' && url.hostname !== 'localhost') {
    return;
  }

  event.respondWith(cacheFirst(event.request));
});

// Cache-First strategy function
async function cacheFirst(request) {
  // Step 1: Check the cache
  const cachedResponse = await caches.match(request);
  if (cachedResponse) {
    return cachedResponse;
  }

  // Step 2: Not in cache — go to network
  try {
    const networkResponse = await fetch(request);

    // Step 3: Cache the fresh network response for next time
    // Response is a stream and can only be consumed once, so clone() it:
    // one copy goes to the cache, one goes back to the browser.
    if (networkResponse && networkResponse.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }

    return networkResponse;
  } catch (error) {
    // Step 4: Network failed and nothing in cache
    console.error('[SW] Fetch failed for:', request.url, error);

    // Optionally return an offline fallback page for navigation requests:
    if (request.mode === 'navigate') {
      const fallback = await caches.match('/index.html');
      if (fallback) return fallback;
    }

    // Last resort: return a network error response
    return Response.error();
  }
}
```

### Registering the Service Worker (in index.html or app.js)

```javascript
// Register the service worker — must be done from the main page JS context
if ('serviceWorker' in navigator) {
  window.addEventListener('load', async () => {
    try {
      const registration = await navigator.serviceWorker.register('/sw.js', {
        scope: '/'
      });
      console.log('[App] Service worker registered:', registration.scope);
    } catch (error) {
      console.error('[App] Service worker registration failed:', error);
    }
  });
}
```

### Lifecycle Summary

| Event | When It Fires | Key Actions |
|---|---|---|
| `install` | First time this SW version is seen by the browser | `caches.open()` + `cache.addAll()` + `self.skipWaiting()` |
| `activate` | After install, after old SW releases clients | Delete old caches + `self.clients.claim()` |
| `fetch` | On every network request from controlled pages | Intercept + apply caching strategy |

**Critical implementation notes**:
- `event.waitUntil()` must receive a Promise. If the Promise rejects during `install`, the SW aborts and falls back to the previous version.
- `response.clone()` is mandatory before `cache.put()` — a Response body is a readable stream that can only be consumed once.
- `self.skipWaiting()` during install + `self.clients.claim()` during activate ensures the new SW takes effect without requiring the user to close and reopen every tab.
- To invalidate the cache and force re-installation, increment `CACHE_NAME` (e.g., `app-cache-v2`). The activate handler will then delete the old `app-cache-v1`.

---

## Safe Area CSS

### Problem

On iPhones and other notched/rounded-corner devices, content at the screen edges is obscured by hardware features: the notch (Dynamic Island), the status bar, rounded corners, and the home indicator bar at the bottom. A PWA running in standalone mode (no browser chrome) needs to account for these insets manually.

### Step 1: Viewport Meta Tag

This tag is required on every HTML page. The `viewport-fit=cover` value tells the browser to extend the app's canvas to fill the entire screen, including behind the notch and home indicator. Without this, the browser adds safe padding automatically and `env()` insets are all `0`.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
```

### Step 2: The env() CSS Variables

These four environment variables are populated by the OS with the exact pixel sizes of each unsafe inset region:

```css
env(safe-area-inset-top)     /* Status bar / notch / Dynamic Island height */
env(safe-area-inset-bottom)  /* Home indicator bar height (~34px on modern iPhones) */
env(safe-area-inset-left)    /* Side inset in landscape mode */
env(safe-area-inset-right)   /* Side inset in landscape mode */
```

**On a rectangular device with no obstructions**: all values are `0`.
**On iPhone with notch, portrait**: `top` = ~44-59px, `bottom` = ~34px, `left` = `right` = 0.
**On iPhone in landscape**: `top` = ~0, `bottom` = ~21px, `left` and `right` = ~44px each.

Always provide a fallback value as the second argument to `env()` for browsers that do not support it:

```css
/* Syntax: env(variable-name, fallback-value) */
padding-top: env(safe-area-inset-top, 0px);
padding-bottom: env(safe-area-inset-bottom, 0px);
```

### Step 3: Applying to a Top Header Bar

A fixed or sticky header must pad its content down below the status bar/notch:

```css
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 56px; /* Design height */

  /* Push content below the safe area */
  padding-top: env(safe-area-inset-top, 0px);

  /* Also extend the element's total height to include the inset */
  /* so the background color fills behind the notch */
  box-sizing: content-box;

  /* Extend background behind the notch using negative margin trick: */
  /* The element visually fills to screen top, content is padded down */
}

/* Alternative: increase the element's height to absorb the inset */
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  /* Total height = design height + safe area */
  height: calc(56px + env(safe-area-inset-top, 0px));
  padding-top: env(safe-area-inset-top, 0px);
  display: flex;
  align-items: flex-end; /* Content anchors to bottom of padded area */
}
```

### Step 4: Applying to a Bottom Navigation Bar

A bottom nav must pad its content above the home indicator:

```css
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;

  /* Extend left/right for landscape side insets */
  padding-left: env(safe-area-inset-left, 0px);
  padding-right: env(safe-area-inset-right, 0px);

  /* Push nav content above the home indicator */
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
```

### Step 5: The calc() Pattern for Fixed Height + Safe Area

When you need an element to have a fixed design height AND absorb the safe area (so the element's background visually covers the unsafe zone):

```css
/* Pattern: fixed design dimension + safe area inset */
.bottom-sheet {
  /* Total height includes both the content area and the home indicator zone */
  min-height: calc(80px + env(safe-area-inset-bottom, 0px));
  padding-bottom: calc(16px + env(safe-area-inset-bottom, 0px));
}

/* Pattern: content area height accounting for header and footer with safe areas */
.main-content {
  /* Subtract header (56px + top inset) and footer (64px + bottom inset) */
  height: calc(
    100vh
    - 56px - env(safe-area-inset-top, 0px)
    - 64px - env(safe-area-inset-bottom, 0px)
  );
  overflow-y: auto;
}

/* Pattern: using dvh (dynamic viewport height) for the full-screen layout */
.full-screen-layer {
  height: 100dvh; /* More reliable than 100vh on mobile browsers */
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
  box-sizing: border-box;
}
```

### Complete Safe Area CSS Example

```css
/* Global safe area setup */
:root {
  --safe-top: env(safe-area-inset-top, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left: env(safe-area-inset-left, 0px);
  --safe-right: env(safe-area-inset-right, 0px);

  /* Design dimensions */
  --header-height: 56px;
  --nav-height: 64px;
}

/* App layout container */
.app {
  display: flex;
  flex-direction: column;
  height: 100dvh;
  overflow: hidden;
}

/* Top header */
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: calc(var(--header-height) + var(--safe-top));
  padding-top: var(--safe-top);
  padding-left: var(--safe-left);
  padding-right: var(--safe-right);
  z-index: 100;
  box-sizing: border-box;
}

/* Scrollable content area */
.app-content {
  flex: 1;
  overflow-y: auto;
  padding-top: calc(var(--header-height) + var(--safe-top));
  padding-bottom: calc(var(--nav-height) + var(--safe-bottom));
  padding-left: var(--safe-left);
  padding-right: var(--safe-right);
}

/* Bottom navigation */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: calc(var(--nav-height) + var(--safe-bottom));
  padding-bottom: var(--safe-bottom);
  padding-left: var(--safe-left);
  padding-right: var(--safe-right);
  z-index: 100;
  box-sizing: border-box;
  display: flex;
  align-items: flex-start; /* Nav items anchor to top; safe area is below */
}
```

---

## Multi-File Architecture

### Why a True PWA Cannot Be a Single HTML File

This is a common misconception. A single `index.html` file cannot be a fully installable, offline-capable PWA. Here is the precise technical reasoning for each constraint:

### Constraint 1: Service Worker Scope and URL Requirements

A service worker must be registered from a **distinct URL** served by the HTTP server — it cannot be a blob URL, an inline script, or a data URI.

- The `navigator.serviceWorker.register(url)` call requires a URL string that the browser fetches as a separate HTTP request.
- The **scope** of a service worker is determined by the directory of its URL. A SW at `/sw.js` controls all pages under `/`. A SW at `/app/sw.js` controls only `/app/*`.
- A SW registered from a blob URL (e.g., `URL.createObjectURL(new Blob([...]))`) is explicitly unsupported in both Chrome and Safari. Chrome silently fails or throws a `DOMException`. Safari similarly rejects non-HTTP(S) SW URLs.
- Even if a blob URL registration worked momentarily in one browser, it would not persist across sessions (blob URLs are ephemeral, tied to the current page's lifetime) — making offline support impossible.

**Bottom line**: `sw.js` must be a real file at a real URL, served with the MIME type `application/javascript` (or `text/javascript`).

### Constraint 2: Manifest Must Be a Separate Linked File

Chrome's installability check fetches the manifest as a separate HTTP resource. An inline manifest (e.g., injected via JavaScript into a `<link>` tag pointing to a blob URL or data URI) does **not** satisfy Chrome's installability criteria reliably:

- Chrome's install criteria checker fetches and parses the manifest URL independently. It does not execute JavaScript.
- Some browsers accept `<link rel="manifest" href="data:application/manifest+json,...">` for parsing purposes, but this approach is not guaranteed across Chrome versions or Safari, and is not supported by Lighthouse or Chrome's install-prompt algorithm.
- The manifest file must be a JSON file at a stable, server-served URL (e.g., `/manifest.json`). It must respond with a `Content-Type` of `application/manifest+json` or `application/json`.

**Bottom line**: `manifest.json` must be a separate file accessible at a URL.

### Constraint 3: Required Minimum File Set

The minimum files that must exist as real server-served files for a fully installable, offline-capable PWA are:

```
/
├── index.html       — The app shell; links manifest and registers SW
├── manifest.json    — Web App Manifest; defines name, icons, display, etc.
└── sw.js            — Service Worker; handles install/activate/fetch
```

Optional but typically needed:
```
├── styles.css       — App styles (can be inlined in index.html to save a round trip)
├── app.js           — App logic (can be inlined in index.html)
└── icons/
    ├── icon-192.png — Required for Chrome installability
    └── icon-512.png — Required for Chrome installability
```

### Constraint 4: Icons as Base64 Data URIs Inside manifest.json

The **icons can be embedded as base64 data URIs** inside `manifest.json` to eliminate the need to host separate image files. This is useful for ultra-minimal hosting scenarios (e.g., a GitHub Pages repo with only three files).

The approach:

```json
{
  "name": "My App",
  "short_name": "MyApp",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#1a1a2e",
  "background_color": "#ffffff",
  "icons": [
    {
      "src": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMAAAADACAYAAABS3GwHAAAA...",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAA...",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}
```

**Browser support status**:
- **Chrome (Android/desktop)**: Data URI icon `src` values are accepted and the app is installable. The install prompt fires normally when all other criteria are met.
- **Safari (iOS)**: Safari uses the `apple-touch-icon` link element (which cannot be a data URI) rather than the manifest icon for the home screen. The manifest icon data URI is not used by iOS for home screen display. Therefore, for iOS home screen icons, a separate `apple-touch-icon.png` file (or an inline `<link rel="apple-touch-icon">` pointing to a data URI in the HTML, not the manifest) is needed.
- **Reliability caveat**: The base64 data URI in the manifest `src` is not officially documented as a supported syntax by the W3C Web App Manifest spec or Chrome's install criteria docs. It works in practice (as confirmed in Google Search Central community threads) but is not a guaranteed forward-compatible approach.

**How to generate the base64 string**:

```javascript
// Node.js: convert icon file to base64 for embedding in manifest.json
const fs = require('fs');
const data = fs.readFileSync('./icon-192.png');
const base64 = data.toString('base64');
const dataUri = `data:image/png;base64,${base64}`;
console.log(dataUri);
```

Or in the browser with Canvas (for generating a simple programmatic icon):

```javascript
function generateIconDataUri(size, bgColor, fgColor, letter) {
  const canvas = document.createElement('canvas');
  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext('2d');

  // Background
  ctx.fillStyle = bgColor;
  ctx.fillRect(0, 0, size, size);

  // Letter
  ctx.fillStyle = fgColor;
  ctx.font = `bold ${size * 0.5}px sans-serif`;
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(letter, size / 2, size / 2);

  return canvas.toDataURL('image/png');
}

// Returns: "data:image/png;base64,iVBORw0KGgo..."
const icon192 = generateIconDataUri(192, '#1a1a2e', '#ffffff', 'A');
```

### Summary: The Three Real Files Rule

| File | Can it be inlined or omitted? | Reason |
|---|---|---|
| `index.html` | Must exist as a real URL | The document itself; `start_url` in manifest must be a real HTTP URL |
| `manifest.json` | Must be a real file at a real URL | Chrome's installability checker fetches it as a separate HTTP request |
| `sw.js` | Must be a real file at a real URL | `navigator.serviceWorker.register()` fetches it via HTTP; blob URLs not supported cross-browser |
| Icon image files | **Can be eliminated** by embedding as base64 data URIs in manifest.json | The `src` field in manifest icon objects accepts data URIs in Chrome; useful for zero-asset-file hosting |

---

## Sources

- [Web app manifest | web.dev](https://web.dev/learn/pwa/web-app-manifest)
- [Add a web app manifest | web.dev](https://web.dev/articles/add-manifest)
- [What does it take to be installable? | web.dev](https://web.dev/articles/install-criteria)
- [Revisiting Chrome's installability criteria | Chrome Developers Blog](https://developer.chrome.com/blog/update-install-criteria)
- [Web app manifest does not meet installability requirements | Lighthouse](https://developer.chrome.com/docs/lighthouse/pwa/installable-manifest)
- [Web application manifest | MDN](https://developer.mozilla.org/en-US/docs/Web/Manifest)
- [Making PWAs installable | MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable)
- [Define your app icons | MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons)
- [Caching strategies | MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching)
- [Using Service Workers | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
- [Service workers and the Cache Storage API | web.dev](https://web.dev/articles/service-workers-cache-storage)
- [env() CSS function | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/env)
- [env() | CSS-Tricks](https://css-tricks.com/almanac/functions/e/env/)
- [Make Your PWAs Look Handsome on iOS | DEV Community](https://dev.to/karmasakshi/make-your-pwas-look-handsome-on-ios-1o08)
- [PWA Icon Requirements: The Complete 2025 Checklist | DEV Community](https://dev.to/albert_nahas_cdc8469a6ae8/pwa-icon-requirements-the-complete-2025-checklist-i3g)
- [Web Icons in 2025: Touch Icons, Adaptive Icons & manifest.json | BrowserUX](https://browserux.com/blog/guides/web-icons/touch-adaptive-icons-manifest.html)
