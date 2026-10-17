#!/usr/bin/env python3
"""Logic Poetry compiler.

One source tree (prose markdown with frontmatter), six outputs:
  PROMPT.md          single-paste version for chat windows (calibration cases only)
  RESEARCH.md        standalone brief builder, compact operator menu and research handoff
  dist/RUNTIME.md    trimmed system prompt for the hosted engine (runtime:cut regions removed,
                     catalog replaced by a digest, runtime-flagged cases only); byte-frozen header
  dist/runtime.json  per-module sizes + sha256 of RUNTIME.md
  examples/INDEX.md  browsable index of every case
  dist/index.json    machine index of every module and its frontmatter

Usage:
  python3 scripts/build-boot.py            build everything
  python3 scripts/build-boot.py --runtime  build only dist/RUNTIME.md + dist/runtime.json
  python3 scripts/build-boot.py --check    build to memory and fail if outputs on disk are stale or a rule breaks

Cut markers: a line that is exactly `<!-- runtime:cut -->` opens a region and `<!-- /runtime:cut -->`
closes it. PROMPT.md drops only the marker lines; RUNTIME.md drops the whole region.
"""
import hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORBIDDEN = re.compile(r"hoffman|creative codex|budget ?/ ?timeline|\bcodex/", re.I)
FRAMEWORK_HEADINGS = ["## What it does", "## When to use it", "## How to apply it", "## Failure mode", "## Example", "## Source and confidence"]
CASE_REQUIRED = ["brand", "category", "market", "steps", "calibration"]
CUT_OPEN, CUT_CLOSE = "<!-- runtime:cut -->", "<!-- /runtime:cut -->"
# Self-imposed guard against silent runtime growth, not a model or context limit.
# Set 2026-09-03 (888fd7f) when the first runtime was 157,886 bytes; ~7 KB headroom.
# Policy: if --check fails here, trim first (move reader-only text behind runtime:cut);
# raise only deliberately and record the reason in CHANGELOG.md.
RUNTIME_BUDGET_BYTES = 166_500
CJK = re.compile(r"[㐀-鿿豈-﫿]")

def est_tokens(text): return int(len(text.encode()) / 3.6) + len(CJK.findall(text))

def parse(path):
    text = (ROOT / path).read_text()
    meta = {}
    if text.startswith("---\n"):
        end = text.index("\n---", 4)
        for line in text[4:end].splitlines():
            if ":" not in line: continue
            k, v = line.split(":", 1); v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                v = [int(x) if x.isdigit() else x for x in v]
            elif v in ("true", "false"): v = (v == "true")
            elif v.startswith('"') and v.endswith('"'): v = v[1:-1]
            meta[k.strip()] = v
        text = text[end + 4:].lstrip("\n")
    return meta, text

def strip_marker_lines(text):
    kept = "\n".join(l for l in text.splitlines() if l.strip() not in (CUT_OPEN, CUT_CLOSE))
    return re.sub(r"\n{3,}", "\n\n", kept).strip() + "\n"

def apply_cuts(text, path, errors):
    out, depth = [], 0
    for n, l in enumerate(text.splitlines(), 1):
        s = l.strip()
        if s == CUT_OPEN:
            if depth: errors.append(f"{path}:{n}: nested runtime:cut")
            depth += 1; continue
        if s == CUT_CLOSE:
            if not depth: errors.append(f"{path}:{n}: unmatched /runtime:cut")
            depth = max(0, depth - 1); continue
        if "runtime:cut" in s: errors.append(f"{path}:{n}: malformed marker")
        if not depth: out.append(l)
    if depth: errors.append(f"{path}: unclosed runtime:cut")
    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

def rel(p): return str(p.relative_to(ROOT))

def prompt_order(index):
    cases = sorted(p for p in (ROOT / "examples/cases").glob("[0-9][0-9]-*.md"))
    calib = [rel(p) for p in cases if index[rel(p)].get("calibration") is True]
    return [
        "method/OPERATING-MANUAL.md", "method/00-core-philosophy.md",
        "method/research-brief.md", "method/research-operators.md", "method/creative-operator-routing.md", "method/shared-wordcraft.md",
        "method/01-zeitgeist.md", "method/02-tension.md", "method/03-insight.md", "method/03b-logic-stack.md",
        "method/04-role.md", "method/05-call-to-action.md", "method/06-strategy.md", "method/06b-gwtb-engine.md",
        "method/07-the-creative.md", "method/07a-manifesto.md", "method/08-big-idea.md", "method/09-small-ideas.md",
        "catalog/README.md", *sorted(rel(p) for p in (ROOT / "catalog").glob("[A-L]-*.md")),
        "frameworks/README.md", *sorted(rel(p) for p in (ROOT / "frameworks").glob("[0-9][0-9]-*.md")),
        "method/debugging-suite.md", "method/creative-moves.md", "method/validation-checklist.md",
        "method/output-models.md", "method/soundcheck.md", "method/brief-types.md", "method/behavioral-guardrails.md",
        "examples/README.md", "examples/insight-calibration-cases.md", "examples/cases/README.md", *calib,
        "examples/gwtb-quality-calibration.md", "examples/model-answer-spotify-listen-like-you-used-to.md",
    ]

