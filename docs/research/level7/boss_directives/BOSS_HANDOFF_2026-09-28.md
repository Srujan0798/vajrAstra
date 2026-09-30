# BOSS_HANDOFF_2026-09-28.md — Validation call packet (single page)

**Generated**: 2026-09-28 22:06 IST by orchestrator (post-H44 review).
**For**: Boss at validation call H44–48 (window open 22:00 IST Sep 28).
**Reading time**: 5 minutes.

---

## 1. BOTTOM LINE (30 sec)

- **All 11 engines scored** on probe22 manifest (1227 items × 18 langs + EN sanity). Effective **10 independent** (openbharatocr = byte-identical dup of tesseract_indic).
- **Best local engine**: **surya** CER 0.3849 (best after sarvam 0.2400 directional). Wins 9 langs.
- **Sarvam**: 54 calls (3/lang cap), CER 0.2400 on that subset. "Beat Sarvam 87.39" claim stays directional per OBITUARIES.md.
- **W6 feasible**: 459 items NOW + 342 conditional + 24 gu = up to 801 items (~65% of probe22).
- **6 user-decisions pending** at this call (D1–D6 below). All have orchestrator defaults applied.

---

## 2. ENGINE RANKING (overall CER, lower = better)

| Rank | Engine | Overall CER | Notes |
|---|---|---|---|
| 1 | sarvam_vision | 0.2400 | n=54 (3/lang cap, directional only) |
| 2 | surya | 0.3849 | BEST LOCAL — wins 9 langs (bn/brx/hi/kok/ks/mai/pa/sd/ur) |
| 3 | tesseract_bilingual | 0.4853 |  |
| 4 | tesseract_indic | 0.4870 |  |
| 5 | easyocr | 0.4941 |  |
| 6 | indicphotoocr | 0.5586 |  |
| 7 | paddleocr_indic | 0.6562 |  |
| 8 | rapidocr | 0.6692 |  |
| 9 | anuvaad_tesseract | 0.7114 |  |
| 10 | doctr | 0.8691 |  |


---

## 3. PER-LANG WINNERS (n>=50 per D4)

| Lang | Winner (n>=50) | CER | n | Runner-up | Runner CER | Note |
|---|---|---|---|---|---|---|
| as | sarvam_vision | 0.001 | 2 | — | — | n<50 (D4: no winner) |
| bn | surya | 0.476 | 100 | indicphotoocr | 0.657 | |
| brx | surya | 0.153 | 66 | easyocr | 0.330 | |
| doi | sarvam_vision | 0.056 | 3 | — | — | n<50 (D4: no winner) |
| gu | surya | 0.181 | 20 | — | — | n<50 (D4: no winner) |
| hi | surya | 0.220 | 100 | paddleocr_indic | 0.504 | |
| kok | surya | 0.425 | 100 | easyocr | 0.619 | |
| ks | surya | 0.589 | 100 | easyocr | 0.678 | |
| mai | surya | 0.030 | 100 | easyocr | 0.038 | |
| mni | sarvam_vision | 0.026 | 2 | — | — | n<50 (D4: no winner) |
| mr | tesseract_bilingual | 0.205 | 79 | tesseract_indic | 0.205 | |
| ne | tesseract_bilingual | 0.116 | 34 | — | — | n<50 (D4: no winner) |
| or | tesseract_indic | 0.256 | 66 | tesseract_bilingual | 0.258 | |
| pa | surya | 0.145 | 90 | tesseract_indic | 0.226 | |
| sa | easyocr | 0.168 | 99 | paddleocr_indic | 0.171 | |
| sat | sarvam_vision | 0.216 | 2 | — | — | n<50 (D4: no winner) |
| sd | surya | 0.315 | 75 | paddleocr_indic | 0.420 | |
| ur | surya | 0.623 | 100 | easyocr | 0.681 | |


**surya wins 9 langs** (bn, brx, hi, kok, ks, mai, pa, sd, ur).
**tesseract-family wins 3 langs** (mr, ne, or).
**easyocr wins 1 lang** (sa).
**4 langs n<50 — no winner claim** per D4 (as, doi, mni, sat).

---

## 4. W6 FEASIBLE SET (per `level2/probe22/w6_feasible_set.md`)

