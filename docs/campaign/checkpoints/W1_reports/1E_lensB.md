# W1E — LENS B: **DOES THE MECHANISM FAIL ON REAL INDIC INPUT?**

Adversarial review of C1–C4 from `1E_hunt.md` (lens A). Agent: 1E-lensB. Run 2026-09-29.
**Mandate: kill the theses. Default REFUTED. A read-only number beats an argument.**

- Read: `docs/campaign/CAMPAIGN_DIRECTIVE.md` Part A (lines 19–117), `1E_hunt.md`, `docs/campaign/BENCHMARK_22.md`.
- Data: `level2/probe22/sheet.csv` (12,324 rows, 11 models, 1,227 scored items), `level2/probe22/manifest.json` (1,283).
- **Scorer caveat, stated up front:** I could **not** reproduce `sheet.csv`'s CER exactly. `metrics.py --normalize` reproduces 128/400 random rows (my number is always ≥ the sheet's). Every CER below is therefore one of: (a) the sheet's own `CER` column, quoted as-is, or (b) my recomputation under one declared normaliser (whitespace-stripped Levenshtein, or `normalize_for_scoring∘normalize_for_metrics`). Counterfactuals are always computed under the same normaliser on both sides, so the *ratios* hold. **UNKNOWN:** which exact normaliser variant built the sheet.
- Wrote only this file. All scratch in `/tmp/lensB/`. Nothing in `src/` run, nothing downloaded, no Sarvam call.

---

## SCOREBOARD

| thesis | verdict | the number that decided it |
|---|---|---|
| **C1** script-block attribution | **WOUNDED** (2 findings survive, the headline is refuted, the metric is degenerate) | per-block Ol Chiki CER = **0.9500 for all 10 engines, identical to 4 dp**; 0 Ol Chiki chars emitted by any local engine in 20/20 sat items |
| **C2** akshara-validity-gated fusion | **REFUTED** | validity-argmax = **0.6766** vs surya-always **0.4190** — 61% *worse than doing nothing*; binarised correlation is **sign-flipped** (penalty==0 → CER 0.6304 > penalty>0 → 0.6099) |
| **C3** script-mismatch abstention | **WOUNDED** (strongest mechanism I found — but not the one proposed, and zero on 8 of 18 langs) | recall **0.0–5.2%** for 8 of 10 engines; anuvaad fires on **0 of 610**; deployable consensus form gets 0.3944 → **0.3296** (65% of oracle gap) but **80% of that is the `sa` cell** |
| **C4** GT script-purity gate | **REFUTED** (as a cause; survives as a labelled split) | stripping the Ol Chiki from the 18 mr items moves CER by **+0.004** (wrong direction); the claimed +0.098 is **14× the arithmetic maximum** (0.0071) |

---

# C1 — SCRIPT-BLOCK ATTRIBUTION · **WOUNDED**

## What I measured

**M1.1 — The 0.543 Ol Chiki share is REAL, and it is n=20, not n=3.**
```
python3 -c "… blocks(GT) …"   # script: /tmp/lensB/common.py
mean per-item OlChiki share of non-WS chars, n=20 sat items = 0.5430
median 0.5000 · char-weighted 0.5369 (1755 / 3269)
bilingual items 16/20 · items >=90% Ol Chiki 3/20 · pure-Bengali 1/20 (sat_14)
```
Reproduces `1E_hunt.md:13` to 4 dp. **This part of C1 survives intact.**

**M1.2 — The 0.457 floor is arithmetically exact.**
`mean over 20 sat items of CER(GT, OlChiki-only-string)` = **0.4570** (my normaliser). Identical to `1 − 0.5430`. **Survives.**

**M1.3 — "our best local engine already scores 0.459" is NOT IN THE DATA. (refuted)**
```
python3 -c "… for every (language, model) cell, |mean CER − 0.459| < 0.0006 …"
→ 0 cells found across all 12,324 rows
sat best local  = indicphotoocr 0.6514 (n=20)   surya 0.7621
sat bilingual-only subset (n=16) best = indicphotoocr 0.5821
```
The closest real numbers to 0.459 in the whole sheet are the tess-family grand mean (0.4918) and surya's (0.3944). **The best local engine sits 0.194 ABOVE the floor, not on it.** The "0.457 vs 0.459 tie — the cell cannot move" claim is built on a number that is not in the file. It is not a tiny-n artefact; it is unsourced.

