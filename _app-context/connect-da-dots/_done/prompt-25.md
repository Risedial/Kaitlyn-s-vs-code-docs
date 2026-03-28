# Prompt 25: Write JS — Variable Data: GI-MAP Panel (10 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:VARIABLES:BATCH3` in `fdn-pwa/index.html` with the 10 GI-MAP panel variable entries below.

**CRITICAL FLAGS**:
- `hpylori`: `isPriorityPathogen: true` — this triggers the priority pathogen alert banner in the UI
- `calprotectin`: `isMedicalReferral: true` — this triggers the medical referral alert banner
- `occult-blood`: `isMedicalReferral: true` — this triggers the medical referral alert banner

Write ALL 10 entries replacing `// PLACEHOLDER:VARIABLES:BATCH3`:

```javascript
    'hpylori': {
      name: 'H. pylori',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Ulcerogenic gastric pathogen — HIGHEST PRIORITY PATHOGEN in FDN',
      elevated: 'TREAT FIRST. H. pylori disrupts gastric acid via ammonia production, collapses colonization resistance for the entire GI tract, impairs protein digestion, produces VacA cytotoxin causing epithelial damage, and triggers upstream dysfunction across all other GI-MAP findings. No other GI-MAP findings should be addressed until H. pylori is cleared.',
      low: 'N/A — negative H. pylori is the expected baseline',
      connections: ['candida', 'dysbiotic-bacteria', 'indican', 'sigas-gi'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: true,
      isMedicalReferral: false
    },
    'candida': {
      name: 'Candida',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Opportunistic yeast — indicator of immune suppression and dysbiosis',
      elevated: 'Dysbiosis and immune suppression enabling opportunistic yeast overgrowth. Associated with: antibiotic use history, elevated cortisol (HPA-driven immune suppression), low sIgA-GI, and high sugar/refined carbohydrate diet. Candida overgrowth in GI-MAP can disseminate to vaginal, oral, and skin surfaces when systemic immunity is also impaired.',
      low: 'N/A — absent or low Candida is expected baseline',
      connections: ['sigas-gi', 'hpa-axis', 'dysbiotic-bacteria'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'parasites': {
      name: 'Parasites',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'GI parasitic load — immune activation and barrier disruption',
      elevated: 'Active parasitic infection. Produces: osmotic diarrhea via villous destruction, immune activation driving sIgA depletion, Zonulin-mediated gut barrier disruption, malabsorption of nutrients. Multiple parasitic species may co-occur. Address alongside H. pylori prioritization.',
      low: 'N/A — absent parasites is expected baseline',
      connections: ['sigas-gi', 'zonulin', 'calprotectin'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'dysbiotic-bacteria': {
      name: 'Dysbiotic Bacteria',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Pathobiont bacterial overgrowth — driver of fermentation, histamine, and estrogen recycling',
      elevated: 'Elevated dysbiotic bacteria drive: Indican production (protein fermentation → tryptophan theft), Beta-glucuronidase activity (estrogen deconjugation → Cluster C amplification), excess histamine production from dietary histidine, and direct mucosal barrier disruption. Pattern recognition is key: which species are elevated reveals mechanism (methane producers → constipation; hydrogen producers → diarrhea; histamine producers → histamine symptoms).',
      low: 'N/A — low or absent dysbiotic bacteria is the expected baseline',
      connections: ['indican', 'beta-glucuronidase', 'histamine-mba', 'sigas-gi'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'commensal-bacteria': {
      name: 'Commensal Bacteria',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Beneficial microbiome composition — SCFA production, immune training, barrier support',
      elevated: 'N/A — healthy commensal populations are beneficial; high diversity is the goal',
      low: 'SCFA (short-chain fatty acid) deficit → colonocyte energy failure → mucosal barrier breakdown. Impaired immune training → dysregulated immune response. sIgA suppression. Loss of colonization resistance against pathogens. Low commensal bacteria confirms the microbiome foundation is compromised and must be addressed as part of GI restoration.',
      connections: ['sigas-gi', 'zonulin', 'indican'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'calprotectin': {
      name: 'Calprotectin / Lactoferrin',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Neutrophil-derived GI inflammation marker — structural pathology indicator',
      elevated: 'MEDICAL REFERRAL REQUIRED. Elevated Calprotectin/Lactoferrin indicates active neutrophilic intestinal inflammation — distinguishing active IBD (Crohn\'s, ulcerative colitis), infectious colitis, or other structural GI pathology from functional GI disorders. Do NOT apply FDN interventions for GI findings until physician evaluation confirms absence of structural pathology.',
      low: 'N/A — low Calprotectin is expected in the absence of active intestinal inflammation',
      connections: ['occult-blood'],
      clusters: ['E'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: true
    },
    'beta-glucuronidase': {
      name: 'Beta-glucuronidase',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Bacterial enzyme deconjugating Phase II estrogen metabolites — Cluster C primary driver',
      elevated: 'Estrogen recycling loop active: deconjugated Phase II estrogen metabolites re-absorbed from gut → elevated systemic estradiol → estrogen dominance symptoms (Cluster C). Also recirculates other hepatically conjugated toxins. Elevated Beta-glucuronidase is the key GI-MAP finding linking gut dysbiosis to hormonal dysfunction.',
      low: 'N/A — low Beta-glucuronidase is expected baseline',
      connections: ['estradiol', 'hepatic-detox', 'dysbiotic-bacteria'],
      clusters: ['C'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'anti-gliadin-iga': {
      name: 'Anti-gliadin IgA',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Local mucosal immune response to gliadin — gluten/cross-reactive food reactivity marker',
      elevated: 'Mucosal immune reactivity to gliadin protein (wheat). May indicate: celiac disease (confirm with systemic anti-tTG/anti-EMA), non-celiac gluten sensitivity, or cross-reactive food reactivity (casein). Must be interpreted alongside sIgA-GI — if both are low, false negative risk is high.',
      low: 'If sIgA-GI is also low: likely false negative — immune collapse prevents mounting even a local IgA response. Do not interpret low Anti-gliadin IgA as "no gluten reactivity" when sIgA-GI is simultaneously suppressed.',
      connections: ['sigas-gi', 'zonulin'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'sigas-gi': {
      name: 'sIgA (GI — Stool)',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Stool mucosal immune defense — gut immune competence marker',
      elevated: 'Active acute immune challenge — immune system mounting appropriate sIgA response to pathogen. Context-dependent: elevated sIgA-GI in presence of active infection is appropriate and reassuring.',
      low: 'Chronic pathogen burden overwhelming sIgA production, or HPA-driven cortisol suppression of mucosal immunity (shared mechanism with sIgA-SHP). Low sIgA-GI removes the primary gut immune exclusion barrier. Also: false negative risk for all antigen-specific tests (Anti-gliadin IgA) when sIgA-GI is low.',
      connections: ['sigas-shp', 'hpa-axis', 'anti-gliadin-iga', 'zonulin'],
      clusters: ['A', 'B'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'occult-blood': {
      name: 'Occult Blood',
      panel: 'GIMAP',
      panelColor: '#22c55e',
      description: 'Fecal hemoglobin — structural mucosal bleeding marker',
      elevated: 'MEDICAL REFERRAL REQUIRED IMMEDIATELY. Occult Blood >10 µg/g indicates structural mucosal bleeding. Differential includes: colorectal cancer, polyps, IBD with mucosal ulceration, bleeding lesion. This is NOT a functional GI finding — FDN interventions must not proceed until physician evaluation excludes structural pathology.',
      low: 'N/A — occult blood below threshold is expected baseline',
      connections: ['calprotectin'],
      clusters: ['E'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: true
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:VARIABLES:BATCH3`
- File now contains all 10 GI-MAP variable entry keys: `'hpylori'`, `'candida'`, `'parasites'`, `'dysbiotic-bacteria'`, `'commensal-bacteria'`, `'calprotectin'`, `'beta-glucuronidase'`, `'anti-gliadin-iga'`, `'sigas-gi'`, `'occult-blood'`
- `hpylori` has `isPriorityPathogen: true`
- `calprotectin` has `isMedicalReferral: true`
- `occult-blood` has `isMedicalReferral: true`
- `isCrossPanel` is `false` for all 10 entries
- The variable batch placeholder `BATCH4` still exists in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-25"`
- `pendingSteps`: remove `"step-25"`
- `flags.variablesBatch3`: set to `true`
- `artifacts.variableCount`: increment by `10`
- `dataChunks.variables.batch3`: set to `["hpylori","candida","parasites","dysbiotic-bacteria","commensal-bacteria","calprotectin","beta-glucuronidase","anti-gliadin-iga","sigas-gi","occult-blood"]`