def runtime_order(index):
    fixed = [
        "method/OPERATING-MANUAL.md", "method/00-core-philosophy.md",
        "method/research-brief.md", "method/research-operators.md", "method/creative-operator-routing.md", "method/shared-wordcraft.md",
        "method/01-zeitgeist.md", "method/02-tension.md", "method/03-insight.md", "method/03b-logic-stack.md",
        "examples/insight-calibration-cases.md",
        "method/04-role.md", "method/05-call-to-action.md", "method/06-strategy.md", "method/06b-gwtb-engine.md",
        "examples/gwtb-quality-calibration.md",
        "method/07-the-creative.md",
        "catalog/README.md", "@catalog-digest",
        "method/creative-moves.md",
        "method/08-big-idea.md", "method/09-small-ideas.md",
        "method/validation-checklist.md", "method/behavioral-guardrails.md",
    ]
    flagged = sorted(k for k, v in index.items() if v.get("runtime") is True and k not in fixed)
    # model answer first, then cases in file order
    flagged.sort(key=lambda k: (0 if "model-answer" in k else 1, k))
    return fixed + flagged

ENTRY = re.compile(r"^\*\*([A-L]\d+[a-z]?)\. ([^*]+?)\*\*(?:\s*[—–-]\s*(.+))?$")
JENTRY = re.compile(r"^- \*\*(J\d+)\. (.+?)\*\*")

def catalog_digest(bodies):
    lines = ["## CREATIVE TECHNIQUES CATALOG — DIGEST", "",
             "One line per technique. Use the IDs when naming techniques in Step 7. The full catalog with mechanics and examples lives in the public repo.", ""]
    for path in sorted(k for k in bodies if k.startswith("catalog/") and re.match(r"catalog/[A-L]-", k)):
        body = bodies[path]
        head = next((l for l in body.splitlines() if l.startswith("### ")), path)
        lines.append(head.replace("### ", "**") + "**")
        for l in body.splitlines():
            m = ENTRY.match(l.strip()) or JENTRY.match(l.strip())
            if not m: continue
            ident, name = m.group(1), m.group(2).strip()
            desc = (m.group(3) or "").strip() if m.lastindex and m.lastindex >= 3 else ""
            desc = re.sub(r"\s+", " ", desc)
            if len(desc) > 140: desc = desc[:137].rstrip() + "…"
            lines.append(f"- {ident}. {name}" + (f" — {desc}" if desc else ""))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"

