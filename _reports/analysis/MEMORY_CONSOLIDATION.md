# Memory Consolidation — single source of truth map

**Date:** 2026-09-29 18:30 IST
**Author:** orchestrator (agent-4 turn)
**Scope:** Repo-wide memory/file inventory → identify ownership, find duplicates, recommend consolidation
**Hard rule:** §9 + user "DO NOT delete memory files" — this document is a MAP, not an executor.
**Reference:** BOSS_CONCERNS.md items 7, 9, 14 (hierarchy + merge); L4 archive-never-delete.

---

## 1. Current memory/law files (the "remember surface")

| File | bytes | lines | Owns (single fact) | Duplicates / overlaps with |
|---|---:|---:|---|---|
| `AGENTS.md` | 3,897 | 68 | Load order for any agent + orchestrator identity (WHO I AM) + hard rules | References OCR_AGENT_MEMORY_FEED, SOUTH_CANON, INTEGRATED-ELITE-STACK; not duplicated |
| `OCR_AGENT_MEMORY_FEED.md` | 167,059 | 1,046 | Process law (§9), state (§10), 270+ workstream-log entries (§11) | §P is mirrored in SOUTH_CANON; §10 state mirrored in HIERARCHY_MAP; §11 entries cross-over with MISS_MONITOR log entries |
| `SOUTH_CANON.md` | 19,965 | 406 | Repo operational law (sections A–O) + §P = how repo maps to OCR_AGENT_MEMORY_FEED | §P overlaps with AGENTS.md "how this repo maps" pointer; not full duplication |
| `BOSS_CONCERNS.md` | 32,486 | 349 | All 50+ boss concerns numbered 1–52 with DONE/RESOLVED timestamps | **Heavy overlap** with `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` (C1–C17 vs items 1–52) and with FINAL_VERDICT_2026-09-27.md outcomes |
| `DISPATCH_LOG.md` | 4,995 | 101 | Dispatch format + 4 Untitled-phase dispatches + agent queue status snapshot | Format lives only here; queue status is now stale (agents are mid-campaign, not in the static 22:30 IST snapshot) |
| `docs/research/level7/MISS_MONITOR.md` | 53,411 | 744 | Append-only monitor log (every Miss sweep) | **Heavy overlap** with OCR_AGENT_MEMORY_FEED §11 entries that Miss wrote; CALL_PACKET §2 engine queue is a derived view |
| `docs/research/level7/CALL_PACKET.md` | 45,148 | 483 | Per-agent status + banked scores + D1–D4 outcomes + W6 spec link | Overlaps with FINAL_VERDICT_2026-09-27.md (verdicts) + LEADERBOARD.md (banked scores) + MISS_MONITOR (engine queue) |
| `docs/research/level7/FINAL_VERDICT_2026-09-27.md` | 14,899 | 283 | Zero-tolerance boss-handoff doc: §3 verdicts, §6.4 lock, §10 audited claims | **Heavy overlap** with VALIDATION_CALL_CHEATSHEET_2026-09-28.md (same boss reading material); partial overlap with CALL_PACKET |
| `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` | 21,520 | 327 | 17 distinct boss concerns (C1–C17) with verbatim quotes + status | **Heavy overlap** with BOSS_CONCERNS.md (50+ items) — same source, different granularity |
| `docs/research/level7/boss_directives/VALIDATION_CALL_CHEATSHEET_2026-09-28.md` | 9,397 | 158 | Boss reading material for H44–48 call (decisions, CER, D1–D4, §6.4) | **Heavy overlap** with FINAL_VERDICT_2026-09-27.md + CALL_PACKET.md (banked scores) |
| `docs/research/level7/boss_directives/VALIDATION_CALL_SCRIPT_2026-09-28.md` | 3,923 | 77 | 22:00 IST call agenda + timing | Unique — operational script, no equivalent |
| `docs/research/level7/boss_directives/CONSOLIDATED_PARALLEL_WORK_2026-09-28.md` | 12,586 | 204 | Parallel work + boss-directives digest for that day | Overlaps with BOSS_CONCERNS § cleanup results + DEEP_REPORT § Phases 2–4 |
| `docs/research/level7/boss_directives/BOSS_HANDOFF_2026-09-28.md` | 6,338 | 143 | Pre-call handoff packet | Overlaps with VALIDATION_CALL_CHEATSHEET (same info, different presentation) |
| `FULL TECHNICAL BRIEFING.md` | 34,025 | 570 | Master doc (Part I technical + Part II current state + Part III directive history) | Part III overlaps with BOSS_CONCERNS § directive history; intentional — Part III is the canonical merge per audit-5 finding A |
| `HIERARCHY_MAP.md` | 16,849 | 316 | File linkage + sealed-dir map (D7 deliverable) | Overlaps with `docs/INDEX.md` (lighter version of same map) |
| `W5_FREEZE_PLAN.md` | 11,386 | 170 | W5 freeze window plan (timeline, checklist, agenda, risks) | Overlaps with `docs/research/level7/W5_FREEZE_AGENDA.md` (12K, 283 lines, more detail); overlaps with VINAY_MEETING_PACKET § 1 (Option A/B/C timing) |
| `W6_QLORA_SPEC.md` | 14,690 | 257 | W6 QLoRA scaffold spec (kok + pa only, K1-locked) | Lives at `docs/research/level7/W6_QLORA_SPEC.md` — **duplicate at root** (none — root is the only copy; verified) |
| `EVIDENCE_SUMMARY.md` | 6,833 | 105 | Disk-truth evidence for Vinay meeting (engine ranking, per-lang CER, W6 GT guard) | Overlaps with CALL_PACKET §3 + LEADERBOARD.md + FINAL_VERDICT §3 |
| `VINAY_MEETING_PACKET.md` | 24,427 | 329 | Vinay meeting packet (Option A/B/C ranking + CTA + risk register + wall-clock math) | Unique — Vinay-specific; absorbed STRATEGY_VINAY_TOMORROW.md + VINAY_CTA.md per DEEP_REPORT Phase 2 |
| `DEEP_REPORT.md` | 10,056 | 170 | 24h cleanup cycle report (Phases 1–7, disk freed, sealed dirs verified) | Unique — historical artifact of the cleanup |
| `INTEGRATED-ELITE-STACK.md` | 13,321 | 170 | Integrated elite-repo map (install/keep/watch + wiring) | Unique — wired into 3 PROMPT_*.md files |
| `docs/research/level7/W5_FREEZE_AGENDA.md` | 11,904 | 283 | W5 freeze agenda (8 items, ~15-20 min) | Overlaps with root `W5_FREEZE_PLAN.md` §3 |
| `docs/research/level7/KILL_CRITERIA.md` | 16,058 | 228 | K1/K2/K3/K4/K5 thresholds + USER-set parameters | Unique — gates law |
| `docs/research/level7/SANTA_METHOD_FINAL.md` | 17,970 | 387 | Adversarial review (santa-method) of LEADERBOARD | Unique — adversarial-review artifact |
| `docs/research/level7/HUMAN_SPOTCHECK_PACKET.md` | 9,496 | 68 | 20-item human spot-check packet | Unique — D3 deliverable |
| `docs/research/level7/H48_HOSTILE_PASS.md` | 21,402 | 192 | H48 hostile pass output (Verdict agent) | Overlaps with FINAL_VERDICT_2026-09-27.md § audits reconciled |
| `W5_BEAT_SARVAM_PLAN.md` | 3,652 | — | Quick W5 plan (referenced in W5_STRATEGY_OPTIONS, VINAY_MEETING_PACKET) | Overlaps with VINAY_MEETING_PACKET § strategy options |
| `W5_STRATEGY_OPTIONS.md` | 3,754 | — | A/B/C strategy options summary | Overlaps with VINAY_MEETING_PACKET § strategy options |
| `LEVEL7_RESEARCH_FINDINGS.md` | 10,014 | — | Level 7 findings digest | Overlaps with `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §11 + W6_QLORA_SPEC |
| `PER_LANG_ROUTING.md` | 5,861 | — | Per-language routing table | Overlaps with EVIDENCE_SUMMARY §3 + LEADERBOARD |
| `COMPUTE_BUDGET_ESTIMATE.md` | 7,166 | — | GPU/compute cost estimates | Overlaps with INTEGRATED-ELITE-STACK § keep-as-reference + C1 lane |
| `LEVEL7_RESEARCH_FINDINGS.md` | — | — | Findings digest | — |
| `W6_HANDOFF.md` | 18,114 | — | W6 handoff (earlier Engine doc) | Overlaps with W6_QLORA_SPEC.md (newer) |

**Total memory surface:** ~750 KB across 30+ files.

---

## 2. Real duplicates (substantial content overlap)

| # | Files | Overlap | Consolidation recommendation |
|---|---|---|---|
| D1 | `BOSS_CONCERNS.md` + `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` | Same boss concerns (~80% content overlap) — items 1–52 vs C1–C17 | **RECOMMENDED:** KEEP BOTH (different granularity + different lock dates; BOSS_CONCERNS.md has per-item DONE/RESOLVED timestamps, SESSION_DIRECTIVES has verbatim quotes). Add cross-link. NO DELETE — user hard rule. |
| D2 | `W5_FREEZE_PLAN.md` + `docs/research/level7/W5_FREEZE_AGENDA.md` | W5 freeze plan + agenda — same items, different framing | **RECOMMENDED:** KEEP BOTH (root = TLDR for boss; level7 = full 283-line agenda). Already cross-referenced. NO MERGE. |
| D3 | `W6_HANDOFF.md` (root) + `docs/research/level7/W6_QLORA_SPEC.md` | Earlier Engine handoff vs newer Verdict spec | **RECOMMENDED:** SUPERSEDE — `W6_QLORA_SPEC.md` is newer (2026-09-29 07:30 IST) and K1-locked; `W6_HANDOFF.md` is older (2026-09-28). Add a "superseded by" note at top of W6_HANDOFF.md. NO DELETE (hard rule). |
| D4 | `docs/research/level7/FINAL_VERDICT_2026-09-27.md` + `docs/research/level7/boss_directives/VALIDATION_CALL_CHEATSHEET_2026-09-28.md` | Both = boss reading material for the validation call; same D1–D4 outcomes | **RECOMMENDED:** KEEP BOTH (different role: FINAL_VERDICT = zero-tolerance snapshot, CHEATSHEET = agenda + decisions). Already cross-referenced. NO MERGE. |
| D5 | `docs/research/level7/H48_HOSTILE_PASS.md` + `docs/research/level7/FINAL_VERDICT_2026-09-27.md` | Hostile pass output (long) vs zero-tolerance edition (digest) | **RECOMMENDED:** KEEP BOTH (H48_HOSTILE_PASS is the input, FINAL_VERDICT is the verdict). Already cross-referenced. |
| D6 | `docs/research/level7/boss_directives/CONSOLIDATED_PARALLEL_WORK_2026-09-28.md` + `BOSS_CONCERNS.md` § REPO CLEANUP + `DEEP_REPORT.md` § Phases 2–4 | Same parallel-work outcome | **RECOMMENDED:** KEEP all 3 (different views: parallel = narrative, BOSS_CONCERNS = checklist, DEEP_REPORT = summary). Already cross-referenced. |
| D7 | `docs/research/level7/boss_directives/BOSS_HANDOFF_2026-09-28.md` + `docs/research/level7/boss_directives/VALIDATION_CALL_CHEATSHEET_2026-09-28.md` | Pre-call handoff packet ≈ Cheatsheet | **RECOMMENDED:** KEEP BOTH (BOSS_HANDOFF = what agents did that day; CHEATSHEET = what boss reads at the call). No merge. |
| D8 | `W5_BEAT_SARVAM_PLAN.md` + `W5_STRATEGY_OPTIONS.md` + `VINAY_MEETING_PACKET.md` § strategy options | All three cover W5 strategy | **RECOMMENDED:** KEEP all 3 (W5_BEAT_SARVAM = quick plan, W5_STRATEGY_OPTIONS = A/B/C summary, VINAY_MEETING_PACKET = full packet for the meeting). Already cross-referenced. |

**No actual destructive merge recommended.** The repo's memory surface is large but each file owns a distinct facet. Cross-linking already exists in AGENTS.md load order. The boss-hard-rule "DO NOT delete memory files" makes consolidation = MAP, not = execute deletes.

---

## 3. Single-source-of-truth map (what each fact's canonical file is)

| Fact (what you want to know) | Canonical file | Section |
|---|---|---|
| What is the project? | `FULL TECHNICAL BRIEFING.md` | Part I §1, Part II §1 |
| What is the master doc? | `AGENTS.md` lines 1–2 | header |
| Agent load order | `AGENTS.md` lines 6–25 | numbered list 1–8 |
| Orchestrator identity (WHO I AM) | `AGENTS.md` lines 43–62 | "WHO I AM" section |
| Hard rules (no training, no downloads, no Sarvam past 54 calls) | `OCR_AGENT_MEMORY_FEED.md` §9 + `AGENTS.md` lines 38–41 | mirrored |
| Process law (HOW to do research → probe → freeze → train) | `OCR_AGENT_MEMORY_FEED.md` §4 | numbered list 1–3 |
| Project history (BHASHINI, Vinay, 9/10 Sep meetings) | `SOUTH_CANON.md` §A–§H | sections A–H |
| Repo operational law (work/labeled/prompts/scripts disk contract) | `SOUTH_CANON.md` §H, §N | section H + section N |
| How repo maps to OCR_AGENT_MEMORY_FEED | `SOUTH_CANON.md` §P | section P (locked 2026-09-27) |
| Boss concerns catalog (all 50+) | `BOSS_CONCERNS.md` | items 1–52 |
| Boss verbatim quotes (C1–C17) | `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` | C1–C17 |
| 3-agent ops model (Engine/Verdict/Miss) | `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §1 | table |
| Evidence law (PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD) | `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §9 | numbered list 1–5 |
| Locked decisions D1–D4 | `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §10 | D1, D2, D3, D4 |
| W6 feasible set + kill criteria | `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §11 + `docs/research/level7/KILL_CRITERIA.md` | campaign §11 + K1–K5 |
| W6 QLoRA scaffold (kok + pa) | `docs/research/level7/W6_QLORA_SPEC.md` | section 1–7 (K1-LOCKED 2026-09-29) |
| W5 freeze agenda (8 items) | `docs/research/level7/W5_FREEZE_AGENDA.md` + `W5_FREEZE_PLAN.md` (TLDR) | both |
| Engine leaderboard (probe22) | `level2/probe22/scores/LEADERBOARD.md` | table |
| South-400 sealed leaderboard | `level2/reports/LEADERBOARD.md` (SEALED) | table |
| Engine CER by script (n=126) | `level2/reports/CER_BY_SCRIPT.md` (SEALED) | sections |
| Probe22 execution law (engines, GT gates, scorer) | `level2/probe22/AGENT_PROTOCOL.md` | §0–§10 |
| §6.4 GT verdicts (BARRED/SAFE/VERIFY-FIRST) | `OCR_AGENT_MEMORY_FEED.md` §10 + `level2/probe22/gt_verification.json` + `level2/probe22/AGENT_PROTOCOL.md` §6.4 | three-way mirrored |
| GT forensics (ne R5 lock, trust scores) | `level2/probe22/gt_forensics.json` | per-language |
| Sarvam API baseline (54-cap) | `level2/probe22/preds/sarvam_vision/*.json` + `EVIDENCE_SUMMARY.md` §6 | disk + summary |
| McNemar paired comparison results | `level2/probe22/scores/mcnemar_full_matrix.json` | matrix |
| Per-language CER (all 18 langs × 11 engines) | `level2/probe22/CALL_PACKET.md` §3 | per-lang table |
| Weak cells (sat, ks, OldScan, or) | `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §11 + `EVIDENCE_SUMMARY.md` §4 | both |
| Vinay meeting packet | `VINAY_MEETING_PACKET.md` | full document |
| Boss reading material (validation call) | `docs/research/level7/boss_directives/VALIDATION_CALL_CHEATSHEET_2026-09-28.md` | full |
| Adversarial review (santa-method) | `docs/research/level7/SANTA_METHOD_FINAL.md` | full |
| 20-item human spot-check packet | `docs/research/level7/HUMAN_SPOTCHECK_PACKET.md` | full |
| Validation-call agenda + timing | `docs/research/level7/boss_directives/VALIDATION_CALL_SCRIPT_2026-09-28.md` | full |
| Cleanup 24h cycle results | `DEEP_REPORT.md` + `CLEANUP_EXECUTION_LOG.md` + `AUDIT_REPORT.md` | three-way |
| Hierarchy + linkage map | `HIERARCHY_MAP.md` (D7) + `docs/INDEX.md` (lighter) | both |
| Integrated elite repo stack | `INTEGRATED-ELITE-STACK.md` | full |
| Current graph state (3990 nodes) | `graphify-out/graph.json` + `GRAPH_REPORT.md` + `docs/INDEX.md` line 52 | disk-truth |
| W5/W6/W7 validation loop (NEW 2026-09-29) | `W5_W6_W7_LOOP.yaml` (root, this turn) | full |
| 24h cleanup audit reports | `_archive/cleanup_2026-09-28/AUDIT_{probe22,level2_other,docs,datasets,hidden}.md` | 7 reports |

---

## 4. Consolidation actions (recommended)

### 4a. CONSOLIDATE NOW (small, safe)

| Action | Files | Why safe |
|---|---|---|
| Add "superseded by W6_QLORA_SPEC.md" banner at top of `W6_HANDOFF.md` | `W6_HANDOFF.md` → `docs/research/level7/W6_QLORA_SPEC.md` | Non-destructive banner; old doc retained for history |
| Cross-link `BOSS_CONCERNS.md` ↔ `SESSION_DIRECTIVES_2026-09-28.md` (one-line each) | both | Removes "which one is canonical?" confusion |
| Cross-link `FULL TECHNICAL BRIEFING.md` Part III ↔ `BOSS_CONCERNS.md` | both | Already exists in Part III banner; verify |
| Move `W5_BEAT_SARVAM_PLAN.md` + `W5_STRATEGY_OPTIONS.md` → `docs/research/level7/` (move, don't delete) | two root files → `docs/research/level7/` | Aligns with campaign workspace convention; old paths in `docs/INDEX.md` |

### 4b. KEEP AS-IS (no action recommended)

| Cluster | Why keep |
|---|---|
| BOSS_CONCERNS / SESSION_DIRECTIVES / VALIDATION_CALL_CHEATSHEET / BOSS_HANDOFF / VALIDATION_CALL_SCRIPT / CONSOLIDATED_PARALLEL_WORK | Each owns a distinct facet of boss-directives; consolidation would lose granularity. Already cross-linked. |
| FINAL_VERDICT / H48_HOSTILE_PASS / SANTA_METHOD_FINAL / HUMAN_SPOTCHECK_PACKET | Each is a Verdict deliverable artifact; KEEP all for audit trail. |
| W5_FREEZE_PLAN (root TLDR) + W5_FREEZE_AGENDA (level7 full) | Two different audiences: root = boss quick-read, level7 = Verdict full briefing. Already cross-referenced. |
| MISS_MONITOR / CALL_PACKET / OCR_AGENT_MEMORY_FEED §11 | Three different log types: MISS_MONITOR = real-time monitor log, CALL_PACKET = per-agent status snapshot, OCR_AGENT_MEMORY_FEED §11 = orchestrator workstream log. KEEP all three. |
| EVIDENCE_SUMMARY / LEADERBOARD / VINAY_MEETING_PACKET | Different consumers (Vinay vs boss vs agents). KEEP all. |

### 4c. ARCHIVE-ONLY (would be cleaner if user approved)

The user's "DO NOT delete memory files" rule + L4 archive-never-delete law block any destructive action. The following **would** be merged if the rule were relaxed — listed for transparency, **NOT EXECUTED**:

- `W6_HANDOFF.md` (18K) → merge into `docs/research/level7/W6_QLORA_SPEC.md` (newer supersedes); keep as `W6_HANDOFF_2026-09-28.archive.md`
- `BOSS_CONCERNS.md` (32K) → keep items 1–52 verbatim, link to SESSION_DIRECTIVES for verbatim quotes (already 80% the same content)
- `docs/research/level7/H48_HOSTILE_PASS.md` (21K) → verdict-edition already in FINAL_VERDICT_2026-09-27.md; H48 = input, FINAL_VERDICT = digest

### 4d. Net consolidation impact if 4a + 4c were both applied

- Before: 30+ memory files, ~750 KB
- After: ~28 files, ~700 KB (only 4a is small; 4c would save ~50K but is BLOCKED)

**The repo is already consolidated.** The cross-link network is dense (AGENTS.md load order + every doc's "Cross-references" section). The cost of further merging > the benefit, because each file owns a distinct facet.

---

## 5. Single-source-of-truth discipline (the rule going forward)

Before creating a new memory file, ask:
1. **Does an existing file already own this fact?** Check the SSOT map (§3) first.
2. **If yes, can I append a section instead of creating a new file?** Append if file is append-only (workstream logs) or if it has a clear section for this (e.g., CALL_PACKET §X).
3. **If a new file is needed, link it from AGENTS.md load order + INDEX.md + the relevant SSOT owner.**

For facts that already have a canonical file:
- **Do not duplicate content** in new files. Reference the canonical file by path.
- **Do not create a "summary" of an existing doc** unless it serves a different audience (boss vs agents).

For facts that don't have a canonical file:
- **Create one canonical file** + register it in this map + AGENTS.md load order.

---

## 6. Audit (this consolidation pass)

- Files inventoried: 30 memory/law files at root + `docs/research/level7/` + `docs/research/level7/boss_directives/`
- Total bytes: ~750 KB
- Files that DUPLICATE substantially: 8 clusters (D1–D8 in §2)
- Files recommended for action: 4 (small cross-link banners in §4a)
- Files recommended for ARCHIVE: 3 (BLOCKED by user rule, §4c)
- Files recommended to MOVE: 2 (root → `docs/research/level7/`, §4a)
- New file created this turn: `W5_W6_W7_LOOP.yaml` (canonical loop spec, no SSOT conflict)
- Sealed dirs untouched: `level2/out/` (4,001 files), `level2/reports/` (48 files), `level2/probe22/out/` (13,289 files), `arc_level_1/` (413 files), `Datasets/akshardrishti_official/` (34,871 files) — verified by disk count.

---

## 7. Next-step recommendation

Apply the §4a actions in the next orchestrator turn (~10 minutes of work):
1. Add banner to `W6_HANDOFF.md` pointing to `W6_QLORA_SPEC.md`.
2. Cross-link `BOSS_CONCERNS.md` ↔ `SESSION_DIRECTIVES_2026-09-28.md`.
3. Move `W5_BEAT_SARVAM_PLAN.md` + `W5_STRATEGY_OPTIONS.md` → `docs/research/level7/`.
4. Update `docs/INDEX.md` with the new paths.

§4b + §4c: **HOLD** (cross-links already exist; destructive merges BLOCKED).

This map will be re-checked at the W5 freeze call (Wed 2026-10-01+) as part of the verification gate.
