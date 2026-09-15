# Contributing to Logic Poetry

Three kinds of contribution, three doors. Everything comes in under the repo licence, CC BY-SA 4.0, and stays attributed to you in git history.

## 1. Add a case

Cases are how the framework learns what good looks like. One file per case in `examples/cases/`, numbered after the last one.

- Copy the shape of an existing case. Frontmatter first: `brand`, `category`, `market`, `steps` (which of the nine steps the write-up covers), `calibration: false`.
- Real campaigns only, with a source someone can check. Award status goes in `award`.
- Write the chain, not a case study. Zeitgeist, Tension, Insight, Role, Call to Action, GWTB, Creative Platform, Big Idea, Small Ideas. Skip a step only if the record does not support it.
- Do not set `calibration: true`. Maintainers promote a case into the single-paste `PROMPT.md` after review.

## 2. Add or finish a framework

`frameworks/` holds named methods that plug into the chain at a step. Copy `frameworks/_TEMPLATE.md`, keep all seven headings, and pass the admission test in `frameworks/README.md`. Thirteen seed entries are waiting for full write-ups; finishing one is the best first contribution.

## 3. Improve the method

Changes to the nine steps, the GWTB engine, the debugging suite or the guardrails live in `method/`. These get the most scrutiny. Open an issue first if the change alters step logic. Step labels can flex; step sequence and the two pit stops cannot.

## Before you open a pull request

```bash
python3 scripts/build-boot.py
```

That regenerates `PROMPT.md`, `RESEARCH.md`, `examples/INDEX.md` and the `dist/` outputs, and fails if a file is missing required fields or headings. Commit the regenerated files with your change. The same check runs on every pull request.

Never edit `PROMPT.md`, `RESEARCH.md`, `examples/INDEX.md` or `dist/` by hand.

## Language

No corporate glaze. Short stacked sentences. If a line can be shorter without losing the idea, cut it.
