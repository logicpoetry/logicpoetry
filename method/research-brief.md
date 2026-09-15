---
id: method/research-brief
title: Build and run a research brief for Logic Poetry
kind: research-workflow
part: method
version: 1.1.0
---

## LOGIC_POETRY_RESEARCH_BRIEF_BUILDER

Turn a brand, campaign or scenario into a specific deep-research assignment. Work backwards from the decisions and operations Logic Poetry needs to support. Research retrieves the material; Logic Poetry develops and selects the campaign through its normal human checkpoints.

The reusable library comes first. A particular assignment adds an evidence-backed overlay without changing the library's brand-agnostic structure.

### Methodology reference

Logic Poetry repository: https://github.com/logicpoetry/logicpoetry

Every completed research brief must repeat this full visible URL. Use the repository's SKILL.md and relevant method/ files to clarify unclear research requirements. Identify the method version used; flag conflicts with supplied instructions. If access is unavailable, say so and use the embedded rules and supplied method.

### Choose the phase and scope

- **INTERVIEW:** When asked to discuss the brief first, ask one useful question at a time and wait. Build the brief from the answers. Start research only when the user asks to begin.
- **BUILD:** Default when asked for a research brief. Return a completed, self-contained brief adapted to the supplied assignment.
- **RESEARCH:** When asked to do the research, build any missing brief internally, then execute it. Return source records, alternative explanations and material for a later Logic Poetry run.
- **RUN:** When asked to use the findings in Logic Poetry, inspect the research handoff, develop Steps 1–3 and stop for human insight selection. Continue only through the authorised checkpoints.
- If the user requests several phases, do them in sequence. Outside INTERVIEW or requested review, a brief is not an extra approval gate. Step 3 and Step 6 remain mandatory human gates.
- **Scope LIBRARY:** No specific assignment; build or extend reusable material across named territories, cultures and mechanisms.
- **Scope BRIEF:** A brand, campaign or scenario is supplied; retrieve relevant library records first, recheck volatile claims, then research the gaps and useful lateral material.
- Existing user decisions remain in force. Mark an approved insight or strategy as fixed; return to its checkpoint before changing it.

The standalone RESEARCH.md includes what INTERVIEW, BUILD and RESEARCH need; its file references are optional navigation. An actual RUN also requires the full Logic Poetry method, through PROMPT.md or the skill files. If that method is unavailable, prepare the research handoff and identify the missing method before continuing.

<!-- runtime:cut -->

### Input the user can supply

    Brand, campaign or scenario:
    What needs to change / the problem:
    Audience and relevant participants:
    Market and cultural context:
    Working / delivery / creative-priority languages:
    Known capabilities, evidence or source links:
    Constraints, timing and required deliverable:
    Existing library or prior research:
    Selected insight or strategy, if any:
    Phase and scope, if different from the defaults:

<!-- /runtime:cut -->

A brand name, paragraph or rough scenario is enough to begin. Separate supplied facts, checked facts, interpretations and unknowns. Outside INTERVIEW, ask only when an ambiguity would materially misdirect research; otherwise produce a useful first version with explicit assumptions. Never invent a brand capability or audience fact to complete a field.

### Build the brief by working backwards

Ask what a strong downstream decision would need to know. Then turn that need into neutral research questions and the material to retrieve.

<!-- runtime:cut -->

| Destination | What the research must make possible | Material to seek | Useful operators |
|---|---|---|---|
| 1. Zeitgeist | Describe a world that exists independently of the brand | Dated shifts, beliefs, cultural scripts, language and context | R01/R03/R06, W09/W10 |
| 2. Tension | Identify a specific unresolved conflict and its boundaries | Incidents, trade-offs, non-use, contradictions and successful exceptions | R01–R05/R07/R21 |
| 3. Insight | Compare explanations of Observation → Desire → Friction | Motive evidence, counterexamples and alternative causal accounts | R02/R05/R07/R08; hypotheses stay labelled |
| 4. Role | Establish a credible capability against the selected tension | Actual assets, utility, delivery owners, proof and limits | R03/R04/R09/R24 |
| 5. CTA | Identify a meaningful, possible change | Behaviour, capability, opportunity, motivation and evaluation options | R21/R22 |
| 6. Strategy | Support a coherent GWTB/GFTB and expose weak links | Evidence connecting audience, situation, change, insight and role | Trace records; do not select strategy during research |
| 7. Creative | Supply culturally and structurally varied expressions | Phrase families, stories, visual/sound cues, metaphors and rules | R07–R17/R26, W01–W15, existing A–L catalog |
| 8. Big Idea | Make the platform tangible in one hero execution | Mechanisms, components, artifacts, dependencies and proof opportunities | R18–R20/R23–R26 |
| 9. Small Ideas | Show how the hero can travel and support the CTA | Routines, participation, channel affordances and journey handoffs | R18/R20/R22/R24/R25 |

