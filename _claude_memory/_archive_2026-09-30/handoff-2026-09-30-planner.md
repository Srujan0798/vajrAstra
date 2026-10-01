---
name: handoff-2026-09-30-planner
description: "START HERE (next planner session) — the Opus planner's handoff at 2026-09-30 ~22:35 IST, written when credit ran out: the project state, every agent's state, what the memory consolidation finished and what is still half-done, the exact next steps, and the rules the boss enforces"
metadata:
  type: project
---

# PLANNER HANDOFF — 2026-09-30 ~22:35 IST (read fully before doing anything)

## 1. Who and what
- **The boss** (Srujan, Vaultstack) runs the AksharDrishti hackathon project in `/Users/srujansai/Desktop/South`.
  - **Goal:** win, beating Sarvam Vision 2.1 and every competitor, with a PORTABLE product (PyTorch/CUDA/CPU; MLX only as a Mac accelerator) that goes to the organisers and then everyone.
  - **Budget:** free only.
  - **Team:** no team mates (Krishna/Aryan/David never appear in plans). Vinay is the lead to inform.
- **His three OpenCode agents do the labour:**
  - Agent 1 Engine `ses_f12a7b89cffet3Qff6UxLW7fYD`
  - Agent 2 Verdict + repair lead `ses_f1233a0a5ffeRSOBSwI87lmxxv`
  - Agent 3 Miss/builder `ses_f16bc20eaffe6J4emd9qVYK7CQ`
- **The planner** (you) writes protocols into this memory, checks state with its own reads, and gives the boss one-line paste lines per agent. Labour only when the boss says "you do it". Subagents only when he asks, Sonnet only, never Opus.
- **Routed skills** (proto-88) before each piece of work, and say which were used: readchk, factchk, mandela, ssotize, verification-before-completion, graphify. Full-file reads. Lists not tables. One agent at a time.

## 2. THE plan
**proto-104 rev 4 (top section)**:
- goal;
- measured facts;
- rulings R-1…R-15;
- steps: R repair → S South from Sarvam-bench fill (R-7) → H handwriting (the official test set = handwritten word crops; the planner viewed 3 = Bengali script) → D1 Bodhan (official weights on the PyTorch path + MLX port, parity) → X external bench on all 22 languages → C Consensus (proto-105) → G the Plan v3 draft for Vinay → GPU when SSH arrives → D2–D5;
- the paste lines in its §6.

Read order: proto-00 (rewritten tonight: read order + where every old protocol lives) → proto-104 → proto-01 → proto-88 → BOSS_CONCERNS.md → proto-103.

## 3. Agents' last measured state (21:00–22:30; re-check W4.md / DISPATCH_LOG.md first)
- **Agent 2:**
  - A0–A3 PASS.
  - A4 CONDITIONAL: the `run_probe.py` `parents[2]` base-path fix is an APPROVED path erratum (R-2); A4 PASS = 0 old-path hits in run_probe.py + the smoke test.
  - A5 open. Then: LAYOUT FROZEN, .gitignore `level2/models_bodhan/`, root strays `out_level3/` + `W4_reports/` → `_archive/stray_2026-09-30/`, verify S2, proto-105, step G.
- **Agent 3:**
  - S1 DONE for real: 0/23,001 official South PDF pages clean.
  - S2 (South from Sarvam-bench fill, ≤100 per language) was paused asking for U9/U24 — both are already approved. The rev 4 paste line tells it to continue.
  - `product/` layer exists (built 20:43).
- **Agent 1:**
  - D0 DONE.
  - H1 in progress (`docs/campaign/H1_TEST_PROFILE.json`, `B12_HANDWRITING_SHARE.md`).
  - Sarvam bench downloaded to `level2/models_bodhan/indic-ocr-bench`.
  - mlx + mlx-vlm installed.
  - **Bodhan BLOCKED:** 403 for Maya0769 (gated=auto; the form was never submitted from that account). BOSS ACTION: while logged in as Maya0769, submit the access form on huggingface.co for `bodhan-ai/indic-ocr`, `hari31416/indic-ocr-mlx-4bit`, `hari31416/indic-ocr-mlx-bf16`. Check: `.venv/bin/python -c "from huggingface_hub import auth_check; auth_check('bodhan-ai/indic-ocr')"`.
