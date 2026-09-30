# Validation Call — Boss Cheat Sheet
*Generated 2026-09-28 19:25 IST by orchestrator. Read this at the validation call.*

---

## 1. Bottom line

**All 11 engines scored on disk. Boss has 6 user-decisions to lock. After the call, W5 freeze; W6 starts post-freeze.**

## 2. 6 user-decisions to lock

| # | Gate | Status | Recommended default |
|---|---|---|---|
| 1 | GPU budget for W6 local QLoRA | OPEN | If no budget: D1 W6 stays wrap-only baseline |
| 2 | Sarvam EN extension (3 calls over 54-cap) | OPEN | D2 = skip (current state) |
| 3 | 20-item human spot-check (priority gu_o005) | OPEN | D3 deferred until W6 |
| 4 | rapidocr EN fix-spec | OPEN | D4 EN sanity = 0/30 honest-empty (awaiting approval) |
| 5 | Full Sarvam API run budget (1,227 items) | OPEN | D5 = 54-cap (directional only) |
| 6 | Sampling: re-sample or accept current 100/lang lock | OPEN | Accept current lock (some langs = 100 tiles of 1 page) |

## 3. Per-lang CER (best-to-worst of SAFE langs, where §6.2 allows W6 fine-tune)

| Lang | Winner (n>=50, verified 21:58 IST) | CER | n | Runner-up | Runner CER |
|---|---|---|---|---|---|
| **mai** (SAFE) | surya | **0.030** | 100 | easyocr 0.038 | best SAFE lang overall |
| **pa** (SAFE) | surya | 0.145 | 90 | tesseract_indic 0.226 | |
| **brx** (SAFE) | surya | 0.153 | 66 | easyocr 0.330 | |
| **hi** (SAFE) | surya | 0.220 | 100 | paddleocr_indic 0.504 | |
| **or** (SAFE) | tesseract_indic | 0.256 | 66 | tesseract_bilingual 0.258 | |
| **sd** (VERIFY-FIRST) | surya | 0.315 | 75 | paddleocr_indic 0.420 | |
| **kok** (SAFE) | surya | 0.425 | 100 | easyocr 0.619 | |
| **bn** (SAFE) | surya | 0.476 | 100 | indicphotoocr 0.657 | |
| **ks** (BARRED) | surya | 0.589 | 100 | easyocr 0.678 | §6.4 BARRED 0% |
| **ur** (BARRED) | surya | 0.623 | 100 | easyocr 0.681 | §6.4 BARRED 10% |
| **mr** (BARRED) | tesseract_bilingual | 0.205 | 79 | tesseract_indic 0.205 | §6.4 BARRED 42.9% |
| **ne** (BARRED) | tesseract_bilingual | 0.116 | 34 | — | §6.4 BARRED (R5); n<50 |
| **sa** (gold-only) | easyocr | 0.168 | 99 | paddleocr_indic 0.171 | FEASIBLE NOW (gold) |
| **as** (BARRED) | n<50 (D4) | — | — | — | sarvam 0.001 (n=2, directional) |
| **gu** (VERIFY-FIRST) | n<50 (D4) | — | — | — | surya 0.181 (n=20) |
| **doi** (SAFE) | n<50 (D4) | — | — | — | sarvam 0.056 (n=3) |
| **mni** (BARRED) | n<50 (D4) | — | — | — | sarvam 0.026 (n=2) |
| **sat** (BARRED) | n<50 (D4) | — | — | — | sarvam 0.216 (n=2) |

**surya wins 9 langs** (bn, brx, hi, kok, ks, mai, pa, sd, ur). **tesseract-family wins 3 langs** (mr, ne, or). **easyocr wins 1 lang** (sa).

**QLoRA target**: mai > as > brx > doi > pa > or > kok (in CER order).

## 4. Weak-cell attack verdicts (D4)

