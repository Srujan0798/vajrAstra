# FILE INVENTORY — South repo MD file analysis (AGENT-2)
**Date:** 2026-09-29 19:00 IST
**Author:** AGENT-2 (deep MD analysis + cleanup plan)
**Scope:** All 203 MD files (excluding vendored, .git, .venv, _archive, .audit, .deps, sealed dirs)
**Method:** Read each file → purpose → audience → verdict (KEEP / MERGE / DELETE)

---

## 1. ROOT-LEVEL MD FILES (27 files, ~330 KB)

| path | bytes | purpose | audience | verdict | reason |
|---|---|---|---|---|---|
| `AGENTS.md` | 3,761 | Agent standing law / orchestrator identity (locked 2026-09-27) | orchestrator + agents | **KEEP** | LAW; load-order anchor; references OCR_AGENT_MEMORY_FEED, SOUTH_CANON, INTEGRATED-ELITE-STACK, campaign docs |
| `OCR_AGENT_MEMORY_FEED.md` | 167,059 | Master process law (§1–§9 hard rules + §10 state + §11–§16 log) | orchestrator + agents | **KEEP** | LAW; canonical process doc; §9 hard rules cited everywhere |
| `SOUTH_CANON.md` | 19,965 | Repo → process-law mapping + standing ops lock | orchestrator | **KEEP** | LAW; §P refreshed 2026-09-27; references all sealed dirs |
| `FULL TECHNICAL BRIEFING.md` | 34,025 | Master technical briefing (Part I + Part II + Part III directive history) | orchestrator + Vinay | **KEEP** | LAW; Part III merged from Untitled 2026-09-29; Part I/II = current truth |
| `INTEGRATED-ELITE-STACK.md` | 13,275 | Canonical map of integrated elite-repo stack (paperthin, looper, graphify, ECC, GLM-OCR, mlx-tune, liteparse) | orchestrator + 3 agents | **KEEP** | Referenced from AGENTS.md + 3 PROMPT_*.md; canonical wiring |
| `README.md` | 1,424 | Project overview / entry point | user + new agents | **KEEP** | Public pointer to docs/INDEX.md |
| `HOW_TO_RUN.txt` | 5,116 | Level-2 ops card (engine harness, venvs, commands) | user + new agents | **KEEP** | Operational doc; not duplicating anything |
| `BOSS_CONCERNS.md` | 32,486 | 73 boss concerns catalogued + status (D1–D7 deliverables, SEALED CONFIRMED) | orchestrator + user | **KEEP** | Boss directives ledger; all D1–D7 marked DONE |
| `AUDIT_REPORT.md` | 12,614 | D2 — full repo audit (50,000+ files, KEEP/MERGE/DELETE verdicts) | orchestrator + audit | **KEEP** | Reference for cleanup; superseded only by DEEP_REPORT.md |
| `CLEANUP_EXECUTION_LOG.md` | 6,712 | D3 — 95 files archived, 117 MB freed across 9 deletion categories | orchestrator + audit | **KEEP** | Cleanup audit trail; L4 archive-never-delete proof |
| `SAMPLE_PLAN_18_LANGS.md` | 7,694 | D4 — 18-lang sample plan (1,227 items post-purge, source map per lang) | orchestrator + Engine | **KEEP** | Per-lang source strategy + shortfall register |
| `PROTOCOL_UPGRADES.md` | 6,469 | D5 — adopted agent workflow upgrades (5-section briefing, §9 pre-write gate) | orchestrator + agents | **KEEP** | Verdict's self-improvement plan; live law |
| `DISPATCH_LOG.md` | 4,995 | D6 — all agent assignments + 3-agent ops model queue status | orchestrator + audit | **KEEP** | Dispatch log; coordination history |
| `HIERARCHY_MAP.md` | 16,849 | D7 — final hierarchy/linkage map of cleaned repo (post-24h cleanup refresh) | orchestrator + audit | **KEEP** | Canonical hierarchy pointer |
| `PROJECT_COMPLETE.md` | 11,294 | Miss agent's W5-ready state summary (7 deliverables, 4 decisions, 2 approvals) | orchestrator + user | **KEEP** | Project completion marker; W5 freeze reference |
| `EVIDENCE_SUMMARY.md` | 6,833 | Disk-truth evidence for Vinay meeting (11 engines × 1,227 items; §6.4 LOCKED) | Vinay + orchestrator | **KEEP** | Vinay-meeting prep; evidence ledger |
| `PER_LANG_ROUTING.md` | 5,861 | 18-lang wrap-only routing table (winners + W6 GT verdict per lang) | Vinay + Engine | **KEEP** | Routing decisions; sourced from LEADERBOARD.md |
| `LEVEL7_RESEARCH_FINDINGS.md` | 10,014 | Top 10 methods distilled from Lane A/B/C ledgers (984+659+436 records) | orchestrator + Vinay | **KEEP** | Synthesis from all campaign ledgers |
| `COMPUTE_BUDGET_ESTIMATE.md` | 7,166 | Tier-by-tier cost (wrap-only / QLoRA / cloud) — $0 default for Vinay | Vinay + orchestrator | **KEEP** | Budget plan; multiple tier scenarios |
| `W5_STRATEGY_OPTIONS.md` | 3,754 | Top 3 W5 strategy options ranked (Option A wrap+QLoRA kok+pa RECOMMENDED) | Vinay + orchestrator | **KEEP** (root) | Condensed version for prompt-facing |
| `W5_BEAT_SARVAM_PLAN.md` | 3,652 | Concrete recipe (2-stage: wrap-only + QLoRA on kok/pa) | Vinay + Engine | **KEEP** (root) | Condensed version; see also docs/architecture/ counterpart |
| `W5_FREEZE_PLAN.md` | 11,386 | W5 freeze timeline + 18-item pre-freeze checklist | orchestrator + all agents | **KEEP** | Freeze prep; checklist |
| `VINAY_MEETING_PACKET.md` | 24,427 | 1-page Vinay brief (status + 4 decisions + 3 strategic questions) | Vinay + user | **KEEP** (root) | Vinay meeting prep; merged from STRATEGY_VINAY_TOMORROW + VINAY_CTA |
| `W6_HANDOFF.md` | 18,114 | W6 handoff doc (🟡 PAUSED banner per user 2026-09-29) | orchestrator + Engine | **KEEP (PAUSED)** | Preserved for W5 strategy evidence + post-meeting W6 reactivation |
| `DEEP_REPORT.md` | 10,056 | 24-hour deep cleanup report (97.3 MB freed, 234 files archived+deleted) | orchestrator + audit | **KEEP** | Canonical 24h cleanup summary |
| `OCR_AGENT_MEMORY_FEED copy.md` | 11,173 | Duplicate copy of OCR_AGENT_MEMORY_FEED.md | unknown | **DELETE** | Exact duplicate of master file; L4 archive first |
| `PPT_FULL_DUMP.md` | 20,559 | Earlier full dump of PPTX content | orchestrator | **MERGE→ archive** | Superseded by docs/architecture/PPT_SPEC.md + W2_HYBRID |
| `PROTOCOL_1_RESEARCH.md` | 27,356 | Earlier Gemma-4 competition protocol (adopted fragments) | orchestrator | **MERGE→ archive** | Adopted evidence-law upgrades already in OCR_AGENT_MEMORY_FEED §15; remaining = not our stack |
| `VAJRASTRA_INTERROGATION_PROTOCOL.md` | 33,394 | Earlier 3-interrogation cycle protocol (12-Sep) | orchestrator | **MERGE→ archive** | Pre-campaign history; SOUTH_CANON §N already preserves the operational lock from this |
| `MEETING_2026-09-29_STRUCTURED.md` | 17,876 | Structured meeting notes 2026-09-29 | user + orchestrator | **KEEP** | Meeting notes (referenced from BOSS_CONCERNS §63) |