def main():
    check = "--check" in sys.argv
    runtime_only = "--runtime" in sys.argv
    errors = []
    files = sorted(p for d in ("method", "catalog", "frameworks", "examples") for p in (ROOT / d).rglob("*.md")
                   if p.name not in ("INDEX.md", "_TEMPLATE.md"))
    index, raw = {}, {}
    for p in files:
        meta, body = parse(rel(p)); index[rel(p)] = meta; raw[rel(p)] = body
        if not meta.get("id"): errors.append(f"{rel(p)}: missing frontmatter id")
        if FORBIDDEN.search(body): errors.append(f"{rel(p)}: forbidden name in text")
        if meta.get("kind") == "framework":
            for h in FRAMEWORK_HEADINGS:
                if h not in body: errors.append(f"{rel(p)}: framework missing heading '{h}'")
        if meta.get("kind") == "case":
            for k in CASE_REQUIRED:
                if k not in meta: errors.append(f"{rel(p)}: case missing '{k}'")
    version = re.search(r"^\s*version:\s*([\d.]+)", (ROOT / "SKILL.md").read_text(), re.M).group(1)

    # PROMPT.md bodies: marker lines stripped. RUNTIME bodies: regions removed.
    prompt_bodies = {k: strip_marker_lines(v) for k, v in raw.items()}
    runtime_bodies = {k: apply_cuts(v, k, errors) for k, v in raw.items()}

    pseq = prompt_order(index)
    missing = [s for s in pseq if s not in prompt_bodies]
    if missing: errors.append(f"PROMPT modules listed but not found: {missing}")
    rseq = runtime_order(index)
    missing = [s for s in rseq if s != "@catalog-digest" and s not in runtime_bodies]
    if missing: errors.append(f"RUNTIME modules listed but not found: {missing}")
    if errors:
        print("\n".join(errors)); sys.exit(f"{len(errors)} problem(s)")

    # ---- PROMPT.md
    head = [
        "# ═══════════════════════════════════════════════",
        f"# LOGIC POETRY — SYSTEM PROMPT v{version}",
        "# Paste this entire document into any chat window.",
        "# The AI will wake up as a Logic Poetry strategist.",
        "# Generated by scripts/build-boot.py — do not edit by hand.",
        "# Source: https://github.com/logicpoetry/logicpoetry · https://logicpoetry.ai",
        "# ═══════════════════════════════════════════════", "",
    ]
    prompt = "\n".join(head) + "\n".join(prompt_bodies[s].rstrip() + "\n\n---\n" for s in pseq)

    # ---- RESEARCH.md: a self-contained entry point, using the same prose and menu.
    research_seq = ["method/research-brief.md", "method/research-operators.md", "method/creative-operator-routing.md"]
    research_parts = [runtime_bodies[k] if k == "method/research-operators.md" else prompt_bodies[k] for k in research_seq]
    research = (f"# LOGIC POETRY — RESEARCH v{version}\n\n"
                "Paste this document into a research-capable AI with a brand, campaign or scenario. "
                "Ask for a tailored research brief, research execution, or a handoff into Logic Poetry.\n\n"
                "Generated by scripts/build-boot.py from the method modules; do not edit by hand.\n\n"
                + "\n\n---\n\n".join(research_parts))

    # ---- RUNTIME.md (byte-frozen header: version + content sha, no date)
    digest = catalog_digest(runtime_bodies)
    parts, modules = [], []
    for s in rseq:
        text = digest if s == "@catalog-digest" else runtime_bodies[s]
        parts.append(text.rstrip() + "\n\n---\n")
        modules.append({"id": s, "bytes": len(text.encode()), "est_tokens": est_tokens(text)})
    body = "\n".join(parts)
    body_sha = hashlib.sha256(body.encode()).hexdigest()
    rhead = [f"# LOGIC POETRY — RUNTIME v{version} · build {body_sha[:12]}",
             "# Hosted-engine system prompt, compiled from the public method. Trimmed for execution, not reading.", ""]
    runtime = "\n".join(rhead) + body
    rbytes = len(runtime.encode())
    if FORBIDDEN.search(runtime): sys.exit("RUNTIME.md: forbidden name leaked")
    if rbytes > RUNTIME_BUDGET_BYTES:
        for m in sorted(modules, key=lambda m: -m["bytes"]): print(f"{m['bytes']:>8}  {m['id']}")
        sys.exit(f"RUNTIME.md is {rbytes} bytes, over the {RUNTIME_BUDGET_BYTES} budget")
    runtime_json = json.dumps({"version": version, "sha256": hashlib.sha256(runtime.encode()).hexdigest(),
                               "bytes": rbytes, "est_tokens": est_tokens(runtime), "modules": modules}, indent=2, ensure_ascii=False) + "\n"

    # ---- indexes
    cases = [(k, v) for k, v in index.items() if v.get("kind") in ("case", "model-answer")]
    rows = ["# Case index", "", "Generated by `scripts/build-boot.py`. Do not edit by hand.", "",
            "| Brand | Category | Market | Steps | In PROMPT | In RUNTIME | File |", "|---|---|---|---|---|---|---|"]
    for k, v in sorted(cases, key=lambda kv: str(kv[1].get("brand", "")).lower()):
        steps = v.get("steps", []); steps = ",".join(str(s) for s in steps) if isinstance(steps, list) else steps
        rows.append(f"| {v.get('brand','')} | {v.get('category','')} | {v.get('market','')} | {steps} | {'yes' if v.get('calibration') else ''} | {'yes' if v.get('runtime') else ''} | [{pathlib.Path(k).name}]({pathlib.Path(k).relative_to('examples')}) |")
    case_index = "\n".join(rows) + "\n"
    dist = json.dumps({"version": version, "prompt_sequence": pseq, "research_sequence": research_seq, "runtime_sequence": rseq, "modules": index}, indent=2, ensure_ascii=False) + "\n"

    outputs = {ROOT / "dist/RUNTIME.md": runtime, ROOT / "dist/runtime.json": runtime_json}
    if not runtime_only:
        outputs.update({ROOT / "PROMPT.md": prompt, ROOT / "RESEARCH.md": research, ROOT / "examples/INDEX.md": case_index, ROOT / "dist/index.json": dist})
    if check:
        stale = [rel(p) for p, s in outputs.items() if not p.exists() or p.read_text() != s]
        if stale: sys.exit(f"stale outputs, run the build: {stale}")
        print(f"check ok: {len(files)} modules · PROMPT {len(pseq)} · RESEARCH {len(research_seq)} · RUNTIME {len(rseq)} ({rbytes//1024} KB, ~{est_tokens(runtime)} tok) · {len(cases)} cases")
    else:
        for p, s in outputs.items():
            p.parent.mkdir(exist_ok=True); p.write_text(s)
        print(f"built: PROMPT.md {len(prompt.splitlines())} lines / {len(prompt.encode())//1024} KB · RESEARCH.md {len(research.encode())//1024} KB · RUNTIME.md {rbytes//1024} KB / ~{est_tokens(runtime)} tok est · {len(cases)} cases indexed")

if __name__ == "__main__":
    main()
