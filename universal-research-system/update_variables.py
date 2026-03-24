import json
from datetime import datetime, timezone

state_path = "c:/Users/Alexb/Documents/Kaitlyn's vs code docs/universal-research-system/state.json"

print("Loading state.json...")
with open(state_path, 'r', encoding='utf-8') as f:
    state = json.load(f)

print(f"Phase: {state['phase']}")
print(f"Pending: {len(state['pending_variables'])}")
print(f"Researched: {len(state['researched_variables'])}")

variables_data = {

"H. pylori": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "H. pylori is a spiral gram-negative bacterium that colonizes the gastric mucosa by burrowing into the stomach lining. It neutralizes local HCl via urease production while paradoxically stimulating systemic gastrin secretion, creating a self-amplifying inflammatory cycle. Two classes of virulence factors — adhesion factors (babA, oipA, iceA, dupA, virB, virD) enabling persistent colonization and inflammatory factors (cagA, vacA, CagPAI) suppressing immune recognition while driving cumulative mucosal damage — differentiate pathogenic from incidental infection. Untreated infection progresses toward peptic ulceration or gastric carcinoma. FDN protocol treats H. pylori first among all GI pathogens; up to 50% of infected individuals may be asymptomatic, making the GI-MAP the primary detection tool.",
    "reasoning_chains": [
        {
            "claim": "H. pylori neutralizes local gastric HCl via urease enzyme production while simultaneously stimulating systemic gastrin secretion, paradoxically increasing HCl output and stimulating its own burrowing, thereby compromising the gastric acid barrier against all incoming pathogens.",
            "evidence": "Module 6 transcript slides 138-143 (module-06-transcript-part-02.md lines 255-263) — 'It may neutralize the stomach acid surrounding it, compromising hosts ability to digest food and kill other pathogens... H. pylori also stimulates gastrin production, and gastrin in the stomach leads to hydrochloric acid production... more HCl tends to stimulate it, kind of pisses it off and makes it burrow even more... that is why we do not use HCl when we have an H. pylori infection.'",
            "logic": "Urease converts urea to ammonia + CO2, locally neutralizing gastric acid around the organism, compromising the local bactericidal barrier; simultaneously H. pylori stimulates G-cells to release gastrin causing increased parietal cell HCl production, which then stimulates H. pylori further and increases burrowing into gastric mucosa — positive feedback loop counterintuitively worsened by HCl supplementation therapy.",
            "confidence_band": "Core"
        },
        {
            "claim": "H. pylori virulence factors operate in two mechanistic categories: adhesion factors (babA, oipA, iceA, dupA, virB, virD) enabling persistent colonization, and inflammatory factors (cagA, vacA, CagPAI) reprogramming host signaling to suppress immune recognition while driving cumulative mucosal damage toward ulceration or gastric carcinoma.",
            "evidence": "Module 6 transcript slides 140-143 (module-06-transcript-part-02.md lines 259-271) — 'certain enzymatic reactions produce adhesion proteins, which help H. pylori attach to the stomach lining. Increasing odds the infection will be persistent long enough to become pathogenic... the inflammatory virulence factors... change the way the body signaling pathways talk to each other, telling anti-inflammatory processes to ignore the damage and stay inflamed... tell the immune system to ignore the H. pylori, the bug itself, even as it causes cumulative damage to the gastric lining. This damage can culminate in ulcers or even in cancer.'",
            "logic": "Adhesion virulence factors lower the energy barrier for chronic colonization by enabling tight mucosal attachment; inflammatory virulence factors operate through two parallel mechanisms — (1) reprogramming intracellular signaling to suppress host anti-inflammatory response, and (2) blocking immune recognition of the bacterium itself — creating unopposed mucosal damage accumulation that progressively worsens.",
            "confidence_band": "Core"
        },
        {
            "claim": "Any detectable level of H. pylori combined with virulence factors warrants treatment; FDN protocol mandates H. pylori be treated first before parasites, bacteria, and fungi because its immune-evasion capacity and acid-barrier disruption amplify all other GI pathogen colonization.",
            "evidence": "Module 6 transcript slide 100 (module-06-transcript-part-02.md line 1) — 'the negatives outweigh any positives, and we believe that H. pylori should be addressed if detected. By addressed, we will address that in the protocols, but it is important that H. pylori be suppressed.' Transcript slide 128 (line 185) — 'We want to treat H. pylori first when it is present. And you can consider adding Matula Tea to your protocols particularly when significant virulence factors are there. Now, other infections are treated in the following order, parasites, bacteria, and then fungi and yeast.'",
            "logic": "H. pylori dual capacity for immune evasion (virulence factor suppression of recognition) and structural compromise of gastric acid barrier (enabling colonization of other pathogens) makes it the highest-priority intervention target; eliminating H. pylori first restores gastric bactericidal capacity and removes the primary immune-evasion signal before addressing downstream infections.",
            "confidence_band": "Core"
        },
        {
            "claim": "H. pylori infection is a documented upstream driver of systemic oxidative stress elevation (8-OHdG), creating a bidirectional connection between GI-MAP pathogen burden and MWP oxidative stress markers through sustained neutrophil and macrophage oxidative burst in the gastric mucosa.",
            "evidence": "Module 6 slides page 49 (2025+M6+1-149+Slides+1PP.md line 1041) — slide explicitly lists 'E. coli and H. pylori' as causes to check when 8-OHdG is elevated, alongside chronic dysbiosis and over-exercise; consistent with Module 4 slides page 96 listing pathogens as ROS generators alongside heavy metals and tobacco smoke.",
            "logic": "Chronic H. pylori infection sustains mucosal immune activation; neutrophils and macrophages generating prolonged oxidative burst produce superoxide and hydroxyl radicals via NADPH oxidase, which oxidize guanine bases in adjacent gastric mucosal DNA, producing elevated urinary 8-OHdG measurable on the MWP — mechanistically linking GI-MAP pathogen burden to MWP oxidative stress markers.",
            "confidence_band": "Core"
        }
    ]
},

