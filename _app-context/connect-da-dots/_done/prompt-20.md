# Prompt 20: Write JS — Symptom Data: Immune System + Hormonal (Female) Categories (12 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:SYMPTOMS:BATCH5` in `fdn-pwa/index.html` with the 12 Immune System + Hormonal (Female) symptom entries below.

Write ALL 12 entries replacing `// PLACEHOLDER:SYMPTOMS:BATCH5`:

```javascript
    'get-sick-constantly': {
      label: 'Get sick constantly',
      category: 'Immune System',
      variables: ['sigas-shp', 'sigas-gi', 'hpa-axis', 'cortisol-diurnal'],
      clusters: ['A', 'B'],
      interpretation: 'Repeated infections — colds, sinusitis, respiratory infections — more than 3–4 times per year reflects collapse of mucosal immune defense. sIgA-SHP (salivary) measures systemic immune defense under HPA control; its suppression by cortisol dysregulation removes the primary upper respiratory mucosal defense. sIgA-GI (stool) measures gut mucosal defense; its depletion reflects GI pathogen burden and immune collapse at the primary exposure site. Both sIgA values falling simultaneously confirm that HPA-driven cortisol is globally suppressing mucosal immunity across all barrier surfaces.',
      mechanismTree: 'HPA Dysregulation (elevated cortisol)\n└─ Cortisol → global sIgA suppression\n   └─ sIgA-SHP low: upper respiratory defense removed\n   └─ sIgA-GI low: gut mucosal defense removed\nLoss of mucosal IgA barriers\n└─ Pathogens no longer neutralized at first contact\n   └─ Frequent infections — colds, sinusitis, GI illness\nCortisol Diurnal Pattern\n└─ Morning cortisol spike timing: if elevated, immune suppression is active\n   └─ Correlation: highest infection frequency at HPA resistance phase'
    },
    'slow-recovery-illness': {
      label: 'Take forever to recover from illness',
      category: 'Immune System',
      variables: ['sigas-shp', 'dhea', 'oxidative-stress', 'hepatic-detox'],
      clusters: ['A', 'B'],
      interpretation: 'Prolonged recovery from illness indicates failure of the resolution phase of immune response rather than failure of the initial response. DHEA is required for immune resolution and anti-inflammatory signaling; its depletion from Pregnenolone Steal leaves the body unable to turn off the inflammatory response after the pathogen is cleared. Systemic oxidative stress impairs the cellular repair processes needed for tissue recovery. Hepatic Detox Impairment means inflammatory cytokine metabolites and pathogen debris are not efficiently cleared from circulation, prolonging the post-illness malaise.',
      mechanismTree: 'DHEA depletion (HPA consequence)\n└─ Loss of immune resolution signaling\n   └─ Inflammatory response cannot terminate efficiently\n      └─ Prolonged post-illness inflammation\nSystemic Oxidative Stress Cascade\n└─ Impaired cellular repair and tissue regeneration\n   └─ Prolonged recovery time after resolution of pathogen\nHepatic Detox Impairment\n└─ Inflammatory byproducts and pathogen debris not cleared\n   └─ Prolonged systemic malaise after acute illness phase'
    },
    'allergies-getting-worse': {
      label: 'Allergies getting worse over time',
      category: 'Immune System',
      variables: ['sigas-gi', 'zonulin', 'histamine-mba', 'dao'],
      clusters: ['A', 'D'],
      interpretation: 'Progressive worsening of allergic reactivity — more allergens, more severe reactions over time — is mechanistically explained by cumulative Zonulin-mediated gut barrier failure. Each leaky gut episode allows new environmental and food antigens to reach subepithelial immune tissue, priming new sensitizations. The allergic repertoire expands because the barrier that prevents initial sensitization is chronically compromised. Low sIgA-GI removes the secretory IgA "immune exclusion" mechanism that normally captures and neutralizes antigens before they can prime sensitization.',
      mechanismTree: 'Zonulin (chronic gut barrier failure)\n└─ Ongoing antigen translocation → progressive immune sensitization\n   └─ New allergen sensitizations added over time\n      └─ Expanding allergy spectrum\nsIgA-GI (low — immune exclusion lost)\n└─ sIgA normally captures and neutralizes antigens at mucosa\n   └─ Without sIgA: antigens reach subepithelial immune tissue freely\n      └─ Sensitization rate accelerates\nHistamine-MBA + Low DAO\n└─ Histamine amplifies mast cell reactivity threshold lowering\n   └─ Allergic reactions become more severe even without new sensitizations'
    },
    'autoimmune-condition': {
      label: 'Autoimmune condition or suspicion',
      category: 'Immune System',
      variables: ['zonulin', 'ohdg', 'oxidative-stress'],
      clusters: ['A', 'B'],
      interpretation: 'Autoimmune activation in the FDN model is mechanistically traced to sustained Zonulin-mediated intestinal hyperpermeability allowing self-antigen molecular mimicry: gut-resident microbial antigens structurally similar to self-tissues cross the epithelium and prime cytotoxic T-cell responses against both the microbial antigen and the structurally similar self-tissue. Systemic oxidative stress accelerates this process by damaging cellular membranes, exposing normally sequestered self-antigens to immune surveillance. The practitioner should prioritize gut barrier restoration as the primary mechanism to interrupt ongoing autoimmune amplification.',
      mechanismTree: 'Zonulin (sustained tight junction disassembly)\n└─ Microbial antigen translocation into systemic immune compartment\n   └─ Molecular mimicry: microbial antigen resembles self-tissue antigen\n      └─ Cytotoxic T-cell cross-reactivity → autoimmune attack\nSystemic Oxidative Stress (8-OHdG)\n└─ Membrane lipid peroxidation → neo-antigen exposure\n   └─ Previously sequestered self-antigens exposed to immune surveillance\n      └─ New autoimmune sensitizations added\nGut barrier restoration priority\n└─ Interrupting ongoing antigen translocation is upstream of all downstream autoimmune amplification'
    },
    'frequent-uti-yeast': {
      label: 'Frequent UTIs, yeast infections, or infections',
      category: 'Immune System',
      variables: ['candida', 'sigas-gi', 'hpa-axis', 'cortisol-diurnal'],
      clusters: ['A', 'B'],
      interpretation: 'Recurrent opportunistic infections — UTIs, vaginal yeast infections, oral thrush, skin fungal infections — confirm systemic immune competence failure. Candida elevation in GI-MAP reflects GI immune collapse that enables yeast overgrowth at the primary colonization site; Candida then disseminates to other mucosal surfaces when systemic immunity is also suppressed. HPA dysregulation drives this through cortisol-mediated immune suppression: cortisol suppresses neutrophil function, reduces sIgA, and creates a hormonal environment that promotes Candida virulence factor expression.',
      mechanismTree: 'Candida (GI-MAP — overgrowth confirmed)\n└─ GI immune collapse → Candida colonization of gut\n   └─ Systemic dissemination to vaginal, urinary, skin surfaces\nHPA Dysregulation (cortisol)\n└─ Cortisol → neutrophil function suppression\n   └─ Candida virulence factor expression promoted\n      └─ Opportunistic infection cascade\nsIgA-GI (low)\n└─ Loss of mucosal Candida containment\n   └─ Candida biofilm formation at mucosal surfaces'
    },
    'pms-pmdd': {
      label: 'PMS / PMDD',
      category: 'Hormonal (Female)',
      variables: ['estradiol', 'progesterone', 'beta-glucuronidase', 'hpa-axis', 'cortisol-diurnal'],
      clusters: ['B', 'C'],
      interpretation: 'PMS and PMDD are driven by Estradiol:Progesterone imbalance amplified by the Estrogen Recycling Loop (Cluster C). Beta-glucuronidase deconjugates Phase II estrogen metabolites in the gut, allowing them to re-enter circulation as active estrogens — producing estrogen dominance in the luteal phase when progesterone should be dominant. HPA dysregulation compounds this by suppressing progesterone synthesis via Pregnenolone Steal. The Cortisol:DHEA ratio (assessed from SHP panel values) determines the degree of HPA-driven progesterone suppression. This is the Cluster B + C convergence signature.',
      mechanismTree: 'Beta-glucuronidase (elevated — Cluster C)\n└─ Estrogen deconjugation → re-circulation of Phase II metabolites\n   └─ Estrogen dominance in luteal phase (progesterone should dominate)\n      └─ PMS symptom pattern: mood, bloating, breast tenderness\nHPA Dysregulation (Pregnenolone Steal)\n└─ Cortisol demand diverts pregnenolone from progesterone synthesis\n   └─ Progesterone insufficiency → amplified luteal estrogen dominance\nCortisol Diurnal Pattern\n└─ Cortisol:DHEA ratio distortion → worsened hormonal volatility\n   └─ Pre-menstrual amplification of cortisol-progesterone antagonism'
    },
    'irregular-periods': {
      label: 'Irregular periods',
      category: 'Hormonal (Female)',
      variables: ['estradiol', 'progesterone', 'cortisol-diurnal', 'hpa-axis', 'pregnenolone-steal'],
      clusters: ['B', 'C'],
      interpretation: 'Menstrual irregularity in the FDN model is primarily driven by HPA disruption of the HPO (Hypothalamic-Pituitary-Ovarian) axis. Elevated cortisol directly suppresses GnRH pulsatility, disrupting the LH surge that triggers ovulation — producing anovulatory cycles or irregular ovulation timing. Pregnenolone Steal diverts steroidogenic substrate away from sex hormone synthesis, lowering the baseline Estradiol and Progesterone needed for regular cycle signaling. The practitioner should assess whether anovulation or luteal phase insufficiency is the primary mechanism using cycle phase-specific SHP values.',
      mechanismTree: 'HPA Dysregulation (cortisol)\n└─ Cortisol → GnRH pulsatility suppression\n   └─ Disrupted LH surge → anovulation or delayed ovulation\n      └─ Irregular, absent, or prolonged cycle\nPregnenolone Steal (active)\n└─ Steroidogenic substrate diverted from sex hormones to cortisol\n   └─ Estradiol and progesterone baselines lowered\n      └─ Insufficient hormonal signaling for regular cycle triggering\nEstradiol:Progesterone ratio\n└─ Imbalance prevents reliable endometrial signaling\n   └─ Unpredictable period onset and flow duration'
    },
    'heavy-periods': {
      label: 'Heavy periods',
      category: 'Hormonal (Female)',
      variables: ['estradiol', 'progesterone', 'beta-glucuronidase'],
      clusters: ['C'],
      interpretation: 'Heavy menstrual bleeding (menorrhagia) in the FDN context is the primary clinical expression of Cluster C — Estrogen Recycling Loop. Elevated Beta-glucuronidase maintains elevated circulating estrogens (from re-absorbed deconjugated metabolites), driving endometrial hypertrophy and excess proliferation during the follicular phase. Low progesterone fails to provide the anti-proliferative counterbalance and adequate endometrial stabilization. The resulting endometrium is excessively thick with fragile vasculature, leading to heavy, often prolonged bleeding at menstruation.',
      mechanismTree: 'Beta-glucuronidase (elevated — core Cluster C mechanism)\n└─ Phase II estrogen metabolite deconjugation → re-absorption\n   └─ Sustained elevated estradiol driving endometrial proliferation\nEstradiol (elevated via recycling)\n└─ Endometrial hypertrophy → thick, vascular-rich lining\n   └─ Heavy bleeding when endometrium sheds\nProgesterone (low)\n└─ Loss of anti-proliferative endometrial stabilization\n   └─ Vascular fragility → excessive bleeding duration and volume'
    },
    'low-libido': {
      label: 'Low libido',
      category: 'Hormonal (Female)',
      variables: ['testosterone', 'dhea', 'hpa-axis', 'pregnenolone-steal', 'indican'],
      clusters: ['A', 'B'],
      interpretation: 'Female libido requires adequate testosterone (though at lower levels than in males) and DHEA as direct androgen precursors. Pregnenolone Steal suppresses DHEA synthesis, which reduces both DHEA and its downstream testosterone conversion. HPA exhaustion compounds this by removing the energy and wellbeing substrate for sexual interest. Indican-driven tryptophan theft depletes serotonin, which at appropriate levels is required for sexual arousal signaling — but this also depletes dopamine precursors critical for the motivational component of libido.',
      mechanismTree: 'Pregnenolone Steal (active)\n└─ Cortisol demand depletes pregnenolone pool\n   └─ DHEA synthesis suppressed → testosterone conversion reduced\n      └─ Androgen deficit → libido loss\nHPA Exhaustion (Phase 3–4)\n└─ Energy deficit state → sexual motivation absent\n   └─ Physical depletion removes libido substrate\nIndican (tryptophan theft)\n└─ Serotonin and dopamine precursor depletion\n   └─ Reward and arousal circuitry underactive → anorgasmia risk'
    },
    'hot-flashes': {
      label: 'Hot flashes',
      category: 'Hormonal (Female)',
      variables: ['estradiol', 'histamine-mba', 'progesterone', 'hpa-axis'],
      clusters: ['B', 'C', 'D'],
      interpretation: 'Hot flashes are a thermoregulatory instability phenomenon driven by the convergence of estrogen withdrawal and histamine-mediated vasodilation. Falling estradiol destabilizes the hypothalamic thermostat, narrowing the thermoneutral zone and triggering vasodilation episodes at lower temperature thresholds. Histamine is a potent direct vasodilator — elevated Histamine-MBA lowers the threshold for hot flash triggering. Low progesterone removes the calming, anti-estrogenic progesterone effect on hypothalamic GnRH pulsatility that normally stabilizes thermoregulation. HPA dysregulation adds cortisol-driven autonomic instability.',
      mechanismTree: 'Estradiol dysregulation (falling or fluctuating)\n└─ Hypothalamic thermostat destabilization\n   └─ Narrowed thermoneutral zone → vasodilation triggered at lower threshold\nHistamine-MBA (elevated)\n└─ Direct vasodilatory H1 activation\n   └─ Triggers or amplifies hot flash vasodilation episode\nProgesterone (low)\n└─ Loss of hypothalamic GnRH-calming effect\n   └─ Increased GnRH pulsatility → amplified LH surge effect on thermoregulation\nHPA Dysregulation\n└─ Sympathetic autonomic instability\n   └─ Exaggerated sweating response to vasodilation trigger'
    },
    'infertility-difficulty-conceiving': {
      label: 'Infertility or difficulty conceiving',
      category: 'Hormonal (Female)',
      variables: ['progesterone', 'estradiol', 'hpa-axis', 'pregnenolone-steal', 'beta-glucuronidase'],
      clusters: ['B', 'C'],
      interpretation: 'Fertility requires adequate progesterone for both ovulation and luteal phase endometrial preparation. Pregnenolone Steal (the central Cluster B-C intersection mechanism) diverts steroidogenic substrate from sex hormones to cortisol synthesis — suppressing DHEA, testosterone, and progesterone. Insufficient luteal phase progesterone prevents adequate endometrial preparation for implantation. Beta-glucuronidase-driven estrogen recycling produces relative estrogen dominance, disrupting the precise Estradiol:Progesterone ratio required for successful implantation signaling.',
      mechanismTree: 'Pregnenolone Steal (Cluster B-C intersection)\n└─ Cortisol synthesis prioritized over sex hormone synthesis\n   └─ Progesterone synthesis suppressed\n      └─ Luteal phase insufficiency → failed implantation\nBeta-glucuronidase (elevated)\n└─ Estrogen recycling → elevated estradiol\n   └─ Disrupted Estradiol:Progesterone implantation ratio\nHPA Dysregulation\n└─ GnRH pulsatility disruption → anovulation or irregular ovulation\n   └─ Reduced conception windows\nProgesterone (low — direct measurement)\n└─ Insufficient endometrial preparation\n   └─ Implantation failure pattern'
    },
    'estrogen-dominance-symptoms': {
      label: 'Estrogen dominance symptoms (weight in hips, painful breasts, water retention)',
      category: 'Hormonal (Female)',
      variables: ['estradiol', 'beta-glucuronidase', 'progesterone', 'hepatic-detox'],
      clusters: ['C'],
      interpretation: 'Estrogen dominance — the cluster of peripheral fat deposition (hips/thighs), fibrocystic breast tissue, water retention, and mood volatility — is the primary clinical expression of the Cluster C Estrogen Recycling Loop. Elevated Beta-glucuronidase maintains supraphysiologic estrogen recirculation even when production is normal. Hepatic Detox Impairment adds a second mechanism: when Phase I/II hepatic estrogen conjugation is impaired, estrogen clearance is slowed and both parent estrogens and Phase I hydroxylation products accumulate. This is the reason estrogen dominance symptoms often occur in women with seemingly "normal" estrogen lab values.',
      mechanismTree: 'Beta-glucuronidase (elevated — Cluster C primary driver)\n└─ Gut deconjugation of Phase II estrogen-glucuronide\n   └─ Reabsorbed estrogens re-enter portal circulation\n      └─ Supraphysiologic estrogen load → dominance symptoms\nHepatic Detox Impairment\n└─ Slow Phase II conjugation of estrogen metabolites\n   └─ Accumulation of Phase I hydroxylated estrogen intermediates (16-OHE1)\n      └─ Estrogen activity amplified, clearance slowed\nProgesterone (low)\n└─ Loss of anti-estrogenic competition at receptor level\n   └─ Unopposed estrogen stimulation of breast, uterine, fat tissue'
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:SYMPTOMS:BATCH5`
- File now contains all 12 entry keys: `'get-sick-constantly'`, `'slow-recovery-illness'`, `'allergies-getting-worse'`, `'autoimmune-condition'`, `'frequent-uti-yeast'`, `'pms-pmdd'`, `'irregular-periods'`, `'heavy-periods'`, `'low-libido'`, `'hot-flashes'`, `'infertility-difficulty-conceiving'`, `'estrogen-dominance-symptoms'`
- The other symptom batch placeholders (`BATCH6` and `BATCH7`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-20"`
- `pendingSteps`: remove `"step-20"`
- `flags.symptomsBatch5`: set to `true`
- `artifacts.symptomCount`: increment by `12`
- `dataChunks.symptoms.batch5`: set to `["get-sick-constantly","slow-recovery-illness","allergies-getting-worse","autoimmune-condition","frequent-uti-yeast","pms-pmdd","irregular-periods","heavy-periods","low-libido","hot-flashes","infertility-difficulty-conceiving","estrogen-dominance-symptoms"]`
