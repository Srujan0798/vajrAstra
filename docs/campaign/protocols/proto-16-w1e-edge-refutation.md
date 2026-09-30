---
name: proto-16-w1e-edge-refutation
description: "Step 1E part 2 (lead + adversarial subagents) — draft 3–5 edge-thesis candidates from 1A–1D + hunt, then try to kill each with 3 adversarial lenses (incumbents did it / mechanism fails on real Indic input / cannot be built in time); only survivors go into EDGE_THESIS.md"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:13:32.739Z
---

# STEP 1E-REFUTE — EDGE THESIS (lead composes; adversarial subagents attack) → `docs/campaign/EDGE_THESIS.md`

## 1. Lead drafts 3–5 candidates
Inputs: 1A (what our numbers really show), 1B (22-language table, weak cells), 1C (what the lead wants: hybrid integration of existing models),
1D (competitors' gaps, comparability), hunt report. Plus the precursors: `docs/architecture/W5_BEAT_SARVAM_PLAN.md`, `docs/architecture/W5_STRATEGY_OPTIONS.md`,
`docs/research/R1_SOTA_MECHANISM_TEARDOWN.md`, `docs/research/level7/KILL_CRITERIA.md`.

**An edge thesis names one specific crack and explains mechanically why exploiting it beats them.** Format per candidate:
`name · the crack (what the field/competitor gets wrong or ignores) · mechanism (causal chain, step by step, down to which engines/data/metric) · target cells
(languages/conditions) · expected effect and how we'd measure it · evidence (URLs, file:line) · falsifier (the observation that would kill it) · cost (dev days, compute, approvals)`.

**Automatically disqualified:** "we use agentic AI" (our method, not an edge) · "combine X and Y" without a mechanism · anything needing a novel backbone ·
anything needing compute, data or downloads we do not have without an approval path · "do the existing thing well".

**Seeds visible to the planner — test them, do not assume them** (drop any the evidence kills):
- (i) *Independent-evaluation edge:* Sarvam built and scored its own benchmark (overlap allegation in `EVIDENCE_SUMMARY.md` §0); we hold 300 human gold pairs
  (bn/hi/sa) plus a 22-language set scored identically across 10 engines. Mechanism would be credibility/comparability, not accuracy — say so if that is all it is.
- (ii) *Calibrated routing over engines we already run:* per-language/per-condition routing with a confidence gate (Laya-style head or simple disagreement signal)
  choosing among 10 engines; needs evidence that the oracle-best engine per item beats the per-language best by a margin (1B data can measure the oracle gap).
- (iii) *Restoration pre-pass for degraded scans* (R4 OldScan lock) — needs evidence it helps non-Latin scripts.
- (iv) *Kashmiri specialist data* (600k-ks-ocr, CC-BY-4.0, ~10.6 GB) — needs the boss's download approval; ks is Sarvam's worst cell.
- (v) *Normalisation/evaluation flaw* found by 1B/1D (e.g. ZWJ/ZWNJ or nukta handling changing scores) — only if 1B's diff shows a real effect.

## 2. Adversarial refutation — 3 subagents per candidate, ≤5 in flight (run in rounds)
Each attacker gets: shared context block + the candidate block + ONE lens prompt below. Instruction to all: **"Your job is to KILL this thesis. Default to REFUTED
when uncertain — a weak thesis reaching the meeting is worse than a good one wrongly killed. Return: REFUTED / SURVIVES / WOUNDED (survives only with a named
change), the strongest evidence (URLs opened, file:line), and the single best counter-argument."**

- **Lens (a) — incumbents already do it.** Search live for Sarvam, Google (Document AI / Gemini OCR), Microsoft (Azure Read), Bodhan, AI4Bharat/IndicPhotoOCR,
  published papers 2024–2026 doing this or something that subsumes it. If they do, the thesis is not an edge. Queries logged.
- **Lens (b) — the mechanism fails on real Indic input.** Attack each link of the causal chain against: complex conjuncts and matras; near-zero-data scripts
  (Ol Chiki, Meetei Mayek); cursive Nastaliq (ur, ks); degraded scans; mixed-script pages; our actual numbers in `docs/campaign/BENCHMARK_22.md` and `sheet.csv`.
  Where a quick read-only measurement on `sheet.csv` can test the mechanism (e.g. oracle-vs-best gap for routing), do it and report the number.
- **Lens (c) — cannot be built in time.** ~5 development days, one operator, no training started (paused), no Sarvam calls left, no new downloads without approval,
  M2 Max with ~9–12 GB for training. Estimate honestly in dev days with the steps listed; anything needing an unapproved download or training is WOUNDED at best.

**Survival rule:** a candidate survives only if fewer than 2 of 3 lenses return REFUTED. WOUNDED counts as survive-with-change (apply the named change).

## 3. Write `docs/campaign/EDGE_THESIS.md`
Sections: (1) one-paragraph verdict (how many survived; zero is an acceptable, honest result — then say what we would need to find one);
(2) each survivor: full candidate block + the three lens verdicts with their best counter-argument + what changed after WOUNDED + falsification test to run first;
(3) killed candidates: one paragraph each, which lens killed it and why — the boss wants the reasoning; (4) sources. ≤1,500 words.

## 4. Checks
Verdict cross-check ([[proto-91-verdict-cross-check]]) with special attention to: every "incumbents haven't done it" claim backed by the searches lens (a) ran;
every cost estimate listing its steps. Checkpoint records candidates, lens verdicts, survivors.

Related: [[proto-15-w1e-edge-hunt]], [[proto-19-w1h-draft-research-plan]], [[proto-51-w5-architecture-freeze]]