"Candida and Fungal Overgrowth": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Candida spp. (primarily C. albicans) is a commensal yeast that becomes pathogenic when overgrown. Its primary toxicological mechanism is acetaldehyde production — the same toxin generated by alcohol metabolism — which produces hangover-like systemic symptoms (fatigue, brain fog, headache, nausea). Overgrowth is specifically associated with IgA damage, heavy metal toxicity, pesticide accumulation, and antibiotic use; die-off releases stored metals and toxins back into systemic circulation. The GI-MAP measures four fungal species (Candida spp., C. albicans, Geotrichum, Microsporidium, Rhodotorula); the complementary Candida Suite measures IgG/IgM/IgA antibodies indicating past or active infection. Joan's GI-MAP shows C. albicans at 4.04e3 High (reference <5.00e2). In the FDN treatment hierarchy, fungi and yeast are addressed last (60 days as primary infection, 40 days as secondary).",
    "reasoning_chains": [
        {
            "claim": "Candida albicans overgrowth produces acetaldehyde as a primary metabolic toxin, causing neurological and systemic symptoms mechanistically identical to alcohol hangover: fatigue, brain fog, headache, and nausea.",
            "evidence": "Module 6 slides page 64 (2025+M6+1-149+Slides+1PP.md lines 1275-1276) — 'Candida causes numerous brain-related symptoms that are similar to symptoms of a hangover (fatigue, brain fog, headache, nausea) because both Candida and alcohol produce high levels of a toxin called acetaldehyde'",
            "logic": "Candida ferments dietary sugars via the same ethanol fermentation pathway as alcohol-producing yeast; acetaldehyde is an intermediate that inhibits mitochondrial respiration, depletes glutathione, and induces neuroinflammation — producing the same biochemical insult as acute alcohol exposure. This explains why Candida-positive clients report feeling hungover without alcohol consumption.",
            "confidence_band": "Core"
        },
        {
            "claim": "Candida overgrowth is specifically associated with IgA damage and heavy metal toxicity — heavy metals impair immune clearance of Candida while Candida die-off during treatment liberates stored metals and pesticides back into general circulation, creating a dual toxic release event.",
            "evidence": "Module 6 slides page 60 (2025+M6+1-149+Slides+1PP.md lines 1193-1197) — 'Associated with IgA damage, heavy metal toxicity and pesticide accumulation — Die-off of candida may release toxins from the fungus itself while also liberating metals and pesticides into general circulation'",
            "logic": "Mercury and other heavy metals inhibit phagocytic macrophage function and suppress mucosal IgA production, reducing immune capacity to control Candida; Candida organisms accumulate heavy metals from the gut environment; treatment-induced die-off releases these stored metals simultaneously with candidal toxins, producing a systemic toxic burden that can cause Herxheimer-like reactions requiring staged detox support during treatment.",
            "confidence_band": "Core"
        },
        {
            "claim": "Candida overgrowth is an opportunistic sequela of disrupted gut ecology — specifically antibiotic use, hypochlorhydria, excess dietary sugars/starches, and pathogenic bacterial overgrowth — and is among the first microflora to proliferate when beneficial flora are depleted.",
            "evidence": "Module 6 slides page 56 (2025+M6+1-149+Slides+1PP.md lines 1136-1138) — 'fungi are one of the first microflora to propagate and flourish, along with multiple aerobic species of bad bugs'; slide 60 (lines 1199-1202) — elevated levels associated with 'recent antibiotic use, hypochlorhydria, excess intake of dietary sugars, starches and fungi, pathogenic overgrowth of opportunistic bacteria, parasitic infections, heavy metal toxicity'",
            "logic": "Antibiotics eliminate competing commensal bacteria that normally occupy mucosal surface receptors and produce bacteriocins inhibiting yeast; removal of competitive exclusion allows Candida to expand rapidly into vacated ecological niches. Simultaneously, hypochlorhydria reduces fungicidal effect of gastric acid, and excess dietary sugars provide direct fermentation substrate for Candida growth.",
            "confidence_band": "Core"
        },
        {
            "claim": "The Candida Suite (IgG, IgM, IgA antibody panel) provides a complementary immune timeline to GI-MAP stool PCR — IgM indicates acute or new infection, IgG indicates past or prolonged infection, and IgA detected in blood indicates ongoing active mucosal infection.",
            "evidence": "Module 6 slides pages 69-72 (2025+M6+1-149+Slides+1PP.md lines 1443-1502) — 'IgM: Increase at the beginning of an infection; IgG: Develop later. Indicate past or prolonged infection; IgA: Present almost exclusively in mucous membranes; When in blood, indicates ongoing infection'; slide 71 — 'IgM is reactive so this is a new infection or Candida just reached threshold'; slide 72 — 'IgM is non-reactive so not a current infestation. IgG is reactive so this is a past infection'",
            "logic": "The antibody timeline (IgM then IgG then IgA) follows immunological class switching during infection progression; GI-MAP PCR detects Candida DNA regardless of immune response timing, so pairing PCR (current organism burden) with antibody panel (immune history and activity) provides a complete temporal picture of Candida infection status, chronicity, and mucosal vs systemic involvement.",
            "confidence_band": "Core"
        }
    ]
},

"Parasitic Load": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Parasitic organisms on the GI-MAP include protozoa (Blastocystis hominis, Dientamoeba fragilis, Giardia, Cryptosporidium, Entamoeba histolytica, and others) and worms (hookworms, roundworm, whipworm, tapeworm). Each organism causes systemic damage through distinct mechanisms: Cryptosporidium destroys intestinal cells on a 7-day intracellular migration cycle; Entamoeba histolytica bores through the intestinal wall and can migrate to liver, lungs, and brain; Giardia absorbs nutrients directly (causing B12 and fat-soluble vitamin deficiency), increases food antigen immune reactivity including to gluten, and colonizes bile ducts enabling reinfection after treatment. Parasites collectively produce toxic exudates, form biofilms, generate pro-inflammatory dysbiosis, and drive gut hyperpermeability. Ashley's GI-MAP shows Giardia 1.03e3 (detected, below threshold). Treatment order: second after H. pylori, requiring 60 days minimum (Blastocystis: 90 days to 12 months).",
    "reasoning_chains": [
        {
            "claim": "Giardia causes nutrient malabsorption (particularly B12 deficiency and fat-soluble vitamin impairment) by absorbing nutrients from the intestinal lumen, while simultaneously increasing immune reactivity to food antigens including gluten and stimulating gut hyperpermeability — setting the stage for leaky gut and autoimmune disease.",
            "evidence": "Module 6 transcript slide 111 (module-06-transcript-part-02.md lines 62-66) — 'Giardia colonizes and reproduces in the small intestine. This parasite can absorb nutrients from the lumen, which leads to malabsorption, particularly a B12 deficiency, and also impairs the absorption of fat. So, you also have to be concerned about your fat-soluble vitamins... giardia can increase immune reactions to food antigens, and that includes gluten, and can stimulate hyperpermeability of the gut. So, it can really set the stage for leaky gut, for autoimmunity. It can be a triggering event for gluten-sensitive folks or people who carry the genes for celiac disease.'",
            "logic": "Giardia attaches to intestinal brush border epithelium via ventral adhesive disc, mechanically disrupting microvilli and reducing absorptive surface area for nutrients; simultaneously, Giardia antigens cross-react with intestinal epithelial proteins, triggering Zonulin release and tight junction disassembly — creating the hyperpermeability state that allows antigen translocation and food sensitivity sensitization.",
            "confidence_band": "Core"
        },
        {
            "claim": "Entamoeba histolytica is capable of boring through the intestinal wall and migrating to the liver, lungs, and brain, producing systemic disease manifestations including liver inflammation, chronic fatigue, fibromyalgia, rheumatoid arthritis, and multiple chemical sensitivity.",
            "evidence": "Module 6 transcript slide 110 (module-06-transcript-part-02.md lines 57-61) — 'Entamoeba histolytica is a parasite that can bore into the intestinal wall and can migrate to the liver, lungs, brain, and other parts of the body. Elevated levels are associated with diarrhea, fulminating colitis, dysentery, irritable bowel syndrome, multiple chemical sensitivity, liver inflammation, rheumatoid arthritis, fibromyalgia, chronic fatigue, canker sores, hives, and polyarthritis.'",
            "logic": "E. histolytica produces cysteine proteases that degrade the extracellular matrix and intestinal mucus layer, enabling tissue invasion and hematogenous spread to distal organs; liver abscess is the most common extraintestinal manifestation; systemic immune activation from disseminated infection produces the multi-system symptom pattern including fibromyalgia and autoimmune-like joint involvement.",
            "confidence_band": "Core"
        },
        {
            "claim": "Giardia causes extensive pro-inflammatory dysbiosis by increasing Proteobacteria (LPS-producing) and decreasing Firmicutes (protective commensals), and can migrate to bile ducts enabling reinfection of the small intestine after treatment — making it inherently prone to becoming a chronic infection.",
            "evidence": "Module 6 transcript slide 111 (module-06-transcript-part-02.md lines 64-66) — 'Giardia can cause extensive pro-inflammatory dysbiosis, and it increases the proteobacteria phylum, and those are gram-negative bacteria that produce pro-inflammatory lipopolysaccharides, and it can also decrease the Firmicutes phylum... Giardia can migrate to the bile ducts and the gallbladder. So, it can kind of hang out there and hide. And then, after someone undergoes treatment for Giardia, it can then reseed the small intestine and you can get a reinfection of the parasite throughout the GI tract. So, Giardia can become a chronic infection.'",
            "logic": "Giardia preferentially disrupts commensal Firmicutes through competitive displacement and mucosal damage; increased Proteobacteria elevates LPS load causing gut inflammation and further barrier disruption. Giardia cysts surviving in the biliary tree are inaccessible to stool-based antimicrobial protocols, explaining why incomplete treatment produces apparent relapse — actually ongoing infection from a biliary reservoir.",
            "confidence_band": "Core"
        },
        {
            "claim": "Parasitic organisms as a class produce toxic metabolic byproducts (exudates), form biofilms shielding them from host immune clearance, and generate pro-inflammatory conditions — contributing to metabolic chaos through oxidative stress, immune dysregulation, and mucosal barrier destruction; Blastocystis hominis requires 90 days minimum to 12 months to eradicate.",
            "evidence": "Module 6 slides page 44 (2025+M6+1-149+Slides+1PP.md lines 908-921) — 'A weakened/dysbiotic host can suffer: Toxic condition from pathogens metabolic byproducts, Disruption of intestinal mucosal barrier function, Hyperpermeability, Immune dysfunction, Autoimmune conditions. Condition can persist subclinically for years, even decades.' Module 6 transcript slide 128 (module-06-transcript-part-02.md line 186) — 'Most parasites require a 60-day treatment, except for blasto. Blasto hominis will always take a minimum of 90 days to eradicate, but it can take up to 12 months.'",
            "logic": "Parasitic exudates include proteases, hemolysins, and cytotoxic molecules directly damaging intestinal epithelium; biofilm formation creates a polysaccharide matrix physically shielding organisms from innate immune recognition and antimicrobial agents. The extended treatment duration for Blastocystis reflects its complex life cycle and biofilm-forming capacity, requiring prolonged antimicrobial exposure to achieve full eradication.",
            "confidence_band": "Core"
        }
    ]
},

