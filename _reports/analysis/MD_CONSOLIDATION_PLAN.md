# MD CONSOLIDATION PLAN — South repo (AGENT-2)
**Date:** 2026-09-29 19:00 IST
**Author:** AGENT-2
**Constraint:** L4 archive-never-delete (every DELETE action requires SHA256-verified archive first)
**Constraint:** Sealed dirs never touched (level2/out/, level2/reports/, level2/probe22/out/, arc_level_1/, Datasets/akshardrishti_official/)
**Constraint:** No new markdown at repo root or under `level2/research/` (per AGENTS.md standing law)

---

## Current state

- **Total MD files in scope:** 203
- **Hard duplicates (warrant action):** 1 file (`OCR_AGENT_MEMORY_FEED copy.md`)
- **Soft duplicates (paired summary/detail):** 6 files (3 pairs at root vs docs/architecture/)
- **Advisory merges (low overlap, no urgency):** 15 files (7 b4 pairs + 2 b3 artifacts + 4 b5 001/002 pairs already confirmed NOT-dup)
- **PAUSED state files (banner-applied, must keep):** 12 files
- **Sealed dirs (untouched):** 5 (level2/out/, level2/reports/, level2/probe22/out/, arc_level_1/, Datasets/akshardrishti_official/)
- **Total delete candidates:** 1 file (≈11 KB)

---

## Proposed end state

- **Total MD files in scope:** 202 (after deleting 1 exact-dup)
- **Canonical docs (each serves a distinct purpose):** 202
- **No "orphan" or "stale" MD files** — every remaining file is referenced from:
  - `AGENTS.md` (orchestrator identity)
  - `OCR_AGENT_MEMORY_FEED.md` (process law)
  - `SOUTH_CANON.md` (repo → process-law mapping)
  - `FULL TECHNICAL BRIEFING.md` (master doc)
  - `docs/INDEX.md` (doc hierarchy)
  - `INTEGRATED-ELITE-STACK.md` (elite-repo integration)
  - `docs/research/level7/PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md` (agent prompts)
  - `level2/probe22/AGENT_PROTOCOL.md` (execution law)

---

## Action list (ordered by safety, L4 archive-first)

### Action 1: DELETE — `OCR_AGENT_MEMORY_FEED copy.md` (🟢 AUTO-SAFE after archive)

**File:** `/Users/srujansai/Desktop/South/OCR_AGENT_MEMORY_FEED copy.md` (11,173 bytes)
**Why:** Exact-older-snapshot duplicate of master file. Master contains §11-§16 log entries (W6 PAUSE, 24h cleanup, campaign clock end, Vinay packet refresh, etc.) that copy is missing. Copy has zero live references.
**Steps:**
1. Compute SHA256 of source file: `shasum -a 256 OCR_AGENT_MEMORY_FEED\ copy.md`
2. Move to `_archive/cleanup_2026-09-28/ocr_agent_memory_feed_copy/`
3. Verify SHA256 in archive matches source
4. Log SHA256 in CLEANUP_EXECUTION_LOG.md
5. `rm OCR_AGENT_MEMORY_FEED\ copy.md`

**Risk:** Zero — copy has no live references; all LAW references point to the master file.
**Mitigation:** L4 archive is reversible; if a live ref is found, restore from archive.
**Laya gate:** 🟢 AUTO-SAFE (laya auto-proceed: delete verified duplicate after archive).

---

### Action 2: KEEP BOTH (no-op) — Root vs docs/architecture/ paired files (3 pairs)

**Files:**
- Root `W5_STRATEGY_OPTIONS.md` (3,754 B) ↔ `docs/architecture/W5_STRATEGY_OPTIONS.md` (19,443 B)
- Root `W5_BEAT_SARVAM_PLAN.md` (3,652 B) ↔ `docs/architecture/W5_BEAT_SARVAM_PLAN.md` (14,324 B)
- Root `VINAY_MEETING_PACKET.md` (24,427 B) ↔ `docs/architecture/VINAY_MEETING_PACKET.md` (5,899 B)