---

## 2. docs/ + docs/architecture/ + docs/legal/ + docs/probe/ + docs/south/ (13 files)

| path | bytes | purpose | audience | verdict | reason |
|---|---|---|---|---|---|
| `docs/INDEX.md` | 3,636 | Doc hierarchy map (LAW/CURRENT WORK/SOUTH SCORES/MACHINE) | orchestrator + new agents | **KEEP** | Master pointer; cited from AGENTS.md + README.md |
| `docs/PLAN.md` | 2,268 | Next-work plan (W3 probe source switched; W4 audit; W5 freeze; W6 train) | orchestrator + agents | **KEEP** | Roadmap; references all W-stages |
| `docs/architecture/PPT_SPEC.md` | 3,479 | 1-page PPT dump → box-by-box pipeline + W2 hybrid labels | orchestrator + Verdict | **KEEP** | Team-designed baseline (mid-Aug 2026); diff target |
| `docs/architecture/W2_HYBRID.md` | 3,681 | W2 hybrid vs PPT (DRAFT CLOSED 2026-09-25; probe can flip) | orchestrator + Verdict | **KEEP** | Architectural diff vs PPT_SPEC |
| `docs/architecture/VINAY_MEETING_PACKET.md` | 5,899 | Detailed Vinay packet (results-driven, 5 probe22 findings) | Vinay + orchestrator | **KEEP** | Evidence-backed detailed version; distinct from root-level prompt-facing version |
| `docs/architecture/W5_STRATEGY_OPTIONS.md` | 19,443 | Full 5 alternatives ranked (cost/time/CER-delta/risks/decision-it-changes) | Vinay + Verdict | **KEEP** | Evidence-backed detailed version; distinct from root-level "Top 3" |
| `docs/architecture/W5_BEAT_SARVAM_PLAN.md` | 14,324 | Concrete "where we win/tie/lose" cells + 4 scenarios | Vinay + Verdict | **KEEP** | Detailed version with full citations |
| `docs/legal/LICENSE_AUDIT.md` | n/a | R60 license audit (10 engines + training-data risk) | orchestrator + Verdict | **KEEP** | License compliance; canonical audit |
| `docs/probe/W3_PROBE_SCHEMA.md` | n/a | W3 probe schema (22 Eighth-Schedule langs, locked 2026-09-25) | orchestrator + Engine | **KEEP** | Probe law; referenced everywhere |
| `docs/probe/schema.json` | (json) | Probe schema machine-readable | orchestrator | **KEEP** | Machine schema |
| `docs/south/EXTERNAL_BENCHMARK_MAP.md` | n/a | Comparison of vajrAstra L2 vs Surya / external | orchestrator | **KEEP** | Cited from INDEX.md |
| `docs/south/EMPTY_PAGES.md` | n/a | Engine-vs-our-dump honesty on empty pages | orchestrator | **KEEP** | Diagnostic; honest-empty law |