- **Vinay** (second-hand, via the vajrAstra session handoff): a 24 GB GPU over SSH arrives 2026-10-01; call on the morning of 2026-10-01.
- **Unknown:** whether the boss pasted the rev 4 paste lines. Check DISPATCH_LOG.

## 4. Memory consolidation (the boss: "merge, delete variants, make the md files big and consistent; verify what is complete")
**DONE:**
- `history-completed-protocols.md` (26 protocols merged verbatim with verified statuses: proto-10…21, 30, 31, 40, 51, 61, 64, 66, 83, 86, 87, 94, campaign-state, open-front, sonnet-handoff).
- `proto-98-clean-repo-master.md` = the cleanup master, PARKED (proto-95, 96, 101, 70, 72, 73, 74, 77, 84, 63, 50 merged).
- 37 originals moved to `_archive_2026-09-30/` (nothing deleted).
- `proto-00` rewritten; `user-profile` updated.
- graphify skill updated to 0.9.65 for claude/opencode/agents.
- `AGENTS.md` start block + `scripts/agent_bootstrap.sh` point to proto-104 (pre-images in the scratchpad: `/private/tmp/claude-501/-Users-srujansai-Desktop-South/8e7ec69e-22b6-4702-a989-3397b9a99c1e/scratchpad/AGENTS.pre-consolidation.md`, `agent_bootstrap.pre-consolidation.sh`).

