# Connection Validation Session 15 — 2026-03-24

**Phase:** connection_validation (final session — convergence reached)
**Pairs evaluated this session:** 26
**Validated:** 12 | **Discarded:** 14
**Session budget used:** 26 pairs × 500 = 13,000 estimated tokens (budget: 18,000)
**Phase transition:** connection_validation → synthesis (pending_variables[] empty AND connections.pending[] empty)

---

## VALIDATED CONNECTIONS (12)

### Parasitic Load → Beta-glucuronidase
**Type:** causal
**Explanation:** Giardia increases Proteobacteria (including E. coli, a primary B-GUS producer) while decreasing Firmicutes, shifting the microbiome toward B-GUS-producing organism overgrowth and directly elevating beta-glucuronidase activity through dysbiotic microbial shift.
**Evidence count:** 2
- **Line 1:** Giardia documented in FDN Module 6 to cause "extensive pro-inflammatory dysbiosis, increases the Proteobacteria phylum" (including E. coli) and "decreases the Firmicutes phylum" — E. coli is explicitly named as one of the three primary GI-MAP B-GUS producers.
- **Line 2:** Parasitic infection collectively shifts microbiome toward B-GUS-producing organism overgrowth through mucosal damage and competitive displacement of butyrate-producing Firmicutes that limit Proteobacteria expansion.

---

### Parasitic Load → Anti-gliadin IgA
**Type:** causal
**Explanation:** Giardia directly increases immune reactions to food antigens including gluten (FDN Module 6 source) and drives Zonulin-mediated gut hyperpermeability allowing gliadin translocation to mucosal immune cells in Peyer's patches, triggering sensitization and elevated AGA-IgA production.
**Evidence count:** 2
- **Line 1 (Core):** FDN Module 6 transcript (module-06-transcript-part-02.md lines 62-66) explicitly states: "giardia can increase immune reactions to food antigens, and that includes gluten" — direct causal statement from FDN source.
- **Line 2 (Relevant):** Giardia stimulates gut hyperpermeability via Zonulin release and tight junction disassembly, allowing gliadin peptides to translocate to submucosal Peyer's patches where mucosal IgA sensitization occurs — mechanistic pathway underlying Giardia-driven gluten sensitivity.

---

### Parasitic Load → Secretory IgA — GI tract
**Type:** causal
**Explanation:** Parasitic organisms bidirectionally modulate GI-MAP SIgA: active parasitic challenge first elevates SIgA via mucosal immune activation, while chronic infection depletes SIgA through immune exhaustion and HPA axis-cortisol-mediated downregulation of mucosal plasma cell SIgA synthesis.
**Evidence count:** 2
- **Line 1:** Parasitic pathogens trigger active SIgA-mediated mucosal immune responses (SIgA elevated: "associated with immune system activation by pathogens" per FDN Module 6); with chronicity, continuous SIgA deployment against parasitic antigens progressively exhausts mucosal IgA reserves.
- **Line 2:** Chronic parasitic infection constitutes a persistent physiological stressor activating HPA → cortisol elevation → glucocorticoid receptor-mediated downregulation of mucosal plasma cell SIgA synthesis — mechanistically linking parasitic burden to SIgA suppression via the stress axis.

---

### Parasitic Load → Occult Blood
**Type:** causal
**Explanation:** Entamoeba histolytica directly bores through the intestinal wall producing fulminating colitis and dysentery with bloody stools, constituting the structural mucosal bleeding that FIT occult blood measures; amoebic colitis represents the IBD-like structural mucosal pathology for which the occult blood referral threshold was designed.
**Evidence count:** 2
- **Line 1 (Core):** FDN Module 6 transcript (module-06-transcript-part-02.md lines 57-61) documents E. histolytica causing "diarrhea, fulminating colitis, dysentery" — dysentery definitionally involves bloody stools producing hemoglobin detectable by FIT occult blood.
- **Line 2 (Core):** The Occult Blood marker's clinical associations (IBD, structural mucosal pathology >10 ug/g requiring medical referral) precisely describe the category of disease that E. histolytica-induced amoebic colitis produces — invasive parasitic colitis is classified within the IBD-like structural mucosal pathology that FIT was designed to detect.