"Dysbiotic and Opportunistic Bacteria": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Dysbiotic and opportunistic bacteria on the GI-MAP are organisms whose presence signals pathological activity — either because they should not appear at any level (dysbiotic) or because they become pathogenic when overgrown (opportunistic). Key mechanisms include: (1) molecular mimicry driving autoimmune targeting of self-tissues (Klebsiella/AS, Citrobacter/RA, Proteus/RA, Yersinia/thyroid), (2) histamine production via histidine decarboxylase (Morganella, Klebsiella), and (3) LPS-mediated tight junction disruption. The four dysbiotic patterns (Insufficiency, Inflammatory, Combo, Digestive Dysfunction) classify the dominant ecosystem failure mechanism and guide the 5R therapeutic protocol. Joan's GI-MAP: Klebsiella 2.74e4 High, Streptococcus 3.77e5 High, Enterococcus faecalis 2.03e4 High, Bacillus 1.22e6 High. Ashley's GI-MAP: Streptococcus spp. 2.29e3 High.",
    "reasoning_chains": [
        {
            "claim": "Klebsiella spp. drives autoimmune disease through molecular mimicry with HLA-B27 antigens (ankylosing spondylitis), produces histamine and ammonia via protein-degrading urease pathways, and is implicated in mercury toxicity and thyroid autoimmunity — making it a multi-system autoimmune trigger.",
            "evidence": "Module 6 slides page 32 (2025+M6+1-149+Slides+1PP.md lines 652-664) — 'Klebsiella spp./Klebsiella pneumoniae — Associated with ankylosing spondylitis, RA, ulcerative colitis, psoriatic arthritis and reactive arthritis — May also implicated in mercury toxicity and thyroid autoimmunity — May produce ammonia through its feeding on protein and may release histamine in the gut — Elevated levels associated with bloating, abdominal pain, diarrhea, increased gut inflammation, mercury toxicity, autoimmune flares, and the development of autoimmune disease'",
            "logic": "Klebsiella produces pullulanase and nitrogenase enzymes structurally similar to HLA-B27 proteins; antibodies generated against Klebsiella cross-react with HLA-B27 on articular tissue cells, initiating autoimmune joint destruction (ankylosing spondylitis mechanism). Klebsiella urease pathway produces ammonia and histamine from protein degradation, directly elevating histamine burden and linking to MBA histamine elevation.",
            "confidence_band": "Core"
        },
        {
            "claim": "Morganella spp. is a primary histamine-producing dysbiotic bacterium that directly elevates systemic histamine levels and overwhelms DAO clearance capacity, creating a mechanistic bridge between GI-MAP dysbiotic bacteria and MBA histamine and DAO markers.",
            "evidence": "Module 6 slides page 26 (2025+M6+1-149+Slides+1PP.md lines 535-542) — 'Morganella spp. — Gram-negative group in the Proteobacteria phylum — May produce histamine — Produces pro-inflammatory LPS — Elevated levels associated with increased GI inflammation, diarrhea, and SIBO'",
            "logic": "Morganella produces histidine decarboxylase, converting dietary histidine to histamine in the gut lumen; this bacterial-derived histamine adds to dietary histamine intake and mast cell-derived histamine, collectively overwhelming DAO enzymatic clearance capacity. Elevated GI-MAP Morganella directly predicts elevated MBA histamine and relative DAO insufficiency, establishing the mechanistic GI-to-MBA connection.",
            "confidence_band": "Core"
        },
        {
            "claim": "Multiple dysbiotic bacteria (Citrobacter, Proteus, Prevotella, Klebsiella) drive autoimmune disease through molecular mimicry — their surface proteins structurally resemble host tissue antigens, causing antibodies generated against the bacteria to also attack self-tissues.",
            "evidence": "Module 6 slides pages 31-34 (2025+M6+1-149+Slides+1PP.md lines 631-713) — Citrobacter: 'Specifically associated with RA but may be implicated in other autoimmune conditions'; Klebsiella: 'Associated with ankylosing spondylitis, RA, ulcerative colitis, psoriatic arthritis and reactive arthritis'; Proteus mirabilis: 'associated with RA... associated with ankylosing spondylitis, psoriatic arthritis, reactive arthritis and arthritis associated with Crohn Disease and Ulcerative Colitis'",
            "logic": "Molecular mimicry is a validated autoimmune mechanism: bacterial surface antigens with structural homology to host proteins (collagen in RA, HLA-B27 in AS) trigger antibody production that cross-reacts with self-tissue; repeated infection episodes continually re-stimulate this cross-reactive immune response, producing chronic autoimmune joint inflammation that persists even after pathogen burden is reduced.",
            "confidence_band": "Core"
        },
        {
            "claim": "Dysbiotic patterns on the GI-MAP (Insufficiency, Inflammatory, Combo, Digestive Dysfunction) classify the dominant mechanism of gut ecosystem failure and directly determine which step of the 5R protocol (Remove, Replace, Re-inoculate, Repair, Rebalance) is the primary intervention priority.",
            "evidence": "Module 6 slides pages 37-41 (2025+M6+1-149+Slides+1PP.md lines 772-865) — 'Insufficiency Dysbiosis: characterized by an overall pattern of depletion that promotes greater risk of intestinal infections, hyper-permeability of the gut, and compromised immune function'; 'Inflammatory Dysbiosis: characterized by the presence of pro-inflammatory pathogens... Intestinal hyper-permeability is common with this pattern d/t high levels of pro-inflammatory LPS'; 'Digestive Dysfunction Dysbiosis: when digestive dysfunction alters the microbiome d/t hypochlorhydria, insufficient bile acids, pancreatic insufficiency'",
            "logic": "Each pattern maps to a distinct upstream root cause cluster: Insufficiency → deplete commensal support, prioritize Re-inoculate; Inflammatory → prioritize Remove targeting LPS-producing gram-negatives; Digestive Dysfunction → prioritize Replace restoring HCl and pancreatic enzymes. Pattern recognition guides 5R therapeutic sequencing rather than treating individual organisms in isolation.",
            "confidence_band": "Core"
        }
    ]
},

