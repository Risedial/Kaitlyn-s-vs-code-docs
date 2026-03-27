use @universal-research-system/knowledge-map.md &  @universal-research-system/session-outputs/2026-03-24-synthesis-0.md to execute this prompt: You are building a mobile-first HTML symptom navigation tool for a functional medicine knowledge system containing 33 validated lab variables and 463 connections. Your source of truth is the knowledge base I've described below. Build a single self-contained HTML file — no external dependencies, no frameworks, inline CSS and JS only.

---

## KNOWLEDGE SYSTEM OVERVIEW

The system contains 33 FDN lab marker variables organized across 5 panels:
- MWP (Metabolic Wellness Panel): Indican, Urinary Bile Acids, 8-OHdG
- MBA (Mucosal Barrier Assessment): Histamine, DAO, Zonulin
- SHP (Stress Hormone Panel): Cortisol Diurnal Pattern, DHEA, Testosterone, Estradiol, Progesterone, Melatonin, sIgA-SHP
- GI-MAP: H. pylori, Candida, Parasites, Dysbiotic Bacteria, Commensal Bacteria, Calprotectin/Lactoferrin, Beta-glucuronidase, Anti-gliadin IgA, sIgA-GI, Occult Blood
- Cross-panel constructs: Systemic Oxidative Stress Cascade, Hepatic Detoxification Impairment, Histamine-DAO Regulatory System, HPA Axis Dysregulation Pattern, Pregnenolone Steal and Steroidogenesis Disruption

Five root cause clusters exist:
- Cluster A — GI Ecosystem Collapse (Primary Driver)
- Cluster B — HPA-Immune Loop (Amplifier)
- Cluster C — Estrogen Recycling Loop (Cross-Panel)
- Cluster D — Mucosal Barrier Breakdown (Histamine)
- Cluster E — Structural GI Pathology (Medical Referral)

---

## SYMPTOM-TO-VARIABLE MAPPING

Build the following symptom library. Each symptom must link to every variable that can produce it and every root cause cluster involved. This is the full mapping — encode it exactly.

### ENERGY & FATIGUE
- "Always tired" → Cortisol Diurnal Pattern, DHEA, HPA Axis Dysregulation, sIgA-SHP, Indican, 8-OHdG, Hepatic Detox Impairment | Clusters A, B
- "Afternoon energy crash" → Cortisol Diurnal Pattern, Blood Glucose Dysregulation, Indican | Cluster B
- "Can't get out of bed in the morning" → Cortisol Diurnal Pattern, DHEA, Melatonin | Cluster B
- "Wired but tired" → Cortisol Diurnal Pattern, HPA Axis Dysregulation, Melatonin | Cluster B
- "Exercise makes me worse" → 8-OHdG, Systemic Oxidative Stress Cascade, DHEA, Cortisol | Clusters A, B
- "No motivation or drive" → DHEA, Testosterone, HPA Axis Dysregulation, Indican (neurotransmitter depletion) | Clusters A, B

### SLEEP
- "Can't fall asleep" → Melatonin, Cortisol Diurnal Pattern, HPA Axis Dysregulation, Histamine-MBA | Clusters B, D
- "Wake up between 1–3am" → Cortisol Diurnal Pattern, Blood Glucose Dysregulation, Hepatic Detox Impairment | Clusters A, B
- "Never feel rested" → Melatonin, Cortisol Diurnal Pattern, 8-OHdG, Histamine-MBA | Clusters B, D
- "Vivid dreams or nightmares" → HPA Axis Dysregulation, Cortisol Diurnal Pattern | Cluster B
- "Need 10+ hours and still tired" → HPA Axis Dysregulation Exhaustion Phase, DHEA, sIgA-SHP | Cluster B

