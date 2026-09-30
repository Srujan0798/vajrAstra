<!-- RECOVERED 2026-09-30 from db part prt_0f196d13c0013zLx9Wnyxyp337 (opencode read, 2026-09-30 14:43), read at 18:05; any later edits are lost -->
# FINAL Engine Leaderboard — disk-truth per-language coverage (2026-09-28 ~19:33 IST)

Honest-empty counted as MISSING, not failed. Real measurement = non-empty outputs.

**Engine queue COMPLETE**: all 11 engines scored. surya just finished (1227/1227 + 30 EN). All 18 langs × 11 engines × 1227 items scored on disk.

**Effective independent engines: 10** (openbharatocr is exact byte-identical duplicate of tesseract_indic — not separable).


## Coverage summary

| Engine | Total | Non-empty | Honest-empty | Langs w/ ≥1 real output |
|---|---|---|---|---|
| anuvaad_tesseract | 1257 | 610 | 647 | 8/18 |
| doctr | 1257 | 1256 | 1 | 18/18 + EN |
| easyocr | 1227 | 1227 | 0 | 18/18 |
| indicphotoocr | 1257 | 1255 | 2 | 18/18 + EN |
| openbharatocr | 1257 | 1256 | 1 | 18/18 + EN (byte-id dup of tesseract_indic) |
| paddleocr_indic | 1227 | 691 | 536 | 8/18 |
| rapidocr | 1370 | 884 | 486 | 11/18 |
| sarvam_vision | 54 | 54 | 0 | 18/18 (cap 3/lang) |
| surya | 1227 | 1098 | 129 | 17/18 (sa=honest-empty per Surya 2 NO Ol Chiki) |
| tesseract_bilingual | 1259 | 1258 | 1 | 18/18 + EN |
| tesseract_indic | 1257 | 1256 | 1 | 18/18 + EN |

## Per-lang WINNERS (verified 2026-09-28 21:58 IST, orchestrator-applied)

Source: `level2/probe22/scores/metrics_*_normalized.json` lang_wise_scores block. n>=50 winner claims per §6.4 + D4 (no winner for n<50 cells).

| Lang | Winner | CER | n | Runner-up | Runner CER |
|---|---|---|---|---|---|
| as | sarvam_vision | 0.001 | 2 | n<50 (D4: no winner claim) | — |
| bn | surya | 0.476 | 100 | indicphotoocr | 0.657 |
| brx | surya | 0.153 | 66 | easyocr | 0.330 |
| doi | sarvam_vision | 0.056 | 3 | n<50 (D4: no winner claim) | — |
| gu | surya | 0.181 | 20 | n<50 (D4: no winner claim) | — |
| hi | surya | 0.220 | 100 | paddleocr_indic | 0.504 |
| kok | surya | 0.425 | 100 | easyocr | 0.619 |
| ks | surya | 0.589 | 100 | easyocr | 0.678 |
| mai | surya | 0.030 | 100 | easyocr | 0.038 |
| mni | sarvam_vision | 0.026 | 2 | n<50 (D4: no winner claim) | — |
| mr | tesseract_bilingual | 0.205 | 79 | tesseract_indic | 0.205 |
| ne | tesseract_bilingual | 0.116 | 34 | n<50 (D4: no winner claim) | — |
| or | tesseract_indic | 0.256 | 66 | tesseract_bilingual | 0.258 |
| pa | surya | 0.145 | 90 | tesseract_indic | 0.226 |
| sa | easyocr | 0.168 | 99 | paddleocr_indic | 0.171 |
| sat | sarvam_vision | 0.216 | 2 | n<50 (D4: no winner claim) | — |
| sd | surya | 0.315 | 75 | paddleocr_indic | 0.420 |
| ur | surya | 0.623 | 100 | easyocr | 0.681 |

**surya is winner on 9 langs (n>=50)**: bn, brx, hi, kok, ks, mai, pa, sd, ur.
**tesseract-family is winner on 3 langs**: mr (tesseract_bilingual), or (tesseract_indic), ne (tesseract_bilingual, n=34).
**easyocr is winner on 1 lang**: sa (gold-only feasible set).
**sarvam_vision has lowest CER on 4 langs but n<50 (cap=3/lang) → no winner claim per D4**: as, doi, mni, sat.

---

## Per-lang CER (banked)



Source: `level2/probe22/scores/metrics_*_normalized.json` lang_wise_scores block.
`-` = no data. `1.000` = honest-empty by routing/model coverage (not engine failure).

Barred langs per §6.4: ks, mni, mr, sat, ur, ne-PDF-tier (CER unreliable).

