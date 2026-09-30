# DEDUP_DOCS_RESEARCH.md — docs/research/ audit (DEDUP-AGENT-4)

**Date:** 2026-09-29
**Scope:** `docs/research/` and `docs/research/level7/`
**Total files scanned:** 86 MD files
**SHA256 method:** `shasum -a 256` on every file; `sort | uniq -c` for collision detection

---

## Byte-identical pairs: 0

All 86 MD files have **unique SHA256 hashes**. No byte-identical pairs exist anywhere in scope. The b4/b5 .md files were regenerated from .jsonl after prior byte-identical dupes were deleted (per `FINAL_VERDICT_2026-09-27.md` Class A/B cleanup). No further mechanical dedup is possible at the byte level.

---

## Topic variants: 12 groups

### Group 1 — LIVE_RESEARCH evolution (3 files, all Vinay-meeting prep)
| File | Lines | Purpose | Status |
|---|---|---|---|
| `docs/research/DEEP_LIVE_RESEARCH.md` | 468 | First pass: 7 user URLs + field SOTA + 2.1 vs 2.0 + Gnani + Laya/Jev + Consensus | superseded |
| `docs/research/LIVE_LATEST_2026-09-29.md` | 295 | Second pass (AGENT-1): "what changed since campaign ledger sealed" | superseded |
| `docs/research/DEEPER_LIVE_RESEARCH_2026-09-29.md` | 499 | Third pass (AGENT-8): second-pass expansion + corrigendum on LIVE_LATEST sat/mni claim | **current** |

**Verdict:** Three sequential passes on the same Vinay-meeting prep mission. Each is longer than the last and corrects the prior. The latest is canonical. Two earlier ones are historical snapshots.

---

### Group 2 — Boss-directive files (5 files, all 2026-09-28)
| File | Lines | Purpose | Status |
|---|---|---|---|
| `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` | ~?| Comprehensive session record of boss directives | historical |
| `docs/research/level7/boss_directives/CONSOLIDATED_PARALLEL_WORK_2026-09-28.md` | ~?| Merged parallel-work concerns ledger | historical |
| `docs/research/level7/boss_directives/VALIDATION_CALL_SCRIPT_2026-09-28.md` | ~?| 5-min validation-call script | call-window |
| `docs/research/level7/boss_directives/VALIDATION_CALL_CHEATSHEET_2026-09-28.md` | ~?| Cheat sheet for boss at validation call | call-window |
| `docs/research/level7/boss_directives/BOSS_HANDOFF_2026-09-28.md` | ~?| Single-page handoff packet (post-H44 review) | call-window |

**Verdict:** All five have distinct roles (record vs consolidated vs script vs cheatsheet vs handoff). All dated 2026-09-28 (pre-call). The two call-window pairs (SCRIPT/CHEATSHEET, BOSS_HANDOFF) overlap on purpose; both are valid for the call window. Keep all five; they're time-stamped snapshots of an evolving pre-call prep.

---

### Group 3 — W5 strategy docs (3 files)
| File | Lines | Purpose |
|---|---|---|
| `docs/research/level7/W5_STRATEGY_OPTIONS.md` | ~? | Verdict's top-3 ranked W5 strategies |
| `docs/research/level7/W5_BEAT_SARVAM_PLAN.md` | ~? | Engine+Verdict joint concrete recipe to beat Sarvam |
| `docs/research/level7/W5_FREEZE_AGENDA.md` | ~? | Verdict's 15-20 min freeze agenda (6 sections A–F) |

**Verdict:** Three different cuts of the same W5 plan: OPTIONS (ranked), BEAT_SARVAM (concrete recipe), FREEZE_AGENDA (call procedure). All load-bearing for the call. Keep all three — they serve different rhetorical roles in the validation call.

---

### Group 4 — Fix-specs pair (2 files)
| File | Purpose |
|---|---|
| `docs/research/level7/FIX_SPECS_FOR_MISS.md` | Verdict→Miss specs for shared artifacts (CALL_PACKET, FINAL_REPORT, MISS_MONITOR) |
| `docs/research/level7/FIX_SPECS_R2_LEADERBOARD.md` | Verdict→Miss specs targeting `LEADERBOARD_REFRESH_2026-09-29.md` post-santa-method RED pass |

**Verdict:** Different scopes (R2 is one targeted pass; FOR_MISS is the general Verdict→Miss spec sheet). Both active and valid. Keep both.

