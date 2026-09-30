---
name: proto-75-vinay-plan-baseline
description: "Added 2026-09-30 — uni C10.3 / CO-089 \"first benchmark: baseline against VINAY'S plan\": stage-by-stage analysis of the lead's 4-stage PPT architecture against measured evidence and every relevant model, what it gets right, what it misses, and what would cross it"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:54:13.049Z
---

# PROTO-75 — BASELINE AGAINST VINAY'S PLAN (research + Verdict) → `docs/campaign/VINAY_PLAN_BASELINE.md`

**Boss:** CO-089 "First benchmark/analysis: baseline against VINAY'S plan — we must cross his plan to even cross Sarvam and the entire India model field." uni C10.3: "full analysis of
EVERY relevant model — starting with VINAY'S PLAN… Prove it with analysis, not confidence." CO-090 is superseded by C9 (prove, then claim).
Note: Vinay is the CEO of the boss's own team; his PPT is the team's baseline architecture — "crossing" it means a demonstrably better plan he will adopt, not a rivalry.

## Inputs
`AksharDrishti_Hackathon_Proposal.pptx` (root) · `docs/research/…/PPT_FULL_DUMP.md` and `PPT_VS_SPEC_DIFF.md` (now under `_reports/research/`; use `find`) · `docs/architecture/PPT_SPEC.md` ·
`docs/campaign/BENCHMARK_22.md` · `docs/campaign/COMPETITOR_INTEL.md` · `docs/campaign/EDGE_THESIS.md` · `docs/campaign/MENTOR_PLAYBOOK.md` (flowchart) · research precursors
(`docs/research/R1_SOTA_MECHANISM_TEARDOWN.md`, `DEEPER_LIVE_RESEARCH_2026-09-29.md`, `LIVE_LATEST_2026-09-29.md`).

## Research subagent — TASK (paste after the shared context block)
> 1. Decompose the PPT architecture into its stages exactly as written (quote slide text): preprocessing (OpenCV), layout (DocLayout-YOLO), recognition (parallel SFT TrOCR + Qwen-VL + PaddleOCR-VL),
>    training (SCST/RL), data plan, evaluation plan, languages covered.
> 2. For each stage: (a) what we have measured on disk that bears on it (engine CERs by script and GT tier, failure taxonomy `level2/reports/FAILURE_TAXONOMY.md`, latency);
>    (b) what 2025–2026 evidence says (open the sources; e.g. current small OCR VLMs, layout models, RL for OCR) — PRIMARY/DERIVED/UNKNOWN;
>    (c) risk for Indic specifically (conjuncts, Nastaliq, Ol Chiki, Meetei Mayek, degraded scans); (d) what the plan omits (e.g. script/language ID for unlabelled test images,
>    confidence routing, normalisation aligned to the evaluation metric, 22-language coverage).
> 3. A comparison table: stage × {Vinay PPT, Sarvam Vision 2.1 (published architecture), Bodhan, our measured wrap-only routing, Option A, Option D} with evidence per cell.
> 4. "What crosses his plan": the smallest set of changes to the PPT that the evidence supports, each with its measured or cited basis and cost in days. No claim without evidence.
> Write only `docs/campaign/VINAY_PLAN_BASELINE.md` (≤2,000 words + tables).

## Verdict check
Every PPT quote verbatim; every cell sourced; "crosses" claims labelled as hypotheses unless measured.

Related: [[proto-19-w1h-draft-research-plan]], [[proto-14-w1d-competitor-intel]], [[proto-78-submission-readiness]]