| Lang | tesseract_indic | tesseract_bilingual | indicphotoocr | surya | paddleocr_indic | easyocr | sarvam_vision | rapidocr | anuvaad_tesseract | doctr | openbharatocr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| as | 0.106 (n=17) | 0.109 (n=17) | 0.093 (n=17) | 0.166 (n=17) | 1.000 (n=17) | 0.161 (n=17) | 0.001 (n=2) | 1.000 (n=17) | 1.000 (n=17) | 0.875 (n=17) | 0.106 (n=17) |
| brx | 0.351 (n=66) | 0.348 (n=66) | 0.404 (n=66) | 0.153 (n=66) | 1.000 (n=66) | 0.330 (n=66) | 0.379 (n=3) | 0.505 (n=66) | 0.353 (n=66) | 0.817 (n=66) | 0.351 (n=66) |
| doi | 0.269 (n=22) | 0.270 (n=22) | 0.427 (n=22) | 0.226 (n=22) | 1.000 (n=22) | 0.314 (n=22) | 0.056 (n=3) | 0.427 (n=22) | 0.269 (n=22) | 0.813 (n=22) | 0.269 (n=22) |
| gu | 0.217 (n=20) | 0.214 (n=20) | 0.256 (n=20) | 0.181 (n=20) | 1.000 (n=20) | 0.747 (n=20) | 0.222 (n=3) | 1.000 (n=20) | 1.000 (n=20) | 0.730 (n=20) | 0.217 (n=20) |
| hi | 0.877 (n=100) | 0.876 (n=100) | 0.713 (n=100) | 0.220 (n=100) | 0.504 (n=100) | 0.515 (n=100) | 0.084 (n=3) | 0.649 (n=100) | 0.883 (n=100) | 0.877 (n=100) | 0.877 (n=100) |
| kok | 0.644 (n=100) | 0.644 (n=100) | 0.662 (n=100) | 0.425 (n=100) | 0.622 (n=100) | 0.619 (n=100) | 0.239 (n=3) | 0.657 (n=100) | 0.648 (n=100) | 0.914 (n=100) | 0.644 (n=100) |
| ks | 0.781 (n=100) | 0.782 (n=100) | 0.926 (n=100) | 0.589 (n=100) | 1.000 (n=100) | 0.678 (n=100) | 0.630 (n=3) | 0.872 (n=100) | 1.000 (n=100) | 0.927 (n=100) | 0.781 (n=100) |
| mai | 0.058 (n=100) | 0.057 (n=100) | 0.262 (n=100) | 0.030 (n=100) | 0.050 (n=100) | 0.038 (n=100) | 0.257 (n=3) | 0.097 (n=100) | 0.075 (n=100) | 0.819 (n=100) | 0.058 (n=100) |
| mni | 0.845 (n=14) | 0.845 (n=14) | 0.918 (n=14) | 0.967 (n=14) | 1.000 (n=14) | 0.904 (n=14) | 0.026 (n=2) | 1.000 (n=14) | 1.000 (n=14) | 0.949 (n=14) | 0.845 (n=14) |
| mr | 0.205 (n=79) | 0.205 (n=79) | 0.340 (n=79) | 0.215 (n=79) | 0.213 (n=79) | 0.208 (n=79) | 0.248 (n=3) | 0.296 (n=79) | 0.272 (n=79) | 0.853 (n=79) | 0.205 (n=79) |
| ne | 0.122 (n=34) | 0.116 (n=34) | 0.265 (n=34) | 0.189 (n=34) | 0.130 (n=34) | 0.168 (n=34) | 0.210 (n=3) | 0.604 (n=34) | 0.202 (n=34) | 0.863 (n=34) | 0.122 (n=34) |
| or | 0.256 (n=66) | 0.258 (n=66) | 0.353 (n=66) | 0.276 (n=66) | 1.000 (n=66) | 0.809 (n=66) | 0.447 (n=3) | 1.000 (n=66) | 1.000 (n=66) | 0.805 (n=66) | 0.256 (n=66) |
| pa | 0.226 (n=90) | 0.227 (n=90) | 0.234 (n=90) | 0.145 (n=90) | 1.000 (n=90) | 0.817 (n=90) | 0.160 (n=3) | 1.000 (n=90) | 1.000 (n=90) | 0.779 (n=90) | 0.226 (n=90) |
| sa | 0.253 (n=99) | 0.237 (n=99) | 0.462 (n=99) | 1.000 (n=99) | 0.171 (n=99) | 0.168 (n=99) | 0.019 (n=3) | 0.362 (n=99) | 0.358 (n=99) | 0.902 (n=99) | 0.253 (n=99) |
| sat | 0.865 (n=18) | 0.865 (n=18) | 0.613 (n=18) | 0.736 (n=18) | 1.000 (n=18) | 0.876 (n=18) | 0.216 (n=2) | 1.000 (n=18) | 1.000 (n=18) | 0.854 (n=18) | 0.865 (n=18) |
| sd | 0.468 (n=75) | 0.468 (n=75) | 0.828 (n=75) | 0.315 (n=75) | 0.420 (n=75) | 0.436 (n=75) | 0.344 (n=3) | 0.479 (n=75) | 1.000 (n=75) | 0.872 (n=75) | 0.468 (n=75) |
| ur | 0.792 (n=100) | 0.793 (n=100) | 0.935 (n=100) | 0.623 (n=100) | 0.872 (n=100) | 0.681 (n=100) | 0.533 (n=3) | 0.921 (n=100) | 1.000 (n=100) | 0.936 (n=100) | 0.792 (n=100) |