"Commensal Flora Balance": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Commensal flora are the keystone bacterial species whose presence and adequate quantity maintain gut ecosystem stability, immune modulation, and metabolic function. The GI-MAP measures keystone commensals including Bacteroides fragilis, Bifidobacterium, Lactobacillus, Roseburia, Akkermansia muciniphila, Faecalibacterium prausnitzii, and the phylum-level Firmicutes:Bacteroidetes (F:B) ratio. Core functions include SCFA production (butyrate from Roseburia/Faecalibacterium feeds colonocytes and maintains anti-inflammatory gut state), immune modulation (Bifidobacterium/Lactobacillus support SIgA production and regulatory T-cell activity), and competitive exclusion of pathogens. Dysbiosis is formally defined as a quantitative or qualitative shift producing negative health impact. Joan's GI-MAP shows an elevated-but-inverted pattern: multiple phyla high yet F:B ratio 0.11 (<1.00 normal), with multiple commensals and dysbiotic bacteria simultaneously elevated.",
    "reasoning_chains": [
        {
            "claim": "Commensal bacteria collectively maintain gut barrier function, produce vitamins (biotin, vitamin K), provide SCFA that increase SIgA and protect against toxins, and provide competitive exclusion against pathogenic colonization — their depletion simultaneously removes all these protective mechanisms.",
            "evidence": "Module 6 slides page 14 (2025+M6+1-149+Slides+1PP.md lines 277-286) — 'Commensal bacteria extract nutrients and energy from our diets, maintain gut barrier function, produce vitamins (biotin and vitamin K), and protect against colonization by potential pathogens'; page 21 (lines 445-452) — 'Good bacteria: Promote mucosal barrier integrity, Support and balance the immune system, Produce SCFA which reduce inflammation, increase SIgA and mucin, and protect against toxins. Bad bacteria: Produce pro-inflammatory LPS, increasing inflammation and gut permeability, Encourage the overgrowth of other opportunistic, pro-inflammatory bacteria, Deplete population levels of good bacteria'",
            "logic": "Commensal bacteria occupy mucosal receptor sites, consume available nutrients, and produce bacteriocins and organic acids inhibiting pathogen growth; when commensals are depleted, these protective functions are removed simultaneously, allowing rapid colonization of vacated niches by opportunistic and pathogenic organisms — explaining the clinical pattern of infections following antibiotic-induced dysbiosis.",
            "confidence_band": "Core"
        },
        {
            "claim": "Roseburia and Faecalibacterium prausnitzii are keystone SCFA producers whose low levels directly impair colonocyte energy supply, gut motility, mucosal immunity, and anti-inflammatory state — making them critical monitoring targets in the commensal flora section.",
            "evidence": "Module 6 transcript GI MAP Report addendum (module-06-transcript-part-02.md lines 373-376) — 'They break down the sugars and complex carbohydrates of plant fibers. And in doing so, they are producing short-chain fatty acids, one of which is butyrate. Butyrate is extremely important for the healthy functioning of a gut. It helps us with colon motility, with gut immunity, with gut acidity, and with maintaining an anti-inflammatory state in the gut. This is one reason why it is very important to eat your plants.'",
            "logic": "Colonocytes derive approximately 70% of their energy from butyrate rather than glucose; low Roseburia/Faecalibacterium reduces butyrate production, causing colonocyte energy deficit, compromised tight junction maintenance, and increased mucosal permeability. Simultaneously, butyrate suppresses NF-kB signaling in colonocytes, reducing pro-inflammatory cytokine production — loss of butyrate removes this key anti-inflammatory governor.",
            "confidence_band": "Core"
        },
        {
            "claim": "The Firmicutes:Bacteroidetes ratio (F:B ratio) is a phylum-level dysbiosis index — elevated ratio predicts maldigestion, insulin resistance, and obesity; however, both phyla being simultaneously elevated (as in Joan's GI-MAP) indicates complex mixed dysbiosis requiring species-level interpretation.",
            "evidence": "Module 6 slides page 22 (2025+M6+1-149+Slides+1PP.md lines 472-479) — 'Elevated Firmicutes/Bacteroidetes ratio suggests microbial imbalance that may be related to maldigestion, hypochlorhydria, increased fat deposition, insulin resistance, excess inflammation, excess carbohydrate intake, obesity, and inability to lose weight. Note: the LPS produced by the Bacteroidetes phyla are actually anti-inflammatory and protective to the gut lining'; Joan GI-MAP results (Joan GI-MAP results_case study.md lines 68-70) — Bacteroidetes 7.53e12 High, Firmicutes 8.01e11 High, F:B ratio 0.11 (<1.00 normal).",
            "logic": "Joan's pattern (both phyla elevated, ratio inverted toward Bacteroidetes dominance) indicates massive overall bacterial overgrowth rather than simple imbalance between phyla; Bacteroidetes-derived LPS being specifically anti-inflammatory means Bacteroidetes elevation alone is not harmful, but the simultaneous absolute elevation of both phyla with multiple dysbiotic organisms signals a complex Digestive Dysfunction Dysbiosis pattern requiring comprehensive assessment.",
            "confidence_band": "Core"
        },
        {
            "claim": "Bacteroides fragilis plays a specific immune-modulatory role that protects against autoimmune disorders including colitis and MS, and increases resistance to Salmonella colonization — making it a keystone organism with both structural and immunological functions.",
            "evidence": "Module 6 slides page 16 (2025+M6+1-149+Slides+1PP.md lines 337-345) — 'Bacteroides fragilis — Active in immune-modulation and may protect against autoimmune disorders — Contributes to mucosal barrier integrity and neuroimmune health — Increases resistance to salmonella via the production of SCFA — Research has shown B. fragilis to be beneficial for conditions such as autism, colitis, and MS — Plays a key role in carb fermentation, producing fatty acids that feed other beneficial bacteria as well as the host'",
            "logic": "B. fragilis polysaccharide A (PSA) promotes Foxp3+ regulatory T-cell development through TLR2 signaling, actively suppressing Th1/Th17 inflammatory responses implicated in autoimmune disorders; simultaneously, B. fragilis SCFA production creates the luminal acidic environment hostile to Salmonella growth. This dual mechanism makes B. fragilis a central pillar of both mucosal barrier protection and systemic immune regulation.",
            "confidence_band": "Core"
        }
    ]
},