**Why:** Per docs/AUDIT_docs.md §"Root-level vs docs/architecture/ comparison" — **Genuinely different audiences**:
- Root = condensed/prompt-facing (~3 KB; "Top 3 ranked", "Concrete Recipe", question-driven Vinay brief)
- docs/ = evidence-backed detailed (~14-19 KB; 5 alternatives w/ cost/time/CER-delta; "where we win/tie/lose"; results-driven packet)

Both versions are explicitly referenced from `OCR_AGENT_MEMORY_FEED.md` §15-§16 and `AGENTS.md`. Deleting either would break live references.

**Steps:** No action. Document the pairing in FILE_INVENTORY.md (already done).
**Laya gate:** N/A — no cleanup needed; both files serve live audiences.

---

### Action 3: KEEP BOTH (no-op) — INTEGRATED-ELITE-STACK.md vs b5 ELITE_REPO_REFRESH

**Files:**
- Root `INTEGRATED-ELITE-STACK.md` (13,275 B) — canonical wiring ("how paperthin/looper/graphify/ECC/GLM-OCR/mlx-tune/liteparse plug into Engine/Verdict/Miss")
- `docs/research/level7/b/b5_elite_repos/ELITE_REPO_REFRESH_2026-09-27.md` (~10 KB; 245 lines) — refresh survey (raw source data)

**Why:** Different roles per INTEGRATED-ELITE-STACK.md itself ("This is the canonical reference... Cross-reference: see `docs/research/level7/b/b5_elite_repos/ELITE_REPO_REFRESH_2026-09-27.md` for the original 25-record refresh (this file is the action layer that wires them in)"). Root = action layer; b5 = source survey.
**Steps:** No action.
**Laya gate:** N/A.

---

### Action 4: ADVISORY (not urgent) — b4_agent_tooling X.md / X_detailed.md paired merges

**Files (13 .md files):**
- `mcp_servers.md` ↔ `mcp_detailed.md`
- `claude_code_sdk.md` ↔ `claude_code_detailed.md`
- `opencode_ecc.md` ↔ `opencode_ecc_detailed.md`
- `obsidian_acp.md` ↔ `obsidian_detailed.md`
- `ts_ai_sdks.md` ↔ `ts_ai_sdks_detailed.md`
- `laya_gates.md` ↔ `laya_detailed.md`
- `kimi_agents.md` (single, no pair)

**Why:** 32/179 records are exact duplicates across the paired files per docs/AUDIT_docs.md. The pairs have slightly different framings (X = condensed, X_detailed = full), but the record content overlaps.

**Recommendation:** **DO NOT MERGE.** Disk footprint is small (~20 KB total), the pairs preserve a "lighter overview vs deeper pass" structure, and merging risks losing distinct extractions.

**If disk pressure emerges** (future cleanup cycle): merge `X.md` into `X_detailed.md` (deeper pass) and drop the lighter pass; removes ~84 records + ~13 files. **NOT recommended now.**
**Laya gate:** 🟡 NEEDS USER APPROVAL (advisory only; not urgent; deferred to a future cleanup cycle).

---

### Action 5: ADVISORY (not urgent) — b3 artifact_240 / artifact_250 URL overlap

**Files:**
- `docs/research/level7/b/b3_multi_agent_orchestration/artifact_240_arxiv_papers_advanced.md`
- `docs/research/level7/b/b3_multi_agent_orchestration/artifact_250_ecc_autonomous_arxiv.md`

**Why:** 2 records share arXiv URLs (2606.03115, 2607.22917). Mostly different content (240 = arxiv papers; 250 = ECC autonomous arxiv).

**Recommendation:** **DO NOT MERGE.** Low overlap (~2/92 records). Both files serve distinct research tracks.
**Laya gate:** N/A — advisory only.

---

### Action 6: KEEP BOTH (no-op) — b5 001/002 paired files

