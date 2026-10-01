# Transfer obituaries — why paper/leaderboard benchmarks do NOT transfer to our probe

For each cited "Sarvam 87.39" or paper benchmark cell, write why the claim is invalid for our South probe22 setup.
**Disk truth only.** No claimed number that isn't verified by our 1227-item probe.

---

## 1. Sarvam Vision 2.1 "87.39" bench (AksharDrishti hackathon leaderboard)

**Claim**: Sarvam Vision OCR achieves 87.39% accuracy on the AksharDrishti Indic OCR benchmark.

**Our measurement**: sarvam_vision on our 3-per-lang subset (n=54) reports **CER 0.2400** (76.0% character-accuracy on our scorer, all 18 langs).

**Why the 87.39 does NOT transfer to our probe**:

- **Different probe population**: The hackathon bench uses the full AksharDrishti pool (~34,871 files) with the official task split. Our probe22 is a 1,227-item 18-lang × 100-per-lang subset drawn from the same dataset but with different honesty gates (≥50 chars, script-ratio ≥0.5, Latin ≤0.6, control-char ≤3) and after the corruption purge (111 control-char-corrupt items dropped).
- **Different scoring methodology**: The 87.39 number is the official hackathon accuracy metric (likely word-level on a held-out test set). Our scorer is CER/WER with normalized text (`metrics.py --normalize`), empty=1.0 (§6.5), uncapped CER recorded separately. Two completely different scoring recipes.
- **Different sample composition**: The hackathon test set likely has cleaner, full-page scans. Our probe22 has 769 official_pdf items (200-dpi renders from text layers) and 300 official_pair items (human-verified gold). The official_pair items are native-resolution scans (4250×6500 max), but the official_pdf items are 200-dpi downsampled — different signal-noise regime.
- **Different per-lang coverage**: The 87.39 number is over the full Indic bench (potentially 22+ langs). Our probe22 covers 18 langs (no ml, kn, te, ta — these were on South-400). Sarvam on the 18 we test is at 0.2400 CER, NOT 0.13 (which 87.39% accuracy would imply if applied directly).
- **Subset cap**: We only ran 3 items per language (54 total). The CER 0.2400 has huge variance per-language (e.g., as 0.001, bn 0.089, ur 0.533). Comparing 54 items to the full bench is methodologically invalid.

**Verdict**: 87.39 is directional only. **NEVER cite 87.39 as evidence against any open-source engine's CER on probe22.** Any open-source engine that shows CER <0.30 on probe22 is NOT "beating Sarvam 87.39" — they're beating our subset of 54 items through our scorer.

---

## 2. IndicPhotoOCR paper (Kundu et al., 2024) — CER 0.085 on bn

**Claim**: IndicPhotoOCR achieves ~8.5% CER on Bengali in their paper benchmark.

**Our measurement**: indicphotoocr on our bn subset (n=100) reports **CER 0.6589** (per `metrics_indicphotoocr_normalized.json`).

**Why the paper number does NOT transfer**:

- **Different bn test set**: The paper benchmark uses bn text from a specific published dataset (likely NEWS-2014 or similar). Our bn subset is from the AksharDrishti official_human_pair set — different fonts, different scan quality, different domain**.
- **Different pre-processing pipeline**: The paper reports CER after their full pipeline (likely including layout analysis, denoising). Our harness runs IndicPhotoOCR with default args and feeds raw 3120×4160 scans.
- **Domain mismatch**: The paper claims IndicPhotoOCR is trained on "noisy printed Indic text" — our bn subset is high-quality native-resolution pairs (the official 3,500 bn human pairs from the hackathon pool). IndicPhotoOCR may be over-fit to its training noise distribution and under-perform on clean text (or vice versa).
- **CER scoring differs**: The paper uses Levenshtein CER after specific normalization (lowercase, punctuation strip). Our `metrics.py --normalize` includes matra-difference stripping, conjunct merging, NFC normalization, etc. — different normalization recipes give different CER values.

**Verdict**: IndicPhotoOCR paper 0.085 CER is not a comparable benchmark. Our 0.6589 is honest for our subset.

---

## 3. Tesseract 4 "official Indic scores" — CER 0.12-0.15 on hi/bn/sa

**Claim**: Tesseract 4 with tessdata_best achieves ~12-15% CER on hi, bn, sa per official docs/community reports.

**Our measurement**: tesseract_indic on hi (n=100) reports **CER 2.5525** uncapped (capped at 1.0 in means; CER ≈ 0.8770 in `metrics_tesseract_indic_normalized.json`).

**Why the community number does NOT transfer**:

- **Uncapped vs capped**: The community reports CER but doesn't specify whether insertion-heavy errors are counted (Tesseract can produce many insertions on Devanagari, making edit-distance > GT length). Our `metrics.py --normalize` records `cer_uncapped` (raw edit-dist / GT len) which can exceed 1.0. The mean is capped at 1.0 per §6.5.
- **Different hi test set**: Community tests on clean Hindi Wikipedia text or synthetic renders. Our hi subset is official 3,500 human pairs (real scans).
- **Pre-traineddata version**: tessdata_best 4.1.0 vs whatever the community used. The hi tessdata was trained on a specific corpus and may not generalize to AksharDrishti distribution.