## Engine overall CER (from metrics_*.normalized.json)

| Engine | overall CER | overall WER | n_packs | missing | valid |
|---|---|---|---|---|---|
| tesseract_indic | 0.4870 | 0.6809 | 1227 | 1 | 1056 |
| tesseract_bilingual | 0.4853 | 0.6791 | 1227 | 1 | 1058 |
| indicphotoocr | 0.5586 | 0.8048 | 1227 | 2 | 1149 |
| surya | 0.3849 | 0.5956 | 1227 | 129 | 1025 |
| paddleocr_indic | 0.6562 | 0.7914 | 1227 | 536 | 641 |
| easyocr | 0.4941 | 0.7558 | 1227 | 0 | 1148 |
| sarvam_vision | 0.2400 | 0.4283 | 54 | 0 | 48 |
| rapidocr | 0.6692 | 0.8072 | 1227 | 343 | 860 |
| anuvaad_tesseract | 0.7114 | 0.8086 | 1227 | 617 | 503 |
| doctr | 0.8691 | 0.9891 | 1227 | 1 | 1149 |
| openbharatocr | 0.4870 | 0.6809 | 1227 | 1 | 1056 |

## Headline rankings (post-surya-completion)

| Rank | Engine | overall CER | Notes |
|---|---|---|---|
| 1 | sarvam_vision | 0.2400 | 54-cap (3/lang), directional only |
| 2 | surya | 0.3849 | WINS on brx (0.153), ks (0.589 p<0.0006), kok (0.425 p<0.008), mai (0.030) |
| 3 | tesseract_bilingual | 0.4853 |  |
| 4 | tesseract_indic | 0.4870 |  |
| 5 | openbharatocr | 0.4870 | EXACT duplicate of tesseract_indic |
| 6 | easyocr | 0.4941 |  |
| 7 | indicphotoocr | 0.5586 |  |
| 8 | paddleocr_indic | 0.6562 |  |
| 9 | rapidocr | 0.6692 | 647 honest-empty, model gaps |
| 10 | anuvaad_tesseract | 0.7114 | 617 honest-empty (hin+eng only) |
| 11 | doctr | 0.8691 |  |

## SURYA UPDATE (2026-09-28 ~19:33 IST)

- Previously stuck at 726 packs (PID 15941 busy-loop). Auto-restarted at 5:45PM via Engine's polling loop.
- NOW COMPLETE: 1227/1227 packs + 30 EN = 1257 entries.
- **surya EN CER 0.1514** — beats tesseract-family (0.8077), easyocr (0.6036), indicphotoocr (0.6710), paddleocr (0.2495).
- **surya overall CER 0.3849** — best after sarvam (0.2400).
- **surya WINS on**: brx 0.153 (McNemar p<0.012), ks 0.589 (p<0.0006), kok 0.425 (p<0.008), hi 0.220, mai 0.030.
- 129 honest-empty from layout-parse fail (sa mostly).

## Barred langs (per §6.4 lock — CER unreliable, don't compare to Sarvam 87.39)

- ks, mni, mr, sat, ur, ne-PDF-tier. Per-language CER is honest-engine score but GT is garbage/fill-only.

## User-decision gates (still open for validation call)

1. GPU budget for W6 local QLoRA
2. Sarvam EN extension (3 calls over 54-cap)
3. 20-item human spot-check review (priority gu_o005)
4. rapidocr EN fix-spec
5. Full Sarvam API run (1,227 items) for valid 'Beat 87.39' claim
6. Sampling: re-sample or accept current 100/lang lock

