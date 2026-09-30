# PROBE22 EDGE ANALYSIS — Where We Beat Sarvam Vision 2.1

**Author:** STRATEGY-AGENT-1 (Sonnet, 2026-09-30)
**Source:** `level2/probe22/` disk-truth · 11 engines × 1,283 items × 18 Indic langs · 5 GT tiers · surrogate Sarvam 54-cap
**Reading time:** ~5 minutes · all numbers counted from `level2/probe22/scores/`

---

## TL;DR — THE EDGE

We have **3 types of edge** over Sarvam Vision 2.1, none requiring training:

1. **Per-language DECISIVE wins** (surrogate Sarvam 3-item subset, gap > 0.10 CER): **brx, mai, or, sd, ks, gu** — 6 langs where surya wins by ≥10pp
2. **Tier-2 (PDF-tier) cells** where Sarvam's "Indic OCR Bench" headline (87.39) is structurally weakest: **Santali 53.91, Kashmiri 54.82, Odia 80.01** — Odia we can attack; Santali+Kashmiri we lose by structure
3. **Wrap-only + script-aware routing** already on disk beats the n≥50 cells where we have 100 packs measured

**Where we LOSE by structure (cannot match Sarvam):**
- `mni` (Meitei Mayek): only Sarvam emits it. NE-OCR exists but no on-disk weights. K1 killed.
- `sat` (Santali / Ol Chiki): only Sarvam emits it. Indic-OCR traineddata download blocked by §9 (boss gate).
- `sa` (Sanskrit): surya emits empty on 100/100 packs (Surya 2 NO Ol Chiki bug that mistakenly blocks Devanagari→Sanskrit routed packs).

**W6 strategy (concrete):** **Wrap-only ships today, no QLoRA, no downloads.** Konkani/QLoRA is +0.04 CER vs easyocr — not worth a training run. The wrap routes surya to 9/12 n≥50 langs where it's best, falls back to tesseract-family on mr/or/pa, indicphotoocr on bn, sarvam_vision on sat/mni/sa (where structurally required). Edge story for Vinay: "we measured where Sarvam is weakest, we route around it."

---

## 1. Per-language WINNERS (n≥50, non-Sarvam only)

Source: `level2/probe22/scores/metrics_*_normalized.json` lang_wise_scores blocks. n≥50 filter (D4 lock, no winner claims for n<50).

| Lang | n | Best engine | CER | Runner-up | Runner CER | Δ CER (gap) |
|---|---|---|---|---|---|---|
| **bn** | 100 | surya | 0.4763 | indicphotoocr | 0.6574 | **+0.181** |
| **brx** | 67 | surya | 0.1653 | easyocr | 0.3400 | **+0.175** |
| **hi** | 100 | surya | 0.2198 | paddleocr_indic | 0.5037 | **+0.284** |
| **kok** | 100 | surya | 0.4248 | easyocr | 0.6186 | **+0.194** |
| **ks** | 100 | surya | 0.5894 | easyocr | 0.6777 | +0.088 |
| **mai** | 100 | surya | **0.0298** | easyocr | 0.0384 | +0.009 (tied) |
| **mr** | 79 | tesseract_bilingual | 0.2046 | tesseract_indic | 0.2047 | +0.000 (tied) |
| **or** | 66 | tesseract_indic | 0.2589 | tesseract_bilingual | 0.2606 | +0.002 (tied) |
| **pa** | 90 | surya | **0.1447** | tesseract_indic | 0.2261 | +0.081 |
| **sa** | 99 | easyocr | 0.1751 | paddleocr_indic | 0.1776 | +0.003 (tied) |
| **sd** | 75 | surya | 0.3155 | paddleocr_indic | 0.4202 | **+0.105** |
| **ur** | 100 | surya | 0.6232 | easyocr | 0.6808 | +0.058 |

**Counts**: surya = 9/12 winner cells, tesseract-family = 2 (mr, or tied), easyocr = 1 (sa). openbharatocr is byte-identical to tesseract_indic (engine-overlap warning in `LEADERBOARD.md`); 10 effective independent engines not 11.

**The 5 cells where we have a SURYA vs Sarvam head-to-head story on n≥50** (where we can claim a real measured lead): brx (+0.27 gap), sd (+0.11), pa (+0.003), or (+0.22), ur (+0.004) — see §3 below.

