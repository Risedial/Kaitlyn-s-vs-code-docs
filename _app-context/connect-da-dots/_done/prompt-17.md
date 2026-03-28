# Prompt 17: Write JS — Symptom Data: Mood & Emotions Category (9 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:SYMPTOMS:BATCH2` in `fdn-pwa/index.html` with the 9 Mood & Emotions symptom entries below.

Each entry must follow the same JavaScript object structure as batch 1. Valid variable IDs are listed in prompt-16.

Write ALL 9 entries replacing `// PLACEHOLDER:SYMPTOMS:BATCH2`:

```javascript
    'anxiety': {
      label: 'Anxiety',
      category: 'Mood & Emotions',
      variables: ['histamine-mba', 'dao', 'hpa-axis', 'indican', 'zonulin', 'cortisol-diurnal'],
      clusters: ['A', 'B', 'D'],
      interpretation: 'Anxiety has multiple independent FDN drivers that must be differentiated. Histamine-mediated anxiety is vasoactive and acute: Histamine-MBA elevated with low DAO indicates impaired degradation, causing CNS arousal via hypothalamic H1 activation. Indican-driven anxiety is neurochemical: bacterial tryptophan theft depletes serotonin precursors while generating kynurenine-pathway neuroinflammatory metabolites. Zonulin-mediated anxiety is systemic: tight junction disassembly allows LPS translocation, driving low-grade neuroinflammation that presents as generalized anxiety. The practitioner must identify which mechanism is primary before selecting interventions.',
      mechanismTree: 'Histamine load (Histamine-MBA + low DAO)\n└─ H1 receptor activation: CNS arousal, vasodilation\n   └─ Acute anxiety, racing heart, flushing\nIndican (tryptophan theft)\n└─ Serotonin precursor depletion\n   └─ Kynurenine pathway activation → quinolinic acid (excitotoxin)\n      └─ NMDA receptor hyperactivation → anxiety/agitation\nZonulin (leaky gut)\n└─ LPS translocation → TLR4 activation in microglia\n   └─ Neuroinflammation → generalized anxiety, fear amplification'
    },
    'depression': {
      label: 'Depression',
      category: 'Mood & Emotions',
      variables: ['indican', 'hpa-axis', 'dhea', 'testosterone', 'ohdg', 'oxidative-stress'],
      clusters: ['A', 'B'],
      interpretation: 'Functional depression in the FDN model is primarily a biochemical deficit state rather than a psychosocial condition, though both can co-occur. Indican elevation points to tryptophan theft as the primary serotonin depletion mechanism. HPA exhaustion depletes the anabolic hormones (DHEA, testosterone) that maintain motivational energy and neuroplasticity. Systemic oxidative stress (8-OHdG) damages neuronal mitochondria, reducing the energy availability for synaptic signaling. These three pathways can independently produce depression-like presentations and must all be assessed.',
      mechanismTree: 'Indican (dysbiosis)\n└─ Bacterial tryptophan catabolism → serotonin precursor deficit\n   └─ Serotonin + dopamine precursor cross-depletion\n      └─ Anhedonia, loss of reward signaling\nHPA Exhaustion (DHEA + Testosterone low)\n└─ Catabolic dominance → neuroplasticity impairment\n   └─ Reduced BDNF expression → hippocampal atrophy pattern\n8-OHdG + Oxidative Stress\n└─ Neuronal mitochondrial damage\n   └─ ATP deficit in prefrontal cortex → executive function loss, flat affect'
    },
    'irritability-short-fuse': {
      label: 'Irritability / short fuse',
      category: 'Mood & Emotions',
      variables: ['histamine-mba', 'cortisol-diurnal', 'hpa-axis'],
      clusters: ['B', 'D'],
      interpretation: 'Irritability and low frustration tolerance are most commonly driven by three intersecting mechanisms in the FDN model. Histamine is directly neuroexcitatory — elevated systemic histamine lowers the threshold for emotional reactivity via hypothalamic and limbic histamine receptors. Cortisol dysregulation (particularly an erratic or inverted diurnal pattern) produces blood glucose instability that directly causes neuroglycopenic irritability. HPA hyperactivation maintains a chronic sympathetic baseline that compresses the stress buffer — minor stressors produce outsized reactions.',
      mechanismTree: 'Histamine-MBA (elevated)\n└─ Limbic H1 activation → emotional excitability threshold lowered\n   └─ Rapid-onset irritability, noise/light sensitivity\nCortisol Diurnal (erratic pattern)\n└─ Blood glucose dysregulation\n   └─ Neuroglycopenic episodes → "hanger" irritability\nHPA Hyperactivation\n└─ Sustained sympathetic tone → compressed stress buffer\n   └─ Exaggerated threat response to minor stressors'
    },
    'emotional-numbness': {
      label: 'Emotional numbness',
      category: 'Mood & Emotions',
      variables: ['hpa-axis', 'dhea', 'cortisol-diurnal'],
      clusters: ['B'],
      interpretation: 'Emotional numbness or blunting is the hallmark presentation of HPA Phase 3–4 (Exhaustion and Collapse). When the HPA axis has been chronically overactivated and the system enters collapse, the characteristic flat cortisol pattern removes the hormonal substrate for emotional responsivity. DHEA depletion eliminates the neuro-protective and mood-modulating effects of this neurosteroid. The practitioner should look for a nearly flat cortisol diurnal pattern — all four data points clustered at or below low-normal range.',
      mechanismTree: 'HPA Collapse Phase (Phase 3–4)\n└─ Cortisol pattern flatlined — no diurnal variation\n   └─ Absence of cortisol-driven emotional responsivity substrate\nDHEA depletion\n└─ Loss of neurosteroid DHEA-S (neuroprotective, mood-modulating)\n   └─ Emotional blunting, dissociation from affect\nCombined effect\n└─ Hormonal emotional substrate depleted across all axes\n   └─ Flatted affect, inability to feel positive or negative emotions'
    },
    'overwhelm-cant-cope': {
      label: "Overwhelm / can't cope with stress",
      category: 'Mood & Emotions',
      variables: ['hpa-axis', 'sigas-shp', 'pregnenolone-steal'],
      clusters: ['B'],
      interpretation: 'The inability to handle stress that was previously manageable is the clinical definition of HPA Phase 2–3 transition. The cortisol:DHEA ratio (assessed from the diurnal panel and DHEA value) reveals whether the system is still mounting a cortisol response but at the cost of depleting anabolic reserves via Pregnenolone Steal. Low sIgA-SHP confirms that HPA suppression of mucosal immunity has already occurred — the immune system is a downstream victim of the same cortisol dysregulation that is overwhelming the psychological stress-coping system.',
      mechanismTree: 'HPA Dysregulation (Cortisol:DHEA ratio imbalanced)\n└─ Cortisol reserve insufficient to buffer new stressors\n   └─ Disproportionate stress response to minor demands\nPregnenolone Steal (active)\n└─ Anabolic hormones sacrificed for cortisol synthesis\n   └─ Emotional resilience substrates (DHEA, progesterone) depleted\nsIgA-SHP (low)\n└─ HPA → immune suppression loop\n   └─ Physical illness adds to total allostatic load → overwhelm amplified'
    },
    'mood-swings': {
      label: 'Mood swings',
      category: 'Mood & Emotions',
      variables: ['estradiol', 'progesterone', 'cortisol-diurnal', 'histamine-mba'],
      clusters: ['B', 'C', 'D'],
      interpretation: 'Mood swings spanning the full emotional range — from euphoria to irritability to tearfulness — indicate hormonal instability across multiple axes simultaneously. Estradiol:Progesterone imbalance (Cluster C — estrogen recycling via Beta-glucuronidase) produces the hormonal volatility. Blood glucose dysregulation from HPA-driven cortisol diurnal dysfunction adds a metabolic volatility layer. Histamine load amplifies emotional reactivity by lowering the limbic response threshold. The practitioner must assess all three panels (SHP, MBA, GI-MAP) to identify the primary amplification mechanism.',
      mechanismTree: 'Estradiol:Progesterone imbalance (Cluster C)\n└─ Beta-glucuronidase → re-circulating estrogen metabolites\n   └─ Estrogen dominance with progesterone insufficiency → emotional volatility\nCortisol Diurnal (erratic)\n└─ Blood glucose instability → metabolic mood fluctuation\n   └─ High and low glucose states create emotional polarity\nHistamine-MBA (elevated)\n└─ Vasoactive + neuroexcitatory histamine peaks\n   └─ Emotional reactivity spikes at histamine load peaks'
    },
    'brain-fog': {
      label: 'Brain fog',
      category: 'Mood & Emotions',
      variables: ['zonulin', 'indican', 'ohdg', 'hepatic-detox', 'histamine-mba', 'dao'],
      clusters: ['A', 'B', 'D'],
      interpretation: 'Brain fog is the most multi-mechanistic symptom in the FDN model and reliably indicates cross-panel dysfunction. Zonulin-mediated LPS translocation triggers microglial activation and neuroinflammation — the most direct mechanism. Indican-driven amino acid depletion removes precursors for acetylcholine and dopamine, impairing cognitive processing speed. Hepatic Detox Impairment allows recirculation of neurotoxic Phase I intermediates. Histamine directly impairs hippocampal and prefrontal cognitive networks. When all four drivers are active, the practitioner should prioritize GI barrier restoration as the upstream intervention.',
      mechanismTree: 'Zonulin (leaky gut)\n└─ LPS translocation → microglial TLR4 activation\n   └─ Neuroinflammation → cognitive processing impairment\nIndican (amino acid theft)\n└─ Acetylcholine precursor (choline, serine) depletion\n   └─ Cholinergic transmission deficit → memory and attention impairment\nHepatic Detox Impairment\n└─ Phase I intermediate accumulation → neurotoxin recirculation\n   └─ Toxic encephalopathy pattern\nHistamine-MBA (elevated)\n└─ Hippocampal H1 activation → impaired spatial and working memory'
    },
    'poor-memory': {
      label: 'Poor memory',
      category: 'Mood & Emotions',
      variables: ['indican', 'ohdg', 'oxidative-stress', 'hpa-axis'],
      clusters: ['A', 'B'],
      interpretation: 'Memory impairment in the functional medicine model traces primarily to two mechanisms: neurotransmitter precursor depletion (Indican-driven tryptophan theft) and oxidative neuronal damage (8-OHdG). Tryptophan is a precursor not only for serotonin but also for kynurenine-pathway metabolites that regulate NMDA receptor function — its depletion impairs hippocampal long-term potentiation. Systemic oxidative stress damages neuronal mitochondria and promotes hippocampal cellular atrophy. Chronic HPA dysregulation adds a third mechanism: cortisol-driven hippocampal neurotoxicity at high sustained cortisol levels.',
      mechanismTree: 'Indican (tryptophan theft)\n└─ Kynurenine pathway imbalance → NMDA receptor dysfunction\n   └─ Impaired hippocampal long-term potentiation → encoding deficit\n8-OHdG + Oxidative Stress\n└─ Neuronal mitochondrial oxidative damage\n   └─ Reduced ATP for synaptic signaling → retrieval impairment\nHPA Dysregulation (chronic elevated cortisol)\n└─ Glucocorticoid receptor downregulation in hippocampus\n   └─ Hippocampal volume reduction → spatial and episodic memory loss'
    },
    'feeling-disconnected': {
      label: 'Feeling disconnected from yourself',
      category: 'Mood & Emotions',
      variables: ['hpa-axis', 'sigas-shp', 'cortisol-diurnal'],
      clusters: ['B'],
      interpretation: 'Depersonalization and derealization — feeling like an observer of your own life, emotional disconnection from self and environment — are Phase 4 (Collapse) HPA presentations. When cortisol has been chronically elevated and then collapses, the resulting flat cortisol pattern removes the hormonal substrate for normal interoception and emotional embodiment. The practitioner should look for the "flat line" cortisol pattern combined with very low sIgA-SHP as the dual confirmation of HPA collapse phase. This presentation requires prioritizing HPA restoration before any other intervention.',
      mechanismTree: 'HPA Collapse Phase (Phase 4)\n└─ Cortisol pattern completely flattened\n   └─ Loss of hormonal interoceptive signaling → emotional disembodiment\nsIgA-SHP (severely low)\n└─ HPA-immune collapse confirmation\n   └─ Systemic energy diversion away from conscious processing\nCortisol flat pattern\n└─ Amygdala hypoactivation (insufficient cortisol substrate)\n   └─ Emotional processing failure → detachment, unreality'
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:SYMPTOMS:BATCH2`
- File now contains all 9 entry keys: `'anxiety'`, `'depression'`, `'irritability-short-fuse'`, `'emotional-numbness'`, `'overwhelm-cant-cope'`, `'mood-swings'`, `'brain-fog'`, `'poor-memory'`, `'feeling-disconnected'`
- Each entry has all 6 required fields with no placeholder text
- The other symptom batch placeholders (`BATCH3` through `BATCH7`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-17"`
- `pendingSteps`: remove `"step-17"`
- `flags.symptomsBatch2`: set to `true`
- `artifacts.symptomCount`: increment by `9`
- `dataChunks.symptoms.batch2`: set to `["anxiety","depression","irritability-short-fuse","emotional-numbness","overwhelm-cant-cope","mood-swings","brain-fog","poor-memory","feeling-disconnected"]`
