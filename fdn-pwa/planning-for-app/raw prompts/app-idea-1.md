## Goal

Add a new feature to the existing PWA at `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\fdn-pwa` called the **Universal Feedback Loop Practice System** — a guided, action-oriented tool that takes a user's selected symptoms from the existing app and returns a clear, simple, step-by-step practice plan they can follow in their daily life. The result is a zero-jargon, zero-overwhelm experience for someone with no prior FDN knowledge or health practice history.

---

## Phase 1: Research & Familiarization (Do this before writing any code)

1. **Read the existing app** — explore `fdn-pwa/` fully. Understand its current structure, how symptoms are stored/selected, the routing, components, and state management patterns in use.

2. **Read the knowledge maps** — read both files in full:
   - `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\knowledge-map.md`
   - `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\source-content-map.md`

3. **Read the course content** — navigate `C:\Users\Alexb\Documents\Kaitlyn's vs code docs\universal-research-system\research-source-content\course` using the source-content-map as your index. Read all relevant files needed to understand:
   - What the **Universal Feedback Loop** methodology is
   - How symptoms map to root causes and actionable practices
   - What the recommended daily/weekly actions are per symptom cluster
   - The language, tone, and framing used in the course

> **CRITICAL RULE:** Every piece of health guidance, practice recommendation, and educational content displayed in this feature MUST come exclusively from the course content. Do NOT use your training data to fill in health advice, protocols, or explanations. If the course doesn't say it, the app doesn't say it.

---

## Phase 2: Feature Design (Before writing any code, output a written plan)

After completing Phase 1, write a concise feature specification covering:

- **Data model** — how selected symptoms map to practice recommendations (derived from course content)
- **User flow** — step-by-step screen sequence from symptom selection → personalized plan
- **UI structure** — what screens/components need to be created or modified
- **UX principles to follow:**
  - One clear action per screen — never show more than the user needs right now
  - Plain language only — no acronyms, no clinical terms unless defined inline
  - Progress visibility — user should always know where they are and what's next
  - Zero ambiguity — every recommended action must answer: what exactly do I do, when, and for how long
  - The plan should feel effortless — if it feels like a lot, simplify further

Present this plan and wait for approval before proceeding to implementation.

---

## Phase 3: Implementation

Build the Universal Feedback Loop Practice System into the existing `fdn-pwa` app with these requirements:

### Functional requirements
- Pull the user's already-selected symptoms from the app's existing state/data layer
- Map each symptom (or symptom cluster) to a curated, course-derived set of daily/weekly practices
- Display a personalized practice plan — ordered, bite-sized, and actionable
- Each practice item must include: what to do, why it matters (1 sentence, plain language), and how often
- Allow the user to mark practices as done (local state — no backend required)
- No third-party API integrations — all logic is local, all content is from the course

### UI/UX requirements
- Match the existing visual design system of `fdn-pwa` exactly (reuse existing components, tokens, styles)
- Mobile-first, with desktop support
- Professional, clean, minimal — no clutter
- Micro-interactions on completion (e.g., checkmark animation) to reinforce positive feedback
- Never show the full plan at once if it creates visual overwhelm — use progressive disclosure

### Code requirements
- Follow the existing file structure, naming conventions, and component patterns in `fdn-pwa`
- No new dependencies unless absolutely necessary and justified
- All course-derived content should be stored as structured data (e.g., JSON) in the app — not hardcoded inline

---

## Out of Scope
- Backend, database, user accounts, or authentication
- Third-party health APIs, tracking services, or analytics
- Modifying any existing symptom selection or educational content features already in the app
- Any health content not found in the course files listed above