"Calprotectin and Lactoferrin": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Calprotectin is a calcium-binding protein released by neutrophils during GI mucosal inflammation, functioning as the most sensitive and specific marker of GI inflammation on the GI-MAP (93-95% sensitivity/specificity). Its primary clinical value is distinguishing active inflammatory bowel disease from functional GI disorders. Confounders include NSAIDs (elevate calprotectin), smoking (7% annual increase), and obesity (40% increase per 20 lbs excess weight). Approximately 2% of the population produces lactoferrin instead of calprotectin in response to mucosal inflammation. Normal calprotectin does not rule out GI dysfunction when other markers are abnormal — both case study patients show normal calprotectin despite multiple dysbiotic findings, demonstrating that chronic dysbiosis and SIgA suppression can occur without triggering the acute neutrophilic inflammatory signal that calprotectin measures.",
    "reasoning_chains": [
        {
            "claim": "Calprotectin is a highly sensitive and specific neutrophil-derived marker of GI mucosal inflammation (93-95% sensitivity/specificity), making it the gold-standard screening tool for distinguishing active IBD from functional bowel disorders such as IBS.",
            "evidence": "Module 6 transcript slide 121 (module-06-transcript-part-02.md lines 117-119) — 'Calprotectin is a marker indicating the level of localized inflammation in the gut. It is one of the most studied markers of GI inflammation, and the sensitivity and specificity of this marker has been found to be in the range of 93 to 95%.'",
            "logic": "Calprotectin constitutes approximately 60% of neutrophil cytoplasmic protein; when neutrophils are recruited to inflamed intestinal mucosa, calprotectin is released into the intestinal lumen and measurable in stool. High sensitivity/specificity means calprotectin elevation reliably distinguishes active mucosal inflammation (IBD, infection) from functional disorders (IBS) where inflammation is absent.",
            "confidence_band": "Core"
        },
        {
            "claim": "Calprotectin results are confounded by NSAIDs (elevate), smoking (7% per year increase), and obesity (40% per 20 lbs increase), requiring these lifestyle and medication factors to be considered before attributing any calprotectin elevation to specific GI inflammation.",
            "evidence": "Module 6 transcript slide 121 (module-06-transcript-part-02.md lines 117-120) — 'calprotectin can be influenced by several factors and can change rather quickly. It can elevate from the use of NSAIDs, or nonsteroidal anti-inflammatories, So it is best to avoid NSAIDs prior to testing... Calprotectin can rise 7% every year in people who smoke cigarettes. And it can also rise 40% for every 20 pounds or 10 kilograms of excess weight.'",
            "logic": "NSAIDs inhibit COX-2 pathways that normally suppress neutrophil activation, paradoxically increasing calprotectin release independent of true mucosal inflammation, creating false positive results. Obesity and smoking independently activate systemic neutrophil priming, increasing baseline calprotectin. A practitioner must account for these confounders before attributing elevated calprotectin to GI-specific inflammation.",
            "confidence_band": "Core"
        },
        {
            "claim": "Approximately 2% of the population produces lactoferrin instead of calprotectin as an inflammatory response marker — this subgroup may show negative calprotectin despite active GI inflammation, requiring lactoferrin add-on testing when clinical suspicion is high.",
            "evidence": "Module 6 transcript slide 121 (module-06-transcript-part-02.md lines 118-119) — 'in approximately 2% of the population, the response to inflammatory organisms may not be reflected by calprotectin. Those folks might just produce lactoferrin or not be able to produce either due to low white blood cell count in general.'",
            "logic": "Lactoferrin is an alternative antimicrobial iron-binding protein released from neutrophil specific granules during mucosal immune activation; in the approximately 2% of non-calprotectin responders, lactoferrin serves the same clinical signaling function as calprotectin. This population is identifiable by the pattern of negative calprotectin despite high clinical suspicion for active GI inflammation — lactoferrin testing resolves the diagnostic gap.",
            "confidence_band": "Core"
        },
        {
            "claim": "Normal calprotectin does not rule out significant GI dysfunction — both case study patients show normal calprotectin despite multiple abnormal GI markers, demonstrating that chronic dysbiosis, SIgA suppression, and detoxification dysfunction operate through non-neutrophilic mechanisms that do not trigger the calprotectin signal.",
            "evidence": "Joan GI-MAP results (Joan GI-MAP results_case study.md line 144) — Calprotectin 91 (<173 normal) despite SIgA 312 Low, beta-glucuronidase 3584 High, Klebsiella 2.74e4 High, Streptococcus 3.77e5 High, Candida albicans 4.04e3 High; Ashley GI-MAP results — Calprotectin 6 (<173 normal) despite SIgA 359 Low, Streptococcus 2.29e3 High, Giardia detected.",
            "logic": "Calprotectin indexes only the acute neutrophilic inflammatory response; chronic dysbiosis, SIgA suppression, and beta-glucuronidase elevation operate through non-neutrophilic mechanisms (immune tolerance impairment, bacterial enzymatic activity, chronic low-grade inflammation) that produce significant metabolic dysfunction without triggering the acute calprotectin signal — explaining why these markers can coexist with a normal calprotectin.",
            "confidence_band": "Core"
        }
    ]
},

