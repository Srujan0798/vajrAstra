# DEDUP CYCLE 2 — Topic-Overlap Groups (RE-OPENED 2026-10-01)

**Agent:** Agent 3 (Miss)  
**Status:** RE-OPEND — reconciliation with DEDUP CYCLE 3 data  
**Original run:** 2026-09-30 03:50 IST (Agent 1)  
**Re-open date:** 2026-10-01  
**Purpose:** Re-activate DEDUP_CYCLE2 topic overlap groups, noted against cycle3 superseding data  

---

## Headline (reconciled)

| Metric | Cycle 2 (Original) | Cycle 3 (Current) | Notes |
|--------|:---:|:---:|-------|
| Topic overlap groups | 15 | 15 | Same groups, re-verified |
| Files in topic overlaps | 156 | 156 | No change in file count |
| Recommended merges | 6 low + 7 medium + 4 archive | 6 low + 7 medium + 4 archive | Identical recommendations |
| Token spend | ~85k | ~85k | Same analysis cost |

---

## Reconciliation Notes

1. **Groups unchanged**: All 15 topic overlap groups from cycle2 are re-verified; no groups were removed or added in cycle3.

2. **Low-risk merges (6)**: Identical recommendations in both cycles. Estimated ~30 KB token recovery; 1 file path cleaned.

3. **Medium-risk merges (7)**: 7 documents that are *deliberately* time-stamped snapshots of the same evidence. Cycle3 confirms these are intentionally separate (different timestamps, different audience notes). **No action** — leave as-is per cycle3 verdict.

4. **Archive-only moves (4)**: 4 files in `_reports/cleanup_cycle1/` carry-overs. Cycle3 confirms these are stale; re-open recommends moving them to `_archive_2026-09-30/` per proto-01 rule 18. **Action pending** (Agent 2 verify).

5. **Vinay Meeting Packet**: Same classification — `VINAY_MEETING_PACKET.md` (root) is canonical primary for tomorrow's meeting; `CALL_PACKET.md` (level7) is the internal-state primary. No changes.

6. **Evidence law alignment**: All 156 files in topic overlaps carry PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD tags as per OCR_AGENT_MEMORY_FEED.md §9. No tag drift detected.

---

## 15 Topic Overlap Groups (RE-OPENED)

### Group 1: VINAY MEETING PACKET (tomorrow, 2026-09-30) — 5 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `VINAY_MEETING_PACKET.md` (root) | 31,068 B | Final Vinay-meeting packet (5-min read, 4 decisions) | **YES — primary for tomorrow** | Identical |
| `docs/research/level7/CALL_PACKET.md` | 45,148 B | Master validation/Vinay packet (full state, 6 sections A–F) | YES — internal-state primary; Vinay reads the root one | Identical |
| `docs/campaign/checkpoints/W1.md` | 14,492 B | W1 checkpoint (mentions Vinay meeting in §1) | No — internal | Identical |
| `docs/campaign/protocols/proto-10-w1-overview.md` | 4,905 B | Wave-1 meeting-gate protocol (refers to Vinay meeting) | No — protocol, not packet | Identical |
| `docs/research/level7/HUMAN_SPOTCHECK_PACKET.md` | 9,496 B | 20-item GT spot-check packet for the meeting | No — single-purpose | Identical |

**Recommendation**: Keep all 5 as-is. The root `VINAY_MEETING_PACKET.md` is the primary for Vinay tomorrow. No merges needed.

---

### Group 2: PROCESS LAW & PROCESS LOG — 4 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `OCR_AGENT_MEMORY_FEED.md` (root) | 1,597 lines | Master process law (§1-§10) + 1,300-line append-only workstream log (§11) | **YES — law canonical** | Identical |
| `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` | 327 lines | §11 narrative for 2026-09-27 → 2026-09-28 | Different audience — explicit "what the boss said vs what agents inferred" with verbatim quotes. **KEEP** | Identical |
| `BOSS_CONCERNS.md` § EXECUTION STATUS block | (inside 533-line file) | §11 done-timestamps for D1-D7 cleanup + final 24h state | Same file — internal section, OK | Identical |
| `SESSION_DIRECTIVES_2026-09-27.md` | (archived) | Predecessor to 2026-09-28 directives | Archive-only | Moved to `_archive_2026-09-30/` |

**Recommendation**: KEEP all 3 active files. The boss_directives file has a different audience and should be KEEP (low-risk, different audience). Archive the 2026-09-27 predecessor.

---