---

### Dysbiotic and Opportunistic Bacteria → Commensal Flora Balance
**Type:** architectural
**Explanation:** Dysbiotic and opportunistic bacteria are the structural inverse of commensal flora in the gut ecosystem; FDN explicitly describes dysbiotic bacteria as depletors of commensal populations through competitive displacement, LPS-mediated inflammation, and metabolic byproducts inhibitory to commensal growth.
**Evidence count:** 2
- **Line 1 (Core):** FDN Module 6 slides page 21 explicitly contrasts: "Bad bacteria: Produce pro-inflammatory LPS, Encourage the overgrowth of other opportunistic bacteria, Deplete population levels of good bacteria" — direct architectural opposition defined in FDN source.
- **Line 2:** The "Insufficiency Dysbiosis" pattern in FDN's four-pattern dysbiosis classification describes exactly this structural relationship: commensal depletion is the defining feature, caused by dysbiotic organism overgrowth — the two variables define the same ecosystem state from inverse perspectives.

---

### Dysbiotic and Opportunistic Bacteria → Beta-glucuronidase
**Type:** causal
**Explanation:** Three specific dysbiotic bacteria on the GI-MAP (Bacteroides fragilis, E. coli, Staphylococcus) produce extracellular B-GUS as part of their metabolic activity; elevated counts produce proportionally elevated B-GUS enzyme activity, demonstrated in Joan's GI-MAP showing B-GUS 3584 High alongside multiple elevated dysbiotic organisms.
**Evidence count:** 2
- **Line 1 (Core):** FDN Module 6 transcript (module-06-transcript-part-02.md line 110) explicitly names Bacteroides fragilis, E. coli, and Staphylococcus as the three GI-MAP organisms that "can really contribute to elevated levels of B-glucuronidase" — direct mechanistic link from named dysbiotic organisms to B-GUS elevation.
- **Line 2 (Core):** Joan's GI-MAP results demonstrate clinical correlation: B-GUS 3584 High (reference <2486) alongside multiple elevated dysbiotic organisms including Bacillus 1.22e6 High, Enterococcus faecalis 2.03e4 High, Streptococcus 3.77e5 High — empirical confirmation of dysbiotic bacteria → elevated B-GUS.

---

### Dysbiotic and Opportunistic Bacteria → Secretory IgA — GI tract
**Type:** causal
**Explanation:** Dysbiotic bacteria activate the HPA axis via LPS-driven pro-inflammatory cytokines, elevating cortisol which downregulates mucosal plasma cell SIgA synthesis through glucocorticoid receptor signaling; both case study patients with elevated dysbiotic organisms show correspondingly low GI-MAP SIgA (Joan: 312 Low, Ashley: 359 Low).
**Evidence count:** 2
- **Line 1 (Core):** FDN Module 6 transcript explicitly states low GI-MAP SIgA is "associated with chronic dysbiosis" — direct clinical association stated in source; chronic dysbiosis from dysbiotic bacterial overgrowth constitutes the stated upstream driver of SIgA suppression.
- **Line 2 (Relevant):** Both case study patients with elevated dysbiotic organisms (Joan: Klebsiella 2.74e4 High, Streptococcus 3.77e5 High; Ashley: Streptococcus 2.29e3 High, Giardia detected) show correspondingly low GI-MAP SIgA — empirical clinical confirmation of the dysbiotic bacteria → SIgA suppression connection.

---

