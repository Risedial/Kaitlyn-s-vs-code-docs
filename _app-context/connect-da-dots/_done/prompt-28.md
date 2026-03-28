# Prompt 28: Verify Data Integrity — Count 76 Symptoms, 28 Variables, 5 Clusters

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `symptomsBatch1`, `symptomsBatch2`, `symptomsBatch3`, `symptomsBatch4`, `symptomsBatch5`, `symptomsBatch6`, `symptomsBatch7`, `variablesBatch1`, `variablesBatch2`, `variablesBatch3`, `variablesBatch4`, `clusterData`
- Files that MUST already exist: `fdn-pwa/index.html`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Perform a data integrity audit of `fdn-pwa/index.html` to confirm all data entries have been written correctly before JS development begins.

**Step 1 — Count symptom entries.**
Use the Bash tool to run:
```bash
grep -c "'[a-z-]*':" fdn-pwa/index.html
```
Or use Python to parse and count DATA.symptoms keys. The expected count is **76 symptom entries**.

**Step 2 — Count variable entries.**
Count the unique variable IDs in DATA.variables. The expected count is **28 variable entries**.

The 28 expected variable IDs are:
`indican`, `urinary-bile-acids`, `ohdg`, `histamine-mba`, `dao`, `zonulin`, `cortisol-diurnal`, `dhea`, `testosterone`, `estradiol`, `progesterone`, `melatonin`, `sigas-shp`, `hpylori`, `candida`, `parasites`, `dysbiotic-bacteria`, `commensal-bacteria`, `calprotectin`, `beta-glucuronidase`, `anti-gliadin-iga`, `sigas-gi`, `occult-blood`, `hpa-axis`, `pregnenolone-steal`, `oxidative-stress`, `hepatic-detox`, `histamine-dao-system`

**Step 3 — Count cluster entries.**
Confirm exactly 5 cluster keys: `'A'`, `'B'`, `'C'`, `'D'`, `'E'`.

**Step 4 — Spot-check critical flags.**
Verify:
- `hpylori` has `isPriorityPathogen: true`
- `calprotectin` has `isMedicalReferral: true`
- `occult-blood` has `isMedicalReferral: true`
- `hpa-axis` has `isCrossPanel: true`
- `pregnenolone-steal` has `isCrossPanel: true`
- `oxidative-stress` has `isCrossPanel: true`
- `hepatic-detox` has `isCrossPanel: true`
- `histamine-dao-system` has `isCrossPanel: true`

**Step 5 — Check for remaining placeholders.**
Search for any remaining `PLACEHOLDER:` strings in `fdn-pwa/index.html`:
```bash
grep -c "PLACEHOLDER:" fdn-pwa/index.html
```
Expected: The only remaining PLACEHOLDER strings should be the JS section placeholders (`PLACEHOLDER:JS:*`), NOT any data or CSS placeholders. If any `PLACEHOLDER:SYMPTOMS:`, `PLACEHOLDER:VARIABLES:`, or `PLACEHOLDER:CLUSTERS` strings remain, do NOT mark this step complete — return to the relevant data batch prompt and complete the missing step.

**Step 6 — Report results.**
Report the audit results in text form:
- Symptom count: X/76
- Variable count: X/28
- Cluster count: X/5
- Critical flags verified: yes/no
- Remaining data placeholders: X (must be 0)

## Verification
Before updating state.json, Claude MUST confirm:
- Symptom count equals exactly **76**
- Variable count equals exactly **28**
- Cluster count equals exactly **5**
- All 5 critical flag spot-checks pass
- Zero `PLACEHOLDER:SYMPTOMS:`, `PLACEHOLDER:VARIABLES:`, or `PLACEHOLDER:CLUSTERS` strings remain in the file

**If any count fails**: Do NOT update state.json with dataIntegrityVerified: true. Instead, identify which batch is missing and re-run the relevant prompt (16–27) before returning here.

## State Update
On successful verification (ALL counts correct), update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-28"`
- `pendingSteps`: remove `"step-28"`
- `flags.dataIntegrityVerified`: set to `true`
- `artifacts.symptomCount`: set to `76` (override with verified count)
- `artifacts.variableCount`: set to `28`
- `artifacts.clusterCount`: set to `5`