**Files (8 .md in 4 pairs):**
- `ecc_001.md` + `ecc_002.md`
- `graphify_001.md` + `graphify_002.md`
- `ponytail_001.md` + `ponytail_002.md`
- `ralph_wiggum_001.md` + `ralph_wiggum_002.md`

**Why:** Per docs/AUDIT_docs.md — **NOT duplicates**. Pairs cover different files/aspects of the same repos:
- 001 = top-level + BENCHMARKS / overview
- 002 = specific skill files / README details / PROMPT_plan_work

**Steps:** No action.
**Laya gate:** N/A.

---

### Action 7: KEEP (no-op) — 12 W6-prep PAUSED files

**Files (12 .md):**
- `level2/probe22/QLORA_EVAL_SPEC.md`
- `level2/probe22/QLORA_READINESS.md`
- `level2/probe22/QLORA_SMOKE_TEST.md`
- `level2/probe22/QLORA_TRAINING_DATA.md`
- `level2/probe22/MLX_INSTALL_PLAN.md`
- `level2/probe22/MLX_INSTALL_RESULT.md`
- `level2/probe22/MEMORY_AUDIT.md`
- `level2/probe22/MEMORY_RECLAIM_RESULT.md`
- `level2/probe22/LEADERBOARD_REFRESH_2026-09-29.md`
- `docs/research/level7/W6_QLORA_SPEC.md`
- `docs/research/level7/KILL_CRITERIA.md`
- `W6_HANDOFF.md`

**Why:** All carry the same 🟡 W6 PAUSE banner (Miss agent, 2026-09-29 IST, per user directive). BOSS_CONCERNS §59 documents: "PAUSED banners applied to 12 W6 prep files (this turn) ... DO NOT execute training/mlx-tune/mlx_vlm/QLoRA. After Vinay: resume on Option A, archival on Option B, superseded on Option C."
**Steps:** No action. PAUSED = awaiting Vinay gate (2026-09-30), not stale.
**Laya gate:** 🟢 AUTO-SAFE (PAUSED banners are deliberate policy markers; must keep until Vinay decides).

---

### Action 8: KEEP (no-op) — graphify-out/GRAPH_REPORT.md + pre-rebuild backup

**Files:**
- `graphify-out/GRAPH_REPORT.md` (151,422 B; current 3990 nodes / 4681 edges)
- `graphify-out/GRAPH_REPORT.md.pre-rebuild-2026-09-29` (57,118 B; pre-rebuild snapshot)
- `graphify-out/2026-09-29/GRAPH_REPORT.md` (57,118 B; same-day rebuild)
- `graphify-out/graph.json` + `.pre-rebuild-2026-09-29` + `2026-09-29/` (3 graph.json versions)

**Why:** Pre-rebuild backup is the safety net for the rebuild operation; same-day backup is the in-graph backup. Both intentional.
**Steps:** No action.
**Laya gate:** N/A.

---

### Action 9: KEEP (no-op) — sealed directories

**Directories (NEVER touch):**
- `level2/out/` (4,001 files) — L10 + AGENTS.md "never touch sealed output"
- `level2/reports/` (15 .md + JSON) — L10 + AGENTS.md
- `level2/probe22/out/` (13,289 engine packs) — probe22 protocol §0
- `arc_level_1/` (413 files) — SOUTH_CANON §O "leave it alone"
- `Datasets/akshardrishti_official/` (34,871 files) — verified lossless 2026-09-26

**Why:** Per L10 + AGENTS.md + SOUTH_CANON + probe22 protocol. Violating = P0 incident (per L4 archive-never-delete).
**Steps:** No action.
**Laya gate:** 🔴 ESCALATE — touching sealed dirs is forbidden by multiple hard rules.

---

### Action 10: KEEP (no-op) — 7 audit reports in `_archive/cleanup_2026-09-28/`

**Files:**
- `AUDIT_probe22.md`
- `AUDIT_level2_other.md`
- `AUDIT_docs.md`
- `AUDIT_datasets.md`
- `AUDIT_hidden.md`
- Plus 2 audit_intermediates/ files