### Commensal Flora Balance → Beta-glucuronidase
**Type:** architectural
**Explanation:** Bacteroides fragilis is simultaneously a keystone commensal organism and primary B-GUS producer; elevated Bacteroidetes in Joan's GI-MAP (7.53e12 High) corresponds to elevated B-GUS (3584 High), demonstrating the dual classification of Bacteroides fragilis bridging the commensal flora and B-GUS measurement.
**Evidence count:** 2
- **Line 1:** Bacteroides fragilis is classified in FDN Module 6 as a commensal organism with key immune-modulatory functions (commensal flora section) AND simultaneously named as one of the three primary B-GUS-producing organisms on the GI-MAP — the same organism bridges both variables.
- **Line 2:** Joan's GI-MAP data demonstrates the clinical correlation: Bacteroidetes elevated at 7.53e12 High (which includes Bacteroides fragilis species) corresponds to B-GUS 3584 High — consistent with disproportionate Bacteroidetes elevation driving elevated B-GUS through the Bacteroides fragilis enzyme production mechanism.

---

### Commensal Flora Balance → Anti-gliadin IgA
**Type:** architectural
**Explanation:** Commensal bacteria produce SCFA that support SIgA synthesis, providing the substrate for antigen-specific AGA-IgA production; commensal depletion suppresses SCFA-mediated SIgA support and reduces AGA-IgA capacity, explaining why both FDN patients with commensal-disrupted ecosystems show low SIgA and suppressed AGA-IgA.
**Evidence count:** 2
- **Line 1:** FDN Module 6 explicitly states "Good bacteria: Produce SCFA which reduce inflammation, increase SIgA and mucin" — commensal flora directly increases SIgA through SCFA; and FDN AGA-IgA teaching explicitly states "when SIgA is elevated, the immune response to gliadin can increase and AGA-IgA will rise" — connecting the commensal→SCFA→SIgA chain to AGA-IgA output.
- **Line 2:** Both case study patients (Ashley: SIgA 359 Low + AGA-IgA 138 normal/suppressed; Joan: SIgA 312 Low + AGA-IgA 83 normal/suppressed) demonstrate commensal-depleted ecosystems with low SIgA producing suppressed AGA-IgA responses — empirical confirmation of the commensal→SCFA→SIgA→AGA-IgA architectural chain.

---

### Commensal Flora Balance → Secretory IgA — GI tract
**Type:** causal
**Explanation:** FDN source explicitly states commensal bacteria produce SCFA that increase SIgA; adequate commensal flora is prerequisite for GI-MAP SIgA production; both case study patients show low GI-MAP SIgA alongside commensal-disrupted dysbiosis, demonstrating the commensal-SCFA-SIgA production dependency.
**Evidence count:** 2
- **Line 1 (Core):** FDN Module 6 slides page 21 explicitly states: "Good bacteria: Produce SCFA which reduce inflammation, increase SIgA and mucin" — direct causal statement that commensal bacteria increase SIgA through SCFA production.
- **Line 2:** Both case study patients show low GI-MAP SIgA (Ashley 359 Low, Joan 312 Low) alongside commensal-disrupted dysbiosis (multiple elevated dysbiotic organisms displacing commensals), providing empirical clinical confirmation of the commensal→SCFA→SIgA production dependency.

---

### Calprotectin and Lactoferrin → Occult Blood
**Type:** correlational
**Explanation:** Calprotectin and occult blood are parallel output markers of the same class of structural GI mucosal pathology; calprotectin distinguishes active IBD from functional GI disorders while occult blood marks IBD-associated structural mucosal bleeding, making them co-indicators of the same acute inflammatory bowel pathology class requiring medical evaluation.
**Evidence count:** 2
- **Line 1:** Calprotectin research in FDN establishes it as a marker for "active inflammatory bowel disease" (93-95% sensitivity/specificity for IBD vs. IBS); IBD is simultaneously one of the primary conditions associated with elevated occult blood per FDN Occult Blood research — both markers are associated with active IBD.
- **Line 2:** Both Calprotectin and Occult Blood serve as medical referral triggers in FDN when elevated: elevated calprotectin signals IBD requiring GI specialist evaluation; elevated occult blood (>10 ug/g) requires "immediate MD/GI specialist referral" — they co-function as safety gates and parallel structural pathology indicators in the same clinical decision pathway.