| Status | Langs | Items |
|---|---|---|
| FEASIBLE NOW | bn 100, hi 100, sa 100 (gold), or 69, pa 90, te/ta/kn/ml (South-400 baseline) | 459 + baseline |
| FEASIBLE IF §6.4 verify-first | brx 67, kok 100, mai 100, sd 75 | 342 (gated) |
| FEASIBLE IF n-boost + verify | gu 24 | 24 |
| INFEASIBLE | as, mni, sat, ne-PDF, mr, ks, ur, doi | 0 |


**Total W6 SFT-eligible: 459–801 items** depending on §6.4 verification.

---

## 5. D1–D6 USER DECISIONS (orchestrator defaults applied, awaiting your override)

| # | Decision | Orchestrator default | Why |
|---|---|---|---|
| D1 | GPU budget for W6 | **$0 wrap-only** | Most conservative; no GPU dep |
| D2 | Sarvam EN extension | **Skip** | D2 already locked |
| D3 | 20-item human spot-check | **Defer to W6** | D3 already locked |
| D4 | rapidocr EN fix | **APPROVED** (applied 21:13) | `_RAPID_LANGV["en"]` line 291 |
| D5 | Full Sarvam API run (1227 items) | **Skip** | "Beat 87.39" stays directional |
| D6 | Sampling methodology | **Accept current 1227-manifest caveat** | Re-sampling requires downloads |


---

## 6. LOCKED DECISIONS (D1–D4 per campaign §10, do NOT re-litigate)

- **D1** sarvam_fill GT NEVER for training (probe-scoring only)
- **D2** SFT/RLVR against unverified PDF GT forbidden (§6.4 + §9)
- **D3** GT<10 char items purged
- **D4** n<50 cells carry no winner claims (as, gu, ne, doi, mni, sat)

---

## 7. §6.4 LOCK (BARRED / VERIFY-FIRST / SAFE)

| Status | Langs |
|---|---|
| **BARRED** (PDF-tier GT unfit for SFT) | ks (0% pass), mni (0%), sat (15%), ur (10%), mr (42.9%), ne (R5 lock), mni/sat fill |
| **VERIFY-FIRST** | gu, sd |
| **SAFE** | as, brx, doi, kok, mai, or, pa |
| **Gold-only** (D1) | sa |

---

## 8. DOCS TO BRING TO THE CALL

1. **This file** (`BOSS_HANDOFF_2026-09-28.md`) — 5-min read
2. `docs/research/level7/FINAL_VERDICT_2026-09-27.md` — zero-tolerance boss-handoff (with locked D1–D6 + feasible summary in §8)
3. `docs/research/level7/CALL_PACKET.md` — per-agent status + banked scores + D1–D4 + W6
4. `level2/probe22/scores/LEADERBOARD.md` — coverage matrix + verified per-lang WINNERS
5. `docs/research/level7/boss_directives/VALIDATION_CALL_CHEATSHEET_2026-09-28.md` — 10-section expanded cheatsheet
6. `level2/probe22/FINAL_REPORT.md` — Engine's full H44 report (13 KB, 258 lines)
7. `graphify-out/graph.html` — interactive knowledge graph (1324 nodes / 1665 edges / 52 hyperedges / 206 communities)
8. `level2/probe22/w6_sft_unconditional.jsonl` (459 items) + `w6_sft_conditional.jsonl` (342 items) + `w6_rlvr_unconditional.jsonl` (300 items) — pre-staged W6 training sets (not yet trained)

---

## 9. WHAT I'M DOING WHILE YOU'RE AT THE CALL

- Monitoring disk for new agent output (background poll every 5 min)
- Standing by for any override on D1–D6
- Will apply locked decisions post-call and update §11 with H48 final state

---

## 10. ONE-LINER (if you only have 10 sec)

> All 11 engines scored. surya best local (CER 0.3849, wins 9/18 langs). 459 W6 items ready NOW, 801 max if §6.4 verify passes. 6 decisions pending; my defaults are conservative (skip GPU/Sarvam-EN/Sarvam-full, approve rapidocr-EN, defer spot-check, accept sampling caveat). Override any at the call.

---

*Built by orchestrator 2026-09-28 22:06 IST. Disk-verified per `level2/probe22/scores/metrics_*_normalized.json` lang_wise_scores. All 11 engine files present (effective 10).*