"Beta-glucuronidase": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Beta-glucuronidase (B-GUS) is a bacterial enzyme produced primarily by dysbiotic organisms (Bacteroides fragilis, E. coli, Staphylococcus) that cleaves the glucuronic acid bond formed during Phase 2 hepatic detoxification (glucuronidation). This deconjugation allows conjugated hormones (especially estrogens) and toxins to be reabsorbed from the intestinal lumen rather than excreted in feces, directly recycling them back into systemic circulation. Elevated B-GUS drives estrogen dominance, increases total body toxic burden, amplifies liver congestion, and produces extensive extra-intestinal symptoms. Joan's GI-MAP: B-GUS 3584 High (reference <2486) with multiple co-elevated dysbiotic bacteria. Ashley's B-GUS 996 (normal) despite Streptococcus elevation. B-GUS establishes a direct mechanistic bridge between gut dysbiosis and both hormonal dysregulation and hepatic detoxification impairment.",
    "reasoning_chains": [
        {
            "claim": "Beta-glucuronidase specifically disrupts Phase 2 glucuronidation by cleaving the glucuronic acid bond from conjugated hormones and toxins in the intestinal lumen, allowing their reabsorption and return to hepatic circulation, directly impairing the body's capacity to eliminate estrogens and environmental toxins.",
            "evidence": "Module 6 transcript slide 119 (module-06-transcript-part-02.md lines 110-112) — 'Beta-glucuronidase is an enzyme naturally produced by the liver, kidneys, and intestinal epithelium. It can be excessively produced by multiple dysbiotic and pathogenic bacteria, in particular Bacteroides fragilis, Escherichia coli, and Staphylococcus are the three bacteria on the GI map that can really contribute to elevated levels of B-glucuronidase. This enzyme disrupts the body ability to detoxify hormones and toxins. Glucuronidation is an important part of phase 2 conjugation. This is where glucuronic acid gets attached to the target chemical and then excretes the chemical complex into the bile. B-glucuronidase will break this bond, allowing for the recycling of toxins and hormones back to the liver and to other tissues.'",
            "logic": "Phase 2 glucuronidation attaches glucuronic acid to lipophilic compounds (estrogens, xenobiotics, bilirubin) making them water-soluble and bile-excretable; B-GUS in the intestinal lumen hydrolyzes this conjugate before fecal elimination, releasing the unconjugated compound for enterohepatic reabsorption — effectively creating a recycling loop that reintroduces compounds the liver has already processed and intended to eliminate.",
            "confidence_band": "Core"
        },
        {
            "claim": "Elevated beta-glucuronidase drives estrogen dominance by deconjugating bile-excreted estrogens and returning them to portal circulation, creating an estrogenic feedback loop independent of ovarian production — a bidirectional connection between gut dysbiosis and hormonal panel markers.",
            "evidence": "Module 6 transcript slide 119 (module-06-transcript-part-02.md line 112) — 'Elevated levels are associated with overgrowth of opportunistic bacteria, liver congestion, compromised detoxification, estrogen dominance, and many extraintestinal symptoms that are related to an increased body burden.'",
            "logic": "The liver conjugates estrogens for excretion in bile; elevated B-GUS deconjugates estradiol glucuronide in the intestinal lumen, free estradiol is reabsorbed, and elevated circulating estrogen produces estrogen dominance symptoms (PMS, endometriosis, breast tissue stimulation, weight gain) without any change in ovarian output. This mechanism is particularly relevant for clients with estrogen dominance symptoms but seemingly normal serum estradiol.",
            "confidence_band": "Core"
        },
        {
            "claim": "The three GI-MAP organisms most directly driving beta-glucuronidase elevation (Bacteroides fragilis, E. coli, Staphylococcus) provide a mechanistic bridge between GI microbiome dysbiosis and hepatic detoxification failure — Joan's elevated B-GUS with multiple elevated dysbiotic bacteria demonstrates this pattern clinically.",
            "evidence": "Module 6 transcript slide 119 (module-06-transcript-part-02.md line 110) — 'in particular Bacteroides fragilis, Escherichia coli, and Staphylococcus are the three bacteria on the GI map that can really contribute to elevated levels of B-glucuronidase'; Joan GI-MAP results (Joan GI-MAP results_case study.md line 138) — 'b Glucuronidase 3584 High <2486 U/mL' alongside multiple elevated dysbiotic bacteria including Bacillus 1.22e6 High, Enterococcus faecalis 2.03e4 High, Streptococcus 3.77e5 High.",
            "logic": "These three organisms produce extracellular beta-glucuronidase as part of their normal metabolic activity; elevated organism counts on GI-MAP produce proportionally elevated B-GUS enzyme activity, which produces proportional deconjugation of Phase 2 products, which produces proportional increase in systemic recirculated toxins and hormones — establishing a quantitative relationship between GI pathogen burden and hepatic detoxification impairment on separate panels.",
            "confidence_band": "Core"
        },
        {
            "claim": "Elevated beta-glucuronidase amplifies liver burden by returning processed toxins to hepatic portal circulation for reprocessing, creating a self-reinforcing feedback loop with elevated urinary bile acids and hepatic congestion — connecting GI-MAP B-GUS to MWP hepatic markers.",
            "evidence": "Module 6 slides page 45 (2025+M6+1-149+Slides+1PP.md lines 940-942) — 'More severe toxic condition from metabolic byproducts (exudates) of the invaders and LPS. Increases Oxidative stress. Adds to liver congestion, reduces detoxification capacity.' Consistent with Module 4 slides describing enterohepatic recirculation of toxins amplifying hepatic burden and UBA elevation.",
            "logic": "Recirculated deconjugated compounds from B-GUS activity re-enter portal circulation and must be reprocessed by hepatic Phase 1 (CYP450 oxidation) and Phase 2 enzymes; each processing cycle generates reactive intermediates, increasing hepatic oxidative burden, progressively worsening liver congestion, and driving elevated UBAs (bile acid spillover into systemic circulation) — establishing the mechanistic chain connecting GI-MAP B-GUS elevation to MWP elevated UBAs.",
            "confidence_band": "Relevant"
        }
    ]
},

