import json

with open('state.json', 'r', encoding='utf-8') as f:
    state = json.load(f)

# ============================================================
# 35 VALIDATED connections (pairs 1-5 and 7-36)
# ============================================================
new_validated = [
    {
        "from": "Histamine \u2014 MBA",
        "to": "Commensal Flora Balance",
        "type": "architectural",
        "explanation": "Both elevated histamine and commensal flora disruption are co-markers of the same dysbiotic ecology; histamine-decarboxylase bacteria proliferate when commensal flora is disrupted, making elevated histamine and disrupted commensal balance co-expressions of the same underlying microbial imbalance.",
        "evidence_count": 2
    },
    {
        "from": "Histamine \u2014 MBA",
        "to": "Calprotectin and Lactoferrin",
        "type": "correlational",
        "explanation": "Elevated histamine drives mast cell degranulation and inflammatory cytokine release that recruits neutrophils to GI tissue; elevated calprotectin and lactoferrin co-occur with histamine excess as co-markers of active GI mucosal inflammation and innate immune activation.",
        "evidence_count": 2
    },
    {
        "from": "Histamine \u2014 MBA",
        "to": "Beta-glucuronidase",
        "type": "architectural",
        "explanation": "Both elevated histamine and elevated beta-glucuronidase are products of the same dysbiotic ecology; histamine-decarboxylase bacteria and beta-glucuronidase-producing bacteria (E. coli, Clostridium) both proliferate in the same disrupted microbiome conditions, making them co-markers of the same dysbiotic ecosystem.",
        "evidence_count": 2
    },
    {
        "from": "Histamine \u2014 MBA",
        "to": "Anti-gliadin IgA",
        "type": "causal",
        "explanation": "Elevated histamine drives Zonulin release and tight junction disassembly, increasing intestinal permeability; this permeability increase allows gliadin antigen penetration through the mucosal barrier into the lamina propria, triggering anti-gliadin IgA immune sensitization and production.",
        "evidence_count": 2
    },
    {
        "from": "Histamine \u2014 MBA",
        "to": "Secretory IgA \u2014 GI tract",
        "type": "architectural",
        "explanation": "Both histamine regulation and mucosal sIgA production are dependent on mucosal architectural integrity and HPA-cortisol signaling; cortisol (which activates mast cell histamine release) simultaneously suppresses sIgA production, making both markers co-expressions of the stress-mucosal immune axis disruption.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Systemic Oxidative Stress Cascade",
        "type": "causal",
        "explanation": "DAO deficiency leads to histamine accumulation driving inflammatory cytokine cascades that generate ROS through neutrophil and macrophage oxidative burst; additionally, intestinal mucosal damage underlying DAO depletion generates systemic oxidative stress via mitochondrial injury and LPS-driven Kupffer cell ROS production.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Hepatic Detoxification Impairment",
        "type": "causal",
        "explanation": "DAO deficiency allows histamine to enter portal circulation, adding to hepatic detoxification burden via the HNMT hepatic pathway; simultaneously, intestinal permeability associated with low DAO allows LPS and bacterial products into portal blood, activating Kupffer cells and driving hepatic inflammation and Phase I/II detoxification impairment.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Histamine-DAO Regulatory System",
        "type": "architectural",
        "explanation": "DAO is the defining enzymatic component of the Histamine-DAO Regulatory System; DAO deficiency directly shifts the histamine-DAO balance toward histamine excess, and DAO production and activity status determines the functional capacity of the entire regulatory system.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Secretory IgA \u2014 SHP",
        "type": "causal",
        "explanation": "DAO deficiency and associated gut mucosal damage activate the gut-brain-HPA axis via LPS translocation and cytokine signaling, driving cortisol elevation that directly and dose-dependently suppresses sIgA production; both DAO depletion and low sIgA are downstream markers of the chronic gut-HPA inflammatory cascade.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "HPA Axis Dysregulation Pattern",
        "type": "architectural",
        "explanation": "Both DAO deficiency and HPA dysregulation are components of the gut-HPA bidirectional axis; gut mucosal damage driving DAO depletion constitutes a chronic physiological stressor activating HPA dysregulation, while HPA activation via the cortisol-mast cell-histamine loop worsens the mucosal environment that produces DAO.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Pregnenolone Steal and Steroidogenesis Disruption",
        "type": "causal",
        "explanation": "DAO deficiency drives gut-HPA axis activation generating chronic cortisol demand that preferentially routes pregnenolone to cortisol synthesis at expense of DHEA and sex hormones (pregnenolone steal); chronic adrenal activation from GI mucosal inflammatory burden drives steroidogenesis disruption through the HPA-adrenal pathway.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Cortisol \u2014 Diurnal Pattern",
        "type": "causal",
        "explanation": "Chronic gut mucosal pathology signaled by low DAO activates the gut-brain-HPA axis continuously through LPS translocation and cytokine signaling, disrupting the normal cortisol diurnal curve; the histamine excess from DAO deficiency sustains the cortisol-mast cell-histamine feedback loop (Stress-Induced Hyper-permeability Cycle) that distorts the diurnal pattern.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "DHEA-S",
        "type": "causal",
        "explanation": "DAO deficiency drives chronic gut inflammatory state activating the HPA axis and elevating cortisol; elevated cortisol reciprocally suppresses DHEA-S production in the zona reticularis through competitive adrenal precursor allocation, shifting the adrenal axis toward catabolic dominance.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Cortisol-to-DHEA Ratio",
        "type": "causal",
        "explanation": "The gut-HPA pathway activated by DAO deficiency simultaneously drives cortisol elevation and DHEA-S suppression, directly shifting the Cortisol:DHEA ratio toward catabolic dominance; DAO deficiency is therefore a predictor of worsening ratio trajectory through both arms of the ratio.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Estradiol",
        "type": "causal",
        "explanation": "DAO deficiency allows histamine accumulation that activates H2 receptors on ovarian granulosa cells stimulating estradiol secretion; DAO deficiency also participates in the histamine-DAO-estrogen positive feedback loop where reduced DAO allows histamine buildup that drives estradiol elevation while elevated estradiol further downregulates DAO gene expression.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Progesterone",
        "type": "causal",
        "explanation": "DAO deficiency drives progesterone insufficiency through two pathways: histamine excess from low DAO elevates estradiol creating estrogen dominance and relative progesterone deficiency; and HPA activation from gut mucosal inflammation elevates cortisol that suppresses pituitary LH surge amplitude, impairing corpus luteum formation and luteal progesterone production.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Testosterone",
        "type": "causal",
        "explanation": "DAO deficiency reduces testosterone through two converging pathways: histamine excess drives estrogen elevation that increases SHBG, reducing free testosterone bioavailability; and HPA activation from gut mucosal pathology drives pituitary LH/FSH suppression, reducing gonadal testosterone production.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Melatonin",
        "type": "architectural",
        "explanation": "DAO-producing crypt cells and melatonin-producing enterochromaffin (EC) cells are both intestinal mucosal cell populations impaired by the same pathological mucosal damage; HPA activation from DAO-related gut inflammation also drives cortisol elevation that inversely suppresses nocturnal melatonin production through the documented cortisol-melatonin inverse relationship.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Dysbiosis-Intestinal Permeability Feedback Loop",
        "type": "architectural",
        "explanation": "DAO is a direct biomarker of intestinal permeability (serum DAO activity correlates inversely with intestinal permeability); DAO deficiency is both a marker within and an amplifier of the dysbiosis-permeability feedback loop, as DAO loss from crypt damage increases histamine accumulation that worsens permeability via Zonulin pathway.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Mucosal Immune Tolerance and sIgA Function",
        "type": "architectural",
        "explanation": "DAO-producing crypt cells and sIgA-producing lamina propria plasma cells are adjacent co-components of the same mucosal architecture; pathological states causing crypt cell apoptosis (depleting DAO) simultaneously damage the lamina propria IgA infrastructure, making both co-dependent biomarkers of mucosal immune tolerance and architectural integrity.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Gut-Brain-HPA Bidirectional Axis",
        "type": "causal",
        "explanation": "DAO deficiency allows histamine accumulation that acts as an enteric nervous system neuromodulator signaling through vagal afferents to the HPA axis; simultaneously, gut mucosal damage (signaled by low DAO) activates the gut-brain-HPA axis through LPS translocation and inflammatory cytokine signaling via the bidirectional gut-brain communication pathway.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Reactive Food Burden \u2014 MRT",
        "type": "causal",
        "explanation": "DAO deficiency correlates with intestinal permeability, allowing dietary antigens to penetrate the mucosal barrier and trigger immune sensitization measurable by MRT; additionally, impaired histamine clearance from DAO deficiency directly amplifies mediator release responses to foods, since histamine is itself a primary inflammatory mediator captured by MRT.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "H. pylori",
        "type": "architectural",
        "explanation": "H. pylori causes gastric and duodenal mucosal damage that destroys DAO-producing crypt cells in affected regions, making both low DAO and H. pylori co-markers of the same mucosal pathological environment; H. pylori-associated inflammation generates histamine and reduces DAO capacity, creating the dual DAO-depletion/histamine-excess pattern.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Candida and Fungal Overgrowth",
        "type": "architectural",
        "explanation": "The same dysbiotic mucosal-damaged GI environment that depletes DAO creates conditions for Candida opportunistic overgrowth; Candida proteases damage intestinal mucosal cells reducing DAO production while Candida produces biogenic amines that add to DAO's histamine clearance burden, creating bidirectional reinforcement.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Parasitic Load",
        "type": "architectural",
        "explanation": "Parasitic infections cause mucosal damage through mechanical trauma and inflammatory infiltration, depleting DAO-producing crypt cells; both low DAO and elevated parasitic load are co-markers of the same GI mucosal compromise correlating with increased intestinal permeability.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Dysbiotic and Opportunistic Bacteria",
        "type": "architectural",
        "explanation": "Dysbiotic bacteria damage intestinal mucosal architecture and deplete DAO-producing crypt cells while simultaneously producing histamine and biogenic amines that overwhelm DAO clearance capacity; low DAO is both a consequence of dysbiotic bacterial mucosal damage and an amplifier of the histamine burden those bacteria produce.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Commensal Flora Balance",
        "type": "architectural",
        "explanation": "Commensal bacteria produce short-chain fatty acids that nourish colonocytes and support mucosal integrity including crypt cell function required for DAO production; depleted commensal flora impairs mucosal health and reduces DAO synthesis, making commensal balance a structural prerequisite for adequate DAO function and histamine clearance.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Calprotectin and Lactoferrin",
        "type": "correlational",
        "explanation": "Low DAO is specifically and consistently observed in IBD conditions (UC, Crohn's) that are characterized by elevated calprotectin and lactoferrin from active neutrophil infiltration; both DAO depletion and elevated calprotectin/lactoferrin are co-markers of active GI mucosal inflammation and autoimmune intestinal disease.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Beta-glucuronidase",
        "type": "architectural",
        "explanation": "Low DAO reflects dysbiotic mucosal damage caused by pathogenic bacteria (E. coli, Clostridium) that are the same species producing elevated beta-glucuronidase; both markers are co-indicators of the same dysbiotic bacterial ecology linked by shared pathogenic organisms that cause crypt damage while producing beta-glucuronidase.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Anti-gliadin IgA",
        "type": "causal",
        "explanation": "Serum DAO activity correlates inversely with intestinal permeability; DAO deficiency signals increased permeability allowing gliadin penetration through the mucosal barrier, triggering anti-gliadin IgA immune responses; histamine excess from DAO deficiency further drives Zonulin release that opens tight junctions and amplifies gliadin antigen exposure.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Secretory IgA \u2014 GI tract",
        "type": "architectural",
        "explanation": "DAO-producing crypt cells and lamina propria sIgA-producing plasma cells share the same mucosal architectural platform; crypt cell apoptosis causing DAO depletion also damages the lamina propria supporting sIgA production, while histamine excess from DAO deficiency drives sustained mucosal inflammation that exhausts mucosal IgA reserves.",
        "evidence_count": 2
    },
    {
        "from": "DAO (Diamine Oxidase)",
        "to": "Occult Blood",
        "type": "correlational",
        "explanation": "Low DAO is a consistent FDN marker of IBD conditions (UC, Crohn's) caused by crypt cell destruction; these same IBD conditions cause mucosal ulceration and structural vessel injury producing detectable occult blood; both DAO depletion and occult blood are co-occurring markers of severe IBD mucosal pathology characterized by crypt destruction and ulceration.",
        "evidence_count": 2
    },
    {
        "from": "Systemic Oxidative Stress Cascade",
        "to": "Hepatic Detoxification Impairment",
        "type": "causal",
        "explanation": "ROS from systemic oxidative stress directly damage hepatocytes via lipid peroxidation and protein oxidation, inactivating hepatic Phase I CYP450 enzymes required for xenobiotic detoxification; lipid peroxidation specifically damages hepatocyte mitochondria and cell membranes, impairing bile production, detoxification, and the full range of hepatic metabolic functions.",
        "evidence_count": 2
    },
    {
        "from": "Systemic Oxidative Stress Cascade",
        "to": "Histamine-DAO Regulatory System",
        "type": "causal",
        "explanation": "Systemic ROS inactivate DAO enzyme (a copper-containing amine oxidase whose active site is oxidatively vulnerable) and damage DAO-producing intestinal mucosal crypt cells, shifting the histamine-DAO balance toward histamine excess; the systemic oxidative cascade impairs histamine clearance capacity while simultaneously increasing histamine production through oxidative immune activation.",
        "evidence_count": 2
    },
    {
        "from": "Systemic Oxidative Stress Cascade",
        "to": "Secretory IgA \u2014 SHP",
        "type": "causal",
        "explanation": "Systemic ROS damage mucosal B-cell and plasma cell function required for sIgA synthesis through oxidative modification of cellular machinery (protein carbonylation, DNA damage); ROS-driven adrenal oxidative stress also dysregulates cortisol-DHEA balance in ways that amplify cortisol-mediated immunosuppression of mucosal IgA-producing plasma cells.",
        "evidence_count": 2
    }
]

