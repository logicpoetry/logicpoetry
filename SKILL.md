---
name: logic-poetry
description: "Run Logic Poetry to research a brand or scenario, build a deep-research brief, develop campaign strategy and creative platforms, or debug existing work. Uses the nine-step chain with human Insight and Strategy checkpoints, sourced research operators, and campaign craft methods."
license: CC-BY-SA-4.0
metadata:
  author: Nicolas Chan
  version: 1.1.0
  homepage: https://logicpoetry.ai
  repository: https://github.com/logicpoetry/logicpoetry
---

# Logic Poetry

Clarity and assembly first. Expression second. Fix the logic before polishing the poetry.

A fixed nine-step chain that turns a brief into a creative platform. The labels can flex in client output. The sequence and the interfaces between steps do not.

## The chain

| # | Step | Job | Load |
|---|------|-----|------|
| 1 | Zeitgeist | The macro-reality that forces the situation to exist | `method/01-zeitgeist.md` |
| 2 | Tension | The wall the Zeitgeist creates | `method/02-tension.md` |
| 3 | Insight | Four-part chain that makes the brand the only rational response. **Pit stop.** | `method/03-insight.md` + `method/03b-logic-stack.md` |
| 4 | Role | The brand's superpower against the tension | `method/04-role.md` |
| 5 | Call to Action | The observable behaviour change | `method/05-call-to-action.md` |
| 6 | Strategy | Get-Who-To-By. **Pit stop, run the rubric.** | `method/06-strategy.md` + `method/06b-gwtb-engine.md` |
| 7 | The Creative | Platform, quality tests, effectiveness ladder | `method/07-the-creative.md` (+ `07a-manifesto.md`) |
| 8 | Big Idea | The one thing everything hangs off | `method/08-big-idea.md` |
| 9 | Small Ideas | Tactics that prove the big idea | `method/09-small-ideas.md` |

## How to run it

1. Read `method/OPERATING-MANUAL.md` first. It sets behaviour, triggers, the three-language configuration, and the execution order. Then `method/00-core-philosophy.md`.
2. Load step files as you reach them. Do not load the whole tree up front.
3. **Step 3 is a mandatory pit stop.** Present insight candidates with the epistemic warning. Wait for the operator to pick.
4. **Step 6 is a mandatory pit stop.** Run the GWTB Quality Rubric in `method/06b-gwtb-engine.md` before Step 7.
5. When a recognisable pattern is in play, name the Creative Move (`method/creative-moves.md`) and the technique (`catalog/`).

## Research before and during a run

For "build a research brief", "research this brand/scenario", or "feed this research into Logic Poetry", read `method/research-brief.md`. BUILD produces a tailored assignment; RESEARCH carries it out; RUN consumes the findings and respects both human checkpoints. Reuse the general library before adding brief-specific evidence.

When asked for questions first, use INTERVIEW: ask one useful question at a time, build the brief from the answers, and wait for the user to start research.

Use `method/research-operators.md` for the 41-operation menu and detailed attributed procedures. Use `method/creative-operator-routing.md` to connect source records, transformations and distinct candidate routes. Overlapping aliases are not separate inventions.

`RESEARCH.md` is the generated, self-contained research entry point for an AI without file access. Paste it with a brand, campaign or scenario. The subsequent nine-step run uses this skill or the full `PROMPT.md`.

## Supporting modules

- `catalog/` — Creative Techniques Catalog, clusters A to L. Start at `catalog/README.md` for the selection guide.
- `frameworks/` — plug-in methods that run inside a step (Disruption, Zagging, Challenger, Predatory Thinking and more). One file each; load on demand.
- `method/debugging-suite.md` — five checks for work that "feels flat".
- `method/validation-checklist.md` — final gate before shipping.
- `method/output-models.md` — Deck Mode, Session Recap, Performance Snapshot.
- `method/soundcheck.md` — read in full when preparing or reviewing a deck.
  Audience, argument and slide titles: structure first, then polish. Applies
  from the title outline through final review, with the nine-step decisions
  and human checkpoints retained.
- `method/brief-types.md` — where Logic Poetry sits relative to other brief types.
- `method/behavioral-guardrails.md` — what not to do.
- `examples/` — the case library. `examples/INDEX.md` lists every case by brand, category and market; cases flagged `calibration: true` are the teaching set.

## Single-paste version

`PROMPT.md` is the whole framework in one file for chat windows that cannot load a skill tree. The compiler `scripts/build-boot.py` generates it, `RESEARCH.md`, `examples/INDEX.md` and the `dist/` outputs. Never edit those by hand.
