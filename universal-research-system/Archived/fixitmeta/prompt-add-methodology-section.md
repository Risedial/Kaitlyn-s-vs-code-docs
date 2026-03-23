<required_reading>
Read these three files completely before doing anything else:

1. `universal-research-system/Archived/landing-page-copy.md`
2. `universal-research-system/Archived/research-patterns-system-context.md`
3. `universal-research-system/Archived/HOW-THIS-SYSTEM-WORKS.md`

After reading all three, confirm in exactly two sentences:
(1) What the existing landing page is selling, who it is for, and what voice it uses.
(2) What the Universal Research System does at a functional level, stated in plain language as a non-technical reader would understand it.

Then proceed immediately to the task. No preamble.
</required_reading>

---

<role>
You are a copywriter who translates complex technical systems into plain-language content that integrates seamlessly into existing copy.
Your stake: the section you add must read as if it was always part of the landing page — matching the existing voice, sentence rhythm, and directness exactly. A reader should not be able to identify where the original copy ends and the new section begins.
Your frame: "Would someone who has never heard of this system, after reading only the section I wrote, understand exactly how the methodology works and why that matters to them — without needing a technical background?"
If the answer is no, rewrite before writing to the file.
</role>

---

<context_snapshot>
Critical facts for this session:

- Target file: `universal-research-system/Archived/landing-page-copy.md` — this file is being appended to, not replaced. All existing content stays exactly as written.
- Source files: `universal-research-system/Archived/research-patterns-system-context.md` and `universal-research-system/Archived/HOW-THIS-SYSTEM-WORKS.md` — extract methodology from these; do not reproduce their structure or vocabulary.
- Audience: The same reader as the existing landing page — a researcher, analyst, strategist, or writer who works on questions too deep or multi-layered to resolve in a single AI conversation, and evaluates tools by whether they carry work forward automatically across sessions without requiring manual reconstruction.
- Purpose: Add one new section that explains the methodology behind the system in plain English: how it identifies every relevant factor, researches each one systematically, and maps the relationships between them with evidence. The reader finishes this section knowing exactly how the system works, not just what it produces.
- Absolute constraint: No em dashes anywhere in the new section. Not one. Rewrite any sentence that would use one. Use commas, colons, parentheses, or restructure the sentence instead.
- Tone: Match the existing landing page exactly. The existing copy is direct and concrete. It uses short sentences. It names specific failure modes by name. It does not use filler language or generic quality claims.
</context_snapshot>

---

<task>
Complete in this exact order. Finish each step fully before starting the next.

1. From the source files, extract the following in plain language. Do not use technical terms from the source documents.

   1a. The sequence of steps the system actually executes, from the moment it receives a question to the moment it produces a final output. State each step as the user would observe it happening, not as an architectural description.

   1b. What the system does with every relevant factor in a topic (the source documents call these "variables" — translate this to plain language throughout: they are the key factors, forces, and concepts that shape the research question). Name three to five specific things the system does to each one, including the evidence standard it requires before a factor's research is considered complete.

   1c. How the system identifies and validates relationships between factors. What does the system require before it will say two factors are connected? Translate the evidence standard into plain language: what exactly does "validated connection" mean to someone who has never seen this system?

   1d. What the user ends up with that they did not have before: what artifact, what capability, what knowledge. Be specific about what makes this different from a conversation transcript or a set of disconnected notes.

2. Invoke the `/hormozi` command. Pass it the content extracted in Step 1 and the directive below.

   Directive for /hormozi:
   Write one new section to append to an existing landing page. The section is titled:

   **How the methodology works**

   The section must contain exactly these elements in this exact order:

   **Opening paragraph**
   Two to three sentences. State what makes this system's approach different from generic AI research or one-shot AI conversations. Ground it in what the system actually does, not what it claims. Write in the same voice as the sentence: "The problem is not intelligence or effort. It is that there is no mechanism for carrying work forward automatically."

   **The step sequence**
   Four to six numbered steps, one sentence each. Each step describes what the system does during that stage. The reader finishes this list knowing exactly what happens from question to finished output, in their own terms.

   **What it requires before saying two things are connected**
   Three to four sentences. Explain the evidence standard the system applies before it will assert that two factors in the research are related. Make the reader understand why this standard exists: what problem does it prevent that a normal AI conversation cannot prevent?

   **What you end up with**
   Two to three sentences. Describe the output: what it is, what the user can do with it across multiple sessions, and what makes it fundamentally different from chat history or scattered notes.

   Constraints that apply to the /hormozi output:
   - No em dashes. None. Replace every instance with a comma, colon, or rewritten sentence.
   - No technical terms from the source documents. Forbidden words and phrases include: stateless, context window, state.json, cold-start, SPEC, phase, pipeline, reasoning chain, confidence band, variable, pending, validated array, orchestrator, schema, connection validation, and any other architecture or system term. If a concept must be referenced, translate it to plain language.
   - Match the voice of the existing landing page exactly. Read the landing page before writing. Short sentences. Specific failure modes named by name. No filler.
   - No conversion copy in this section. No calls-to-action, no urgency language, no pricing references.

3. Review the output from Step 2 before writing to the file. Check each of these specifically:
   - Are there any em dashes? If yes, remove them.
   - Are there any technical terms from the source documents? If yes, replace them.
   - Does the voice match the existing landing page? Read three sentences from the existing landing page, then read three sentences from the new section. If the rhythm feels different, rewrite to match.
   - Does the opening paragraph read as a natural continuation of the existing copy? If no, adjust the transition.

4. Append the reviewed output to the bottom of `universal-research-system/Archived/landing-page-copy.md`. Do not replace or modify any existing content. Add the new section after the last line of the existing file, preceded by a markdown horizontal rule (`---`).

5. Read back the first three sentences of the new section as written to the file, to confirm the append was successful.
</task>

---

<constraints>
- No em dashes in any new content added to the file. This applies to all content: headers, body text, and numbered lists. Zero exceptions.
- No technical terms from the source documents in the new section. The reader should not encounter vocabulary that requires a technical background to understand.
- The existing file content must not be modified in any way. Append only. If in doubt about whether an action is an edit or an append, it is an append.
- Every claim about how the system works must be traceable to the source files. Do not invent capabilities that are not documented in `research-patterns-system-context.md` or `HOW-THIS-SYSTEM-WORKS.md`.
- The new section must be self-contained. A reader who reads only this section, without reading the rest of the landing page, must still understand what is being described and why it matters to them.
</constraints>

---

<fallback>
If the `/hormozi` command produces conversion-focused sales copy instead of explanatory methodology content: do not re-invoke the command. Edit the output directly to remove conversion language, then proceed to Step 3.

If any of the three required files cannot be read: stop immediately. Report the exact file path that failed and do not proceed from memory.

If the voice of the output does not match the existing landing page after one edit attempt: flag the specific sentences that feel off, state what the existing landing page does differently in concrete terms, and ask the user to confirm the direction before writing to the file.

If context pressure becomes a constraint: complete Steps 1 and 2 fully. Steps 3 through 5 can be completed in a follow-up session using the Step 2 output as direct input.
</fallback>
