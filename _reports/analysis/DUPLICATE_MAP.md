# DUPLICATE MAP — South repo MD files (AGENT-2)
**Date:** 2026-09-29 19:00 IST
**Method:** Identify file pairs/groups that are byte-identical, near-identical, or share major content overlap

---

## Duplicate set 1: OCR_AGENT_MEMORY_FEED (root + copy)

- **file_a:** `/Users/srujansai/Desktop/South/OCR_AGENT_MEMORY_FEED.md` (167,059 bytes)
  - Master process-law doc (§1–§16, all append-only log entries)
- **file_b:** `/Users/srujansai/Desktop/South/OCR_AGENT_MEMORY_FEED copy.md` (11,173 bytes)
  - Partial copy (only §1–§10; missing §11–§16 append-only log)
- **diff:** `copy.md` is a ~2-month-old snapshot before the §11-§16 log was added. ~93% of master is NOT in copy. NOT a current duplicate but is the source of bloat.
- **recommendation:** **DELETE `OCR_AGENT_MEMORY_FEED copy.md`** (L4 archive → _archive/cleanup_2026-09-28/ first with SHA256). Master is the canonical LAW file; copy is stale.

---

## Duplicate set 2: W5 Strategy (root vs docs/architecture/)

- **file_a:** `/Users/srujansai/Desktop/South/W5_STRATEGY_OPTIONS.md` (3,754 bytes)
  - "Top 3 Ranked" pre-Vinay-meeting prep (87 lines, condensed)
- **file_b:** `/Users/srujansai/Desktop/South/docs/architecture/W5_STRATEGY_OPTIONS.md` (19,443 bytes)
  - "5 alternatives with cost/time/CER-delta/risks/decision-it-changes" (181 lines, evidence-backed)
- **diff:** Root = "Top 3 Ranked" (just A/B/C + ranking rationale); docs/ = 5 full alternatives + D alternative + scoring per option. Root is **subset** of docs/. Both versions explicitly cross-referenced from OCR_AGENT_MEMORY_FEED §15-§16 + BOSS_CONCERNS §53+. **Genuinely different audiences**: root = "what Vinay needs to see at the prompt"; docs/ = "evidence-backed version for the record".
- **recommendation:** **KEEP BOTH.** Different audiences, both live references, no live duplication.

---

## Duplicate set 3: W5 Beat-Sarvam Plan (root vs docs/architecture/)

- **file_a:** `/Users/srujansai/Desktop/South/W5_BEAT_SARVAM_PLAN.md` (3,652 bytes)
  - "Concrete Recipe" (107 lines; 2-stage: wrap-only + QLoRA on kok+pa)
- **file_b:** `/Users/srujansai/Desktop/South/docs/architecture/W5_BEAT_SARVAM_PLAN.md` (14,324 bytes)
  - "Concrete Plan to Beat 87.39" (235 lines; TL;DR + 3 scenarios + where-we-win/tie/lose cells)
- **diff:** Root = condensed plan (Stages 1/2/3 with brief mechanism); docs/ = 235-line detailed plan with full citations, 4 scenarios vs Sarvam, budget ask per item. **Genuinely different audiences**: root = prompt-facing; docs/ = full evidence record.
- **recommendation:** **KEEP BOTH.** Same rationale as duplicate set 2.

---

## Duplicate set 4: VINAY_MEETING_PACKET (root vs docs/architecture/)

- **file_a:** `/Users/srujansai/Desktop/South/VINAY_MEETING_PACKET.md` (24,427 bytes)
  - Question-driven + W6 PAUSE banner; 3 strategic questions; companion-doc cross-refs to STRATEGY_VINAY_TOMORROW + VINAY_CTA (now merged into this file per Phase 2 cleanup); Verdict's question-driven edition body preserved
- **file_b:** `/Users/srujansai/Desktop/South/docs/architecture/VINAY_MEETING_PACKET.md` (5,899 bytes)
  - Results-driven; 5 probe22 findings; 5 strategy options (A/B/C/D/E); budget ask ~₹1005 + W6 fine-tune scope; Verdict's W6-specific guidance
