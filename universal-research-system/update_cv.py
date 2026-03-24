import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('universal-research-system/state.json', 'r', encoding='utf-8') as f:
    state = json.load(f)

new_validated = [
  {"from": "Urinary Bile Acids", "to": "Systemic Oxidative Stress Cascade", "type": "causal",
   "explanation": "Hepatic dysfunction (elevated UBAs) impairs Phase I/II detoxification, generating CYP450-derived ROS as recirculating bile acids and toxins undergo processing; impaired Phase II conjugation allows Phase I reactive intermediates to accumulate, feeding the systemic oxidative stress cascade.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Hepatic Detoxification Impairment", "type": "causal",
   "explanation": "Elevated UBAs are the direct urinary indicator of failed hepatic first-pass bile acid clearance — the marker and the dysfunction are the same hepatic failure event; bile acid recirculation compounds Phase I/II processing overwhelm, creating a feedback loop that deepens detoxification impairment.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Histamine-DAO Regulatory System", "type": "architectural",
   "explanation": "Poor bile flow (very low UBAs) eliminates bile acids' bacteriostatic function in the small intestine, enabling SIBO; SIBO bacteria simultaneously elevate histamine production (histamine-decarboxylase activity) while dysbiosis-driven mucosal crypt damage reduces DAO production, destabilizing both arms of the Histamine-DAO regulatory system.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Secretory IgA \u2014 SHP", "type": "architectural",
   "explanation": "Both elevated UBAs (systemic immune-complex and antigen load exceeding hepatic clearance) and sIgA SHP depletion (HPA-driven cortisol suppression of immune output) are co-consequences of the same chronic metabolic stress state; immune-complex load reflected in UBA elevation constitutes the physiological stressor driving HPA activation and downstream sIgA suppression.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "HPA Axis Dysregulation Pattern", "type": "causal",
   "explanation": "The liver is the primary site of cortisol inactivation; hepatic congestion (elevated UBAs) impairs cortisol metabolism and clearance, disrupting HPA negative feedback; simultaneously, the systemic toxic and antigen load reflected by elevated UBAs constitutes a chronic physiological stressor driving CRH/ACTH/cortisol axis dysregulation.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Pregnenolone Steal and Steroidogenesis Disruption", "type": "causal",
   "explanation": "Hepatic dysfunction (UBAs) impairs cholesterol/steroid hormone metabolism and clearance, disrupting substrate availability for steroidogenesis; the chronic toxic and antigen load signaled by elevated UBAs drives HPA demand that exceeds adrenal capacity, triggering pregnenolone steal away from DHEA and sex hormone pathways.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Cortisol \u2014 Diurnal Pattern", "type": "causal",
   "explanation": "Hepatic dysfunction (elevated UBAs) impairs cortisol inactivation, causing accumulation that disrupts HPA negative feedback and distorts the diurnal cortisol rhythm; the systemic inflammatory and toxic load from liver congestion constitutes a persistent physiological stressor directly dysregulating cortisol's pulsatile diurnal secretion pattern.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "DHEA-S", "type": "causal",
   "explanation": "Hepatic congestion (elevated UBAs) impairs DHEA sulfation and clearance while generating chronic inflammatory and toxic stress that shifts adrenal steroidogenesis toward cortisol at the expense of DHEA-S; liver dysfunction disrupts Phase II sulfotransferase activity required for DHEA-to-DHEA-S conversion.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Cortisol-to-DHEA Ratio", "type": "causal",
   "explanation": "Hepatic dysfunction (elevated UBAs) simultaneously impairs cortisol clearance (shifting ratio toward cortisol dominance) and suppresses DHEA-S through adrenal stress and impaired sulfotransferase activity, producing net catabolic C:D ratio dysregulation from both directions.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Estradiol", "type": "causal",
   "explanation": "The liver is the primary site for estrogen glucuronidation and excretion; hepatic dysfunction (elevated UBAs) impairs Phase II estrogen conjugation, reducing fecal estrogen excretion and allowing estradiol recirculation; poor bile flow (very low UBAs) further impairs bile-mediated fecal steroid elimination, compounding estradiol accumulation.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Progesterone", "type": "causal",
   "explanation": "Hepatic dysfunction (elevated UBAs) impairs progesterone metabolism and clearance; the chronic stress and inflammatory load from liver congestion drives HPA cortisol dominance which competitively suppresses progesterone production through shared steroidogenic precursor competition and negative feedback on the HPG axis.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Testosterone", "type": "causal",
   "explanation": "The liver produces SHBG which regulates free testosterone bioavailability; hepatic dysfunction (elevated UBAs) impairs SHBG production and testosterone metabolism; the chronic inflammatory and toxic stress from liver congestion drives adrenal cortisol dominance that suppresses gonadal testosterone production through HPG axis inhibition.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Melatonin", "type": "architectural",
   "explanation": "Bile acids modulate GI motility and secretory function through FXR/TGR5 receptors in the enteric nervous system; poor bile flow (very low UBAs) disrupts enterochromaffin cell function and GI mucosal integrity, impairing the GI EC cell melatonin output measured by the FDN SHP noon melatonin marker; both reflect the same GI mucosal and secretory dysfunction.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Dysbiosis-Intestinal Permeability Feedback Loop", "type": "causal",
   "explanation": "Very low UBAs eliminate bile acids' bacteriostatic antimicrobial function in the small intestine, directly enabling the bacterial overgrowth that initiates the Dysbiosis-IP Feedback Loop; the already-validated UBA-to-Zonulin causal connection confirms that bile flow disruption directly activates TJ disassembly, feeding the self-amplifying dysbiosis-permeability cycle.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Mucosal Immune Tolerance and sIgA Function", "type": "causal",
   "explanation": "Poor bile flow (very low UBAs) drives SIBO and dysbiosis which continuously challenges and exhausts GI sIgA reserves, eroding mucosal immune tolerance; elevated UBAs (hepatic immune-complex overload) reflect the systemic antigen burden that also depletes mucosal sIgA through sustained immunological demand beyond replenishment capacity.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Gut-Brain-HPA Bidirectional Axis", "type": "architectural",
   "explanation": "Bile acids have direct gut-brain signaling roles through FXR and TGR5 receptors in the enteric nervous system and portal circulation; UBA abnormalities reflect disrupted bile acid signaling that modulates gut-enteric-brain communication; the hepatic portal system sits at the anatomical intersection of gut-derived signals and systemic circulation, making liver function central to the gut-brain-HPA bidirectional axis.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Reactive Food Burden \u2014 MRT", "type": "causal",
   "explanation": "Poor bile flow (very low UBAs) impairs fat emulsification and lipid digestion, leaving partially digested food antigens available for immune sensitization; the SIBO enabled by poor bile flow drives intestinal permeability that allows food antigens to translocate and trigger the MRT-measurable mediator release responses underlying food reactivity burden.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "H. pylori", "type": "architectural",
   "explanation": "H. pylori-generated antigen and immune complex load contributes to hepatic congestion measured by elevated UBAs; H. pylori infection impairs gastric acid output and disrupts bile flow coordination, contributing to conditions producing very low UBAs; both share gastric and hepatic dysfunction as the structural connecting node.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Candida and Fungal Overgrowth", "type": "architectural",
   "explanation": "Bile acids have potent antifungal properties in the GI tract; poor bile flow (very low UBAs) eliminates this antifungal function, enabling candida and fungal overgrowth; both UBA abnormalities and fungal overgrowth reflect the same dysbiotic GI ecology where microbial control mechanisms are compromised.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Parasitic Load", "type": "architectural",
   "explanation": "Poor bile flow (very low UBAs) reduces bile acid-mediated antimicrobial and antiparasitic protection in the small intestine; conversely, heavy hepatobiliary parasitic infection directly impairs hepatic bile production and enterohepatic clearance, elevating UBAs; both share hepatobiliary dysfunction as the structural connecting node.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Dysbiotic and Opportunistic Bacteria", "type": "architectural",
   "explanation": "Bile acids are the primary antimicrobial agents in the small intestine; poor bile flow (very low UBAs) directly enables dysbiotic and opportunistic bacterial overgrowth by removing the bile-acid bacteriostatic barrier; conversely, dysbiotic bacteria generating antigen and immune complex load that congests the liver is a primary mechanism producing elevated UBAs.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Commensal Flora Balance", "type": "causal",
   "explanation": "Bile acids are critical regulators of commensal microbiome composition through FXR-mediated signaling and direct bacteriostatic effects; disrupted bile flow (UBA abnormalities in either direction) directly alters the bile acid concentration gradient that shapes commensal flora composition and density throughout the GI tract.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Calprotectin and Lactoferrin", "type": "architectural",
   "explanation": "Both very low UBAs and elevated calprotectin/lactoferrin are co-markers of IBD: IBD generates GI mucosal neutrophil inflammation producing calprotectin/lactoferrin while simultaneously impairing bile acid reabsorption in the terminal ileum producing very low UBAs; both share IBD-driven intestinal mucosal inflammation as the upstream structural element.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Beta-glucuronidase", "type": "architectural",
   "explanation": "Hepatic Phase II glucuronide conjugation (impaired when UBAs are elevated) and beta-glucuronidase (which cleaves glucuronide conjugates to recirculate estrogens and toxins) are opposing arms of the same enterohepatic detoxification cycle; the dysbiotic bacteria producing beta-glucuronidase are the same organisms generating the antigen/immune complex load that elevates UBAs.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Anti-gliadin IgA", "type": "architectural",
   "explanation": "Poor bile flow (very low UBAs) enables SIBO-driven intestinal permeability that allows intact gliadin peptides to translocate and trigger anti-gliadin IgA mucosal immune responses; both anti-gliadin IgA and UBA abnormalities are downstream consequences of the same intestinal permeability and dysbiotic conditions.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Secretory IgA \u2014 GI tract", "type": "causal",
   "explanation": "The chronic antigen and immune complex burden reflected in elevated UBAs constitutes ongoing sIgA demand, exhausting GI mucosal sIgA reserves; poor bile flow (very low UBAs) drives SIBO and dysbiosis that continuously challenges and progressively depletes GI sIgA through sustained secretory demand beyond replenishment capacity.",
   "evidence_count": 2},
  {"from": "Urinary Bile Acids", "to": "Occult Blood", "type": "causal",
   "explanation": "Very low UBAs in IBD/Crohn's context indicate impaired bile flow from intestinal mucosal disease that simultaneously causes mucosal erosion and microhemorrhage detected as occult blood; poor bile flow enabling SIBO produces mucosal damage from dysbiosis-driven inflammation; elevated UBAs from systemic toxin load can also indicate hepatic-biliary pathology associated with upper GI hemorrhagic events.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "Zonulin", "type": "causal",
   "explanation": "Systemic oxidative stress (8-OHdG) directly damages tight junction proteins — ROS degrade occludin, claudins, and ZO proteins constituting the TJ complex, increasing intestinal permeability; Zonulin reflects the TJ disassembly state triggered by this oxidative epithelial damage, making 8-OHdG elevation a direct causal upstream driver of Zonulin-mediated permeability.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "Histamine \u2014 MBA", "type": "causal",
   "explanation": "Oxidative stress (8-OHdG) directly activates mast cell degranulation through ROS-triggered mast cell signaling pathways, releasing preformed histamine stores; the systemic oxidative and inflammatory conditions generating 8-OHdG elevation also stimulate histamine-producing immune cells and dysbiotic bacteria to increase histamine production.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "DAO (Diamine Oxidase)", "type": "causal",
   "explanation": "Oxidative stress (8-OHdG) damages intestinal epithelial cells including the crypt cells exclusively responsible for DAO production; the oxidative and inflammatory conditions that generate elevated 8-OHdG also impair mucosal architecture and crypt cell differentiation, reducing DAO output capacity and histamine degradation.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "Systemic Oxidative Stress Cascade", "type": "architectural",
   "explanation": "8-OHdG is the principal urinary biomarker of oxidative DNA damage and directly measures the magnitude of the Systemic Oxidative Stress Cascade; the same ROS-generating mechanisms driving the cascade (pathogen load, mitochondrial dysfunction, CYP450 processing) produce the guanine oxidation that generates 8-OHdG, making this an architectural co-measurement relationship.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "Hepatic Detoxification Impairment", "type": "causal",
   "explanation": "Oxidative stress (8-OHdG) damages hepatic mitochondria and Phase I/II enzyme systems, impairing detoxification capacity; conversely, hepatic detoxification impairment generates Phase I CYP450-derived ROS that further elevates 8-OHdG, creating a bidirectional causal relationship where each dysfunction amplifies the other.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "Histamine-DAO Regulatory System", "type": "causal",
   "explanation": "Oxidative stress (8-OHdG) simultaneously disrupts both arms of the Histamine-DAO regulatory balance: ROS activates mast cell degranulation elevating histamine production while oxidative damage to intestinal crypt cells reduces DAO output and histamine degradation, creating a double-hit that destabilizes the regulatory equilibrium from both directions.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "Secretory IgA \u2014 SHP", "type": "causal",
   "explanation": "Oxidative stress (8-OHdG) impairs B-lymphocyte and plasma cell function through ROS-mediated DNA and mitochondrial damage, directly reducing sIgA production capacity; the chronic inflammatory state generating 8-OHdG elevation also drives HPA cortisol dominance which dose-dependently suppresses sIgA secretion as measured in the SHP panel.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "HPA Axis Dysregulation Pattern", "type": "causal",
   "explanation": "Systemic oxidative stress (8-OHdG) constitutes a chronic physiological stressor activating HPA CRH/ACTH/cortisol signaling; ROS directly damages adrenal steroidogenic cells and mitochondria impairing cortisol production capacity while simultaneously triggering HPA stress response, producing a pattern of HPA dysregulation with impaired output capacity.",
   "evidence_count": 2},
  {"from": "8-OHdG", "to": "Pregnenolone Steal and Steroidogenesis Disruption", "type": "causal",
   "explanation": "Oxidative stress (8-OHdG) damages adrenal steroidogenic enzymes and mitochondria (steroidogenesis is mitochondria-dependent), directly impairing pregnenolone synthesis and the downstream steroidogenic cascade; the chronic HPA stress activation from oxidative burden also drives pregnenolone steal away from DHEA and sex hormone pathways toward cortisol production.",
   "evidence_count": 2},
]