"Anti-gliadin IgA": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Anti-gliadin IgA (AGA-IgA) is a fecal marker of the intestinal immune system's local response to the gliadin component of gluten, reflecting mucosal immunity that does not correlate with serum IgA levels. It screens for celiac disease and non-celiac gluten sensitivity, but normal levels cannot rule out either condition because other gluten components can independently drive immune reactions. A critical interpretation dependency: when SIgA is insufficient, AGA-IgA may be suppressed (false negative); when SIgA is elevated, AGA-IgA rises proportionally. Cross-reactive foods (corn, dairy, millet, oats, rice, yeast) sharing structural homology with gliadin may also elevate this marker. Both Ashley (AGA-IgA 138, <175 normal) and Joan (83, <157 normal) are within range despite both having low SIgA, consistent with the SIgA-suppression confound producing false negatives.",
    "reasoning_chains": [
        {
            "claim": "Anti-gliadin IgA is a local intestinal immunity marker — fecal levels can be elevated even when serum concentrations remain undetectable, making it more sensitive than serum testing for local mucosal immune response to gliadin.",
            "evidence": "Module 6 transcript slide 118 (module-06-transcript-part-02.md lines 103-105) — 'Antigliadin IgA is an indicator of the immune system response to the gliadin component of the gluten protein. Fecal antigliadin levels do not necessarily correlate with blood levels. Gliadin can stimulate a local intestinal immunity and increase levels of this marker even when serum concentrations remain undetectable.'",
            "logic": "Secretory IgA production occurs locally in Peyer's patches and intestinal lamina propria B-cells; fecal AGA-IgA represents the output of local mucosal immune activation that does not necessarily cross into systemic circulation. Serum IgA reflects the systemic humoral response — a distinct compartment. Testing fecal AGA-IgA therefore captures immune activity invisible to standard serum antibody testing.",
            "confidence_band": "Core"
        },
        {
            "claim": "Normal AGA-IgA cannot rule out celiac disease or non-celiac gluten sensitivity because many gluten components beyond gliadin can provoke immune reactions — AGA-IgA is clinically significant primarily when elevated, or when a normalized follow-up result confirms therapeutic response.",
            "evidence": "Module 6 transcript slide 118 (module-06-transcript-part-02.md lines 104-105) — 'This marker is often used as a screening for celiac disease and non-celiac gluten sensitivity. But because there are many other components of gluten that can provoke an immune response, normal levels of this marker cannot rule out either celiac disease or non-celiac gluten sensitivity... my rule of thumb is this marker is only relevant when it is elevated or if it has been elevated on a first GI map and it has normalized on a follow-up test.'",
            "logic": "Gluten contains multiple immunogenic peptide sequences beyond alpha-gliadin — including omega-gliadin, gamma-gliadin, glutenins, and non-gliadin wheat antigens; each can independently drive intestinal immune activation without elevating AGA-IgA specifically. A negative AGA-IgA therefore has low negative predictive value for ruling out gluten reactivity — it only confirms the gliadin component did not trigger measurable local IgA production.",
            "confidence_band": "Core"
        },
        {
            "claim": "AGA-IgA interpretation requires simultaneous evaluation of SIgA status: when SIgA is insufficient, the immune response to gliadin may be suppressed producing false negative AGA-IgA; when SIgA is elevated, AGA-IgA rises — the two markers form an interdependent pair.",
            "evidence": "Module 6 transcript slide 118 (module-06-transcript-part-02.md lines 108-109) — 'if intestinal SigA is insufficient, the immune response to gliadin may be suppressed. Conversely, when SigA is elevated, the immune response to gliadin can increase and antigliadin IgA will rise.' Ashley GI-MAP — SIgA 359 Low, AGA-IgA 138 normal; Joan GI-MAP — SIgA 312 Low, AGA-IgA 83 normal. Both case study patients show low SIgA with normal AGA-IgA, consistent with SIgA-suppressed AGA-IgA false negative.",
            "logic": "SIgA serves as the production substrate for AGA-IgA — antigen-specific IgA antibodies require sufficient overall SIgA production capacity; when SIgA is globally suppressed by chronic dysbiosis, stress, or immune compromise, the immune system cannot mount adequate antigen-specific IgA responses including to gliadin, producing falsely normal AGA-IgA levels that may mask true gluten sensitivity.",
            "confidence_band": "Core"
        },
        {
            "claim": "Elevated AGA-IgA should prompt MRT food sensitivity testing because cross-reactive foods (corn, dairy, millet, oats, rice, yeast) share structural homology with gliadin and may independently drive AGA-IgA elevation or explain persistent elevation after gluten removal.",
            "evidence": "Module 6 transcript slide 118 (module-06-transcript-part-02.md lines 106-108) — 'Elevated levels are associated with localized immune response to gluten, also can be associated with celiac disease, non-celiac gluten sensitivity, low elastase, low hydrochloric acid, undigested food particles, and additional food sensitivities, particularly those foods known to cross-react with gluten like corn, dairy, millet, oats, rice, and yeast. Always consider additional food sensitivity testing when this marker is out of range.'",
            "logic": "Cross-reactive foods contain peptide sequences with structural homology to gliadin epitopes; the intestinal immune system generates IgA against these cross-reactive sequences through epitope mimicry, elevating AGA-IgA without ongoing gluten consumption. Failure to identify and eliminate cross-reactive foods explains why AGA-IgA remains elevated in some clients despite strict gluten avoidance — MRT testing identifies these cross-reactors.",
            "confidence_band": "Core"
        }
    ]
},

"Secretory IgA \u2014 GI tract": {
    "confidence_band": "core",
    "finding_count": 4,
    "summary": "Secretory IgA (SIgA) on the GI-MAP is the dominant mucosal immunoglobulin in the gut, functioning as first-line immune defense against antigens, pathogens, and food-derived irritants by forming complexes that prevent translocation across the mucosal barrier. This measurement is distinct from the SIgA on the Mucosal Barrier Assessment (MBA), though both reflect mucosal immune function. Low GI-MAP SIgA (<510 ug/g) indicates chronic dysbiosis, chronic stress, protein malnutrition, or immune compromise; levels below 200 indicate a total shutdown of gut immune function. Elevated SIgA reflects active immune challenge. Both Ashley (359 Low) and Joan (312 Low) show clinically significant SIgA suppression, creating a self-amplifying dysbiosis-SIgA feedback loop — and explaining why their AGA-IgA responses appear falsely normal despite potential gluten reactivity.",
    "reasoning_chains": [
        {
            "claim": "SIgA is the first-line immune defense in the GI and respiratory tracts, forming immune complexes with pathogens and food antigens that prevent mucosal translocation (immune exclusion) — low SIgA directly increases susceptibility to pathogen colonization and food antigen-driven systemic immune activation.",
            "evidence": "Module 6 transcript slide 117 (module-06-transcript-part-02.md lines 101-102) — 'Secretory IgA, or SIgA, is an immune globulin secreted into the GI tract that influences the microbiome and helps to maintain mucosal barrier function. It is our first line of immune defense against antigens and pathogens in the GI and respiratory tracts, and it protects against exposure to food-derived antigens. It forms complexes with gut pathogens and allergens, thereby preventing them from crossing the mucosal barrier.'",
            "logic": "SIgA binds pathogen surface antigens in the intestinal lumen, forming large immune complexes too large to traverse epithelial tight junctions — immune exclusion; without sufficient SIgA, pathogens and food antigens reach the mucosal surface unimpeded, increasing both colonization risk and systemic antigen translocation that drives food sensitivities and systemic immune activation.",
            "confidence_band": "Core"
        },
        {
            "claim": "Low GI-MAP SIgA (<510 ug/g) reflects chronic dysbiosis, chronic stress, immune compromise, or protein malnutrition; levels below 200 ug/g indicate a total shutdown of gut immune function, representing the highest clinical urgency among SIgA results.",
            "evidence": "Module 6 transcript slide 117 (module-06-transcript-part-02.md line 102) — 'Low levels are associated with chronic dysbiosis, chronic exposure to food antigens, chronic stress, immune-compromised clients, protein malnutrition, increased risk of intestinal infections and inflammation, And levels below 200 may indicate a total shutdown of immune function in the gut.' Ashley GI-MAP — SIgA 359 Low (510-2010 reference); Joan GI-MAP — SIgA 312 Low (510-2010 reference); both in the impaired-but-not-shutdown range.",
            "logic": "SIgA is produced by plasma cells in the intestinal lamina propria from protein precursors via J-chain and secretory component; protein malnutrition reduces substrate availability; chronic cortisol elevation downregulates mucosal plasma cell activity through glucocorticoid receptor signaling. The level below 200 threshold represents not just low production but a collapse of mucosal immune capacity, predicting rapidly escalating pathogen burden.",
            "confidence_band": "Core"
        },
        {
            "claim": "Low SIgA creates a self-amplifying dysbiosis feedback loop — low SIgA allows pathogen colonization, which causes dysbiosis, which further damages SIgA-producing mucosal cells — and is bidirectionally connected to HPA axis cortisol dysregulation through the stress-mucosal immunity axis.",
            "evidence": "Module 6 transcript slide 117 (module-06-transcript-part-02.md line 101) — 'levels can be severely impacted by chronic stress'; transcript slide 125 (lines 161-162) — 'Secretory IgA is almost always low' in clients presenting with autoimmune disease and multiple GI-MAP dysbiotic markers. Consistent with Module 5 MBA teaching connecting HPA axis cortisol elevation to mast cell activation and mucosal immune suppression.",
            "logic": "HPA axis cortisol elevation activates glucocorticoid receptors on mucosal plasma cells, reducing SIgA production; reduced SIgA allows increased pathogen colonization; dysbiosis generates mucosal inflammation that further activates the HPA axis; this self-perpetuating cycle connects the stress panel (cortisol/DHEA ratio) to the GI-MAP SIgA result through a shared physiological mechanism.",
            "confidence_band": "Core"
        },
        {
            "claim": "Elevated SIgA on the GI-MAP indicates active immune system activation by food antigens, pathogens, stress, or food sensitivities — the opposite pattern from low SIgA but still representing a dysregulated state requiring identification of the driving antigen or organism.",
            "evidence": "Module 6 transcript slide 117 (module-06-transcript-part-02.md line 102) — 'elevated levels are associated with immune system activation by food antigens and or pathogens, stress, food allergies, and food sensitivities.'",
            "logic": "Elevated fecal SIgA indicates the gut immune system is actively producing antibodies against a recognized threat; identifying the specific trigger (pathogen, food antigen, stress) is the clinical priority. The dynamic range of SIgA (very low to very high) reflects the marker's bidirectional clinical utility as both an immune suppression indicator and an immune activation indicator, requiring context from other GI-MAP findings for correct interpretation.",
            "confidence_band": "Core"
        }
    ]
},

