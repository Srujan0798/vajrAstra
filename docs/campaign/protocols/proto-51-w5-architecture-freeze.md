---
name: proto-51-w5-architecture-freeze
description: "Wave 5 part 2 — ARCHITECTURE_FREEZE.md is produced only at the all-agent architecture call after Vinay's decisions; gates, pre-call packet, call agenda, and the freeze document layout (CO-053/054/055/059)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:16:57.621Z
---

# WAVE 5 · PART 2 — ARCHITECTURE FREEZE → `docs/campaign/ARCHITECTURE_FREEZE.md` (D09)

**Hard gate:** written only at (or immediately after) the architecture call, after the boss reports Vinay's decisions. Level 7 stays frozen until then (CO-059).
Never pre-write the freeze. Never start training from it without the boss's explicit go (W6 is PAUSED; `src/` tree is U3).

## Gates that must be true before the call (Verdict checks, lead records)
1. `EDGE_THESIS.md` is evidence-backed (survivors with falsifiers) or explicitly empty.
2. `DRAFT_RESEARCH_PLAN.md` was presented; the boss has written down Vinay's answers (U4 option + backbone, download approvals, W6 go/no-go) — ask for them if missing.
3. `BENCHMARK_22.md` and `SAMPLING_PLAN.md` exist; the scored set is named (1,227 or 1,283 after U5).
4. `MULTI_LLM_EVAL.md` critiques are dispositioned.
5. `docs/research/level7/KILL_CRITERIA.md` K1/K2 re-read; any kill that fires is honoured.

## Pre-call packet (lead, ≤2 pages) → `docs/campaign/checkpoints/W5_reports/precall.md`
Vinay's decisions verbatim (from the boss) · chosen option and backbone · what changes vs the lead's PPT 4-stage architecture · per-language routing table
(from `PER_LANG_ROUTING.md` updated with 1B numbers) · data per training language (SAFE tiers only; barred: ks, mni, ur, sat, mr, ne-PDF) · compute/memory plan ·
kill criteria · open risks.

## The call (all three roles as subagents + the boss)
Agenda: (1) read decisions; (2) Engine presents the build plan; (3) Verdict attacks it (hostile pass, same lenses as [[proto-16-w1e-edge-refutation]]); (4) Miss lists
dependencies and approvals; (5) the boss decides; (6) freeze. CO-054 bar: "architecture so strong others would try to steal it" — the evidence must show why, or the doc says it doesn't yet.

## `ARCHITECTURE_FREEZE.md` layout
1. Decision record (who decided what, when). 2. Architecture diagram (mermaid) with every component's source (model, licence, on disk or approval needed).
3. Per-language plan (route, engine, training yes/no, GT tier, n). 4. Training plan (only if approved): data, backbone, method, compute, smoke test first, kill criteria.
5. Evaluation plan: set, metric, normalisation (aligned with Sarvam's per 1B diff), significance test, n ≥ 50 rule. 6. What is explicitly out of scope.
7. Change control: any change after freeze needs the boss + a Verdict note.

Related: [[proto-50-w5-repo-map-and-drift]], [[proto-19-w1h-draft-research-plan]], [[proto-92-boss-decisions]]
