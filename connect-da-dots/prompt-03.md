# Prompt 03: Write sw.js — Service Worker with Cache-First Strategy

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `initialized`
- Files that MUST already exist: `fdn-pwa/sw.js` (stub from step-01)

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Write tool to overwrite `fdn-pwa/sw.js` with the complete Service Worker implementation below. Copy this code exactly — do not modify any logic, variable names, or comments:

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

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/sw.js` is non-empty and readable
- File contains `CACHE_NAME = 'fdn-nav-v1'`
- File contains all three event listeners: `install`, `activate`, `fetch`
- `ASSETS` array contains all three required paths: `'./index.html'`, `'./manifest.json'`, `'./sw.js'`
- `self.skipWaiting()` is present in the install handler
- `self.clients.claim()` is present in the activate handler
- Fetch handler has `if (event.request.method !== 'GET') return;` guard

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-03"`
- `pendingSteps`: remove `"step-03"`
- `flags.swWritten`: set to `true`
