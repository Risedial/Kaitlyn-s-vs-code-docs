# Prompt 21: Write JS — Symptom Data: Hormonal (Male & Shared) + Cardiovascular + Pain & Inflammation (12 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:SYMPTOMS:BATCH6` in `fdn-pwa/index.html` with the 12 entries below covering Hormonal (Male & Shared), Cardiovascular & Circulatory, and Pain & Inflammation categories.

Write ALL 12 entries replacing `// PLACEHOLDER:SYMPTOMS:BATCH6`:

```javascript
    'low-testosterone-symptoms': {
      label: 'Low testosterone symptoms (low drive, muscle loss, fatigue)',
      category: 'Hormonal (Male & Shared)',
      variables: ['testosterone', 'dhea', 'hpa-axis', 'pregnenolone-steal', 'indican'],
      clusters: ['A', 'B'],
      interpretation: 'The constellation of low libido, muscle wasting, fatigue, and mood deflation in males maps directly to Cluster B HPA dysfunction via Pregnenolone Steal. When cortisol demand chronically exceeds steroidogenic capacity, pregnenolone is diverted away from DHEA → testosterone synthesis. The result is measurably low testosterone alongside measurably elevated or dysregulated cortisol. Indican elevation adds the amino acid depletion mechanism: protein-stealing bacteria reduce the amino acid substrate for testosterone synthesis and muscle protein.',
      mechanismTree: 'HPA Dysregulation → Pregnenolone Steal\n└─ Pregnenolone pool diverted to cortisol synthesis\n   └─ DHEA synthesis reduced → testosterone synthesis reduced\n      └─ Low testosterone: low drive, muscle loss, fatigue\nIndican (protein catabolism by bacteria)\n└─ Amino acid substrate for muscle protein and hormone synthesis stolen\n   └─ Sarcopenia amplification: muscle breakdown without repair capacity\nCombined effect\n└─ Testosterone-low + catabolic dominance + amino acid deficit\n   └─ Compound muscle wasting and motivational failure'
    },
    'cant-build-muscle': {
      label: "Can't build or maintain muscle",
      category: 'Hormonal (Male & Shared)',
      variables: ['testosterone', 'dhea', 'cortisol-diurnal', 'hpa-axis'],
      clusters: ['B'],
      interpretation: 'Muscle anabolism requires the hormonal balance to favor synthesis over breakdown. Cortisol is catabolic — it promotes protein breakdown and inhibits protein synthesis. Testosterone and DHEA are anabolic — they promote protein synthesis and muscle fiber repair. When HPA dysregulation sustains elevated cortisol and Pregnenolone Steal depletes testosterone and DHEA, the hormonal balance permanently tilts toward catabolism. Exercise stimulates protein synthesis only if the anabolic hormonal environment is present; without it, exercise-induced muscle protein breakdown is not matched by synthesis.',
      mechanismTree: 'Cortisol (elevated — catabolic dominance)\n└─ Ubiquitin-proteasome pathway activation → muscle protein breakdown\n   └─ Catabolic rate exceeds anabolic capacity\nTestosterone + DHEA (low — Pregnenolone Steal consequence)\n└─ Loss of anabolic signaling at androgen receptors in muscle\n   └─ mTOR pathway underactivation → reduced protein synthesis\nNet hormonal balance\n└─ Cortisol:Testosterone ratio elevated beyond anabolic threshold\n   └─ Training produces no lasting muscle gain'
    },
    'weight-gain-despite-diet': {
      label: 'Weight gain despite diet/exercise',
      category: 'Hormonal (Male & Shared)',
      variables: ['cortisol-diurnal', 'estradiol', 'indican', 'urinary-bile-acids'],
      clusters: ['A', 'B', 'C'],
      interpretation: 'Weight gain that is resistant to dietary restriction reflects multiple metabolic disruptions acting simultaneously. Cortisol promotes visceral adipogenesis via glucocorticoid receptor activation in abdominal adipose tissue. Estrogen recycling (elevated Estradiol from elevated Beta-glucuronidase) promotes peripheral fat deposition, particularly at hips and thighs. Indican reflects GI dysbiosis that impairs proper metabolic signaling and nutrient partitioning. Poor bile flow (low Urinary Bile Acids) impairs fat-soluble vitamin absorption and metabolic signaling.',
      mechanismTree: 'Cortisol Diurnal (elevated — Cluster B)\n└─ Visceral adipogenesis via glucocorticoid receptor in abdominal fat\n   └─ Apple-shaped fat distribution — cortisol-driven pattern\nEstradiol (elevated via recycling — Cluster C)\n└─ Peripheral adipogenesis at hips, thighs, breasts\n   └─ Pear-shaped or combined fat distribution\nIndican (GI dysbiosis)\n└─ Metabolic endotoxemia → insulin resistance signaling\n   └─ Caloric restriction fails to overcome insulin resistance\nUrinary Bile Acids (low)\n└─ Bile acid signaling (FXR, TGR5) impairment\n   └─ Reduced metabolic rate, impaired fat-soluble signaling'
    },
    'heart-palpitations': {
      label: 'Heart palpitations / racing heart',
      category: 'Cardiovascular & Circulatory',
      variables: ['histamine-mba', 'dao', 'cortisol-diurnal', 'hpa-axis'],
      clusters: ['B', 'D'],
      interpretation: 'Cardiac palpitations and racing heart in the absence of structural cardiac pathology are commonly histamine-mediated and/or HPA-mediated. Histamine activates H2 receptors in cardiac myocytes, producing positive chronotropic (rate-increasing) and inotropic effects — the clinical experience of a racing, forceful heartbeat. Low DAO amplifies this by allowing dietary histamine to reach cardiac receptors. HPA dysregulation adds a second catecholamine-driven mechanism: elevated cortisol sustains sympathetic tone, and adrenaline co-release produces palpitations. Both mechanisms must be assessed.',
      mechanismTree: 'Histamine-MBA (elevated) + Low DAO\n└─ H2 receptor activation in cardiac myocytes\n   └─ Positive chronotropy → heart rate increase\n   └─ Positive inotropy → forceful heartbeat sensation\nHPA Dysregulation (cortisol)\n└─ Sustained sympathetic tone\n   └─ Epinephrine co-release → adrenergic palpitations\nCombined Cluster B + D\n└─ Histaminergic + adrenergic palpitation mechanisms simultaneously active\n   └─ Worse after histamine-rich meals AND stress exposure'
    },
    'low-blood-pressure-dizziness': {
      label: 'Low blood pressure / dizziness on standing',
      category: 'Cardiovascular & Circulatory',
      variables: ['hpa-axis', 'dhea', 'cortisol-diurnal'],
      clusters: ['B'],
      interpretation: 'Orthostatic hypotension — dizziness or lightheadedness when standing — is the hemodynamic signature of HPA Phase 3–4 (Exhaustion-Collapse). Cortisol is required for vascular tone maintenance via upregulation of catecholamine sensitivity in vascular smooth muscle. In HPA exhaustion, the near-flat cortisol pattern removes this vascular tone support, resulting in inadequate vasoconstriction response to standing. DHEA depletion removes the vascular endothelial protective effects of this neurosteroid. The practitioner should look for near-flat cortisol diurnal pattern with sub-low values across multiple time points.',
      mechanismTree: 'HPA Collapse Phase (flat cortisol pattern)\n└─ Cortisol requirement for vascular tone maintenance absent\n   └─ Catecholamine receptor downregulation → vasodilation\n      └─ Orthostatic hypotension on standing\nDHEA (low)\n└─ Loss of vascular endothelial protection\n   └─ Reduced vascular tone reserve\nClinical pattern\n└─ Flat cortisol 4-point salivary curve (all points at or below low-normal)\n   └─ Confirms HPA Collapse phase as primary driver'
    },
    'high-blood-pressure': {
      label: 'High blood pressure',
      category: 'Cardiovascular & Circulatory',
      variables: ['cortisol-diurnal', 'histamine-mba', 'oxidative-stress'],
      clusters: ['B', 'D'],
      interpretation: 'Functional hypertension without primary structural cardiovascular disease involves three FDN mechanisms. Cortisol drives blood pressure elevation via multiple pathways: sodium retention (mineralocorticoid effect), sympathetic activation, and vascular wall remodeling. Histamine has a paradoxical vasoconstriction effect at high doses via H1 receptor-mediated baroreceptor reflex amplification — though vasodilation predominates at low doses. Systemic oxidative stress promotes endothelial dysfunction and vascular stiffness, reducing arterial compliance and raising systolic pressure.',
      mechanismTree: 'Cortisol Diurnal (elevated — Cluster B)\n└─ Sodium retention (mineralocorticoid-like effect) → volume expansion\n   └─ Sympathetic activation → peripheral vasoconstriction\n      └─ Elevated blood pressure\nSystemic Oxidative Stress\n└─ Endothelial NO synthase uncoupling → reduced nitric oxide\n   └─ Vascular stiffness → elevated systolic pressure\nHistamine-MBA (elevated — context-dependent)\n└─ H1 baroreceptor sensitization → vasoconstrictor reflex amplification\n   └─ Compounding effect on elevated cortisol-driven BP'
    },
    'joint-pain': {
      label: 'Joint pain',
      category: 'Pain & Inflammation',
      variables: ['zonulin', 'ohdg', 'oxidative-stress', 'dao'],
      clusters: ['A', 'D'],
      interpretation: 'Non-traumatic joint pain in the FDN model is primarily explained by immune complex deposition driven by Zonulin-mediated antigen translocation. When LPS and food antigens cross the gut epithelium, they enter systemic circulation where IgG immune complexes form. These complexes preferentially deposit in synovial tissue — a well-vascularized joint lining — triggering complement activation and local neutrophilic inflammation. Systemic oxidative stress (8-OHdG elevated) amplifies this by promoting prostaglandin synthesis and inflammatory cytokine production. Low DAO allows histamine to reach joint mast cells, amplifying synovial inflammation.',
      mechanismTree: 'Zonulin (antigen translocation)\n└─ LPS + food antigens → systemic immune complex formation\n   └─ Immune complex deposition in synovial tissue\n      └─ Complement activation → neutrophilic synovitis\n8-OHdG + Oxidative Stress\n└─ COX pathway activation → prostaglandin synthesis\n   └─ Inflammatory cytokine amplification\n      └─ Joint pain and swelling amplified\nLow DAO\n└─ Histamine accumulation at synovial mast cells\n   └─ Mast cell degranulation → synovial inflammation'
    },
    'muscle-aches': {
      label: 'Muscle aches without exertion',
      category: 'Pain & Inflammation',
      variables: ['oxidative-stress', 'ohdg', 'hpa-axis', 'cortisol-diurnal'],
      clusters: ['A', 'B'],
      interpretation: 'Diffuse myalgia without exertion reflects global metabolic impairment of muscle tissue rather than localized pathology. Systemic oxidative stress (8-OHdG elevated) damages mitochondrial DNA in muscle cells, reducing ATP synthesis and producing the biochemical substrate of muscle pain. Elevated cortisol is directly myotoxic at high sustained levels via glucocorticoid-induced muscle protein catabolism. The combination of oxidative mitochondrial damage and catabolic dominance produces a persistent, widespread achiness that is not relieved by rest — distinguishing it from exercise-induced soreness.',
      mechanismTree: 'Systemic Oxidative Stress + 8-OHdG\n└─ Skeletal muscle mitochondrial DNA damage\n   └─ ATP synthesis impaired → lactic acid accumulation at rest\n      └─ Diffuse myalgia without exertion\nCortisol (elevated — catabolic)\n└─ Glucocorticoid-mediated muscle protein breakdown\n   └─ Sarcomere structural damage → aching\nCombined effect\n└─ Mitochondrial impairment + protein catabolism\n   └─ Muscle cannot maintain structural integrity without energy substrate'
    },
    'headaches': {
      label: 'Headaches',
      category: 'Pain & Inflammation',
      variables: ['histamine-mba', 'dao', 'zonulin', 'indican', 'cortisol-diurnal'],
      clusters: ['A', 'B', 'D'],
      interpretation: 'Headaches in the FDN model require mechanism stratification. Histamine-driven headaches are vascular: H1 receptor-mediated vasodilation of cranial blood vessels produces the throbbing quality. Low DAO amplifies dietary histamine contributions. Zonulin-mediated LPS translocation drives neuroinflammation affecting meningeal and cortical sensory processing — producing diffuse, pressure-type headaches. Indican-driven neurotransmitter depletion removes serotonin\'s vasoconstrictive headache-protective role. Cortisol dysregulation produces tension-type headaches via sustained nuchal and temporalis muscle tension.',
      mechanismTree: 'Histamine-MBA + Low DAO (Cluster D)\n└─ Cranial vascular H1 vasodilation → throbbing vascular headache\n   └─ Worse after histamine-containing meals\nZonulin (LPS translocation)\n└─ Neuroinflammation via microglial TLR4 activation\n   └─ Meningeal sensitization → pressure-type headache\nIndican (serotonin precursor depletion)\n└─ Loss of serotonin vasoconstrictive protection\n   └─ Increased vulnerability to vascular headache triggers\nCortisol dysregulation\n└─ Sustained nuchal and scalp muscle tension\n   └─ Tension-type headache pattern'
    },
    'migraines': {
      label: 'Migraines',
      category: 'Pain & Inflammation',
      variables: ['histamine-mba', 'dao', 'estradiol', 'hpa-axis', 'zonulin'],
      clusters: ['B', 'C', 'D'],
      interpretation: 'Migraines represent the maximum convergence of vascular, hormonal, neuroinflammatory, and histaminergic mechanisms. Histamine is the primary vascular trigger: H1-mediated cranial vasodilation combined with neurogenic inflammation. Estradiol cycling (Cluster C — estrogen recycling) is the primary hormonal trigger for menstrual migraines; fluctuating estradiol affects serotonin receptor sensitivity and mast cell degranulation threshold. Zonulin-driven neuroinflammation sensitizes the trigeminal-vascular complex — the anatomical substrate of migraine. HPA dysregulation sustains the cortisol-driven sympathetic hyperarousal that lowers the migraine threshold.',
      mechanismTree: 'Histamine-MBA + Low DAO (primary vascular mechanism)\n└─ Cranial vascular H1 activation → vasodilation\n   └─ Trigeminal-vascular activation → migraine cascade\nEstradiol cycling (Cluster C — menstrual trigger)\n└─ Estrogen withdrawal → mast cell degranulation → histamine spike\n   └─ Menstrual migraine pattern correlates with estrogen drop\nZonulin (neuroinflammatory sensitization)\n└─ LPS → microglial activation → trigeminal sensitization\n   └─ Lower migraine threshold for all other triggers\nHPA Dysregulation\n└─ Cortisol-driven sympathetic hyperarousal → migraine prodrome amplification'
    },
    'fibromyalgia-like': {
      label: 'Fibromyalgia-like symptoms',
      category: 'Pain & Inflammation',
      variables: ['ohdg', 'oxidative-stress', 'hpa-axis', 'indican'],
      clusters: ['A', 'B'],
      interpretation: 'The fibromyalgia presentation — widespread musculoskeletal pain, tender points, fatigue, and cognitive fog — maps onto a convergence of three FDN mechanisms that collectively explain the syndrome without requiring a primary neurological diagnosis. Systemic oxidative stress (8-OHdG) damages muscle mitochondria and produces central sensitization preconditions. HPA exhaustion provides the widespread pain amplification (cortisol normally has analgesic properties; its depletion removes this natural pain buffering). Indican-driven amino acid depletion removes serotonin precursors — serotonin is a key endogenous analgesic and sleep-deepening neurotransmitter.',
      mechanismTree: 'Systemic Oxidative Stress + 8-OHdG\n└─ Muscle mitochondrial dysfunction → diffuse myalgia\n   └─ Central sensitization preconditions established\nHPA Exhaustion (low cortisol — analgesic loss)\n└─ Cortisol normally has analgesic/anti-inflammatory properties\n   └─ Flat/low cortisol removes this pain-buffering effect\n      └─ Pain amplification at previously sub-threshold stimuli\nIndican (serotonin precursor depletion)\n└─ Serotonin deficit → descending pain inhibition impaired\n   └─ Widespread pain threshold lowered'
    },
    'chronic-pain': {
      label: 'Chronic pain',
      category: 'Pain & Inflammation',
      variables: ['oxidative-stress', 'ohdg', 'zonulin', 'hpa-axis'],
      clusters: ['A', 'B'],
      interpretation: 'Persistent pain lasting beyond normal tissue healing timelines indicates central sensitization — a state where the nervous system maintains elevated pain signaling independent of peripheral tissue damage. Systemic oxidative stress damages nociceptor myelin sheaths, producing ectopic pain signaling. Zonulin-driven LPS translocation maintains the neuroinflammatory state that sustains central sensitization. HPA exhaustion removes cortisol\'s endogenous analgesic and anti-inflammatory effects, allowing neuroinflammation to persist unchecked. Restoration of gut barrier integrity (addressing Zonulin) is the highest-leverage upstream intervention for central sensitization.',
      mechanismTree: 'Systemic Oxidative Stress (8-OHdG)\n└─ Nociceptor myelin oxidative damage\n   └─ Ectopic pain signaling without peripheral tissue injury\nZonulin (LPS-driven neuroinflammation)\n└─ Sustained microglial activation → central sensitization maintenance\n   └─ Pain amplification and threshold lowering persist\nHPA Exhaustion (low cortisol)\n└─ Loss of cortisol analgesic effect\n   └─ Neuroinflammation unchecked by HPA anti-inflammatory signaling\n      └─ Chronic pain cycle sustained'
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:SYMPTOMS:BATCH6`
- File now contains all 12 entry keys: `'low-testosterone-symptoms'`, `'cant-build-muscle'`, `'weight-gain-despite-diet'`, `'heart-palpitations'`, `'low-blood-pressure-dizziness'`, `'high-blood-pressure'`, `'joint-pain'`, `'muscle-aches'`, `'headaches'`, `'migraines'`, `'fibromyalgia-like'`, `'chronic-pain'`
- The symptom batch placeholder `BATCH7` still exists in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-21"`
- `pendingSteps`: remove `"step-21"`
- `flags.symptomsBatch6`: set to `true`
- `artifacts.symptomCount`: increment by `12`
- `dataChunks.symptoms.batch6`: set to `["low-testosterone-symptoms","cant-build-muscle","weight-gain-despite-diet","heart-palpitations","low-blood-pressure-dizziness","high-blood-pressure","joint-pain","muscle-aches","headaches","migraines","fibromyalgia-like","chronic-pain"]`