### MOOD & EMOTIONS
- "Anxiety" → Histamine-MBA, DAO, HPA Axis Dysregulation, Indican (tryptophan depletion → serotonin deficit), Zonulin (LPS-driven neuroinflammation), Cortisol | Clusters A, B, D
- "Depression" → Indican (neurotransmitter depletion via tryptophan theft), HPA Axis Dysregulation, DHEA, Testosterone, 8-OHdG, Systemic Oxidative Stress | Clusters A, B
- "Irritability / short fuse" → Histamine-MBA, Cortisol Diurnal Pattern, Blood Glucose Dysregulation, HPA Axis Dysregulation | Clusters B, D
- "Emotional numbness" → HPA Axis Dysregulation Exhaustion Phase, DHEA, Cortisol (flat pattern) | Cluster B
- "Overwhelm / can't cope with stress" → HPA Axis Dysregulation, sIgA-SHP, Cortisol:DHEA ratio, Pregnenolone Steal | Cluster B
- "Mood swings" → Estradiol, Progesterone, Cortisol Diurnal Pattern, Histamine-MBA, Blood Glucose Dysregulation | Clusters B, C, D
- "Brain fog" → Zonulin (LPS translocation), Indican (amino acid depletion), 8-OHdG, Hepatic Detox Impairment, Histamine-MBA, DAO | Clusters A, B, D
- "Poor memory" → Indican (tryptophan/neurotransmitter depletion), 8-OHdG, Systemic Oxidative Stress, HPA Axis Dysregulation | Clusters A, B
- "Feeling disconnected from yourself" → HPA Axis Dysregulation Collapse Phase, sIgA-SHP, Cortisol flat pattern | Cluster B

### DIGESTION
- "Bloating" → Indican (SIBO/dysbiosis), H. pylori, Candida, Dysbiotic Bacteria, DAO-low, Histamine-MBA, Anti-gliadin IgA, sIgA-GI | Clusters A, D
- "Gas / flatulence (especially foul-smelling)" → Indican (putrefactive dysbiosis), H. pylori, Dysbiotic Bacteria, Parasites | Cluster A
- "Constipation" → Indican (hypomotility signal), Urinary Bile Acids (low = poor bile flow), Dysbiotic Bacteria, Cortisol | Clusters A, B
- "Diarrhea" → H. pylori, Parasites, Candida, Calprotectin/Lactoferrin, Zonulin, sIgA-GI | Clusters A, D, E
- "Alternating constipation and diarrhea" → H. pylori, Dysbiotic Bacteria, Zonulin, sIgA-GI, Indican | Clusters A, D
- "Heartburn / reflux" → H. pylori (disrupts gastric acid), Indican (hypochlorhydria signal), Urinary Bile Acids | Cluster A
- "Nausea" → H. pylori, Parasites, Histamine-MBA, Urinary Bile Acids (high) | Clusters A, D
- "Food feels like it just sits there" → Indican (hypomotility), H. pylori, Urinary Bile Acids (low bile flow) | Cluster A
- "Stomach pain / cramping" → H. pylori, Parasites, Calprotectin/Lactoferrin, Histamine-MBA, Zonulin | Clusters A, D, E
- "Can't eat without feeling sick" → H. pylori, Anti-gliadin IgA, Zonulin, DAO-low, Histamine load | Clusters A, D

### FOOD REACTIONS
- "Reactions to many foods" → Zonulin (leaky gut → systemic antigen load), DAO-low, Histamine-MBA, Anti-gliadin IgA, sIgA-GI, MRT reactive foods | Clusters A, D
- "Gluten sensitivity" → Anti-gliadin IgA, Zonulin, sIgA-GI (interpretation dependency), Histamine-MBA | Clusters A, D
- "Dairy reactions" → Anti-gliadin IgA (cross-reactive: dairy shares gliadin homology), Zonulin, DAO | Clusters A, D
- "Histamine-rich food reactions (wine, aged cheese, fermented foods)" → Histamine-MBA, DAO, Histamine-DAO Regulatory System | Cluster D
- "Getting worse after eating fermented foods or probiotics" → Histamine-MBA, DAO-low, SIBO (Indican) | Cluster D