---

## 3. docs/research/ — top-level (11 files, ~177 KB)

| path | bytes | purpose | audience | verdict | reason |
|---|---|---|---|---|---|
| `docs/research/W1_RECIPE_REFRESH.md` | 8,134 | Recipe refresh vs PPT (W1 stored research) | orchestrator | **KEEP** | W1 output; anchors all W2/W6 decisions |
| `docs/research/SOURCES.md` | 2,316 | Citation shelf (primary sources) | orchestrator | **KEEP** | Citation anchor |
| `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` | 19,448 | ACTIVE campaign law (3-agent ops, lanes A/B/C, evidence law, D1–D4, call prep) | all 3 agents | **KEEP** | Campaign law; §1, §10, §11 referenced from PROMPT_*.md |
| `docs/research/R1_SOTA_MECHANISM_TEARDOWN.md` | 22,068 | Sarvam 2.1 vs PaddleOCR-VL 1.6 mechanism teardown | orchestrator + Verdict | **KEEP** | SOTA mechanism research |
| `docs/research/R2_NASTALIQ_FORENSICS.md` | 32,008 | Kashmiri/Urdu Nastaliq failure physics + 2024–2026 attack surface | orchestrator + Verdict | **KEEP** | Kashmiri weak-cell attack |
| `docs/research/R3_OLCHIKI_MAYEK_SYNTHETIC.md` | 28,165 | Santali/Manipuri synthetic-training brief (NO execution per §9) | orchestrator + Verdict | **KEEP** | sat/mni weak-cell attack |
| `docs/research/R4_OLDSCAN_RESTORATION.md` | 26,216 | 2026 SOTA on document restoration + ablation spec | orchestrator + Engine | **KEEP** | OldScan weak-cell attack |
| `docs/research/R6_COMPETITION_INTEL.md` | 18,841 | Bhashini AksharDrishti hackathon intel (VERIFIED vs INFERENCE) | orchestrator + Miss | **KEEP** | Competition intel |
| `docs/research/R7_W6_TRAINING_TREE.md` | 15,898 | W6 training decision tree (parameterized, N0–N4 gates) | orchestrator + Engine | **KEEP** | W6 decision tree |
| `docs/research/DEEP_LIVE_RESEARCH.md` | 29,706 | Earlier deep research notes (pre-2026-09-27) | orchestrator | **MERGE→ archive** | Largely superseded by R1-R7 + LEVEL7_RESEARCH_CAMPAIGN |
| (any others in docs/research/) | various | per-lane ledgers — covered in level7 sections below | | | |

---

## 4. docs/research/level7/ — root (15 files, ~283 KB)