**M1.4 — The multi-script census kills the general claim.**
```
blocks = maximal same-Unicode-block runs, >=10 chars, non-script chars do NOT break a run
lang   n  multi(>=2 distinct Indic scripts)  pct   block census
as 19 0 0.0%  ·  bn 100 0 0.0%  ·  brx 67 0 0.0%  ·  doi 27 0 0.0%  ·  gu 24 0 0.0%
hi 100 0 0.0%  ·  kok 100 0 0.0%  ·  ks 100 0 0.0%  ·  mai 100 0 0.0%  ·  mni 20 0 0.0%
mr 79 0 0.0%  ·  ne 37 0 0.0%  ·  or 69 0 0.0%  ·  pa 90 0 0.0%  ·  sa 100 0 0.0%
sd 75 0 0.0%  ·  ur 100 0 0.0%  ·  sat 20 16 80.0%
TOTAL 1227 items → 16 multi-script = 1.30%. ALL 16 ARE `sat`.
```
**C1 buys exactly one cell of 18 (and zero of the 4 South tags on this evidence).** 17 of 18 languages are 100% single-script. Only `gu` has a 10-char cross-script run (1 item), `kok` 1, `ur` 1 — all below the ≥10-char / ≥2-script bar.

**M1.5 — The proposed metric is DEGENERATE on the exact cell it claims to rescue.**
```
Ol Chiki characters emitted, sat n=20, per engine:
  surya 0 · anuvaad 0 · openbharatocr 0 · tesseract_indic 0 · tesseract_bilingual 0
  indicphotoocr 0 · paddleocr_indic 0 · rapidocr 0 · doctr 0 · easyocr 0
  sarvam_vision 316 chars over 3/3 items
→ OlChiki-block CER = 0.9500 for ALL TEN ENGINES, identical to 4 dp
   (19/20 items score 1.0 because the block is absent; sat_14 has no Ol Chiki in GT → 0.0)
Page-CER spread across the same 10 engines: 0.6514 → 1.0000. Per-block spread: 0.0000.
```
The metric converts a 0.35-wide page-CER range into a **flat line** exactly where C1 wanted to create signal. surya emits a Bengali block on 14/20 sat items, indicphotoocr on 20/20, the other eight on 0/20 — so the sat per-block table has **one** informative cell (Bengali × 2 engines) out of 20.

**M1.6 — The alignment objection FAILS (point for C1).**
```
Ol Chiki word count vs Bengali word count, 16/16 bilingual sat items: ratio 1.00 on every item
```
It is a **transliteration**, not a free translation. Blocks are separable by line. (`sat_05`: `ᱪᱤᱠᱤ ᱠᱚᱛᱮ ᱚᱞ ᱟᱠᱟᱱᱟ?` / `চিকি কতে অল আকানা?` — 1 word / 1 word.)

**M1.7 — Implementation trap (cheap named change).** A naive "maximal single-Unicode-block run" splitter that treats every non-script char as a run boundary fragments `sat_05` into 8+ runs of <10 chars and returns **zero** blocks. The splitter must carry non-script chars *inside* the current run. 20 lines.

## Which link breaks

**The third link — "per-block CER creates a metric that can move the `sat` cell."** It cannot: the metric has zero variance across engines because the block is empty for all of them. The *first* link (0.543 share, n=20) and the *second* (0.457 floor) hold.

## Best counter-argument to my kill

"Zero Ol Chiki characters from 10 engines in 20/20 items is not a broken metric — it is the single sharpest fact anyone has about Santali. Report it as a **coverage** number (`olchiki_chars_emitted / olchiki_chars_in_gt` = **0/1755**), not a CER. Coverage is 0, is not capped, does not degenerate, and immediately motivates F6's font-inventory finding." **I accept this. It is the surviving form of C1 and it is worth 0.5 day, not 1 day.**

---

# C2 — AKSHARA-VALIDITY-GATED FUSION · **REFUTED**

I wrote a fair-faith 15-rule akshara verifier (`/tmp/lensB/validity.py`: terminal virama, orphan ZWJ/ZWNJ, nukta on a non-composable base, matra-without-base, Malayalam chillu+virama, intra-token script mixing, hasant-at-EOL, degenerate clusters, digit-run hallucination) and tested it against every cheap alternative on identical data.

