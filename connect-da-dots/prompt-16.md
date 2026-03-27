# Prompt 16: Write JS — Symptom Data: Energy & Fatigue + Sleep Categories (11 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:SYMPTOMS:BATCH1` in `fdn-pwa/index.html` with the 11 symptom entries below.

Each entry follows this exact JavaScript object structure:
```javascript
'symptom-id': {
  label: 'Display label shown in UI',
  category: 'Category Name',
  variables: ['variable-id-1', 'variable-id-2'],  // IDs from DATA.variables
  clusters: ['A', 'B'],                             // Capital letters only
  interpretation: '2-3 sentence practitioner-voice explanation.',
  mechanismTree: 'Root mechanism\n└─ Secondary pathway\n   └─ Tertiary effect'
},
```

**Valid variable IDs** (only use these exact strings): `indican`, `urinary-bile-acids`, `ohdg`, `histamine-mba`, `dao`, `zonulin`, `cortisol-diurnal`, `dhea`, `testosterone`, `estradiol`, `progesterone`, `melatonin`, `sigas-shp`, `hpylori`, `candida`, `parasites`, `dysbiotic-bacteria`, `commensal-bacteria`, `calprotectin`, `beta-glucuronidase`, `anti-gliadin-iga`, `sigas-gi`, `occult-blood`, `hpa-axis`, `pregnenolone-steal`, `oxidative-stress`, `hepatic-detox`, `histamine-dao-system`

Write ALL 11 entries replacing `// PLACEHOLDER:SYMPTOMS:BATCH1`:

