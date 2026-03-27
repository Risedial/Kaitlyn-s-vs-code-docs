# Prompt 18: Write JS — Symptom Data: Digestion Category (10 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:SYMPTOMS:BATCH3` in `fdn-pwa/index.html` with the 10 Digestion symptom entries below.

**IMPORTANT**: Several digestion symptoms include `hpylori` in their variables array. The renderSymptom() function (added in a later step) will check for `hpylori` in the variables array and render a red alert banner before the variable pills section for those symptoms.

Write ALL 10 entries replacing `// PLACEHOLDER:SYMPTOMS:BATCH3`:

```javascript
    'bloating': {
      label: 'Bloating',
      category: 'Digestion',
      variables: ['indican', 'hpylori', 'candida', 'dysbiotic-bacteria', 'dao', 'histamine-mba', 'anti-gliadin-iga', 'sigas-gi'],
      clusters: ['A', 'D'],
      interpretation: 'Bloating is the most common multi-driver GI symptom and requires systematic source discrimination. Upper GI bloating appearing within 30–60 minutes of eating typically indicates SIBO (Indican elevated) or H. pylori-driven hypochlorhydria. Lower GI bloating appearing hours after eating indicates dysbiotic fermentation. Histamine-driven bloating is distinguished by accompanying histamine symptoms (flushing, headache). Anti-gliadin IgA elevation suggests gluten-reactive mucosal inflammation contributing to distension.',
      mechanismTree: 'H. pylori (if positive)\n└─ Gastric acid disruption → bacterial overgrowth of upper GI\n   └─ Fermentation gases → upper GI bloating + early satiety\nIndican (SIBO/dysbiosis)\n└─ Bacterial gas production in small intestine\n   └─ Abdominal distension, pain, altered motility\nHistamine + low DAO\n└─ Histamine-driven smooth muscle spasm\n   └─ Gut distension without gas production\nAnti-gliadin IgA (elevated)\n└─ Gluten-reactive mucosal inflammation → villous disruption\n   └─ Malabsorption → osmotic load → bloating'
    },
    'gas-flatulence': {
      label: 'Gas / flatulence (especially foul-smelling)',
      category: 'Digestion',
      variables: ['indican', 'hpylori', 'dysbiotic-bacteria', 'parasites'],
      clusters: ['A'],
      interpretation: 'Foul-smelling gas specifically — as opposed to normal dietary gas — indicates putrefactive dysbiosis: bacterial fermentation of undigested protein rather than carbohydrate. Indican is the direct biomarker for this mechanism (protein putrefaction by bacteria). H. pylori disrupts gastric acid, allowing bacteria to colonize regions where acid normally provides sterilization. Dysbiotic bacteria produce hydrogen sulfide and skatole — the compounds responsible for foul odor. Parasitic infection should be evaluated when accompanied by alternating stool consistency.',
      mechanismTree: 'Indican (putrefactive dysbiosis)\n└─ Bacterial catabolism of undigested protein → hydrogen sulfide, skatole\n   └─ Foul-smelling gas — distinguishing feature of protein putrefaction vs. carbohydrate fermentation\nH. pylori (gastric acid disruption)\n└─ Hypochlorhydria → small intestinal bacterial colonization\n   └─ Bacterial fermentation in wrong location → early, excessive gas\nDysbiotic Bacteria\n└─ Sulfur-reducing bacteria overgrowth\n   └─ Hydrogen sulfide production → foul odor, gut motility disruption'
    },
    'constipation': {
      label: 'Constipation',
      category: 'Digestion',
      variables: ['indican', 'urinary-bile-acids', 'dysbiotic-bacteria', 'cortisol-diurnal'],
      clusters: ['A', 'B'],
      interpretation: 'Constipation in the FDN model requires discrimination between two primary mechanisms: hypomotility-driven (nervous system and bile acid) vs. dysbiosis-driven (microbiome composition). Indican elevation signals hypomotility — when transit is slow, bacteria have more time to steal amino acids. Urinary Bile Acids low signals poor bile flow (from gallbladder dysfunction or hepatic congestion), and bile acids are primary drivers of colonic motility. Cortisol dysregulation contributes via the HPA-gut axis: elevated cortisol suppresses gut motility through CRH receptor activation in the colon.',
      mechanismTree: 'Urinary Bile Acids (low — poor bile flow)\n└─ Bile acids are direct colonic secretagogues and motility drivers\n   └─ Reduced bile → slowed colonic transit → constipation\nIndican (elevated — slow transit signal)\n└─ Prolonged transit time → increased bacterial tryptophan theft\n   └─ Circular: dysbiosis worsens hypomotility\nCortisol Dysregulation\n└─ HPA-gut axis: elevated cortisol → CRH receptor activation in colon\n   └─ Smooth muscle inhibition → motility reduction'
    },
    'diarrhea': {
      label: 'Diarrhea',
      category: 'Digestion',
      variables: ['hpylori', 'parasites', 'candida', 'calprotectin', 'zonulin', 'sigas-gi'],
      clusters: ['A', 'D', 'E'],
      interpretation: 'Diarrhea requires immediate source stratification. Calprotectin/Lactoferrin elevation indicates active intestinal inflammation requiring MEDICAL REFERRAL — this is not a functional GI pattern. Parasitic infection produces osmotic diarrhea via villous destruction. H. pylori drives secretory diarrhea via VacA toxin disruption of gastric acid and downstream small intestinal dysfunction. Zonulin elevation indicates tight junction disruption with osmotic fluid leak. Low sIgA-GI reflects immune collapse that allows pathogens to persist.',
      mechanismTree: 'Calprotectin/Lactoferrin (if elevated)\n└─ STOP: Active intestinal inflammation — MEDICAL REFERRAL REQUIRED\n   └─ Do not apply FDN interventions until physician evaluates for IBD/structural pathology\nH. pylori + Parasites\n└─ Secretory and osmotic diarrhea mechanisms\n   └─ Villous destruction → malabsorption → osmotic diarrhea\nZonulin (tight junction disruption)\n└─ Fluid leak into intestinal lumen\n   └─ Secretory component → loose, frequent stools\nsIgA-GI (low — immune collapse)\n└─ Pathogen persistence → chronic infectious diarrhea pattern'
    },
    'alternating-constipation-diarrhea': {
      label: 'Alternating constipation and diarrhea',
      category: 'Digestion',
      variables: ['hpylori', 'dysbiotic-bacteria', 'zonulin', 'sigas-gi', 'indican'],
      clusters: ['A', 'D'],
      interpretation: 'Alternating bowel habit is the IBS-pattern presentation in FDN and typically reflects dysbiosis-driven motility dysregulation rather than a functional disorder. H. pylori disrupts gastric acid → impaired small intestinal sterilization → dysbiosis → erratic motility pattern. Dysbiotic bacterial populations produce both motility-slowing (methane) and motility-stimulating (hydrogen) gases, creating alternating patterns. Zonulin elevation adds a leak-driven secretory component that produces episodic diarrhea interspersed with hypomotility constipation phases.',
      mechanismTree: 'H. pylori → Dysbiotic Bacteria\n└─ Methane-producing organisms → hypomotility (constipation phase)\n└─ Hydrogen-producing organisms → hypermotility (diarrhea phase)\n   └─ Alternating dominance creates oscillating bowel pattern\nZonulin (tight junction disruption)\n└─ Episodic intestinal permeability spikes → secretory diarrhea events\nIndican (dysbiosis marker)\n└─ Confirms bacterial fermentation substrate for alternating gas types'
    },
    'heartburn-reflux': {
      label: 'Heartburn / reflux',
      category: 'Digestion',
      variables: ['hpylori', 'indican', 'urinary-bile-acids'],
      clusters: ['A'],
      interpretation: 'Heartburn and reflux in the FDN model are commonly driven by hypochlorhydria rather than hyperacidity — a counterintuitive mechanism. H. pylori infection directly suppresses gastric acid secretion via ammonia production, leading to incomplete protein digestion, bacterial overgrowth of the stomach, and elevated intra-gastric pressure from fermentation gases pushing content into the esophagus. Indican elevation confirms the resulting SIBO. Urinary Bile Acids can be elevated when bile acid reflux (duodeno-gastric reflux) contributes to the presentation.',
      mechanismTree: 'H. pylori (primary driver)\n└─ Ammonia production → gastric acid neutralization\n   └─ Hypochlorhydria → elevated intra-gastric fermentation pressure\n      └─ LES pressure overwhelmed → reflux of fermentation gases\nIndican (SIBO/dysbiosis)\n└─ Confirms bacterial overgrowth from hypochlorhydric environment\n   └─ Gas pressure amplifies reflux events\nUrinary Bile Acids (if elevated)\n└─ Duodeno-gastric bile reflux component\n   └─ Bile acid damage to gastric mucosa → worsened acid sensitivity'
    },
    'nausea': {
      label: 'Nausea',
      category: 'Digestion',
      variables: ['hpylori', 'parasites', 'histamine-mba', 'urinary-bile-acids'],
      clusters: ['A', 'D'],
      interpretation: 'Nausea requires differentiating pathogen-driven from histamine-driven from bile-driven mechanisms. H. pylori-associated nausea is characteristically worse in the morning or on an empty stomach and improves after eating (due to food buffering gastric acid). Parasitic infection-associated nausea accompanies GI urgency and alternating stool changes. Histamine-mediated nausea is vasoactive and often accompanies flushing and headache. Elevated Urinary Bile Acids (hepatic congestion) produces nausea via bile acid recirculation, particularly worse after fatty meals.',
      mechanismTree: 'H. pylori\n└─ VacA cytotoxin → gastric epithelial injury\n   └─ Morning nausea, empty-stomach worsening, food-relief pattern\nHistamine-MBA (elevated)\n└─ H3 receptor activation → enteric nervous system sensitization\n   └─ Vasoactive nausea — accompanies flushing/headache\nUrinary Bile Acids (elevated — hepatic congestion)\n└─ Bile acid reflux into stomach\n   └─ Post-fatty-meal nausea, bloating, bile taste'
    },
    'food-sits-there': {
      label: 'Food feels like it just sits there',
      category: 'Digestion',
      variables: ['indican', 'hpylori', 'urinary-bile-acids'],
      clusters: ['A'],
      interpretation: 'Gastroparesis-like symptoms — the sensation of food sitting in the stomach for hours — reflect hypomotility of the upper GI tract. H. pylori infection damages the interstitial cells of Cajal (the pacemaker cells of gastric motility) and produces the VacA toxin that disrupts gastric epithelial integrity. Low Urinary Bile Acids indicates insufficient bile flow, impacting fat digestion and CCK-mediated gastric emptying signals. Indican elevation is the downstream confirmation: when gastric emptying is slow, bacteria have prolonged access to protein substrate for fermentation.',
      mechanismTree: 'H. pylori (motility disruption)\n└─ Cajal cell damage + VacA toxin → gastric emptying impaired\n   └─ Gastroparesis-like pattern: early satiety, prolonged fullness\nUrinary Bile Acids (low — poor bile flow)\n└─ Reduced CCK stimulation → impaired gallbladder contraction\n   └─ Fat digestion stall → gastric emptying delayed\nIndican (elevated downstream)\n└─ Slow transit → extended bacterial access to protein → fermentation gases\n   └─ Distension and pressure sensation amplify "sitting" feeling'
    },
    'stomach-pain-cramping': {
      label: 'Stomach pain / cramping',
      category: 'Digestion',
      variables: ['hpylori', 'parasites', 'calprotectin', 'histamine-mba', 'zonulin'],
      clusters: ['A', 'D', 'E'],
      interpretation: 'Abdominal pain and cramping requires urgent stratification. Calprotectin/Lactoferrin elevation is a MEDICAL REFERRAL trigger — active neutrophilic gut inflammation may indicate Crohn\'s disease, ulcerative colitis, or infectious colitis requiring physician evaluation before FDN interventions. H. pylori produces gnawing epigastric pain, characteristically improved by eating but worsening 2–3 hours after meals. Histamine-driven cramping is smooth muscle spasm responding to mast cell degranulation. Zonulin-driven pain reflects tight junction disruption with associated mucosal stretch and pain signaling.',
      mechanismTree: 'Calprotectin/Lactoferrin (if elevated)\n└─ STOP: Active intestinal neutrophilic inflammation — MEDICAL REFERRAL REQUIRED\n   └─ Physician evaluation required before any FDN intervention\nH. pylori\n└─ Gastric mucosal ulceration → gnawing epigastric pain\n   └─ 2–3 hour post-meal worsening pattern\nHistamine-MBA (elevated)\n└─ Mast cell degranulation → gut smooth muscle spasm\n   └─ Cramping without structural change\nZonulin (tight junction disruption)\n└─ Mucosal stretch pain signaling\n   └─ Diffuse abdominal cramping after meals'
    },
    'cant-eat-without-sick': {
      label: "Can't eat without feeling sick",
      category: 'Digestion',
      variables: ['hpylori', 'anti-gliadin-iga', 'zonulin', 'dao', 'histamine-mba'],
      clusters: ['A', 'D'],
      interpretation: 'Consistent post-meal illness — regardless of what is eaten — indicates that the act of eating itself is triggering a systemic reaction, not a specific food intolerance. H. pylori infection creates a situation where gastric acid is suppressed and any food bolus becomes a fermentation substrate. When Anti-gliadin IgA is elevated alongside Zonulin, eating triggers acute tight junction disassembly and LPS translocation — producing systemic malaise post-meal. Low DAO means histamine from foods cannot be degraded, so any meal with histamine content triggers immediate reactions.',
      mechanismTree: 'H. pylori (gastric environment disruption)\n└─ Any food bolus → fermentation substrate in hypochlohydric stomach\n   └─ Post-meal gas, bloating, nausea — food-independent\nAnti-gliadin IgA + Zonulin (food-triggered barrier disruption)\n└─ Eating → IgA immune activation → tight junction signaling cascade\n   └─ Acute LPS translocation → systemic malaise after every meal\nLow DAO (histamine cannot be degraded)\n└─ Dietary histamine absorbed intact\n   └─ Dose-dependent post-meal histamine reaction'
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:SYMPTOMS:BATCH3`
- File now contains all 10 entry keys: `'bloating'`, `'gas-flatulence'`, `'constipation'`, `'diarrhea'`, `'alternating-constipation-diarrhea'`, `'heartburn-reflux'`, `'nausea'`, `'food-sits-there'`, `'stomach-pain-cramping'`, `'cant-eat-without-sick'`
- Each entry has all 6 required fields
- `'diarrhea'` and `'stomach-pain-cramping'` entries include `'calprotectin'` in their variables arrays
- `'bloating'`, `'diarrhea'`, `'stomach-pain-cramping'`, and `'cant-eat-without-sick'` include `'hpylori'` in their variables arrays
- The other symptom batch placeholders (`BATCH4` through `BATCH7`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-18"`
- `pendingSteps`: remove `"step-18"`
- `flags.symptomsBatch3`: set to `true`
- `artifacts.symptomCount`: increment by `10`
- `dataChunks.symptoms.batch3`: set to `["bloating","gas-flatulence","constipation","diarrhea","alternating-constipation-diarrhea","heartburn-reflux","nausea","food-sits-there","stomach-pain-cramping","cant-eat-without-sick"]`