### SKIN
- "Hives / urticaria" → Histamine-MBA, DAO-low, Zonulin, Histamine-DAO Regulatory System | Cluster D
- "Eczema / rashes" → Histamine-MBA, Zonulin (leaky gut antigen load), Anti-gliadin IgA, sIgA-GI | Clusters A, D
- "Flushing / redness (especially face)" → Histamine-MBA, DAO-low, Estradiol | Clusters C, D
- "Itching (no visible rash)" → Histamine-MBA, DAO, Urinary Bile Acids (high — bile salt itch) | Clusters A, D
- "Acne" → Estradiol (elevated), Progesterone (low), Beta-glucuronidase, HPA Axis Dysregulation, Hepatic Detox Impairment | Clusters B, C
- "Skin that ages fast" → 8-OHdG, Systemic Oxidative Stress Cascade | Clusters A, B

### IMMUNE SYSTEM
- "Get sick constantly" → sIgA-SHP (low), sIgA-GI (low), HPA Axis Dysregulation, Cortisol (immune suppression) | Clusters A, B
- "Take forever to recover from illness" → sIgA-SHP, DHEA, Systemic Oxidative Stress, Hepatic Detox Impairment | Clusters A, B
- "Allergies getting worse over time" → sIgA-GI, Zonulin, Histamine-MBA, DAO | Clusters A, D
- "Autoimmune condition or suspicion" → Zonulin (sustained TJ disassembly → antigen translocation → autoimmune activation), 8-OHdG, Systemic Oxidative Stress | Clusters A, B
- "Frequent UTIs, yeast infections, or infections" → Candida, sIgA-GI (low), HPA Axis Dysregulation, Cortisol | Clusters A, B

### HORMONAL (FEMALE)
- "PMS / PMDD" → Estradiol (elevated), Progesterone (low), Beta-glucuronidase (recycling estrogen), HPA Axis Dysregulation, Cortisol:DHEA ratio | Clusters B, C
- "Irregular periods" → Estradiol, Progesterone, Cortisol, HPA Axis Dysregulation, Pregnenolone Steal | Clusters B, C
- "Heavy periods" → Estradiol (elevated), Progesterone (low), Beta-glucuronidase | Cluster C
- "Low libido" → Testosterone (low), DHEA, HPA Axis Dysregulation, Pregnenolone Steal, Indican (amino acid depletion) | Clusters A, B
- "Hot flashes" → Estradiol dysregulation, Histamine-MBA (histamine triggers vasodilation), Progesterone (low), HPA | Clusters B, C, D
- "Infertility or difficulty conceiving" → Progesterone (low), Estradiol imbalance, HPA Axis, Pregnenolone Steal, Beta-glucuronidase | Clusters B, C
- "Estrogen dominance symptoms (weight in hips, painful breasts, water retention)" → Estradiol (elevated), Beta-glucuronidase (recycling), Progesterone (low), Hepatic Detox Impairment | Cluster C

### HORMONAL (MALE & SHARED)
- "Low testosterone symptoms (low drive, muscle loss, fatigue)" → Testosterone (low), DHEA, HPA Axis Dysregulation, Pregnenolone Steal, Indican | Clusters A, B
- "Can't build or maintain muscle" → Testosterone (low), DHEA, Cortisol (catabolic), HPA Axis Dysregulation | Cluster B
- "Weight gain despite diet/exercise" → Cortisol (elevated, promotes fat storage), Estradiol (elevated via B-GUS recycling), Indican (metabolic disruption), Urinary Bile Acids | Clusters A, B, C

### CARDIOVASCULAR & CIRCULATORY
- "Heart palpitations / racing heart" → Histamine-MBA (cardiac H2 receptor activation), DAO-low, Cortisol, HPA Axis Dysregulation | Clusters B, D
- "Low blood pressure / dizziness on standing" → HPA Axis Dysregulation Exhaustion Phase, DHEA (low), Cortisol (flat) | Cluster B
- "High blood pressure" → Cortisol (elevated), Histamine (vasoconstriction paradox), Systemic Oxidative Stress | Clusters B, D

