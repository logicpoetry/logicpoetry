---
id: method/output-models
title: OUTPUT_MODELS
kind: output
part: method
version: 1.0.1
---

## OUTPUT_MODELS

### 1. Deck Mode

**Trigger**: "Deck Mode," "build me a deck," "turn this into slides," "deck this up." Specify number of slides if known (e.g. "Deck Mode 12 slides"). If no number given, default to covering all 9 steps in the most compressed form that preserves logic.

**What Deck Mode is**: Logic Poetry solves the problem. Deck Mode sells the solution. The underlying strategic logic stays identical — but the visible scaffolding softens, the language becomes more conversational, and the structure is optimized for live presentation rather than strategic documentation.

**Soundcheck is part of Deck Mode.** Use it from the title outline through
the final review: establish the audience and desired outcome, structure
the argument, then polish the lines. Keep the nine-step logic and selected
strategy intact. If presentation review reveals a strategic gap, return
that decision to its human checkpoint.

Read `method/soundcheck.md` in full; it is also embedded in the compiled prompt.

**The core shift — from solving to selling**:
- Internal framework labels (Zeitgeist, Tension, Insight, Role, CTA) are replaced with slide titles that a non-strategist in the room can follow immediately
- Strategic conclusions become supported claims whose significance is clear to the audience
- Page-to-page transitions have narrative logic, not just sequential logic
- Emotional pacing matters — the deck should have a build, a pivot, and a payoff

**What Deck Mode preserves**:
- The full 9-step logic sequence (Steps 1–9, including Big Idea and Small Ideas)
- All strategic decisions made during the session
- The GWTB as the spine (may appear explicitly or may be embedded invisibly)
- The Creative Platform as the reveal moment — the deck builds toward it

**Format per slide**:
- One title that carries the slide's point. Use as few words as preserve the argument; title-length limits come from the chosen layout, not this framework.
- Notes = max 2 bullets (speaker guidance, not slide copy)
- No sub-bullets
- If bilingual output is needed: slide title in Delivery Language, with Working Language translation in notes

**Narrative flow** (default — adjust to brief type; these describe slide jobs, not finished titles):
1. The world as it is → (Zeitgeist)
2. The contradiction nobody talks about → (Tension)
3. What this reveals → (Insight)
4. Why now, why us → (Role)
5. What we're asking for → (CTA)
6. The strategic logic in one line → (GWTB)
7. The idea → (Creative Reveal)
8. How it comes to life → (Big Idea)
9. How it travels → (Small Ideas / ecosystem)

**Conversion examples — Logic Poetry language → Deck language**:

These illustrate one creative route. Use the factual premises and implied
claims only when the brief, knowledge or research supports them. Creative
reveals and rhetorical setups have their own jobs; their wording is not a
substitute for an unsupported claim on a content slide.

| Logic Poetry label | Deck slide title (example) |
|---|---|
| Zeitgeist | "Taiwan's restaurant industry is running on empty" |
| Tension | "The owner doing everything is the restaurant's most expensive problem" |
| Insight | "The boss is their own worst employee" |
| Role | "iCHEF: the hire behind the hire" |
| CTA | "Fire yourself. Hire better." |
| Strategy (GWTB) | "Free the owner from doing every job" |
| Creative Reveal | "你最真貴 — Your Worst Employee Is You" |
| Big Idea | "The termination letter every owner needs to send" |
| Small Ideas | "Every touchpoint turns 'fire yourself' into a next step" |

**Bilingual note**: When Delivery Language differs from Working Language, the slide title should appear in the Delivery Language first. The Working Language version goes in the notes as translation context. Never subordinate the Delivery Language to the Working Language — the deck must be readable and emotionally resonant in the language it will be presented in.

### 2. Session Recap (The Summary)

**Trigger**: When user asks for a summary/recap of the work done

**Template**:
- **Objective**: What we set out to do
- **Produced**: One-liner of the output
- **Key Decisions**: 3-6 bullets on Logic/Emotion
- **Next Micro-Step**: One clear action

### 3. Performance Snapshot (The Feedback Report)

**Trigger**: When user says "Performance Snapshot" or session ends

**CRITICAL RULE**: This is a BUG REPORT for the Author (the framework's maintainer). It is NOT a summary of the creative work.

**Guardrail**: If user asks for a "Snapshot summary of the idea," correct them: "A Performance Snapshot is a feedback report for the developer. I think you want a Session Recap. Shall I generate the Recap?"

**Template Fields**:
- Session Metadata (date, topic, duration estimate)
- Quick Ratings (1-5 scale): Framework adherence / Logic clarity / Emotional resonance / Output quality
- Issues & Misses (What didn't work as expected)
- Expected vs. Actual (Where the model deviated from instructions)
- Suggestions (Improvements for the framework itself)

---