---

### Anti-gliadin IgA → Secretory IgA — GI tract
**Type:** architectural
**Explanation:** AGA-IgA is mechanistically a subset of total SIgA directed against gliadin epitopes; FDN explicitly states SIgA status determines AGA-IgA response capacity, with low total SIgA suppressing antigen-specific AGA-IgA production; both FDN case study patients show low SIgA with correspondingly suppressed AGA-IgA, confirming this SIgA-dependent architectural relationship.
**Evidence count:** 2
- **Line 1 (Core):** FDN Module 6 transcript (module-06-transcript-part-02.md lines 108-109) explicitly states: "if intestinal SIgA is insufficient, the immune response to gliadin may be suppressed. Conversely, when SIgA is elevated, the immune response to gliadin can increase and AGA-IgA will rise" — direct bidirectional dependency stated in FDN source.
- **Line 2 (Core):** Both case study patients show the pattern: Ashley (SIgA 359 Low + AGA-IgA 138 within range/suppressed) and Joan (SIgA 312 Low + AGA-IgA 83 within range/suppressed) — empirical confirmation that low total SIgA correlates with suppressed antigen-specific AGA-IgA responses in both FDN clinical cases.

---

## DISCARDED CONNECTIONS (14)

### Parasitic Load → Calprotectin and Lactoferrin
**Reason:** Most parasitic organisms (Giardia, Blastocystis) drive eosinophilic/mast cell rather than neutrophilic mucosal responses; Ashley shows Giardia detected alongside normal calprotectin (6 ug/g), demonstrating clinical dissociation; FDN case study data establishes that parasitic burden can coexist with normal calprotectin. Insufficient evidence at Relevant confidence for a validated connection.

### Dysbiotic and Opportunistic Bacteria → Calprotectin and Lactoferrin
**Reason:** Joan shows multiple elevated dysbiotic organisms (Klebsiella 2.74e4 High, Streptococcus 3.77e5 High) alongside normal calprotectin (91 ug/g); FDN Calprotectin research explicitly states chronic dysbiosis operates through non-neutrophilic mechanisms that do not trigger the calprotectin signal; insufficient evidence at Relevant confidence.

### Dysbiotic and Opportunistic Bacteria → Anti-gliadin IgA
**Reason:** Dysbiotic bacteria have competing effects on AGA-IgA: LPS-driven permeability increases gliadin exposure (upward pressure) while dysbiosis-driven SIgA suppression reduces AGA-IgA production capacity (downward pressure); both patients show normal AGA-IgA despite significant dysbiosis; competing mechanisms prevent a validated directional connection at Relevant confidence.

### Dysbiotic and Opportunistic Bacteria → Occult Blood
**Reason:** Both patients show normal occult blood (Ashley: below detection, Joan: 0) despite significant dysbiotic bacterial burden including multiple organisms elevated above reference range; chronic dysbiotic bacteria produce functional GI dysfunction without structural mucosal bleeding that FIT occult blood measures; no independent evidence at Relevant confidence.

### Commensal Flora Balance → Calprotectin and Lactoferrin
**Reason:** Commensal flora depletion (insufficiency dysbiosis) does not directly drive neutrophilic GI inflammation that calprotectin measures; both patients show normal calprotectin despite significant dysbiosis; commensal depletion affects mucosal barrier through SCFA depletion and competitive exclusion loss, below the threshold required to trigger the neutrophilic calprotectin response.