### PAIN & INFLAMMATION
- "Joint pain" → Zonulin (antigen translocation → immune complex deposition), 8-OHdG, Systemic Oxidative Stress, DAO-low | Clusters A, D
- "Muscle aches without exertion" → Systemic Oxidative Stress, 8-OHdG, HPA Axis Dysregulation, Cortisol (catabolic) | Clusters A, B
- "Headaches" → Histamine-MBA (vasodilation), DAO-low, Zonulin, Indican (neurotransmitter depletion), Cortisol | Clusters A, B, D
- "Migraines" → Histamine-MBA, DAO-low, Estradiol (hormonal trigger), HPA Axis, Zonulin | Clusters B, C, D
- "Fibromyalgia-like symptoms" → 8-OHdG, Systemic Oxidative Stress, HPA Axis Dysregulation, Indican (amino acid depletion) | Clusters A, B
- "Chronic pain" → Systemic Oxidative Stress Cascade, 8-OHdG, Zonulin, HPA Axis Dysregulation | Clusters A, B

### RESPIRATORY
- "Stuffy nose / runny nose (not seasonal)" → Histamine-MBA, DAO-low, Zonulin (antigen translocation), Anti-gliadin IgA | Clusters A, D
- "Asthma-like symptoms" → Histamine-MBA (H1 bronchospasm), DAO-low, Zonulin | Cluster D
- "Post-nasal drip" → Histamine-MBA, DAO, Zonulin | Cluster D

### COGNITIVE & NEUROLOGICAL
- "Difficulty concentrating" → Indican (tryptophan/neurotransmitter depletion), 8-OHdG, Histamine-MBA, Zonulin (LPS neuroinflammation) | Clusters A, D
- "Word-finding problems" → 8-OHdG, Systemic Oxidative Stress, Indican, Zonulin | Clusters A, B
- "Sensitivity to light or sound" → Histamine-MBA, DAO-low, HPA Axis Dysregulation | Clusters B, D
- "Tingling or numbness" → 8-OHdG (nerve oxidative damage), Systemic Oxidative Stress | Cluster A

### STRESS & NERVOUS SYSTEM
- "Can't handle stress the way I used to" → HPA Axis Dysregulation (Phase 3+ Exhaustion), Cortisol:DHEA ratio, sIgA-SHP, DHEA (low) | Cluster B
- "Burnout" → HPA Axis Dysregulation Exhaustion/Collapse Phase, Cortisol (flat), DHEA, sIgA-SHP | Cluster B
- "Panic attacks" → Histamine-MBA (acute vasoactive release), HPA Axis Dysregulation, Cortisol | Clusters B, D
- "Feel like I can't relax" → HPA Axis Dysregulation, Cortisol (elevated), Histamine-MBA, Melatonin (low) | Clusters B, D

---

## VARIABLE REFERENCE PANEL

For each variable, build a detail card with:
- Variable name (exact)
- Plain language description (1–2 sentences max)
- What it means when elevated
- What it means when low/deficient
- Root cause clusters it belongs to
- Connected variables (list names only)

Use this data:

Indican | Signals SIBO, dysbiosis, protein maldigestion | High: bacterial overgrowth stealing tryptophan, liver burden | Low: n/a | Clusters A | Connects to: Urinary Bile Acids, 8-OHdG, Zonulin, Histamine-MBA, DAO, sIgA-SHP

Urinary Bile Acids | Liver detoxification throughput marker | High: liver congestion, toxin overload | Low: poor bile flow, gallbladder dysfunction, IBD | Cluster A | Connects to: Hepatic Detox Impairment

8-OHdG | DNA oxidative damage biomarker | High: oxidative stress exceeding repair = accelerated aging, cancer risk | Cluster A | Connects to: Systemic Oxidative Stress Cascade

Zonulin | Intestinal tight junction regulator | High: leaky gut, antigen translocation, autoimmune risk | Cluster A, D | Connects to: Histamine-MBA, DAO, sIgA-SHP, 8-OHdG

