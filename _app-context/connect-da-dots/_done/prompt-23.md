# Prompt 23: Write JS — Variable Data: MWP + MBA Panels (6 entries)

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
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:VARIABLES:BATCH1` in `fdn-pwa/index.html` with the 6 variable entries below. These entries cover the MWP (Metabolic Wellness Panel) and MBA (Mucosal Barrier Assessment) panels.

Each variable entry follows this structure:
```javascript
'variable-id': {
  name: 'Display Name',
  panel: 'PANEL_CODE',           // 'MWP', 'MBA', 'SHP', 'GIMAP', or 'CROSS'
  panelColor: '#hexcolor',       // exact panel color from design system
  description: 'Short description',
  elevated: 'What elevated means clinically',
  low: 'What low means, or N/A string',
  connections: ['connected-variable-id'],   // other variable IDs this connects to
  clusters: ['A'],               // capital letters only
  isCrossPanel: false,           // true only for 5 cross-panel constructs
  isPriorityPathogen: false,     // true only for H. pylori
  isMedicalReferral: false       // true only for Calprotectin and Occult Blood
},
```

Panel colors (use exactly):
- MWP: `#e07c3a`
- MBA: `#3abde0`
- SHP: `#8b5cf6`
- GIMAP: `#22c55e`
- CROSS: `#94a3b8`

Write ALL 6 entries replacing `// PLACEHOLDER:VARIABLES:BATCH1`:

```javascript
    'indican': {
      name: 'Indican',
      panel: 'MWP',
      panelColor: '#e07c3a',
      description: 'Signals SIBO, dysbiosis, and protein maldigestion',
      elevated: 'Bacterial overgrowth stealing tryptophan in small intestine; liver detoxification burden from indole metabolites; protein maldigestion with bacterial fermentation of undigested protein (putrefactive dysbiosis). Correlates with slow GI transit and SIBO pattern.',
      low: 'N/A — not interpreted as low in this context',
      connections: ['urinary-bile-acids', 'ohdg', 'zonulin', 'histamine-mba', 'dao', 'sigas-shp'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'urinary-bile-acids': {
      name: 'Urinary Bile Acids',
      panel: 'MWP',
      panelColor: '#e07c3a',
      description: 'Liver detoxification throughput and bile flow marker',
      elevated: 'Liver congestion, toxin overload, or cholestasis — bile acids spilling into circulation. Associated with fat malabsorption, systemic toxin recirculation, and cholestatic itch at very high levels.',
      low: 'Poor bile flow, gallbladder dysfunction, or inflammatory bowel disease (IBD) causing bile acid malabsorption. Insufficient bile → fat and fat-soluble vitamin malabsorption → impaired GI motility signaling.',
      connections: ['hepatic-detox'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'ohdg': {
      name: '8-OHdG',
      panel: 'MWP',
      panelColor: '#e07c3a',
      description: 'DNA oxidative damage biomarker — marker of oxidative stress exceeding repair capacity',
      elevated: 'Oxidative stress exceeding cellular repair capacity. Indicates accelerated aging, increased cancer risk, mitochondrial dysfunction, and vulnerability to all degenerative conditions. High 8-OHdG predicts progression of nearly every chronic condition assessed in FDN.',
      low: 'N/A — not interpreted as low in this context',
      connections: ['oxidative-stress'],
      clusters: ['A'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'histamine-mba': {
      name: 'Histamine (MBA)',
      panel: 'MBA',
      panelColor: '#3abde0',
      description: 'Biogenic amine with immune, vascular, and neural signaling functions',
      elevated: 'Excess histamine production (from mast cell degranulation, dysbiotic bacteria, or food sources) OR impaired degradation (low DAO). Produces vascular, neurological, skin, and GI symptoms. Must be interpreted alongside DAO to determine production vs. degradation driver.',
      low: 'N/A — not interpreted as low in this context',
      connections: ['dao', 'zonulin', 'histamine-dao-system'],
      clusters: ['D'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'dao': {
      name: 'DAO (Diamine Oxidase)',
      panel: 'MBA',
      panelColor: '#3abde0',
      description: 'Primary histamine-degrading enzyme; mucosal integrity proxy',
      elevated: 'Early compensatory upregulation in response to acute mucosal injury — transiently elevated as the mucosa attempts to increase histamine clearance. This paradoxical elevation may indicate early-stage mucosal damage before enzyme depletion.',
      low: 'Chronic mucosal destruction depletes DAO-producing enterocytes. Low DAO in IBD, intestinal damage, and advanced dysbiosis. Results in histamine intolerance — inability to degrade dietary histamine, producing dose-dependent reactions to fermented and histamine-rich foods.',
      connections: ['histamine-dao-system'],
      clusters: ['D'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
    'zonulin': {
      name: 'Zonulin',
      panel: 'MBA',
      panelColor: '#3abde0',
      description: 'Intestinal tight junction regulator — the physiological gatekeeper of gut permeability',
      elevated: 'Tight junction disassembly → leaky gut → antigen translocation, LPS leak, autoimmune risk. Gliadin (wheat protein) is a direct Zonulin release trigger. Dysbiotic bacteria also trigger Zonulin. Sustained Zonulin elevation drives progressive immune sensitization and systemic inflammation.',
      low: 'N/A — not interpreted as low in this context',
      connections: ['histamine-mba', 'dao', 'sigas-shp', 'ohdg'],
      clusters: ['A', 'D'],
      isCrossPanel: false,
      isPriorityPathogen: false,
      isMedicalReferral: false
    },
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:VARIABLES:BATCH1`
- File now contains all 6 variable entry keys: `'indican'`, `'urinary-bile-acids'`, `'ohdg'`, `'histamine-mba'`, `'dao'`, `'zonulin'`
- Each entry has all required fields including `isCrossPanel`, `isPriorityPathogen`, `isMedicalReferral`
- `isCrossPanel` is `false` for all 6 entries (none are cross-panel constructs)
- The other variable batch placeholders (`BATCH2`, `BATCH3`, `BATCH4`) still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-23"`
- `pendingSteps`: remove `"step-23"`
- `flags.variablesBatch1`: set to `true`
- `artifacts.variableCount`: increment by `6`
- `dataChunks.variables.batch1`: set to `["indican","urinary-bile-acids","ohdg","histamine-mba","dao","zonulin"]`
