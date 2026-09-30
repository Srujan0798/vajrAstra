---
name: proto-19-w1h-draft-research-plan
description: "Step 1H (lead) — write DRAFT_RESEARCH_PLAN.md, the 15–20 minute document the boss presents to Vinay, in the lead's own requested order, section by section with sources, word budgets and the honesty rules"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:14:37.384Z
---

# STEP 1H — THE DRAFT RESEARCH PLAN (lead writes) → `docs/campaign/DRAFT_RESEARCH_PLAN.md`

**Why:** the lead asked for "this initial draft research plan. I'll discuss it with you, and then we will finalize" in "a 15–20 minute session… you present the plan,
we can cross question each other". The existing packet is a 5-minute decision menu. This document is what the boss actually presents; the packet becomes the evidence appendix.
**Written last in Wave 1**, from the verified outputs of 1A–1G. The lead writes it (it is composition, not labour). ≤4 printed pages (~1,800 words) + tables.

## Structure (follow the lead's own order of thinking from the transcript)
**Title block:** "AksharDrishti — Draft Research Plan for review" · date · prepared by the boss · status DRAFT for cross-questioning · one line: "Every number states its n; sources in the appendix."

1. **The problem and the bar (≈120 words).** Beat Sarvam Vision 2.1 on Indic OCR across 22 languages, honestly. What their headline 87.39 is and is not comparable to
   (from 1D's comparability table). Our rule: no claims without n.
2. **How an OCR model is trained — the flowchart (≈150 words + the mermaid chart from 1C).** Mark BUILT / SPEC-ONLY / PAUSED on each node. This answers his first step.
3. **Where we stand today — the 22-language benchmark (≈250 words + the coverage table and a compact CER table from 1B).** Scored n per language; best local engine per
   language with n ≥ 50; the South small-n finding (kn/ml ≈4 scored pages); the Sarvam paired result stated exactly as 1A wrote it (n=3/lang, directional); what is weak
   (Santali, Meetei Mayek, Nastaliq, degraded scans).
4. **What changed in the field in the last 6 weeks (≈250 words).** From 1D + the research precursors (`LIVE_LATEST_2026-09-29.md`, `DEEPER_LIVE_RESEARCH_2026-09-29.md`):
   at most 6 items, each "what it is · why it matters for our weak cells · status (usable now / needs download approval / watch)". Only items with an opened source.
5. **Proposed hybrid integration vs your PPT (≈350 words + a 2-column table).** PPT 4-stage baseline (OpenCV → DocLayout-YOLO → parallel TrOCR + Qwen-VL + PaddleOCR-VL →
   SCST/RL) vs what the evidence now supports. Present **Option A** (wrap-only routing + QLoRA on kok+pa) and **Option D** (wrap + script-router + restoration pre-pass +
   Sarvam subsidy for sat/mni) side by side: what ships, cost, risk, evidence, which cells each moves. Backbone question (Qwen2.5-VL-3B vs GLM-OCR 0.9B) with the evidence
   from 1A K5. State our recommendation and label it a recommendation.
6. **Our edge (≈250 words).** Survivors of 1E with mechanism + falsifier, or honestly "no edge survived refutation yet; here is what would give us one".
7. **What the multi-LLM evaluation said (≈200 words).** From 1F: the top critiques, what we accepted and changed, what we rejected and why. ChatGPT leg may be pending.
8. **Questions for cross-questioning (≈150 words).** The decisions only Vinay/the boss can make: U1 (dates), U2 (submission deadline), U4 (Option A vs D, backbone),
   U5 (score the 56 additions, re-draw kok/pa), download approvals (e.g. Kashmiri 600k-ks-ocr, backbone weights), whether W6 training proceeds (the `src/` tree, U3).
9. **Next 5 days if approved (≈120 words).** Day-by-day, each with a kill criterion (from `docs/research/level7/KILL_CRITERIA.md`).
**Appendix:** source list (file:line and URLs), pointer to `VINAY_MEETING_PACKET.md` (corrected), `BENCHMARK_22.md`, `COMPETITOR_INTEL.md`, `EDGE_THESIS.md`, `MULTI_LLM_EVAL.md`, `MENTOR_PLAYBOOK.md`.

## Honesty rules for this document
- No number without its n and metric. No "wins", "beats", "SOTA" unless 1A/1B verified it at n ≥ 50 with the test named.
- Every date weekday-correct; uncertain dates written "TBC".
- If a section's input step was cut for time, the section says so in one line — never fill it from memory.

## Checks and close-out
Verdict cross-check ([[proto-91-verdict-cross-check]]): pick every number in the document and trace it to 1A/1B/1D outputs. Then Miss adds the pointer line to the packet
(if 1G did not). Checkpoint 1H DONE; Wave 1 exit gate ([[proto-10-w1-overview]]); `DISPATCH_LOG.md` entry; boss report ([[proto-90-templates]]) including the
ChatGPT paste request and the U-questions ([[proto-92-boss-decisions]]).

Related: [[proto-10-w1-overview]], [[proto-12-w1b-benchmark22]], [[proto-13-w1c-mentor-playbook]], [[proto-16-w1e-edge-refutation]], [[proto-17-w1f-multi-llm-eval]]
