# System Map — Inventory Pass
**Source:** `raw context/claude conversation.md`
**Date:** 2026-03-22

---

## 1. Source File

| Item | Role | Notes |
|---|---|---|
| `raw context/claude conversation.md` | Raw brain dump — conversation transcript | Claude ↔ Kaitlyn dialogue, 282 lines, 9:04–9:27 PM session |

---

## 2. Entities Inventoried

### 2A. The Person and Their Project

| Item | Role Layer | Explicit Content | Implicit Content |
|---|---|---|---|
| **Kaitlyn** (user) | meta-meta | Building a "health transformation framework" / methodology | Practitioner context — likely FDN-certified or in training; building client-facing or teaching material |
| **Health transformation methodology** | meta | Integrates FDN with mechanistic physiology | Needs to go deeper than standard FDN practice; oriented toward clinical reasoning, not just marker collection |
| **Visual diagram request** (line 235–236) | macro | "Visual diagram where each FDN marker connects to where the possibility lies for malfunction" | The diagram is a central deliverable — interactive HTML was partially produced but the underlying logical framework needs extraction |

---

### 2B. Framework / System

| Item | Role Layer | Explicit Content | Implicit Content |
|---|---|---|---|
| **FDN (Functional Diagnostic Nutrition)** | meta | HIDDEN stressors model; HEAT acronym (Health, Eating, Activity, Tress, Sleep); "metabolic chaos" concept; lab marker panel | Underlying contract: dysfunction precedes disease; upstream stressors compound; markers are proxies for systemic load |
| **Metabolic chaos** | meta | Compounding subclinical dysfunction producing measurable downstream collapse | Self-reinforcing loop architecture — not linear chains but feedback webs |
| **HIDDEN stressors / HEAT** | macro | H-E-A-T categories for upstream load | Organizing principle for root cause classification |
| **Nodal reasoning** (line 151–153) | meta | "Using pattern of findings across multiple markers to localize dysfunction" | Currently absent from standard FDN practice; identified as extension point |

---

### 2C. Lab Markers

| Marker | Role Layer | Explicit Content | Implicit Content / Dependencies |
|---|---|---|---|
| **SIgA (Secretory IgA)** | micro | Measured in saliva or stool; proxy for mucosal immune resilience; "sensitive but non-specific" | Downstream readout of 7-node axis; low reading = system-level signal, not localized diagnosis |
| **Cortisol / DHEA ratio** | micro | Bidirectional marker; captures HPA output (cortisol) AND reserve capacity (DHEA); high ratio = elevated cortisol, depleted DHEA, or both | Three distinct patterns with different intervention logic; ratio is terminal output of multi-loop feedback system |
| **OAT (Organic Acids Test)** | micro | Mentioned indirectly; Clostridia → HPHPA metabolite | Contains neurotransmitter metabolite markers; bridges gut microbiome to brain chemistry |
| **Full FDN marker panel** (implied) | micro | Not enumerated in this conversation but referenced as the target population for the visual diagram | Includes adrenal, sex hormone, thyroid, gut, neurotransmitter, immune markers — needs full list for complete diagram |

---

### 2D. Biological Systems and Pathways

