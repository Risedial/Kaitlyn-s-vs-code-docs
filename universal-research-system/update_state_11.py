import json

path = "C:/Users/Alexb/Documents/Kaitlyn's vs code docs/universal-research-system/state.json"

with open(path, 'r', encoding='utf-8') as f:
    state = json.load(f)

# Remove first 36 pending pairs
state["connections"]["pending"] = state["connections"]["pending"][36:]

new_validated = [
    {"from": "Cortisol-to-DHEA Ratio", "to": "Progesterone", "type": "causal",
     "explanation": "An elevated cortisol:DHEA ratio suppresses progesterone through two simultaneous mechanisms: cortisol (C-21 steroid) competitively occupies progesterone receptors blocking progesterone action, and chronic HPA activation reduces pituitary LH surge amplitude, impairing corpus luteum formation and luteal progesterone synthesis \u2014 Joan's 25.3:1 ratio coexists with severe progesterone deficiency of 56 pg/mL (FDN minimum 222).",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Testosterone", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio suppresses testosterone through three convergent pathways: depleted DHEA reduces androgen precursor substrate; HPA-driven pituitary LH/FSH suppression reduces gonadal production; cortisol-induced adiposity increases aromatase converting testosterone to estradiol. The 18-year-old male case (C:DHEA ratio 11, testosterone 6 pg/mL) demonstrates severity.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Melatonin", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio drives melatonin dysregulation bidirectionally: cortisol excess suppresses nocturnal pineal melatonin causing hyperarousal sleep disruption; DHEA depletion and hypometabolism contribute to elevated noon melatonin from EC cells. FDN Module 2 explicitly lists decreased melatonin and sleep disturbances as downstream consequences of elevated cortisol in the acute/compensatory phase.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Dysbiosis-Intestinal Permeability Feedback Loop", "type": "causal",
     "explanation": "The cortisol:DHEA ratio is the upstream trigger of the FDN Metabolic Chaos cascade (Module 1 Slide 38): elevated ratio suppresses sIgA, enabling dysbiosis and SIBO, which drives intestinal hyperpermeability. Simultaneously, sympathetic dominance suppresses parasympathetic digestive secretions creating hypochlorhydric hypomotile conditions that independently drive the dysbiosis-permeability feedback loop.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Mucosal Immune Tolerance and sIgA Function", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio directly suppresses mucosal immune tolerance through glucocorticoid-receptor-mediated inhibition of GALT plasma cell IgA production, pIgR secretory component transport, and IL-6/IL-10 IgA class-switching signaling. Module 1 Slide 38 names this as the cascade's most proximal step: 'High cortisol:DHEA ratio \u2192 low sIgA.'",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Gut-Brain-HPA Bidirectional Axis", "type": "architectural",
     "explanation": "The cortisol:DHEA ratio is the primary quantitative output marker of the HPA axis operational state, while the Gut-Brain-HPA Bidirectional Axis is the structural feedback system generating and maintaining that ratio. They are co-components of the same system. Module 6 cascade explicitly labels SHP (cortisol, DHEA) as one node in the gut-HPA feedback loop.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Reactive Food Burden \u2014 MRT", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio initiates the cascade producing reactive food burden: cortisol suppresses sIgA, dysbiosis develops, intestinal permeability increases, and food antigens cross into a cytokine-shifted lamina propria that biases toward sensitization, expanding MRT reactive burden. Module 1 Slide 38 names 'antigen penetration' as a downstream step of the ratio elevation pathway.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "H. pylori", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio creates permissive conditions for H. pylori colonization: cortisol-mediated sIgA suppression removes the mucosal immune barrier limiting H. pylori attachment; sympathetic-dominant suppression of parasympathetic activity reduces HCl output, diminishing the gastric acid bactericidal barrier that would otherwise prevent H. pylori establishment.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Candida and Fungal Overgrowth", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio permits Candida overgrowth through two mechanisms: cortisol reduces phagocytic macrophage activity and sIgA production (primary antifungal defenses); cortisol-driven dysbiosis depletes commensal bacteria that occupy mucosal receptor sites and produce antifungal bacteriocins, removing both immune and ecological Candida containment. Candida is specifically associated with IgA damage \u2014 the suppression driven by elevated ratio.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Parasitic Load", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio creates vulnerability to parasitic colonization through cortisol-mediated suppression of sIgA (primary mucosal parasite defense), T-cell and eosinophil function, and gut motility creating stasis conditions favoring parasitic establishment. Module 6 Slide 5 confirms pathogens including parasites as contributors to adrenal dysfunction, establishing bidirectionality.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Dysbiotic and Opportunistic Bacteria", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio enables dysbiotic bacterial overgrowth through two pathways: sIgA suppression removes immune containment of gram-negative pathogens; parasympathetic suppression reduces HCl and bile acids creating the Digestive Dysfunction Dysbiosis conditions favoring bacterial overgrowth. Module 1 Slide 38 explicitly names 'more bad bacteria than good \u2192 dysbiosis' as downstream of the ratio.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Commensal Flora Balance", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio depletes commensal flora through two pathways: sIgA suppression removes selective immune pressure favoring commensals over pathogens, allowing dysbiotic displacement; HCl and digestive secretion suppression via sympathetic dominance creates Digestive Dysfunction Dysbiosis conditions that directly deplete commensal populations. Slide 38: 'more bad bacteria than good' directly states commensal depletion.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Calprotectin and Lactoferrin", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio drives the dysbiosis cascade that, when reaching Inflammatory Dysbiosis pattern (high gram-negative LPS-producing organisms), produces neutrophilic calprotectin/lactoferrin elevation. Module 6 Slide 38 correlates Inflammatory Dysbiosis with elevated calprotectin. Ratio-driven sIgA suppression enables gram-negative colonization whose LPS activates TLR4-NFkB-driven neutrophil recruitment generating calprotectin.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Beta-glucuronidase", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio drives dysbiosis through sIgA suppression and digestive impairment, enabling overgrowth of B-GUS-producing organisms (Bacteroides fragilis, E. coli, Staphylococcus). Joan's ratio 25.3:1 with B-GUS 3584 High alongside multiple dysbiotic organisms demonstrates this pattern: HPA catabolic dominance drives the dysbiotic ecology producing toxic estrogen recycling via B-GUS.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Anti-gliadin IgA", "type": "architectural",
     "explanation": "Elevated cortisol:DHEA ratio suppresses sIgA (Slide 38), and AGA-IgA is sIgA-dependent \u2014 when sIgA is suppressed by elevated cortisol, AGA-IgA is also suppressed producing false negatives. Both Joan (ratio 25.3:1, AGA-IgA 83 normal) and Ashley (AGA-IgA 138 normal) show this pattern with low sIgA. They are co-components of the cortisol-driven mucosal immune suppression system.",
     "evidence_count": 2},
    {"from": "Cortisol-to-DHEA Ratio", "to": "Secretory IgA \u2014 GI tract", "type": "causal",
     "explanation": "Elevated cortisol:DHEA ratio directly suppresses GI tract sIgA through glucocorticoid receptor-mediated inhibition of GALT plasma cell activity, pIgR transport protein reduction, and IL-6/IL-10 class-switching suppression. Module 1 Slide 38: 'High cortisol:DHEA ratio \u2192 low sIgA.' Both Joan (312 Low) and Ashley (359 Low) demonstrate GI sIgA suppression alongside elevated cortisol:DHEA ratios.",
     "evidence_count": 2},
    {"from": "Estradiol", "to": "Progesterone", "type": "architectural",
     "explanation": "Estradiol and Progesterone form the Pg:E2 ratio (5th Fundamental Homeostatic Control per Wolcott), an architectural counterbalance system requiring simultaneous evaluation. Elevated E2 with inadequate progesterone produces estrogen dominance even when absolute E2 appears normal. Both Joan (ratio 10:1) and Ashley (ratio 9:1) are 4\u20137x below FDN minimum of 42.7\u201367.5:1, demonstrating how E2 and P4 are clinically co-defined by their relationship.",
     "evidence_count": 2},
    {"from": "Estradiol", "to": "Testosterone", "type": "architectural",
     "explanation": "Estradiol and testosterone are co-outputs of the steroidogenesis cascade with an inverse aromatase-mediated relationship: adipose CYP19A1 converts testosterone to estradiol, simultaneously reducing testosterone and elevating E2. The T:E2 ratio is a FDN clinical marker (Joan: T:E2 1.6 vs. FDN optimal 5.0\u20138.25). This aromatase pathway creates a direct architectural link between both sex hormone markers.",
     "evidence_count": 2},
    {"from": "Estradiol", "to": "Dysbiosis-Intestinal Permeability Feedback Loop", "type": "architectural",
     "explanation": "Elevated beta-glucuronidase from gut dysbiosis deconjugates bile-excreted estrogens returning them to portal circulation, driving elevated circulating estradiol \u2014 an architectural link where the dysbiosis-permeability loop produces estradiol elevation through its B-GUS enzymatic output. Both are co-components of the B-GUS-estrogen recycling pathway within the metabolic chaos system.",
     "evidence_count": 2},
    {"from": "Estradiol", "to": "Gut-Brain-HPA Bidirectional Axis", "type": "architectural",
     "explanation": "Estradiol is both a downstream output of the Gut-Brain-HPA Bidirectional Axis (cortisol-driven steroidogenesis disruption and peripheral aromatase activation produce estrogen dominance) and an upstream contributor to HPA activation. The FDN cascade positions sex hormone dysregulation including estradiol as both product and perpetuator of the metabolic chaos axis. Module 6 cascade lists SHP estradiol as a named cascade node.",
     "evidence_count": 2},
    {"from": "Progesterone", "to": "Testosterone", "type": "architectural",
     "explanation": "Progesterone and testosterone are co-outputs of the adrenal/gonadal steroidogenesis cascade: both require adequate DHEA substrate and HPA functional capacity; pituitary LH suppression from HPA catabolic dominance reduces both progesterone (via corpus luteum) and testosterone (via gonadal production) simultaneously. Module 3 steroidogenesis pathway shows both P4 and T as downstream products of the same precursor pool.",
     "evidence_count": 2}
]