Histamine-MBA | Biogenic amine: immune, vascular, neural functions | High: excess production or impaired degradation | Cluster D | Connects to: DAO, Zonulin, Histamine-DAO Regulatory System

DAO | Histamine-degrading enzyme, mucosal integrity proxy | High: early injury compensatory upregulation | Low: chronic mucosal destruction, IBD | Cluster D | Connects to: Histamine-DAO Regulatory System

sIgA-SHP | Salivary mucosal immune defense | Low: cortisol suppression, chronic stress, immune collapse | High: active acute immune challenge | Cluster B | Connects to: HPA Axis Dysregulation

HPA Axis Dysregulation | Adrenal stress response cascade (5 phases) | All phases: progressive cortisol dysregulation driving downstream immune, sex hormone, sleep deficits | Cluster B | Connects to: Cortisol Diurnal Pattern, DHEA, sIgA-SHP, Pregnenolone Steal

Pregnenolone Steal (regulatory downregulation) | Mechanism reducing DHEA/sex hormones under cortisol demand | Active: DHEA, testosterone, progesterone all suppressed while cortisol elevated | Cluster B | Connects to: DHEA, Testosterone, Estradiol, Progesterone

Cortisol Diurnal Pattern | 4-point salivary cortisol arc | Flat: exhaustion/collapse | Elevated: acute/compensatory stress | Low overall: adrenal exhaustion | Cluster B

DHEA | Anabolic counterbalance to cortisol | Low: catabolic dominance, immune suppression, aging acceleration | Cluster B

Testosterone | Anabolic hormone (male primary, female secondary) | Low: fatigue, low libido, muscle loss, depression | Cluster B

Estradiol | Primary estrogen | Elevated: Cluster C estrogen recycling via B-GUS | Low: menopause, HPA suppression | Cluster C

Progesterone | Anti-estrogenic, calming hormone | Low: anxiety, poor sleep, heavy periods, infertility | Cluster C

Melatonin | Circadian rhythm hormone | Noon elevation: GI dysbiosis signal | Low: insomnia, poor antioxidant capacity | Cluster B

H. pylori | Ulcerogenic gastric pathogen | Positive: treat first — disrupts all other colonization resistance | Cluster A

Candida | Opportunistic yeast | Elevated: dysbiosis, immune suppression | Cluster A

Parasites | GI parasitic load | Positive: immune activation, barrier disruption | Cluster A

Dysbiotic Bacteria | Pathobiont bacterial overgrowth | Elevated: drives indican, B-GUS, histamine excess | Cluster A

Commensal Bacteria | Beneficial microbiome | Low: SCFA deficit, sIgA suppression, immune dysregulation | Cluster A

Calprotectin/Lactoferrin | Neutrophil-derived GI inflammation marker | Elevated: active IBD, distinguish from functional GI disorders | Cluster E

Beta-glucuronidase | Bacterial enzyme deconjugating estrogens/toxins | Elevated: estrogen recycling loop, hormone disruption, toxic recirculation | Cluster C | Connects to: Estradiol, Hepatic Detox Impairment

Anti-gliadin IgA | Local mucosal immune response to gliadin | Elevated: gluten/cross-reactive reactivity | Low with low sIgA: likely false negative | Cluster A | Connects to: sIgA-GI

sIgA-GI | Stool mucosal immune defense | Low: chronic pathogen load, dysbiosis, immune collapse | Elevated: acute immune challenge | Cluster A, B

Occult Blood | Fecal hemoglobin, structural mucosal bleeding marker | >10 ug/g: medical referral required immediately | Cluster E

Systemic Oxidative Stress Cascade | Overarching amplifier of all dysfunction | Active: accelerates every other dysregulation simultaneously | All clusters

Hepatic Detoxification Impairment | Liver Phase I/II/III overwhelm | Active: toxin and hormone recirculation, bile acid spillover | Cluster A, C