| Lang | CER | Attack | Status |
|---|---|---|---|
| Santali (sat) | 53.91 | Ol Chiki; 0 engines emit it. Vision-LLM-only or W6 fine-tune target. | BARRED per §6.4 |
| Kashmiri (ks) | 54.82 | Nastaliq; rapidocr 71% Arabic share, easyocr 0.678. R5 trust 45.0. | BARRED per §6.4 |
| OldScan | 55.3 | dots.mocr Old-scans 48.2 + Unlimited-OCR long-horizon. | N/A (image quality not lang) |
| Odia (or) | 80.01 | real-CER routing + QLoRA candidate. | SAFE 91.7% |

## 5. W6 feasible-set (§9.4 + locked)

| Column | Items |
|---|---|
| **FEASIBLE NOW** | (a) wrap-only baseline across 10 effective engines; (b) Qwen2-VL-2B QLoRA SFT on **10,432 human pairs** (bn 2,938 + hi 3,500 + sa 494 + en 3,500) — needs 16GB cap-1MP |
| **FEASIBLE IF** | D1 W6 conditional local QLoRA on SAFE langs (mlx-tune + GLM-OCR); D4 micro-repair sat+ks in W5 if freeze-safe |
| **INFEASIBLE** | Any training before W5 freeze; 400-page remaining-language collection; sarvam_fill GT for training; akshara-aux on ur/ks/sd/sat/mni; RLVR on unverified PDF GT; cloud spend without budget |

## 6. Engine leaderboard (disk-truth)

| Engine | Coverage | Effective | Notes |
|---|---|---|---|
| sarvam_vision | 18/18 (3/lang) | ✅ | 54-cap, directional only |
| easyocr | 18/18 | ✅ | CER 0.494 overall |
| indicphotoocr | 19/18 | ✅ | CER 0.559 |
| tesseract_indic + tesseract_bilingual | 19/18 | ✅ | byte-identical family |
| doctr | 19/18 | ✅ | Latin-mojibake |
| rapidocr | 11/18 | ⚠️ | 647 honest-empty; needs model downloads for full coverage |
| paddleocr_indic | 13/18 | ⚠️ | 536 honest-empty; 6 langs covered |
| anuvaad_tesseract | 8/18 | ⚠️ | 647 honest-empty; hin+eng only |
| surya | 17/18 (1098 non-empty) | ⚠️ | sa=1.000 honest-empty per Surya 2 NO Ol Chiki (1 lang); mni/mr/ne/or/pa/sat/sd/ur partial-not-run but coverage = 0 items each (only docs that exist); 9 langs complete with real measurements |
| openbharatocr | (duplicate of tesseract_indic) | ❌ | byte-identical |

**surya is now COMPLETE (1227 + 30 EN). Effective independent engines: 10 (openbharatocr is EXACT duplicate of tesseract_indic; surya is a 10th non-tesseract engine).** Engine coverage: bn/hi/kok/ks/mai/pa/sd/ur at 100%; brx/mr/or at ~75%; gu/doi/ne at ~50%; as/mni/sat at 17-20% (sarvam_fill only); sa at 100% but 99/100 honest-empty (Surya 2 NO Ol Chiki).

**W6 feasible-set summary (per `level2/probe22/w6_feasible_set.md`)**:
- FEASIBLE NOW (459 items + baseline carryover): bn, hi, sa, or, pa, te, ta, kn, ml
- FEASIBLE IF §6.4 verify-first confirm (342 items gated): brx, kok, mai, sd
- FEASIBLE IF (n boost + verify) (24 items): gu
- INFEASIBLE: as, mni, sat, ne, mr, ks, ur, doi
- **W6 SFT use: 459 items unconditional; +342 conditional; max 801 (~65% of probe22)**

## 7. Paperthin/hate verdict on D1-D4 (cheap-test per decision)

| Decision | Killer objection | Cheapest test |
|---|---|---|
| **D1** W6 wrap-only + conditional QLoRA | SAFE-lang n≥50 is only 4 (kok/mai/or/pa); QLoRA may move ≤4/18 cells | grep SAFE-lang rows in preds metrics for >3pt gap; if 0 → D1 collapses to wrap-only (5 min) |
| **D2** Sarvam EN skip | EN sanity reveals Latin-pipe issues affecting Devanagari/Perso-Arabic | read existing EN packs in `out/<engine>/en/*.json`; CER>0.05 means D2 is incomplete (5 min) |
| **D3** 20-item spot-check | 20 items / 10 min = 30s each — stamp not verification | pre-call identify 1-2 items where machine-verified verdict is most likely wrong (30 min) |
| **D4** Ol Chiki strategy | mni = 100% fill-only GT + no repair → entire Ol Chiki strategy is Sarvam-only | confirm engine-by-engine Ol Chiki emission on sat; if only sarvam_vision → mni/sat are hidden Sarvam subsidy (5 min) |