| System/Pathway | Role Layer | Explicit Content | Implicit Content |
|---|---|---|---|
| **SIgA Production Axis (7 nodes)** | micro | 1. Antigen sampling (Peyer's patches/M cells) → 2. IgA class switching (MLNs) → 3. Gut homing (α4β7/CCR9) → 4. Plasma cell differentiation (lamina propria) → 5. Dimeric IgA + J chain secretion → 6. pIgR transcytosis (epithelium) → 7. SC cleavage / luminal release | Each node has distinct upstream vulnerability; same output (low SIgA) can originate from different failed nodes |
| **GALT** | macro | Distributed network: Peyer's patches, ILFs, MLNs, lamina propria | Induction site + decision node + effector site — staged functional architecture; microbiome-dependent for structural maturation |
| **HPA Axis** | macro | Cortisol production; DHEA as reserve capacity; three ratio patterns: (1) high cortisol/low DHEA, (2) low cortisol/low DHEA, (3) both moving in opposition | Self-reinforcing: gut permeability → loads HPA → degrades gut; blood sugar instability → loads HPA; neurotransmitter depletion → impairs stress resilience → loads HPA |
| **Vitamin A / Retinoic Acid Axis** | micro | Retinol → retinoic acid conversion in Peyer's patch DCs; drives IgA class switching + gut-homing imprinting + Treg induction + epithelial differentiation; regulates Th1/Th17 balance; innate immune function (NK, neutrophils, macrophages) | BCMO1 polymorphism can reduce plant-source conversion 50–70%; self-reinforcing deficiency loop (deficiency → epithelial metaplasia → impaired absorption → worsened deficiency) |
| **IDO → Kynurenine shunting** | micro | Cortisol activates IDO; shunts tryptophan away from serotonin toward kynurenine pathway | Simultaneously depletes serotonin AND generates neuroinflammatory metabolites; underemphasized in FDN resources |
| **Estrobolome** | micro | Gut microbiome → estrogen recirculation; specific gut-hormone bridge | Mechanistically specific; connects dysbiosis directly to estrogen dominance patterns |
| **Clostridia → HPHPA → Dopamine interference** | micro-micro | Clostridia produce HPHPA metabolite; HPHPA competes with dopamine pathways at enzyme level | Measurable on OAT; microbiome-brain axis at enzyme level; direct causal mechanism not metaphorical |
| **Progesterone steal** | macro | Progesterone → cortisol shunting under HPA load; bridge between HPA and sex hormone cascade | Explains why chronic stress produces adrenal AND gonadal dysfunction simultaneously (not sequentially) |

---

### 2E. Nutrients / Biochemical Variables

| Item | Role Layer | Explicit Content | Implicit Content |
|---|---|---|---|
| **Vitamin A (Retinol)** | micro-micro | Preformed (animal sources): liver, cod liver oil, egg yolks, full-fat dairy, fatty fish. Pro-vitamin (beta-carotene, plant sources): requires conversion | Rate-limiting for IgA axis, Treg induction, epithelial integrity, innate immunity, Th17 suppression |
| **BCMO1 enzyme** | micro-micro | Converts beta-carotene to retinol; polymorphisms reduce efficiency 50–70% | Hidden insufficiency risk for plant-heavy diets; testing not standard in FDN but relevant |
| **Retinoic acid** | micro-micro | Active form; produced by Peyer's patch and MLN DCs from retinol | Simultaneous driver of class switching + homing imprinting; cannot be replaced by dietary beta-carotene in those with BCMO1 variants |
| **TGF-β** | micro-micro | Co-signal for Treg induction and IgA class switching | Produced in MLN microenvironment; MLN conditioning toward tolerance depends on this |
| **APRIL / BAFF** | micro-micro | Survival signals for plasma cells; required for IgA class switching | Chronic inflammation disrupts these → paradoxical reduction in SIgA despite immune activation |
| **IL-6** | micro-micro | Plasma cell survival in lamina propria | Disrupted by chronic inflammation |
| **Cortisol** | micro-micro | Downregulates pIgR expression directly; loads HPA; activates IDO; drives progesterone steal | Most cross-systemic variable in the entire map |
| **Bile / pancreatic lipase** | micro-micro | Required for fat-soluble vitamin absorption (A, D, E, K) | Digestive insufficiency = hidden vitamin A deficiency even with good intake |

---

### 2F. Root Cause Categories (from implicit widget structure, line 251)

| Category | Role Layer | Systems Covered |
|---|---|---|
| Nutrient / Mineral | micro | Vitamin A, zinc, magnesium, fat-soluble vitamins |
| Hormonal / HPA | macro | Cortisol, DHEA, progesterone steal, thyroid |
| Neurotransmitter | micro | Serotonin (IDO/kynurenine), dopamine (HPHPA), GABA |
| Microbiome / Gut | macro | Dysbiosis, GALT underdevelopment, estrobolome, Clostridia metabolites |
| Structural / Barrier | micro | Epithelial integrity, tight junctions, pIgR expression |
| Immune | micro | Treg/Th17 balance, SIgA, IgG/IgE class switching, innate function |
| Metabolic | macro | Mitochondrial function, oxidative stress, blood sugar stability |

---

### 2G. Visual Artifacts (Partially Produced)

| Item | Role Layer | Explicit Content | Implicit Content |
|---|---|---|---|
| **Interactive HTML root cause mapper** (line 247–263) | macro/deliverable | Every major FDN marker; upstream failure nodes by category; color-coded pills; filter by system; clickable pills | Format: single HTML file; interactive; client-facing or practitioner-facing; may need expansion to cover full FDN panel |
| **Layered interactive cortisol/DHEA map** (line 270–282) | macro/deliverable | Three tiers: upstream inputs → HPA mechanics → downstream consequences; bidirectional arrows; three ratio patterns | Built in same session; format consistent with first widget; may need to be standalone or integrated |

---

## 3. Relationships Map

```
RAW CONVERSATION
│
├── METHODOLOGY GOAL: Integrate FDN with mechanistic physiology
│   ├── Depends on: FDN marker list (complete)
│   ├── Depends on: Upstream root cause taxonomy
│   └── Depends on: Nodal reasoning logic
│
├── CENTRAL DELIVERABLE: FDN Marker → Root Cause Visual Diagram
│   ├── Input: Every FDN lab marker
│   ├── Input: Root cause categories (7 types)
│   ├── Input: Specific mechanisms per marker (conversation content)
│   └── Output: Interactive HTML widget
│
├── MARKER DEEP-DIVES (conversation content to extract)
│   ├── SIgA → 7-node axis → 6 failure points
│   ├── Cortisol/DHEA → HPA axis → 3 ratio patterns → upstream inputs
│   ├── Neurotransmitters → IDO/kynurenine, HPHPA/dopamine
│   └── (implied) Thyroid, sex hormones, gut permeability, OAT markers
│
├── VITAMIN A AXIS (cross-cutting variable)
│   ├── Affects: SIgA axis (class switching, homing)
│   ├── Affects: Epithelial barrier
│   ├── Affects: Treg/Th17 balance
│   ├── Affects: Innate immunity
│   └── Constrained by: BCMO1 polymorphism, digestive function, bile
│
└── NODAL REASONING FRAMEWORK (implied methodology extension)
    ├── Input: Pattern of multiple markers
    ├── Process: Map to most likely failed nodes
    └── Output: Prioritized intervention targets
```

---

## 4. Parameters Controlled by Each Major Item

| Item | Parameters It Controls |
|---|---|
| SIgA level | Reflects: antigen education quality, class switching efficiency, homing accuracy, plasma cell density, plasma cell output, pIgR expression, SC processing |
| Cortisol/DHEA ratio | Reflects: HPA load, adrenal reserve, upstream stressors (gut, blood sugar, sleep, trauma, infection), downstream impacts (pIgR, IDO, progesterone steal) |
| Vitamin A status | Controls: epithelial cell differentiation, IgA class switching, gut homing imprinting, Treg induction, Th17 suppression, innate immune maturation, pIgR (indirectly via epithelial health) |
| Microbiome composition | Controls: GALT maturation, IgA class switching stimulus, SIgA-mediated feedback shaping of microbiome, estrogen recirculation (estrobolome), HPHPA production (Clostridia), kynurenine/serotonin balance |
| pIgR expression | Controls: The transport bottleneck between dimeric IgA production and luminal SIgA delivery; directly suppressed by cortisol |

---

## 5. All External References

| Reference | Type | Location in Conversation |
|---|---|---|
| α4β7 integrin / CCR9 | Gut homing receptors | Lines 9, 46, 97 |
| pIgR (polymeric immunoglobulin receptor) | Transport mechanism | Lines 17, 52, 97, 127 |
| BCMO1 | Enzyme / gene | Lines 196, 197 |
| IDO (indoleamine 2,3-dioxygenase) | Enzyme | Line 257 |
| HPHPA | OAT metabolite | Line 261 |
| Estrobolome | Microbiome subpopulation | Lines 259, 260 |
| Segmented filamentous bacteria | Microbiome taxon | Line 103 |
| MAdCAM-1 / CCL25 | Adhesion molecule / chemokine | Line 97 |
| Foxp3+ Tregs | Immune cell subset | Line 176 |

---

**Gate cleared: Proceed to Step 01.**