**M2.1 — The gap's shape reproduces; the absolute numbers do not.**
```
random.seed(20260926); random.sample(sorted(GT.keys()), 300) ; 10 local engines ; repo normalizer
best single  = surya 0.4190   (claim 0.5229)
ORACLE       = 0.3213          (claim 0.4277)
gap +0.0977 = 23.3% rel        (claim 18%)
on all 1,227 : surya 0.3944 · ORACLE 0.2947 · gap 0.0997
oracle winner = surya on 201/300; a non-surya engine wins only 99/300 (33%)
```
The relative gap (17.7% vs 18%) reproduces. The absolute best-single (0.42 vs 0.52) does not. **A 0.10 absolute discrepancy at n=300 is not noise** — it means the two samples/normalisers are not the same draw. The ceiling number should not go to a CEO meeting without the sample pinned.

**M2.2 — THE KILL: the validity verifier is worse than doing nothing.**
```
rule (300 items, sheet CER)                        mean CER
ORACLE                                             0.3213
surya always                                       0.4190
consensus_script (C3's rule, no GT)                0.3534
MBR-1best / medoid                                 0.5150
shortest_nonempty                                  0.6012
VALIDITY-ARGMAX  (C2's proposal)                  0.6766
→ captures −263.8% of the oracle gap. Picks doctr on 155/300 items (52%).
```

**M2.3 — WHY: the rules are structurally blind to the failure mode.**
```
3,000 predictions by profile:      mean CER   mean validity penalty   penalty==0
  has_Indic  n=2211                0.5009      2.098                 31%
  empty      n=441                 1.0000     10.000                  0%
  no Indic block n=348             0.8653      0.234                 80%   ← the wrong-script garbage
```
A ruleset built on **Brahmic grapheme clusters** (virama, nukta, matra, chillu, ZWJ) scores **Latin/no-block garbage at penalty 0.234 and near-zero 80% of the time**, and scores *real Indic text* at 2.098. It systematically prefers the garbage. This is a design failure of the feature class, not a tuning failure — 300 lines of the same rules will not fix it.

**M2.4 — The correlation is sign-flipped.**
```
Pearson r(penalty, CER) = +0.1831  (n=3,000 rows)
penalty == 0 : n=968  mean CER 0.6304
penalty >  0 : n=2032 mean CER 0.6099     ← the "valid" rows are WORSE
```

**M2.5 — It adds harm on top of a working rule.**
`consensus_script 0.3534` → `consensus_script + validity gate 0.4547` (**+0.101**). The gate is not useless; it is actively destructive.

**M2.6 — On the items that carry the prize, the verifier is indifferent.**
```
72 switch items (a non-surya engine beats surya): oracle-winner is among the validity-minimum
engines on 13/72 = 18%.  In 40/72 cases >=2 engines tie at the validity minimum.
penalty of the ORACLE-WINNER mean 2.868, ==0 on 13/72
penalty of surya                 mean 5.208, ==0 on 18/72   ← surya is "more valid" than the right answer
```

**M2.7 — The fusion ceiling is an EMPTY-STRING detector, not complementary recognition.**
```
300 items:  surya always 0.4190 · consensus_script 0.3534 · "if surya empty, take the longest
            non-empty output" 0.3545 · ORACLE 0.3213
            → the 2-day mechanism and the 1-line mechanism are indistinguishable.
268 items where surya did NOT abstain:
            surya 0.3496 · consensus_script 0.3452 · ORACLE 0.3314
            residual gap 0.0182; the rule captures 0.0044 of it (24%).
37 switches: 32 on surya-EMPTY items, 5 on surya-non-empty.
All 1,227:   surya 0.3944 → rule 0.3296, ORACLE 0.2947 (65% of gap).
             Per language the gain is: sa −0.6352 (100/100 switches, surya empty 100/100),
             mni −0.0416, sat −0.0777, doi −0.0988, ne −0.0741, gu −0.0719, brx −0.0472,
             and EXACTLY +0.0000 with 0 switches on as, hi, kok, ks, mai, pa, sd, ur.
             sa alone = 0.6352 x 100/1227 = −0.0518 of the −0.0648 total = 80%.
```
An orthography verifier **cannot** see this, because the signal is "the string is empty", not "the string is ill-formed".

