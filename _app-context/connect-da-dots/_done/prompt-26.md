# Prompt 26: Write JS — Variable Data: Cross-Panel Constructs (5 entries)

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `dataSkeletonWritten`
- Files that MUST already exist: `fdn-pwa/index.html` (with DATA skeleton from step-15)

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:VARIABLES:BATCH4` in `fdn-pwa/index.html` with the 5 cross-panel construct variable entries below. This is the LAST variable batch — after this step, all 28 variable entries will be present.

**CRITICAL**: All 5 entries in this batch have `isCrossPanel: true`. This flag causes the UI to render the `CROSS-PANEL AMPLIFIER` badge and the dashed-border `.var-pill--cross` variant for these variables.

The cross-panel construct panel code is `'CROSS'` with color `#94a3b8`.

Write ALL 5 entries replacing `// PLACEHOLDER:VARIABLES:BATCH4`:

```javascript
    'hpa-axis': {
      name: 'HPA Axis Dysregulation Pattern',
      panel: 'CROSS',
      panelColor: '#94a3b8',
      description: 'Adrenal stress response cascade — 5-phase progressive model: Alarm → Resistance → Exhaustion → Collapse → Recovery',
      elevated: 'Phase-dependent interpretation. Phase 1 (Alarm): acute cortisol elevation, all markers responding appropriately. Phase 2 (Resistance): cortisol elevated, DHEA beginning to fall, sIgA-SHP declining. Phase 3 (Exhaustion): cortisol variable, DHEA significantly low, sIgA suppressed. Phase 4 (Collapse): cortisol flat/low, DHEA very low, sIgA severely suppressed — referral-level presentation. Phase 5 (Recovery): gradual normalization with appropriate support.',
      low: 'N/A — phase-dependent interpretation. "Low" cortisol in context = Phase 3–4 Exhaustion/Collapse',
      connections: ['cortisol-diurnal', 'dhea', 'sigas-shp', 'pregnenolone-steal', 'melatonin'],
      clusters: ['B'],
      isCrossPanel: true,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'pregnenolone-steal': {
      name: 'Pregnenolone Steal and Steroidogenesis Disruption',
      panel: 'CROSS',
      panelColor: '#94a3b8',
      description: 'Downstream mechanism (not a direct lab value) — cortisol demand diverts pregnenolone from sex hormone synthesis',
      elevated: 'When cortisol demand chronically exceeds pregnenolone synthesis capacity, the steroidogenesis pathway prioritizes cortisol production at the expense of DHEA and downstream sex hormones (testosterone, estradiol, progesterone). Clinical signature: DHEA low + Testosterone low + Progesterone low in the presence of elevated or erratic cortisol. This is a MECHANISM construct, not a directly measured lab value — infer from the SHP panel pattern.',
      low: 'N/A — Pregnenolone Steal is a mechanism construct, not a measured value',
      connections: ['dhea', 'testosterone', 'estradiol', 'progesterone', 'cortisol-diurnal'],
      clusters: ['B'],
      isCrossPanel: true,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'oxidative-stress': {
      name: 'Systemic Oxidative Stress Cascade',
      panel: 'CROSS',
      panelColor: '#94a3b8',
      description: 'Overarching amplifier of all dysfunction across all panels — measured via 8-OHdG',
      elevated: 'Oxidative stress exceeds the body\'s antioxidant defense capacity simultaneously across all organ systems. Accelerates every other dysregulation: worsens HPA dysfunction, mucosal barrier breakdown, hormonal imbalance, GI pathology, and neurological impairment. Elevated 8-OHdG is the direct measurement. This construct should be considered active and amplifying whenever 8-OHdG is elevated above optimal range.',
      low: 'N/A — low oxidative stress is the healthy baseline',
      connections: ['ohdg', 'hepatic-detox', 'hpa-axis'],
      clusters: ['A', 'B', 'C', 'D', 'E'],
      isCrossPanel: true,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'hepatic-detox': {
      name: 'Hepatic Detoxification Impairment',
      panel: 'CROSS',
      panelColor: '#94a3b8',
      description: 'Liver Phase I/II/III overwhelm — impairs clearance of hormones, toxins, and metabolic byproducts',
      elevated: 'Liver detoxification pathway overwhelm. Phase I CYP450 enzymes produce reactive intermediates faster than Phase II conjugation can neutralize them. Phase III transport proteins fail to excrete conjugated compounds. Results: toxin and hormone recirculation (especially estrogen — connects to Cluster C), bile acid spillover, neurotoxin accumulation. Urinary Bile Acids elevated confirms Phase III excretion impairment. This construct amplifies Cluster C (estrogen recycling) and all toxin-driven symptom patterns.',
      low: 'N/A — adequate hepatic detoxification is expected baseline',
      connections: ['urinary-bile-acids', 'beta-glucuronidase', 'ohdg', 'oxidative-stress'],
      clusters: ['A', 'C'],
      isCrossPanel: true,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'histamine-dao-system': {
      name: 'Histamine-DAO Regulatory System',
      panel: 'CROSS',
      panelColor: '#94a3b8',
      description: 'Functional balance of histamine production vs. DAO degradation capacity — the histamine intolerance construct',
      elevated: 'System disrupted: histamine load exceeds DAO degradation capacity. Interpret using Histamine-MBA:DAO ratio. High Histamine + Low DAO = degradation failure (primary histamine intolerance). High Histamine + High DAO = production excess overwhelming degradation. Low Histamine + Low DAO = total mucosal collapse (DAO production failure without histamine load yet). This construct integrates both values to determine clinical mechanism and intervention priority.',
      low: 'N/A — the Histamine-DAO Regulatory System is a functional construct, not a measured value',
      connections: ['histamine-mba', 'dao', 'zonulin', 'estradiol'],
      clusters: ['D'],
      isCrossPanel: true,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:VARIABLES:BATCH4`
- File now contains all 5 cross-panel variable entry keys: `'hpa-axis'`, `'pregnenolone-steal'`, `'oxidative-stress'`, `'hepatic-detox'`, `'histamine-dao-system'`
- All 5 entries have `isCrossPanel: true`
- All 5 entries have panel code `'CROSS'` and panelColor `'#94a3b8'`
- All 4 variable batch placeholders (`BATCH1`–`BATCH4`) are now gone from the file
- The `// PLACEHOLDER:CLUSTERS` placeholder still exists in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-26"`
- `pendingSteps`: remove `"step-26"`
- `flags.variablesBatch4`: set to `true`
- `artifacts.variableCount`: increment by `5`
- `dataChunks.variables.batch4`: set to `["hpa-axis","pregnenolone-steal","oxidative-stress","hepatic-detox","histamine-dao-system"]`
