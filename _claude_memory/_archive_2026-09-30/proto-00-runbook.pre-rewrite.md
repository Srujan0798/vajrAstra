---
name: proto-00-runbook
description: "MASTER RUNBOOK for Sonnet — the order to read and execute the Opus-written protocol files (proto-01 … proto-93), how to pick the next step, how to dispatch, checkpoint and report; read this first every session"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:56:55.837Z
---

# RUNBOOK — Sonnet executes, Opus planned (written 2026-09-29 ~21:00 IST by Opus 5.5 at max effort)

You are the **lead** (orchestrator-executor) of the South / AksharDrishti Indic OCR campaign, repo `/Users/srujansai/Desktop/South`.
The Opus planner already read the repo, measured the state on disk and wrote every task as a protocol file in this memory folder.
Your job: execute them faithfully, deeply and in order, using **Sonnet subagents** for the labour. You do not re-plan. You may
correct a protocol only when disk evidence contradicts it; record the correction in the wave checkpoint.

## 0. Every session starts like this (≈5 minutes)
1. Read, in order: this file → [[proto-01-law-and-guardrails]] → [[proto-02-preflight-and-checkpoints]] → [[proto-90-templates]].
2. Read `docs/campaign/CAMPAIGN_DIRECTIVE.md` Part A (verified state) and Part S (decisions U1–U5). Do not read the whole file.
3. Run the pre-flight in [[proto-02-preflight-and-checkpoints]] and write its output into the current checkpoint.
4. Find the next step (table below): the first step whose checkpoint line is not `DONE`.
5. Open that step's protocol file and execute it exactly. One step's protocol file is self-contained: sources, commands, subagent prompts, output template, done-criteria.

## 1. Step table (execution order — do not skip ahead)
| Step | Protocol file | Who | Output | Depends on |
|---|---|---|---|---|
| W1 overview | [[proto-10-w1-overview]] | lead | plan of Wave 1 | — |
| 1A | [[proto-11-w1a-packet-audit]] | Verdict subagent | `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` | — |
| 1B | [[proto-12-w1b-benchmark22]] | Engine subagent | `docs/campaign/BENCHMARK_22.md` + script | — |
| 1C | [[proto-13-w1c-mentor-playbook]] | Miss subagent | `docs/campaign/MENTOR_PLAYBOOK.md` | — |
| 1D | [[proto-14-w1d-competitor-intel]] | research subagent | `docs/campaign/COMPETITOR_INTEL.md` | — |
| 1E-hunt | [[proto-15-w1e-edge-hunt]] | research subagent | hunt report (in checkpoint) | 1D helpful |
| 1E-refute | [[proto-16-w1e-edge-refutation]] | lead + 3 adversarial subagents per candidate | `docs/campaign/EDGE_THESIS.md` | 1A–1D + hunt |
| 1F | [[proto-17-w1f-multi-llm-eval]] | lead + OpenCode + reviewer subagent + boss (ChatGPT) | `docs/campaign/MULTI_LLM_EVAL.md`, `CHATGPT_EVAL_PROMPT.md` | 1A–1E |
| 1G | [[proto-18-w1g-apply-verify]] | Miss applies, Verdict verifies | corrected packet + verify log | 1A |
| 1H | [[proto-19-w1h-draft-research-plan]] | lead | `docs/campaign/DRAFT_RESEARCH_PLAN.md` | all of W1 |
| W2 | [[proto-20-w2-sampling-reconcile]] → [[proto-21-w2-variance-and-resource]] | Engine + Verdict | `docs/campaign/SAMPLING_PLAN.md`, `level2/unified/manifest_22.json` | W1 done, after meeting |
| W3 | [[proto-30-w3-skill-inventory]] → [[proto-31-w3-laya-jev-verdict]] | Miss + Verdict | `docs/campaign/SKILL_STACK.md` | W1 done |
| W4 | [[proto-98-clean-repo-master]] (master order) → [[proto-95-research-harvest-decisions]] → [[proto-96-archive-reports-compaction]] · [[proto-97-research-still-to-do]] (proto-40 superseded) | Verdict decides, Miss executes, Verdict verifies | `docs/campaign/RESEARCH_DECISIONS.md`, `docs/campaign/audit/RESEARCH_FATES.csv`, `_archive/INDEX.md` | W1 done |
| W5 | [[proto-50-w5-repo-map-and-drift]] → [[proto-51-w5-architecture-freeze]] | Miss + Verdict; freeze at the call | `FINAL_REPO_MAP.md`, errata, `ARCHITECTURE_FREEZE.md` | U1 answered; the call |

Always-on support files: [[proto-91-verdict-cross-check]] (how every output is verified), [[proto-92-boss-decisions]] (U1–U12 and how to ask),
[[proto-93-measured-facts]] (numbers the planner measured, with the command that reproduces each), [[proto-99-concern-crosswalk]] (every boss concern → status → protocol),
[[proto-60-monitor-and-checkpoint-discipline]], [[proto-79-council-briefing-prompts]].

