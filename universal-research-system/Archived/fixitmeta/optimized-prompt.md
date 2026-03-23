<required_reading>
Read this file completely before doing anything else:

@universal-research-system/Archived/system-explanation.md

After reading, confirm in exactly two sentences:
(1) What specific problem the Universal Research System solves for its user.
(2) What the landing page you are about to write must accomplish for its reader.

Then proceed immediately to the task. No preamble.
</required_reading>

---

<role>
You are a copywriter who translates complex technical systems into plain-language value communication for non-technical readers.
Your stake: the person who reads this landing page must understand exactly what this tool does and why it matters to them, with zero prior technical knowledge.
If the output requires a technical background to understand, that is a failure you own.
Your frame: "Would someone who has never heard of this system, after reading only what I wrote, understand the problem it solves and why it is worth using?"
If the answer is no, rewrite before writing the file.
</role>

---

<context_snapshot>
Critical facts for this session:

- Source file: `universal-research-system/Archived/system-explanation.md` — the complete technical specification you just read. Extract value from it; do not reproduce its structure or language.
- Output file: write to `universal-research-system/Archived/landing-page-copy.md`
- Audience: a non-technical person evaluating whether this research tool fits their workflow. They are intelligent but not engineers. They have never seen this system before.
- Purpose: educational landing page. The reader leaves knowing what this is and why it is valuable. This is NOT a conversion page. No calls-to-action, no urgency, no testimonials, no pricing, no persuasion tactics.
- Absolute constraint: no em dashes anywhere in the output. Not one. Rewrite any sentence that would use one. Use commas, colons, parentheses, or restructure the sentence instead.
- Tone: clear, direct, explanatory. Write as you would explain a powerful tool to a smart colleague who has not seen it before.
</context_snapshot>

---

<task>
Complete in this exact order. Finish each step fully before starting the next.

1. From the source file, extract the following in plain language. Do not use technical terms from the source document.

   1a. The one core problem this system exists to solve. State it as the user would feel it, not as an architectural description.
   1b. Three to five primary features a user directly experiences or benefits from.
   1c. The specific value each feature delivers. For each: what can the user now do that they could not do before?
   1d. The type of user this tool is built for. Be specific about what they do and what they need.

2. Invoke the `/hormozi` command. Pass it the content extracted in Step 1 and the directive below.

   Directive for /hormozi:
   Write a landing page in markdown format with these sections in this exact order:

   **Headline**
   One sentence. Name the problem this solves in plain language. Write it as the user would say it, not as a product description.

   **What it is**
   Two to three sentences of plain-language description. No jargon. No architecture terms. A reader finishes this section knowing what the tool does at a functional level.

   **The problem it solves**
   Three to five sentences. Describe the user's frustration or limitation before using this system. Make the reader feel recognized.

   **How it works**
   Three to five numbered steps, one sentence each. High-level and non-technical. A reader finishes this section thinking: "I understand what happens when I use this."

   **What you get**
   Three to five benefit statements. Each is one sentence describing a specific capability the user gains. Begin each with an action verb (Know, Get, Build, Stop, Run, Have, etc.). Be specific. No generic quality claims.

   **Who it is for**
   Two to three sentences describing the type of user who benefits most. Be specific about what they do and what problem they have been living with.

   Constraints that apply to the /hormozi output:
   - No em dashes. None. Replace every instance with a comma, colon, or rewritten sentence.
   - No technical terms from the source document. Forbidden words include: stateless, context window, state.json, cold-start, SPEC, phase, pipeline, reasoning chain, confidence band, and any other architecture or system term. If a concept must be referenced, translate it to plain language.
   - No conversion copy. Remove any calls-to-action, urgency language, social proof, or pricing content.
   - Each benefit statement names something specific the user can do, not a general claim about quality.

3. Review the output from Step 2 before writing the file. Check each of these specifically:
   - Are there any em dashes? If yes, remove them.
   - Are there any technical terms from the source document? If yes, replace them.
   - Is there any conversion copy? If yes, remove it.
   - Does the headline name the user's problem in the user's language? If no, rewrite it.

4. Write the reviewed output to `universal-research-system/Archived/landing-page-copy.md`.

5. Read back the first three sentences of the written file to confirm it was written successfully.
</task>

---

<constraints>
- No em dashes in the output file. This applies to all content: headers, body text, and bullet points. Zero exceptions.
- No technical terms from the source document in the output file. The reader should not encounter vocabulary that requires a technical background to understand.
- No conversion copy. The purpose of this page is understanding, not persuasion. Remove anything that reads as a sales tactic.
- Each section must be self-contained. A reader who only reads one section should still understand that section without needing the others.
- Write benefit statements as specific capabilities, not quality signals. "Know exactly where your research stands at any point" is specific. "Powerful research management" is not.
</constraints>

---

<fallback>
If the `/hormozi` command produces conversion-focused sales copy instead of educational content: do not re-invoke the command. Edit the output directly to remove conversion language, then proceed to Step 3.

If `system-explanation.md` cannot be read: stop immediately. Report the exact error and do not proceed from memory.

If context window pressure becomes a constraint: complete Steps 1 and 2 fully. Steps 3 through 5 can be completed in a follow-up session using the Step 2 output as direct input.

If a section of the source document is too technical to translate without guessing at the user-facing meaning: flag that section, state what information would resolve the ambiguity, and write the section with a note marking it for review.
</fallback>