**M2.8 — The cited mechanism does not transfer (arXiv 2607.00250v5, abstract opened).**
Title: *LV-ROVER-MLT: Low-Resource Maltese OCR by Synthetic Fine-Tuning and Multi-Stream Arbitration.* Author: Adam Darmanin (single), "working paper".
- "synthetic fine-tuning of **Tesseract 5** with five complementary recognition streams" — the five streams are **the same recogniser at five settings**, not five independent model families. Our 10 are genuinely independent. ROVER-style agreement between five views of one recogniser is not evidence about agreement between different recognisers.
- "**lexicon-gated** word-level arbitration **adapted to Maltese diacritics and hyphenation**" — the eligibility gate is a **Maltese lexicon + a Maltese diacritic/hyphenation rule set** (Ċ Ġ Ħ Ż). It is not a generic akshara verifier, and it is not the mechanism C2 proposes to port.
- Held-out CER **0.0074** vs next 0.0161. Their operating point is ~40× better than our 0.2947 oracle. Gates have essentially nothing to arbitrate at CER 0.0074.
- "significant improvement over stock Tesseract on Luxembourgish, while the **Hungarian result was inconclusive**" — one positive transfer out of two reported.
- Basis: NOMOCRAT **57 verified annotated pages**.
- **Verdict: a 57-page, single-author, same-recogniser, 0.7%-CER Maltese competition win is not evidence that an orthography gate will move a 29.5%-CER, 10-independent-engine, 18-language Indic board.** The paper's own second transfer target is the reported failure.

## Which link breaks

**The premise link, and then the mechanism link.** The premise ("the fusion ceiling is complementary recognition") is an abstention artefact: 32 of 37 switches are surya-empty, 80% of the total gain is the `sa` cell where surya is empty 100/100. The mechanism ("an akshara verifier can pick the winner") is blind by construction: the non-Bramic garbage scores cleanest. Every link after that is downstream of a number that is already wrong.

## Best counter-argument to my kill

"The 0.0997 oracle gap on 1,227 items is real and I did not refute it — I refuted the *verifier* and the *attribution*. A **learned** router over 10 engines × 22 languages, trained on the 1,227 scored items with a script-coverage feature and an is-empty feature, is a different object and is not what C2 proposed. The right W1 artefact is therefore not a 300-line rule file; it is the **oracle-vs-achievable decomposition table** I just produced (per-language oracle, oracle-minus-surya, share of the gap that is surya-empty), which costs 0.5 day and is what the training decision in W6 actually needs."

**I accept the measurement, reject the 2-day build.** If the gap survives after `sa` is fixed, the residual is 0.0182 on non-abstained items and my five cheap rules all fail on it.

---

# C3 — SCRIPT-MISMATCH AS A FREE ABSTENTION SIGNAL · **WOUNDED**

**M3.1 — The detector reproduces, and the separation is real.**
```
CER | block-overlap with GT  vs  CER | no overlap      (non-empty predictions only)
engine              n_match  CER|match  n_mismatch  CER|mismatch
surya                  1076    0.311          22       0.901
tesseract_indic        1188    0.479          36       0.859
openbharatocr          1190    0.480          36       0.859
easyocr               1076    0.457         151       0.820
indicphotoocr          923    0.453         302       0.898
doctr                     1    0.828        1225       0.870   ← NO SIGNAL (mismatch is BETTER)
```

**M3.2 — THE KILL: precision 95–100%, recall 0.0–5.2%. It is a confirmation signal, not an abstention signal.**
```
engine              flagged  false_pos  precision  real_bad  recall   n_empty
surya                   22          1      95.5%      469     4.3%     129
anuvaad_tesseract        0          0        n/a      317     0.0%     617   ← fires on 0 of 610
paddleocr_indic          1          0     100.0%      340     0.3%     536   ← 1 of 691
rapidocr                 2          0     100.0%      678     0.3%     343
openbharatocr           36          0     100.0%      680     5.0%       1
tesseract_indic         36          0     100.0%      678     5.2%       3
tesseract_bilingual     37          0     100.0%      677     5.2%       1
easyocr                151          3      98.0%      677    17.9%       0
indicphotoocr          302          1      99.7%      549    35.4%       2
doctr                 1225          3      99.8%        1    99.9%       1
```
The attack in my brief is **confirmed exactly**: the detector fires on **0 of 610** rows for `anuvaad_tesseract` and **1 of 691** for `paddleocr_indic` — the two engines that abstain most. A detector that fires on 0 of 2 engines is not a routing feature; it is a lint. And `doctr`'s 1,225 "flags" carry no information (0.828 match vs 0.870 mismatch).