---

### Group 5 — H48 verification docs (2 files)
| File | Purpose |
|---|---|
| `docs/research/level7/H48_HOSTILE_PASS.md` | Verdict's 4-paperthin-skill hostile pass (mandela/factchk/hate/santa-method) |
| `docs/research/level7/H48_ENGINE_SPOTCHECK.md` | Engine's spot-check log for Verdict's H48 weak-cell claims |

**Verdict:** Hostile pass (adversarial) + spot-check (verification of claims). Complementary, distinct roles. Keep both.

---

### Group 6 — Elite-repo pairs (4 pairs of `_001` vs `_002`)
| `_001` file | `_002` file | Same topic? |
|---|---|---|
| `b/b5_elite_repos/ecc_001.md` | `b/b5_elite_repos/ecc_002.md` | YES — both ECC repo profiles |
| `b/b5_elite_repos/graphify_001.md` | `b/b5_elite_repos/graphify_002.md` | YES — both graphify repo profiles |
| `b/b5_elite_repos/ponytail_001.md` | `b/b5_elite_repos/ponytail_002.md` | YES — both ponytail profiles |
| `b/b5_elite_repos/ralph_wiggum_001.md` | `b/b5_elite_repos/ralph_wiggum_002.md` | YES — both Ralph profiles |

**Verdict:** Each pair covers the **same** repo but **different** extracts (different source URLs, different sub-features). `_001` is the repo-overview pass; `_002` is the deeper sub-feature pass (e.g., `ecc_002` covers specific ECC skills; `graphify_002` covers `--code-only` flag; `ponytail_002` covers `/ponytail-review` commands; `ralph_wiggum_002` covers `plan-work` mode). They are intentionally two-passes over different surfaces — not duplicates. Keep all 8.

---

### Group 7 — Agent-tooling pairs (6 pairs of "overview" vs "_detailed")
| "overview" file | "_detailed" file | Same topic? |
|---|---|---|
| `b/b4_agent_tooling/claude_code_sdk.md` | `b/b4_agent_tooling/claude_code_detailed.md` | YES — both Claude Code SDK |
| `b/b4_agent_tooling/mcp_servers.md` | `b/b4_agent_tooling/mcp_detailed.md` | YES — both MCP servers |
| `b/b4_agent_tooling/opencode_ecc.md` | `b/b4_agent_tooling/opencode_ecc_detailed.md` | YES — both OpenCode+ECC |
| `b/b4_agent_tooling/laya_gates.md` | `b/b4_agent_tooling/laya_detailed.md` | YES — both Laya gates |
| `b/b4_agent_tooling/ts_ai_sdks.md` | `b/b4_agent_tooling/ts_ai_sdks_detailed.md` | YES — both TS AI SDKs (Vercel AI SDK) |
| `b/b4_agent_tooling/obsidian_acp.md` | `b/b4_agent_tooling/obsidian_detailed.md` | YES — both Obsidian ACP |

**Verdict:** Each pair has the **same first source URL** (verified via header diff). The "overview" file is a short, top-level summary; the "_detailed" file is the longer deeper pass on the same surface (different second/third source URLs go deeper into sub-features). Per `FINAL_VERDICT_2026-09-27.md` Class C regeneration, the .md files were regenerated from separate .jsonl passes, so the duplication is **structural**, not redundant. Keep all 12 — but flag for a future "merge _overview into _detailed" if the campaign extends past W5.

---

### Group 8 — R1–R7 individual research deliverables (6 files, distinct topics)
| File | Lines | Topic | Scope |
|---|---|---|---|
| `R1_SOTA_MECHANISM_TEARDOWN.md` | 168 | Sarvam Vision 2.1 vs PaddleOCR-VL 1.6 mechanism teardown | one paper, narrow |
| `R2_NASTALIQ_FORENSICS.md` | 324 | Why Kashmiri cell fails + attack surface for Nastaliq under ≤2B VLM | one script family |
| `R3_OLCHIKI_MAYEK_SYNTHETIC.md` | 200 | Ol Chiki + Meitei Mayek synthetic-training brief | two scripts |
| `R4_OLDSCAN_RESTORATION.md` | 268 | Old-scan restoration SOTA + cost + ablation spec | one problem class |
| `R6_COMPETITION_INTEL.md` | 158 | Bhashini AksharDrishti hackathon official intel | one competition |
| `R7_W6_TRAINING_TREE.md` | 123 | Parameterized W6 training decision tree (gates only) | one decision tree |

