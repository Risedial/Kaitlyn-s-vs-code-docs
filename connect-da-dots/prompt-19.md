# Prompt 19: Write JS — Symptom Data: Food Reactions + Skin Categories (11 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:SYMPTOMS:BATCH4` in `fdn-pwa/index.html` with the 11 Food Reactions + Skin symptom entries below.

Write ALL 11 entries replacing `// PLACEHOLDER:SYMPTOMS:BATCH4`:

```javascript
    'reactions-many-foods': {
      label: 'Reactions to many foods',
      category: 'Food Reactions',
      variables: ['zonulin', 'dao', 'histamine-mba', 'anti-gliadin-iga', 'sigas-gi'],
      clusters: ['A', 'D'],
      interpretation: 'Reactivity to an expanding range of foods — progressively fewer safe foods — is the clinical signature of Zonulin-mediated intestinal hyperpermeability combined with DAO insufficiency. When Zonulin is elevated, previously non-reactive dietary antigens cross the gut epithelium and prime immune sensitization. Low DAO means biogenic amines from an expanding category of foods produce reactions. Low sIgA-GI confirms immune collapse at the mucosal surface, allowing broader antigen translocation. The priority intervention is gut barrier restoration, not food elimination.',
      mechanismTree: 'Zonulin (leaky gut — primary driver)\n└─ Tight junction disassembly → antigen translocation\n   └─ Progressive immune sensitization to new antigens\n      └─ Expanding food reactivity list\nLow DAO\n└─ Failure to degrade dietary histamine and biogenic amines\n   └─ Reactions to any histamine-containing food\nsIgA-GI (low — immune collapse)\n└─ Loss of secretory IgA barrier\n   └─ Uncontrolled antigen absorption → broadening reactivity'
    },
    'gluten-sensitivity': {
      label: 'Gluten sensitivity',
      category: 'Food Reactions',
      variables: ['anti-gliadin-iga', 'zonulin', 'sigas-gi', 'histamine-mba'],
      clusters: ['A', 'D'],
      interpretation: 'Elevated Anti-gliadin IgA confirms local mucosal immune reactivity to gliadin protein, which is distinct from systemic anti-tTG/anti-EMA (celiac) testing. An important interpretation nuance: if Anti-gliadin IgA is low alongside low sIgA-GI, this is likely a false negative — immune collapse prevents mounting even the local IgA response. Zonulin is mechanistically upstream: gliadin itself is a known Zonulin-release trigger, and Zonulin-mediated tight junction disruption is the mechanism that allows gliadin to reach subepithelial immune cells. Histamine-MBA may be elevated due to cross-reactive immune activation at the mucosal barrier.',
      mechanismTree: 'Anti-gliadin IgA (elevated)\n└─ Mucosal immune recognition of gliadin protein\n   └─ Local IgA-mediated inflammatory cascade\nZonulin (gliadin is a Zonulin trigger)\n└─ Gliadin binding to CXCR3 receptor → Zonulin release\n   └─ Tight junction disassembly → gliadin reaches subepithelial immune cells\n      └─ Amplified immune reaction\nsIgA-GI (low — interpret Anti-gliadin IgA with caution)\n└─ False negative risk: immune collapse prevents mounting anti-gliadin response'
    },
    'dairy-reactions': {
      label: 'Dairy reactions',
      category: 'Food Reactions',
      variables: ['anti-gliadin-iga', 'zonulin', 'dao'],
      clusters: ['A', 'D'],
      interpretation: 'Dairy reactivity in the FDN context most commonly involves cross-reactive molecular mimicry rather than true lactose intolerance. Some dairy proteins (particularly casein alpha-s1) share structural homology with gliadin, meaning Anti-gliadin IgA-positive clients may cross-react to dairy via antibody cross-reactivity. Zonulin elevation allows dairy protein antigens to reach subepithelial immune tissue. Low DAO cannot degrade the biogenic amines in dairy (including histamine in aged cheeses and casein-derived casomorphin).',
      mechanismTree: 'Anti-gliadin IgA (cross-reactivity mechanism)\n└─ Casein structural homology with gliadin\n   └─ Anti-gliadin IgA cross-reacts with dairy → immediate mucosal reaction\nZonulin (barrier failure)\n└─ Dairy proteins cross epithelium without degradation\n   └─ Subepithelial immune sensitization to milk antigens\nLow DAO\n└─ Cannot degrade dairy-derived biogenic amines\n   └─ Histamine-like reaction to cheese, fermented dairy'
    },
    'histamine-food-reactions': {
      label: 'Reactions to histamine-rich foods (wine, aged cheese, fermented foods)',
      category: 'Food Reactions',
      variables: ['histamine-mba', 'dao', 'histamine-dao-system'],
      clusters: ['D'],
      interpretation: 'Reproducible reactions specifically to histamine-rich foods — wine, aged cheese, vinegar, fermented vegetables, cured meats — are the clinical signature of Histamine Intolerance driven by DAO enzyme insufficiency. When DAO cannot degrade dietary histamine in the gut lumen, it absorbs intact and enters systemic circulation producing dose-dependent reactions: flushing, headache, rhinorrhea, palpitations, and gastrointestinal cramping. The Histamine-DAO Regulatory System construct captures the functional ratio between histamine load and degradation capacity.',
      mechanismTree: 'DAO (insufficient enzyme capacity)\n└─ Dietary histamine from wine/aged cheese/fermented food absorbed intact\n   └─ Systemic histamine load → H1, H2, H3 receptor activation\nHistamine-MBA (elevated system load)\n└─ Endogenous histamine production already near threshold\n   └─ Dietary load pushes system over tolerance threshold\nHistamine-DAO Regulatory System (disrupted ratio)\n└─ Load exceeds degradation capacity\n   └─ Dose-dependent reactions scaling with histamine content of meal'
    },
    'worse-after-fermented': {
      label: 'Getting worse after eating fermented foods or probiotics',
      category: 'Food Reactions',
      variables: ['histamine-mba', 'dao', 'indican'],
      clusters: ['D'],
      interpretation: 'Worsening after fermented foods or probiotic supplementation is pathognomonic for histamine intolerance with concurrent SIBO. Fermented foods are among the highest dietary histamine sources. If DAO is insufficient, these foods overwhelm degradation capacity. SIBO (indicated by Indican elevation) adds a second mechanism: SIBO bacteria also produce histamine from dietary histidine, so probiotics introduced into a SIBO environment can transiently worsen bacterial histamine production. This is a clinical sign to address SIBO and DAO deficiency before recommending fermented foods.',
      mechanismTree: 'Low DAO + high histamine food exposure\n└─ Fermented food histamine absorbed intact\n   └─ Dose-dependent histamine reaction: worsening 30–60 min after eating\nIndican (SIBO)\n└─ SIBO bacteria produce histamine from dietary histidine\n   └─ Probiotic introduction into SIBO environment → transient worsening\nClinical implication\n└─ Treat SIBO (address Indican) BEFORE recommending fermented foods\n   └─ DAO support required alongside microbiome restoration'
    },
    'hives-urticaria': {
      label: 'Hives / urticaria',
      category: 'Skin',
      variables: ['histamine-mba', 'dao', 'zonulin', 'histamine-dao-system'],
      clusters: ['D'],
      interpretation: 'Urticaria is the prototypical histamine-driven skin manifestation. Mast cell degranulation releases histamine into dermal tissue, causing the characteristic wheal-and-flare reaction via H1 receptor activation in dermal vasculature. When DAO is insufficient, systemically absorbed dietary histamine can also trigger urticarial reactions. Zonulin-mediated leaky gut allows allergens and LPS to reach dermal immune cells, amplifying the mast cell degranulation threshold reduction. The Histamine-DAO regulatory system assessment reveals whether the primary problem is excess production or insufficient degradation.',
      mechanismTree: 'Histamine-MBA (elevated) + Low DAO\n└─ Dermal mast cell degranulation → H1 receptor activation\n   └─ Wheal-and-flare urticarial reaction\nZonulin (leaky gut)\n└─ Allergen translocation → systemic antigen sensitization\n   └─ Lowered mast cell degranulation threshold\nHistamine-DAO Regulatory System\n└─ Interpret Histamine:DAO ratio to determine production vs. degradation driver\n   └─ High histamine + high DAO = production excess\n   └─ High histamine + low DAO = degradation failure'
    },
    'eczema-rashes': {
      label: 'Eczema / rashes',
      category: 'Skin',
      variables: ['histamine-mba', 'zonulin', 'anti-gliadin-iga', 'sigas-gi'],
      clusters: ['A', 'D'],
      interpretation: 'Eczema and chronic rashes in the FDN model are primarily driven by two converging mechanisms: gut-skin axis dysfunction via Zonulin-mediated antigen translocation, and histamine-driven dermal inflammation. Zonulin elevation allows food antigens and LPS to reach systemic circulation → immune complexes deposit in dermal tissue → chronic inflammatory skin lesion. Anti-gliadin IgA elevation suggests that gluten reactivity is contributing a systemic immune activation that targets dermal tissue as a secondary site. Low sIgA-GI confirms the loss of mucosal immune compartmentalization that normally prevents skin sensitization.',
      mechanismTree: 'Zonulin (gut-skin axis)\n└─ Food antigen + LPS translocation → systemic immune activation\n   └─ Immune complex deposition in dermal tissue → eczema\nHistamine-MBA (elevated)\n└─ Dermal H1 activation → vasodilation, itch, inflammation\n   └─ Eczema flare correlation with dietary histamine load\nAnti-gliadin IgA + Low sIgA-GI\n└─ Gluten-reactive systemic IgA immune activation\n   └─ Dermatitis herpetiformis-like dermal IgA deposition pattern'
    },
    'flushing-redness': {
      label: 'Flushing / redness (especially face)',
      category: 'Skin',
      variables: ['histamine-mba', 'dao', 'estradiol'],
      clusters: ['C', 'D'],
      interpretation: 'Facial flushing is the most characteristic histamine-mediated vascular symptom. Histamine activates H1 receptors in cutaneous vasculature, producing vasodilation and the characteristic erythema. When DAO is insufficient, the threshold for triggering visible flushing drops markedly. Estradiol has an important modulating role: elevated estradiol (Cluster C mechanism) both stimulates mast cell histamine release AND inhibits DAO enzyme activity — creating a hormonal amplification of histamine-driven flushing. This explains why flushing often worsens cyclically in women with estrogen dominance.',
      mechanismTree: 'Histamine-MBA + Low DAO\n└─ H1 receptor activation in facial cutaneous vasculature\n   └─ Vasodilation → visible flushing, warmth, redness\nEstradiol (elevated — Cluster C)\n└─ Estrogen → mast cell histamine release amplification\n   └─ Estrogen → DAO inhibition (reduces degradation capacity)\n      └─ Dual estrogen effect: more histamine + less clearance\nClinical note\n└─ Cyclical flushing (worse pre-menstrually) → assess Cluster C first'
    },
    'itching-no-rash': {
      label: 'Itching (no visible rash)',
      category: 'Skin',
      variables: ['histamine-mba', 'dao', 'urinary-bile-acids'],
      clusters: ['A', 'D'],
      interpretation: 'Pruritus without visible skin lesion (pruritus sine materia) has two FDN-relevant mechanisms beyond histamine. Histamine H1 activation produces itch without rash when the histamine dose is subthreshold for vasodilation but sufficient for itch receptor activation. Elevated Urinary Bile Acids — indicating hepatic congestion and bile acid spillover into systemic circulation — produce the characteristic cholestatic itch: bile salts deposit in skin and activate TGR5 receptors on sensory nerve endings, producing intense pruritus particularly of hands, feet, and trunk.',
      mechanismTree: 'Histamine-MBA (subthreshold vasodilation dose)\n└─ H1 itch receptor activation without sufficient vasodilation for visible wheal\n   └─ Pruritus without urticaria — itch without rash\nUrinary Bile Acids (elevated — hepatic congestion)\n└─ Bile salt systemic recirculation\n   └─ Bile salt deposition in skin → TGR5 receptor activation\n      └─ Cholestatic itch: palms, soles, trunk — no visible lesion\nLow DAO\n└─ Histamine accumulation below urticaria threshold but above itch threshold\n   └─ Dose-dependent itch without visible reaction'
    },
    'acne': {
      label: 'Acne',
      category: 'Skin',
      variables: ['estradiol', 'progesterone', 'beta-glucuronidase', 'hpa-axis', 'hepatic-detox'],
      clusters: ['B', 'C'],
      interpretation: 'Acne in the FDN model is primarily a hormonal amplification + detoxification failure syndrome. Elevated Beta-glucuronidase in the GI-MAP recirculates deconjugated estrogen metabolites through the Estrogen Recycling Loop (Cluster C), elevating systemic estradiol and stimulating sebaceous gland activity. Low progesterone (Cluster C consequence) removes the anti-androgenic, anti-inflammatory counterbalance. HPA axis dysregulation adds the cortisol-driven sebum stimulation and androgen conversion components. Hepatic Detox Impairment prevents adequate Phase II estrogen conjugation, feeding back into the recycling loop.',
      mechanismTree: 'Beta-glucuronidase (elevated — Cluster C)\n└─ Estrogen deconjugation → reabsorption → elevated systemic estradiol\n   └─ Sebaceous gland stimulation → excess sebum\nProgesterone (low)\n└─ Loss of anti-androgenic counterbalance\n   └─ Androgen receptor hypersensitivity in sebaceous glands\nHPA Dysregulation\n└─ Cortisol → DHEA-S → androgen conversion\n   └─ Androgenic acne driver\nHepatic Detox Impairment\n└─ Phase II conjugation failure → estrogen Phase I intermediates recirculate\n   └─ Amplifies estrogen dominance driving sebum production'
    },
    'skin-ages-fast': {
      label: 'Skin that ages fast',
      category: 'Skin',
      variables: ['ohdg', 'oxidative-stress'],
      clusters: ['A', 'B'],
      interpretation: 'Accelerated skin aging — premature wrinkling, loss of elasticity, uneven pigmentation — is the visible expression of systemic oxidative burden measured by 8-OHdG. Oxidative stress causes DNA damage in dermal fibroblasts, reducing their collagen and elastin synthesis capacity. Reactive oxygen species cross-link collagen fibers, reducing their flexibility and producing the visible texture of oxidative aging. Mitochondrial DNA damage (directly measured by 8-OHdG) impairs cellular energy production in dermal cells, reducing their repair and regeneration capacity.',
      mechanismTree: '8-OHdG (DNA oxidative damage)\n└─ Dermal fibroblast DNA damage\n   └─ Reduced collagen and elastin synthesis capacity\nSystemic Oxidative Stress Cascade\n└─ ROS cross-linking of existing collagen fibers\n   └─ Loss of skin elasticity and flexibility → visible wrinkling\nMitochondrial DNA damage\n└─ Reduced cellular energy for dermal repair\n   └─ Impaired wound healing, reduced cell turnover\n      └─ Dull, aging appearance'
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:SYMPTOMS:BATCH4`
- File now contains all 11 entry keys: `'reactions-many-foods'`, `'gluten-sensitivity'`, `'dairy-reactions'`, `'histamine-food-reactions'`, `'worse-after-fermented'`, `'hives-urticaria'`, `'eczema-rashes'`, `'flushing-redness'`, `'itching-no-rash'`, `'acne'`, `'skin-ages-fast'`
- The other symptom batch placeholders (`BATCH5` through `BATCH7`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-19"`
- `pendingSteps`: remove `"step-19"`
- `flags.symptomsBatch4`: set to `true`
- `artifacts.symptomCount`: increment by `11`
- `dataChunks.symptoms.batch4`: set to `["reactions-many-foods","gluten-sensitivity","dairy-reactions","histamine-food-reactions","worse-after-fermented","hives-urticaria","eczema-rashes","flushing-redness","itching-no-rash","acne","skin-ages-fast"]`
