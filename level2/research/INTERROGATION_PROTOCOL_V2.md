# VAJRASTRA INTERROGATION PROTOCOL — v2.0 UPGRADE (delta over v1.0)
Owner: Srujan · 2026-09-13 · Applies ON TOP of v1.0. v1.0 stays canonical for
questions/roles/laws. This file adds the EVOLUTION MACHINERY: question fission,
hybrid human-genius loop, debate auto-generation, and the protocol's own
mutation cycle. Law: nothing here overrides ULTIMATE_HYBRID_CONCERN.md.

## PART 0.5 — DISK-TRUTH CORRECTIONS to v1.0 (verified 13 Sep, ~14:00)
Read these BEFORE running, or agents will chase phantoms:
- DECISIONS.log = level2/DECISIONS.log, currently **22 entries** (v1.0 said 17 — count drifted; recount live, never cite stale).
- Gates: no research/gates/ dir exists yet. Gate artifacts are loose files:
  research/gate_20pages_final.py, gate_results_final.json, gate_pages.json,
  test_v5_te.py, test_baseline_3pages.py. FIRST ACTION of EXEC role:
  `mkdir level2/research/gates`, create gates/INDEX.md, retro-index existing
  gate results into it (H8 is not future work — it is v2.0 step 1).
- CER_STAGE3B.json EXISTS in level2/reports/ (v1.0 C-track calls it "planned" —
  it landed; verify content before claiming).
- "Seal gates G1–G11" — no such literal gates in seal_gen.py. The machine checks
  live in seal_gen.py + verify_v2.py; A18 must audit THOSE, not a phantom list.
- Regression-alarm logic lives inside verify_v2.py (grep confirmed); there is no
  standalone alarm daemon. H7/H13 refer to wiring inside verify_v2 output.
- HOW_TO_RUN.txt is at repo root. Smoke tests: research/smoke/{anuvaad_tesseract,
  bodhan-indic-ocr, python-doctr, surya-ocr}.
- Smoke note: research/smoke/bodhan-indic-ocr exists — the "bodhan empty" story
  is documented there; E1's NE-OCR/VisionBodhan verification should read it first.

## PART 1.5 — QUESTION-FISSION LAW (the recursion that makes it evolve)
A question bank is dead weight if answering a question ends it. New law:
1. EVERY answered P0/P1 question MUST spawn 1–3 successor questions
   (fission), logged as children: Q-A7 → Q-A7.1 (deeper), Q-A7.2 (broader),
   Q-A7.3 (inverted — "what would be true if we're wrong?").
2. A question is TERMINAL only when: (a) its answer changed zero artifacts,
   (b) it spawned zero conflicts, AND (c) a fission attempt produced only
   questions already in the bank. Anything else stays OPEN.
3. Genealogy: every question carries lineage (parent id). Cycles are forbidden
   (a child identical to an ancestor = dead branch; log as CONFIRMED-STABLE).
4. Fission depth cap: 4 generations per lineage per day. Beyond that the
   lineage must either convert to a DECISIONS.log entry or a scheduled gate.
5. Daily fission quota per category: ≥3 new questions born from answers.
   A category that cannot fission for 2 straight days is DECLARED EXHAUSTED
   and gets merged into its richest neighbor (kill zombie categories).
6. THE INVERSION RULE (genius trick): every strong claim gets an inverted
   twin question automatically. "Consensus pseudo-GT is safe" → "What would
   poisoned consensus look like, and would our detectors catch it?"
   Inverted questions feed RED first.