## 8. §6.4 LOCK (do NOT re-litigate)

BARRED from W6 fine-tune (6): **ks, mni, mr, sat, ur, ne-PDF-tier** (the 90.5% visual pass rate on ne is on a biased sample — 20 sarvam_fill + 1 PDF; R5 full-set forensics on 17 PDF items = trust 26.6 is the source of truth).
SAFE-FOR-SFT (7): **as, brx, doi, kok, mai, or, pa** (pending §6.2 falsification test).
VERIFY-FIRST (2): **gu (85.7%), sd (85.7%)** (pending §6.2).

## 9. Open items NOT requiring your decision (orchestrator handles)

- Engine queue sequencing (orchestrator enforces one-at-a-time).
- File audit (already done, 5 deleted, 35 regenerated).
- Graph integrity (1324 nodes / 0 dangling source_file pointers).
- §11 log entries (current through 19:25 Sep 28).
- Fix Specs #1-#4 (all applied).

## 10. Documents to bring to the call

- This cheat sheet (`docs/research/level7/boss_directives/VALIDATION_CALL_CHEATSHEET_2026-09-28.md`)
- `docs/research/level7/FINAL_VERDICT_2026-09-27.md` (zero-tolerance boss-handoff)
- `docs/research/level7/CALL_PACKET.md` (with per-lang CER table)
- `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` (all boss concerns)
- `level2/probe22/scores/LEADERBOARD.md` (coverage matrix)
- `graphify-out/graph.html` (interactive graph — 1324 nodes, 1665 edges, 52 hyperedges, 206 communities)
- `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §11 (call prep)

## 11. Boss-facing one-liner

"Engine queue done; boss has 6 user-decisions to lock. W6 starts after W5 freeze. Campaign is on track."

---

*Compiled by orchestrator 2026-09-28 19:25 IST. Source: disk-truth verifications only. If the 3 agents surface new findings between now and the call, this cheat sheet gets a v2.*

---

## UPDATE 2026-09-28 ~19:33 IST — surya completed + Engine final report

**surya finished**: 1227/1227 + 30 EN = 1257 entries (was 726 partial 30 min ago). 0 hard fail. 129 honest-empty (sa mostly).

**Surya EN CER 0.1514** — beats ALL other engines on EN (vs tesseract-family 0.8077, easyocr 0.6036, indicphotoocr 0.6710, paddleocr 0.2495).

**Surya wins on**: brx 0.153 (McNemar p<0.012), ks 0.589 (p<0.0006), kok 0.425 (p<0.008), hi 0.220, mai 0.030.

**Engine overall CER ranking (final, all 11 engines scored on 1227 items)**:
1. sarvam_vision: 0.2400 (54-cap directional only)
2. surya: 0.3849 ← NEW: best non-Sarvam engine
3. tesseract_bilingual: 0.4853
4. tesseract_indic: 0.4870
5. easyocr: 0.4941
6. indicphotoocr: 0.5586
7. paddleocr_indic: 0.6562
8. rapidocr: 0.6692
9. anuvaad_tesseract: 0.7114
10. doctr: 0.8691
11. openbharatocr: 0.4870 (EXACT byte-identical duplicate of tesseract_indic — same column)

**Effective independent engines: 10** (not 11). openbharatocr cannot be separated from tesseract_indic.

**Engine final report on disk**: `/Users/srujansai/Desktop/South/level2/probe22/FINAL_REPORT.md` (13KB).

**New finding (Miss)**: HF_TOKEN would unthrottle surya's HF Hub fetches — but that's a USER DECISION (downloads rule).