new_discarded = [
    {"from": "Cortisol-to-DHEA Ratio", "to": "Occult Blood",
     "reason": "Elevated cortisol:DHEA ratio does not reliably predict occult blood; occult blood reflects structural mucosal pathology (polyps, cancer, ulcers, IBD) rather than functional HPA-driven dysbiosis. Both case study patients show dissociation: Joan's extreme ratio 25.3:1 with occult blood 0. Causal pathway requires multiple unconfirmed intermediate steps without meeting Relevant confidence threshold."},
    {"from": "Estradiol", "to": "Melatonin",
     "reason": "Estradiol dominance produces sleep disturbances through temperature dysregulation and anxiety-mediated arousal, but FDN source materials do not document a direct structural pathway between estradiol levels and melatonin production or regulation. No \u22652 independent evidence lines at Relevant confidence."},
    {"from": "Estradiol", "to": "Mucosal Immune Tolerance and sIgA Function",
     "reason": "Estradiol and mucosal sIgA share HPA-cortisol as a common upstream driver but no direct structural mechanism connecting estradiol to sIgA production is documented in FDN source materials. They are co-indicators of HPA dysfunction rather than structurally connected."},
    {"from": "Estradiol", "to": "Reactive Food Burden \u2014 MRT",
     "reason": "No direct structural connection between estradiol levels and reactive food burden in FDN source materials. Reactive food burden is driven by sIgA depletion and gut permeability from HPA-cortisol dysregulation; estradiol is a co-downstream product of that cascade, not a direct driver."},
    {"from": "Estradiol", "to": "H. pylori",
     "reason": "No structural connection between estradiol levels and H. pylori colonization in FDN source materials. H. pylori colonization is enabled by sIgA depletion and gastric acid barrier compromise (HPA-cortisol-mediated), not by estradiol levels specifically."},
    {"from": "Estradiol", "to": "Candida and Fungal Overgrowth",
     "reason": "No direct structural connection between estradiol levels and Candida overgrowth documented in FDN source materials. Candida is enabled by immune suppression (sIgA, IgA damage, heavy metals) and commensal depletion \u2014 mechanisms not directly driven by estradiol in the FDN framework."},
    {"from": "Estradiol", "to": "Parasitic Load",
     "reason": "No structural connection between estradiol levels and parasitic load in FDN source materials. Parasitic susceptibility is enabled by sIgA depletion and mucosal immune compromise driven by HPA-cortisol, not by estradiol specifically."},
    {"from": "Estradiol", "to": "Dysbiotic and Opportunistic Bacteria",
     "reason": "The structural connection is directional: dysbiotic bacteria produce beta-glucuronidase that deconjugates hepatically-processed estrogens driving elevated circulating estradiol. The reverse pathway (estradiol driving dysbiotic bacteria) is not documented in FDN source materials."},
    {"from": "Estradiol", "to": "Commensal Flora Balance",
     "reason": "No structural connection between estradiol levels and commensal flora balance in FDN source materials. Both reflect downstream consequences of HPA-cortisol dysregulation but estradiol does not directly drive commensal depletion."},
    {"from": "Estradiol", "to": "Calprotectin and Lactoferrin",
     "reason": "No structural connection between estradiol levels and calprotectin/lactoferrin in FDN source materials. Calprotectin reflects neutrophilic GI inflammation driven by gram-negative pathogen LPS burden, not hormonal dysregulation."},
    {"from": "Estradiol", "to": "Beta-glucuronidase",
     "reason": "The structural connection is directional: B-GUS deconjugates bile-excreted estrogens returning them to circulation, driving elevated estradiol (validated connection). The reverse pathway (elevated estradiol driving B-GUS elevation) is not documented in FDN source materials."},
    {"from": "Estradiol", "to": "Anti-gliadin IgA",
     "reason": "No structural connection between estradiol levels and anti-gliadin IgA in FDN source materials. AGA-IgA is determined by sIgA status and gliadin antigen exposure, not by estradiol."},
    {"from": "Estradiol", "to": "Secretory IgA \u2014 GI tract",
     "reason": "No direct structural connection between estradiol levels and GI tract sIgA production in FDN source materials. GI sIgA is primarily driven by cortisol suppression and commensal flora SCFA support, not by estradiol specifically."},
    {"from": "Estradiol", "to": "Occult Blood",
     "reason": "No structural connection between estradiol levels and occult blood. Occult blood reflects structural GI mucosal bleeding from lesions (polyps, cancer, IBD); estradiol excess does not specifically predict structural mucosal bleeding."},
    {"from": "Progesterone", "to": "Melatonin",
     "reason": "Progesterone deficiency produces sleep disruption through GABA-A receptor pathway (allopregnanolone binding) rather than through melatonin dysregulation. FDN source materials do not document a direct structural connection between progesterone levels and melatonin production or EC cell activity."}
]