**M3.3 — The false positives are not random, and they are exactly the population we care about.**
```
pooled over 10 engines: 1,812 flagged, 8 with CER<0.3 (0.44% FP)
all 8 FPs are Gujarati items: gu_05 (surya 0.1194, doctr 0.0448, easyocr 0.1791),
                               gu_01 (doctr 0.1447, easyocr 0.2171), gu_07 (doctr 0.2357, easyocr 0.2978)
gu_05 GT: 'છંગ, ind. A term used in multiplying by six any number above unity.'
surya → 'Section I. A term used in multiplying by six any number above unity.'
```
3 Gujarati chars, 68 Latin. A pure block-overlap test mis-fires on the **"Indian-language page with a large English span"** class — the mixed-script population this whole campaign targets. That is 1/24 = 4.2% of the `gu` cell from a single rule, and it is a *systematic* class, not noise.

**M3.4 — Abstention is the wrong action; DROPPING the flagged rows breaks the board.**
```
mean CER, all rows → mean CER after dropping flagged rows (n changes)
surya             0.3944 (1227) → 0.3852 (1205)   −0.0092
openbharatocr     0.4918 (1227) → 0.4807 (1191)   −0.0111
paddleocr_indic   0.6629 (1227) → 0.6627 (1226)   −0.0002
doctr             0.8704 (1227) → 0.9141 (2)      +0.0437  ← ABSTAINING MAKES IT WORSE
indicphotoocr     0.5634 (1227) → 0.4542 (925)    −0.1092
easyocr           0.5013 (1227) → 0.4566 (1076)   −0.0447
```
n becomes 1227 / 1205 / 1226 / **2** / 925 / 1076 — the leaderboard stops being a fixed-n comparison, and for `doctr` the rule **raises** the reported CER from 0.8704 to 0.9141 while leaving 2 scored rows. F4's own argument (report abstain_rate, don't drop) is the right one.

**M3.5 — The deployable form works, and it is NOT the form proposed.**
```
char-weighted plurality script across the 10 engines' OWN outputs (no ground truth anywhere),
tie-break to surya:
  all 1,227 : surya 0.3944 → 0.3296 ; ORACLE 0.2947 ; captures 65.0% of the gap ; 144 switches
  300 sample: 0.4190 → 0.3534 ; 37 switches ; helped 36, hurt 0
```

**M3.6 — The mechanism is EXACTLY ZERO on cursive Nastaliq, and on 8 of 18 languages.**
```
lang   n   surya    rule     ORACLE   delta    switched
ks   100  0.5894  0.5894  0.5872  +0.0000     0     ← Nastaliq
ur   100  0.6232  0.6232  0.6224  +0.0000     0     ← Nastaliq
sd    75  0.3155  0.3155  0.3145  +0.0000     0     ← Nastaliq
as 19 · hi 100 · kok 100 · mai 100 · pa 90 → +0.0000, 0 switches (395 items)
mni  20  0.9769  0.9353  0.8531  −0.0416    11     helps, still dead (best local 0.858)
sat  20  0.7621  0.6844  0.6481  −0.0777     6     helps, still dead (best local 0.6514)
sa  100  1.0000  0.3648  0.1516  −0.6352   100     ← 80% of the whole gain
```
**A wrong-but-Arabic Nastaliq rendering is still in the Arabic block, so script agreement is mathematically invariant to the single largest error class in `ks`/`ur`/`sd`.** This is the mechanism-fails-on-real-Indic-input test, and it fails cleanly.

## Which link breaks

**Link 2 — "script agreement as a per-item per-engine feature over 10 local engines" — breaks for 8 of 10 engines**, because the engines that abstain most never mismatch, and because a wrong-in-Arabic-script Nastaliq output is indistinguishable by this feature. Links 3 (false-positive cost) and 4 (abstention is the wrong action) both break too. Link 1 (the separation exists) is the only one that holds, and it holds for the wrong reason: it mostly detects *non-Bramic garbage*, which 53% of the time is the empty string.

## NAMED CHANGE that would save it