<!-- /runtime:cut -->

Information about channels can be researched early. Specific execution choices remain downstream; the GWTB remains channel-agnostic.

### Brief contract

For BUILD, return a self-contained assignment containing mission, context with evidence status, a question/material/operator/evidence map for the relevant nine steps, competing explanations, selected/conditional/deferred operations, concrete queries and source habitats, the record/citation contract, required outputs and continuation criteria. Make priorities specific to the supplied assignment. Include each selected operator's transformation rule, fixed inputs, output and rejection check; IDs alone are insufficient. Repeat critical source and checkpoint rules inside the completed brief so another AI can execute it.

<!-- runtime:cut -->

### BUILD output: a completed research brief

Write a brief that another research-capable AI can use without this conversation or these files. Do not return a template with the assignment's name pasted into generic questions. Include all sections below, filled as far as the supplied information permits.

1. **Research mission and scope.** Name the actual entity/scenario, problem, decision the research must support, audience/context and limits. Use the user's objectives; distinguish them from your hypotheses.
2. **Context and assumptions.** State what is supplied, checked, inferred or missing. Record language priorities, constraints, existing decisions and source access.
3. **Backward requirements.** Adapt the nine-row table to this assignment. For each relevant step: unresolved question, exact kind of material, why it matters, target operator IDs and what would count as adequate evidence. Mark genuinely premature questions for later.
4. **Competing explanations.** Frame at least several plausible explanations as questions when the evidence permits. Specify what could support, narrow or disconfirm each. Avoid leading instructions such as “prove that consumers want X.”
5. **Operator coverage.** Consider the full R/W menu and existing craft families. Group selected, conditional and deferred operators with reasons. For selected operators, include the transformation rule, what stays fixed, input requirements, source habitats, potential output and rejection check. Define the operation in the completed brief so its ID never depends on another file. Representation across discovery, meaning, expression and tangible action matters more than forcing every operation to run.
6. **Search assignments.** Give concrete, assignment-specific queries; named source collections or source types; native-language variants where relevant; alternative/negative searches; and near, adjacent and distant reference directions. Distinguish proposed sources from inspected sources.
7. **Research record contract.** Reproduce the record and citation rules below in the finished brief. It must remain usable when copied into another AI.
8. **Required research outputs.** Reproduce the source atlas, material library, permutation workspace, handoff and coverage requirements below, tailored to the assignment.
9. **Scope and continuation.** Set a thorough but bounded first sweep, then redirect according to gaps and diminishing returns. A useful starting target is 30–40 substantive records and 12–15 ingredient combinations. These are planning targets; evidence quality and useful coverage control completion.
10. **Acceptance check.** Require traceable claims, distinct mechanisms, explicit uncertainty, preservation of selected premises, and no auto-selection of Insight or Strategy.

The finished brief must contain a direct execution instruction: “Conduct this research and return the specified records and handoff. Treat research hypotheses as hypotheses; do not run past Logic Poetry's human checkpoints.”

**Specificity test:** would the questions, source choices and required materials remain substantially unchanged if the assignment were replaced with an unrelated category? If yes, revise. Show what in the supplied assignment caused each priority.

<!-- /runtime:cut -->

### RESEARCH record contract

Five record types: **evidence, cultural material, mechanism, brand capability, creative hypothesis**. Every record stands alone.

    Readable ID and title:
    Record type:
    Specific material / supported claim:
    Original context: market, community, language, situation and period:
    Evidence scope: sample, method, denominator and limitations where relevant:
    Source: author/organisation, exact title, publication date or “not stated”:
    Locator: page/section/table/timestamp; access date:
    Full source URL, visibly written beside the claim:
    Original short wording, if needed and permitted:
    Contrary evidence and alternative interpretation:
    Reusable structure or mechanism, labelled as analysis:
    Operations to try and what must remain fixed:
    Destination Logic Poetry steps:
    Creative hypotheses, separately labelled, with parent records:
    Verification question / failure condition:

For **cultural material**, add recognition evidence, expected completion, meaning, variants, original script/pronunciation where relevant and any documented reuse restrictions.
For **mechanisms**, add the function, components, causal sequence, conditions and transfer mismatches.
For **brand capabilities**, add the delivery owner, proof and practical limits.
For **hypotheses**, cite each ingredient but do not imply the citations validate the new idea.