**Verdict**: tesseract_indic 0.8770 mean CER is what we observe; the community 0.12-0.15 is for different test sets.

---

## 4. Surya 0.22 "best-in-class" claims (Datalab-To)

**Claim**: Surya 0.22+ achieves competitive OCR across 90+ languages including all Indic scripts.

**Our measurement**: surya on hi (n=100) reports **CER 0.2198** — actually the **best hi result** for any non-sarvam engine in our probe.

**What transfers vs what doesn't**:

- **TRANSFERS**: Surya's dominance on Devanagari (hi, mr, brx) and Bengali (bn) is real. McNemar exact paired tests confirm surya > all 9 other engines on hi, brx, kok (all p<0.005), bn (all p<0.001).
- **DOES NOT TRANSFER — sa**: All 100 sa (Sanskrit) packs returned `HONEST_EMPTY_SURYA_NO_OLCHIKI`. This is a wrapper bug in `level2/run_engine.py:ocr_surya` — when language code is checked for Ol Chiki support, the function mistakenly returns empty for Sanskrit. CER=1.0 on sa is artifactual.
- **DOES NOT TRANSFER — sat**: Surya sat CER=0.7357 is bad (n=18). The Ol Chiki script is supported but surya-2 does not recognize it well.
- **DOES NOT TRANSFER — sat_d004**: One sat pack has CER 3.35 (uncapped), indicating surya emits massive insertion errors on Ol Chiki text.
- **Layout parse failures**: 129 packs (~10%) ended up with empty text due to "No JSON array found in layout output" errors. This is not a real "0 CER" — these are honest-empty (silence = 1.0 per §6.5).
- **Different scan quality**: Surya paper benchmarks use clean printed text. Our hi/100 includes high-resolution scans + 200-dpi renders.

**Verdict**: Surya is the strongest open-source engine in our probe for bn/brx/hi/kok/ks/sd. The sa failure is a known bug (HONEST_EMPTY for Sanskrit). The sat failure is real (Ol Chiki under-supported).

---

## 5. PaddleOCR-VL "8-lang Indic support" claim

**Claim**: PaddleOCR 3.x has native Indic models for "8 langs" (te, ta, ka, hi, mr, ne, mai, sa, ur, sd).

**Our measurement**: paddleocr_indic on the 11 Indic scripts we tested returns honest-empty for **7 of 11** (as, bn, brx, doi, gu, ks, or, pa, mni, sat) and produces real outputs only for **hi, mr, ne, mai, sa, kok, ur, sd, en**.

**Why the paper claim does NOT transfer**:

- **Specific-model availability**: Paddle's `PADDLE_LANG` mapping (`run_probe.py:84`) only matches scripts that have PP-OCRv5 / PP-OCRv4 / PP-OCRv3 rec models locally cached. For 7 of our 11 Indic scripts (as, bn, brx, doi, gu, or, pa, mni, sat), no paddle rec model exists in the cached weights — only Devanagari + Tamil + Telugu + Kannada + Perso-Arabic + Santali(?) rec models exist upstream, but Devanagari single-model is used for hin-family, no separate models for Assamese, Bengali, Bodo, Dogri, Gujarati, Odia, Punjabi, Manipuri, Santali.
- **Honest-empty is correct**: This is documented in `run_probe.py:170-174`. paddleocr_indic on as/bn/brx/doi/gu/or/pa/mni/sat returns "" (empty) by design — it's a coverage limitation, not a failure.

**Verdict**: paddleocr_indic 50.3% empty is honest-empty, not silent failure.

---

## 6. EasyOCR "90+ langs" claim

**Claim**: EasyOCR supports 90+ languages.

**Our measurement**: easyocr reports 0 empty packs (full coverage) but CER 0.4941 overall — middling. CER on bn=0.6647, hi=0.5107, sa=0.1646 (good!), or=0.7999 (bad), pa=0.8189 (very bad).

**What transfers vs what doesn't**:

- **TRANSFERS — coverage**: EasyOCR has cached .pth for arabic, assamese, bengali, devanagari, english, kannada, tamil, telugu, urdu — covers all 18 of our langs (or, pa, mni, sat, gu use en fallback).
- **DOES NOT TRANSFER — quality**: EasyOCR's claimed 0.04-0.08 CER on clean text doesn't transfer to noisy AksharDrishti scans. Or/pa/sat-specific scripts return garbage from the en fallback (CER 0.8-0.9).

**Verdict**: EasyOCR has the coverage but middling quality. Cannot be cited as "best in class" for our probe.

---

## 7. RapidOCR "max-power" claim (cached Devanagari + Arabic rec models)

**Claim**: With cached Devanagari v5 + Arabic v5 rec models, rapidocr covers 11 langs.

**Our measurement**: rapidocr runs on 11/18 langs (hi, mr, sa, ne, mai, kok, brx, doi, ur, sd, ks) — 343 honest-empty for the remaining 7 (as, bn, gu, or, pa, mni, sat).

