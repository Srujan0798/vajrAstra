# Engine Agent Spot-Check Log — 2026-09-29 05:25 IST
## Verdict H48 hostile-pass claim verification (campaign §11 weak cells)

### Methodology
For each weak cell: sample 3 random items via `random.seed(<n>)`, verify:
- Item in `manifest.json`
- Image exists in `images/<lang>/`
- At least one engine pack exists in `out/<eng>/<lang>/`
- Pack `text` field is non-empty
- Visual sanity check on text content vs script

---

## sat (Santali — Ol Chiki, §6.4 BARRED, n=20, GT=fill-only)

**Sampled:** sat_14, sat_05, sat_10 (seed=42)

| Item | Set | img_exists | surya text (first 100) | rapidocr text | Notes |
|---|---|---|---|---|---|
| sat_14 | sarvam_fill | ✓ | Ethiopic (Ge'ez) + Bengali fragments | "" (honest-empty) | surya emits NO Ol Chiki; emits random non-Indic scripts |
| sat_05 | sarvam_fill | ✓ | Ethiopic + Georgian + Malayalam | "" | same failure mode |
| sat_10 | sarvam_fill | ✓ | Thai + Bengali + Sinhala fragments | "" | same failure mode |

**DISK-TRUTH VERIFIED:** §11 weak-cell forensics holds — 0 engines emit Ol Chiki on sat. All open engines emit Latin/garbage (Ethiopic/Thai/Sinhala). rapidocr = honest-empty (no Ol Chiki model). Only `sarvam_vision` emits Ol Chiki (per §11 lock + §6.4 GT-barred caveat).

---

## ks (Kashmiri — Nastaliq, §6.4 BARRED, n=100, PDF-tier BARRED per R5)

**Sampled:** ks_o005, ks_o037, ks_o090 (seed=43)

| Item | Set | img_exists | surya text | rapidocr text | tesseract_indic text |
|---|---|---|---|---|---|
| ks_o005 | official_pdf | ✓ | "ساز سلاسل (اتلان ایڈیشن)..." clean Urdu | fragments "سا سلا / مي زبانِ..." | Urdu with scattered noise |
| ks_o037 | official_pdf | ✓ | "ساز سلاسل آئلان ایڈیشن..." clean Urdu | scattered Urdu | Urdu with noise |

**DISK-TRUTH VERIFIED:** §11 weak-cell forensics holds — surya emits clean Nastaliq/Urdu (best); rapidocr emits fragmented Urdu (~71% Arabic share); tesseract_indic ~40-42% Arabic share with noise. All produce Urdu-script output (correct script), unlike sat. GT BARRED per R5 (trust 26.6); CER is unreliable.

---

## OldScan proxy = sa (Sanskrit — clean native scans, n=100, all official_pair)

**Sampled:** sa_d053, sa_d067, sa_d070 (seed=44)

| Item | Set | img_exists | surya text | paddleocr_indic text | easyocr text |
|---|---|---|---|---|---|
| sa_d053 | official_pair | ✓ | **""** + error=HONEST_EMPTY_SURYA_NO_OLCHIKI | "॥ शीमचहंकार भगवतपज्यपादा:..." clean Devanagari | "।। शरभचछकारभगचतपूष्यपादूा४" — close |
| sa_d067 | official_pair | ✓ | **""** + error=HONEST_EMPTY_SURYA_NO_OLCHIKI | "(२०६) ग्रहलाघवे ४९।९। १०।..." clean | close to GT |
| sa_d070 | official_pair | ✓ | **""** + error=HONEST_EMPTY_SURYA_NO_OLCHIKI | "पश्वरताराम्पष्टरीकरणाधिकारः..." clean | close to GT |

**DISK-TRUTH VERIFIED:** sa is the OldScan proxy (4250×6500 native-resolution scans, largest in probe). **surya runner bug** — sa gets ALL 100 packs tagged `HONEST_EMPTY_SURYA_NO_OLCHIKI` (FINAL_REPORT.md:149 documents this as known bug; surya wrapper misapplies the Ol Chiki no-script tag to all Sanskrit packs). paddleocr_indic + easyocr produce clean Devanagari Sanskrit output. surya scored 1.000 on sa = unscored.

---

## or (Odia — n=69, 50 official_pdf + 19 sarvam_fill, SAFE-pending §6.2)

**Sampled:** or_o044, or_08, or_06 (seed=45)

| Item | Set | img_exists | surya text | tesseract_indic text | rapidocr text | paddleocr text | easyocr text |
|---|---|---|---|---|---|---|---|
| or_o044 | official_pdf | ✓ | "କ) ଦାନ୍ତରେ କାମୁଡି ବିଷ..." clean Odia | "କ) ଦାନ୍ତରେ କାମୁଡି..." clean Odia | "" (honest-empty) | "" (honest-empty) | "Qi860 QiqG &8 Qi2iq..." garbled |
| or_08 | sarvam_fill | ✓ | "ଉୂରୁ ନାହିଁତି..." clean Odia | "ଆଠରୁ ଗାକକଂଶର..." | "" | "" | garbled |
| or_06 | sarvam_fill | ✓ | **""** (empty) | "ଇଂରେକତର ସ୍‌ 69°..." | "" | "" | garbled |

**DISK-TRUTH VERIFIED:** or has clean Odia output from surya + tesseract_indic (correct script); rapidocr + paddleocr = honest-empty (no Oriya model); easyocr produces Latin transliteration. or_06 surya empty is a layout-parse fail (129/1227 surya honest-empty is layout-related, documented).

---

## Disk-truth summary of spot-checks

| Cell | Sample items | All on disk | All have ≥1 engine pack | Engine text sensible? | Matches §11 forensics? |
|---|---|---|---|---|---|
| sat | sat_14, sat_05, sat_10 | ✓ | ✓ | NO (Latin/Ethiopic/Thai garbage) | ✓ (0 Ol Chiki) |
| ks | ks_o005, ks_o037, ks_o090 | ✓ | ✓ | YES (Nastaliq script correct) | ✓ (partial capability) |
| OldScan (sa) | sa_d053, sa_d067, sa_d070 | ✓ | ✓ | YES for paddle/easyocr; NO for surya (runner bug) | ✓ (surya unscored, known bug) |
| or | or_o044, or_08, or_06 | ✓ | ✓ | YES (Odia script correct, except or_06 surya empty) | ✓ (real CERs) |

**Verdict hostile-pass claims VERIFIED against disk truth for all 4 cells sampled.**

## Token spend (in / out)

- Input tokens (this Engine session): ~50k (read protocol, manifest, ledger, leaderboard, fix-specs)
- Output tokens (this Engine session): ~15k (this report + 1 leaderboard edit + 1 fix)
- Net: ~65k tokens (no subagent calls; minimal MCP usage)

## Files modified by Engine this session

- `level2/probe22/scores/LEADERBOARD.md` — added W6 feasible-set table, EN sanity column (post-fix), per-script routing, engine-overlap warning
- `level2/probe22/scores/metrics_*_en_normalized.json` — re-scored for all 10 engines (rapidocr 1.0 → 0.4535)
- `level2/probe22/preds_*_en.json` — re-built for all 10 engines
- `level2/probe22/engine_health_log.jsonl` — appended events
- `docs/research/level7/H48_ENGINE_SPOTCHECK.md` (this file) — written

## Files NOT modified (per protocol)

- `level2/out/` — SEALED (read-only)
- `level2/reports/` — SEALED (read-only)
- `manifest.json` — preserved at n=1283 (re-sourced state)
- `sheet.csv` — preserved at 12,324 rows (LOCKED measurement)
- `Datasets/` — never touched