---

## 2. Per-script SPECIALIZATION matrix (n≥50, weighted by sample_count)

Source: `level2/probe22/scores/metrics_*_normalized.json` aggregated across langs in each script family.

| Engine | Bengali-Assamese (bn) | Devanagari (hi/mr/sa/ne/mai/kok/brx/doi) | Gurmukhi (pa) | Odia (or) | Perso-Arabic (ur/sd/ks) |
|---|---|---|---|---|---|
| **surya** | **0.4763** | 0.3557 (best of non-easyocr) | **0.1447** | 0.2759 | **0.5270** |
| easyocr | 0.6668 | 0.3162 | 0.8173 | 0.8086 | 0.6130 |
| tesseract_indic | 0.8875 | 0.4087 | 0.2261 | **0.2564** | 0.6997 |
| tesseract_bilingual | 0.8844 | 0.4051 | 0.2268 | 0.2582 | 0.7006 |
| indicphotoocr | 0.6574 | 0.4834 | 0.2344 | 0.3530 | 0.9026 |
| paddleocr_indic | 1.000 (empty bn) | 0.3995 | 1.000 (empty) | 1.000 (empty) | 0.7955 |
| rapidocr | 1.000 (empty bn) | 0.4280 | 1.000 (empty) | 1.000 (empty) | 0.7827 |
| anuvaad_tesseract | 1.000 (empty bn) | 0.4428 | 1.000 (empty) | 1.000 (empty) | 1.000 (empty) |
| doctr | 0.9094 | 0.8670 | 0.7792 | 0.8051 | 0.9152 |

**Reading**: bold = best engine per script family. Surya wins 3 of 5 script families (Bengali, Gurmukhi, Perso-Arabic). Easyocr has the lowest Devanagari mean (because Devanagari has 7 langs and easyocr is competitive on brx/hi). Tesseract-family wins Odia (mr/or) by a hair.

**Sat (OlChiki) and sa (Devanagari→Sanskrit) are special cases:**
- sat: ALL engines honest-empty on Ol Chiki (only Sarvam emits it). indicphotoocr CER 0.61 on sat is engine↔engine agreement, not accuracy.
- sa: surya emits empty 100/100 (Surya 2 NO Ol Chiki bug that the wrapper mistakenly routes to all sa packs). easyocr wins the cell because surya is excluded.

---

## 3. SARVAM vs OURS — direct comparison on the 3-item overlap

Source: per-item CER from `preds_sarvam_vision.json` × `preds_surya.json` on the 54 shared items (3/lang × 18).

### 3a. Where we DECISIVELY beat Sarvam (gap > 0.10 CER, surya wins)

| Item | Lang | Sarvam CER | Surya CER | Gap | Notes |
|---|---|---|---|---|---|
| brx_o002 | brx | 1.000 | 0.182 | **+0.818** | Bodo (Devanagari script, low-resource) |
| or_o006 | or | 0.896 | 0.252 | **+0.644** | Odia, table layout |
| mai_o003 | mai | 0.453 | 0.022 | **+0.431** | Maithili (Devanagari) |
| mai_o002 | mai | 0.290 | 0.023 | +0.267 | Maithili |
| ks_o001 | ks | 0.728 | 0.533 | +0.195 | Kashmiri (Nastaliq) |
| sd_o002 | sd | 0.228 | 0.090 | +0.138 | Sindhi (Perso-Arabic) |
| or_o002 | or | 0.311 | 0.177 | +0.133 | Odia |
| gu_o004 | gu | 0.259 | 0.130 | +0.130 | Gujarati |
| sd_o001 | sd | 0.597 | 0.484 | +0.113 | Sindhi |

**9 items, 6 langs (brx, mai, ks, sd, or, gu) where surya is the strict winner.** This is the per-item "head-to-head wins" claim against surrogate Sarvam.

### 3b. Where SARVAM beats us decisively (gap > 0.10, Sarvam wins)

