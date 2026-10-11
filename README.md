# Logic Poetry

> **Want to use it right now?** Open [`PROMPT.md`](PROMPT.md), press the copy button in the top-right of the file view, paste it into any chat window as your first message. Use the current repository files as the method source.
>
> **Sending an AI agent here?** Tell it to read [`SKILL.md`](SKILL.md). Claude Code, Codex and Cursor pick it up as a skill.

**A nine-step framework for turning a brief into a creative platform and connected campaign.** Logic first, poetry second. Built for strategists and creatives, and for the AI agents they work with.

**Read the changes:** [`CHANGELOG.md`](CHANGELOG.md) records dated additions and corrections. The working method is **1.1.0**; the latest Git tag is **v1.0.0**. Later changes remain under Unreleased. As of 11 October 2026, the Blueprint integration is committed and pushed to the private GitHub repository; neither a runtime build nor a changelog entry establishes hosted deployment.

## The chain

1. **Zeitgeist** — the macro-reality that forces the situation to exist
2. **Tension** — the wall that reality creates
3. **Insight** — the four-part chain that makes the brand the only rational response *(mandatory pit stop: humans pick the insight)*
4. **Role** — the brand's superpower against the tension
5. **Call to Action** — the observable behaviour change
6. **Strategy** — Get-Who-To-By, scored against a quality rubric *(mandatory pit stop)*
7. **The Creative** — the platform, with quality tests and an effectiveness ladder
8. **Big Idea** — the hero execution that brings the platform to life
9. **Small Ideas** — tactics that prove and extend the hero, connected into audience journeys through Blueprint

Step labels can flex. Step logic cannot.

Around the chain: a twelve-cluster **creative techniques catalog**, a **debugging suite** for work that feels flat, defined **output models** (deck, recap, feedback report), and **calibrated award cases** so the AI knows what good looks like.

## Blueprint for connected campaigns

At Step 9, [Nicolas Chan's Blueprint](frameworks/14-blueprint.md) connects the platform, Big Idea and Small Ideas. For each tactic, explain what it contributes to the creative centre and what its CTA urges people to do next.

Each arrow records CTA intent: the action urged, its destination or outcome, and the message connecting the encounters logically. A hyperlink, sign or point of sale helps facilitate that intent where appropriate. The map plots our intended pathways. People may take other routes and still achieve the outcome: a post intended to prompt word of mouth might instead lead someone straight to the website to buy. Audit missing steps, broken handoffs and disconnected tactics; success does not require following the plotted sequence.

The module provides ecosystem maps, highlighted example routes, a connection table and five audit views, with Nespresso, Shopline and HireRight examples from the author's training deck. Use it to design a connected campaign or audit an existing journey. The Insight and Strategy human checkpoints remain intact.

## Research from a brand, campaign or scenario

Copy [RESEARCH.md](RESEARCH.md) into a research-capable AI and add the assignment. Ask it to build a research brief, carry out research, or prepare findings for Logic Poetry. It works backwards from all nine steps and the operator library, preserving full source URLs and human checkpoints.

To discuss the brief before research, give an assistant with repository access this instruction:

> Read https://github.com/logicpoetry/logicpoetry/blob/main/RESEARCH.md and use INTERVIEW mode. Ask me one question at a time to build my research brief. Show me the completed brief and wait until I say “Start research.”

If the assistant cannot read the repository, attach RESEARCH.md with the same instruction.

For the subsequent nine-step run, give the AI [PROMPT.md](PROMPT.md) or access to the skill files alongside the research handoff.

The reusable library supports brand-specific overlays. See [the operator library](method/research-operators.md) for 41 documented operations with overlaps mapped, and [operator routing](method/creative-operator-routing.md) for combinations and review.

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
README.md             how to use the current method
CHANGELOG.md          dated additions, corrections and release status
PROMPT.md             single-paste version, generated, do not edit
RESEARCH.md           standalone research-brief builder and handoff, generated
method/                the nine steps and the supporting logic
catalog/              creative techniques, clusters A to L
frameworks/           plug-in methods that run inside a step, one file each
examples/             the case library, with a generated INDEX.md
dist/index.json       machine index of every module, generated
scripts/build-boot.py the compiler: rebuilds PROMPT.md, RESEARCH.md, INDEX.md and dist/
```

Prose is the source of truth. Every file carries a small frontmatter block so machines can index it without anyone writing YAML.

## Contributing

Three doors: add a case, add or finish a plug-in framework, improve the method. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Every pull request runs the compiler, which rejects missing fields and stale generated files.

## Growing it

Add a file, run the compiler, commit:

```bash
python3 scripts/build-boot.py
```

Cases marked `calibration: true` go into the single-paste `PROMPT.md`; the rest stay in the library. Record notable changes under Unreleased in [`CHANGELOG.md`](CHANGELOG.md), update this README when user-facing behaviour changes, and run `python3 scripts/build-boot.py --check`. Released versions receive tags; local edits do not create a release.

## Author and licence

Authored by **Nicolas Chan**. Insight methodology informed by Julian Cole / Strategy Finishing School.

The base method is released under [CC BY-SA 4.0](LICENSE): credit the source and share adaptations under the same terms. The locally integrated [Blueprint module](frameworks/14-blueprint.md) retains Nicolas Chan's proprietary attribution (`LicenseRef-Proprietary`); its inclusion grants no redistribution rights.