Replace the **GT-block-overlap** feature with the **cross-engine consensus-script** feature (char-weighted plurality over the 10 engines' own outputs, tie-break to surya, no GT). Measured: 0.3944 → 0.3296 on all 1,227, 65% of the oracle gap, 36/37 switches helped, 0 hurt. Report it as `surya_all_empty_rate` alongside it, because 80% of the gain is one cell. **Do not** call it an abstention signal; call it a router. Cost 0.5 day, not 1.

---

# C4 — GT SCRIPT-PURITY GATE · **REFUTED as a cause · survives as a labelled split**

**M4.1 — Every headline number in F2 reproduces EXACTLY.**
```
mr items with >=1 Ol Chiki char = 18 of 79 scored.  ids: mr_o001, o005, o014, o019, o023,
o028, o032, o037, o046, o050, o055, o059, o064, o068, o073, o082, o094, o099
engine                  clean(n=61)  contaminated(n=18)  contribution to the 79-mean
openbharatocr              0.1055         0.5411              +0.0992
tesseract_indic            0.1055         0.5411              +0.0992
easyocr                    0.1087         0.5464              +0.0997
surya                      0.1196         0.5396              +0.0957
paddleocr_indic            0.1179         0.5372              +0.0955
anuvaad_tesseract          0.1888         0.5556              +0.0836
indicphotoocr              0.2707         0.5749              +0.0693
doctr                      0.8468         0.8728              +0.0058
```
Claim was 0.105 / 0.537–0.541 / +0.098. **All three confirmed to 3 dp, and the effect is universal across all 10 engines.**

**M4.2 — THE KILL: the cause is arithmetically impossible.**
```
Ol Chiki chars in the 79 SCORED mr items (sheet.csv GT)  = 64      (claim: 645)
total GT chars on those 18 items                          = 9,000
MAXIMUM CER these 64 chars can contribute                 = 64/9000 = 0.0071
claimed contribution                                       = +0.098   → 14x the ceiling
manifest.json, all 100 mr items, Ol Chiki chars            = 916
```
645 sits between the two sets. F2 counted (or reported) the **manifest 100** while claiming a **79-item** effect — the exact manifest-vs-scored conflation `CAMPAIGN_DIRECTIVE.md` A4 warns about, and the same conflation appears in F2's own UNRESOLVED line ("F1's floor is a 79-item estimate"). The scored-set number is **64**, one order of magnitude smaller.

**M4.3 — DIRECT TEST: remove the alleged cause and the CER does not move.**
```
CER over the 18 items, GT as-is  vs  GT with the 64 Ol Chiki characters STRIPPED (my normaliser)
surya              0.7244 → 0.7285   (+0.0041)
openbharatocr      0.7268 → 0.7308   (+0.0040)
tesseract_indic    0.7268 → 0.7308   (+0.0040)
indicphotoocr      0.8119 → 0.8168   (+0.0050)
easyocr            0.7389 → 0.7424   (+0.0035)
anuvaad_tesseract  0.7500 → 0.7542   (+0.0042)
paddleocr_indic    0.7255 → 0.7298   (+0.0043)
```
Removing the Ol Chiki makes the score **slightly worse** (deletion counting), by 0.004. The 0.53 gap between the 61 clean and the 18 contaminated items is **not caused by the Ol Chiki.**

**M4.4 — The confound.**
```
                        clean (n=61)   contaminated (n=18)
Latin+alnum share          0.0257          0.1903      (7.4x)
digit share                0.0122          0.0960      (7.9x)
```
The 18 items are the table / English-heavy pages. The engines' 0.54 CER there is a **real failure on mixed-script table content**, not a GT artefact. (Note: the sheet's own `has_table` column reads `False` for all 79 mr items, so the field does not catch this — a second reason not to trust it as a gate input.)

**M4.5 — BLAST RADIUS: the punctuation whitelist is not a `pa` footnote, it is the difference between a fix and destroying 3 cells.**
```
lang  off-script  items      chars   charset
pa    Devanagari  88/90     1070    । U+0964 x743, ॥ U+0965 x308, ि ् र क x2 each  → 1051/1070 = punctuation
bn    Devanagari  99/100     355    । U+0964 x349, then 6 single real letters          → 349/355 = punctuation
or    Devanagari  34/69       82    । U+0964 x82 (100% punctuation)
as    Devanagari  12/19       26    । U+0964 x26 (100% punctuation)
gu    Devanagari   3/24       12    म ल ा ॥ । उ ्   ← REAL letters, small n
kok   Gurmukhi     1/100       6    ਠ ੰ ਢ ੀ ਲ     ← REAL letters, n=1
ur    Devanagari   1/100       9    ल े ी ख न ज      ← REAL letters, n=1 (legit Urdu loanword)
or    Bengali      1/69        8    র ম া ন স ো    ← REAL letters, n=1
mr    OlChiki     18/79       64    ᱭ ᱫ ᱬ ᱨ ᱶ ᱷ    ← REAL letters, the only large case
```
F2 flagged the `pa` risk and **missed `bn` (99/100), `or` (34/69) and `as` (12/19)**, which are the same danda class. A gate without the whitelist does not "shred Punjabi" — it **removes 3 of the 18 language cells outright.**

