# W1E — LENS C: **IT CANNOT BE BUILT IN TIME** (adversarial, feasibility + window)

Agent: lens-C (feasibility kill). Run 2026-09-29 21:37–21:52 IST. **Read-only on the repo; this file is the only thing I wrote.**
Law: every number below carries a command I ran on this disk, with set, n and metric. I ran no engine, called no Sarvam, downloaded nothing, trained nothing, edited no repo file.
Analysis scripts lived outside the repo at `/var/folders/…/T/opencode/1Ec/{load,cer2,fusion}.py`. The `load.py` re-implements Unicode-block segmentation (`unicodedata` + an explicit block table); `cer2.py` imports the repo's own `level2/probe22/metrics.py` by path.

**Verdict line, up front, because three of the four theses rest on numbers I could not reproduce:**

| # | Thesis | Claimed | **Measured** | Verdict |
|---|---|---|---|---|
| C1 | Script-block attribution | sat is 54.3% Ol Chiki; floor 0.457; best engine 0.459 — "the same number" | sat is **0.4331** Ol Chiki; floor **0.5669**; best local sat CER is **0.6514**; **0 Ol Chiki chars emitted by any of 10 local engines** | **REFUTED** |
| C2 | Akshara-validity-gated fusion | oracle 0.4277 vs best single 0.5229 (−0.095, "the edge") | gap is real but **67% of it is one language (`sa`)**; cross-language gap is **0.0332** | **WOUNDED → REFUTED as stated** |
| C3 | Script-mismatch as free abstention signal | 1 day; surya 0.313 match vs 0.963 mismatch | match 0.2382 / mismatch 0.6676 (n=886); the 0.963 has **zero rows** behind it; surya routing gain is **−0.0351 (negative)**; abstain rate **already published 2026-09-28** | **REFUTED** |
| C4 | GT script-purity gate | 0.5 day; 18/79 mr; 645 Ol Chiki chars; +0.098 | 18/79 ✓ but **64 chars, not 645**; **arithmetic ceiling of the claimed cause is +0.00324 vs observed +0.4356 — off by 134×** | **REFUTED** |