Histamine-DAO Regulatory System | Functional balance of histamine load vs degradation capacity | Disrupted: histamine intolerance — use Histamine:DAO ratio | Cluster D

---

## UI REQUIREMENTS

**Layout:**
- Mobile-first. Max-width 430px, centered on desktop.
- Dark background (#0f0f12), card-based design.
- No external libraries, no CDN dependencies.
- Single HTML file, everything inline.

**Home screen:**
- Title: "What are you experiencing?"
- Search bar at top (filters symptom list in real-time)
- Symptom cards organized into collapsible category sections:
  Energy & Fatigue | Sleep | Mood & Emotions | Digestion | Food Reactions | Skin | Immune System | Hormonal | Pain & Inflammation | Respiratory | Cognitive & Neurological | Stress & Nervous System | Cardiovascular
- Each symptom is a tappable card

**Symptom detail screen (shown when symptom is tapped):**
- Back button
- Symptom name as header
- Section: "Possible Variables" — each variable listed as a tappable pill/badge. Color-coded by panel (MWP=orange, MBA=teal, SHP=purple, GI-MAP=green, Cross-panel=gray)
- Section: "Root Cause Clusters" — show all clusters implicated as colored tags
- Section: "What This Means" — 2-3 sentence plain-language interpretation of what these variables collectively suggest

**Variable detail screen (shown when variable pill is tapped from symptom screen):**
- Back button (returns to symptom)
- Variable name as header
- Panel badge
- What it is (plain language, 1-2 sentences)
- When elevated / when low sections
- "Connected Variables" — tappable pills linking to those variable cards
- "Root Cause Clusters" — which clusters this variable participates in
- "Commonly co-elevated with" — list variables that are mechanistically linked

**Root cause cluster detail (tappable from any cluster tag):**
- Cluster name and letter
- Plain language description
- Which variables indicate this cluster
- What symptoms this cluster produces (reverse map)
- Priority note (e.g., Cluster A: treat before all others)

**Navigation:**
- All navigation is push-state (no page reloads)
- Smooth slide transitions between screens
- Persistent bottom nav: Home | Search | Clusters (3 tabs)

**Search:**
- Real-time filtering across all symptoms AND variable names simultaneously
- Results grouped: Symptoms | Variables

**Color system:**
- MWP (Metabolic Wellness Panel): #e07c3a (amber)
- MBA (Mucosal Barrier Assessment): #3abde0 (teal)  
- SHP (Stress Hormone Panel): #8b5cf6 (purple)
- GI-MAP: #22c55e (green)
- Cross-panel constructs: #94a3b8 (slate)
- Cluster A: #ef4444 (red)
- Cluster B: #f97316 (orange)
- Cluster C: #ec4899 (pink)
- Cluster D: #06b6d4 (cyan)
- Cluster E: #fbbf24 (amber/warning)

**Typography:**
- System font stack. Headings bold. Body 15px. Cards have 16px padding. Generous line-height (1.6).

**Interactions:**
- Tap a symptom → symptom detail
- Tap a variable pill → variable detail
- Tap a cluster tag → cluster detail
- Back button → previous screen
- All state managed in JS (no reload)
- Active states on all tappable elements

**Performance:**
- All data embedded as a JS object at the top of the script
- No fetches, no APIs, no storage
- Loads instantly

---

## ADDITIONAL REQUIREMENT: HIERARCHY DISPLAY

On the symptom detail screen, after listing variables, show a visual hierarchy using indentation or arrows:

SURFACE SYMPTOM
  └─ Immediate mechanism variable (e.g., Histamine-MBA)
      └─ Root driver variable (e.g., Indican → SIBO)
          └─ Deepest upstream cause (e.g., H. pylori, Candida, HPA Dysregulation)

Keep this as a text-tree, no canvas/SVG needed. This gives users the sense of drilling from symptom → mechanism → root cause.

---

Build the complete file. Do not truncate. Include all symptoms and all variables from the mapping above. The goal is that someone can pick any sensation they're experiencing and trace it to its deepest physiological root cause cluster.