state["connections"]["validated"].extend(new_validated)
state["connections"]["discarded"].extend(new_discarded)

state["last_updated"] = "2026-03-24T21:00:00Z"

session_entry = {
    "date": "2026-03-24T21:00:00Z",
    "phase_executed": "connection_validation",
    "variables_researched": [],
    "connections_validated": [
        "Cortisol-to-DHEA Ratio -> Progesterone",
        "Cortisol-to-DHEA Ratio -> Testosterone",
        "Cortisol-to-DHEA Ratio -> Melatonin",
        "Cortisol-to-DHEA Ratio -> Dysbiosis-Intestinal Permeability Feedback Loop",
        "Cortisol-to-DHEA Ratio -> Mucosal Immune Tolerance and sIgA Function",
        "Cortisol-to-DHEA Ratio -> Gut-Brain-HPA Bidirectional Axis",
        "Cortisol-to-DHEA Ratio -> Reactive Food Burden \u2014 MRT",
        "Cortisol-to-DHEA Ratio -> H. pylori",
        "Cortisol-to-DHEA Ratio -> Candida and Fungal Overgrowth",
        "Cortisol-to-DHEA Ratio -> Parasitic Load",
        "Cortisol-to-DHEA Ratio -> Dysbiotic and Opportunistic Bacteria",
        "Cortisol-to-DHEA Ratio -> Commensal Flora Balance",
        "Cortisol-to-DHEA Ratio -> Calprotectin and Lactoferrin",
        "Cortisol-to-DHEA Ratio -> Beta-glucuronidase",
        "Cortisol-to-DHEA Ratio -> Anti-gliadin IgA",
        "Cortisol-to-DHEA Ratio -> Secretory IgA \u2014 GI tract",
        "Estradiol -> Progesterone",
        "Estradiol -> Testosterone",
        "Estradiol -> Dysbiosis-Intestinal Permeability Feedback Loop",
        "Estradiol -> Gut-Brain-HPA Bidirectional Axis",
        "Progesterone -> Testosterone"
    ],
    "connections_discarded": [
        "Cortisol-to-DHEA Ratio -> Occult Blood",
        "Estradiol -> Melatonin",
        "Estradiol -> Mucosal Immune Tolerance and sIgA Function",
        "Estradiol -> Reactive Food Burden \u2014 MRT",
        "Estradiol -> H. pylori",
        "Estradiol -> Candida and Fungal Overgrowth",
        "Estradiol -> Parasitic Load",
        "Estradiol -> Dysbiotic and Opportunistic Bacteria",
        "Estradiol -> Commensal Flora Balance",
        "Estradiol -> Calprotectin and Lactoferrin",
        "Estradiol -> Beta-glucuronidase",
        "Estradiol -> Anti-gliadin IgA",
        "Estradiol -> Secretory IgA \u2014 GI tract",
        "Estradiol -> Occult Blood",
        "Progesterone -> Melatonin"
    ],
    "output_file": "session-outputs/2026-03-24-connection-validation-11.md"
}
state["session_log"].append(session_entry)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)

with open(path, 'r', encoding='utf-8') as f:
    v = json.load(f)

print("Pending remaining:", len(v["connections"]["pending"]))
print("Validated total:", len(v["connections"]["validated"]))
print("Discarded total:", len(v["connections"]["discarded"]))
print("Session log entries:", len(v["session_log"]))
print("Phase:", v["phase"])
print("Last updated:", v["last_updated"])
