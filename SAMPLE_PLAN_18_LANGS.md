> SUPERSEDED 2026-09-30 by docs/campaign/SAMPLING_PLAN.md (Wave 2, D04) — retained per L4; read the new plan for current state.

# SAMPLE_PLAN_18_LANGS.md — D4
**Date:** 2026-09-28 | **Source:** Untitled T4
**Target:** 100 samples/language × 18 languages = 1,800 minimum
**Current state:** 1,227 items (manifest.json final, post-purge)
**Gap:** Need to verify current state meets T4 standards; source remainder from existing source PDFs/papers if needed.

---

## 1. CURRENT STATE (per AGENT_PROTOCOL.md §1 — LOCKED 2026-09-26)

**Manifest final: n=1,227** (verified, post-corruption-purge + noise-drop).

| code | language | drawn n | human pairs | PDF layer | Sarvam fill | status |
|---|---|---|---|---|---|---|
| as | Assamese | 19 | 0 | 0 | 19 | shortfall (gates rejected 11) |
| bn | Bengali | 100 | 100 | 0 | 0 | ✅ target met |
| brx | Bodo | 67 | 0 | 47 | 20 | shortfall (mojibake) |
| doi | Dogri | 27 | 0 | 7 | 20 | shortfall (11 clean upstream) |
| gu | Gujarati | 24 | 0 | 4 | 20 | shortfall (gates rejected most) |
| hi | Hindi | 100 | 100 | 0 | 0 | ✅ target met |
| ks | Kashmiri | 100 | 0 | 100 | 0 | ✅ target met (PDF tier) |
| kok | Konkani | 100 | 0 | 100 | 0 | ✅ target met |
| mai | Maithili | 100 | 0 | 100 | 0 | ✅ target met |
| mni | Manipuri | 20 | 0 | 0 | 20 | shortfall (script gate fail) |
| mr | Marathi | 79 | 0 | 79 | 0 | shortfall (21 corrupt purged) |
| ne | Nepali | 37 | 0 | 17 | 20 | shortfall (29 corrupt purged) |
| or | Odia | 69 | 0 | 50 | 19 | shortfall (9 corrupt purged) |
| pa | Punjabi | 90 | 0 | 90 | 0 | shortfall (10 corrupt purged) |
| sa | Sanskrit | 100 | 100 | 0 | 0 | ✅ target met |
| sat | Santali | 20 | 0 | 0 | 20 | shortfall (0 clean PDF) |
| sd | Sindhi | 75 | 0 | 75 | 0 | shortfall (25 corrupt purged) |
| ur | Urdu | 100 | 0 | 100 | 0 | ✅ target met |
| **TOTAL** | **18 langs** | **1,227** | **300** | **769** | **158** | |

---

## 2. GAP ANALYSIS (T4.2 + T4.3)

**Languages below 100:** 11 of 18

| Lang | Current | Gap to 100 | Source-able from existing? | Plan |
|---|---|---|---|---|
| as | 19 | -81 | YES — PDF layers exist, but gates reject (control chars). **Source from official pairs if any exist**, else source from Sarvam leftovers (20 already used). Need: 81 more pages. |
| brx | 67 | -33 | PARTIAL — PDF layers mojibake-gated. Need 33 more clean pages. |
| doi | 27 | -73 | NO — only 11 clean upstream. Need 73 pages from Sarvam leftovers or accept fill. |
| gu | 24 | -76 | PARTIAL — gates reject most. Need 76 more, source from existing PDF pages with script-validation gate loosened? No — must keep gate strict. |
| mni | 20 | -80 | NO — script metadata fail. Need Meitei-Mayek pages. |
| mr | 79 | -21 | YES — corrupt purged, can re-source. Need 21 more clean pages. |
| ne | 37 | -63 | YES — 29 corrupt purged, can re-source. Need 63 more. |
| or | 69 | -31 | YES — 9 corrupt purged. Need 31 more. |
| pa | 90 | -10 | YES — 10 corrupt purged. Need 10 more. |
| sat | 20 | -80 | NO — 0 clean PDF upstream. **Santali gap is structural** — needs W6 fine-tune or vision-LLM. |
| sd | 75 | -25 | YES — 25 corrupt purged. Need 25 more. |

---

## 3. SOURCE STRATEGY (T4.2 — pull from existing source PDFs only, no fabrication)

### 3.1 Hard rules
- **NO downloads** of any kind (AGENTS.md §9 + OCR_AGENT_MEMORY_FEED.md §9)
- **NO fabrication** — every sample must trace to an actual page in `Datasets/akshardrishti_official/`
- **Varied pages, random offsets** — no "first page only" or "one paper per file" pattern
- **Stratified round-robin** across source PDFs (same basis as South 400)

### 3.2 Per-language source plan

