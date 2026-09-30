---
name: proto-10-w1-overview
description: "Wave 1 (meeting gate, before Vinay meeting Wed 2026-09-30) — goal, the lead's actual asks, batch structure α/β/γ, dependencies, time budget, cut-order, and exit gate"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:10:49.151Z
---

# WAVE 1 — MEETING GATE (must finish before the boss meets Vinay, Wed 2026-09-30)

## Why this wave exists
The lead (very likely Vinay, CEO of the boss's team Vaultstack AI) asked, in the raw transcript of `MEETING_2026-09-29_STRUCTURED.md`, for:
1. an **initial draft research plan** he can cross-question in a **15–20 minute session** ("you present the plan, we can cross question each other… then we execute");
2. **hybrid integration of existing models**, not a new backbone ("research on existing models and what are the best hybrid way of integrations");
3. **benchmarks for all 22 languages**, 5–10 samples each ("you have done for South Indian languages only, no? So just cover the other languages also before giving your final");
4. **multi-LLM evaluation** of the plan by OpenCode, Claude and ChatGPT ("by the process mentioned, not by the AI mentioned");
5. a research method: Consensus.app (10 free searches/day), an OCR-training flowchart, last-6-weeks breakthroughs, and a comparison with the PPT architecture.

What exists: `VINAY_MEETING_PACKET.md` (root, 26.8 KB, "READY"), `EVIDENCE_SUMMARY.md`, `PER_LANG_ROUTING.md`, `COMPUTE_BUDGET_ESTIMATE.md`, 3 copies of
`W5_BEAT_SARVAM_PLAN.md` (root, `docs/architecture/`, `docs/research/level7/`), 2 of `W5_STRATEGY_OPTIONS.md` (`docs/architecture/`, `docs/research/level7/`),
`PPT_VS_SPEC_DIFF.md`, `PPT_FULL_DUMP.md`, heavy live research. What does NOT exist: a 22-language score table, a multi-LLM evaluation, a training flowchart,
a draft research plan in the lead's format. And the packet carries claims that would not survive cross-examination (see [[proto-11-w1a-packet-audit]]).

**Wave goal:** the boss walks in with (a) a packet whose every number is true and states its n, and (b) `docs/campaign/DRAFT_RESEARCH_PLAN.md` in the
lead's own format, backed by the 22-language table, competitor intel, edge thesis (or an honest "none survived") and a multi-LLM critique.

## Batches and dependencies
```
α (parallel, ≤5):  1A packet audit (Verdict) | 1B 22-lang table (Engine) | 1C mentor playbook (Miss) | 1D competitor intel (research) | 1E-hunt (research)
                        │                           │                          │                          │                        │
γ-early:           1G apply 1A fix-specs + Verdict re-verify  (starts as soon as 1A returns)
β:                 1E-refute (lead drafts 3–5 candidates from 1A–1D + hunt → 3 adversarial lenses each, rounds of ≤5)
β2:                1F multi-LLM eval (needs 1B, 1D, 1E results; ChatGPT leg needs the boss)
γ-final:           1H DRAFT_RESEARCH_PLAN.md (lead) → Verdict cross-check → pointer at top of VINAY_MEETING_PACKET.md
```

## Time budget (Sonnet wall-clock, rough)
α ≈ 45–90 min in parallel · 1G ≈ 30–45 min · 1E-refute ≈ 60 min · 1F ≈ 30 min + boss's ChatGPT paste · 1H ≈ 30 min · checks ≈ 30 min.

## Cut-order if time runs out (keep the top ones)
1G packet corrected → 1B table → 1H draft plan → 1C → 1D → 1F → 1E. A short, true packet beats a long one with one false claim. Tell the boss what was cut.

## Files this wave may write (and only these)
`level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` (create folder) · `docs/campaign/BENCHMARK_22.md` · `level2/unified/build_benchmark_22.py` ·
`docs/campaign/MENTOR_PLAYBOOK.md` · `docs/campaign/COMPETITOR_INTEL.md` · `docs/campaign/EDGE_THESIS.md` · `docs/campaign/MULTI_LLM_EVAL.md` ·
`docs/campaign/CHATGPT_EVAL_PROMPT.md` · `docs/campaign/DRAFT_RESEARCH_PLAN.md` · `docs/campaign/checkpoints/W1.md` + `W1_reports/` ·
the meeting documents named in the 1A fix-specs (after pre-images are archived) · `DISPATCH_LOG.md` (append) · `OCR_AGENT_MEMORY_FEED.md` §11 (append).

## Exit gate (all must hold; Verdict checks)
- Every numeric claim in `VINAY_MEETING_PACKET.md` is VERIFIED or removed (1A ledger, 1G verify log).
- `BENCHMARK_22.md` exists, shows labelled n **and** scored n for all 22 languages, reproduces `EVIDENCE_SUMMARY.md` §3.
- `MENTOR_PLAYBOOK.md`, `COMPETITOR_INTEL.md`, `EDGE_THESIS.md`, `MULTI_LLM_EVAL.md` (ChatGPT leg may be "pending boss"), `DRAFT_RESEARCH_PLAN.md` exist.
- `DISPATCH_LOG.md` has one Wave-1 entry; `docs/campaign/checkpoints/W1.md` ends `STATUS: COMPLETE`.
- The boss has a ≤10-line report, the ChatGPT paste request, and the U1–U5 questions ([[proto-92-boss-decisions]]).

Related: [[proto-00-runbook]], [[proto-11-w1a-packet-audit]], [[proto-12-w1b-benchmark22]], [[proto-19-w1h-draft-research-plan]]