- **diff:** Root = question-driven 1-page brief; docs/ = results-driven detailed packet with W6 path options (V1-V5). **Both are Vinay-facing but at different decision depths**.
- **recommendation:** **KEEP BOTH.** Different audiences (root = pre-meeting prep for user; docs/ = strategy options table for Vinay's decision-making).

---

## Duplicate set 5: STRATEGY_VINAY_TOMORROW.md + VINAY_CTA.md (already merged)

- **file_a:** Originally `/Users/srujansai/Desktop/South/STRATEGY_VINAY_TOMORROW.md` (~6.3 KB; strategy narrative)
- **file_b:** Originally `/Users/srujansai/Desktop/South/VINAY_CTA.md` (~4.8 KB; CTA + 3 strategic questions)
- **status:** **ALREADY MERGED** into `VINAY_MEETING_PACKET.md` (24,427 bytes) per Phase 2 of 24h cleanup (2026-09-29). Source files archived to `_archive/cleanup_2026-09-28/` with SHA256, then deleted. **No action.**

---

## Duplicate set 6: INTEGRATED-ELITE-STACK.md vs b5 ELITE_REPO_REFRESH

- **file_a:** `/Users/srujansai/Desktop/South/INTEGRATED-ELITE-STACK.md` (13,275 bytes)
  - "How the 25+ elite repos are wired into this project" (install/keep/watch + 3-agent ops model integration)
- **file_b:** `/Users/srujansai/Desktop/South/docs/research/level7/b/b5_elite_repos/ELITE_REPO_REFRESH_2026-09-27.md` (245 lines, ~10 KB)
  - Refresh survey of 25+ elite repos (raw source data)
- **diff:** **Genuinely different**: INTEGRATED-ELITE-STACK = canonical wiring (action layer; "where do we use paperthin/mlx-tune/liteparse"); b5 ELITE_REPO_REFRESH = source survey (raw research). Referenced from AGENTS.md + 3 PROMPT_*.md.
- **recommendation:** **KEEP BOTH.** Root is canonical wiring; b5 is source survey.

---

## Duplicate set 7: b4_agent_tooling — paired X.md / X_detailed.md (7 pairs)

| pair | both files ~1.5 KB each | ~7 records duplicated |
|---|---|---|
| `mcp_servers.md` ↔ `mcp_detailed.md` | both | 7 records duplicated |
| `claude_code_sdk.md` ↔ `claude_code_detailed.md` | both | 7 records duplicated |
| `opencode_ecc.md` ↔ `opencode_ecc_detailed.md` | both | ~3 records duplicated |
| `obsidian_acp.md` ↔ `obsidian_detailed.md` | both | mostly different sources |
| `ts_ai_sdks.md` ↔ `ts_ai_sdks_detailed.md` | both | ~2 records duplicated |
| `laya_gates.md` ↔ `laya_detailed.md` | both | ~4 records duplicated |
| `kimi_agents.md` (single, no pair) | single | n/a |

- **diff:** 32/179 records in b4_agent_tooling are exact duplicates across the paired `X.md` / `X_detailed.md` files. Different framings (X = condensed/overview; X_detailed = full record), but the record content overlaps.
- **recommendation:** **ADVISORY MERGE only** (per docs/AUDIT_docs.md §hard recommendations #2). If disk pressure becomes an issue, consider merging `X.md` into `X_detailed.md` (deeper pass) and dropping the lighter pass; removes ~84 records + ~13 files. **NOT urgent**; disk footprint is small.

---

## Duplicate set 8: b3 artifact_240 / artifact_250 (2 shared URLs)

- **file_a:** `/Users/srujansai/Desktop/South/docs/research/level7/b/b3_multi_agent_orchestration/artifact_240_arxiv_papers_advanced.md`
- **file_b:** `/Users/srujansai/Desktop/South/docs/research/level7/b/b3_multi_agent_orchestration/artifact_250_ecc_autonomous_arxiv.md`
- **diff:** 2 arXiv URLs shared (2606.03115, 2607.22917). Mostly different content (240 = arxiv papers; 250 = ECC autonomous arxiv).
- **recommendation:** **ADVISORY MERGE only** (per docs/AUDIT_docs.md). Low overlap; OK to keep both.

---

## Duplicate set 9: b5_elite_repos X_001 / X_002 (NOT duplicates, kept both)

- `ecc_001.md` + `ecc_002.md` — **NOT duplicates** (001 = top-level + skills; 002 = specific skill files)
- `graphify_001.md` + `graphify_002.md` — **NOT duplicates** (001 = baseline + BENCHMARKS; 002 = README details)
- `ponytail_001.md` + `ponytail_002.md` — **NOT duplicates** (001 = overview; 002 = README details)
- `ralph_wiggum_001.md` + `ralph_wiggum_002.md` — **NOT duplicates** (001 = overview; 002 = PROMPT_plan_work deep dive)

- **recommendation:** **KEEP BOTH.** Different content; pairs cover different files/aspects of the same repos.

---

## Duplicate set 10: VINAY_MEETING_PACKET "merged from" (cross-refs)

The root-level `VINAY_MEETING_PACKET.md` (24,427 bytes) is the merged version per Phase 2 cleanup. The body now contains content from:
- Original `VINAY_MEETING_PACKET.md` (Verdict 2026-09-29 22:00 IST; question-driven edition)
- `STRATEGY_VINAY_TOMORROW.md` (Miss 2026-09-29; strategy narrative; now in archive)
- `VINAY_CTA.md` (Miss 2026-09-29; CTA + 3 strategic questions; now in archive)

The Provenance line at line 329 explicitly documents this: "Merged from `VINAY_MEETING_PACKET.md` (Verdict agent, 2026-09-29 22:00 IST), `STRATEGY_VINAY_TOMORROW.md` (Miss agent, 2026-09-29 IST), and `VINAY_CTA.md` (Miss agent, 2026-09-29 IST) per audit-5 finding. Source files deleted."

- **recommendation:** **KEEP AS-IS** — merged file is canonical; archival sources are in `_archive/`.

---

## Duplicate set 11: level2/models/ vs level2/out/ (already documented)

- **file_a:** `level2/models/<engine>/json/*.json` (4,000 JSON files)
- **file_b:** `level2/out/<engine>/<lang>/<page>.json` (4,001 JSON files + README.md)
- **status:** Already documented in `level2/MODELS_VS_OUT.md` — SHA256-verified identical. KEEP BOTH (per Phase 6 decision 2026-09-29). Out/ = writer's output (live, SEALED); models/ = documented view (PROMPT.md + RUN.md + metrics.json + quality_20.json metadata unique). **No MD duplicate** — these are JSON files.

---

## Duplicate set 12: PROBE22 PAUSED banner — 12 files with same banner header

12 files share the identical "🟡 W6 PAUSE BANNER (Miss agent, 2026-09-29 IST, per user directive)" banner at the top:

1. `level2/probe22/QLORA_EVAL_SPEC.md`
2. `level2/probe22/QLORA_READINESS.md`
3. `level2/probe22/QLORA_SMOKE_TEST.md`
4. `level2/probe22/QLORA_TRAINING_DATA.md`
5. `level2/probe22/MLX_INSTALL_PLAN.md`
6. `level2/probe22/MLX_INSTALL_RESULT.md`
7. `level2/probe22/MEMORY_AUDIT.md`
8. `level2/probe22/MEMORY_RECLAIM_RESULT.md`
9. `level2/probe22/LEADERBOARD_REFRESH_2026-09-29.md`
10. `docs/research/level7/W6_QLORA_SPEC.md`
11. `docs/research/level7/KILL_CRITERIA.md`
12. `W6_HANDOFF.md`

- **diff:** Each file's banner is identical (~700 bytes of HTML comment). Body content differs (each is a different W6-prep doc).
- **recommendation:** **KEEP BANNER** — the banner is a deliberate, applied-in-this-session policy marker; it documents the freeze state on each W6-prep file. NOT a deletion candidate; the banner provides the at-a-glance status.

---

## Summary

| Duplicate set | Files affected | Action |
|---|---|---|
| 1. OCR_AGENT_MEMORY_FEED copy.md | 1 | **DELETE** (L4 archive first) |
| 2-4. Root-vs-docs/ root summary/detail pairs | 6 files (3 pairs) | **KEEP BOTH** (different audiences) |
| 5. STRATEGY_VINAY_TOMORROW + VINAY_CTA | already merged | NO ACTION |
| 6. INTEGRATED-ELITE-STACK vs b5 refresh | 2 | **KEEP BOTH** (wiring vs source) |
| 7. b4_agent_tooling X.md / X_detailed.md | 13 files (6 pairs + 1 single) | ADVISORY MERGE ONLY (not urgent) |
| 8. b3 artifact_240 / 250 | 2 files | ADVISORY MERGE ONLY (low overlap) |
| 9. b5 001/002 pairs | 8 files (4 pairs) | **NOT duplicates; KEEP BOTH** |
| 10. VINAY_MEETING_PACKET merged refs | already merged | NO ACTION |
| 11. models/ vs out/ (JSON) | n/a (no MD) | KEEP BOTH (documented) |
| 12. PAUSED banner header | 12 files | **KEEP BANNER** (deliberate policy) |

**Total duplicates that warrant action: 1 file (`OCR_AGENT_MEMORY_FEED copy.md`).** Everything else is either a true paired summary/detail pair (different audiences), a deliberate banner, or already-merged. **No "stale" duplicates beyond the one copy file.**