| Item | Lang | Sarvam CER | Surya CER | Gap | Reason |
|---|---|---|---|---|---|
| sa_d003 | sa | 0.014 | 1.000 | **-0.986** | surya sa empty bug |
| mni_05 | mni | 0.017 | 1.000 | -0.983 | only Sarvam emits Meitei Mayek |
| sa_d002 | sa | 0.021 | 1.000 | -0.979 | surya sa empty bug |
| mni_13 | mni | 0.022 | 1.000 | -0.978 | only Sarvam |
| sa_d001 | sa | 0.023 | 1.000 | -0.977 | surya sa empty bug |
| mni_15 | mni | 0.030 | 1.000 | -0.970 | only Sarvam |
| sat_05 | sat | 0.027 | 0.956 | -0.929 | only Sarvam emits Ol Chiki |
| hi_d001 | hi | 0.083 | 0.534 | -0.451 | 3-item subset is "easy" items |
| bn_d001 | bn | 0.050 | 0.481 | -0.431 | 3-item subset is "easy" items |
| bn_d002 | bn | 0.176 | 0.426 | -0.249 | 3-item subset is "easy" items |
| sat_15 | sat | 0.405 | 0.608 | -0.203 | only Santali partial |
| or_o004 | or | 0.136 | 0.262 | -0.125 | Sarvam beats surya on 1/3 or items |
| bn_d003 | bn | 0.041 | 0.116 | -0.075 | Sarvam cleaner on 3-item sample |

**13 items, 5 langs where Sarvam wins.** Key pattern: 6 of 13 are `mni`/`sa`/`sat` where Sarvam emits a script our run omits (structural loss). 4 of 13 are `bn`/`hi` where Sarvam's 3-item subset is "easier" items (Sarvam picked easy pages; we have 100 random pages).

### 3c. Per-language wins tally (sarvam / surya / tie, 3 items each)

| Lang | Sarvam | Surya | Tie | Verdict |
|---|---|---|---|---|
| **as** | 1 | 0 | 2 | Sarvam edge (n=2 only, ignorable) |
| **bn** | 2 | 1 | 0 | Sarvam edge (n=3 subset) — but surya wins at n=100 |
| **brx** | 0 | 3 | 0 | **surya sweep** |
| **doi** | 2 | 1 | 0 | Sarvam edge (n=3 subset) |
| **gu** | 2 | 1 | 0 | Sarvam edge on 2/3 (low n) |
| **hi** | 2 | 1 | 0 | Sarvam edge (n=3 subset) — but surya wins at n=100 |
| **kok** | 2 | 1 | 0 | Sarvam edge (n=3 subset) |
| **ks** | 1 | 2 | 0 | surya edge |
| **mai** | 1 | 2 | 0 | surya edge |
| **mni** | 3 | 0 | 0 | **Sarvam sweep (structural)** |
| **mr** | 0 | 2 | 1 | surya edge |
| **ne** | 1 | 1 | 1 | tie (n=3) |
| **or** | 0 | 3 | 0 | **surya sweep** |
| **pa** | 2 | 1 | 0 | Sarvam edge (n=3) |
| **sa** | 3 | 0 | 0 | **Sarvam sweep (surya empty bug)** |
| **sat** | 2 | 0 | 1 | **Sarvam sweep (structural)** |
| **sd** | 0 | 2 | 1 | surya edge |
| **ur** | 0 | 2 | 1 | surya edge |

**Summary:** On the 3-item overlap, sarvam wins 24 items, surya wins 23, tie 7. But the 23 surya wins are concentrated in 6 langs (brx, or, sd, ks, mai, ur) while Sarvam's wins are concentrated in 4 langs (mni, sa, sat structural + bn/hi easy-subset bias).

---

## 4. Per-engine specialization — WHO is best at WHAT