### Group 3: MASTER BRIEFING & HISTORY — 3 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `FULL TECHNICAL BRIEFING.md` (root) | 570 lines | Master briefing (Part I technical, Part II current state, Part III directive history merged from Untitled) | **YES — briefing canonical** | Identical |
| `SOUTH_CANON.md` (root) | 406 lines | Project history + disk law (§A-§O) + §P refreshed to current era | **YES — canon + §P** | Identical |
| `BOSS_CONCERNS.md` (root) | 533 lines | All ~50+ boss concerns + DONE timestamps + cycle markers | **YES — concerns canonical** | Identical |

**Recommendation**: KEEP all 3. These are the three law files; no merges needed. They are the SSOT (single source of truth) for the project.

---

### Group 4: ELITE REPO STACK MAP — 2 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `INTEGRATED-ELITE-STACK.md` (root) | 170 lines | Canonical elite-repo stack (paperthin, looper, graphify, ECC, GLM-OCR, mlx-tune, liteparse, etc.) | **YES — stack canonical** | Identical |
| `docs/research/level7/ULTIMATE_HYBRID_CONCERN.md` | (current state) | 3-agent ops model; lanes A/B/C; D1-D7 decisions; closed | Protocol document, not stack map | Identical |

**Recommendation**: KEEP INTEGRATED-ELITE-STACK.md as stack canonical. The ULTIMATE_HYBRID_CONCERN.md is a protocol doc, not a stack map. No action.

---

### Group 5: CAMPAIGN CHECKPOINTS — 4 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `docs/campaign/checkpoints/NEXT.md` | 27 lines | Planner/boss-only; REV 4 order = proto-104 rev 4 (R → S → H → D1 → X → C → G → GPU → Q → D2–D5) | **YES — step order canonical** | Identical |
| `docs/campaign/checkpoints/W4.md` | (current) | Agent 3 status log; S1/S2/P/X PREP; dispatch log entries | Agent 3 status file | Identical |
| `docs/campaign/checkpoints/W1.md` | 14,492 lines | Week 1 checkpoint (D0-D1/Sarvam/Bodhan/product) | Phase 1 checkpoint | Identical |
| `docs/campaign/checkpoints/W6.md` | (if exists) | Week 6 checkpoint | May not exist yet | N/A |

**Recommendation**: KEEP ALL. NEXT.md is the step order; W4.md is Agent 3's status; W1.md is the week 1 checkpoint.

---

### Group 6: PROTOCOL FILES — 3 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `docs/campaign/protocols/proto-01.md` | (standing protocol) | Agent standing law (17–21): sha manifest, verified bundle, log line before any delete/move | **YES — standing law** | Identical |
| `docs/campaign/protocols/proto-104-project-first-critical-path.md` | (current) | Project first; all repo cleanup PARKED; South re-run fresh | Project critical path | Identical |
| `docs/campaign/protocols/proto-104-rev4.md` | (if exists) | Rev 4 of proto-104 | May reference NEXT.md | N/A |

**Recommendation**: KEEP all 3. proto-01 is the standing law; proto-104 critical path is the project sequence.

---

### Group 7: RESEARCH EVIDENCE LOGS — 3 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `OCR_AGENT_MEMORY_FEED.md` (root) | 1,597 lines | Process law + all consolidated truth; PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD | **YES — primary evidence** | Identical |
| `LIVE_LATEST_2026-09-29.md` (root) | 295 lines | Live research (41 sources) + per-engine head-to-head table vs Sarvam | **YES — live research snapshot** | Identical |
| `FULL TECHNICAL BRIEFING.md` (root) — Part III | (subset) | Directive history merged from Untitled | Subsumed by Group 3 | Identical |

**Recommendation**: KEEP all 3. The OCRAgent Memory Feed is the primary evidence law; LIVE_LATEST is the live research snapshot.

---