```javascript
    'always-tired': {
      label: 'Always tired',
      category: 'Energy & Fatigue',
      variables: ['cortisol-diurnal', 'dhea', 'hpa-axis', 'sigas-shp', 'indican', 'ohdg', 'hepatic-detox'],
      clusters: ['A', 'B'],
      interpretation: 'Persistent fatigue without a clear cause reflects convergence of HPA dysregulation depleting cortisol reserve, GI-driven amino acid theft reducing neurotransmitter production, and accumulated oxidative damage impairing mitochondrial ATP output. This is the signature multi-system presentation in functional exhaustion. The practitioner should map which driver is upstream by examining cortisol diurnal pattern shape alongside Indican and 8-OHdG values together.',
      mechanismTree: 'HPA Dysregulation (Cortisol Diurnal Pattern flat or inverted)\n└─ Pregnenolone Steal → DHEA depletion\n   └─ Anabolic collapse → exercise intolerance, motivational fatigue\nGI Dysbiosis (Indican elevation)\n└─ Tryptophan theft by bacteria → serotonin/melatonin deficit\n   └─ Neurotransmitter depletion → non-restorative sleep, mood-fatigue loop\nOxidative Burden (8-OHdG)\n└─ Mitochondrial DNA damage\n   └─ Reduced ATP synthesis → cellular energy deficit'
    },
    'afternoon-energy-crash': {
      label: 'Afternoon energy crash',
      category: 'Energy & Fatigue',
      variables: ['cortisol-diurnal', 'indican'],
      clusters: ['B'],
      interpretation: 'A reproducible post-lunch energy collapse is a hallmark of cortisol diurnal dysfunction — specifically a premature afternoon cortisol drop rather than the physiologically sustained curve. Blood glucose instability (not directly measured in the 5-panel system) compounds this when GI dysbiosis impairs bile acid function and carbohydrate metabolism. The Indican value provides context: elevated Indican suggests SIBO-driven hypomotility and impaired nutrient absorption that worsens glucose regulation.',
      mechanismTree: 'Cortisol Diurnal Pattern (premature afternoon drop)\n└─ Loss of cortisol-driven glucose counter-regulation\n   └─ Blood glucose crash → fatigue, carbohydrate craving\nGI Dysbiosis (Indican)\n└─ Bile acid disruption (see Urinary Bile Acids)\n   └─ Fat and carbohydrate malabsorption → worsened glucose instability'
    },
    'cant-get-out-of-bed': {
      label: "Can't get out of bed in the morning",
      category: 'Energy & Fatigue',
      variables: ['cortisol-diurnal', 'dhea', 'melatonin'],
      clusters: ['B'],
      interpretation: 'Difficulty mobilizing in the morning reflects a blunted cortisol awakening response — the normal cortisol spike that occurs within 30 minutes of waking is absent or severely reduced in HPA exhaustion phases 3 and 4. Low DHEA compounds this by removing the anabolic counterbalance. Melatonin dysregulation is the third vector: elevated nocturnal melatonin extending past wake time, often seen when GI dysbiosis drives ectopic melatonin production.',
      mechanismTree: 'HPA Axis (Cortisol Awakening Response blunted)\n└─ Loss of morning cortisol surge\n   └─ Inability to mobilize glucose and energy for morning activity\nDHEA depletion\n└─ Catabolic dominance overnight\n   └─ Morning stiffness, motivational paralysis\nMelatonin dysregulation\n└─ Circadian rhythm phase delay\n   └─ Melatonin not cleared by wake time → grogginess'
    },
    'wired-but-tired': {
      label: 'Wired but tired',
      category: 'Energy & Fatigue',
      variables: ['cortisol-diurnal', 'hpa-axis', 'melatonin'],
      clusters: ['B'],
      interpretation: 'The paradox of feeling simultaneously exhausted and mentally activated is a classic HPA Phase 2 (Resistance) or early Phase 3 (Exhaustion) signature. Cortisol is dysregulated — often elevated in the evening when it should be falling — while the body is physically depleted. This evening cortisol elevation directly suppresses melatonin production, preventing the neurological wind-down needed for restorative sleep. The practitioner should look for a cortisol pattern with late-day elevation despite morning blunting.',
      mechanismTree: 'HPA Phase 2–3 Dysregulation\n└─ Evening cortisol elevation (inverted diurnal pattern)\n   └─ Sympathetic nervous system activation → mental alertness\nMelatonin suppression (by elevated evening cortisol)\n└─ Failure of circadian wind-down\n   └─ Physical exhaustion + neurological hyperarousal simultaneously'
    },
    'exercise-makes-worse': {
      label: 'Exercise makes me worse',
      category: 'Energy & Fatigue',
      variables: ['ohdg', 'oxidative-stress', 'dhea', 'cortisol-diurnal'],
      clusters: ['A', 'B'],
      interpretation: 'Post-exertional malaise — where exercise reliably worsens rather than improves wellbeing — indicates the oxidative stress burden is already exceeding the body\'s antioxidant and repair capacity. Exercise generates reactive oxygen species; when the baseline 8-OHdG is elevated, this additional oxidative load causes net tissue damage rather than adaptation. DHEA depletion removes the primary anabolic hormone needed for post-exercise repair and muscle protein synthesis.',
      mechanismTree: 'Oxidative Stress Cascade (8-OHdG elevated)\n└─ Exercise generates additional ROS beyond repair capacity\n   └─ Net mitochondrial and DNA damage → post-exertional fatigue\nDHEA depletion\n└─ Loss of anabolic signaling\n   └─ Failure to mount protein synthesis response post-exercise\nCortisol dysregulation\n└─ Exercise-triggered cortisol spike in depleted system\n   └─ Catabolic dominance → muscle breakdown, not rebuilding'
    },
    'no-motivation-or-drive': {
      label: 'No motivation or drive',
      category: 'Energy & Fatigue',
      variables: ['dhea', 'testosterone', 'hpa-axis', 'indican'],
      clusters: ['A', 'B'],
      interpretation: 'Loss of motivation and drive at a neurochemical level reflects depletion of both the anabolic hormones (DHEA, testosterone) and the neurotransmitter precursors required for dopamine and serotonin synthesis. Indican elevation signals bacterial tryptophan theft — tryptophan is the precursor to serotonin AND the kynurenine pathway, so its depletion simultaneously reduces serotonin and increases neuroinflammatory metabolites. HPA axis dysregulation compounds this by sustaining a cortisol-dominant catabolic state.',
      mechanismTree: 'Indican (SIBO/dysbiosis)\n└─ Bacterial tryptophan catabolism → serotonin precursor depletion\n   └─ Dopamine pathway cross-depletion → motivational anhedonia\nDHEA + Testosterone depletion (via Pregnenolone Steal)\n└─ Loss of anabolic drive signaling\n   └─ Physical and motivational inertia\nHPA Dysregulation\n└─ Sustained cortisol elevation → cortisolergic dominance\n   └─ Reward circuit suppression → apathy'
    },
    'cant-fall-asleep': {
      label: "Can't fall asleep",
      category: 'Sleep',
      variables: ['melatonin', 'cortisol-diurnal', 'hpa-axis', 'histamine-mba'],
      clusters: ['B', 'D'],
      interpretation: 'Sleep onset insomnia is driven by two independent physiological vectors that frequently co-occur: HPA-driven evening cortisol elevation suppressing melatonin production, and histamine-mediated CNS arousal. Histamine is a potent wakefulness neurotransmitter; elevated systemic histamine (from mucosal barrier breakdown) activates H1 receptors in the hypothalamus, maintaining the arousal state. The practitioner should examine both the cortisol diurnal pattern shape and histamine/DAO levels to determine primary driver.',
      mechanismTree: 'HPA Dysregulation (evening cortisol not falling)\n└─ Cortisol directly suppresses pineal melatonin secretion\n   └─ Absence of sleep-onset melatonin surge → can\'t cross into sleep\nHistamine load (Histamine-MBA elevated)\n└─ H1 receptor activation in tuberomammillary nucleus\n   └─ Sustained histaminergic arousal → racing mind at night\nCombined effect\n└─ Cortisol + histamine synergistically maintain wakefulness'
    },
    'wake-up-1-3am': {
      label: 'Wake up between 1–3am',
      category: 'Sleep',
      variables: ['cortisol-diurnal', 'hepatic-detox'],
      clusters: ['A', 'B'],
      interpretation: 'Waking reliably between 1 and 3am is the traditional TCM liver window — and biochemically corresponds to two mechanisms: cortisol-mediated counter-regulatory surges in response to nocturnal blood glucose drops, and hepatic detoxification surges that generate metabolite-driven arousal signals. When Hepatic Detox Impairment is present, Phase I intermediates accumulate in the small hours and trigger sympathetic activation. Blood glucose dysregulation (not directly measured but inferred from Cortisol Diurnal Pattern and Indican) is the third vector.',
      mechanismTree: 'Cortisol Diurnal Pattern (reactive nocturnal surge)\n└─ Blood glucose drops overnight\n   └─ Cortisol counter-regulatory spike at 1–3am → waking\nHepatic Detoxification Impairment\n└─ Phase I metabolite accumulation peaks during liver\'s peak processing window\n   └─ Reactive oxygen species + sympathetic activation → arousal\nGI Dysbiosis (Indican, implied)\n└─ Impaired bile acid conjugation → fat malabsorption → unstable overnight glucose'
    },
    'never-feel-rested': {
      label: 'Never feel rested',
      category: 'Sleep',
      variables: ['melatonin', 'cortisol-diurnal', 'ohdg', 'histamine-mba'],
      clusters: ['B', 'D'],
      interpretation: 'Non-restorative sleep — sleeping adequate hours but waking unrefreshed — reflects the failure of deep NREM and REM architecture rather than simple sleep duration. Melatonin dysregulation impairs the circadian signal that gates REM sleep timing. Elevated 8-OHdG indicates ongoing mitochondrial oxidative damage that impairs the cellular repair processes that are supposed to occur during sleep. Histamine elevation fragmented sleep architecture by triggering micro-arousals throughout the night.',
      mechanismTree: 'Melatonin dysregulation\n└─ Impaired REM sleep gating\n   └─ Reduced slow-wave and REM sleep stages → no cellular restoration\n8-OHdG (Oxidative DNA damage)\n└─ Mitochondrial repair machinery overwhelmed during sleep\n   └─ Waking with accumulated oxidative deficit\nHistamine load\n└─ H1-mediated micro-arousals throughout sleep architecture\n   └─ Sleep fragmentation → no sustained deep sleep'
    },
    'vivid-dreams-nightmares': {
      label: 'Vivid dreams or nightmares',
      category: 'Sleep',
      variables: ['hpa-axis', 'cortisol-diurnal'],
      clusters: ['B'],
      interpretation: 'Vivid dreams and nightmares are a functional marker of HPA activation during sleep — specifically, cortisol surges during REM sleep increase dream intensity and emotional content. This reflects HPA Phase 2 (Resistance) hyperactivation where the stress axis continues firing during sleep phases when it should be suppressed. The practitioner should examine whether cortisol elevations occur at the 11pm and/or 3am data points on the diurnal panel.',
      mechanismTree: 'HPA Dysregulation (cortisol intrusion into REM)\n└─ Cortisol elevation during REM windows (11pm–3am)\n   └─ Amygdala hyperactivation → emotionally intense dream content\nCortisol Diurnal Pattern (night-time elevation)\n└─ Loss of normal nocturnal cortisol nadir\n   └─ Sustained sympathetic tone during REM sleep → nightmare threshold lowered'
    },
    'need-10-hours-still-tired': {
      label: 'Need 10+ hours and still tired',
      category: 'Sleep',
      variables: ['hpa-axis', 'dhea', 'sigas-shp'],
      clusters: ['B'],
      interpretation: 'Requiring 10 or more hours of sleep without feeling restored is a hallmark of HPA Axis Phase 3 (Exhaustion) and Phase 4 (Collapse). The HPA system has lost the ability to mount an adequate cortisol awakening response; the body remains in a low-cortisol, high-sleep-pressure state for extended periods. Low sIgA-SHP confirms immune suppression secondary to chronic cortisol dysregulation. DHEA depletion removes the primary anabolic hormone needed to restore energy between sleep cycles.',
      mechanismTree: 'HPA Exhaustion/Collapse Phase (Phase 3–4)\n└─ Cortisol Awakening Response absent or severely blunted\n   └─ Body remains in sleep-pressure state past physiological wake time\nDHEA depletion\n└─ No anabolic counterbalance to catabolic overnight state\n   └─ Cellular energy cannot be replenished even with extended sleep\nsIgA-SHP (low — immune collapse)\n└─ Chronic HPA suppression of mucosal immunity\n   └─ Persistent low-grade immune activation → fatigue amplification'
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:SYMPTOMS:BATCH1`
- The file now contains all 11 symptom entry keys: `'always-tired'`, `'afternoon-energy-crash'`, `'cant-get-out-of-bed'`, `'wired-but-tired'`, `'exercise-makes-worse'`, `'no-motivation-or-drive'`, `'cant-fall-asleep'`, `'wake-up-1-3am'`, `'never-feel-rested'`, `'vivid-dreams-nightmares'`, `'need-10-hours-still-tired'`
- Each entry has `label`, `category`, `variables`, `clusters`, `interpretation`, and `mechanismTree` fields
- No entry has placeholder text such as `// ...` or `TODO`
- The other 6 symptom batch placeholders (`BATCH2` through `BATCH7`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-16"`
- `pendingSteps`: remove `"step-16"`
- `flags.symptomsBatch1`: set to `true`
- `artifacts.symptomCount`: increment by `11`
- `dataChunks.symptoms.batch1`: set to `["always-tired","afternoon-energy-crash","cant-get-out-of-bed","wired-but-tired","exercise-makes-worse","no-motivation-or-drive","cant-fall-asleep","wake-up-1-3am","never-feel-rested","vivid-dreams-nightmares","need-10-hours-still-tired"]`