# 1 DISCARDED pair
new_discarded = [
    {
        "from": "Histamine \u2014 MBA",
        "to": "Occult Blood",
        "reason": "Histamine-driven vascular permeability and mast cell-mediated inflammation affect mucosal barrier function but do not specifically predict structural mucosal bleeding sufficient for occult blood detection; occult blood reflects structural vessel/mucosal integrity failure requiring distinct pathological processes beyond histamine intolerance. No independent evidence lines at Relevant confidence support a direct causal or co-structural relationship."
    }
]

# Pairs to remove from pending (all 36)
pairs_to_remove = set([
    ("Histamine \u2014 MBA", "Commensal Flora Balance"),
    ("Histamine \u2014 MBA", "Calprotectin and Lactoferrin"),
    ("Histamine \u2014 MBA", "Beta-glucuronidase"),
    ("Histamine \u2014 MBA", "Anti-gliadin IgA"),
    ("Histamine \u2014 MBA", "Secretory IgA \u2014 GI tract"),
    ("Histamine \u2014 MBA", "Occult Blood"),
    ("DAO (Diamine Oxidase)", "Systemic Oxidative Stress Cascade"),
    ("DAO (Diamine Oxidase)", "Hepatic Detoxification Impairment"),
    ("DAO (Diamine Oxidase)", "Histamine-DAO Regulatory System"),
    ("DAO (Diamine Oxidase)", "Secretory IgA \u2014 SHP"),
    ("DAO (Diamine Oxidase)", "HPA Axis Dysregulation Pattern"),
    ("DAO (Diamine Oxidase)", "Pregnenolone Steal and Steroidogenesis Disruption"),
    ("DAO (Diamine Oxidase)", "Cortisol \u2014 Diurnal Pattern"),
    ("DAO (Diamine Oxidase)", "DHEA-S"),
    ("DAO (Diamine Oxidase)", "Cortisol-to-DHEA Ratio"),
    ("DAO (Diamine Oxidase)", "Estradiol"),
    ("DAO (Diamine Oxidase)", "Progesterone"),
    ("DAO (Diamine Oxidase)", "Testosterone"),
    ("DAO (Diamine Oxidase)", "Melatonin"),
    ("DAO (Diamine Oxidase)", "Dysbiosis-Intestinal Permeability Feedback Loop"),
    ("DAO (Diamine Oxidase)", "Mucosal Immune Tolerance and sIgA Function"),
    ("DAO (Diamine Oxidase)", "Gut-Brain-HPA Bidirectional Axis"),
    ("DAO (Diamine Oxidase)", "Reactive Food Burden \u2014 MRT"),
    ("DAO (Diamine Oxidase)", "H. pylori"),
    ("DAO (Diamine Oxidase)", "Candida and Fungal Overgrowth"),
    ("DAO (Diamine Oxidase)", "Parasitic Load"),
    ("DAO (Diamine Oxidase)", "Dysbiotic and Opportunistic Bacteria"),
    ("DAO (Diamine Oxidase)", "Commensal Flora Balance"),
    ("DAO (Diamine Oxidase)", "Calprotectin and Lactoferrin"),
    ("DAO (Diamine Oxidase)", "Beta-glucuronidase"),
    ("DAO (Diamine Oxidase)", "Anti-gliadin IgA"),
    ("DAO (Diamine Oxidase)", "Secretory IgA \u2014 GI tract"),
    ("DAO (Diamine Oxidase)", "Occult Blood"),
    ("Systemic Oxidative Stress Cascade", "Hepatic Detoxification Impairment"),
    ("Systemic Oxidative Stress Cascade", "Histamine-DAO Regulatory System"),
    ("Systemic Oxidative Stress Cascade", "Secretory IgA \u2014 SHP"),
])