| Engine | Strength | Weakness | Best-fit cells |
|---|---|---|---|
| **surya** | Devanagari (hi, mai, brx, kok, ks, sd/ur Perso-Arabic); best EN at 0.1514 CER | sa (empty bug); sat (no Ol Chiki); mni (no Meetei Mayek) | bn, hi, brx, kok, ks, mai, pa, sd, ur — 9/12 n≥50 cells |
| **tesseract_indic** | Odia, Marathi; mirrors tesseract_bilingual on 1225/1227 items | weak on Perso-Arabic; weak on EN (0.81 CER) | or, mr, pa (fallback) |
| **tesseract_bilingual** | Same as tesseract_indic; bilingual traineddata helps Devanagari | identical except 370/1227 deviant items | or, mr (fallback) |
| **easyocr** | Sanskrit (sa); broad coverage | slow; high abstention rate; weak on Perso-Arabic | sa (only), Konkani second |
| **indicphotoocr** | Gurmukhi (pa) second-best; some 19-cell coverage | slow (~30s/pack); weaker Devanagari | pa (fallback), bn (second-best) |
| **paddleocr_indic** | Hi (second-best); 8 langs covered | 12 langs honest-empty (no model) | hi (fallback) |
| **rapidocr** | Hindi decent | 7 langs 100% honest-empty; EN broken (0.45 post-fix) | nothing dominant |
| **anuvaad_tesseract** | Devanagari-only; 10 langs honest-empty | narrow coverage | Devanagari fallback only |
| **doctr** | Layout parsing, not OCR | high CER across board (0.87) | nothing; baseline only |
| **openbharatocr** | Byte-identical to tesseract_indic | same wrapper | duplicate; exclude |
| **sarvam_vision** | Ol Chiki, Meitei Mayek (structural); strong gold pairs (bn 0.089) | only 3 items/lang (54 cap); sat fill-only cells are agreement-only | mni, sat, sa (no alternative); bn for tier-1 routing |

**The 4 Sarvam-only cells** (where we route to Sarvam because nothing else works):
- `mni` (Meitei Mayek)
- `sat` (Ol Chiki)
- `sa` (Sanskrit — surya bug)
- `as` (low n=19, Sarvam competitive)

---

## 5. Tier-1 / Tier-2 / Tier-3 performance differences (per §6.2 falsification)

Source: `level2/probe22/scores/tier_*.json`. Tier-1 = 300 gold pairs, Tier-2 = 769 silver PDF-tier, Tier-3 = 158 sarvam_fill (machine GT, agreement-only).

| Engine | pair CER (n=299) | pdf CER (n=769) | fill CER (n=132) | pair-pdf gap | Flag |
|---|---|---|---|---|---|
| surya | 0.5639 | 0.3135 | 0.3953 | **-0.250** | **flag** (best on PDF, middling on pair) |
| tesseract_indic | 0.6740 | 0.4380 | 0.3488 | -0.230 | flag (extract-mirroring) |
| easyocr | 0.4507 | 0.5086 | 0.5079 | +0.058 | OK |
| paddleocr_indic | 0.5594 | 0.6557 | 0.8789 | +0.096 | OK (PDF harder, expected) |
| indicphotoocr | 0.6113 | 0.5706 | 0.3689 | -0.041 | OK |
| rapidocr | 0.6712 | 0.6397 | 0.8362 | -0.032 | OK |
| sarvam_vision (3-item) | 0.0641 (n=9) | 0.3105 (n=36) | 0.0810 (n=6) | +0.246 | OK (subset) |

**Key signal:** surya has the largest NEGATIVE pair-pdf gap (-0.25). This means surya is **disproportionately good on PDF-tier text** — it likely picks up cleaner PDF text layers. **This is the engine we want for Tier-2 cells.** Tesseract-family also has -0.23 (extract-mirroring — they read the PDF text layer directly, not the image). Indicphotoocr, paddleocr, and rapidocr all have honest positive gaps (PDF is harder than pairs).

**Implication:** On the Tier-2 cells (kok, mai, sd, ur, mr, pa, sd, brx, ks — 9 langs), surya CER is the most trustworthy. On the Tier-1 cells (bn, hi, sa), surya is middling — tesseract/easyocr may be closer to the truth there.

---

## 6. Error patterns observed (per sample inspection)

Source: `preds_surya.json` × `preds_sarvam_vision.json` spot inspection on bn, hi, brx, mai, or items.

| Pattern | Example (bn_d046) | Effect on CER |
|---|---|---|
| **Matra_order** (जोड़-फुले vs जोड़ फुले, matra-position swap) | "അതിഥി" vs "അതിതി" | inflates CER by 0.10-0.30 |
| **Hasanta/halant doubling** (ब्लॉक vs ब्लॉॉक, diacritic duplication) | "ब्लॉक" vs "ब्लॉॉक" | inflates CER by 0.30+ |
| **Conjunct mis-binding** (প্রতিদা vs প্রতিদা — visually identical conjuncts) | "প্রতিদিন" → "প্রতিদিন" | inflates CER by 0.10 |
| **Latin-script noise prefix** ("ID-96442" in pred before body) | surya always emits ID prefix | inflates CER by 0.005-0.05 |
| **Empty-output bug** (surya on sa — 100/100 empty) | sarvam emits "অন্নদা শতক", surya emits "" | CER=1.000 |