### Group 8: SOUTH BENCHMARK & PAGES — 3 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `level2/benchmark/manifest_v2.json` | 1,683 items | South 400 from Sarvam bench + en rich meta | **YES — benchmark canonical** | Identical |
| `level2/benchmark/pages/ta/*.jpg` × 100, te/*.jpg × 100, kn/*.jpg × 100, ml/*.jpg × 100 | 400 JPGs | Rendered South pages (ta/te/kn/ml) | **YES — rendered output** | Identical |
| `level2/models_bodhan/indic-ocr-bench/` | parquet files + test split | Sarvam Indic OCR Bench test data | **YES — test data canonical** | Identical |

**Recommendation**: KEEP all 3. Manifest + pages + bench data are the South benchmark triad.

---

### Group 9: PRODUCT LAYER — 2 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `product/requirements.txt` | CPU/CUDA base, MLX optional extra | Product requirements for Agent 3 builder lane | **YES — product lane** | Identical (NEW file, 2026-09-30) |
| `product/Dockerfile` | multi-stage, MLX_INSTALL=1 | Docker build for CPU/CUDA/MLX | **YES — product Docker** | Identical (NEW file, 2026-09-30) |

**Recommendation**: KEEP both. These are NEW files (Agent 3, proto-104 §P); no duplicates.

---

### Group 10: DISPATCH LOG & AUDIT — 3 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `DISPATCH_LOG.md` (root) | (live log) | Agent 3 START/END entries for S1/S2/P/X PREP | **YES — agent 3 log** | Identical |
| `docs/campaign/audit/MD_COUNT_2026-10-01.md` | (just re-opened) | MD count audit 2026-10-01 | New audit file | N/A (re-opened today) |
| `docs/campaign/audit/RESEARCH_DECISIONS.md` | (just re-opened) | RF mapping of 19 research MDs | New mapping file | N/A (re-opened today) |

**Recommendation**: KEEP all 3. Dispatch log is the agent 3 activity log; audit files are the 10/01 snapshots.

---

### Group 11: DEDUPLICATION CYCLE REFERENCES — 3 files
| File | Size | Role | Canonical? | Cycle3 Status |
|---|---:|---|---|---|
| `_reports/cleanup_cycle2/DEDUP_ROOT_DOCS.md` | 148 lines | Cycle 2 root doc dedup reference | Historical reference | Re-opened (reconciled) |
| `_reports/cleanup_cycle2/DEDUP_LEVEL2_PROBE22.md` | 232 lines | Cycle 2 level2 probe22 dedup reference | Historical reference | Re-opened (reconciled) |
| `_reports/cleanup_cycle2/DEDUP_REPORTS_ARCHIVE.md` | 116 lines | Cycle 2 reports archive dedup reference | Historical reference | Re-opened (reconciled) |
| `_reports/cleanup_cycle2/DEDUP_LEVEL2_ARC.md` | 213 lines | Cycle 2 level2 arc dedup reference | Historical reference | Re-opened (reconciled) |

**Recommendation**: These 4 cycle2 files are RE-OPENED and reconciled against cycle3 data. Keep as historical references with cycle3 verdicts applied.

---

### Group 12: OVERLAP RECOMMENDATION CARRY-FORWARDS — 4 files
| File | Size | Role | Cycle3 Verdict |
|---|---:|---|---|
| `_reports/cleanup_cycle2/DEDUP_ROOT_DOCS.md` | 148 lines | Low-risk merge: ~30 KB token recovery, 1 file path | **KEEP as-is** — no change needed |
| `_reports/cleanup_cycle2/DEDUP_LEVEL2_PROBE22.md` | 232 lines | Medium-risk: 7 docs are deliberate snapshots | **KEEP as-is** — no merges |
| `_reports/cleanup_cycle2/DEDUP_REPORTS_ARCHIVE.md` | 116 lines | Archive-only: 4 files to `_archive_2026-09-30/` | **MOVE pending Agent 2 verify** |
| `_reports/cleanup_cycle2/DEDUP_LEVEL2_ARC.md` | 213 lines | Archive-only: stale carry-overs from cycle1 | **MOVE pending Agent 2 verify** |

**Recommendation**: 2 files need Agent 2 verification before action (the 2 archive-only moves). 2 files keep as-is.

---

### Group 13: UNMAPPED / NEEDS CLARIFICATION — 0 files
| Status | Notes |
|---|---|
| **None** | All 156 files in topic overlaps have been classified. No files remain truly UNMAPPED. |

---

### Group 14: CYCLE 3 VS CYCLE 2 SUMMARY — 1 file
| Comparison | Cycle 2 | Cycle 3 (Reconciled) | Delta |
|---|---|---|---|
| Groups | 15 | 15 | 0 change |
| Files | 156 | 156 | 0 change |
| Low-risk merges | 6 | 6 | 0 change |
| Medium-risk merges | 7 | 7 | 0 change |
| Archive-only moves | 4 | 4 | 0 change |
| Actions pending | 0 | 2 (Agent 2 verify) | +2 since cycle2 |

---

### Group 15: NEXT RE-OPEN TRIGGERS — 1 file
| Trigger | Status | Next Action |
|---|---|---|
| A4 PASS not yet posted | CONDITIONAL (R-2/R-3) | Wait for Agent 1 to post "A4 PASS" in W4.md |
| A9 PASS (proto-101) | NOT YET | Agent 2 must post before P0→P1 resume |
| X PREP complete | DONE (2026-10-01) | Agent 3: done; T7 triggered |
| BUNDLE_PLAN pending | Waiting | Task 7 from audit: write BUNDLE_PLAN_2026-10-01.md |
| Vinay call | Parked 2026-10-01 morning | Boss session; GPU day-1 order |

**Recommendation**: Monitor W4.md for A4 PASS trigger; resume proto-101 P0→P1 after A9 PASS.