## PART 2.5 — HYBRID HUMAN-GENIUS LOOP (what only Srujan decides)
The protocol is not autonomous — it is HYBRID. Split decision rights:
AGENT-DECIDABLE (never wait for human): measurements, recounts, 4-page gates,
report regen, question fission, debate scheduling, protocol versioning.
HUMAN-DECISION-REQUIRED (block until Srujan answers, max 3 pending at a time —
agents must BATCH these for one daily session, not interrupt):
  H1. Team-facing commitments (anything promised to Vinay/David/Bhashini).
  H2. Money (Level-3 keys, Sarvam credits signup account, GPU asks to Vinay).
  H3. Legal/risk (data licensing D9, ToS calls, compliance statements).
  H4. Scope bets (add govt-doc pages? add engine #11? drop openbharatocr?).
  H5. Exam-week tradeoffs (what stops during 18–22).
GENIUS-INJECTION RITUALS (the human value-add, protect these from automation):
  R1. MORNING SMELL-TEST (5 min): Srujan reads DASHBOARD + overnight conflicts,
      asks up to 5 unfiltered "does this smell right?" questions. Agents MUST
      convert each into measurable form same day (a smell → a gate or a query).
      This is the un-hackable channel for human intuition; honor every input.
  R2. EVENING FIVE (5 min): Srujan picks the day's 5 most surprising findings
      and tags each: "chase / park / kill." Chase = becomes P0 tomorrow.
  R3. WEEKLY STRANGER HOUR: fresh agent (no memory) gets docs only + one task;
      where it stumbles = next protocol fix. Bus-factor test is recurring now.
  R4. RIVAL SIMULATION (before Sep 16, then weekly): a red-team agent reads
      ONLY what a competitor could see (repo README, public artifacts, our
      demo script) and writes "how I'd beat Vaultstack in 3 slides."
Every HUMAN-DECISION-REQUIRED item older than 48h auto-escalates to the top
of the morning smell-test sheet — silence is a decision too; log it as such.

## PART 3.5 — DEBATE ENGINE v2 (motions breed motions)
Beyond v1.0's ten motions:
1. AUTO-MOTION RULE: any RED↔BLUE stalemate >24h, or any cross-lane research
   disagreement, AUTOMATICALLY becomes a scheduled debate motion (logged).
   No human needed to call the debate; Srujan may veto only.
2. CROSS-POLLINATION MATRIX: every day, generate ≥2 hybrid questions from
   DIFFERENT category pairs (tag them Q-B×E, Q-D×F, Q-C×G):
   - B×E: "If gates show PARSeq +10%, does the Sarvam cost-benefit flip?"
   - D×F: "Which missing hard-page type (govt/handwriting/scan-degradation)
     hurts our Sep-16 story most, per the failure taxonomy data?"
   - C×G: "If AKER replaces CER, what does that do to the deck's metric claims?"
   Hybrids are where non-obvious conflicts live — prioritize their fission.
3. Debate verdicts MUST end in one of: DECISIONS.log entry / scheduled gate /
   new question born into the bank. A debate that ends in talk only = failed
   debate; SCRIBE flags it.
4. EVIDENCE WEIGHTING (v1.0 rule kept, sharpened): disk-file > measured gate >
   published source > reasoned argument. Rhetoric scores zero. A side citing
   vibes forfeits the round — that is not cruelty, it is the anti-fooling law.

## PART 6 — THE PROTOCOL EVOLVES ITSELF (mutation cycle)
This protocol is a living artifact with its own metabolism:
1. NIGHTLY META-REVIEW (boss agent, 10 min): for each category — conflicts
   generated (want >0), fission rate (want ≥3), gates spawned (want ≥1/2 days),
   artifacts changed (want ≥1/3 days). Categories failing all four for 2 days
   get MUTATED: rewrite their question generators or merge them.
2. COMFORT AUDIT (the anti-theater law): any day ending with ZERO exposed
   conflicts, ZERO failed claims, ZERO changed conclusions = FAILED DAY for
   the interrogation, even if the project itself had a good day. Log it in
   the day's summary line. A week of comfort = the protocol is being gamed —
   raise severity: force RED to attack the protocol's own questions.
3. PROTOCOL VERSIONING: this file + v1.0 live in research/. Every mutation
   bumps a version line here (v2.1, v2.2...) with a 1-line changelog + date.
   INTERROGATION_CHANGELOG appended at file bottom. Never edit history.
4. QUESTION SCORING (weekly): each bank question gets scored 0–3 on novelty
   (asked before?), yield (artifacts changed per answer), conflict-potential
   (claims it can undermine). Questions scoring 0 across all three for a week
   are archived to the question graveyard (research/gates/INDEX.md section),
   not deleted — dead questions are the protocol's fossil record.
5. ESCALATION PATH: if the interrogation exposes something that threatens
   the seal or the Sep-16 story (e.g., a metric is a lie, GT is poisoned),
   it goes STRAIGHT to HUMAN-DECISION-REQUIRED H-queue with severity P0 —
   do NOT let agents "fix forward" silently. Trust repairs need sunlight.

## PART 7 — EXIT CRITERIA REFINEMENT (over v1.0 H15)
The 7-day loop is DONE when, in one final review pass:
  - gates/INDEX.md covers every open B-item (gate run or logged waiver)
  - DECISIONS.log carries a verdict for every PART-3 debate
  - the H-queue is empty (Srujan answered everything pending)
  - a rival-simulation artifact exists (R4) and its top-3 attacks each have
    a written, evidence-backed answer in SEP16_ONE_SCREEN.md
  - comfort-audit shows ≥1 real conflict per day for the final 3 days
  - Level-3 kickoff message (five-liner with ₹ numbers) drafted for Vinay
Until ALL six: the loop continues. After ALL six: seal this file as v2.0-final
and the protocol sleeps until the next benchmark round (L3 or North track).

## INTERROGATION_CHANGELOG
- v2.0 2026-09-13 — initial: disk-truth corrections, fission law, hybrid
  human-genius loop, debate auto-motion, cross-pollination, mutation cycle,
  comfort audit, exit criteria refinement. (Srujan + opencode session)