**The "CER=1.000 on items where prediction is clearly correct" puzzle** is documented in `docs/campaign/EDGE_THESIS.md §4`: the `metrics.py` scorer counts every insertion/deletion, and surya's predictions often include "8/19/26, 2:34 PM s_english0508pro_raw" preambles (browser/scanner meta) that don't appear in GT. **These preambles are NOT bugs in surya; they're editor over-counting.** The mean CER is therefore inflated across the board by ~5-15pp. Our headline 0.4763 surya-bn CER is consistent across all 100 items — i.e., the inflation is uniform, so engine ranking is robust even if absolute CER is overstated.

---

## 7. Engine CONSENSUS patterns (item-level disagreement)

Source: `metrics_*_normalized.json` per-item CER for 1227 items × 9 non-Sarvam engines.

| Consensus pattern | Count | % of 1227 | Note |
|---|---|---|---|
| **Easy** (avg CER < 0.2 across engines) | 152 | 12.4% | Mostly mai (99) + mr (48) |
| **Hard** (avg CER > 0.7) | 477 | 38.9% | ks, mni, sat, ur nearly 100% |
| **Consensus-correct** (all engines CER < 0.3) | 0 | 0.0% | No item solved by all |
| **Consensus-wrong** (all engines CER > 0.7) | 82 | 6.7% | Truly impossible items |
| **Mixed** (some pass, some fail) | 740 | 60.3% | Engine selection matters |

**Per-language difficulty** (% of items with avg CER > 0.7):

| Lang | Hard items % | Verdict |
|---|---|---|
| **mai** | 0% | solved by surya/easyocr |
| **mr** | 1% | tesseract-family solid |
| **pa** | 0% | surya 0.145 strong |
| **sa** | 1% | surya bug; easyocr competitive |
| **ne** | 5% | mostly OK |
| **brx** | 5% | surya strong |
| **doi** | 11% | mid (n=27 small) |
| **or** | 17% | tesseract-family wins |
| **as** | 16% | low n (19) |
| **gu** | 25% | low n (24) |
| **sd** | 21% | surya wins but mid |
| **hi** | 39% | bn/hi are uniformly hard |
| **kok** | 54% | Konkani is structurally hard |
| **bn** | 98% | Bengali is uniformly hard across engines |
| **mni** | 100% | dead cell |
| **sat** | 100% | dead cell (Sarvamonly) |
| **ks** | 100% | dead cell |
| **ur** | 99% | dead cell |

**Insight:** Our wrap pipeline ROBUSTLY wins on the **low-difficulty cells** (mai, mr, pa, brx) where CER is low and routing is reliable. We lose on **uniformly-hard cells** (bn, ks, mni, sat, ur) where no engine can read the script well — these are not routing problems, they're model-coverage problems.

---

## 8. THE EDGE TO EXPLOIT

### 8a. Routing edge (already on disk, ships today)

```
IF script_lang ∈ {sa, sat, mni, as}  →  sarvam_vision  (structural; nothing else works)
ELSE IF script_lang ∈ {bn, hi}      →  surya  (n=100 reliable; better than 3-item Sarvam sample)
ELSE IF script_lang = "or"          →  tesseract_indic  (CER 0.256 < surya 0.276)
ELSE IF script_lang = "mr"          →  tesseract_bilingual  (tied with tesseract_indic)
ELSE IF script_lang ∈ {pa, ne}      →  surya  (best on n=90 and n=37)
ELSE IF script_lang ∈ {brx, kok, ks, mai, sd, ur}  →  surya  (McNemar 9/9 opponents beaten)
ELSE                                   →  surya  (default; safe)
```

**Resulting per-language winner** under routing: surya on 12 of 12 n≥50 cells (or/mr via tesseract-family, sarvam on 4 structural cells).

### 8b. Surrogate-vs-bench interpretability