## 1b. ADDED 2026-09-30 by the Opus monitor — the full order from now to completion (supersedes the table above where they differ)
| Phase | Steps (protocol files) | Gate |
|---|---|---|
| **W1-finish (meeting day, TODAY)** | [[proto-64-meeting-day-finish]] + **[[proto-86-draft-plan-fixes]] (13 verified defects in the plan the boss presents — do these first)** + [[proto-85-boss-explainer-and-question-bank]] (explain card + top-10 Q&A if time) | before the Vinay meeting; D12 guard: no new scope |
| **W1.5 integrity** | [[proto-61-sheet-provenance-forensics]] · [[proto-62-gt-tier-stratified-reporting]] · [[proto-65-gt-defects-register]] · [[proto-66-concern-register-rebuild]] · [[proto-80-hackathon-metric-alignment]] · [[proto-82-engine-empty-output-patterns]] · [[proto-83-licence-verification]] | after meeting |
| **W2 data** | [[proto-20-w2-sampling-reconcile]] → [[proto-21-w2-variance-and-resource]] · [[proto-71-south-rerun-same-standard]] Phase A | U5, U11 for execution |
| **W2.5 structure (the boss's level2/hierarchy concern)** | [[proto-72-per-file-audit]] (read-only, can start right after the meeting; research files and `_archive`/`_reports` take their verdicts from proto-95/96 — import, don't re-judge) → [[proto-70-level2-restructure]] Phases 0–1 → U10 → Phases 3–5 · [[proto-73-md-fact-consolidation]] · [[proto-74-root-hidden-hygiene]] · [[proto-63-single-canonical-files]] | U10, U12 |
| **W2.7 coverage + law** | [[proto-81-handwriting-degraded-coverage]] · [[proto-84-law-hierarchy-consolidation]] | U13 |
| **W3 tools + streams** | [[proto-30-w3-skill-inventory]] · [[proto-31-w3-laya-jev-verdict]] · [[proto-76-workstreams-and-agent-health]] · [[proto-77-graph-concerns]] | — |
| **W4 clean repo + research (boss 2026-09-30)** | **[[proto-98-clean-repo-master]]** — Phase 0 freeze → 1 map (graphify, inventories, primary sources → docs/sources/) → 2 read + rate every file ([[proto-95-research-harvest-decisions]] ∥ [[proto-72-per-file-audit]]) → 3 topic finals → 4 execute (proto-74/63, [[proto-96-archive-reports-compaction]]; proto-70 after U10) → 5 verify + map · [[proto-97-research-still-to-do]] (RQs run inside Plan v3 days) · [[proto-75-vinay-plan-baseline]] | U29–U32 decided; new U# rows from the harvest |
| **W5 close** | [[proto-50-w5-repo-map-and-drift]] · [[proto-78-submission-readiness]] · [[proto-51-w5-architecture-freeze]] | U1, U2, U4; the call |
Parallel-safe pairs (different files): W1.5 with W2.5 Phase 0–1 (read-only); W3 with W4. Never run W2.5 Phase 3 (moves) while any engine run or other writer is active.
Every step starts by reading its rows in [[proto-99-concern-crosswalk]] and ends by updating those rows in `BOSS_CONCERNS.md`.


## 1c. ADDED 2026-09-30 — PLAN V2 (after the Vinay meeting): execute [[proto-87-plan-v2-execution]] as the spine of the next five days
Plan v2 folds W1.5 (61, 62, 80, 82, 83) into its Day 1, adds the comparable-number step (Day 2) and ONE leakage-controlled fine-tune (Day 3), then coverage + submission (Day 4) and re-score (Day 5).
The structure waves (70, 72, 73, 74, 63, 66, 84) run in parallel only when they touch different files and never during engine runs. Waves 3–5 follow after Day 5.

## 1d. ADDED 2026-09-30 ~14:45 — PLAN V3 ([[proto-89-plan-v3-bodhan-base]]) supersedes Plan v2's recogniser choice
Day 1 of Plan v2/v3 is the same except the baseline run includes Bodhan (proto-89 §A); from Day 2 on, follow proto-89 (Bodhan base, block-level leak-free data, local QLoRA) instead of proto-87 §B.
Tools and approvals: [[proto-94-tool-integration]] (U23–U28 in proto-92).

## 2. Parallelism
- Wave 1 batch α = 1A, 1B, 1C, 1D in parallel (4 subagents), plus 1E-hunt as the 5th if nothing else is running. Then 1E-refute rounds (≤5 in flight),
  then 1F, then 1G (can start as soon as 1A returns), then 1H last.
- Never more than 5 subagents in flight. Every subagent: `model: "sonnet"`. Never Opus.
- The lead never does a subagent's broad labour itself, but the lead **does** compose every deliverable from reports (subagents return evidence, the lead writes).
  Exception: a protocol that says "the subagent writes file X" — then only that file.

## 3. After every step
1. Verdict cross-check per [[proto-91-verdict-cross-check]] (a separate Sonnet subagent, never the author). Max 2 fix rounds, then escalate to the boss.
2. Update `docs/campaign/checkpoints/W<n>.md` (template in [[proto-90-templates]]): step → DONE with the evidence line.
3. At wave end: append one `DISPATCH_LOG.md` entry, tick closed rows of the directive's Part G0 crosswalk (only with reproducing evidence),
   send the boss a ≤10-line report (template in [[proto-90-templates]]). Continue to the next wave unless the boss said stop or a U-decision blocks it.

## 4. Deadline logic
Wave 1 must be complete **before the boss's meeting with Vinay on Wed 2026-09-30**. If time runs short, the priority inside Wave 1 is:
1G (packet corrected — removes false claims) > 1B (22-language table — the lead's explicit ask) > 1H (draft research plan) > 1C > 1D > 1F > 1E.
A short, true packet beats a long one with one false claim. Tell the boss what was cut.

## 5. When a protocol is wrong
If disk contradicts a protocol (a path moved, a count changed), do not improvise silently: re-measure, follow the evidence, write
`PROTOCOL-DEVIATION: <what> — <evidence>` in the checkpoint, and mention it in the wave report.

Related: [[sonnet-handoff]], [[campaign-state]], [[model-tiering]], [[boss-standard]]
