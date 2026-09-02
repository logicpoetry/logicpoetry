# Logic Poetry

**A nine-step framework for turning a brief into a creative platform.** Logic first, poetry second. Built for strategists and creatives, and for the AI agents they work with.

> The brief is never the problem. The story is always there. Logic Poetry is the tool for finding it.

## The chain

1. **Zeitgeist** — the macro-reality that forces the situation to exist
2. **Tension** — the wall that reality creates
3. **Insight** — the four-part chain that makes the brand the only rational response *(mandatory pit stop: humans pick the insight)*
4. **Role** — the brand's superpower against the tension
5. **Call to Action** — the observable behaviour change
6. **Strategy** — Get-Who-To-By, scored against a quality rubric *(mandatory pit stop)*
7. **The Creative** — the platform, with quality tests and an effectiveness ladder
8. **Big Idea** — the one thing everything hangs off
9. **Small Ideas** — the tactics that prove it

Step labels can flex. Step logic cannot.

Around the chain: a twelve-cluster **creative techniques catalog**, a **debugging suite** for work that feels flat, defined **output models** (deck, recap, feedback report), and **calibrated award cases** so the AI knows what good looks like.

## Three ways in

**1. As an agent skill** (Claude Code, Codex, Cursor, anything that reads `SKILL.md`)

```bash
git clone https://github.com/neekchan/logicpoetry ~/.claude/skills/logicpoetry
```

Then say *"use Logic Poetry on this brief."* The agent reads the router and loads only the steps it needs.

**2. As a single paste** (ChatGPT, Gemini, Claude.ai, any chat window)

Copy the contents of [`BOOT.md`](BOOT.md) into a fresh chat as your first message. The AI wakes up as a Logic Poetry strategist.

**3. As a book**

Start at [`codex/00-core-philosophy.md`](codex/00-core-philosophy.md) and read the steps in order. The [`examples/`](examples/) folder shows the chain applied to real campaigns.

## Layout

```
SKILL.md              the router agents read first
BOOT.md               single-paste version, generated, do not edit
codex/                the nine steps and the supporting logic
catalog/              creative techniques, clusters A to L
examples/             calibration cases and a full model answer
scripts/build-boot.py rebuilds BOOT.md from the modules
```

## Growing it

Add logic as a file under `codex/` or `catalog/`, or a case under `examples/cases/`. Then run:

```bash
python3 scripts/build-boot.py
```

That regenerates `BOOT.md` and fails if anything breaks the layout. Versions are tagged; see [`CHANGELOG.md`](CHANGELOG.md).

## Author and licence

Authored by **Nicolas Chan**. Insight methodology informed by Julian Cole / Strategy Finishing School.

Released under [CC BY-SA 4.0](LICENSE): use it, adapt it, teach it, build products on it. Credit the source and share adaptations under the same terms.