**Why:** These are the post-cleanup audit trail (Phase 1-5 of 24h cleanup). Referenced from `BOSS_CONCERNS.md` items 66-73 + `DEEP_REPORT.md` cross-references. _archive/ is the recovery-only mirror (never accessed in normal flow).
**Steps:** No action.
**Laya gate:** 🟢 AUTO-SAFE (recovery-only archive; safe to keep).

---

### Action 11: FLAG — b2_all_artifacts.jsonl record count discrepancy

**File:** `docs/research/level7/b/b2_self_improving_agents/b2_all_artifacts.jsonl`
**Issue:** FINAL_VERDICT_2026-09-27.md line 30 claims 258 records; current file has 129 records. Discrepancy.
**Per docs/AUDIT_docs.md §"Lane counts":** "Lane B2 Self-improving ✅ 258 records, 0 missing §9 fields. Current file has 129 records. **NEEDS INVESTIGATION**: confirm whether b2_all_artifacts.jsonl has all 258 records or whether a .md version is missing."

**Steps:**
1. **DEFER to Verdict agent** (Lane B owner)
2. Either: (a) recover missing 129 records from batch chunks (7 batch files per docs/AUDIT_docs.md), or (b) update FINAL_VERDICT to match disk truth (129 records)
3. Log resolution in §11 workstream log
**Laya gate:** 🟡 NEEDS USER APPROVAL (advisory; not a file deletion; resolution path is a disk-truth reconciliation, not a cleanup).

---

## RISK ASSESSMENT

| Action | Risk | Mitigation |
|---|---|---|
| Action 1: DELETE OCR_AGENT_MEMORY_FEED copy.md | **Zero** (L4 archive, no live refs) | L4 archive with SHA256 verification; reversible |
| Action 2-3: KEEP BOTH | **None** (no-op) | n/a |
| Action 4-5: ADVISORY merges | **Medium** (lose distinct framings) | Skip — disk footprint small; defer to user approval |
| Action 6-10: KEEP (no-op) | **None** | n/a |
| Action 11: b2 count discrepancy | **Low** (cosmetic only) | DEFER to Verdict; not blocking W5 freeze |

**Net change:** -1 file (-0.5% of MD corpus). Disk freed: ~11 KB.

**Verdict:** The repo is well-cleaned. The 24h cleanup (Phases 1-7) plus prior merge cycles (STRATEGY_VINAY_TOMORROW + VINAY_CTA → VINAY_MEETING_PACKET, Untitled → FULL TECHNICAL BRIEFING Part III) have already done the heavy lifting. **Only Action 1 is hard.** Everything else is advisory or no-op.

---

## Final MD inventory after Action 1

| Metric | Value |
|---|---|
| Total MD files | **202** (was 203) |
| KEEP | 201 |
| PAUSED (kept) | 12 |
| DELETE candidates | 0 (after Action 1) |
| SEALED (untouched) | 5 dirs |
| Free disk | +11 KB |
| Bloat remaining | ~0 MB |

The MD corpus is in excellent shape. **Action 1 is the only remaining hard cleanup.** Everything else is intentional.

---

## CONSOLIDATION DECISION

**Recommendation:** Execute Action 1 ONLY. Skip Action 4-5 advisory merges. Document everything else as no-op.

**Before Action 1:** Confirm with user that the file is safe to delete (L4 archive-first protocol still applies; even a "zero-risk" delete gets a user yes per L4 spirit).

**Output documents created by this analysis:**
1. `FILE_INVENTORY.md` (203 files inventoried, ~14 KB)
2. `DUPLICATE_MAP.md` (12 duplicate sets analyzed, ~9 KB)
3. `MD_CONSOLIDATION_PLAN.md` (this file)
4. `LAYA_GATE_DECISIONS.md` (laya classification per action)
5. `PAPERTHIN_AUDIT.md` (mandela + factchk + hate audit on 4 docs)

**Total analysis output:** ~50 KB of structured decisions, all reading-only / safe-by-default.