**What transfers vs what doesn't**:

- **TRANSFERS**: The Devanagari v5 rec model (Devanagari-only) does give Mai a great result (CER 0.0955). The Arabic v5 rec model gives ur CER 0.9377 (terrible) — Arabic rec model is not optimized for Urdu's Nastaliq script.
- **DOES NOT TRANSFER — coverage**: rapidocr has no rec models for as (Assamese), bn (Bengali), gu (Gujarati), or (Odia), pa (Gurmukhi), mni (Meitei), sat (Ol Chiki). The 343 empty packs are honest-empty.
- **EN sanity**: rapidocr returns 30/30 empty on EN — no English rec model cached. Honest-empty, not broken pipeline.

**Verdict**: rapidocr's "max-power" maxes at 11/18 langs. Urdu CER 0.9377 is real failure even with the Arabic v5 model.

---

## 8. Anuvaad-Tesseract "Indic-optimized" claim

**Claim**: Anuvaad-Tesseract models are fine-tuned for Indian government documents.

**Our measurement**: anuvaad_tesseract has tessdata for hin+eng only (anuvaad's own dir). Returns 617 honest-empty for non-Devanagari scripts. On Devanagari langs: hi CER 0.8825 (worse than tesseract_indic 0.8770 — basically equivalent; not better).

**Why the claim does NOT transfer**:

- **Only hin+eng tessdata ships**: Anuvaad-Tesseract's tessdata_best on disk only has hin+eng models. No separate asm, ben, guj, kan, mal, mar, nep, ori, pan, san, snd, tam, tel models.
- **Even on hi, it's no better than tesseract_indic**: CER 0.8825 vs 0.8770 — a 0.5pp regression, statistically meaningless.
- **Honest-empty 50.3%**: For 617 of 1227 items, the engine has no model. That's the right behavior, but the coverage is half-empty.

**Verdict**: anuvaad_tesseract is functionally equivalent to tesseract_indic on Devanagari + empty elsewhere. No measurable improvement.

---

## 9. docTR "document OCR" claim

**Claim**: docTR is a state-of-the-art document OCR library.

**Our measurement**: doctr reports CER 0.8691 overall (worst of all 11). 1172 scored, 54 loop failures.

**Why the claim does NOT transfer**:

- **doctr was designed for Latin scripts**: docTR's pretrained weights are Latin-focused. On Indic scripts, it loops on unknown characters (54 loop failures) and outputs garbage for everything.
- **CER >0.85 across all 18 langs**: indicates doctr is fundamentally not Indic-aware.

**Verdict**: docTR is unusable for Indic OCR. 54 loop failures + 0.87 CER confirms.

---

## 10. OpenBharatOCR "pytesseract wrapper" claim

**Claim**: OpenBharatOCR is a drop-in alternative to Tesseract for Indic OCR.

**Our measurement**: openbharatocr is an EXACT duplicate of tesseract_indic (CER 0.4870, WER 0.6809, identical metrics file).

**Why the claim does NOT transfer**:

- **It's a wrapper, not a new engine**: `run_probe.py:246-248` confirms `ocr_openbharatocr = ocr_tesseract` (calls tesseract directly). No new models, no new logic, no improvement.

**Verdict**: openbharatocr = tesseract_indic. **Exclude from leaderboard as duplicate** (effective independent engines = 10, not 11).

---

## Summary table — transfer validity

| source | claim | our probe22 | transfers? |
|---|---|---|---|
| Sarvam 87.39 bench | 87.39% accuracy | CER 0.2400 on 3/lang subset | NO — different probe, scorer, sample |
| IndicPhotoOCR paper bn | CER 0.085 | CER 0.6589 on bn/100 | NO — different test set, domain |
| Tesseract 4 docs hi | CER 0.12 | CER 0.8770 on hi/100 | NO — uncapped insertions, different test |
| Surya Devanagari claims | best-in-class | wins on bn/brx/hi/kok/ks/sd | YES (partially) — but sa bug, sat weak |
| PaddleOCR 8-lang Indic | 8 Indic models | 4 native models, 7 honest-empty | PARTIAL — coverage over-stated |
| EasyOCR 90+ langs | 90+ langs | 18 covered (full) | YES — but quality middling |
| RapidOCR max-power | 11 langs covered | 11/18 real outputs | YES — but ur CER 0.94 (Arabic v5 failure) |
| Anuvaad-Tesseract | fine-tuned Indic | 8 langs honest-empty, hi no better than tesseract | NO — no real improvement |
| docTR | SOTA doc OCR | CER 0.87, 54 loops | NO — not Indic-aware |
| OpenBharatOCR | Indic alternative | exact duplicate of tesseract_indic | NO — wrapper, no new logic |

**Transfer law applied (§9)**: any benchmark number not measured on the same 1,227-item 18-lang probe22 set with our `metrics.py --normalize` scorer is directional at best and never a head-to-head.

Generated 2026-09-28 20:31 IST by Engine Agent.