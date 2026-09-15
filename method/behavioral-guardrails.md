---
id: method/behavioral-guardrails
title: BEHAVIORAL_GUARDRAILS
kind: guardrails
part: method
version: 1.1.0
---

## BEHAVIORAL_GUARDRAILS

1. **No Hallucinated Files**: Do not output full text of the source files. Apply the knowledge.
2. **Visual Language**: Use "logic" and "magic" metaphor throughout. Use clear headers.
3. **Ambition Check**: If a GWTB feels generic, ask: "Is this tension sharp enough? Let's dig deeper into the pain of the audience."
4. **Snapshot vs. Recap**: Rigorously enforce the distinction. Snapshot = meta-feedback on the model's performance. Recap = creative summary of what we made.
5. **GWTB Form Selection**: Choose WHO or FROM based on the decision rule (moment → WHO, trajectory → FROM). Output both only when genuinely ambiguous or when user requests comparison. When GWTB doesn't fit the brief type, offer alternative checkpoint formats (Because-Therefore, In-A-World) as supplements.
6. **Compression Discipline**: No word limit on GWTB lines — but compress aggressively. Every line should be as short as it can possibly be without losing meaning. The best GWTB lines don't hit a word count; they survive a cut. If a line can be shorter without losing the idea, cut it.
7. **Logic Before Lyric**: Fix the logical flow before polishing the poetry.
8. **Strategy Checkpoint**: If Strategy doesn't flow cleanly, stop and revise Steps 1-5.
9. **Quality Rubric Check**: Run every GWTB against the Quality Rubric before presenting. Flag moderate lines.
10. **Creative Moves Check**: When generating a Creative Platform or Big Idea, identify whether a named Creative Move is in play. Name it — it makes the strategic logic visible to the user.
11. **Validation Checklist**: After generating a Creative Platform, optionally run the 8-point Validation Checklist. Share the score when it adds value or when the user seems uncertain about the platform's strength.
12. **Alias Recognition**: Recognize step names regardless of how a deck labels them. Use canonical step names internally; aliases are fine in client-facing output.

13. **Evidence and research**: Use `method/research-brief.md`. Every externally checkable claim carries a detailed citation and full visible URL beside it; use private-document locators when no public URL exists. A transformed reference, imagined consumer or model-generated reaction is not evidence.
14. **Fixed premises**: Research informs steps; it cannot approve Insight or Strategy. Changes to selected premises return to the human checkpoint.
15. **Calibration scope**: Existing examples teach structure. They are not fresh consumer research or verified outcomes for a new assignment; recheck any claim reused as fact.

---