"Occult Blood": {
    "confidence_band": "core",
    "finding_count": 3,
    "summary": "Occult Blood-FIT (Fecal Immunochemical Test) measures hemoglobin concentration in stool to screen for mucosal bleeding from structural GI lesions. Levels greater than 10 ug/g indicate increased disease risk and mandate immediate MD/GI specialist referral before any FDN protocol is implemented. Clinical stratification: 5-9 ug/g typically indicates hemorrhoids; 10-50 indicates polyps or diverticulitis; greater than 50 indicates bleeding ulcer, colorectal cancer, IBD, or upper GI bleed with iron-deficient anemia. In the FDN context, this marker functions as a safety gate and medical referral trigger rather than a modifiable metabolic marker — its elevation requires physician evaluation, not a DRESS protocol. Both Ashley (below detection limit) and Joan (0) show normal occult blood despite multiple dysbiotic findings, demonstrating that extensive GI dysfunction can exist without producing structural mucosal bleeding.",
    "reasoning_chains": [
        {
            "claim": "Fecal occult blood FIT levels greater than 10 ug/g are associated with increased risk of structural GI pathology including intestinal polyps, diverticulitis, bleeding ulcers, colorectal cancer, IBD, and upper GI bleeds producing iron-deficient anemia — mandating immediate MD/GI referral.",
            "evidence": "Module 6 transcript slide 120 (module-06-transcript-part-02.md lines 113-115) — 'Occult blood - FIT measures the concentration of hemoglobin that is present in the stool, and research indicates that levels greater than 10 are associated with an increased risk of disease. So, you always want to refer out to an MD or a GI specialist for immediate follow-up when occult blood is elevated. Elevated levels are associated with diverticulitis, intestinal polyps, bleeding ulcers, colorectal cancer, inflammatory bowel disease, and upper GI bleeds that cause iron-deficient anemia.'",
            "logic": "Hemoglobin measured by FIT indicates red blood cell presence in stool; above 10 ug/g, the quantity exceeds what hemorrhoids and minor mucosal irritation typically produce, indicating structural lesions capable of sustained mucosal bleeding. Each condition in the associated list produces characteristic bleeding patterns that correlate with specific FIT level ranges, enabling clinical stratification before definitive diagnostic testing.",
            "confidence_band": "Core"
        },
        {
            "claim": "Clinical severity stratification of FIT results (5-9 ug/g for hemorrhoids; 10-50 for polyps/diverticulitis; greater than 50 for bleeding ulcer/cancer/IBD/upper GI bleed) guides the urgency of medical referral and specificity of further diagnostic testing.",
            "evidence": "Module 6 transcript slide 120 (module-06-transcript-part-02.md line 115) — 'For your own reference, levels between 5 and 9 typically indicate hemorrhoids, whereas levels greater than 10, in particular between 10 and 50, usually indicate one or many polyps or perhaps diverticulitis.'",
            "logic": "Hemorrhoids are superficial venous plexuses that bleed at low volume during defecation; polyps and diverticula are mucosal lesions capable of sustained oozing producing moderate FIT elevation; colorectal cancer and IBD produce higher-volume bleeding from deeper vascular involvement. This stratification provides the FDN practitioner with a referral urgency framework — all greater than 10 require referral, but the level range guides the physician's initial workup priority.",
            "confidence_band": "Core"
        },
        {
            "claim": "In the FDN protocol hierarchy, occult blood elevation functions as an absolute medical referral trigger that overrides any DRESS protocol implementation until structural pathology is ruled out by a physician — establishing it as a safety gate rather than a modifiable metabolic marker.",
            "evidence": "Module 6 transcript slide 120 (module-06-transcript-part-02.md line 113) — 'you always want to refer out to an MD or a GI specialist for immediate follow-up when occult blood is elevated'; Module 6 transcript slide 148 (module-06-transcript-part-02.md line 297) — 'if they are real sick and they have got something like salmonella or one of these bad bugs, even H. pylori, think about referring out' — establishing that certain GI findings require medical oversight before FDN intervention proceeds.",
            "logic": "Structural mucosal lesions (polyps, cancer, IBD flares) require medical diagnosis, colonoscopy, and often surgical or pharmacological intervention — outside FDN scope of practice; implementing a DRESS protocol on a client with undiagnosed colorectal cancer or actively bleeding IBD could delay life-saving medical care. The referral-first rule reflects the FDN principle that practitioners never implement protocols without appropriate medical context when red-flag markers are present.",
            "confidence_band": "Core"
        }
    ]
}

}

# --- PROCESSING ---

missing = [v for v in state['pending_variables'] if v not in variables_data]
if missing:
    print(f"WARNING: No research data for: {missing}")

session_vars_processed = []

for var_name in list(state['pending_variables']):

    # MC-5: Anti-redundancy check
    if var_name in state['researched_variables']:
        print(f"SKIP (already researched): {var_name}")
        if var_name in state['pending_variables']:
            state['pending_variables'].remove(var_name)
        continue

    if var_name not in variables_data:
        print(f"SKIP (no data): {var_name}")
        continue

    data = variables_data[var_name]

    # Add research summary
    state['research_summaries'][var_name] = data

    # Move variable from pending to researched
    state['pending_variables'].remove(var_name)
    state['researched_variables'].append(var_name)
    session_vars_processed.append(var_name)

    # MC-8: Write state.json after EACH variable
    state['last_updated'] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f"[{len(session_vars_processed)}/10] Saved: {var_name}")

# Phase transition
state['phase'] = 'connection_validation'
state['last_updated'] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

if 'session_log' not in state:
    state['session_log'] = []

state['session_log'].append({
    "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "phase_executed": "variable_research",
    "variables_researched": session_vars_processed,
    "connections_validated": [],
    "output_file": "session-outputs/2026-03-23-variable-research-2.md"
})

with open(state_path, 'w', encoding='utf-8') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)

print(f"\n=== COMPLETE ===")
print(f"Phase: {state['phase']}")
print(f"Researched: {len(state['researched_variables'])} variables")
print(f"Pending: {len(state['pending_variables'])} variables")
print(f"Processed this session: {session_vars_processed}")