**M4.6 — The honesty question.** The gate converts `mr` 0.205 → 0.105 by **deleting the 18 hardest, most representative `mr` items** — the table/English-span pages, which are the pages the product will actually see. `mr` is currently a cell the tess-family **wins**. Reporting 0.105 as "the Marathi score" is a self-inflicted score cut dressed as a purity fix. If the split is worth reporting, it must be published as **two columns (prose n=61 / table-or-Latin n=18)**, never as one number with 18 rows deleted.

## Which link breaks

**The causal link — "Ol Chiki injected into the GT causes the +0.098."** It is 14× over the arithmetic ceiling, and removing the Ol Chiki moves the CER by 0.004 in the wrong direction. The **descriptive** link (18/79 items split 0.105 vs 0.541) is exact and survives. The **whitelist** link breaks harder than stated (3 cells, not 1).

## Best counter-argument to my kill

"The split is real and reproducible to 3 dp on 79 items, and a reader who sees a single `mr 0.205` has no way to know 23% of that cell is table pages. Publishing `mr_prose 0.106 (n=61) | mr_table 0.541 (n=18)` is strictly more informative than either 0.205 or 0.105, costs 0.5 day, and touches nothing locked. The *gate* is wrong; the *split* is right." **I accept this. It is the surviving form of C4 and it must not be labelled a purity fix.**

---

## EVERY COMMAND I RAN

**Reading**
1. `read docs/campaign/CAMPAIGN_DIRECTIVE.md` (lines 1–120)
2. `read docs/campaign/checkpoints/W1_reports/1E_hunt.md` (full, 74 lines)
3. `cut -c1-800 docs/campaign/BENCHMARK_22.md | head -100` and `| sed -n '100,220p'`
4. `head -1 level2/probe22/sheet.csv` · `wc -l level2/probe22/sheet.csv` · `ls -la level2/probe22/`
5. `sed -n '128,160p;540,580p' level2/probe22/metrics.py | cut -c1-300` · `grep -n "def preprocess" -A 30 metrics.py`
6. `webfetch https://arxiv.org/abs/2607.00250` (abstract opened, full text)

**Scratch written (outside the repo)**
7. `cat > /tmp/lensB/common.py` — CSV loader, Unicode-block classifier, block splitter, Levenshtein, CER
8. `python3 -c "…"` to patch `common.py` twice: Oriya range 0x0B80→**0x0B50–0x0B7F** (my first pass had it wrong and reported 0 blocks for all 69 `or` items), and the block splitter to carry non-script chars inside a run
9. `cat > /tmp/lensB/validity.py` — the 15-rule akshara verifier; patched `clusters()` because `re` in Python 3.14 here rejects `\X`
10. `cat > /tmp/lensB/c2.py`, `c2b.py`, `c2c.py`, `c2d.py`, `c2e.py`, `c3f.py` — C2/C3 measurement drivers, run with `timeout 900/1200/1500 python3 …`

**Measurements (all read-only, all on `sheet.csv` unless stated)**
11. C1: Ol Chiki share per sat item, n=20 → mean 0.5430, median 0.5000, char-weighted 0.5369
12. C1: `CER(GT, OlChiki-only)` floor, n=20 → 0.4570
13. C1: multi-script census, all 1,227 items, runs ≥10 chars → 16 items, all `sat`
14. C1: Ol Chiki chars emitted per engine on 20 sat items → 0 for all 10 local engines
15. C1: per-block CER by engine on sat → 0.9500 for all 10; page CER 0.6514–1.0000
16. C1: `|mean CER − 0.459| < 0.0006` sweep over all 12,324 rows → **0 cells**
17. C1: Ol Chiki vs Bengali word-count ratio, 16/16 bilingual items → 1.00
18. C2: seeded 300 sample (`random.seed(20260926)`), oracle / best-single → 0.3213 / 0.4190
19. C2: `r(penalty, CER)` over 3,000 rows → +0.1831; penalty==0 → 0.6304 (n=968) vs penalty>0 → 0.6099 (n=2,032)
20. C2: validity-argmax 0.6766 · MBR-1best 0.5150 · shortest_nonempty 0.6012 · consensus_script 0.3534 · surya 0.4190 · oracle 0.3213
21. C2: penalty by output profile → has_Indic 2.098 (31% zero), no-Indic-block 0.234 (**80% zero**), empty 10.0
22. C2: oracle-winner among validity-minimum on 72 switch items → 13/72 (18%)
23. C2: empty-detector (0.3545) vs consensus_script (0.3534) on 300; 268 non-abstained items 0.3496 / 0.3452 / 0.3314; 32 of 37 switches on surya-empty
24. C2: same rules on all 1,227 → 0.3944 → 0.3296, oracle 0.2947, per-language delta table
25. C3: block-overlap detector — CER|match vs CER|mismatch and precision/recall per engine, all 12,324 rows
26. C3: FP inspection — 8 pooled FPs, all Gujarati; `gu_05` GT vs surya prediction printed
27. C3: drop-the-flagged-rows effect on mean and n, per engine
28. C4: off-script character census per language, charset breakdown (danda counts)
29. C4: mr clean(61) vs contaminated(18) CER, 10 engines, sheet metric
30. C4: strip-Ol-Chiki strip-out test, 7 engines, my normaliser
31. C4: Ol Chiki char count in scored mr (64) vs `manifest.json` mr (916); arithmetic ceiling 0.0071
32. C4: Latin/alnum and digit share, clean vs contaminated