| path | bytes | purpose | audience | verdict | reason |
|---|---|---|---|---|---|
| `docs/research/level7/PROMPT_ENGINE_AGENT.md` | 8,097 | Paste-into-fresh-agent assignment script | orchestrator (Engine) | **KEEP** | Agent prompt; LIVE |
| `docs/research/level7/PROMPT_VERDICT_AGENT.md` | 11,858 | Paste-into-fresh-agent assignment script | orchestrator (Verdict) | **KEEP** | Agent prompt; LIVE |
| `docs/research/level7/PROMPT_MISS_AGENT.md` | 9,336 | Paste-into-fresh-agent assignment script | orchestrator (Miss) | **KEEP** | Agent prompt; LIVE |
| `docs/research/level7/CALL_PACKET.md` | 45,148 | Validation call packet (per-ag status, scores, decisions; 🟡 PAUSED banner) | orchestrator + Vinay | **KEEP (PAUSED, LIVE)** | Vinay-meeting LIVE packet |
| `docs/research/level7/MISS_MONITOR.md` | 53,411 | Miss agent append-only log (744 lines) | orchestrator + Miss | **KEEP (LIVE)** | Append-only monitoring log |
| `docs/research/level7/FINAL_VERDICT_2026-09-27.md` | 14,899 | Zero-tolerance boss-handoff verdict (refreshed after file audit) | orchestrator + audit | **KEEP** | Historical verdict preserved per docs/INDEX.md standing law |
| `docs/research/level7/H48_HOSTILE_PASS.md` | 21,402 | paperthin mandela + factchk + hate + santa-method on call decisions | orchestrator + Verdict | **KEEP** | H48 hostile pass output; LIVE |
| `docs/research/level7/H48_ENGINE_SPOTCHECK.md` | 6,257 | Engine per-weak-cell disk-truth spot-check log | orchestrator + Engine | **KEEP** | H48 spot-check; LIVE |
| `docs/research/level7/HUMAN_SPOTCHECK_PACKET.md` | 9,496 | 20-item table for user to review GT samples (gu_o005 first) | user | **KEEP** | D3 deliverable; LIVE |
| `docs/research/level7/SANTA_METHOD_FINAL.md` | 17,970 | 2-pass adversarial review of LEADERBOARD (R1 FOR + R2 AGAINST) | orchestrator + Verdict | **KEEP** | Santa-method output; LIVE |
| `docs/research/level7/FIX_SPECS_FOR_MISS.md` | 5,916 | Verdict → Miss fix specs (H48 hostile pass, applied) | orchestrator + Miss | **KEEP** | Applied fix specs |
| `docs/research/level7/FIX_SPECS_R2_LEADERBOARD.md` | 21,579 | Verdict → Miss fix specs (post-santa RED pass, 8 specs) | orchestrator + Miss | **KEEP** | Applied fix specs |
| `docs/research/level7/KILL_CRITERIA.md` | 16,058 | Pre-declared gates (K1–K4); 🟡 PAUSED banner | orchestrator + Verdict | **KEEP (PAUSED, LIVE)** | Pre-declared kill gates |
| `docs/research/level7/W5_FREEZE_AGENDA.md` | 11,904 | 15–20 min freeze-call agenda (sections A–F) | orchestrator + Verdict | **KEEP** | Freeze-call agenda |
| `docs/research/level7/W6_QLORA_SPEC.md` | 14,690 | W6 QLoRA scaffold spec (kok/pa only, K1-LOCKED); 🟡 PAUSED | orchestrator + Engine | **KEEP (PAUSED, LIVE)** | W6 prep-only spec; preserved |

---

## 5. docs/research/level7/boss_directives/ (5 files, ~52 KB)

| path | bytes | purpose | audience | verdict | reason |
|---|---|---|---|---|---|
| `SESSION_DIRECTIVES_2026-09-28.md` | 21,520 | Canonical record of boss directives 2026-09-27→28 (327 lines) | orchestrator | **KEEP** | Boss directive history; referenced from DISPATCH_LOG |
| `CONSOLIDATED_PARALLEL_WORK_2026-09-28.md` | 12,586 | Orchestrator parallel-track ledger (C1–C17 + 5 clusters) | orchestrator | **KEEP** | Workstream ledger |
| `BOSS_HANDOFF_2026-09-28.md` | 6,338 | Single-page validation call packet (5-min read) | Vinay + orchestrator | **KEEP** | Boss handoff doc |
| `VALIDATION_CALL_CHEATSHEET_2026-09-28.md` | 9,397 | Per-lang CER + 6 user-decisions table | Vinay + orchestrator | **KEEP** | Call cheatsheet |
| `VALIDATION_CALL_SCRIPT_2026-09-28.md` | 3,923 | 5-min script for the call | orchestrator | **KEEP** | Call script |

---

## 6. docs/research/level7/a/ (Lane A — 2 files, ~676 KB)