**NOT DONE (the two Sonnet agents were stopped before writing anything):**
- **Task B — concerns + meetings:**
  - merge every concern (BOSS_CONCERNS.md Part 1 + proto-99: CO-001…096, C1–C17, uni items, M1–M8, #1–#81, HL1–HL12, H1–H15) into ~30 themes K-01…K-30. Draft theme list: win/beat all · portable product · handwriting/test set · the lead's method · one 22-language benchmark with South merged · 100 independent samples per language · evidence/honesty · leakage/fair eval · incident safety · repo cleanliness · research harvest + use · tools (graphify/ECC/Laya) · agent process · memory/concerns stored · meeting truth + PPT baseline · levels in order · licences · sealed dirs · GT defects register (`GT_DEFECTS.md` missing) · empty-output patterns · metric set · submission readiness · explain card · other workstreams · dates · GPU · Sarvam budget · graph concerns · Sep-16 correction owed to Vinay · clock;
  - each theme with a status verified by a command + owner step;
  - write it into proto-99 §0 AND `BOSS_CONCERNS.md` Part 0 (before Part 1; Part 1 is append-only);
  - plus proto-103 §0 = every meeting in one place (Sep 9 WhatsApp, Sep 10, Sep 25, Sep 29, Sep 30 decisions + Vinay's 4 second-hand answers).
- **Task C — law/rules/tools/decisions:**
  - proto-01 absorbs proto-02, 60, 62, 79, 90, 91 and campaign-law, plus a LAW ORDER block;
  - `boss-rules.md` (feedback) absorbs boss-standard, model-tiering and both feedback-* files, plus 8 current rules (planner no labour unless told; subagents only on request, Sonnet; no team mates; portable product/MLX never assumed; win = effort never law-breaking; routed skills every time; full reads + graphify; lists, one agent at a time);
  - proto-88 gets a `STATUS 2026-09-30` section (graphify, ECC with which skill per step, Laya NOT used, Consensus, `.venv311` = THE env for engines/scoring, `.venv` = Python 3.14, MCPs) and absorbs agent-automation-setup;
  - proto-92 absorbs conflicts-register;
  - proto-93 gets F73–F80 (the facts are in proto-104 §1);
  - proto-97 gets RQ statuses (RQ-1/3/7/9/12 DONE, RQ-2 → H1, RQ-10 TRIGGERED, rest OPEN);
  - proto-100 gets B-18 post-correction, B-19 handwriting LoRA, B-20 legacy-font→Unicode South GT, B-21 synthetic lines — check first: proto-100 already shows one "B-18" hit;
  - proto-104 gets APPENDIX A (verbatim proto-65, 71, 75, 76, 78, 80, 81, 82 + step Q = GT_DEFECTS.md before D2), inserted before its `# HISTORY` line;
  - archive each merged source.
- **After B and C:** rebuild `MEMORY.md` (it still lists the archived ids); run `bash scripts/agent_bootstrap.sh --sync-only`; then MOVE (not delete) the stale mirror copies in `docs/campaign/protocols/` whose memory source is archived → `docs/campaign/protocols/_archive_2026-09-30/`.

## 5. The repo md hierarchy (the boss, 22:30: "AGENTS.md is total trash… hierarchy not connected… where is my hybrid concern… merge variants… are we using the research or not")
- **AGENTS.md:**
  - below the START HERE block it is STALE: the CAMPAIGN_DIRECTIVE v5 "active law", the Level-7 clock, old graph numbers, the "WHO I AM" orchestrator block, the Tue 2026-09-30 meeting.
  - Rewrite it short: project + goal; START HERE; hard rules (incl. rules 17–21, portable, no team mates); the 3 agents; the ONE doc hierarchy with links; a list of historical docs marked read-only history.
  - Link `level2/ULTIMATE_HYBRID_CONCERN.md` (the South-era operator law HL1–HL12, still binding where not superseded) in the law chain.
- **Also rewrite:** `docs/INDEX.md` (stale: FULL TECHNICAL BRIEFING as master, LEVEL7 as active law) and `README.md` (stale: "A9 PASS" gate, Vinay packet "tomorrow").
- **Root md files that are stale or misleading:**
  - PROJECT_COMPLETE.md — misleading: the project is NOT complete;
  - AUDIT_REPORT.md, CLEANUP_EXECUTION_LOG.md, PROTOCOL_UPGRADES.md, W5_FREEZE_PLAN.md, LOOP_SPEC_W5_W6_W7.md, INTEGRATED-ELITE-STACK.md, PAPERTHIN_AUDIT.md, LIVE_LATEST_2026-09-29.md, VINAY_MEETING_PACKET.md, SAMPLE_PLAN_18_LANGS.md, FULL TECHNICAL BRIEFING.md, OCR_AGENT_MEMORY_FEED.md (212 KB of history + process law).

  The proto-98 master has the rules to move/merge them: bundle + sha + log line; the boss's "go".
- **Scale:** docs/research has 88 md files, docs/campaign 127, _reports 50+, _archive 150+.
- **graphify:** `graphify update .` was started and STOPPED. graph.json is still the 14:34 version (valid, 6,796 nodes; backup `…/scratchpad/graph.pre-update.json`). Re-run it, then use GRAPH_REPORT islands/orphans for the hierarchy work.
- **Research use (honest):**
  - `RESEARCH_DECISIONS.md` = 24 RF rows;
  - the Consensus answers are stored (`docs/sources/consensus/`) and mapped in proto-105, but Agent 2 has NOT processed them yet;
  - B-01/B-02/B-12 prep analyses exist (`docs/campaign/B01_4BIT_ANALYSIS.md`, `B02_ARABIC_NORMALIZATION.md`, `B12_HANDWRITING_SHARE.md`);
  - the 88 docs/research files were never harvested (proto-95, now inside the proto-98 master, parked).

  The boss wants the research used: un-park the harvest for Agent 2 after proto-105.

## 6. Hard rules for the next planner
- no Opus subagents;
- no commit/push without the boss;
- never delete — move to an archive with a log;
- no downloads/Sarvam spend/training without the boss (Sarvam: only the 12 approved South calls, R-8);
- sealed dirs `level2/out`, `level2/reports`, `Datasets/` are read-only;
- `.env` holds the Sarvam key — never print it;
- NEXT.md is planner/boss only;
- never say done without a reproducing command.

The full transcripts of this planner session are in `~/.claude/projects/-Users-srujansai-Desktop-South/` (`8e7ec69e-….jsonl` and `c2d53b6f-….jsonl`).
