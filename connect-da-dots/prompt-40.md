# Prompt 40: Final PWA Verification Checklist

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `manifestVerified`
- Files that MUST already exist: `fdn-pwa/index.html`, `fdn-pwa/manifest.json`, `fdn-pwa/sw.js`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Run the final comprehensive verification of the completed FDN Symptom Navigator PWA. This is a read-only audit — no file modifications unless a critical defect is found.

**Step 1 — File existence check.**
```bash
ls -lh fdn-pwa/index.html fdn-pwa/manifest.json fdn-pwa/sw.js
```
Expected: all three files present, non-zero size.

**Step 2 — Zero remaining placeholders.**
```bash
grep -c "PLACEHOLDER" fdn-pwa/index.html
```
Expected: `0`. If any remain, report which ones and stop — do NOT mark this step complete.

**Step 3 — Data counts.**
```python
import json, re

with open('fdn-pwa/index.html', encoding='utf-8') as f:
    src = f.read()

# Count symptom entries
symptom_keys = re.findall(r"'([a-z][a-z0-9\-]+)':\s*\{[^}]*label:", src)
print(f"Symptom entries found: {len(symptom_keys)}")

# Count variable entries
var_keys = re.findall(r"'([a-z][a-z0-9\-]+)':\s*\{[^}]*panel:", src)
print(f"Variable entries found: {len(var_keys)}")

# Count cluster entries
cluster_keys = re.findall(r"'([A-E])':\s*\{[^}]*letter:", src)
print(f"Cluster entries found: {len(cluster_keys)}")
```
Expected: symptoms ≥ 76, variables ≥ 28, clusters = 5.

**Step 4 — Zero innerHTML with dynamic content.**
```bash
grep -n "innerHTML\s*=" fdn-pwa/index.html | grep -v "^\s*//"
```
Expected: 0 matches (or only commented-out lines).

**Step 5 — Zero external URLs in index.html.**
```bash
grep -n "https\?://" fdn-pwa/index.html | grep -v "^\s*//"
```
Expected: 0 matches.

**Step 6 — Service worker registered.**
```bash
grep -n "serviceWorker.register" fdn-pwa/index.html
```
Expected: 1 match — `navigator.serviceWorker.register('./sw.js')`.

**Step 7 — DOMContentLoaded init.**
```bash
grep -n "DOMContentLoaded" fdn-pwa/index.html
```
Expected: at least 1 match binding `init`.

**Step 8 — Critical function presence.**
```python
required_fns = [
    'function buildMaps',
    'function el(',
    'function txt(',
    'function openSheet',
    'function closeSheet',
    'function pushSheet',
    'function popSheet',
    'function navigateTab',
    'function renderScreen',
    'function renderHome',
    'function renderSymptom',
    'function renderVariable',
    'function renderCluster',
    'function renderSearch',
    'function init(',
]
with open('fdn-pwa/index.html', encoding='utf-8') as f:
    src = f.read()
missing = [fn for fn in required_fns if fn not in src]
if missing:
    print("MISSING FUNCTIONS:", missing)
else:
    print("All 15 required functions present: PASS")
```

**Step 9 — H. pylori and medical referral guards.**
```bash
grep -n "hpylori" fdn-pwa/index.html | head -5
grep -n "isMedicalReferral" fdn-pwa/index.html | head -5
grep -n "isPriorityPathogen" fdn-pwa/index.html | head -5
```
Expected: each has at least 1 match.

**Step 10 — sw.js cache-first strategy.**
```bash
grep -n "cache-first\|cacheFirst\|cache\.match\|respondWith" fdn-pwa/sw.js | head -10
```
Expected: matches showing cache-first fetch handler present.

**Step 11 — manifest.json standalone display.**
```python
import json
with open('fdn-pwa/manifest.json') as f:
    m = json.load(f)
assert m.get('display') == 'standalone', f"display={m.get('display')}"
assert m.get('name') == 'FDN Symptom Navigator', f"name={m.get('name')}"
assert len(m.get('icons', [])) == 2, f"icons count={len(m.get('icons', []))}"
print("manifest.json: PASS")
```

**Step 12 — Final report.**
Output exactly one of:
- `FINAL VERIFICATION: PASS — FDN Symptom Navigator PWA build complete.`
- `FINAL VERIFICATION: FAIL — [list each failing check]`

Only mark state complete on PASS.

## Verification
Before updating state.json, Claude MUST confirm:
- All three PWA files exist and are non-zero
- Zero PLACEHOLDER strings remain in index.html
- Symptom count ≥ 76, variable count ≥ 28, cluster count = 5
- Zero unguarded `innerHTML =` assignments
- Zero external URLs in index.html
- All 15 required functions present
- `hpylori`, `isMedicalReferral`, and `isPriorityPathogen` all appear in index.html
- sw.js has cache-first fetch handler
- manifest.json has `display: "standalone"` and 2 icons

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-40"`
- `pendingSteps`: remove `"step-40"`
- `flags.finalVerification`: set to `true`
- `artifacts.symptomCount`: set to actual count
- `artifacts.variableCount`: set to actual count
- `artifacts.clusterCount`: set to 5
