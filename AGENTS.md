# AGENTS.md — working on this repo with an AI agent

You are editing **Logic Poetry**, an open-source creative-strategy method. This file tells your agent how the repo works. If you want to *use* the method rather than edit it, load `SKILL.md` instead.

## The one rule

**Prose is the source of truth. Machines read the frontmatter. Generated files are never edited by hand.**

Generated files: `PROMPT.md`, `RESEARCH.md`, `examples/INDEX.md`, and `dist/` outputs. Change the modules, then rebuild:

```bash
python3 scripts/build-boot.py          # rebuild
python3 scripts/build-boot.py --check  # what CI runs on every pull request
```

Commit the regenerated files with your change.

## Layout

| Path | What it is | Edit? |
|---|---|---|
| `SKILL.md` | Router agents load to run the method | Yes, sparingly |
| `method/` | The nine steps, the GWTB engine, debugging suite, output models, guardrails | Yes, with care |
| `catalog/` | Creative techniques, clusters A to L | Yes |
| `frameworks/` | Plug-in methods, one file each, built from `_TEMPLATE.md` | Yes |
| `examples/` | Case library. `cases/` holds one file per campaign | Yes |
| `PROMPT.md` | Single-paste version for chat windows | Never, generated |
| `RESEARCH.md` | Standalone research brief builder and handoff | Never, generated |
| `examples/INDEX.md`, `dist/` | Indexes | Never, generated |

## What must not change

- The nine-step sequence and the interfaces between steps. Labels can flex in client output; logic and order cannot.
- The two mandatory pit stops: Insight (Step 3) and Strategy (Step 6). Never let the method run past them unattended.
- The name. "Logic Poetry" only. The compiler rejects the previous name.

## Frontmatter

Every module starts with a small YAML block. Required everywhere: `id`, `kind`, `version`. Cases also need `brand`, `category`, `market`, `steps`, `calibration`. Frameworks need the seven template headings in the body. The compiler enforces all of this; read its error, fix the module, rerun.

## Adding things

- **Case:** copy an existing file in `examples/cases/`, next number, `calibration: false`. Real campaign, checkable source.
- **Framework:** copy `frameworks/_TEMPLATE.md`, pass the admission test in `frameworks/README.md`.
- **Method change:** open an issue first if it touches step logic.

Full contributor guide: `CONTRIBUTING.md`.

## README and change-log upkeep

- Add a dated entry under `CHANGELOG.md` → Unreleased for every notable method, framework, case-library or usage change. State what changed, why it matters and how it was checked.
- Update `README.md` when entry points, capabilities, layout, version status or licensing change. Keep its change-log link visible.
- Preserve existing history. Record meaningful corrections and distinguish working module versions, tagged releases, local edits and hosted deployment.
- Documentation-only edits do not require a method version bump. Method edits still require generated outputs to be rebuilt and checked.

## Voice

Short stacked sentences. Point form where it earns it. No corporate glaze: no "leverage", "unlock", "synergy", "robust", "thought leadership". If a line can be shorter without losing the idea, cut it.