### Commensal Flora Balance → Occult Blood
**Reason:** Commensal imbalance produces functional gut ecosystem dysfunction (reduced SCFA, impaired mucosal immunity) but not structural mucosal lesions causing active bleeding; both patients show normal occult blood despite commensal imbalance; no independent evidence at Relevant confidence connects commensal ecosystem changes to structural mucosal bleeding.

### Calprotectin and Lactoferrin → Beta-glucuronidase
**Reason:** Joan shows elevated B-GUS (3584 High) alongside normal calprotectin (91 ug/g), demonstrating direct clinical dissociation; calprotectin and beta-glucuronidase measure mechanistically independent processes (neutrophilic mucosal inflammation vs. bacterial enzyme activity); no structural connection supported by independent evidence at Relevant confidence.

### Calprotectin and Lactoferrin → Anti-gliadin IgA
**Reason:** Calprotectin reflects innate neutrophilic immune response (acute GI inflammation) while AGA-IgA reflects adaptive mucosal IgA response to a specific dietary antigen — mechanistically independent immune pathways; no clinical correlation from case study data; no independent evidence at Relevant confidence supports a validated connection.

### Calprotectin and Lactoferrin → Secretory IgA — GI tract
**Reason:** Both patients show low SIgA (Ashley 359, Joan 312) alongside normal calprotectin (Ashley 6, Joan 91), demonstrating dissociation; SIgA suppression operates through cortisol-mediated inhibition of mucosal plasma cell activity and chronic dysbiosis — not through neutrophilic inflammation measured by calprotectin; no structural causal connection at Relevant confidence.

### Beta-glucuronidase → Anti-gliadin IgA
**Reason:** Joan shows elevated B-GUS (3584 High) alongside normal AGA-IgA (83), demonstrating clinical dissociation; any B-GUS-to-AGA-IgA pathway requires multiple indirect steps (B-GUS → toxin burden → permeability → gliadin translocation → IgA sensitization) without direct FDN evidence; insufficient independent evidence at Relevant confidence.

### Beta-glucuronidase → Secretory IgA — GI tract
**Reason:** Ashley shows normal B-GUS alongside low SIgA (359 Low), demonstrating SIgA suppression occurs independently of B-GUS status; primary SIgA suppressors are chronic dysbiosis and cortisol per FDN research; any B-GUS-to-SIgA pathway requires multiple intermediate steps (B-GUS → toxin burden → HPA → cortisol → SIgA) without direct FDN evidence at Relevant confidence.

### Beta-glucuronidase → Occult Blood
**Reason:** Joan shows elevated B-GUS (3584 High) alongside normal occult blood (0), confirming dissociation; B-GUS drives estrogen recycling and hepatic congestion by deconjugating Phase 2 compounds but does not produce structural mucosal lesions causing active bleeding; no independent evidence at Relevant confidence.

### Anti-gliadin IgA → Occult Blood
**Reason:** Severe celiac ulcerative jejunitis causing mucosal bleeding requires advanced structural pathological disease beyond the functional metabolic chaos model FDN operates within; both patients show normal AGA-IgA and normal occult blood; no independent evidence within the FDN framework at Relevant confidence.

### Secretory IgA — GI tract → Occult Blood
**Reason:** Both patients show low SIgA (Ashley 359 Low, Joan 312 Low) alongside normal occult blood (both 0 or below detection), directly demonstrating dissociation; SIgA insufficiency increases pathogen susceptibility but does not reach the structural tissue integrity failure threshold that FIT occult blood measures; no independent evidence at Relevant confidence.

---

## CONVERGENCE STATUS

- `pending_variables[]`: empty ✓
- `connections.pending[]`: empty ✓ (all 26 pairs processed this session)
- **Convergence condition met → phase = "synthesis"**

**Total validated connections in knowledge map:** 463
**Total discarded connections:** 67
**Total researched variables:** 33

**Next session:** Phase 5 — Synthesis. Reads all validated connections, identifies emergent patterns (chains, clusters, cross-domain bridges), writes conclusion document and populates knowledge-map.md.
