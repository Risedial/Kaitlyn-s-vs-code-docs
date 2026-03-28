# Prompt 24: Write JS — Variable Data: SHP Panel (7 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:VARIABLES:BATCH2` in `fdn-pwa/index.html` with the 7 SHP (Stress Hormone Panel) variable entries below.

**IMPORTANT**: Two entries in this batch are CROSS-PANEL CONSTRUCTS and must have `isCrossPanel: true`. These are `hpa-axis` (HPA Axis Dysregulation Pattern) and `pregnenolone-steal` (Pregnenolone Steal and Steroidogenesis Disruption).

Write ALL 7 entries replacing `// PLACEHOLDER:VARIABLES:BATCH2`:

```javascript
    'cortisol-diurnal': {
      name: 'Cortisol Diurnal Pattern',
      panel: 'SHP',
      panelColor: '#8b5cf6',
      description: '4-point salivary cortisol arc measuring diurnal rhythm integrity',
      elevated: 'Overall elevated: acute or compensatory stress phase (Phase 1–2 HPA). Elevated at specific time points: morning spike → alarm phase; evening elevation → inverted pattern, sleep disruption, anxiety. Must interpret each time point in context of full arc shape.',
      low: 'Overall low / flat pattern: adrenal exhaustion (Phase 3–4 HPA). Flat cortisol is the hallmark of burnout, emotional numbness, orthostatic hypotension, and inability to mobilize morning energy. All four time points near or below low-normal = Collapse phase.',
      connections: ['dhea', 'hpa-axis', 'pregnenolone-steal', 'sigas-shp'],
      clusters: ['B'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'dhea': {
      name: 'DHEA',
      panel: 'SHP',
      panelColor: '#8b5cf6',
      description: 'Anabolic neurosteroid — counterbalance to cortisol catabolic dominance',
      elevated: 'N/A — not clinically significant in isolation in the FDN context. Elevated DHEA alone is not a common FDN finding.',
      low: 'Catabolic dominance: DHEA depletion removes the anabolic counterbalance to cortisol. Results in immune suppression, muscle wasting, fatigue, accelerated aging, emotional blunting, reduced resilience. DHEA is the primary marker of chronic stress progression severity. Depleted via Pregnenolone Steal.',
      connections: ['hpa-axis', 'pregnenolone-steal', 'testosterone'],
      clusters: ['B'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'testosterone': {
      name: 'Testosterone',
      panel: 'SHP',
      panelColor: '#8b5cf6',
      description: 'Anabolic hormone — primary in males, secondary role in females',
      elevated: 'N/A in typical FDN context for males. In females: elevated testosterone may indicate PCOS-related androgen excess or estrogen recycling feedback.',
      low: 'Fatigue, low libido, muscle loss, depression, reduced motivation and drive. In males: primary androgen deficiency. In both sexes: secondary to Pregnenolone Steal diverting substrate from testosterone synthesis. Assess alongside DHEA and cortisol to determine HPA vs. primary gonadal etiology.',
      connections: ['dhea', 'pregnenolone-steal', 'hpa-axis'],
      clusters: ['B'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'estradiol': {
      name: 'Estradiol',
      panel: 'SHP',
      panelColor: '#8b5cf6',
      description: 'Primary estrogen — measured in SHP but mechanistically central to Cluster C',
      elevated: 'Cluster C estrogen recycling via elevated Beta-glucuronidase deconjugating Phase II metabolites. Estrogen dominance: weight at hips, fibrocystic breasts, heavy periods, PMS, water retention. Also: early follicular phase elevation, estrogen-sensitive condition.',
      low: 'Menopause, perimenopause, or HPA-driven suppression (Pregnenolone Steal). Hot flashes, vaginal atrophy, bone density loss, mood changes. Low in context of high cortisol confirms Pregnenolone Steal mechanism.',
      connections: ['beta-glucuronidase', 'progesterone', 'hepatic-detox', 'pregnenolone-steal'],
      clusters: ['C'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'progesterone': {
      name: 'Progesterone',
      panel: 'SHP',
      panelColor: '#8b5cf6',
      description: 'Anti-estrogenic, calming neurosteroid — the hormonal counterbalance to estrogen',
      elevated: 'N/A — not typically a finding in functional medicine context without exogenous supplementation.',
      low: 'Anxiety, poor sleep, heavy periods, PMS, infertility, luteal phase insufficiency. Progesterone is the first sex hormone depleted by Pregnenolone Steal. Low progesterone removes the calming GABA-A receptor modulating effect of allopregnanolone (progesterone metabolite), producing anxiety and sleep disruption.',
      connections: ['estradiol', 'hpa-axis', 'pregnenolone-steal', 'beta-glucuronidase'],
      clusters: ['C'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'melatonin': {
      name: 'Melatonin',
      panel: 'SHP',
      panelColor: '#8b5cf6',
      description: 'Circadian rhythm hormone and endogenous antioxidant',
      elevated: 'Noon elevation (normally near zero at noon): GI dysbiosis signal — enteric nervous system dysbiosis produces ectopic melatonin secretion. Daytime melatonin = fatigue, cognitive fog, circadian inversion pattern.',
      low: 'Insomnia, non-restorative sleep, poor antioxidant capacity. Low melatonin at 11pm: circadian phase delay or cortisol suppression of pineal melatonin. Melatonin is also a potent antioxidant — its depletion amplifies oxidative burden measured by 8-OHdG.',
      connections: ['cortisol-diurnal', 'hpa-axis'],
      clusters: ['B'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'sigas-shp': {
      name: 'sIgA (SHP — Salivary)',
      panel: 'SHP',
      panelColor: '#8b5cf6',
      description: 'Salivary mucosal immune defense — HPA-controlled upstream mucosal immunity',
      elevated: 'Active acute immune challenge — the immune system is mounting an IgA response. Acutely elevated sIgA confirms immune system still functional. Context-dependent: elevated during active infection is appropriate.',
      low: 'Cortisol suppression of sIgA production (primary FDN mechanism). Chronic stress depletes salivary sIgA, removing first-line upper respiratory and oral mucosal defense. Low sIgA-SHP confirms HPA-driven immune suppression. Correlates with frequent illness, slow recovery, susceptibility to respiratory infections.',
      connections: ['hpa-axis', 'cortisol-diurnal'],
      clusters: ['B'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:VARIABLES:BATCH2`
- File now contains all 7 SHP variable entry keys: `'cortisol-diurnal'`, `'dhea'`, `'testosterone'`, `'estradiol'`, `'progesterone'`, `'melatonin'`, `'sigas-shp'`
- None of these 7 entries have `isCrossPanel: true` (the SHP cross-panel constructs come in BATCH4, not here)
- The other variable batch placeholders (`BATCH3`, `BATCH4`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-24"`
- `pendingSteps`: remove `"step-24"`
- `flags.variablesBatch2`: set to `true`
- `artifacts.variableCount`: increment by `7`
- `dataChunks.variables.batch2`: set to `["cortisol-diurnal","dhea","testosterone","estradiol","progesterone","melatonin","sigas-shp"]`