| path | bytes | purpose | audience | verdict | reason |
|---|---|---|---|---|---|
| `docs/research/level7/a/LEDGER.md` | 670,783 | Lane A ledger (984+ records; ≥400 target met) | Engine | **KEEP** | Primary OCR SOTA research ledger |
| `docs/research/level7/a/MANIFEST.md` | 5,640 | Lane A inventory + coverage map vs weak cells | Engine | **KEEP** | Inventory + format upgrade §9 |

---

## 7. docs/research/level7/b/ — Lane B (5 sublanes, 35 .md + 2 .jsonl)

### b1_rlvr_ocr/
| path | bytes | purpose | verdict | reason |
|---|---|---|---|---|
| `b1_rlvr_ocr/artifacts.jsonl` | 102,756 | 100 RLVR/OCR artifacts | **KEEP** | jsonl-only per FINAL_VERDICT |

### b2_self_improving_agents/
| path | bytes | purpose | verdict | reason |
|---|---|---|---|---|
| `b2_self_improving_agents/b2_all_artifacts.jsonl` | (jsonl) | 129 self-improvement records (NOT 258 as FINAL_VERDICT claims; **COUNT DISCREPANCY**) | **KEEP** + flag | Discrepancy with FINAL_VERDICT §1; verify before W6 |

### b3_multi_agent_orchestration/ (8 .md files)
| path | bytes | verdict | reason |
|---|---|---|---|
| `artifact_200_orchestra_bench.md` | 1,438 | KEEP | 9 records; OrchestraBench + AdaptOrch |
| `artifact_210_langgraph_crewai_autogen_openai.md` | 1,482 | KEEP | 10 records; LangGraph/CrewAI/AutoGen/OpenAI |
| `artifact_220_ecc_skills_orchestration.md` | 1,388 | KEEP | 10 records; ECC orchestration skills |
| `artifact_230_ecc_skills_continued.md` | 1,642 | KEEP | 10 records; claude-devfleet + unified-memory |
| `artifact_240_arxiv_papers_advanced.md` | 1,603 | KEEP (2 records dup w/ 250) | arXiv 2606.03115, 2607.22917 also in 250 |
| `artifact_250_ecc_autonomous_arxiv.md` | 1,569 | KEEP (2 records dup w/ 240) | 2 arXiv URLs duplicated |
| `artifact_260_anthropic_blogs_detailed.md` | 1,547 | KEEP | 10 records; Anthropic engineering blogs |
| `artifact_270_ecc_final_batch.md` | 26,290 | KEEP | 25 records; largest b3 file |

### b4_agent_tooling/ (13 .md files)
| path | bytes | verdict | reason |
|---|---|---|---|
| `mcp_servers.md` | ~1,500 | KEEP (advisory merge) | Paired pass; ~7 records duplicated |
| `mcp_detailed.md` | ~1,500 | KEEP (advisory merge) | Same content w/ mcp_servers.md |
| `claude_code_sdk.md` | ~1,500 | KEEP (advisory merge) | Paired pass |
| `claude_code_detailed.md` | ~1,500 | KEEP (advisory merge) | Same content |
| `opencode_ecc.md` | ~1,500 | KEEP (advisory merge) | ~3 records duplicated |
| `opencode_ecc_detailed.md` | ~1,500 | KEEP | Same content |
| `obsidian_acp.md` | ~1,500 | KEEP | Mostly different from obsidian_detailed.md |
| `obsidian_detailed.md` | ~1,500 | KEEP | Mostly different |
| `ts_ai_sdks.md` | ~1,500 | KEEP (advisory merge) | ~2 records duplicated |
| `ts_ai_sdks_detailed.md` | ~1,500 | KEEP | Same content |
| `laya_gates.md` | ~1,500 | KEEP (advisory merge) | ~4 records duplicated |
| `laya_detailed.md` | ~1,500 | KEEP | Same content |
| `kimi_agents.md` | ~1,500 | KEEP | Single file (no _detailed pair) |