# Build set of pairs to move
pairs_to_remove = set((c["from"], c["to"]) for c in new_validated)

# Verify all pairs exist in pending
pending_set = set((p["from"], p["to"]) for p in state["connections"]["pending"])
missing = [(f, t) for f, t in pairs_to_remove if (f, t) not in pending_set]
if missing:
    print("WARNING - not found in pending:", missing)

# Move pairs
orig_pending = len(state["connections"]["pending"])
state["connections"]["pending"] = [p for p in state["connections"]["pending"] if (p["from"], p["to"]) not in pairs_to_remove]
removed = orig_pending - len(state["connections"]["pending"])

state["connections"]["validated"].extend(new_validated)

# Update state
state["last_updated"] = "2026-03-24T12:00:00Z"
state["session_log"].append({
    "date": "2026-03-24T12:00:00Z",
    "phase_executed": "connection_validation",
    "variables_researched": [],
    "connections_validated": [f"{c['from']} \u2192 {c['to']}" for c in new_validated],
    "output_file": "session-outputs/2026-03-24-connection-validation-2.md"
})

print(f"Removed from pending: {removed} (expected 36)")
print(f"New pending count: {len(state['connections']['pending'])}")
print(f"New validated count: {len(state['connections']['validated'])}")

with open('universal-research-system/state.json', 'w', encoding='utf-8') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)

print("state.json written successfully")
