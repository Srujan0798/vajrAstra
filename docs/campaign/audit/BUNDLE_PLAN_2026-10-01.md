# Bundle Plan — 2026-10-01

**Owner:** Agent 3 (Miss)  
**Status:** DRAFT — awaiting boss go / proto-104 Day 5 gate  
**Generated:** 2026-10-01  
**Purpose:** Consolidate all audit outputs into a boss-ready bundle plan; every phase needs the boss's "go" per proto-01 rules 17-21.

---

## Bundle Contents (all created in this session)

| # | Artifact | Path | Status |
|---|----------|------|--------|
| 1 | MD Count | `docs/campaign/audit/MD_COUNT_2026-10-01.md` | ✅ DONE |
| 2 | Research Decisions Mapping | `docs/research/RESEARCH_DECISIONS.md` | ✅ DONE |
| 3 | DEDUP CYCLE 2 Re-opened | `docs/campaign/audit/DEDUP_CYCLE2_REOPENED.md` | ✅ DONE |
| 4 | WORTH Ranking | `docs/campaign/audit/FILE_WORTH_RANKING.csv` | ✅ DONE |
| 5 | Audit Report (summary) | *generated inline below* | ✅ DONE |

---

## Audit Report — Summary

### Live MD Files
- **Total:** 601 .md files (excluding Datasets/, .venv/, _archive/, node_modules/)
- **Scored:** 513 files in WORTH ranking (FILE_WORTH_RANKING.csv)
- **WORTH range:** 71 (highest) to 38 (lowest)
- **Top 5 by WORTH:** OCR_AGENT_MEMORY_FEED.md, LIVE_LATEST_2026-09-29.md, FULL TECHNICAL BRIEFING.md, AGENTS.md, DISPATCH_LOG.md (all WORTH 71)
- **Bottom 5 by WORTH:** .venv311 package license/README files (all WORTH 38)

### Key Decisions — RF Mappings
- **19 research MDs** mapped to RQ-1 through RQ-19 in `docs/research/RESEARCH_DECISIONS.md`
- **15 DEDUP_CYCLE2 topic overlap groups** re-opened and reconciled in `docs/campaign/audit/DEDUP_CYCLE2_REOPENED.md`
- **All 156 files in topic overlaps** classified; 6 low-risk merges + 7 medium-risk + 4 archive-only recommended

### Agent 3 Workstream (proto-104 §P)
- **S1:** Real South feasibility (0/23,001 clean, 76% legacy mojibake) ✅
- **S2:** 400 South pages rendered (ta/te/kn/ml × 100) ✅
- **P:** Product layer (requirements.txt, Dockerfile, B21 spec) ✅
- **X PREP:** run_bench_x.py + 5-item dry run (hin CER 0.104, kan CER 0.056, tel CER 0.008) ✅

### Sealed Dirs — Verified Untouched
- `level2/out`: 4,001 files
- `level2/reports`: 0 files
- `level2/probe22/out`: 0 files
- `arc_level_1`: 413 files
- `Datasets/akshardrishti_official`: 34,871 files

### Constraints Honored
- ✅ NEW files only — no edits to existing files under `level2/`, `docs/`, root
- ✅ No downloads — used only installed tesseract data + on-disk caches
- ✅ No new languages — only tested installed langs (hin/kan/tel)
- ✅ No commits — all changes in working tree only
- ✅ CPU only — no GPU used
- ✅ No sealed dir modifications

---

## Phases Pending — Boss Go Required

| Phase | Trigger | Action Required |
|-------|---------|-----------------|
| **A4 PASS** | Not yet posted in W4.md | Agent 1 must post "A4 PASS" before P0→P1 resume |
| **A9 PASS** (proto-101) | Not yet posted | Agent 2 must post before P0→P1 can advance |
| **Vinay call** | 2026-10-01 morning | Boss session; GPU day-1 order; HF token → Mac .env only |
| **proto-104 Day 5** | Boss says "resume cleanup" | proto-98 cleanup master resume |
| **BUNDLE_PLAN** | This file | awaiting boss review |

---

## Immediate Next Steps (if boss says "go")

1. **If A4 PASS posted:** Agent 1 proceeds with S4 engine runs on South 400
2. **If A9 PASS posted:** Agent 3 resumes proto-101 P0→P1
3. **If Vinay call convenes:** GPU day-1 setup; HF token to Mac .env; Bodhan download
4. **If proto-98 resume:** Agent 3 does read-only inventory first; every mutating phase needs boss go

---

## Register

- **DISPATCH_LOG.md** entries recorded for all Agent 3 actions (S1 START/END, S2 START/END, P START/END, P CPU DRY RUN START/END, X PREP START/END, WORTH CSV RUN, BUNDLE PLAN START/END)
- **No git commit** performed (per proto-01 rule 18)
- **No training** performed
- **No Sarvam calls** beyond free credit ₹67 cap (already expended)
- **Sealed dirs** verified untouched (per proto-01 rule 19)

