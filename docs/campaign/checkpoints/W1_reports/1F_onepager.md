# 1F — ONE-PAGER (the artefact the three evaluators were to critique)

Built 2026-09-29 by the Sonnet lead from the verified Wave-1 outputs (1A audit, 1B benchmark, 1C playbook, 1D competitor intel, 1E refutation). Every number carries its n and metric. No adjectives without numbers.

## 1. Goal

Beat **Sarvam Vision 2.1** on Indic OCR across **22 Indian languages**, honestly, using **hybrid integration of existing open models** (no new backbone), in about **5 development days**, on **one Apple M2 Max**, with **no paid API budget left** (the 57-call Sarvam cap is spent).

## 2. Current state, with n

- **probe22**: 1,283 manifest items / 18 languages; **1,227 scored** by 10 local engines (11 model strings; `tesseract_bilingual` ≡ `tesseract_indic` ≡ `openbharatocr` are byte-identical) = 12,324 `sheet.csv` rows. **Sarvam ran on 54 of them** (3 per language, 18 languages).
- **South**: 400 labelled pages (ta/te/kn/ml × 100), but only **126 carry a CER** (219 nulled `gt_thin` GT<200 chars, 55 nulled legacy mojibake).
- **22-language table**: **13 of 22 languages have scored n ≥ 50**; **1 language (ml) is below the lead's 5–10 floor** at n=5; 8 more sit at n 19–37 and carry no winner claim (D4).
- **Best local engine, n≥50**: surya 9 languages, tesseract-family 2, easyocr 1 — of the 12 languages where n≥50.
- **Sarvam comparison (n=54, 3/lang — DIRECTIONAL, not a win)**: surya's mean CER is lower in **10 of 18** languages; item-level **Sarvam better 28, surya better 21, tie 5**. Sarvam mean CER **0.2640**; best local **0.2956**; surya overall **0.3944**. McNemar p<0.05 vs every testable opponent in only **5** languages (bn, brx, hi, kok, ks); **ur is 0 of 9**.
- **What we cannot claim**: our per-language CER is not comparable to Sarvam's headline **87.39**, which is a **word-accuracy-style macro-average over 22 languages with English excluded**, on a benchmark Sarvam built and scored itself. Verified NO — different metric, different items, different normalisation.

## 3. Baseline architecture (the lead's PPT, 4 stages)

OpenCV preprocess → **DocLayout-YOLO (YOLOv10)** layout → **parallel recognition SFT**: TrOCR (ViT/BEiT+RoBERTa) + Qwen-VL + PaddleOCR-VL 1.6, seq2seq SFT with an **akshara-boundary auxiliary loss** → **SCST/RL on CER** → post-SFT IndicBERT-style noisy→JSON head → SimPO/DPO on ranked JSON. Eval against Sarvam, IndicDLP, Indic Vision Bench, no fine-tune on test. Source: `docs/architecture/PPT_SPEC.md`.

## 4. Two options on the table

| | **Option A — wrap-only** | **Option D — wrap + router + restoration + subsidy** |
|---|---|---|
| Ships | per-script routing table over the 10 engines we already run; R4 restoration pre-pass; Sarvam API subsidy for sat/mni | same wrap, plus an explicit script-router, R4 restoration, Sarvam subsidy for sat/mni, and R4 restoration of barred cells |
| Cost | $0 | $0–30 (the $12 API line is **unsourced**) |
| Cells moved | the 7 languages whose best-engine CER is in the 0.10–0.40 band | same + the barred/low-n cells |
| Risk | no accuracy gain; a routing table is a presentation win | spends a day on a router whose measured routing gain was **−0.0351 CER (negative)** |
| Evidence | 7 of 12 languages n≥50 in the 0.10–0.40 band; Sarvam's weak cells are Kashmiri 54.82, Santali 53.91, OldScan 55.3 | the restoration pre-pass is borrowed from PreP-OCR, measured only on **English/French/Spanish** historical pages — no non-Latin measurement |
| **Conflict** | recommended by Miss, and by `docs/research/level7/W5_STRATEGY_OPTIONS.md` | recommended by Verdict in `docs/architecture/W5_STRATEGY_OPTIONS.md` (5 ranked options, ranks D first) |

**Backbone question (unresolved conflict, boss decision U4):** the feed locks **Qwen2.5-VL-3B @4-bit** as PRIMARY (`W6_QLORA_SPEC.md:53`); GLM-OCR 0.9B is ALTERNATE 2. **No candidate weights are on disk** (HF cache has 7 entries, none qwen/glm). GLM-OCR is **absent from the OmniDocBench v1.6 table** the packet cites it in.

## 5. Edge thesis

**Zero of four candidates survived adversarial refutation** (3 lenses × 4 candidates, survival = fewer than 2 REFUTED). What did survive is a **coverage** fact, not an accuracy edge: **0 of 200 local-engine predictions on Santali contain a single Ol Chiki codepoint**, and `level2/probe22/tessdata/` has **none of `mni`, `sat`, `kan`, `mal`, `tam`, `tel`**. Our two dead languages have **one font each** on this machine. The likely fix is one ~2–4 MB traineddata file — a **download approval**, not an idea.

The one concrete engineering item with a measured payoff: **the fusion ceiling is real but 67% of it is the `sa` cell, where surya emits 100% empty predictions** — a bug, not a fusion problem. Ex-`sa` the oracle gap is 0.0332, not 0.095.

## 6. Known risks

1. **The evidence sheet cannot regenerate our own numbers.** `sheet.csv`'s stored `CER` column reproduces from its own `gt`/`prediction` via the repo's `metrics.py` on only **100 of 400** sampled rows (66/400 exact). All headline numbers are computed *from* that column, so they are internally consistent, but a reviewer who re-runs the scorer gets different numbers. Fixing it means regenerating a LOCKED file = boss decision U5.
2. **South scored n is tiny**: 126 of 400; kn/ml at 4–6 pages on the script partition (25 and 5 on the lang-tag partition — the two partitions disagree, and both are reported).
3. **Low-n tail**: 8 languages at n 19–37, no winner claim allowed.
4. **No Santali / Meetei Mayek local support**; Urdu/Kashmiri Nastaliq cursive and untested.
5. **Normalisation is NOT a problem for us** — 0 exact-match flips across 12,324 rows. (This kills one whole proposed edge; do not spend 5 days there.)
6. **W6 training is PAUSED** and an untracked `src/` QLoRA/GRPO tree (~1,195 lines, written 19:51–20:07 IST today) exists without authorisation (boss decision U3).
7. **Dates are unsettled** (U1: "after next Wednesday" is ambiguous; U2: the submission deadline is contradicted across 43 files).

## 7. The 5 questions we most want criticised

1. Given that **zero edge theses survived**, is wrapping 10 existing engines the right play at all — or is the honest answer "we cannot beat Sarvam honestly in 5 days, and the plan should say that"?
2. **87.39 is not comparable to our CER.** Should we stop trying to compare, and instead publish a 22-language table on our own terms and let the comparison be made by a third party?
3. Our Sarvam comparison is **n=3 per language**. Is reporting it at all a net positive, or does any framing of it become a cross-examination trap?
4. Option A vs Option D — and is a **2-hour change** (report median CER + abstain rate instead of mean, because 43.7%–50.3% of some engines' predictions are empty) worth more than either option?
5. The `sheet.csv` CER column is not re-derivable. Does that disqualify the artefact as external evidence, and what is the cheapest way to make our numbers checkable before a CEO cross-questions them?