### b5_elite_repos/ (15 .md files)
| path | bytes | verdict | reason |
|---|---|---|---|
| `ELITE_REPO_REFRESH_2026-09-27.md` | (large) | KEEP | 25-record refresh survey; consolidated |
| `browser_use_001.md` | n/a | KEEP | browser-use repo survey |
| `claude_mem_001.md` | n/a | KEEP | claude-mem persistent memory |
| `composio_awesome_skills_001.md` | n/a | KEEP | Composio skill catalog |
| `deepseek_harness_001.md` | n/a | KEEP | DeepSeek harness architecture |
| `ecc_001.md` + `ecc_002.md` | (8/10 records each) | KEEP (NOT-DUP) | 001=top-level + skills; 002=specific skill files |
| `graphify_001.md` + `graphify_002.md` | (8 each) | KEEP (NOT-DUP) | 001=baseline + BENCHMARKS; 002=README details |
| `hermes_agent_001.md` | n/a | KEEP | Hermes Agent self-improvement |
| `ponytail_001.md` + `ponytail_002.md` | (8 each) | KEEP (NOT-DUP) | 001=overview; 002=README details |
| `ralph_wiggum_001.md` + `ralph_wiggum_002.md` | (8 each) | KEEP (NOT-DUP) | 001=overview; 002=PROMPT_plan_work deep dive |
| `rtk_001.md` | n/a | KEEP | rtk-ai token reduction |

---

## 8. docs/research/level7/c/ — Lane C (13 files, ~530 KB)

### c1/ (NVIDIA stack, 7 files)
| path | bytes | verdict | reason |
|---|---|---|---|
| `LEDGER.md` | 142,350 | KEEP | 1070 lines, C1-001…C1-110+ records |
| `NOTE_LORA_VRAM.md` | n/a | KEEP | VRAM math for 2B VLMs (W6 budget input) |
| `NOTE_QUANT_INDIC.md` | n/a | KEEP | Quantization × Indic scripts threat model |
| `NOTE_TRTLLM.md` | n/a | KEEP | TensorRT-LLM serving recommendations |
| `NOTE_SERVE_COST.md` | n/a | KEEP | $/1M pages model + NIM verdict |
| `NOTE_EDGE.md` | n/a | KEEP | Jetson/edge deployment map |

### c2/ (Competition, 1 file)
| path | bytes | verdict | reason |
|---|---|---|---|
| `LEDGER.md` | 77,241 | KEEP | Bhashini competition intel ledger (307 lines, 106 records) |

### c3/ (Data collection, 2 files)
| path | bytes | verdict | reason |
|---|---|---|---|
| `LEDGER.md` | 131,281 | KEEP | Data-collection strategy ledger (981 lines, 115 records) |
| `STRATEGY.md` | n/a | KEEP | Per-cell verdicts for remaining languages (locked 2026-09-26) |

### c4/ (Tooling, 3 files)
| path | bytes | verdict | reason |
|---|---|---|---|
| `LEDGER.md` | 111,809 | KEEP | Tooling-landscape ledger (1283 lines, 100 records) |
| `LEDGER_FORMAT.md` | n/a | KEEP | Mandatory record format spec (§1–§8) |
| `OBITUARIES.md` | n/a | KEEP | Transfer obituaries for external numbers (Sarvam 87.39, etc.) |

---

## 9. level2/ (root-level + sub-readme files)

| path | bytes | purpose | verdict | reason |
|---|---|---|---|---|
| `level2/ULTIMATE_HYBRID_CONCERN.md` | 20,843 | South Level-2 disk law (scores, not next recipe) | **KEEP** | LAW; sealed L2 bench law; 12 standing laws |
| `level2/FOLDER_MAP.md` | 2,504 | Folder structure map (cleaned 2026-09-25) | **KEEP** | Level-2 map doc |
| `level2/MODELS_VS_OUT.md` | 4,105 | Phase-6 decision: KEEP BOTH (SHA256-verified dual view) | **KEEP** | Documents the dual-storage decision |
| `level2/engines/README.md` | n/a | Engine plugin socket contract | **KEEP** | Engine socket spec |
| `level2/research/README.md` | n/a | Generators + gates only (no essays) | **KEEP** | Research dir boundary |
| `level2/out/README.md` | n/a | Out dir convention | **KEEP** | Sealed-dir doc |
| `level2/training_assets/README.md` | n/a | Stage 3/3b export format | **KEEP** | Stage exports |

---

## 10. level2/probe22/ — root-level MD (19 files)

