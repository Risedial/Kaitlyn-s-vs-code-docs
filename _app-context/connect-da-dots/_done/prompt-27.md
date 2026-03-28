# Prompt 27: Write JS — Cluster Data: All 5 Root Cause Clusters

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:CLUSTERS` in `fdn-pwa/index.html` with the 5 root cause cluster entries below.

Each cluster entry follows this structure:
```javascript
'LETTER': {
  letter: 'LETTER',           // single capital letter
  name: 'Short name',
  fullName: 'Cluster X — Full Name (Role)',
  color: '#hexcolor',         // exact cluster color from design system
  mechanism: 'Mechanism description...',
  priorityNote: 'Priority note string, or null',
  variables: ['variable-id-1', ...]   // IDs from DATA.variables
},
```

Cluster colors (use exactly):
- A: `#ef4444` (red)
- B: `#f97316` (orange)
- C: `#ec4899` (pink)
- D: `#06b6d4` (cyan)
- E: `#fbbf24` (amber/warning)

Write ALL 5 entries replacing `// PLACEHOLDER:CLUSTERS`:

```javascript
    'A': {
      letter: 'A',
      name: 'GI Ecosystem Collapse',
      fullName: 'Cluster A — GI Ecosystem Collapse (Primary Driver)',
      color: '#ef4444',
      mechanism: 'Pathogenic overgrowth collapses colonization resistance → drives intestinal permeability (Zonulin elevation) → antigen and LPS translocation into systemic circulation → systemic immune activation + toxin recirculation → amplifies all downstream clusters. H. pylori is the highest-priority pathogen: clear before addressing all other GI-MAP findings. GI Ecosystem Collapse is the upstream driver of systemic dysfunction in the FDN model — address before all other clusters.',
      priorityNote: 'Address before all other clusters. GI dysfunction is the upstream driver of systemic dysfunction in the FDN model. H. pylori must be treated first if positive.',
      variables: ['indican', 'urinary-bile-acids', 'ohdg', 'zonulin', 'hpylori', 'candida', 'parasites', 'dysbiotic-bacteria', 'commensal-bacteria', 'anti-gliadin-iga', 'sigas-gi', 'hepatic-detox', 'oxidative-stress']
    },
    'B': {
      letter: 'B',
      name: 'HPA-Immune Loop',
      fullName: 'Cluster B — HPA-Immune Loop (Amplifier)',
      color: '#f97316',
      mechanism: 'Chronic stress → cortisol dysregulation progressing through 5 phases (Alarm → Resistance → Exhaustion → Collapse → Recovery) → immune suppression via sIgA depletion + sex hormone depletion via Pregnenolone Steal + circadian rhythm disruption via melatonin suppression → self-perpetuating loop. Each HPA phase produces a distinct symptom and biomarker pattern. The HPA-Immune Loop amplifies all other cluster dysfunctions simultaneously.',
      priorityNote: null,
      variables: ['cortisol-diurnal', 'dhea', 'testosterone', 'melatonin', 'sigas-shp', 'hpa-axis', 'pregnenolone-steal', 'sigas-gi']
    },
    'C': {
      letter: 'C',
      name: 'Estrogen Recycling Loop',
      fullName: 'Cluster C — Estrogen Recycling Loop (Cross-Panel)',
      color: '#ec4899',
      mechanism: 'Elevated Beta-glucuronidase (dysbiotic bacteria in GI-MAP) deconjugates Phase II estrogen metabolites in the gut lumen → reabsorbed deconjugated estrogens re-enter portal circulation as active estrogens → systemic estrogen dominance despite potentially normal production levels → symptoms of excess estrogen (heavy periods, PMS, fibrocystic breasts, weight at hips) + progesterone insufficiency (anxiety, poor sleep, infertility). Hepatic Detoxification Impairment amplifies the recycling loop by slowing Phase II conjugation.',
      priorityNote: null,
      variables: ['estradiol', 'progesterone', 'beta-glucuronidase', 'hepatic-detox']
    },
    'D': {
      letter: 'D',
      name: 'Mucosal Barrier Breakdown',
      fullName: 'Cluster D — Mucosal Barrier Breakdown (Histamine)',
      color: '#06b6d4',
      mechanism: 'Mucosal destruction → DAO enzyme-producing enterocyte loss → histamine accumulates unmetabolized → vasoactive and neuroactive histamine reaches systemic circulation → symptoms across cardiovascular (palpitations, blood pressure), neurological (anxiety, brain fog, sensitivity), respiratory (rhinitis, bronchospasm), and skin (hives, flushing, eczema) systems. Zonulin-mediated gut barrier disruption amplifies by allowing additional allergen sensitization.',
      priorityNote: null,
      variables: ['histamine-mba', 'dao', 'zonulin', 'histamine-dao-system']
    },
    'E': {
      letter: 'E',
      name: 'Structural GI Pathology',
      fullName: 'Cluster E — Structural GI Pathology (Medical Referral)',
      color: '#fbbf24',
      mechanism: 'Elevated Calprotectin/Lactoferrin or Occult Blood >10 µg/g indicates structural GI pathology that must be evaluated by a physician before any FDN interventions proceed. These findings can represent inflammatory bowel disease (Crohn\'s, ulcerative colitis), colorectal polyps, adenocarcinoma, or bleeding lesions. These are referral triggers, not FDN intervention triggers. The practitioner\'s role is to immediately refer and coordinate with the treating physician.',
      priorityNote: 'MEDICAL REFERRAL REQUIRED. Elevated Calprotectin/Lactoferrin or Occult Blood >10 µg/g — refer to physician before any FDN interventions.',
      variables: ['calprotectin', 'occult-blood']
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:CLUSTERS`
- File now contains all 5 cluster entry keys: `'A'`, `'B'`, `'C'`, `'D'`, `'E'`
- Cluster A `variables` array contains 13 IDs including `'hpylori'`, `'zonulin'`, `'oxidative-stress'`, `'hepatic-detox'`
- Cluster B `variables` array contains 8 IDs including `'hpa-axis'` and `'pregnenolone-steal'`
- Cluster C `variables` array contains exactly 4 IDs: `'estradiol'`, `'progesterone'`, `'beta-glucuronidase'`, `'hepatic-detox'`
- Cluster D `variables` array contains exactly 4 IDs: `'histamine-mba'`, `'dao'`, `'zonulin'`, `'histamine-dao-system'`
- Cluster E `variables` array contains exactly 2 IDs: `'calprotectin'`, `'occult-blood'`
- Cluster E `priorityNote` mentions `'MEDICAL REFERRAL REQUIRED'`

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-27"`
- `pendingSteps`: remove `"step-27"`
- `flags.clusterData`: set to `true`
- `artifacts.clusterCount`: set to `5`
- `dataChunks.clusters`: set to `{"A": ["indican","urinary-bile-acids","ohdg","zonulin","hpylori","candida","parasites","dysbiotic-bacteria","commensal-bacteria","anti-gliadin-iga","sigas-gi","hepatic-detox","oxidative-stress"], "B": ["cortisol-diurnal","dhea","testosterone","melatonin","sigas-shp","hpa-axis","pregnenolone-steal","sigas-gi"], "C": ["estradiol","progesterone","beta-glucuronidase","hepatic-detox"], "D": ["histamine-mba","dao","zonulin","histamine-dao-system"], "E": ["calprotectin","occult-blood"]}`