| Lang | Source strategy | Pages needed | Estimated yield |
|---|---|---|---|
| as | Re-run extract_gt.py with relaxed MAX_CTRL_CHARS? NO — gates must stay strict. Source from Sarvam leftovers (20 used, 0 remaining per §1). **Realistic: accept 19 as final**, flag as low-n cell per §6.7 | 0 (accept) | 19 |
| brx | Source additional Bodo/gu pages (4,645 images in test split). **EXCLUDED** per §1 — `Bodo/gu/` is a copy of test set, NOT GT. Source from `Bodo/` proper (after mojibake gate). | 33 | ~10-20 more |
| doi | Only 11 clean upstream. Accept 27 as final, flag low-n. | 0 (accept) | 27 |
| gu | Re-run with script gate tweaked? NO. Accept 24 as final, flag low-n. | 0 (accept) | 24 |
| ks | ✅ 100 met | 0 | 100 |
| mni | Only 20 fill exist. Accept 20 as final. **PERMANENT caveat on leaderboard per §6.7 + §6.4** | 0 (accept) | 20 |
| mr | Re-source 21 more from official Marathi PDFs (1,071 pages, 21 purged). | 21 | ~20 more |
| ne | Re-source 63 more from official Nepali PDFs (464 pages, 29 purged). | 63 | ~30-50 more |
| or | Re-source 31 more from official Odia PDFs (1,625 pages, 9 purged). | 31 | ~30+ more |
| pa | Re-source 10 more from official Punjabi PDFs (23,372 pages, 10 purged). | 10 | 10+ |
| sat | 0 clean PDF. **PERMANENT gap**. D4 micro-repair option (5-10 pages, W5, only if freeze safe). | 0 | 20 (fill-only) |
| sd | Re-source 25 more from official Sindhi PDFs (4,342 pages, 25 purged). | 25 | ~25+ more |
| kok | ✅ 100 met | 0 | 100 |
| mai | ✅ 100 met | 0 | 100 |
| sa | ✅ 100 met | 0 | 100 |
| ur | ✅ 100 met | 0 | 100 |
| hi | ✅ 100 met | 0 | 100 |
| bn | ✅ 100 met | 0 | 100 |

---

## 4. RE-SOURCE EXECUTION PLAN

### 4.1 For re-sourceable langs (mr, ne, or, pa, sd)
1. Re-run `extract_gt.py` with hardened gate (no relaxation)
2. Draw additional samples via `build_manifest.py` from candidate pool
3. Update manifest + fragments
4. Re-run engines on new samples
5. Update sheet.csv

### 4.2 For low-n langs (as, doi, gu, mni, sat)
1. **Accept current n as final** — no fabrication
2. Flag as low-n cell per §6.7 (no winner claims)
3. Add permanent caveat to leaderboard rows
4. For sat: D4 micro-repair option (5-10 curated pages, W5, ONLY if freeze safe)

### 4.3 For structural gaps (sat — 0 clean PDF)
- D4 micro-repair: 5-10 curated pages from outside sources
- **Requires user approval** (downloads policy)
- Only sat + ks eligible (weak cells, beating Sarvam matters)
- Only after W5 freeze confirmation

---

## 5. SOUTH MERGE STATUS (T2.2 + T4.4)

**Already merged into main flow 2026-09-26:**
- Old `Datasets/{te,ta,kn,ml}/` deleted (byte-identical to official)
- South 400 samples in `arc_level_1/labeled/` (SEALED L1-GOLD)
- South 400 engine outputs in `level2/out/` (SEALED)
- No separate treatment — single source of truth

**T4.4 verification: PASSED — South samples already at the same standard (100/lang target met, full pipeline through 10 engines).**

---

## 6. EXECUTION TIMELINE

| Phase | Owner | Status | Deadline |
|---|---|---|---|
| Re-source mr/ne/or/pa/sd | Engine agent | PENDING | before W5 freeze |
| Accept low-n as final | Orchestrator | LOGGED | immediate |
| sat micro-repair (optional) | Engine agent + User approval | BLOCKED on user approval | W5 only |
| Update manifest + sheet.csv | Engine agent | After re-source | before W5 |

---

## 7. WHAT THIS PLAN DOES NOT DO

- Does NOT download any external data (downloads law)
- Does NOT fabricate GT (honesty law)
- Does NOT re-source for langs already at 100 (over-engineering)
- Does NOT re-source for barred langs (ks/mni/ur/sat/mr/ne PDF-tier) — already excluded from W6
- Does NOT re-source for PDF-tier langs where PDF GT is still useful (safe-for-SFT langs get prioritized)

---

## 8. OUTCOME

If re-source phase succeeds:
- 13 of 18 langs at 100 samples
- 5 of 18 langs (as, doi, gu, mni, sat) at 19-27 samples with permanent low-n caveats
- Total: ~1,350-1,400 items (improvement from 1,227)
- All bars to T4 met EXCEPT structural gaps (sat) which require user approval

If re-source phase blocked or fails:
- 1,227 items (current state)
- Same caveat structure
- W6 proceeds with current manifest