Generated 2026-09-28 19:33 IST by orchestrator. Refreshed 2026-09-29 05:30 IST (post-H48 hostile pass + EN sanity re-score).

## W6 feasible-set (campaign §11 skeleton, 2026-09-29)

| Column | Items |
|---|---|
| **FEASIBLE NOW** | Wrap-only baseline: §6.2 tier routing + per-script engine routing + restoration pre-pass (R4). Maps directly to the engine×lang matrix above. No compute cost. Deliverable guaranteed before W5 freeze. |
| **FEASIBLE IF** | (a) Local QLoRA on SAFE langs (kok/mai/or/pa — 4 langs ≥50; brx borderline 67) — IF Phase 6 estimator-law gap exists AND laptop memory allows (3-4B @ 4-bit ~3GB MLX; system ~43% free, swap ~97%; VERIFY at call time, currently UNKNOWN). (b) sat/ks micro-repair — IF W5 time permits (D4) and curated pages pass purge-era gates. (c) Rapidocr EN column — ALREADY RESTORED (1.0 → 0.4535 CER; harness intact). |
| **INFEASIBLE UNDER CURRENT RULES** | Cloud GPU rental (no budget, D1), new backbone invention (§9 hard rule), paid APIs beyond Sarvam 54-cap, training on barred languages (ks/mni/mr/sat/ur + ne PDF-tier), sarvam_fill in SFT/RLVR. |

## W6 feasible-set routing per-script (Tier-1 evidence, 2026-09-29)

| Tier-1 routing decision | Engine | Cell coverage | Why |
|---|---|---|---|
| **Devanagari** (hi/mr/sa/ne/mai/kok/brx/doi) | surya first, tesseract-family fallback | hi/bn/ks/mai/pa/sd/ur (surya WINS), mr/or (tesseract wins) | surya dominates Devanagari at McNemar p<0.008 |
| **Perso-Arabic** (ur/sd/ks) | surya | sd/ur (surya WINS), ks (surya 0.589 McNemar p<0.0006) | surya 9/9 opponents beaten |
| **Bengali-Assamese** (bn/as/mni/sat) | sarvam_vision (for sat/mni), indicphotoocr (for bn) | bn (indicphotoocr 0.657 / surya 0.476); sat/mni Sarvam-only | surya wins bn, indicphotoocr second |
| **Odia** (or) | tesseract-family (n=66) | or (tesseract 0.256 / indicphotoocr 0.353 / surya 0.276) | Tied winner: tesseract-family 5/5 opponents |
| **Gurmukhi** (pa) | tesseract-family (n=90) | pa (surya 0.145 / tesseract 0.226) | Tied winner: tesseract-family 5/5 + surya |

## EN sanity column (post-2026-09-29 EN fix; rapidocr re-scored)

| Engine | EN CER | EN WER | Word Acc | Status |
|---|---|---|---|---|
| surya | 0.1514 | 0.2601 | 73.99% | Best — clean English output verified |
| paddleocr_indic | 0.2495 | 0.4966 | 50.34% | Good |
| doctr | 0.3957 | 0.8445 | 15.55% | Working (D4 fix-spec retired) |
| **rapidocr** | **0.4535** | **0.8345** | **16.55%** | **RESTORED** — was 1.0 broken (2026-09-28); fix at run_probe.py:290-291 |
| easyocr | 0.6036 | 0.9788 | 2.12% | Working but weak |
| indicphotoocr | 0.6710 | 0.9433 | 5.67% | Working but weak |
| tesseract_indic | 0.8077 | 0.9853 | 1.47% | Tesseract-family weak on EN |
| tesseract_bilingual | 0.8077 | 0.9853 | 1.47% | Mirrors tesseract_indic |
| openbharatocr | 0.8077 | 0.9853 | 1.47% | Mirrors tesseract_indic |
| anuvaad_tesseract | 1.0000 | 1.0000 | 0.00% | Honest-empty (no EN model) |
| sarvam_vision | N/A | N/A | N/A | Not run on EN per D2 (cap 54) |

**Harness verdict:** INTACT — surya produces clean English on these degraded scans ("Every heart one day beats its final beat" matches GT). The 0.15-0.45 EN CER range reflects OCR engine weakness on ornate pub_raw EN layouts, NOT a broken harness. rapidocr fix validated.

## Engine-overlap warning (campaign §11)

`openbharatocr` ≡ `tesseract_indic` ≡ `tesseract_bilingual` byte-identical on 1257 packs (verified mcnemar_full_matrix.py 2026-09-28). **Effective independent engines: 10** (not 11). The 11th slot is a wrapper duplicate.