**Verdict:** Each R-file has a **distinct narrow topic** and a **distinct research methodology** (primary sources only, URLs verified). None overlap with `level7/` campaign docs (those are lane ledgers + agent prompts + protocol). R5 (GT forensics) is referenced in level7/PROMPT_*.md but its file lives in `level2/reports/` (sealed per AGENTS.md). Keep all 6.

---

### Group 9 — Lane ledgers in level7/c/ (4 lanes, distinct purposes)
| File | Lines | Lane |
|---|---|---|
| `c/c1/LEDGER.md` | 142,350 | NVIDIA stack for OCR/document VLMs (TensorRT-LLM, NIM, NeMo, quant, Jetson, serving cost, LoRA VRAM) |
| `c/c2/LEDGER.md` | 77,241 | Competition Intel (Bhashini etc.) |
| `c/c3/LEDGER.md` | 131,281 | Data-Collection Strategy (quality-first, remaining langs) |
| `c/c4/LEDGER.md` | 111,809 | Tooling Landscape (100 records) |

Plus `c/c3/STRATEGY.md`, `c/c4/LEDGER_FORMAT.md`, `c/c4/OBITUARIES.md`, `c/c1/NOTE_*.md` (5 small notes).

**Verdict:** Four lanes, four distinct scopes. The `c/c1/NOTE_*.md` files (EDGE, TRTLLM, QUANT_INDIC, SERVE_COST, LORA_VRAM) are individual notes — each ~1.5-2 KB — supporting the c1 NVIDIA-stack ledger. No duplicates. Keep all.

---

### Group 10 — level7/a/ (2 files, the main Lane A ledger)
| File | Size | Purpose |
|---|---|---|
| `a/LEDGER.md` | 670,783 bytes (~984 records) | Main Lane A record ledger (OCR/DocAI SOTA 2025–2026) |
| `a/MANIFEST.md` | 5,640 bytes | Inventory + status of Lane A artifacts |

**Verdict:** LEDGER = the records; MANIFEST = the inventory pointer. Both needed. Keep both.

---

### Group 11 — level7/b/b3/ multi-agent-orchestration artifacts (8 files, distinct)
| File | Topic |
|---|---|
| `artifact_200_orchestra_bench.md` | OrchestraBench |
| `artifact_210_langgraph_crewai_autogen_openai.md` | LangGraph + CrewAI + AutoGen + OpenAI |
| `artifact_220_ecc_skills_orchestration.md` | ECC skills for orchestration |
| `artifact_230_ecc_skills_continued.md` | ECC skills (continued batch) |
| `artifact_240_arxiv_papers_advanced.md` | Advanced arXiv papers |
| `artifact_250_ecc_autonomous_arxiv.md` | ECC autonomous harness + arXiv |
| `artifact_260_anthropic_blogs_detailed.md` | Anthropic engineering blogs (detailed) |
| `artifact_270_ecc_final_batch.md` | ECC final batch |

**Verdict:** Each `artifact_NNN_*.md` is one converted .jsonl pass on a distinct slice of multi-agent-orchestration research. Different `source_url` per file (verified via header). Keep all 8.

---

### Group 12 — Top-level level7/ protocol/law files (6 files, distinct roles)
| File | Purpose |
|---|---|
| `LEVEL7_RESEARCH_CAMPAIGN.md` (note: lives in `docs/research/` not `docs/research/level7/`) | Campaign LAW: 3-agent model, lanes, evidence rules, D1–D4 |
| `level7/PROMPT_ENGINE_AGENT.md` | Assignment script: paste into Engine subagent |
| `level7/PROMPT_VERDICT_AGENT.md` | Assignment script: paste into Verdict subagent |
| `level7/PROMPT_MISS_AGENT.md` | Assignment script: paste into Miss subagent |
| `level7/CALL_PACKET.md` | Validation-call primary brief |
| `level7/HUMAN_SPOTCHECK_PACKET.md` | Human spot-check packet for call |
| `level7/MISS_MONITOR.md` | Miss Agent's monitoring log |
| `level7/KILL_CRITERIA.md` | W6 kill criteria |
| `level7/W6_QLORA_SPEC.md` | W6 QLoRA spec |
| `level7/SANTA_METHOD_FINAL.md` | Final adversarial review of LEADERBOARD |
| `level7/FINAL_VERDICT_2026-09-27.md` | End-of-campaign verdict doc |
| `level7/ELITE_REPO_REFRESH_2026-09-27.md` (note: actually at `b/b5_elite_repos/ELITE_REPO_REFRESH_2026-09-27.md`) | B5 elite-repo refresh note |