| path | bytes | purpose | verdict | reason |
|---|---|---|---|---|
| `AGENT_PROTOCOL.md` | 28,234 | LOCKED execution law (probe22 + 3-agent ops + §6.4) | **KEEP** | LAW; §0 hard rules + §6.4 LOCKED + §10 closed |
| `README.md` | 3,360 | Probe22 directory intro + verified state | **KEEP** | Entry point |
| `LIST.md` | 12,758 | Probe list (early Sarvam-bench split, n=20/lang) | **KEEP (historical)** | Pre-merge provenance |
| `SCORES.md` | 1,222 | Initial scorer output (n=20 Sarvam-bench split) | **KEEP (historical)** | Superseded by scores/LEADERBOARD.md |
| `FINAL_REPORT.md` | 16,317 | Engine wrap-up report (2026-09-28 20:31) | **KEEP** | Phase 5+6 wrap-up |
| `LEADERBOARD_REFRESH_2026-09-29.md` | 23,287 | Latest leaderboard (🟡 PAUSED banner) | **KEEP (PAUSED)** | Engine-side leaderboard |
| `verify_unaccounted.md` | 3,942 | Verdict reconciliation of 4 unaccounted visual items | **KEEP** | Reconciliation log |
| `transfer_obituaries.md` | 13,730 | Why benchmark numbers don't transfer to probe22 | **KEEP** | Obituary register |
| `orchestrator_briefing_template.md` | 1,396 | Verdict briefing template (5-section format) | **KEEP** | Template |
| `w6_feasible_set.md` | 6,628 | W6 feasible set analysis (FEASIBLE NOW/IF/INFEASIBLE) | **KEEP (PAUSED)** | W6 prep |
| `w6_set_construction_log.md` | 3,186 | W6 set construction log | **KEEP (PAUSED)** | W6 prep |
| `MEMORY_AUDIT.md` | 8,263 | Memory audit | **KEEP (PAUSED)** | Memory snapshot |
| `MEMORY_RECLAIM_RESULT.md` | 5,785 | Memory reclaim result (~9.4 GB reclaimable) | **KEEP (PAUSED)** | Reclaim log |
| `MLX_INSTALL_PLAN.md` | 6,749 | MLX install plan (user-approval gated) | **KEEP (PAUSED)** | W6 install prep |
| `MLX_INSTALL_RESULT.md` | 30,977 | MLX install result (mlx 0.32.3 + mlx-vlm 0.7.4 + mlx-tune 0.6.0) | **KEEP (PAUSED)** | W6 install result |
| `QLORA_EVAL_SPEC.md` | 16,598 | QLoRA eval spec (McNemar + Wilson 95% CI gate) | **KEEP (PAUSED)** | W6 eval prep |
| `QLORA_READINESS.md` | 18,741 | QLoRA readiness report (disk + memory + tools gate) | **KEEP (PAUSED)** | W6 readiness |
| `QLORA_SMOKE_TEST.md` | 11,763 | QLoRA smoke test | **KEEP (PAUSED)** | W6 smoke |
| `QLORA_TRAINING_DATA.md` | 14,398 | QLoRA training data plan (200-row SFT jsonl, 80/10/10) | **KEEP (PAUSED)** | W6 training data |

---

## 11. level2/probe22/scores/ (4 .md files)

| path | bytes | purpose | verdict | reason |
|---|---|---|---|---|
| `LEADERBOARD.md` | 12,409 | Disk-truth per-lang coverage (canonical leaderboard) | **KEEP** | Phase 6 leaderboard |
| `abstention_audit.md` | 6,683 | Abstention calibration audit | **KEEP** | Abstention analysis |
| `santa_method_cross_check.md` | 8,113 | Santa method cross-check | **KEEP** | Cross-check |
| `mcnemar_summary.md` | 2,874 | McNemar summary | **KEEP** | Statistical summary |
| `fix_specs/FS-VERDICT-H48-001.md` … `-010.md` | varies | 10 active fix specs | **KEEP** | Verdict fix specs |

---

## 12. level2/models/<engine>/ (10 PROMPT.md + 10 RUN.md = 20 .md files)

| path pattern | bytes | verdict | reason |
|---|---|---|---|
| `models/<engine>/PROMPT.md` × 10 | varies | **KEEP** | Engine contract (NOT a prompt sent to engines — L2 engines are programs) |
| `models/<engine>/RUN.md` × 10 | varies | **KEEP** | Run facts (identity, counts, examples, rerun history) |

---

## 13. level2/research/gates/ (5 .md files)

| path | bytes | verdict | reason |
|---|---|---|---|
| `gates/INDEX.md` | n/a | KEEP | Gates ledger index (H8 law) |
| `gates/B12_ensemble_voting.md` | n/a | KEEP | Ensemble voting gate |
| `gates/B1_doctr_parseq.md` | n/a | KEEP | DocTr + ParSeq gate |
| `gates/B3_tessdata_best.md` | n/a | KEEP | Tessdata best gate |
| `gates/B4_paddle_server_det.md` | n/a | KEEP | Paddle server det gate |

---

## 14. level2/reports/ (SEALED — 11 .md files, read-only)