# Remove from pending
before = len(state['connections']['pending'])
state['connections']['pending'] = [
    p for p in state['connections']['pending']
    if (p['from'], p['to']) not in pairs_to_remove
]
after = len(state['connections']['pending'])
print(f"Removed from pending: {before - after} pairs (expected 36)")

# Add to validated
state['connections']['validated'].extend(new_validated)
print(f"Added to validated: {len(new_validated)} pairs")

# Add to discarded
state['connections']['discarded'].extend(new_discarded)
print(f"Added to discarded: {len(new_discarded)} pairs")

# Update last_updated
state['last_updated'] = '2026-03-24T19:00:00Z'

# Build session log entry
connections_validated_log = [f"{v['from']} -> {v['to']}" for v in new_validated]
connections_discarded_log = [f"{d['from']} -> {d['to']}" for d in new_discarded]

state['session_log'].append({
    "date": "2026-03-24T19:00:00Z",
    "phase_executed": "connection_validation",
    "variables_researched": [],
    "connections_validated": connections_validated_log,
    "connections_discarded": connections_discarded_log,
    "output_file": "session-outputs/2026-03-24-connection-validation-5.md"
})

# Write back
with open('state.json', 'w', encoding='utf-8') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)

print(f"\nFinal state:")
print(f"  Pending: {len(state['connections']['pending'])}")
print(f"  Validated: {len(state['connections']['validated'])}")
print(f"  Discarded: {len(state['connections']['discarded'])}")
print(f"  Session log entries: {len(state['session_log'])}")
print("state.json written successfully.")