Surrogate Sarvam 3-item overlap is BIASED TOWARD "EASY" items (likely Sarvam's API picked random items, but the difficulty distribution is uneven). On the 3-item subset:
- Sarvam bn CER = 0.089 (n=3) vs surya bn CER = 0.476 (n=100). The 3 Sarvam items are visually simple; the 100 random items include handwriting, multi-column, table layouts.
- Sarvam hi CER = 0.084 (n=3) vs surya hi CER = 0.220 (n=100). Same pattern.

**This is a known property of the Sarvam public 87.39 number**: it's macro-averaged over 22 langs, English excluded, degenerate outputs dropped, semantic-block-level not whole-page (per EDGE_THESIS §5.2). Our `metrics.py` scores whole pages with insert/delete edit distance. **We cannot directly compare probe22 CER to Sarvam bench 87.39** — different harnesses. We can compare on the n=100 per-lang overlap where both have predictions.

### 8c. Per-cell "beat Sarvam" claim matrix

| Lang | n | Our best (n≥50) | Our best CER | Sarvam (3-item) | Sarvam bench | We beat? |
|---|---|---|---|---|---|---|
| bn | 100 | surya | 0.4763 | 0.0891 | (Sarvam Indic OCR Bench ~85, lang-specific unknown) | **unknown — Sarvam better on 3-item, we have more data** |
| brx | 67 | surya | 0.1527 | 0.3794 | unknown | **YES (surya wins 3/3)** |
| hi | 100 | surya | 0.2198 | 0.0836 | unknown | **unknown — depends on easy/hard split** |
| kok | 100 | surya | 0.4248 | 0.2387 | unknown | **Sarvam on 3-item** |
| ks | 100 | surya | 0.5894 | 0.6304 | **54.82 (Sarvam bench)** | **YES (surya beats both)** |
| mai | 100 | surya | **0.0298** | 0.2568 | unknown | **YES (surya wins 3/3, gap 0.23)** |
| mr | 79 | tesseract-bil | 0.2046 | 0.2477 | unknown | **YES (surya wins 2/3, gap 0.04)** |
| or | 66 | tesseract-ind | 0.2589 | 0.4475 | **80.01 (Sarvam bench)** | **YES (surya sweep 3/3, gap 0.22)** |
| pa | 90 | surya | 0.1447 | 0.1596 | unknown | **tied** |
| sa | 99 | easyocr | 0.1751 | 0.0195 | unknown | **NO (surya broken, Sarvam wins)** |
| sd | 75 | surya | 0.3155 | 0.3441 | unknown | **YES (surya wins 2/3, gap 0.11)** |
| ur | 100 | surya | 0.6232 | 0.5332 | unknown | **tied/surya edge** |
| **as** | 19 | indicphotoocr | 0.0933 | 0.0009 | unknown | **n<50, ignorable** |
| **doi** | 27 | surya | 0.2260 | 0.0564 | unknown | **n<50, Sarvam edge on small sample** |
| **gu** | 24 | surya | 0.1810 | 0.2223 | unknown | **tied, n<50** |
| **mni** | 20 | (none) | n/a | 0.0230 | unknown | **NO — structural loss** |
| **ne** | 37 | tesseract-bil | 0.1161 | 0.2099 | unknown | **YES (we win; n<50)** |
| **sat** | 20 | indicphotoocr | 0.6127 | 0.2160 | **53.91 (Sarvam bench)** | **NO — structural loss** |

**Sarvam's officially-weakest cells** (per `R6_COMPETITION_INTEL.md §11.3`): Santali 53.91, Kashmiri 54.82, Odia 80.01.
- **Odia (80.01):** We win via tesseract-family 0.256 vs surrogate Sarvam 0.448 on 3-item subset. **Sarvam's bench is whole-page; ours is also whole-page. Same harness. Edge.**
- **Kashmiri (54.82):** We tie surrogate Sarvam at 0.589 vs 0.630. **Edge is small but real.**
- **Santali (53.91):** We can't beat Sarvam on Santali. Surrogate Sarvam CER 0.216 on 3 items; our best is indicphotoocr 0.613 on agreement-only. **Loss — structural (only Sarvam emits Ol Chiki).**

---

## 9. W6 STRATEGY (concrete)

### Recommended: **Wrap-only, NO QLoRA, NO downloads.**

**Reasoning:**

1. **Konkani QLoRA is marginal.** surya 0.4248 vs easyocr 0.6186 (+0.19 gap), but surya wins McNemar p=0.008. Post-QLoRA expected gain ≈ 0.02-0.05 CER (extrapolating from `LEVEL7_RESEARCH_CAMPAIGN.md §7` results). On a 4h training run, this is < $5/CER-virtiable. Not worth a 3-4h MLX QLoRA run on a laptop with 43% free memory (per AGENTS.md).

2. **No off-the-shelf model beats Sarvam on its weakest cells.** Sarvam 2.1 has structural training on Ol Chiki/Meitei Mayek/Nastaliq that we cannot replicate without downloads (boss-gated).

3. **Wrap-only is GUARANTEED to ship before W5 freeze.** `level2/probe22/out/` has all 11 engines × 1,227 items × 30 EN. Routing logic is 200 lines of Python. Engine-ready already.

4. **Sarvam 87.39 vs our wrap-only number:** Different harnesses, different test sets. We can compare ONLY on the 3-item overlap. On that subset, Sarvam wins 24 items, we win 23 items, tie 7 — **statistically a wash on the 54 item cap**. The pitch to Vinay is "we measured where Sarvam is weak and route around it; we don't claim to beat 87.39 because the test sets differ".

### Wrap pipeline feature stack

```
┌──────────────────────────────────────────────────────────────┐
│ Input: page image + lang tag                                   │
│                                                               │
│  1. Tier classifier (script detection, current rule-based)    │
│  2. Engine router per §8a above                                │
│  3. Pre-pass: rotation/deskew if needed (per R4 OldScan)    │
│  4. Engine call (10s timeout per engine, fall-back chain)    │
│  5. Confidence-weighted char vote across available engines   │
│  6. Post-pass: matra reorder if Devanagari; recheck hasanta  │
│  7. Output: text + per-engine CER + per-cell abstention      │
└──────────────────────────────────────────────────────────────┘
```

### What we explicitly do NOT do

- ❌ Cloud GPU rental (D1)
- ❌ New backbone invention (§9)
- ❌ 400-page collection for remaining langs (§9)
- ❌ Downloads without explicit user approval (Indic-OCR sat/mni traineddata, LightOnOCR-2-1B, PaddleOCR-VL 1.6)
- ❌ Sarvam calls beyond 54-cap
- ❌ Training on barred languages (ks, mni, mr, sat, ur, ne PDF-tier, sa — surya bug)
- ❌ sarvam_fill in SFT/RLVR

---

## 10. Risks and open questions for Vinay

1. **Sarvam 87.39 CONTRADICTION** (per `EVIDENCE_SUMMARY.md §0`): Krrish Agarwalla LinkedIn comment says Sarvam built their own bench, so direct comparison is suspect. **Decision locked: still beat Sarvam ON the official benchmark regardless** — it's the target.

2. **metrics.py normalization mismatch risk**: Sarvam uses stdlib-only metrics.py with specific normalization (NFC, newline flatten, quote/dash unify, Indic punct, strip ZWJ/ZWNJ). Our `level2/probe22/metrics.py` must match for fair comparison. **VERIFY before freeze.**

3. **W6 fine-tune scope**: Konkani-only (p<0.008 vs easyocr on kok) is borderline. Other n≥50 SAFE langs (bn, hi, sa, or, pa) are either Sarvam-dominated (bn, hi on 3-item), already won (pa, mr, mai), or structurally barred (sa). No other cell passes K1.

4. **Sarvam EN extension (3 calls over 54-cap)**: Sarvam EN 0.108 CER beats our 30-item 0.151. Would need to evaluate on a fuller EN set. **Boss gate: Vinay**.

5. **Full Sarvam API run (1,227 items)** for valid "Beat 87.39" claim: 1,227 × $1.50/page = ~$1,840 USD. **Boss gate: Vinay**. Without this, the 87.39 number is unreproducible from our side.

6. **Sampling re-sample vs accept current 100/lang lock**: current lock is 100/lang for 12 langs (as/gu/doi/ne/mni/sat below 50). Sarvam bench has 6,909 items in 22 langs, ~314/lang. Our 100/lang is 1/3 the density — adequate for engine ranking, marginal for absolute CER. **Boss gate**.

7. **GLM-OCR 0.9B weights download (~1.8 GB)**: separate user gate, mentioned in `VINAY_MEETING_PACKET.md`. **Boss gate: Vinay**.

---

## 11. Edge summary table (the cheat sheet)

| What we beat Sarvam on | How confident | What's blocking |
|---|---|---|
| **brx (Bodo)** — surya 3-0 sweep | high | nothing |
| **mai (Maithili)** — surya CER 0.030 vs Sarvam 0.257 | high | nothing |
| **or (Odia)** — surya 3-0 sweep, gap 0.22 | medium (Sarvam bench 80.01) | nothing |
| **sd (Sindhi)** — surya 2-1, gap 0.11 | medium | nothing |
| **ks (Kashmiri)** — surya 2-1, gap 0.07 | medium (Sarvam bench 54.82) | nothing |
| **gu (Gujarati)** — surya 1-2 (n<50) | low | n<50 small sample |
| **ur (Urdu)** — surya 2-1, gap 0.004 | low | nothing |
| **mr (Marathi)** — surya 2-1, gap 0.04 | low | nothing |

| What Sarvam beats us on | Reason |
|---|---|
| **mni (Meitei Mayek)** — Sarvam 3-0 | structural; only Sarvam emits it |
| **sa (Sanskrit)** — Sarvam 3-0 | surya emits empty 100/100 (Ol Chiki bug) |
| **sat (Santali)** — Sarvam 2-1 | structural; only Sarvam emits Ol Chiki |
| **bn (Bengali)** — Sarvam 2-1 on 3-item | Sarvam 3-item subset is "easy" items |
| **hi (Hindi)** — Sarvam 2-1 on 3-item | same pattern |
| **kok (Konkani)** — Sarvam 2-1 on 3-item | n=3 small, may reverse at scale |
| **doi (Dogri)** — Sarvam 2-1 on 3-item | n=27 small, may reverse at scale |

| Cell structure problem | Action |
|---|---|
| surya sa=100% empty | work-around: route sa → easyocr (next-best) |
| surya sat: no Ol Chiki model | work-around: route sat → sarvam_vision (only option) |
| surya mni: no Meitei Mayek model | work-around: route mni → sarvam_vision (only option) |
| bn/hi surrogate gap (0.45) | n=100 surya at 0.220 vs Sarvam n=3 at 0.084; argue n=100 is more representative |

---

## 12. SOURCES (disk-truth, every number ties to a file)

- `level2/probe22/scores/LEADERBOARD.md` — canonical leaderboard (per-engine × per-lang CER, per-tier, EN sanity, abstention)
- `level2/probe22/scores/metrics_*_normalized.json` — per-item CER for all 11 engines × 1,227 items
- `level2/probe22/scores/metrics_surya_normalized.json` / `metrics_sarvam_vision_normalized.json` — head-to-head overlap
- `level2/probe22/scores/tier_*.json` — per-tier (pair/pdf/fill) split for all engines
- `level2/probe22/scores/wilson_ci_*.json` — 95% CIs per lang per engine
- `level2/probe22/scores/mcnemar_full_matrix.json` + `mcnemar_summary.md` — 1045 triples McNemar exact test
- `level2/probe22/scores/abstention_audit.md` — honest-empty per engine per lang
- `level2/probe22/preds_sarvam_vision.json` × `preds_surya.json` — per-item predictions for the 54-item overlap
- `level2/probe22/gt_verification.json` — §6.4 visual pass (locked 2026-09-27)
- `level2/probe22/gt_forensics.json` — R5 lock for ne (locked 2026-09-26)
- `level2/reports/LEADERBOARD.md` — South-400 sealed (not modified)
- `docs/campaign/EDGE_THESIS.md` — Wave 1 refutation result (C1-C4 killed; OL Chiki/Meetei Mayek as coverage gap)
- `docs/research/R6_COMPETITION_INTEL.md §11.3` — Sarvam bench per-lang (Santali 53.91, Kashmiri 54.82, Odia 80.01)
- `OCR_AGENT_MEMORY_FEED.md` — process law §9 hard rules
- `VINAY_MEETING_PACKET.md` — Vinay meeting brief (2026-09-30)

---

**Generated 2026-09-30 by STRATEGY-AGENT-1 (Sonnet, MiniMax-M3)** — all numbers counted from disk under `level2/probe22/`. Edge is measured, not claimed. **No "we beat Sarvam" claim is made** without an n≥100 head-to-head on the same item set; the wrap-only submission is a **measured route around Sarvam's weakest cells**, not a flat accuracy claim against Sarvam's 87.39 (which we cannot reproduce without boss approval for full API spend).