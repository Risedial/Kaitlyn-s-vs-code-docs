# Prompt 01: Initialize Build — Create fdn-pwa/ Directory and Stub Files

## Prerequisites
- state.json flags that MUST be `true` before this prompt runs: none
- Files that MUST already exist: `connect-da-dots/state.json`

## Hard Constraints
1. **32,000 token output limit** — Neither Claude Code nor any sub-agent it spawns may output more than 32,000 tokens in a single response. If a task risks exceeding this, split it into further sub-tasks and stop after the first sub-task completes.
2. **No truncation** — When writing data entries (symptoms, variables, clusters), write ALL entries for that batch. Never use `// ... more`, ellipses, or placeholder comments.
3. **State sync required** — Read `connect-da-dots/state.json` at the start of every session. Complete the single assigned task. Update `state.json` to mark that step complete before exiting.
4. **No external dependencies** — No CDN, no npm, no external URLs in any generated file.
5. **File writes only via Write tool** — Never use bash heredoc or shell redirection to write application files.

## Task
1. Read `connect-da-dots/state.json` and confirm `flags.initialized` is `false`. If it is already `true`, abort — this step has already run.
2. Use the Bash tool to create the output directory: `mkdir -p fdn-pwa`
3. Use the Write tool to create `fdn-pwa/manifest.json` with content `{}` (two characters — this is a stub that prompt-02 will overwrite).
4. Use the Write tool to create `fdn-pwa/sw.js` with content `// FDN Service Worker — stub` (this is a stub that prompt-03 will overwrite).
5. Use the Write tool to create `fdn-pwa/index.html` with content `<!DOCTYPE html><!-- FDN Symptom Navigator PWA — stub, overwritten by prompt-04 -->` (this is a stub that prompt-04 will overwrite).

Do NOT write any real CSS, JS, or manifest content in this step. All three files are stubs only.

## Verification
Before updating state.json, Claude MUST confirm:
- `fdn-pwa/` directory exists (use Bash: `ls fdn-pwa/` or equivalent)
- `fdn-pwa/manifest.json` exists and is readable
- `fdn-pwa/sw.js` exists and is readable
- `fdn-pwa/index.html` exists and is readable

## State Update
On successful verification, update `connect-da-dots/state.json`:
- `completedSteps`: append `"step-01"`
- `pendingSteps`: remove `"step-01"`
- `flags.initialized`: set to `true`
- `artifacts.filesWritten`: append `"fdn-pwa/manifest.json"`, `"fdn-pwa/sw.js"`, `"fdn-pwa/index.html"`