### Citation rules to include in every completed brief

Every externally checkable claim needs its supporting citation immediately beside it, including the opening synthesis and any extracted record. Write the full, verbatim URL visibly. No shortened URL, hidden hyperlink label, citation widget, footnote number or bibliography-only substitute. Repeat the URL when a record or claim is reused.

Use: Claim. Source: Author/organisation, “Exact title,” date or “not stated,” page/section/table/timestamp; accessed YYYY-MM-DD. Full URL: the complete inspected URL.

Open and inspect sources before calling them verified. Preserve the observed supporting URL; never invent a slug or citation. Prefer original works, primary research, creators, official technical documentation and first-person records. Seek independent corroboration and contrary evidence for consequential or disputed claims.

Distinguish original fact, source interpretation, your inference and creative hypothesis. Retain populations, dates, methods and denominators for statistics. A case demonstrates possibility, not prevalence. Copies of one press release or study remain one evidence family.

State when only an abstract, excerpt, transcript or secondary account was accessible. Keep unsupported leads out of the verified evidence pool. Private sources use an exact permitted document name and locator when no public URL exists; never invent or expose a private URL.

Keep quotations short. Prefer song titles, themes and source pointers to lyric collections. Never invent consumer quotes, familiar expressions, recognition, campaign results or prototype reactions. If browsing is unavailable, return a labelled research plan and unverified leads; do not present recall as completed research.

### Research deliverables

Return an orientation, source atlas, complete records, ingredient combinations, a source-linked handoff indexed to the nine steps, and a coverage/continuation audit. Retain uncertainty and previous human selections. These are inputs for discussion, not approved campaign decisions.

<!-- runtime:cut -->

### RESEARCH outputs

1. **Orientation:** scope, assumptions, strongest discoveries, useful surprises and material gaps. No winning campaign selection.
2. **Source atlas:** actual places inspected, full URLs, productive queries, what each habitat supplied and which operators its material can feed.
3. **Material library:** complete self-contained records, including contrary cases and a labelled “interesting, application unclear” shelf. Preserve specific details.
4. **Permutation workspace:** compatible ingredient combinations using different operations. For each: parent records with full URLs, transformation, emergent proposition, destination step, fixed premises, weakest assumption and next test. These are raw hypotheses, not approved insights or finished platforms.
5. **Logic Poetry handoff:** context sheet; record-to-step index; supported observations; alternative explanations; capability/CTA evidence; cultural/mechanism packets; missing evidence; prior human selections, if any. Mark readiness for discussion, not approval. Do not write a fake completed nine-step campaign.
6. **Coverage and continuation:** territories, communities, languages, source families and operator inputs covered; overlaps removed; unverified leads; missing material; next searches. Report what changed from previous library runs.

<!-- /runtime:cut -->

### Intake for a Logic Poetry run

Inspect the handoff and its actual source records. Recheck time-sensitive claims. Preserve record IDs and full citations in working evidence; do not turn source-linked hypotheses into facts. Start from context and tension, build the Insight chain, present candidates with the existing epistemic warning, and wait at Step 3. After selection, run Role/CTA/Strategy and wait at Step 6 before creative work.

The research packet can supply material to later steps without deciding them. Use creative-operator-routing.md for operations and platform tests. A citation to an ingredient supports that ingredient, not the campaign derived from it.

### Source territories to consider

Language and familiar works; visual/sonic/sensory cues; rituals; games/rules/systems; lived behaviour; measurable reality; objects/spaces/media; conventions/failures; adjacent crafts; change across time/place; actual interventions; new creative tools. Include unfamiliar material and exceptions as well as culturally familiar references.

For a thorough sweep, inspect the territory guide below and add assignment-specific habitats where they supply genuinely different material. Keep public reusable records separate from client-specific evidence.

<!-- runtime:cut -->

## RESEARCH_TERRITORY_GUIDE

These are starting habitats. A completed brief chooses concrete collections and queries appropriate to its assignment. The research output records actual inspected URLs.

