# Prompt 15: Write JS — DATA Object Skeleton with Nested Placeholders

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: `htmlShellWritten`
- Files that MUST already exist: `fdn-pwa/index.html` (shell from step-04)

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
Use the Edit tool to replace the placeholder comment `// PLACEHOLDER:JS:DATA-SKELETON` in `fdn-pwa/index.html` with the DATA object skeleton shown below. This skeleton declares the structure and inserts nested placeholder comments that subsequent prompts (16–27) will replace with actual entries.

**CRITICAL**: Each nested placeholder comment string must be unique and match the exact strings used in prompts 16–27.

Replace `// PLACEHOLDER:JS:DATA-SKELETON` with:

```javascript
const DATA = {
  symptoms: {
// PLACEHOLDER:SYMPTOMS:BATCH1
// PLACEHOLDER:SYMPTOMS:BATCH2
// PLACEHOLDER:SYMPTOMS:BATCH3
// PLACEHOLDER:SYMPTOMS:BATCH4
// PLACEHOLDER:SYMPTOMS:BATCH5
// PLACEHOLDER:SYMPTOMS:BATCH6
// PLACEHOLDER:SYMPTOMS:BATCH7
  },
  variables: {
// PLACEHOLDER:VARIABLES:BATCH1
// PLACEHOLDER:VARIABLES:BATCH2
// PLACEHOLDER:VARIABLES:BATCH3
// PLACEHOLDER:VARIABLES:BATCH4
  },
  clusters: {
// PLACEHOLDER:CLUSTERS
  }
};
```

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/index.html` no longer contains `// PLACEHOLDER:JS:DATA-SKELETON`
- File now contains `const DATA = {`
- File contains all 7 symptom batch placeholders: `PLACEHOLDER:SYMPTOMS:BATCH1` through `PLACEHOLDER:SYMPTOMS:BATCH7`
- File contains all 4 variable batch placeholders: `PLACEHOLDER:VARIABLES:BATCH1` through `PLACEHOLDER:VARIABLES:BATCH4`
- File contains `// PLACEHOLDER:CLUSTERS`
- The `// PLACEHOLDER:JS:SW-REGISTRATION` and all other JS placeholder comments still exist in the file

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-15"`
- `pendingSteps`: remove `"step-15"`
- `flags.dataSkeletonWritten`: set to `true`