**Verdict:** Each has a distinct function (law / assignment / brief / monitor / criteria / spec / review / verdict / refresh). All load-bearing. Keep all.

---

## Topic-variant pair checks (per STEP 3)

| Comparison | Different scopes? | Verdict |
|---|---|---|
| `R1-R7` files vs `level7/` campaign docs | **YES — distinct.** R1-R7 are individual research deliverables with narrow topics (one model teardown, one script, one ablation). `level7/` is the campaign law + lane ledgers + agent prompts + per-lane research outputs. | No overlap. Keep both. |
| `W1_RECIPE_REFRESH.md` vs `R7_W6_TRAINING_TREE.md` | **YES — distinct.** W1 = closed 2026-09-25 research pass on training recipes in the field (recipe refresh, no scoring). R7 = parameterized W6 decision tree for **our** training (gates + base selection + data + curriculum + RLVR + weak cells + inference). | No overlap. Keep both. |
| `LEVEL7_RESEARCH_CAMPAIGN.md` vs `level7/PROMPT_*.md` | **YES — distinct.** CAMPAIGN.md is LAW (3-agent model, lanes, evidence rules, D1–D4). PROMPT_*.md are ASSIGNMENT SCRIPTS (paste into fresh subagent sessions to dispatch the 3 worker agents). | No overlap. Keep both. |
| `docs/research/SOURCES.md` | **Citation shelf only** (18 lines, 1 table of 10 sources). Living recipe lives in `W1_RECIPE_REFRESH.md`; hybrid architecture lives in `docs/architecture/W2_HYBRID.md`. | No overlap. KEEP (it's the citation shelf pointer). |
| `LIVE_LATEST_2026-09-29.md` vs `MEETING_2026-09-29_STRUCTURED.md` | **YES — distinct.** LIVE_LATEST = live research findings from user URLs + field SOTA + corrigenda (research content). MEETING = structured boss-meeting notes (D1–D7 decisions, A1–A5 action items, transcript). | No overlap. Keep both. |
| `uni_v3_ORIGINAL_2026-09-29.md` | **Directive.** Different from research — it's the boss's master directive (19 parts, R0.1-R0.4, T1-T9), archived per AGENTS.md to `_archive/directives/`. | No overlap. KEEP (sealed per archive law). |
| `level7/` subdirs `a/`, `c1-c4/`, `boss_directives/` | **Each subdir has a distinct lane/role.** a = Lane A; c1 = NVIDIA stack; c2 = Competition Intel; c3 = Data Collection; c4 = Tooling Landscape; boss_directives = pre-call prep packets. | No overlap. Keep all. |

---

## Recommended actions: 0 deletes, 3 MERGE candidates, 0 KEEP-only changes

No file needs deletion. All 86 files are load-bearing per their author/role. Three historical-snapshot pairs can be **MERGED** to free disk + simplify, but doing so loses audit trail. Recommendation: **KEEP all** unless user explicitly authorizes historical-snapshot deletion.

| # | File(s) | Action | Rationale |
|---|---|---|---|
| 1 | `DEEP_LIVE_RESEARCH.md`, `LIVE_LATEST_2026-09-29.md`, `DEEPER_LIVE_RESEARCH_2026-09-29.md` | **MERGE candidate** (3→1) | Three sequential passes on the same Vinay-meeting prep. DEEPER is canonical (latest, longest, corrigenda-loaded). The other two are historical snapshots. **Risk:** loses provenance of how research evolved. **Safe path:** archive the two older to `_archive/research/live_research_pass{N}/` and keep DEEPER as `LIVE_RESEARCH_FINAL_2026-09-29.md`. **Authorization needed** before any merge — campaign §9 says "evidence carries decision-changers, no retroactive edits." |
| 2 | `boss_directives/` 5 files (all 2026-09-28) | **KEEP all** | Distinct roles (session record / consolidated / script / cheatsheet / handoff). Date-stamped snapshots of an evolving pre-call prep. No merge makes sense — they each answered a different question. |
| 3 | 4 elite-repo `_001/_002` pairs | **KEEP both** | Different surfaces of same repo (overview vs sub-feature pass). Intentional two-pass per FINAL_VERDICT Class C. |
| 4 | 6 agent-tooling `_detailed` pairs | **KEEP both** | Same: overview vs deeper pass. Future merge candidate if campaign extends past W5. |
| 5 | `R1-R7` 6 files | **KEEP all** | Distinct narrow topics; one file per topic; primary-source citations. |
| 6 | `W1_RECIPE_REFRESH.md` | **KEEP** | Closed 2026-09-25; W1 status CLOSED. Hybrid architecture lives elsewhere. |
| 7 | `R7_W6_TRAINING_TREE.md` | **KEEP** | Plan only; gates binding; superseded by R7 in subsequent revisions if any. |
| 8 | `LEVEL7_RESEARCH_CAMPAIGN.md` | **KEEP** | LAW — anchors all 3 agents. |
| 9 | `PROMPT_ENGINE/VERDICT/MISS_AGENT.md` | **KEEP** | Assignment scripts — verbatim paste per agent dispatch. |
| 10 | `SOURCES.md` | **KEEP** | Citation shelf (18 lines, 10 sources). Already a slim pointer file. |
| 11 | `LIVE_LATEST_2026-09-29.md` | **KEEP** (or part of MERGE candidate 1) | Distinct from DEEPER; both are AGENT-1 vs AGENT-8 passes. |
| 12 | `MEETING_2026-09-29_STRUCTURED.md` | **KEEP** | Structured meeting notes (D1-D7, A1-A5) — irreplaceable. |
| 13 | `uni_v3_ORIGINAL_2026-09-29.md` | **KEEP** (sealed per archive law) | Master directive, archived per AGENTS.md. |
| 14 | `level7/a/LEDGER.md` + `a/MANIFEST.md` | **KEEP both** | Records vs inventory. |
| 15 | `level7/c/{c1-c4}/LEDGER.md` | **KEEP all** | Distinct lanes (NVIDIA / competition / data / tooling). |
| 16 | `level7/b/b3/`, `b4/`, `b5/` artifacts | **KEEP all** | Each is a converted .jsonl on a distinct sub-topic slice. |
| 17 | `level7/boss_directives/*.md` (5) | **KEEP all** | Pre-call prep snapshots, distinct roles. |
| 18 | `level7/H48_*.md`, `level7/W5_*.md`, `level7/W6_QLORA_SPEC.md`, `level7/KILL_CRITERIA.md`, `level7/SANTA_METHOD_FINAL.md`, `level7/FINAL_VERDICT_2026-09-27.md`, `level7/FIX_SPECS_*.md`, `level7/CALL_PACKET.md`, `level7/HUMAN_SPOTCHECK_PACKET.md`, `level7/MISS_MONITOR.md`, `level7/ELITE_REPO_REFRESH_2026-09-27.md` | **KEEP all** | Each has a unique role in the validation-call window or post-campaign cleanup. |
| 19 | `level7/c/c1/NOTE_*.md` (5 small notes) | **KEEP all** | Support the c1 NVIDIA-stack ledger; one note each (EDGE, TRTLLM, QUANT_INDIC, SERVE_COST, LORA_VRAM). |
| 20 | `level7/c/c3/STRATEGY.md`, `level7/c/c4/LEDGER_FORMAT.md`, `level7/c/c4/OBITUARIES.md` | **KEEP all** | Companion docs to their respective LEDGERs. |

---

## Token spend (DEDUP-AGENT-4)

- 1 glob call
- 6 bash calls (hash check, size sort, head checks, diffs)
- 9 read calls (key files for content comparison)
- 1 write call (this report)

Estimated tokens: ~22K input + ~3K output. No MCP calls. No git changes. No edits to any research file. Read-only audit.

---

## Summary

- **Byte-identical pairs: 0** (already cleaned in prior Class A/B passes)
- **Topic variants: 12 groups**, all with distinct roles after header diff
- **Recommended actions: 0 deletes, 1 MERGE candidate (3 live-research passes → 1, with archive of 2), 19 KEEP**

The repo is dedup-clean at the byte level. The remaining "duplicates" are intentional two-pass extractions (overview + _detailed / _001 + _002), which is by design per `FINAL_VERDICT_2026-09-27.md` Class C. The only real consolidation candidate is the live-research triplet, and that requires user authorization before merge.

*End of report.*