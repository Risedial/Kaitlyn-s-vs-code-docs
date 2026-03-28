# Prompt 22: Write JS — Symptom Data: Respiratory + Cognitive & Neurological + Stress & Nervous System (11 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:SYMPTOMS:BATCH7` in `fdn-pwa/index.html` with the final 11 symptom entries below covering Respiratory, Cognitive & Neurological, and Stress & Nervous System categories. This is the LAST symptom batch — after this prompt, all 76 symptom entries will be present in the file.

Write ALL 11 entries replacing `// PLACEHOLDER:SYMPTOMS:BATCH7`:

```javascript
    'stuffy-runny-nose': {
      label: 'Stuffy nose / runny nose (not seasonal)',
      category: 'Respiratory',
      variables: ['histamine-mba', 'dao', 'zonulin', 'anti-gliadin-iga'],
      clusters: ['A', 'D'],
      interpretation: 'Perennial (non-seasonal) nasal congestion and rhinorrhea indicate chronic histamine-driven mucosal inflammation rather than pollen allergy. Histamine activates H1 receptors in nasal mucosal vasculature producing vasodilation and increased mucus secretion. Low DAO prevents clearance of dietary histamine, making symptoms diet-dependent. Zonulin-driven antigen translocation allows food antigens to reach nasal mucosal immune cells, priming IgE responses that perpetuate the histamine release. Anti-gliadin IgA elevation indicates a gluten-reactive component that may present as persistent rhinitis rather than classic GI symptoms.',
      mechanismTree: 'Histamine-MBA + Low DAO\n└─ Nasal mucosal H1 activation → vasodilation\n   └─ Increased mucus production → congestion and rhinorrhea\nZonulin (antigen translocation)\n└─ Food antigens reach nasal mucosal immune tissue\n   └─ IgE sensitization → histamine release at nasal mucosa\nAnti-gliadin IgA (elevated)\n└─ Gluten-reactive mucosal immune activation\n   └─ May present as rhinitis without classic GI symptoms (silent gluten reactivity)'
    },
    'asthma-like': {
      label: 'Asthma-like symptoms',
      category: 'Respiratory',
      variables: ['histamine-mba', 'dao', 'zonulin'],
      clusters: ['D'],
      interpretation: 'Asthma-like symptoms — bronchospasm, wheeze, tightness — without a confirmed asthma diagnosis may reflect histamine-driven bronchial smooth muscle contraction. H1 receptor activation in bronchial smooth muscle is a well-established mechanism of histamine-induced bronchospasm. When DAO is insufficient, dietary histamine reaches bronchial tissue and can trigger bronchospasm within minutes to hours of eating. Zonulin-driven antigen translocation amplifies this by allowing food and microbial antigens to sensitize bronchial mucosal immune cells, lowering the histamine threshold for bronchospasm.',
      mechanismTree: 'Histamine-MBA + Low DAO\n└─ H1 receptor activation in bronchial smooth muscle\n   └─ Bronchoconstriction → wheeze, tightness, reduced airflow\nZonulin (antigen translocation)\n└─ Bronchial mucosal sensitization to food antigens\n   └─ Food-triggered bronchospasm via IgE-mast cell-histamine cascade\nClinical pattern\n└─ Post-meal bronchospasm (within 2 hours) → histamine intolerance mechanism\n└─ Exercise-triggered bronchospasm → assess HPA/cortisol-driven oxidative component'
    },
    'post-nasal-drip': {
      label: 'Post-nasal drip',
      category: 'Respiratory',
      variables: ['histamine-mba', 'dao', 'zonulin'],
      clusters: ['D'],
      interpretation: 'Chronic post-nasal drip — excessive mucus accumulation in the posterior nasopharynx — is driven by the same histamine-mediated nasal mucosal hypersecretion as rhinitis but predominantly affects the posterior mucosal surfaces. Histamine H1 and H2 receptor activation stimulates goblet cell mucus production and mucosal gland secretion. Low DAO prevents dietary histamine clearance, making the symptom diet-responsive. The practitioner should test whether post-nasal drip resolves within 24–72 hours of a low-histamine diet; if so, DAO deficiency is likely primary.',
      mechanismTree: 'Histamine-MBA + Low DAO\n└─ H1/H2 stimulation of posterior nasal and nasopharyngeal goblet cells\n   └─ Excess mucus production pooling in posterior pharynx\nZonulin (mucosal sensitization)\n└─ Antigen translocation → mucosal immune activation at nasopharynx\n   └─ Chronic mucosal secretory state\nDiagnostic trial\n└─ Low-histamine diet for 72 hours → significant improvement confirms DAO primary driver'
    },
    'difficulty-concentrating': {
      label: 'Difficulty concentrating',
      category: 'Cognitive & Neurological',
      variables: ['indican', 'ohdg', 'histamine-mba', 'zonulin'],
      clusters: ['A', 'D'],
      interpretation: 'Difficulty concentrating reflects impairment of prefrontal cortex executive function — the most metabolically expensive and vulnerable brain region. Indican-driven tryptophan theft depletes both serotonin (required for attention maintenance) and dopamine precursors (required for working memory and executive function). 8-OHdG-measured oxidative damage impairs prefrontal mitochondrial ATP production. Histamine activates histaminergic arousal circuits that paradoxically impair focused attention — the hyperarousal state makes sustained concentration impossible. Zonulin-driven LPS neuroinflammation reduces prefrontal processing speed.',
      mechanismTree: 'Indican (neurotransmitter precursor depletion)\n└─ Tryptophan theft → serotonin + dopamine precursor deficit\n   └─ Prefrontal dopaminergic tone insufficient for sustained attention\n8-OHdG (prefrontal mitochondrial damage)\n└─ ATP deficit in highest-metabolic-demand brain region\n   └─ Cognitive processing slowed, sustained attention impossible\nHistamine-MBA (hyperarousal)\n└─ H1 histaminergic arousal circuit overstimulation\n   └─ Inability to maintain single focus → distractibility'
    },
    'word-finding-problems': {
      label: 'Word-finding problems',
      category: 'Cognitive & Neurological',
      variables: ['ohdg', 'oxidative-stress', 'indican', 'zonulin'],
      clusters: ['A', 'B'],
      interpretation: 'Anomia — difficulty retrieving specific words during speech — is an early cognitive vulnerability marker that reflects language network oxidative burden and neuroinflammatory disruption. The left hemisphere perisylvian language network is particularly vulnerable to oxidative stress because of its high metabolic demands. Systemic 8-OHdG elevation reflects oxidative damage to these neural circuits. Zonulin-driven LPS neuroinflammation specifically disrupts the semantic processing networks required for lexical access. Indican-driven amino acid depletion impairs glutamate-glutamine cycling in language network synapses.',
      mechanismTree: 'Systemic Oxidative Stress (8-OHdG)\n└─ Left perisylvian language network oxidative burden\n   └─ Lexical-semantic retrieval network impaired\n      └─ Word-finding failures, pauses, circumlocution\nZonulin (LPS neuroinflammation)\n└─ Microglial activation in language association cortex\n   └─ Semantic processing speed reduction\nIndican (amino acid depletion)\n└─ Glutamate-glutamine cycling impairment at language synapses\n   └─ Neurotransmitter release insufficiency → retrieval failure'
    },
    'sensitivity-light-sound': {
      label: 'Sensitivity to light or sound',
      category: 'Cognitive & Neurological',
      variables: ['histamine-mba', 'dao', 'hpa-axis'],
      clusters: ['B', 'D'],
      interpretation: 'Photophobia and phonophobia are sensory hypersensitivity states reflecting central sensitization driven by histamine-mediated neuroinflammation and HPA-driven autonomic hyperreactivity. Histamine directly sensitizes thalamic sensory relay neurons via H1 receptor activation — the thalamus is the gating station for all sensory input. HPA hyperactivation maintains a cortisol-driven sympathetic baseline that compresses the sensory tolerance range. This combination produces pathological sensory gating failure: stimuli that should be filtered at the thalamic level pass through and are perceived as overwhelming.',
      mechanismTree: 'Histamine-MBA (elevated)\n└─ H1 receptor activation in thalamic sensory relay neurons\n   └─ Thalamic sensory gating impaired\n      └─ Normal light/sound perceived as overwhelming\nHPA Dysregulation (sympathetic hyperarousal)\n└─ Cortisol-driven autonomic baseline elevation\n   └─ Compressed sensory tolerance range\n      └─ Hyperreactivity to previously tolerated stimuli\nCombined effect\n└─ Histaminergic sensitization + sympathetic hyperarousal\n   └─ Photophobia and phonophobia co-occurring'
    },
    'tingling-numbness': {
      label: 'Tingling or numbness',
      category: 'Cognitive & Neurological',
      variables: ['ohdg', 'oxidative-stress'],
      clusters: ['A'],
      interpretation: 'Peripheral neuropathic symptoms — tingling, numbness, pins-and-needles — in the FDN model trace to oxidative nerve damage. 8-OHdG elevation reflects DNA oxidative damage that extends to peripheral nerve mitochondria. Peripheral nerves are particularly vulnerable to oxidative mitochondrial damage because of the metabolic demands of maintaining the membrane potential along their entire length. When mitochondrial energy production is impaired by oxidative damage, peripheral nerve myelin integrity is compromised, producing the characteristic tingling and numbness of early peripheral neuropathy.',
      mechanismTree: '8-OHdG (peripheral nerve mitochondrial damage)\n└─ Myelin synthesis capacity impaired (requires mitochondrial ATP)\n   └─ Myelin sheath thinning → conduction velocity slowing\n      └─ Tingling, paresthesia\nSystemic Oxidative Stress Cascade\n└─ Reactive oxygen species attacking membrane lipids in nerve sheaths\n   └─ Progressive demyelination → numbness in terminal distribution\nClinical note\n└─ Prioritize 8-OHdG reduction (antioxidant substrate) before nerve symptoms progress'
    },
    'cant-handle-stress': {
      label: "Can't handle stress the way I used to",
      category: 'Stress & Nervous System',
      variables: ['hpa-axis', 'sigas-shp', 'dhea'],
      clusters: ['B'],
      interpretation: 'Reduced stress resilience — the consistent sense that stressors that were previously manageable now overwhelm the system — is the clinical definition of the HPA Phase 2–3 transition (Resistance to Exhaustion). The Cortisol:DHEA ratio (calculated from SHP panel values) is the key assessment tool: as DHEA falls relative to cortisol, the anabolic buffer against catabolic stress is progressively depleted. sIgA-SHP confirms downstream immune suppression — when the immune system has already become a victim of HPA dysregulation, total allostatic load increases further with each new stressor.',
      mechanismTree: 'HPA Phase 2→3 Transition\n└─ Cortisol reserve sufficient to mount but not sustain stress response\n   └─ Each stress episode depletes the cortisol reserve faster\n      └─ Recovery time between stressors extends\nDHEA (declining — Pregnenolone Steal)\n└─ Cortisol:DHEA ratio rising\n   └─ Anabolic buffer against catabolic stress progressively depleted\nsIgA-SHP (low — HPA downstream)\n└─ Immune suppression adds to total allostatic load\n   └─ Body managing stress + immune challenge simultaneously'
    },
    'burnout': {
      label: 'Burnout',
      category: 'Stress & Nervous System',
      variables: ['hpa-axis', 'cortisol-diurnal', 'dhea', 'sigas-shp'],
      clusters: ['B'],
      interpretation: 'Clinical burnout is HPA Phase 3–4 (Exhaustion-Collapse) with characteristic flat cortisol pattern and severely depleted anabolic hormones. The cortisol diurnal pattern in burnout typically shows all four time points clustering at or below low-normal, or an inverted pattern with the highest value at bedtime. DHEA is typically severely suppressed. sIgA-SHP confirms the immune collapse component that distinguishes burnout from ordinary fatigue. The practitioner should treat this as a medical-level HPA restoration priority before addressing any other dysfunctional patterns.',
      mechanismTree: 'HPA Phase 3–4 (Exhaustion-Collapse)\n└─ Cortisol diurnal pattern: flat or inverted\n   └─ Cortisol Awakening Response absent\n      └─ Cannot mobilize for demands of daily life\nDHEA severely depleted\n└─ Complete anabolic collapse\n   └─ No emotional or physical resilience substrate\nsIgA-SHP (very low — immune collapse confirmed)\n└─ Mucosal immunity completely suppressed\n   └─ Vulnerable to opportunistic infections while depleted\nClinical priority\n└─ HPA Phase 4 Collapse is a restoration priority — all other interventions secondary'
    },
    'panic-attacks': {
      label: 'Panic attacks',
      category: 'Stress & Nervous System',
      variables: ['histamine-mba', 'hpa-axis', 'cortisol-diurnal'],
      clusters: ['B', 'D'],
      interpretation: 'Panic attacks are acute autonomic storms that in the FDN model are most commonly triggered by acute histamine vasoactive release combined with an already-hyperactivated HPA axis. Histamine produces sudden vasodilation in cerebral and cardiac vasculature, which is interpreted by the nervous system as cardiovascular emergency — triggering the panic cascade: adrenaline release, hyperventilation, palpitations. An already-hyperactivated HPA system (cortisol elevated, sympathetic baseline high) dramatically lowers the threshold for histamine-triggered panic. The practitioner should assess post-meal timing and histamine-rich food associations.',
      mechanismTree: 'Histamine-MBA (acute vasoactive release)\n└─ Sudden cerebral vasodilation → autonomic alarm signal\n   └─ Epinephrine counter-release → palpitations, hyperventilation\n      └─ Panic cascade triggered\nHPA Hyperactivation (baseline)\n└─ Cortisol-sustained sympathetic tone\n   └─ Compressed panic threshold → minor histamine spike triggers full attack\nCombined Cluster B + D\n└─ HPA-primed sympathetic baseline + histamine trigger\n   └─ Post-meal panic (within 30–60 min of histamine-rich food) — key clinical pattern'
    },
    'feel-cant-relax': {
      label: "Feel like I can't relax",
      category: 'Stress & Nervous System',
      variables: ['hpa-axis', 'cortisol-diurnal', 'histamine-mba', 'melatonin'],
      clusters: ['B', 'D'],
      interpretation: 'Persistent inability to relax — muscle tension, racing thoughts, difficulty winding down even in safe environments — reflects sustained HPA activation maintaining a cortisol-driven sympathetic baseline combined with histamine-mediated neurological arousal. Cortisol maintains the physiological state of preparedness: muscles tensed, mind scanning, arousal systems activated. Melatonin deficiency (low) removes the primary circadian signal that normally initiates physiological wind-down in the evening. Elevated histamine maintains histaminergic hypothalamic arousal circuits in the active state.',
      mechanismTree: 'HPA Dysregulation (cortisol elevated)\n└─ Sustained sympathetic nervous system activation\n   └─ Physiological "readiness" state maintained even at rest\n      └─ Muscle tension, mental hypervigilance\nHistamine-MBA (elevated)\n└─ Histaminergic arousal circuit (tuberomammillary nucleus) sustained\n   └─ Wakefulness signal maintained past appropriate evening wind-down\nMelatonin (low)\n└─ Absence of circadian wind-down signal\n   └─ No physiological cue to shift from sympathetic to parasympathetic dominance'
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:SYMPTOMS:BATCH7`
- File now contains all 11 entry keys: `'stuffy-runny-nose'`, `'asthma-like'`, `'post-nasal-drip'`, `'difficulty-concentrating'`, `'word-finding-problems'`, `'sensitivity-light-sound'`, `'tingling-numbness'`, `'cant-handle-stress'`, `'burnout'`, `'panic-attacks'`, `'feel-cant-relax'`
- All 7 symptom batch placeholders (`BATCH1`–`BATCH7`) are now gone from the file
- The 4 variable batch placeholders (`VARIABLES:BATCH1`–`BATCH4`) still exist
- The `CLUSTERS` placeholder still exists

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-22"`
- `pendingSteps`: remove `"step-22"`
- `flags.symptomsBatch7`: set to `true`
- `artifacts.symptomCount`: increment by `11`
- `dataChunks.symptoms.batch7`: set to `["stuffy-runny-nose","asthma-like","post-nasal-drip","difficulty-concentrating","word-finding-problems","sensitivity-light-sound","tingling-numbness","cant-handle-stress","burnout","panic-attacks","feel-cant-relax"]`
