# Logic Poetry

> **Want to use it right now?** Open [`PROMPT.md`](PROMPT.md), press the copy button in the top-right of the file view, paste it into any chat window as your first message. Or use the one-click copy at [logicpoetry.ai](https://logicpoetry.ai).
>
> **Sending an AI agent here?** Tell it to read [`SKILL.md`](SKILL.md). Claude Code, Codex and Cursor pick it up as a skill.

**A nine-step framework for turning a brief into a creative platform.** Logic first, poetry second. Built for strategists and creatives, and for the AI agents they work with.

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
git clone https://github.com/logicpoetry/logicpoetry ~/.claude/skills/logicpoetry
```

Then say *"use Logic Poetry on this brief."* The agent reads the router and loads only the steps it needs.

**2. As a single paste** (ChatGPT, Gemini, Claude.ai, any chat window)

Copy the contents of [`PROMPT.md`](PROMPT.md) into a fresh chat as your first message. The AI wakes up as a Logic Poetry strategist.

**3. As a book**

Start at [`method/00-core-philosophy.md`](method/00-core-philosophy.md) and read the steps in order. The [`examples/`](examples/) folder shows the chain applied to real campaigns.

## Layout

```
SKILL.md              the router agents read to run the method
AGENTS.md             the rules agents read to edit this repo (CLAUDE.md points here)
PROMPT.md             single-paste version, generated, do not edit
method/                the nine steps and the supporting logic
catalog/              creative techniques, clusters A to L
frameworks/           plug-in methods that run inside a step, one file each
examples/             the case library, with a generated INDEX.md
dist/index.json       machine index of every module, generated
scripts/build-boot.py the compiler: rebuilds PROMPT.md, INDEX.md and dist/
```

Prose is the source of truth. Every file carries a small frontmatter block so machines can index it without anyone writing YAML.

## Contributing

Three doors: add a case, add or finish a plug-in framework, improve the method. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Every pull request runs the compiler, which rejects missing fields and stale generated files.

## Growing it

Add a file, run the compiler, commit:

```bash
python3 scripts/build-boot.py
```

Cases marked `calibration: true` go into the single-paste `PROMPT.md`; the rest stay in the library. Versions are tagged; see [`CHANGELOG.md`](CHANGELOG.md).

## Author and licence

Authored by **Nicolas Chan**. Insight methodology informed by Julian Cole / Strategy Finishing School.

Released under [CC BY-SA 4.0](LICENSE): use it, adapt it, teach it, build products on it. Credit the source and share adaptations under the same terms.