Net: **0 of 4 survive as stated.** One salvage (C3's median column) is a 2-hour reporting change, not a day of engineering. Ranking and the "what would I actually do" answer are at the end.

---

## A FINDING THAT PRICES ALL FOUR: the scored `CER` column is not reproducible from the repo's own scorer

Before any of the four can land a number "beside page CER", it has to land a number on the *same scale* as page CER. It cannot.

Command (400 rows sampled from `level2/probe22/sheet.csv`, `random.seed(0)`), comparing my re-computed CER against the stored `CER` column using three flag combinations of the repo's own `metrics.py`:

| normalisation path | exact match on stored CER |
|---|---|
| `preprocess(normalize=True)` + `calculate_cer` | **156/400 (39.0%)** |
| `preprocess(replace_n=True)` | 128/400 |
| raw / NFC / NFKC∘NFC | 2–6/400 |

The real Phase-6 scorer is `level2/probe22/scores/score_engine.py` (which also applies a validity filter — `score_tesseract_indic.log` reports `valid_n 1056` of 1227, `loop_n 148`, `short_gt_n 27`, `overall_cer 0.4870`). I could not locate the code that emitted `sheet.csv`'s `CER` column; `error_tag` appears in no `.py` in the repo.

**Consequence, unpriced in every thesis:** a per-block CER (C1), a gated/fused CER (C2) and a filtered mr CER (C4) will be computed on a *different normaliser* from the published leaderboard, and cannot be placed in the same column without a visible discontinuity. Discovering this is not free: it is a half-day of archaeology at minimum, and if `score_engine.py` is the intended scorer then the 1,227-row sheet and the 10,560-row `valid_n`-filtered leaderboard are two different denominators, which is a **question for Vinay, not a coding task**.

This alone is worth more to tomorrow's meeting than all four theses combined, and it is 0 days of new engineering — it is one Verdict question.

---

## C1 — SCRIPT-BLOCK ATTRIBUTION

**Verdict: REFUTED.** Not on cost. On payoff: the thing it is built to prove is already measurably false.

### The measurement

`sat` in the scored set is **n=20** (`sheet.csv`, 20 rows × 10 engines). Character-level block composition of the 20 GT strings, 4,052 chars total:

| block | chars | share |
|---|---|---|
| OLCHIKI (U+1C50–1C7F) | 1,755 | **0.4331** |
| BENGALI (U+0980–09FF) | 1,308 | 0.3229 |
| **LATIN** | **953** | **0.2353** |
| DEVANAGARI | 26 | 0.0064 |
| PUNCT | 10 | 0.0025 |

The same on the 20 manifest `sat` items: 0.428. **The hunt's "54.3%" does not reproduce on either set.** Three consequences:

1. The claimed floor `1 − 0.543 = 0.457` is wrong. The true floor for an engine that reads Ol Chiki perfectly and is silent on everything else is **`1 − 0.4331 = 0.5669`**.
2. The claimed "best local engine on `sat` scores 0.459" **does not exist.** Stored `sheet.csv` sat means, n=20 each: `indicphotoocr 0.6514`, `surya 0.7621`, `doctr 0.8683`, `tesseract_indic/tesseract_bilingual/openbharatocr 0.8785`, `easyocr 0.8885`, `rapidocr/anuvaad_tesseract/paddleocr_indic 1.0000`. There is no value between 0.0265 and 0.4773 in the whole sat column.
3. Therefore **the cell is not saturated — it has 0.085 CER of measured headroom** against perfect-Ol-Chiki. The thesis's central sentence ("the monolingual floor and the observed score are the same number") is the exact inverse of the truth.

### The payoff is worse than that

**Not one of the 10 local engines emits a single Ol Chiki character on any of the 20 scored `sat` items.** 200 engine-item pairs, 0 characters emitted, against 1,755 in GT. `CER_olchiki` would read **1.0000 for all ten**.

The claimed value was "the one place we can prove an engine reads Ol Chiki." The measurement says: none of them do, and the metric would be a one-line restatement of a fact already on disk — `level2/probe22/scores/abstention_audit.md` §3, "Surya sa=100% Honest-Empty — CORRECT … Surya 2 has NO Ol Chiki support", and directive defect **K6**.

The three Sarvam rows make the rest of it concrete (`sarvam_vision`, 3 items, cap spent):
- `sat_05` — transliteration, 46 Ol Chiki → 46, 43 Bengali → 42, **24 Latin → 24**. CER 0.0265.
- `sat_13` — GT 50 chars, prediction **500** chars, Ol Chiki 40 → **265**. A 10× length explosion, CER 1.0.
- `sat_15` — Ol Chiki 32 → **5**, Bengali 28 → **54**. It dropped Ol Chiki and hallucinated Bengali. CER 0.4054.

So n=3, one clean row, one explosion, one script swap. The hunt itself flags this as "directional only". It is also the only place the claim could have held, and it is held by the model we are not allowed to call again.

### The build, honestly costed — 1 day is roughly right, which does not save it

Steps: (1) block-segment GT and prediction, ~half a day, but the two must be **aligned**, and they are not. `sat_05` is one sentence in three parallel renderings (Ol Chiki, Bengali, Latin), so a per-block CER asks "did you get the Ol Chiki half right", which **rewards an engine that reads one script and ignores two**. The correct unit is the parallel *line*, which needs line detection, not block segmentation — a different build. (2) Decide the alignment failure mode, (3) re-score, (4) table, (5) Verdict pass. **1.5–2 days for a defensible artefact**, 1 day for a block-level one that is semantically wrong on the only data that motivated it.

Scope, if generalised beyond `sat`: **220 of 1,227 GT strings have >1 substantial non-Latin block.** 204 two-block, 16 three-block, 274 have none, 733 have exactly one (so per-block ≡ page, no information). Of the 220, **154 are `pa` (81) and `bn` (77)** — and the hunt's own F2 note concedes `pa` 88/90 items carry Devanagari-*block* chars that are only the dandā `।` U+0964, which Gurmukhi legitimately uses. So 37% of the multi-block set is a punctuation artefact that needs a whitelist before it can be scored at all. Genuinely bilingual: **~66 items** (`mr` 23, `or` 16, `sat` 16, `as` 5, `gu` 1, `kok` 1). That is a 66-item appendix, not a leaderboard row.

**Approvals:** no download, no training, no boss decision. A new script under `level2/unified/` (where 1B put `build_benchmark_22.py`) is the only friction, and two OpenCode processes are live in this repo. **Latency: zero** — it is the cheapest thing on this list, and it buys a column of 1.0000s.

**Displaces:** nothing from D14/D15/D16 if scoped to `sat` only. At 1.5–2 days it displaces **D15 `MULTI_LLM_EVAL.md` in full** — one of the two things the lead explicitly asked for and which does not exist on disk (directive A2 A3, "NOT DONE").

**Single best counter-argument (for it, stated at its strongest):** *"It is honest-negative, it is 1 day, and a CEO respects a team that measures a cell properly and reports the cell is dead."* My answer: that honesty is already available **for free** — "no local engine emits Ol Chiki; `sat` is structurally dead; Sarvam is the only reader and it failed 2 of 3" is a **two-line paragraph in the packet**, and it is stronger as a paragraph than as a table of tens. The build is spent on presentation, and the presentation is the part the founder is short of time for.

---

## C2 — AKSHARA-VALIDITY-GATED FUSION

**Verdict: WOUNDED → REFUTED as stated.** The ceiling is real; the thesis mis-states where it lives, and the mechanism has no measured chance against what is left.

### The ceiling is real — credit where due

Seeded sample `random.seed(20260926)`, 300 items, stored `sheet.csv` CER, 10 local engines:

| set | best single | oracle (per-item min) | gap |
|---|---|---|---|
| 300-item sample, 10 engines | surya 0.4190 | 0.3213 | **+0.0977** (+23.3% rel) |
| **full 1,227**, 10 engines | surya 0.3944 | 0.2947 | **+0.0997** (+25.3% rel) |

The magnitude reproduces. (Absolute values differ from the hunt's 0.5229/0.4277 — likely a different id ordering — but the *gap* is 0.098 vs their 0.095, and the gap is the claim.) I also checked the obvious attack and it **fails**: three of the ten engines are near-duplicates, but min-over-duplicates is idempotent, so dropping them moves the gap 0.0977 → 0.0976.

Incidental correction worth logging: **directive A8's "tesseract_bilingual ≡ tesseract_indic" is wrong on this set.** Byte-identity of prediction strings over 1,227 items: `tesseract_indic` ≡ `openbharatocr` **1225/1227**, but `tesseract_bilingual` only **370/1227**. It is a distinct engine.

### But the gain is one language, and it is a documented engine bug

Per-language decomposition of the 300-sample gap (oracle − surya), contribution to the mean:

| lang | n | surya | oracle | gain | ×(n/300) |
|---|---|---|---|---|---|
| **sa** | 24 | **1.0000** | 0.1565 | **−20.2434** | **−0.1619** |
| kok | 26 | 0.4502 | 0.3811 | −1.7957 | −0.1556 |
| brx | 16 | 0.2034 | 0.1120 | −1.4634 | −0.0780 |
| doi | 6 | 0.4553 | 0.2137 | −1.4493 | −0.0290 |
| hi | 22 | 0.3177 | 0.2997 | −0.3973 | −0.0291 |
| mr | 14 | 0.3366 | 0.2626 | −1.0352 | −0.0483 |
| or | 17 | 0.2856 | 0.2303 | −0.9393 | −0.0532 |
| *(14 others)* | | | | | **+0.0642** |

**`sa` alone contributes 166% of the total gain; the other 17 languages together are a net −0.064.** Remove `sa` and the fusion thesis inverts:

| set | best single | oracle | gap |
|---|---|---|---|
| full 1,227, all langs | 0.3944 | 0.2947 | +0.0997 (+25.3%) |
| **full 1,227, excluding `sa`** (n=1,127) | 0.3407 | 0.3074 | **+0.0332 (+9.8%)** |
| 300 sample, excluding `sa` (n=276) | 0.3684 | 0.3356 | +0.0328 (+8.9%) |

And what `sa` is: surya scores **CER 1.0000** on all `sa` rows because it returns nothing — `abstention_audit.md` §3 already diagnosed it, and directive defect **K6** already records the mislabelling. So the "fusion ceiling" is *a known surya coverage bug on one language, which any of eight other engines happens to read.* Fix the bug by routing `sa` to any tesseract, and the fusion opportunity **evaporates** — no verifier required.

**The honest headline is: the cross-language fusion ceiling is 0.033 CER (9.8% relative), not 0.095 (18–25%).** The thesis overstates its own prize by ~3×.

### Against a 0.033 ceiling, the mechanism has to beat the anchor, not the oracle

The only measured implementation is ROVER-lite at 0.5519 — **worse than the anchor**. The proposed akshara verifier is unbuilt, and its job is to turn a 0.033 opportunity into a positive delta while the measured prior is **−0.06**.

### Honest build cost

Steps: (1) multiple-sequence alignment across 10 streams of unequal length — the hunt's `difflib` opcode alignment is a stand-in, and it is where ROVER-lite failed; (2) per-script rule set. **This is the hidden 2 days.** A validity rule is per-script and the data is 18 scored languages. Conjunct stacking (`ক্ষ`, `শ্র`, `জ্ঞ`) needs cluster segmentation, not codepoint rules; Perso-Arabic is ZWJ/ZWNJ-dependent in ways a terminal-virama rule does not model; Nastaliq is contextually re-ordered; and the four scripts where fusion would matter most (`mni`, `sat`, `ks`, `ur`) are exactly the ones with **no trained data and no tessdata** (hunt F6: 12 traineddata files, no `mni`, no `sat`/`ol_chiki`, no `kan`/`mal`/`tam`/`tel`) — a rule set there is guesswork. Writing 22 scripts of cluster rules that are individually correct and jointly *not* shredding valid conjuncts is 3–5 days of the kind of work that surfaces 3 hard bugs per script. (3) Gate + plurality-without-quorum abstention and a false-abstain rate. (4) Re-score. (5) Verdict pass.

**4–5 days for 22 scripts. 2 days is a 3-script demo.**

Re-scoring cost on an M2 Max: not the bottleneck and the thesis is right about that — the stored CERs already exist, so scoring a fused string over 1,227 items is stdlib Levenshtein on existing predictions, **minutes, not hours**. Memory is not the constraint. **The bottleneck is the rules and the alignment, and neither is a compute problem.**

**Approvals:** no download, no training, no boss decision for the *research* prototype. But any deliverable that touches `sheet.csv` or `level2/probe22/scores/` is inside **U5** (unanswered) and hits the cross-check law (Verdict must sign off before it counts). **Latency: 0 for a prototype, boss-dependent for anything that changes a published number.**

**Displaces:** 4–5 days is **the entire window**. It displaces D14 (done, 21:14), D15 (missing, lead's ask), D16 (missing, **the thing the boss presents tomorrow**), 1G and 1H. Not a trade — a cancellation.

**Single best counter-argument (for it):** *"The 0.033 is a real 9.8% relative improvement on 18 languages and no one in the field is doing it; ship the 3 scripts that matter and label the rest."* My answer: that is a **W2/W3 item after the freeze**, because the honest one-line version — "an akshara-validity-gated vote is the only mechanism we found plausibly worth the cross-language fusion gap" — is a *perfect* sentence for the research plan D16, and it costs **zero days** as prose. The engineering is what cannot be afforded, not the idea.

---

## C3 — SCRIPT-MISMATCH AS A FREE ABSTENTION SIGNAL

**Verdict: REFUTED.** Half of it is already on disk; the other half has a negative payoff; the "1 day" is not honest.

### What reproduces, and it is good

Abstention over all 12,324 rows — **exact match to the hunt**:

| engine | empty % | mean CER | median CER | ≥0.999 % |
|---|---|---|---|---|
| surya | 10.5 | 0.3944 | 0.3058 | 13.2 |
| rapidocr | 28.0 | 0.6753 | 0.7577 | 28.3 |
| paddleocr_indic | 43.7 | 0.6629 | 0.9241 | 44.3 |
| anuvaad_tesseract | 50.3 | 0.7153 | 1.0000 | 54.8 |
| indicphotoocr / tesseract_* / easyocr / doctr | 0.0–0.2 | 0.49–0.87 | — | 1.6–8.3 |

This is the one clean, well-powered claim in the set. **It is also already delivered**: `level2/probe22/scores/abstention_audit.md`, dated 2026-09-28 18:00 IST, Verdict agent, Santa-method hostile pass, §1 engine-by-engine empty table, §2 per-language table (n≥50), §3 LOW-COVERAGE flags. `scores/LEADERBOARD.md` carries an "Honest-empty" column per engine. Rule 0.7: past work is gold; do not re-litigate finished work.

### What does not reproduce

The hunt reports "surya 0.313 (match) vs 0.963 (mismatch), n=1098". Under a real script check (Latin excluded — Latin is not a script signal, it is transliteration noise):

| engine | n non-empty | match n | match CER | mismatch n | mismatch CER |
|---|---|---|---|---|---|
| surya | **886** | 803 | **0.2382** | 83 | **0.6676** |
| tesseract_indic | 1,118 | 916 | 0.4138 | 202 | 0.6770 |
| indicphotoocr | 1,225 | 927 | 0.4529 | 298 | 0.9041 |
| easyocr | 883 | 802 | 0.4033 | 81 | 0.7013 |
| paddleocr_indic | 517 | 515 | 0.3062 | 2 | 0.3306 |
| anuvaad_tesseract | 610 | 610 | 0.4273 | **0** | — |
| rapidocr | 610 | 607 | 0.4421 | 3 | 0.4733 |
| **doctr** | **2** | 1 | 0.8282 | 1 | 0.8110 |

The gap is real but **half the size claimed** (0.238 vs 0.668, not 0.313 vs 0.963), on a different n (886, not 1098). And the mechanism of the discrepancy is worse than a number being wrong:

> With Latin **included** in the block set — which is the definition that produces the hunt's `n=1098` — the mismatch set is **empty for every single engine** (surya 1,098 match / **0** mismatch; tesseract_indic 1,224 / **0**; doctr 1,226 / **0**). The hunt's 0.963 mismatch mean is an average over **no rows**. The hunt's own UNRESOLVED admits the threshold is untested. A statistic that depends on an unspecified threshold, and reports a value for the empty side of that threshold, does not survive a room with a CTO in it.

**The 212 rows the feature is blind to.** Splitting surya's 1,227 rows four ways: `match` 803 (0.2382), `mismatch` 83 (0.6676), `empty` 129 (1.0000), and **`latin_only` 212 (0.5106)** — outputs whose only non-punctuation block is Latin. As specified, a Latin-only output on a Bengali GT is either "mismatch" (if you count Latin) or **no signal at all** (if you don't). **17.3% of surya's rows sit in a bucket the feature does not name**, and they are the second-largest failure mode after refusal.

### The routing payoff is negative, for the engine the thesis features

On the items where engine X's output script mismatches the GT script, what is the **best of the other nine** on the *same* items?

| engine | n mismatch | own CER | best other | **gain from routing** |
|---|---|---|---|---|
| **surya** | 83 | 0.6676 | 0.7027 | **−0.0351** |
| indicphotoocr | 298 | 0.9041 | 0.5505 | +0.3536 |
| tesseract_indic | 202 | 0.6770 | 0.5109 | +0.1661 |
| tesseract_bilingual | 203 | 0.6752 | 0.5081 | +0.1671 |
| openbharatocr | 202 | 0.6770 | 0.5109 | +0.1661 |
| easyocr | 81 | 0.7013 | 0.6131 | +0.0882 |
| rapidocr | 3 | 0.4733 | 0.1974 | +0.2760 |
| paddleocr_indic | 2 | 0.3306 | 0.2248 | +0.1058 |
| **anuvaad_tesseract** | **0** | — | — | **no signal** |

**For surya — the best engine, the one the whole report is built around — routing makes the score worse.** Only 20.7% of surya's mismatch items have any alternative below CER 0.5. The signal is real as a *detector* and useless as a *router*, because when surya fails this way the item is hard for everyone. That is the diagnosis, and it is one sentence: **it detects hard items, not bad engines.**

Honest counterweight: it *does* work for indicphotoocr (+0.354) and the tesseracts (+0.166). So there is a real, cheap oracle-routing result hiding here — **just not the one proposed, and not on the engine we lead with.**

### Is "report median instead of mean" a day or an hour?

An hour. `scores/build_leaderboard.py` has no `median` token; `scores/LEADERBOARD.md` has no `median` row. It is one `statistics.median` and one table column. **The 1-day estimate is dishonest for the part that is real, and the abstain half is 0 days because it is done.** Calling a 1-hour change "1 day of engineering" is how a 5-day window dies.

**But the median is not cosmetic, and that is the one thing here worth doing.** Per-language winners, mean vs median, 18 languages: **6 flip.**

| lang | mean winner | median winner |
|---|---|---|
| mr | tesseract_bilingual | **surya** |
| ne | tesseract_bilingual | **surya** |
| or | tesseract_indic | **surya** |
| gu | sarvam_vision | surya |
| as | indicphotoocr | **sarvam_vision (n=3)** |
| sd | surya | **sarvam_vision (n=3)** |

Two of those six are **n=3 Sarvam rows winning on median**, which violates locked decision **D4** ("n<50 = no winner"). **Any median column must carry the same n≥50 gate or it manufactures winners out of three samples** — and `BENCHMARK_22.md` is the artefact the lead reads tomorrow. Three flips among local engines is a genuine robustness caveat worth one sentence.

**Approvals:** median column = edit `scores/build_leaderboard.py` (not sealed; truth-bearing; needs Verdict sign-off per the cross-check law). **Latency: same day, no boss decision.** Abstain rate: **0 days, already published.**

**Displaces:** 2 hours. Nothing.

**Single best counter-argument (for it):** *"Median + abstain-rate is the reporting standard in the one 2026 paper that measured this class of engine, and reporting mean-only is how we got K1 — a 'beats Sarvam 9/18' claim built on n=3."* My answer: **this is right, and it is 2 hours.** Report it as a correction to K1's own denominator, not as a thesis. That framing is what makes it survive; the "free abstention signal" framing is what kills it.

---

## C4 — GT SCRIPT-PURITY GATE

**Verdict: REFUTED — and this is the one that would do actual damage.**

### The 18/79 is real. The 645 characters is not.

| quantity | hunt | measured |
|---|---|---|
| scored `mr` items with Ol Chiki | 18 of 79 | **18 of 79** ✓ |
| Ol Chiki chars, scored 79 items | 645 | **64** |
| Ol Chiki chars, full 100-item manifest | — | 916 (35 items) |
| scored `mr` GT total | — | 39,500 chars |

Per contaminated item: **1 to 6 Ol Chiki characters inside a 500-character GT string.** `mr_o001` 5/500, `mr_o005` 6/500, `mr_o014` 1/500 … `mr_o099` 4/500.

### The mechanism is arithmetically falsified

A substituted character from a different block costs at most 2 edits (delete + insert). So the **maximum CER this artefact can possibly inject**, if every engine mis-copied every single injected character on every item:

```
2 × 64 / 39,500 = 0.00324
```

**Observed 18-vs-61 delta** (stored `sheet.csv` CER, clean = 61 items, contaminated = 18):

| engine | clean n=61 | contaminated n=18 | delta | 79-item mean |
|---|---|---|---|---|
| tesseract_indic | 0.1055 | 0.5411 | **+0.4356** | 0.2047 |
| tesseract_bilingual | 0.1053 | 0.5409 | +0.4355 | 0.2046 |
| openbharatocr | 0.1055 | 0.5411 | +0.4356 | 0.2047 |
| easyocr | 0.1087 | 0.5464 | +0.4377 | 0.2084 |
| surya | 0.1196 | 0.5396 | +0.4200 | 0.2153 |
| rapidocr | 0.2011 | 0.6173 | +0.4162 | 0.2959 |
| anuvaad_tesseract | 0.1888 | 0.5556 | +0.3668 | 0.2724 |
| paddleocr_indic | 0.1179 | 0.5372 | +0.4193 | 0.2134 |
| indicphotoocr | 0.2707 | 0.5749 | +0.3042 | 0.3400 |
| doctr | 0.8468 | 0.8728 | +0.0260 | 0.8528 |

**+0.4356 observed against a +0.00324 ceiling: the claimed cause explains 0.7% of the effect — off by a factor of 134.**

The `+0.098` figure is the right *arithmetic* on the wrong *cause* (`18/79 × (0.54 − 0.11) = 0.098`), and it matches the size of the mr effect. But the script artefact is not what produces it. The 18 items are simply harder content, and a script-purity gate would remove **0.003 of the 0.098** it claims. The hunt has attributed a 0.44 gap to a 0.003 cause.

### Why this is the dangerous one

`docs/campaign/BENCHMARK_22.md` (D14, written 21:14 tonight, the lead's explicit ask) line 104 publishes:

> `| mr | Marathi | 79 | 0.215 / 0.019 | … | 0.205 / 0.027 | … | 0.213 / 0.039 | … | 0.248 (n=3) |` … **`tesseract_bilingual` 0.205**

Drop the 18 items and `mr` goes **0.205 → 0.1055**. A **−0.10 improvement in our own published number, in our best-looking language, the night before cross-examination, via a filter whose stated justification I have just shown to be off by 134×.**

If Vinay's engineer recomputes one thing it will be this. The answer we would have to give is: *"we removed a fifth of our Marathi items on the night before the meeting because a script filter told us to, and the filter was wrong."* There is no version of that which helps us.

And the correct filter is not a script filter anyway — the 18 items differ by **content difficulty**, not by script purity, and a difficulty filter that drops your worst 23% of a language is **score cherry-picking**, not measurement. It also would not be honest to present it as GT hygiene.

### Governance: it is blocked twice over

- `sheet.csv` is **LOCKED**. Scoring changes are **boss decision U5**, which is unanswered (`docs/campaign/protocols/proto-92-boss-decisions.md`: "Score the 56 manifest additions … changes the LOCKED `sheet.csv`"), and `docs/campaign/checkpoints/W1.md` records **"STOPPED BY BOSS 2026-09-29 ~21:05 IST … No step is DONE."**
- `AGENT_PROTOCOL.md` and `run_probe.py` are on the **CANNOT-apply list** (`OCR_AGENT_MEMORY_FEED.md` §1 ops model, lines 788 / 877 / 890), and the sampling gates that generated `mr` live in `AGENT_PROTOCOL` (feeds §9 forbids lowering them).
- Directive A7 seals `level2/out/`, `level2/reports/`, `level2/probe22/out/`. `sheet.csv` is outside those, so the *filesystem* would permit it. **The permission is what is missing.**

So: the thesis requires a boss decision that has been explicitly deferred ("yes, AFTER the meeting — not tonight") to authorise a change that **raises our own headline number**, justified by a mechanism that is false. That is the exact shape of request a CEO should refuse, and the answer should be no even if the arithmetic had been right.

**Approvals:** boss decision **U5** (unanswered; latency unbounded — the boss stopped the wave at 21:05) **plus** an explicit "we may lower our own scores" authorisation, which is a different and much harder yes. **No download, no training.** Even with approval this is a **post-meeting (W2) item**, and it must ship as *"we found our mr cell is bimodal by item difficulty"* — not as a script-purity gate.

**Displaces:** 0.5 day of a window that has D15 and D16 missing. It is the *worst* use of the 5 days on the list.

**Single best counter-argument (for it):** *"The contamination is real — 64 wrong characters in locked GT is still wrong — and it is 0.5 day to flag, and a gate stops the same pipeline adding more."* My answer: the *flag* is 20 minutes and correct, and it belongs in the sampling plan as one line — but flagging is not re-scoring, and the +21 `mr` additions do raise the count. **Ship the flag to W2, refuse the re-score, and do not put a "we cleaned our data" line in a packet that is being cross-examined tomorrow.**

---

## RANKING BY EXPECTED VALUE PER DAY OF THE FOUNDER'S SCARCEST RESOURCE

The scarce resource is not compute — it is the ~5 days of one operator who is simultaneously holding D14, D15, D16, 1G and 1H, and who presents to his CEO on 2026-09-30.

| rank | thesis | EV/day | why |
|---|---|---|---|
| **1** | **C3, the median + abstain-rate half only** | **very high** | ~2 h. Corrects K1's own denominator. 6/18 per-language winners flip on median; 2 of those flip to n=3 Sarvam and **violate D4** — so the fix has real content and a real trap. The abstain half is already delivered; the honest claim is the *reporting correction*, not a new signal. |
| **2** | **C1, `sat` only, paragraph not table** | **medium, as prose** | 0 days: "no local engine emits a single Ol Chiki character across 20 `sat` items (0 vs 1,755 in GT); Sarvam read it on 1 of 3 and hallucinated it on another." That is a better slide than a table of 1.0000s. As engineering (1.5–2 d) it is a miss. |
| **3** | **C2, as a sentence in D16** | **medium, as prose** | 0 days. "An akshara-validity-gated vote is the only mechanism we found plausibly worth the cross-language fusion gap (0.033, 9.8% rel, ex-`sa`)." The engineering (4–5 d) is a W2/W3 item after the freeze. |
| **4** | **C3's routing half / C2's verifier** | **low, as engineering** | surya routing gain is **negative** (−0.0351). Mechanism measured worse than the anchor. |
| **5** | **C4** | **negative** | Refuted 134×, blocked by U5, and moves our own number in our favour the night before a competitive meeting. |
| — | **The `sheet.csv` CER-reproducibility question** | **highest of all, and 0 days** | 39% match against the repo's own scorer, and two candidate denominators (1,227 rows vs `valid_n 1056`). This is a Verdict question, not engineering — and it is the only item on this list that could change what we *say* in the meeting tomorrow. |

### What I would actually attempt in this window

**Two hours, not a thesis: add `median_CER` and `abstain_rate` to `scores/build_leaderboard.py` and to `BENCHMARK_22.md`, gated on the existing D4 n≥50 rule so no n=3 Sarvam row can win on median.** One-line caveat on the table: *"per-language winner differs under mean vs median in 6/18 cells; 2 of those are n=3 and carry no winner claim."* That is a robustness disclosure that a CEO respects, it costs 2 hours of a 5-day window, and it displaces nothing.

**Zero days, in prose:** the `sat` finding as a paragraph (0 Ol Chiki chars from 10 local engines), and the fusion finding as a correctly-scoped sentence in D16 (cross-language ceiling 0.033, not 0.095; 67% of the raw gap is the `sa` surya bug already logged in `abstention_audit.md` §3 and directive K6).

**One question, to the boss or to Verdict, before anything else:** *which code produced the `CER` column in `sheet.csv`, and is the intended denominator 12,324 rows or the 10,560 valid rows?* Until that is answered, no new metric can be placed beside an old one, and that blocks C1, C2 and C4 equally.

**Not attempted:** C1 as a build, C2 as a build, C3's routing, and C4 in any form before U5 is answered.

---

## UNRESOLVED

1. **The scorer for `sheet.csv` is unidentified.** Best reproduction 156/400 (39.0%) using `metrics.py` `preprocess(normalize=True)` + `calculate_cer`. `error_tag` appears in no `.py` in the repo. `level2/probe22/scores/score_engine.py` exists and reports `valid_n 1056 / loop_n 148 / short_gt_n 27` for tesseract_indic, but I did not establish that it wrote `sheet.csv`. **UNKNOWN and load-bearing for C1, C2, C4.**
2. **Two denominators are in circulation** — 12,324 `sheet.csv` rows and the `valid_n`-filtered 1,056-per-engine leaderboard. I did not determine which `BENCHMARK_22.md` uses for each column.
3. **The Ol Chiki share of `sat` is 0.4331 (scored) / 0.428 (manifest), not 0.543.** I did not find what produced 0.543. A 3-item or single-item measurement is the likely origin; `sat_05` alone is not it (Ol Chiki 46/113 = 0.407). **UNKNOWN provenance of the 54.3% figure.**
4. **Why the 18 `mr` items score 0.44 worse is UNKNOWN.** I proved it is not the 64 Ol Chiki characters. Candidates not excluded: page/scan quality, source-PDF tier, or text density. I did not inspect the images (no visual verification run, and `visual_verify` is out of scope for this lens).
5. **All 79 scored `mr` items are `mr_o*` (`set: official_pdf`, `gt_source: official_pdf_layer`)** — there is no 61-item "clean" *provenance* set, only a 61-item "no Ol Chiki" set. Whether the 18 are a different scan tier is untested.
6. **Directive A8's engine-equivalence claim is partly wrong and I did not finish the audit.** Measured: `tesseract_indic` ≡ `openbharatocr` 1225/1227 prediction strings; `tesseract_bilingual` only 370/1227. I checked predictions, not weights or configs, and did not check the other 7 engines for pairs.
7. **`latin_only` (212 surya rows, CER 0.5106) is undefined in the proposed feature.** Whether it should count as mismatch, match, or abstain is a design choice the thesis never makes, and it moves the surya numbers materially.
8. **The `sa` decomposition was done on the stored CER, which is itself unexplained (item 1).** If the stored CER is filtered, the sa-vs-rest split could shift. The sa surplus is large enough (166% of a 0.098 gap) that I doubt it flips, but I have not checked.
9. **`indicphotoocr` routing gain +0.3536 is real and unexploited.** n=298 mismatch items. I did not check whether those 298 overlap `sa`/Devanagari coverage gaps, which would explain it without any routing merit. **An oracle-routing result may be sitting here and it is not the proposed thesis.**
10. **Per-language median flips: 6/18.** Two are n=3 Sarvam (D4 violation). I did not test whether the local-only flips (mr, ne, or) survive a bootstrap or are within sampling noise on n=37–79.
11. **`sats` multi-block scope is 220/1,227 items, of which 154 are `pa`/`bn` Devanagari-dandā artefacts.** I did not implement the punctuation whitelist the hunt recommends, so the ~66 genuinely bilingual items are an upper bound.
12. **The boss has not resumed the wave.** `docs/campaign/checkpoints/W1.md` ends `STOPPED BY BOSS 2026-09-29 ~21:05 IST`. This report was produced against a stopped campaign; if the stop holds, the only live item is the `sheet.csv` question, and it is a question, not a task.
13. **`src/` (U3) and the Sarvam cap (57/57) were untouched by this lens.** I ran no engine, made no API call, and opened no `src/` file.

---

### Files and commands relied on

- `docs/campaign/CAMPAIGN_DIRECTIVE.md` — Part A (lines 19–117), Parts B/C/D/E
- `docs/campaign/checkpoints/W1.md` (STOPPED 21:05, U1–U5 pending) · `docs/campaign/protocols/proto-92-boss-decisions.md` (U5) · `proto-00-runbook.md:20,43` · `proto-19:35` · `proto-21:38,42,44` · `proto-50:36` · `proto-51:19`
- `docs/campaign/checkpoints/W1_reports/1E_hunt.md` (the source of C1–C4)
- `docs/campaign/BENCHMARK_22.md:104,131,247,291` (mr 0.205 published; winner declared)
- `level2/probe22/sheet.csv` — 12,324 rows, 10 engines × 1,227 + 54 Sarvam (verified by `csv.DictReader`, `Counter(model)`)
- `level2/probe22/manifest.json` — 1,283 items (20 sat, 100 mr)
- `level2/probe22/metrics.py:128-146` (`normalize_for_metrics`/`normalize_for_scoring`), `:381-404` (`preprocess`), `:494-560` (`is_loop_or_catastrophic`, `calculate_cer`, `edit_distance`)
- `level2/probe22/scores/score_engine.py:18,54,97,490,552` · `scores/abstention_audit.md` §1–§3 (2026-09-28 18:00 IST) · `scores/LEADERBOARD.md:3,12,22,63,115,116,126,174` · `scores/build_leaderboard.py` (no `median`/`abstain` token)
- `level2/probe22/logs/score_tesseract_indic.log` (`valid_n 1056`, `loop_n 148`, `overall_cer 0.4870`)
- `OCR_AGENT_MEMORY_FEED.md:788,877,890` (CANNOT-apply list) · `level2/unified/build_benchmark_22.py:1-50`
- Scripts (outside the repo): `/var/folders/…/T/opencode/1Ec/load.py` (block segmentation), `cer2.py` (repo metrics import + CER), `fusion.py` (oracle/vote)

### Commands that produced the numbers above

`csv.DictReader(sheet.csv)` → 12,324 rows; `Counter(model)` → 10 × 1,227 + 54; block composition of unique GT by `image_id` (1,227) for `sat` and `mr`; stored-`CER` per-language and per-engine means/medians/emptiness; `random.seed(20260926); random.sample(sorted(ids),300)` for the fusion sample; `min()`-oracle over 10 and 8 engines with and without `sa`; per-language gap decomposition; `difflib`-free routing test (`min` of the other 9 engines' stored CER on the same `image_id`); block-set match/mismatch with Latin in and Latin out; `statistics.median` per-engine and per-language winner comparison; 400-row CER reproduction against three `metrics.py` normalisation paths. Metric definition for all CER figures: the **stored** `CER` column of `sheet.csv` unless explicitly labelled as recomputed.