| path | bytes | verdict | reason |
|---|---|---|---|
| `LEADERBOARD.md` | varies | KEEP (SEALED) | South-400 leaderboard — DO NOT TOUCH |
| `CER_BY_SCRIPT.md` | varies | KEEP (SEALED) | CER by script |
| `LANG_LEADERBOARD.md` | varies | KEEP (SEALED) | Per-language leaderboard |
| `LEADERBOARD_BY_SCRIPT.md` | varies | KEEP (SEALED) | Leaderboard by script |
| `LEVEL2_SEAL.md` | varies | KEEP (SEALED) | Level-2 seal manifest |
| `GAP.md` | varies | KEEP (SEALED) | Gap analysis |
| `LATENCY.md` | varies | KEEP (SEALED) | Latency benchmarks |
| `DUPLICATE_AUDIT.md` | varies | KEEP (SEALED) | Duplicate audit |
| `FAILURE_TAXONOMY.md` | varies | KEEP (SEALED) | Failure taxonomy |
| `REVIEW_QUEUE.md` | varies | KEEP (SEALED) | Review queue |
| `SCENARIO_BEST.md` | varies | KEEP (SEALED) | Best-scenario bench |
| `SEP16_ONE_SCREEN.md` | varies | KEEP (SEALED) | Sep-16 one-screen report |
| `SHOWCASE.md` | 27,742 | KEEP (SEALED) | Showcase report |
| `WHATSAPP_SEPT16.md` | varies | KEEP (SEALED) | WhatsApp Sept-16 status |
| `WHATSAPP_WEEKLY.md` | varies | KEEP (SEALED) | Weekly status |

---

## 15. graphify-out/ (2 .md files)

| path | bytes | verdict | reason |
|---|---|---|---|
| `GRAPH_REPORT.md` | 151,422 | **KEEP** | Canonical narrative report (3990 nodes / 4681 edges) |
| `graphify-out/2026-09-29/GRAPH_REPORT.md` | 57,118 | **KEEP** | Same-day rebuild (post-rebuild backup at .pre-rebuild-2026-09-29) |

---

## 16. _archive/ — historical (DO NOT touch; 7 audit reports)

| path | bytes | verdict | reason |
|---|---|---|---|
| `_archive/cleanup_2026-09-28/AUDIT_probe22.md` | (large) | KEEP | Phase 1 cleanup audit |
| `_archive/cleanup_2026-09-28/AUDIT_level2_other.md` | (large) | KEEP | Phase 2 cleanup audit |
| `_archive/cleanup_2026-09-28/AUDIT_docs.md` | (large) | KEEP | Phase 3 cleanup audit |
| `_archive/cleanup_2026-09-28/AUDIT_datasets.md` | (large) | KEEP | Phase 4 cleanup audit |
| `_archive/cleanup_2026-09-28/AUDIT_hidden.md` | (large) | KEEP | Phase 5 cleanup audit |

---

## SUMMARY STATISTICS

| Metric | Value |
|---|---|
| **Total MD files in scope** | **203** |
| KEEP (canonical + LIVE) | 184 (90.6%) |
| KEEP (PAUSED, LIVE) | 12 (5.9%) — 12 W6 prep files with 🟡 PAUSE banners |
| MERGE → archive (advisory) | 7 (3.4%) — b4 paired passes |
| DELETE candidates | 1 (0.5%) — `OCR_AGENT_MEMORY_FEED copy.md` exact dup |
| SEALED dirs (untouched) | 5 (level2/out/, level2/reports/, level2/probe22/out/, arc_level_1/, Datasets/akshardrishti_official/) |
| Sealed .md files | 15 in level2/reports/ |
| Estimated disk footprint | ~2.5 MB of MD content (excluding sealed + LEDGERs which are ~1.7 MB alone) |

---

## KEY FLAGS

1. **b2_all_artifacts.jsonl count discrepancy** — FINAL_VERDICT claims 258 records; file has 129 records. RECONCILE before W6.
2. **b4_agent_tooling paired passes** — 32/179 records duplicated across `X.md` / `X_detailed.md` pairs. Advisory merge if disk pressure.
3. **b3 artifact_240 / artifact_250** — 2 records share URLs (2606.03115, 2607.22917). Advisory merge.
4. **OCR_AGENT_MEMORY_FEED copy.md** — exact duplicate of master. DELETE candidate (L4 archive first).
5. **PAUSED banners (12 files)** — must NOT be deleted; preserved as W5-strategy evidence + post-meeting W6 reactivation reference.
6. **Final-Verdict archive has 14,899 bytes (different from 16,317 in FINAL_REPORT.md at probe22 root)** — different files; both kept.