| Territory | Look for | Places and retrieval directions | Operations it can feed |
|---|---|---|---|
| Language people carry | Idioms, proverbs, slang, stock replies, signage, ambiguity and local variants | Dictionaries, language corpora, oral histories, public discussions and actual usage; retain meaning, rhythm and expected completion | R12–R17, W02/W06/W07/W10 |
| Familiar works and stories | Titles, fables, myths, scenes, character roles, morals and genre expectations | Original creators, publishers, studios, library catalogues, film institutes and folklore collections; distinguish recognition of a title from knowledge of a detail | R08/R10/R12/R13, W01/W03/W05 |
| Visual, sonic and sensory shorthand | Symbols, silhouettes, compositions, interfaces, chants, sounds and textures | Museums, design archives, original audiovisual works and product documentation; inspect the medium or label description-only access | R26, W09/W11–W15 |
| Rituals and social scripts | Sequences, roles, props, permission, milestones and ordinary routines | Ethnographies, community publications, etiquette, demonstrations and participants' accounts | R01/R02/R06/R07/R23 |
| Games, rules and systems | Constraints, rewards, information gaps, exchange and cooperation | Rulebooks, manuals, practitioners, public-service systems and original experiments | R08–R11/R18–R20 |
| Lived behaviour and hidden friction | Workarounds, non-use, abandonment, reluctant participation and contradictions | Studies, diaries, reviews, complaints and task observations; compare users, former users, intermediaries and non-users | R01–R06/R21 |
| Reality that can become proof | Measurements, physical properties, hidden labour, infrastructure and natural mechanisms | Original studies, datasets, technical demonstrations, patents and specialist explanations; verify the mechanism before transferring it | R09/R18–R20/R24/R26 |
| Objects, spaces and media with another job | Receipts, labels, uniforms, waiting spaces, distribution and unused capacity | Product/service documentation, field observation, design archives and platform documentation; extract function and constraints | R10/R18–R20/R23/R24 |
| Conventions, alternatives and failures | Default promises, stale metaphors, failed launches, refusal and successful restraint | Actual category communications, independent reporting, criticism and postmortems; absence of search results is not proof of novelty | R05/R07/R08/R12 |
| Adjacent worlds and unfamiliar crafts | Comedy, theatre, choreography, pedagogy, accessibility, repair and fan practices | Practitioners' process accounts and documented work; search near and far, identifying why a mechanism could transfer | R03/R09/R10/R25 |
| Movement through time and place | Changing meanings, obsolete objects, local codes and contested symbols | Local-language sources, historical archives and dated usage; distinguish recognition, affection and willingness to participate | R05–R07/R12/R13, W10 |
| Campaigns and designed interventions | The precise move, enabling capability, execution and actual outcome | Original work, creator accounts and independent evaluation; include modest work and failures, distinguish claimed impact from measured impact | Existing A–L catalog, R24/R25 |
| Tools that reveal operations | Puzzles, constrained writing, word/sound tools and visual transformations | Original tools, creator explanations and source code when available; separate observed behaviour, documented design and inference | R16/R17/R26, W01–W15 |

### Search for alternatives deliberately

For each priority question, compare the familiar explanation, negative cases and critics, historical/local/specialist variants, and functionally relevant analogies. Keep room for discoveries whose application is not yet clear. Do not use “inversion” as a reason to manufacture an opposing fact.

A useful query names a behaviour, situation or mechanism. Examples of query shapes: “last time I tried [action]” + “[obstacle]”; “[category] stopped using because”; “[function] mechanism in [adjacent field]”; exact phrase + origin + local variants. Adapt them to actual language and circumstances.

### Three intake examples

**Brand-only input:** establish the exact entity and market where possible. Retrieve category conventions, actual capabilities and user/non-user situations. Treat the objective as missing; research alternative problem definitions instead of assigning a campaign goal.

**Campaign input:** preserve the stated objective, audience, constraints and approved decisions. Research the evidence and expressive/operational material needed for that campaign. An approved GWTB narrows downstream permutations; it does not authorise changing its premise.

**Scenario without a brand:** research the actors, action and circumstances. The Role may later be a behaviour, movement, public service or institution. Record possible enablers without inventing a commercial sponsor.

### Research acceptance

Assess evidence strength and creative potential separately. Retain source details, alternative interpretations, useful structures and lineage. A long list of famous references is insufficient if the actual inputs required by selected operators are missing.

For a platform, later test strategic fit, credibility, distinctiveness, recognition, five different executions, hero comprehension, feasibility and impact. A research method alone does not establish award potential. Current award criteria must be checked for the relevant category.

<!-- /runtime:cut -->

### Begin

Use the user's supplied assignment and requested phase. Use INTERVIEW when asked for questions first; BUILD for a brief; RESEARCH to gather information; RUN for a Logic Poetry run. If no assignment was supplied, invite a brand, campaign or scenario and preserve LIBRARY as the available default scope.