---

## UNRESOLVED

1. **The sheet's exact normaliser.** `metrics.py --normalize` reproduces only 128/400 random rows (my recompute is always ≥). I could not find the variant that built `sheet.csv`, so I could not independently verify **any** CER in `BENCHMARK_22.md` beyond those my code reproduces. **Every downstream claim about "0.5229 vs 0.4277" inherits this.** The 0.10 absolute discrepancy on C2's 300-sample is *probably* this and *might* be a different sample draw. UNKNOWN, and it should be resolved before any of these numbers reach the meeting.
2. **Whether `sat`'s 0.543 Ol Chiki share holds beyond 20 items.** It cannot: `sat` has n=20 scored and n=20 labelled. There is no larger `sat` set on disk. F2's "no 1,683-item recount" is moot for this language. But the same bilingual-raster pattern was **not** looked for in the 4 South tags — `CER_BY_SCRIPT.md` shows 43 of 126 scored South pages are Latin-dominant, which is a *different* mixed-script population (English inside a Tamil book) with different physics. I did not measure it: `level2/out/` predictions exist but I did not verify their join keys.
3. **Whether a *learned* router closes the residual gap.** After the `sa` abstention cell is fixed, the residual oracle gap is **0.0182** on the 268 non-abstained 300-sample items, and all five cheap rules I tested capture at most 24% of it. UNKNOWN whether a trained per-language router (in scope for W6, out of scope for W1) captures it. This is the only version of C2 that might survive, and it is not a 300-line rule file.
4. **`doctr`'s 1,225 "mismatch" flags are not signal** (0.828 match vs 0.870 mismatch, n=1 vs 1,225). I do not know whether `doctr` is emitting Latin, garbage punctuation, or truncated Devanagari. My profile split said 0/3,000 predictions are Latin-only, which contradicts my expectation for `doctr` and I did not resolve it — my `sc()` returns `None` for digits and ASCII punctuation, so a numeric or punctuation-only output lands in the `other` bucket with only 348 members. **My "other" bucket may be under-counting Latin.** The conclusion (validity-argmax is worse) does not depend on it, but the profile table in §C2 M2.3 should be read with that caveat.
5. **The `ur` Devanagari (n=1) and `or` Bengali (n=1) contamination cases.** I did not open the items to decide whether they are loanwords, OCR artefacts, or bilingual content. They are below any gate threshold and I did not chase them.
6. **Whether the 18 mr items are genuinely "tables".** The sheet's `has_table` column says `False` for all 79. My Latin-share evidence is strong (7.4×) but I did not open a page image to confirm. If they are tables, `mr` needs a table-aware sub-score and the gate is doubly wrong. If they are not, the confound needs a new name. **This is the single thing I would check first before anyone acts on C4.**
7. **ArXiv 2607.00250 §3 ablation (+0.00386, CI 0.00266–0.00517, p<0.0001 for the diacritic-restoration gate).** I opened the abstract only. The abstract says "lexicon-gated" and "Maltese diacritics and hyphenation"; the 1E report's characterisation of a "diacritic-restoration gate" as the largest contributor is from the paper body, which I did not read. DERIVED-FROM-ABSTRACT, not PRIMARY.
8. **The falsifier I did not run.** A ruleset that also penalises non-Bramic and empty output (add ~4 rules) would stop preferring `doctr`, and might land somewhere between 0.4190 and 0.6766. I did not test it because C2's thesis is a *Brahmic akshara* verifier; if the boss wants a 0.5-hour extension, that is the experiment. I expect it to land at ≈ surya_fixed (no gain) because M2.7 shows the gap is empty-strings, but I have not measured it.
