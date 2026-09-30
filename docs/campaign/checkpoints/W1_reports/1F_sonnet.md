# 1F — independent senior review of `DRAFT_RESEARCH_PLAN.md`

**Reviewer:** fresh hostile reviewer, Sonnet session. **Date:** 2026-09-30. **Basis:** the plan plus the four permitted evidence files only. No 1A/1G/fix-spec/DISPATCH_LOG was opened. All arithmetic below is recomputed, not copied.

**Bottom line up front.** The plan is unusually honest and has no plan. Its own Option A risk cell reads *"no accuracy gain at all; a presentation win"* (plan:129). It recommends the concession and asks the CEO to accept a weaker headline. That is the correct level of candour and the wrong level of strategy. Separately, the plan's single most important ask — the only edge it claims — is **scoped in a way that would deliver nothing if approved as written**, and the headline "2.5× behind" is **~62% attributable to two languages in which no local engine can emit a character at all**. Both are below, with the arithmetic.

---

## 1. The five most serious weaknesses

### W1 — The human-verified comparison is 62% a coverage gap being reported as an accuracy gap

The plan's one-liner (plan:95) is *"on the 18 human-verified items where Sarvam ran, Sarvam's CER is 2.5× lower than our best local engine (0.171 vs 0.430)"*.

The plan does not say which 6 languages those 18 items come from. It is reconstructable from its own tier table, and the reconstruction is exact:

- gold tier `official_pair_txt`, n=9 → 3 languages × 3 = **bn, hi, sa** (plan:91 states "bn/hi/sa").
- fill tier `sarvam_bench`, n=9 → 3 languages × 3. Solve for the third from the printed tier mean: `3·x = 9(0.278) − 3(0.0230) − 3(0.4773)` → `x = 0.3340`. That is **Assamese's paired Sarvam CER 0.3339** to four decimals. Tier = **as, mni, sat**.

So the human-verified set is **bn, hi, sa, as, mni, sat** — and **two of the six are the two dead-script languages** the plan's own §6 (plan:141) says no local engine can read, and that the plan's own Q5/Q6 propose fixing with one file.

Recomputing the same comparison with the two dead-script languages removed (12 items: bn, hi, sa, as):

| | Sarvam | best local | ratio | pp gap |
|---|---:|---:|---:|---:|
| as published (18 items, 6 langs) | 0.1710 | 0.4300 | **2.51×** | 0.259 |
| ex-`mni`+`sat` (12 items, 4 langs) | 0.1315 | 0.2295 | **1.75×** | **0.098** |
| surya instead of best-local (18 items) | 0.1710 | 0.6325 | **3.70×** | 0.462 |

**Concrete failure:** the plan hands a CEO a bold "we are 2.5× behind" and, three pages later, a one-file fix for the condition that causes 62% of that gap. The CEO will either (a) treat the project as 2.5× behind and demote it, or (b) discover the confound and discount the entire document. Both outcomes lose the week. The number is not wrong — it is **uninterpretable without the two-line qualifier that the plan does not print**, and "2.5×" is the single most likely sentence to be quoted back to the team.

Second-order: the plan's own 2-hour "median + abstention" recommendation (plan:131) is the direct remedy for this. It is listed in the plan as a nice-to-have on Day 1. It should be the first thing the CEO sees, because it is what makes the 0.430 interpretable.

### W2 — The only edge is mis-scoped by 3× in languages and 5–8× in size, and the plan says so about itself in one place and the opposite in another

- plan §6, line 141: *"`tessdata/` has none of `sat`, `mni`, `kan`, `mal`, `tam`, `tel`."*
- plan Q5, line 159, **bold**: *"**Scoped correctly: `tam`/`tel`/`kan`/`mal` traineddata is already on disk, so the download is only `sat` and `mni`.**"*

Verified on disk — `level2/probe22/tessdata/` contains exactly 12 files: `asm ben eng guj hin mar nep ori pan san snd urd`. **No `tam`, `tel`, `kan`, `mal`, `mni`, `sat`.** The bold Q5 claim is false; §6 is right; the two contradict each other inside one document.

The size claim is also wrong by an order of magnitude. The 12 files already on disk are **8.0–15.4 MB, mean 11.6 MB** (measured). The plan asserts "~2–4 MB" in four places (plan:115, 143, Q5:159, §5:128 "one 2–4 MB file each"). The smallest traineddata on this machine is 8.0 MB. Six languages at the observed per-file mean is **~70 MB, not 2–4 MB**.

**Concrete failure:** a 2-4 MB, two-language, unverified ask gets approved in ten seconds and delivers two marginally-better cells on n=20 each. A ~70 MB, six-language, verified ask against a known-good source is a different decision that must be argued, and it covers `kan`/`mal`/`tam`/`tel` — three of the four thinnest South cells. The plan's framing has optimised the ask into uselessness. Note also that the resource itself is **UNVERIFIED** (plan:115: *"we did not open its file listing"*), which `EDGE_THESIS:36` flags as a pre-approval blocker the plan did not discharge — while the fix is a free, no-approval file listing, not a model download.

### W3 — "Best local" is a per-language argmin selected on the same items it is scored on, and it is the column compared to Sarvam

The plan applies "no claim without its n" (plan:20) to Sarvam, correctly, at length. It applies it to itself nowhere.

- 10 engines × 22 languages = 220 configurations. The plan reports the per-language **argmin** on the same items, with no held-out split, no selection correction, and **no confidence interval anywhere in the document**.
- The tier table's third column is **"best local per item"** — a per-item oracle over 10 engines, which no deployable system produces. The one-liner (plan:95) then labels 0.430 as *"our best local engine."* An oracle is not an engine. The plan itself knows this distinction: §6 (plan:145) uses the same oracle correctly and calls it an oracle, and reports the honest spread (1.75× to 3.70×, above). §3 collapses it.
- n ranges 5 to 100. Per-item CER is heavy-tailed with mass pinned at 1.0 (abstentions). The 8-of-22 no-winner-claim list (plan:81) is right, but 8 is the *stated* floor — the 12 languages with n=50–100 still have no interval.

**Concrete failure:** the plan's entire "we lead on PDF-layer GT" claim rests on a winner chosen from 10 engines on the same rows. With 10 candidates and n=69–100, the argmin mean is biased low by roughly the inter-engine spread. A judge who spots this rejects the whole table, including the parts that are correct. The fix is one bootstrap CI per cell and a leave-one-engine-out selection check — hours, not days, and it is nowhere in the 5-day plan.

### W4 — "12 languages qualify" silently drops Tamil, four rows after the plan's own table says 13

plan:79 prints **"n ≥ 50 | 13 of 22"**. plan:83, two sentences later, prints **"Best local engine at n≥50 (12 languages qualify): surya 9, tesseract-family 2, easyocr 1"**. Recomputed: the 13 are `bn brx hi kok ks mai mr or pa sa sd ta ur` → **surya 10**, tess-family 2, easyocr 1. The 12-count is arithmetically the *probe22-only* set (Tamil excluded) and the "7 of those 12" in the 0.10–0.40 band is the same silent exclusion (8 of 13 with `ta` at 0.331). `ta` is also missing from the worst-first ranked list at plan:83, where it would sit between `sd` 0.316 and `or` 0.259.

Tamil is **the only South language with n≥50**. The plan drops it from the analysis without saying so, immediately after tabulating it. §5 (plan:128) propagates the same "7 of 12" into the Option A evidence cell.

Related, same paragraph: plan:72 says *"the smallest scored n of all 22 is 19 (Assamese)"* — true for the probe22 18, false for all 22, since **Malayalam is n=5**, as the plan's own table three lines later concedes. Two self-contradictions inside 12 lines of the section that is supposed to be the plan's factual spine.

**Concrete failure:** a CEO comparing the table to the prose sees a 12 vs 13 mismatch and stops trusting the document. This is a fifteen-minute fix and it is the cheapest credibility win available.

### W5 — The 87.39 denominator is stated with the wrong cause, and it imports an exclusion that was not applied

plan:12: *"6,909 curated text-block samples (6,609 valid after their own exclusion of ambiguous-GT and degenerate outputs)"*.

`COMPETITOR_INTEL:10` — the plan's own permitted evidence — says: *"n in the headline = 6,609 (22 Indic languages); English (300) is EXCLUDED"*. 6,909 − 300 English = 6,609 **exactly**, leaving zero items for any ambiguous-GT or degenerate-output exclusion.

**The plan has attached the wrong mechanism to its single most important number.** It believes the headline denominator is a *valid-sample* count after predictions were dropped. If that were true, the 22-row macro-average would be over a denominator that moves with the model's behaviour — a materially different and much more attackable claim than a plain 22-language sample count. The plan's §1 conclusion happens to survive (the metric is still not comparable), but the reasoning chain that produces it rests on a false fact about Sarvam's denominator, and §1 is the section the CEO will read first.

Also in §1: *"it is 6,909 blocks, ours is 1,227 pages"* (plan:15). probe22's 1,227 are **items**, not pages — `BENCHMARK_22:216` describes them as "clean rendered page crops". Calling them pages merges the probe22 item basis with the South-400 page basis, which is the exact merge `BENCHMARK_22` Table 3 exists to forbid, and it does so in the paragraph arguing for non-merging.

---

## 2. Will each proposed method work for Indic scripts? (conjuncts, matras, Nastaliq, Ol Chiki, Meetei Mayek)

**M1 — Per-script routing, wrap-only, already on disk** *(plan:123, the recommended Option A)*. Script-agnostic in mechanism, so it does not fail for any specific script. **But the plan already measured it at −0.0351 CER** (plan:129, 137) and still ships it as Option A's deliverable. The measurement is right in aggregate and wrong in conclusion: routing was measured as a blanket policy, and the plan's own data shows the margin is wildly heterogeneous — 28.4 points on `hi`, 19.4 on `kok`, versus ~6.8 on `pa` and a *collapse* on `sa` (surya 1.000 → easyocr 0.175). A **gap-gated** router — route only where the winner's advantage exceeds a threshold, hold the incumbent otherwise — is untested and is the obvious repair. The plan rejected the router on the strength of the one router it happened to test. **Likely to work for Indic only in the gated form.**

**M2 — Learned script-router** *(Option D, plan:125)*. **No, for Nastaliq specifically, and the plan already proved it.** `EDGE_THESIS:25` / plan:137: script-mismatch routing has 95–100% precision and **0–5% recall**, with **exactly zero gain on `ks`, `ur`, `sat`** — because Nastaliq is script-invariant, so the strongest available signal is definitionally silent on the two languages where we are worst (0.589, 0.623) and on the one where we emit nothing. Adding a learned router on top of a feature that is silent exactly where it is needed is a day spent to reproduce a published negative. Drop it.

**M3 — R4 restoration pre-pass** *(Option D, plan:125, 128)*. **Likely net-negative for our worst cells.** The plan concedes the only measurement is English/French/Spanish historical pages. The specific failure for Indic: a lexicon-or-n-gram restoration gate tuned on Latin-script historical material will substitute high-frequency Latin-script words into **Nastaliq**, whose vocabulary is heavily Persian/Arabic/Urdu-loanword and whose orthography is a *different script*. The result is a fluent, plausible, wrong output — which scores worse than a garbled one, because the garbled one at least fails where the GT is. On `ur`/`ks` this converts a 0.59–0.62 CER into something that looks better on paper and is worse in use. Do not spend the day.

**M4 — Sarvam API subsidy for `sat`/`mni`** *(Option D, plan:125)*. This is not a method. It places the competitor's output inside your own 22-language table. The plan objects on **cost** (plan:129, "$0–30", "$12 API figure is unsourced") and never on **contamination** — the objection that actually matters. If anyone runs it, the resulting table must label those two cells as vendor output or the whole document is fraudulent. This is the most serious *strategic* item in the option table and the plan prices it instead of disqualifying it.

**M5 — Median + abstention rate** *(Day 1, plan:131)*. Script-agnostic and correct. **Ordering caveat:** median-over-a-half-empty-distribution flatters an engine that abstains 50% of the time, because the median only describes the half it answered. Abstention rate must be the **headline** and the median second, or the change becomes a way to launder the abstention bug into a good score. Also note this is **largely already delivered** — `BENCHMARK_22` Table 2 prints mean/median per cell and its empty-prediction table prints per-language counts. The un-done part is the **South-400 half, where it is not computable**: `BENCHMARK_22:222` records that `CER_STAGE3B.json` stores only `cer/wer/gt_chars`, no prediction text, so abstention on the 126 South pages requires **re-running engines over pages**, which is hours of inference, not a 2-hour CSV edit. The 2-hour estimate covers roughly half the job.

**M6 — Tesseract traineddata for Ol Chiki / Meetei Mayek** *(Day 2)*. **The one method here that is very likely to work, and the plan has it wrong** — see W2. Substantively: Tesseract is a conventional LSTM recogniser with a per-language traineddata, so adding `sat`/`mni` models cannot fail the way a VLM does — it will emit the script, imperfectly, instead of emitting nothing. That converts an unmeasurable 0.86–1.00 cell into a measurable one. On the two dead languages, this is the highest expected-value CER movement available at $0. Note the counter-risk: it does not make those cells *good*, and `plan:172` sets the kill at "Ol Chiki CER > 0.90 across all engines" — a bar that a traineddata install may miss while still being a large improvement over emitting nothing, so the kill criterion is set to discard a partial win. Set it at "beats the current best" instead.

**M7 — Fix the surya `sa` all-empty bug** *(Day 1, plan:145, 170)*. The plan asserts "a bug, not a fusion problem" with no root cause. The evidence contradicts "bug": surya is empty on **100/100 `sa`**, and **0/100 on `hi` and 0/100 on `bn`** — all three are the same `official_pair_txt` gold tier, so it is not a data-tier effect. The parsimonious cause is **"surya does not support Sanskrit"** — a language-coverage gap in the model, i.e. a routing decision, not a software defect. If so, the fix is a config change plus a re-score, and `easyocr` already holds the cell at 0.175. **This matters for the schedule:** the plan books a full day and calls it "the only real engineering item this week produced", and the same finding is 67% of the fusion oracle (plan:145). If the cause is coverage, both evaporate without engineering — the week has three days of slack and no plan for it, and the fusion ceiling re-opens at 0.0332 with no selector to spend it on (routing measured −0.0351).

**M8 — Akshara-boundary auxiliary loss** *(SPEC-ONLY, plan:44, PPT_SPEC:13)*. **Likely to work for the eight southern/western Bramic scripts, structurally inapplicable to three of the five scripts you care about, and probably not implementable as specified in the time allowed.** Specifically:
- *Bramic with real conjunct formation — Devanagari, Bengali, Assamese, Gujarati, Malayalam, Kannada, Telugu, Tamil, Oriya:* this is where the technique has signal, and where the classic failure (rakar, repha, ৰ, the South-Indian vattu forms) is a compositional sub-glyph problem an explicit boundary head can help with. Genuinely the one Indic-specific idea in the whole architecture.
- *Nastaliq (`ur`, `ks`):* **no.** Nastaliq is cursive, descending, non-linear, with heavy contextual substitution and *many-to-one* shaping. The problem there is which contextual form to select, not where a cluster boundary falls. A left-to-right boundary objective is structurally wrong for the script.
- *Ol Chiki (`sat`):* **no, and not "weak" — zero.** Ol Chiki is a non-conjunct abugida: consonant letters carry the inherent vowel intrinsically, dependent vowels are separate marks, and there is no half-form formation. There is no akshara boundary to supervise. An auxiliary loss on `sat` optimises a label set that does not exist in the script. (My assessment of the script, not a citation.)
- *Meetei Mayek (`mni`):* **no, same reason** — a non-conjunct abugida with syllabic letters and no Devanagari-style conjuncts. Also zero signal.
- *Implementation:* a VLM emitting markdown/text directly (Qwen2.5-VL, PaddleOCR-VL) has **no akshara boundary token to supervise**. The loss is only implementable by bolting a CTC/char-level head over grapheme clusters onto a model whose entire value is that it emits markdown/JSON. That is a different model, and it is not 5 days on one machine.

The plan correctly marks all of this SPEC-ONLY, so this is a critique of the architecture's suitability for a 1–2 language cell, not of the week's schedule. But it should be said out loud: **the one Indic-specific technique in the design has no signal on Ol Chiki or Meetei Mayek — the two languages the plan's only edge is about.**

**M9 — OpenCV deskew/denoise/binarize** *(SPEC-ONLY, plan:35; PPT_SPEC:31 marks it KEEP)*. **Likely harmful on the two populations the plan cares about.** South-400 is 200-dpi 19th–20th-century book and government scans, and `ur`/`ks`/`sat` are thin-stroke and low-contrast. Fixed/global binarization on 200-dpi degraded paper is a known failure mode, and it is worst exactly where the stroke weight is thinnest — Ol Chiki and Meetei Mayek. If the preprocessing box is ever enabled, it must be evaluated as a hypothesis on the South cells, not assumed from the PPT.

---

## 3. Missing 2025–2026 techniques and open resources

Confidence marked per the brief. I did not open any of these; the arXiv IDs in the plan's own appendix are format-valid but their titles are unverifiable from the permitted files.

1. **olmOCR / olmOCR-Mix-0225** *(Frieder et al.; olmOCR v1 2024, mix dataset and second generation 2025)* — **HIGH confidence the project exists; MODERATE confidence on exact 2025 release names.** The single biggest miss. It is the field's dedicated **old/degraded/deteriorated scan** OCR work, and the plan's "degraded scans (untested)" (plan:104) and South-400 population are precisely its target. The plan mentions "OldScan 55.3" four times and never once as a place where a model exists. Open weights, permissive licence.
2. **Tesseract `indic.traineddata` from `tessdata_best`** — **HIGH confidence.** The canonical multi-script Indic Tesseract model covering ~17 scripts. This is a **known-good, documented** route to `sat`/`mni`/`kan`/`mal`/`tam`/`tel`, and a fallback if the GitHub pack is absent. Its per-language files are in the same size class as the 8–15 MB already on this disk — which independently falsifies the plan's "2–4 MB". The plan does not mention it.
3. **Google Document AI / Azure AI Document Intelligence** (GA, 2025–2026) — **MODERATE-HIGH that they exist with broad Indic language coverage; UNCERTAIN on Indic OCR accuracy; UNCERTAIN on free-tier size.** Relevant not as a product but as a **measurement instrument**: the plan's binding constraint is paired n≥50 comparisons against a strong general VLM, and a public API with a free tier can supply that at $0 with no Sarvam cap involved. The plan considers only "a $12 unpriced Sarvam API" and never a free tier, so its only route to the measurement it needs is the one route it is capped out of.
4. **DeepSeek-OCR** (2025, open weights) — **MODERATE-HIGH.** Modern open document OCR, cheap to run. Indic performance **UNCERTAIN**.
5. **MinerU 2.5** (2025, open) — **MODERATE.** Strong on layout/tables, which is where the plan's Day-3 table has no coverage (0% table items in our corpus *and* in Sarvam's — `COMPETITOR_INTEL:79`).
6. **Nanonets-OCR-s / Nanonets-OCR2-3B** (2025, open) — **MODERATE-HIGH.** Already named at `PPT_SPEC:33` as the reason to drop TrOCR-from-scratch, but **absent from the plan's option space**. The architecture note recommends it and the plan never costs it.
7. **IndicCorp / Sangraha / Bhashini-derived synthetic page generation for `ta`/`te`/`kn`/`ml`** — **HIGH confidence these corpora exist; they are already in `PPT_SPEC:21` (S3, S6).** Out of the 2025–2026 window, so not a "new technique" — but this is the *sharpest* omission in the document. The plan's 5 days create **zero** new labelled data and accept Malayalam at **n=5**, which its own §3 calls below the floor. Synthesising 500–2,000 pages per thin language from a text corpus is the only route that lifts `ml`/`kn`/`te` off the floor at $0 and requires no training, no download, and no new model. The plan does not consider it, and Day 1–5 are all reporting work.
8. **Aakshara (AI4Bharat Indic NLP toolkit)** — **MODERATE confidence it exists; MODERATE that it ships Ol Chiki / Meetei Mayek conventions** (`EDGE_THESIS:15` asserts it does). If true it is a better-documented and larger Ol Chiki / Meetei Mayek resource than the unverified 2–4 MB pack, and it also directly refutes the "no download" premise of the killed grapheme-validity thesis.
9. **Grapheme-cluster-aware CER for Indic** — **UNCERTAIN as a specific 2025–2026 paper; CERTAIN as a standard** (Unicode UAX #29 already encodes the Indic grapheme rules, which is what `EDGE_THESIS:15` cites against C2). Character-level Levenshtein counts a 4-codepoint matra-conjunct cluster as 4 edits, so codepoint CER systematically penalises correct output. Both scorers here happen to strip ZWJ/ZWNJ, which defuses the worst of it — so this is a *reporting* refinement, not a fix. Cheap, genuinely new for Indic, and nobody in `COMPETITOR_INTEL` reports it.

**Two sourcing problems in §4 itself, independent of the above.** plan:112 kills the team's router idea on the authority of *"consensus-entropy OCR verification (CVPR 2026)"* — the plan gives **no title, no authors, no identifier anywhere in the body**, and the identifier in the appendix (`EDGE_THESIS:16` → arXiv 2504.11101) is never linked to the claim. That is the single most consequential external claim in the plan: it is what killed C3, a *published* version of the team's own idea. Similarly, plan:113's "LV-ROVER-MLT (DocEng 2026 winner)" and plan:114's "GlotOCR Bench (LMU/TU Munich)" carry **no identifiers at all**, and Option D's entire justification rests on the first one (plan:128). The plan's evidence law is not applied to its citations.

---

## 4. Evaluation: what is unfair or statistically unsupported

Ordered by severity.

1. **No confidence interval appears anywhere in the document.** 22 languages × 10 engines, n = 5 to 100, per-item CER with mass pinned at 1.0 from abstentions, and **every** claim is a point estimate. The "2.5×", the "we lead on PDF-layer GT", the "9 of 12 winners" — all noiseless. The plan says "directional at best" for the Sarvam pairing and then prints a bolded 2.5× immediately above that caveat. Bootstrap CIs are hours of work and are absent from a 5-day plan whose whole thesis is evaluation integrity.
2. **The winner is selected on the scored items** (W3). 220 configurations, argmin reported on the same rows, no held-out split, no selection correction. This biases *our* side upward and is the one place the plan's "no claim without its n" law is not applied to itself.
3. **"Best local per item" is an oracle, presented as an engine** (W1/W3). The honest spread on the same 18 items is 1.75× to 3.70×; the plan quotes the most favourable point and labels it "our best local engine."
4. **The tier stratification is confounded with language difficulty, and the plan does not make the conditionality explicit.** Splitting by GT provenance is only valid if tier is unrelated to how hard the language is for us. It is not: the fill tier is 100% the three hardest cells for us (`as` 0.189, `mni` 0.858, `sat` 0.651) and two of three are dead-script. "Sarvam wins on human-verified GT" and "we win on PDF-layer GT" are both partly statements about *which languages are in which tier*, not about ground-truth quality. The plan correctly stops short of calling the pooled 10/18 a win; it should equally stop short of calling the tier split a resolution.
5. **Neither tier is unbiased, so the split cannot settle the question either.** The plan's hypothesis (plan:97) is that PDF text layers reward layout-literal output. If true, our "lead" is a scorer artefact. The symmetric implication is that *their* lead is also a scorer artefact on a set that happens to contain our two dead languages. The parsimonious reading of the whole section is **"we cannot tell"** — which the plan never states, because "we cannot tell" is less presentable than either number.
6. **The "2.5× lower" ratio is the wrong statistic and ambiguously worded.** On a metric capped at 1.0 with ~50% of some engines' items sitting exactly at 1.0, a ratio is unstable; the percentage-point gap is the interpretable form (0.098 vs 0.259 — a 2.6× difference in the gap itself). And "2.5× lower CER" reads to most executives as "Sarvam is 2.5× better", which is the reciprocal, 0.398×, and wrong.
7. **`K2 pa: p=1.00 … NOT MET` is arithmetically impossible and load-bearing.** For a two-sided exact McNemar, `p = 1.000` is attained only at **0 discordant pairs** (verified by enumeration: the maximum attainable two-sided p is 1.000 at every discordance level, but the *only* input yielding exactly 1.000 with n>0 is zero discordance — i.e. both engines byte-identical on every item). `pa` has surya 0.1447 vs tesseract_indic 0.226 on n=90, an 8.1-point mean gap. Zero discordant pairs is incompatible with that. Either the test is not McNemar, or the number is wrong. It is load-bearing: it removed Punjabi from QLoRA scope (plan:60). A kill criterion that removes a training target on an impossible p-value needs its harness checked before the CEO sees it.
8. **A McNemar p-value is being read as a statement about mean-CER magnitude.** K1 reports "19.4pt vs easyocr p=0.0107 n=100" (plan:59). McNemar tests the **sign count** of paired wins, not the size of the mean gap. Attaching a p to a 19.4-point difference implies a test that was not run. Separately, if `kok` was not pre-specified, reporting the maximum over 45 within-language pairwise comparisons needs a multiplicity adjustment; the plan cites `W6_QLORA_SPEC.md:75` for K2 but says nothing about K1's pre-specification.
9. **§4.2 uses `mixed_script=False` on all 12,324 rows as evidence the corpus is single-script — and that field is known to be wrong.** `EDGE_THESIS:17` (C4) establishes 18 of 79 Marathi items carry injected Ol Chiki, and the whole C4 analysis rests on per-row Unicode-block computation, not on the flag. The plan uses a field it (elsewhere) knows is unreliable to kill a metric. Conclusion is probably still right for the wrong reason; the citation is not.
10. **The 54 paired items are 4.4% of the pool and the selection is never described** (54/1,227). Whether the 3 items per language were drawn randomly, pre-registered, or picked after seeing results changes what n=3 means. The plan says n=3 is directional and then leans on it.
11. **The 87.39 denominator carries the wrong exclusion** (W5). If the plan's reading were right, the 22-row macro-average would be over a denominator that moves with the model's own degenerate outputs — a stronger attack on Sarvam than any claim the plan actually makes, and one that would collapse under a single line from their card. Do not take it to a CEO.
12. **Option D's "Sarvam subsidy" would contaminate the table** (M4) and the plan raises cost, not integrity.
13. **Internal contradictions, all reproducible:** 12 vs 13 languages at n≥50 (W4); "smallest scored n of all 22 is 19" vs `ml`=5; `tam`/`tel`/`kan`/`mal` "already on disk" vs §6's own inventory, **filesystem-verified against the plan** (W2); "12 critiques we did run" vs "seven of **eleven** critiques" (plan:151); and in that same paragraph, **"two critiques raised by all three reviewers"** when §7's own first sentence says **one of three evaluators could not run and one is still waiting on a paste** (plan:149). That sentence conflates the 3 LLM *evaluators* with the 3 adversarial *lenses* from `EDGE_THESIS`. The paragraph that reports the document's own evaluation is the least accurate section of the document.

**What is fair and should survive:** the paired 54-item comparison is same-scorer on both sides (`BENCHMARK_22:344`), which is the correct design; refusing 87.39 as incomparable is right; collapsing the three byte-identical Tesseract aliases is right; refusing to present the pooled 10/18 is right; the `-sa` fusion restatement at 0.0332 and the withdrawal of the non-reproducing 0.4277/0.5229 pair are the right kind of disclosure; and publishing that the evidence sheet cannot regenerate its own CER column is a genuine mark of integrity that most teams would have buried.

---

## 5. Option A vs Option D

**A > D, decisively — but A as specified is not the right A.**

D's entire increment over A is three things, and all three are negative or contaminated:

- a **learned script-router**, whose underlying feature is measured at 0–5% recall and **exactly zero gain on `ks`, `ur`, `sat`** — silent on precisely the languages where we are worst and where the bar is set;
- an **R4 restoration pre-pass** borrowed from Latin-script historical-page measurement with no non-Latin evidence, and with a specific mechanism to *hurt* Nastaliq (Latin-script n-grams substituted into a non-Latin script);
- a **Sarvam API subsidy** that puts competitor output inside our own table and is objected to on price, not integrity.

Against that, A costs $0, needs no approval, and its one new artifact is already on disk. D is strictly worse on every axis the plan itself measures. The plan's recommendation is correct.

**But the plan then recommends an A whose main deliverable is the component it measured as harmful.** A "ships the per-script routing table that is already on disk" (plan:125) — and the plan's own number for that table is **−0.0351 CER** (plan:129). Shipping a demonstrably negative component as the product of a hackathon week is a bad trade even at $0.

**The A I would run: A plus two corrections.**
1. **Gap-gated routing** instead of blanket routing — switch only where the incumbent's margin exceeds a threshold, verified per language. `hi` 28.4pt, `kok` 19.4pt, `sa` −0.825pt (switch *away* from surya): the heterogeneity is already in the plan's own data, and a threshold rule is a 2-hour change with a measurable payoff. This converts A's dead deliverable into a live one and costs nothing.
2. **A redefined Day 1** — abstention rate as the headline column, median second, plus the 2–3 hour check of whether `sa` is a coverage gap (fix) or a bug (do not fund a day). If it is coverage, the week has three days of slack and the plan has nothing for them; the cheapest high-value use of that slack is synthesising `ml`/`kn`/`te` pages from IndicCorp/Sangraha to lift three languages off the floor, which is the only move in the document that changes a headline number.

**Do not spend the router day, the restoration day, or the API money.** If the CEO insists on spending a day beyond A, spend it on the traineddata acquisition (W2/M6) — it is the only item that moves CER in the right direction at $0.

---

## 6. The single change that most increases the chance of beating Sarvam honestly

**Correctly scope, verify, and source the traineddata acquisition — six languages from a known-good source, not two from an unverified pack.** Then *ask* the CEO to approve it on those terms.

Why this and not something cleverer:

- It is the only item on the board that **moves our CER in the right direction** for **$0** in **one day** with no training. The rest of the 5-day plan is measurement and reporting, which by construction cannot improve the score.
- Tesseract with a real `sat`/`mni` traineddata **cannot fail the way a VLM does** — it emits the script imperfectly instead of emitting nothing. That converts an unmeasurable cell (0.86–1.00, and an honest-empty) into a measurable one. On the two languages where the bar is also lowest — Sarvam's own worst Indic cells are Santali 53.91 and Kashmiri 54.82 (`COMPETITOR_INTEL:32,39`) — a merely-competent local engine can plausibly reach parity. That is the only place on the board where 1 day of work could flip cells.
- It covers `kan`/`mal`/`tam`/`tel` as well, which are three of the four thinnest South cells. The plan's version of this ask explicitly excludes them on a **filesystem-false** premise.
- Its cost is the ask, not the work — and the ask as written would be approved and deliver nothing.

**And the biggest question the plan never asks:** the Sarvam call cap. `BENCHMARK_22:353` records it as reached, with 3/lang as "all we will ever have without the boss's explicit yes". Every candidate claim in §3 rests on 54 items. The existing 10/18 is *weak positive* evidence that the pairing might genuinely be competitive on our corpus — and the plan's response to "n=3 is noise" is to publish a demo with no accuracy gain, when the correct response is to buy n≥50 per language. **Do not ask the CEO to choose between a win and a loss on 54 items; ask for the calls that make it decidable.** Note the price is genuinely unknown (the plan calls $12 unsourced), so this is also a question, not a blocker — and it should be asked as a question rather than assumed as a blocker, which is what the plan does.

---

## 7. Are the ten questions the right ten?

**No. Three are wasted, one is misdirected, and the most important question is buried at #10.**

| # | Verdict |
|---|---|
| **Q1** (dates; "43 files carry a wrong weekday") | **Wrong venue.** This is a data-hygiene ticket for whoever owns the repo. It does not belong beside "are you willing to present the weaker headline". Fold into Q2. |
| **Q2** (deadline: Oct 4 / Oct 15 / qualifiers 30-09) | **Keep.** Genuinely CEO-level, genuinely unanswerable by the team, and it determines whether the 5-day plan is 3 days or 10. |
| **Q3** (Option A or D, which backbone) | **Keep**, but the document already answers it: it recommends A, and it recommends Qwen2.5-VL-3B "on the strength of the lock" (plan:133) — which is not a technical argument for a model with no weights on disk. Ask instead: *is downloading a backbone at all in scope for a wrap-only week?* One question, one decision. |
| **Q4** (backbone weights: download or stay wrap-only at $0?) | **Delete — duplicate of Q3.** Q4 is a strict special case of Q3. This slot is better spent on the Sarvam call cap. |
| **Q5** (download Ol Chiki / Meetei Mayek) | **Keep, but it must be rewritten before it is asked** (W2). As written the bold scoping sentence is false against the filesystem and the size is off by 5–8×. **Verify the pack's file listing first — that is free and needs no approval.** Fall back to `tessdata_best` `indic` models, which are known-good and are the same size class as the files already on disk. Also: change the Day-3 kill criterion from "Ol Chiki CER > 0.90" to "beats the current best", or the plan will discard a partial win. |
| **Q6** (reopen §6.4 for `mni`/`sat`?) | **Keep and promote.** This is the best-argued item in the list — a verifier that cannot read Ol Chiki cannot judge Ol Chiki — and it "could change two languages' status". It belongs at #2. |
| **Q7** (the untracked `src/`/`tests/` build, imports after 21:00) | **Wrong venue.** This is an internal process/governance item for the CTO. Phrased as it stands ("stop it, archive it, or authorise it?") it asks a CEO to adjudicate the team's own agent behaviour. |
| **Q8** ("may I tell you our evidence sheet cannot regenerate its own CER column?") | **Misdirected, and redundant with Q9.** Asking permission to disclose a known defect you have already decided to disclose is not a decision. Fold into Q9 as the reason. |
| **Q9** (re-score 56 items, regenerate `sheet.csv`, adopt `sheet_v2`) | **Keep. This is the most important operational question in the document** — a reviewer who re-runs the scorer and gets different numbers will discard everything else. Move to #1. |
| **Q10** (present the tier-stratified result rather than the pooled one?) | **Keep and promote to #1.** This is the only question that changes what the company says in public. It is currently #10 of 10, behind a clerical question. If the CEO is asked anything else first, it should be this. And it must be asked **with W1's qualifier attached** — "2.5× behind on human-verified GT, of which ~62% of the gap is two languages no local engine can read" — or the plan has handed over a number it cannot defend. |

**The five questions I would actually put to the CEO:**

1. **Are we willing to publish the tier-stratified result, with the dead-script qualifier attached?** (present Q10 + W1)
2. **May we regenerate the LOCKED evidence sheet and adopt `sheet_v2` for all external reporting?** (present Q9 + Q8)
3. **May we raise the Sarvam call cap and run a matched n≥50-per-language comparison on the 13 languages where we have n≥50?** — never asked, and it is the only thing that makes the win-or-loss decidable. Price is unknown; that is part of the question.
4. **May we download ~70 MB of Tesseract traineddata for six languages (`sat`, `mni`, `kan`, `mal`, `tam`, `tel`) from a known-good source?** (rewritten Q5; note the existing files on disk are 8–15 MB each)
5. **Is the success criterion "beat Sarvam across 22 languages", or "beat Sarvam on a stated matched protocol at n≥50 on the languages we can measure"?** — because Option A, which the plan recommends, **cannot** do the first, and the plan says so itself (plan:129). Nobody in the document ever asks whether the goal can move.

**One question the plan should add and does not:** *who is the third-party arbiter?* §1 concludes "let a third party compare" (plan:18) and no such party is named, engaged, or costed anywhere. A self-published table compared by the authors' own tooling, by the same team that just documented that its own evidence sheet cannot regenerate its numbers, has no external value. Either name the arbiter or drop the claim.

---

### Sources relied on

**Files opened (permitted only):**
- `docs/campaign/DRAFT_RESEARCH_PLAN.md` — full, 184 lines. Cited as `plan:N`.
- `docs/campaign/BENCHMARK_22.md` — full, 360 lines. Cited as `BENCHMARK_22:N`. Load-bearing: `:22` (n≥50 count, C12), `:24` (South two-partition finding), `:82` (1,283/1,227 tier totals), `:92-115` (Table 2 per-language mean/median + Sarvam n=3), `:144-165` (empty-prediction counts), `:177-181` (2b-1 lang-tag scored n), `:199-206` (2b-3 cross-tab), `:216-223` (Table 3 basis diff), `:263` (C11 loop-exclusion), `:275-299` (Sarvam paired table, surya means per language), `:310-344` (normalisation diff, both scorers opened), `:340` (87.39 = UNKNOWN), `:344` (only defensible statement), `:353` (Sarvam call cap reached).
- `docs/campaign/COMPETITOR_INTEL.md` — full, 105 lines. Load-bearing: `:10` (87.39 = 6,609 Indic, 300 English excluded, 87.3909), `:14` (Bodhan bench, 0.4-pt margin), `:16` (Bodhan ₹0.20/image, ₹10 credit), `:26` (bench as instrument, 6,909 test + 1,173 small_representative), `:32-42` (the 8/22 flip table, Kashmiri −8.90), `:52-65` (comparability table), `:67` (the one surviving sentence), `:79` (0% table / 0% mixed / 100% printed), `:91` (87.39 metric UNKNOWN).
- `docs/campaign/EDGE_THESIS.md` — full, 61 lines. Load-bearing: `:8` (4 drafted, 0 survived), `:14-17` (C1–C4 verdicts), `:21` (0 of 200 Ol Chiki), `:25` (router recall 0.0–5.2%, zero gain on ks/ur/sat, −0.0351, abstention %), `:27` (C4: 18/79 Marathi carry injected Ol Chiki), `:34-36` (tessdata 12 files, none of mni/sat/kan/mal/tam/tel; pack listing UNVERIFIED), `:50` (sheet.csv CER cannot re-derive), `:56` (fusion 0.3213 vs 0.4190, 67% `sa`, ex-`sa` 0.0332), `:55` (credibility edge, buildable from data already held).
- `docs/architecture/PPT_SPEC.md` — full, 39 lines. Load-bearing: `:13` (akshara-boundary aux loss; TrOCR + Qwen 3.5 VL + PaddleOCR-VL 1.6; Kashmiri layout-box GT), `:17` (eval boxes, no fine-tune on test), `:21` (Bhashini/IndicCorp/Sangraha data sources S3/S6 — unused by the plan), `:31-37` (stage KEEP/HYBRID verdicts, Nanonets-OCR2-3B).

**Disk verification I ran (read-only, no downloads, nothing in `src/`):**
- `ls -la level2/probe22/tessdata/` — 12 files: `asm ben eng guj hin mar nep ori pan san snd urd`. **Confirms `EDGE_THESIS:34`; refutes `plan:159`.** Sizes 7.99–15.40 MB, mean 11.6 MB, total 271,760 KB.
- Python aggregation (written to a temp dir outside the repo) — recomputed from `BENCHMARK_22` Table 2 and the paired table: n≥50 set and winner counts; 0.10–0.40 band membership; the 6,909→6,609 basis; the 87.3909 macro; the three tier means; the 2.51× / 1.75× / 3.70× recomputations; the 0.259 vs 0.098 pp gaps; the 62% dead-script share; the fill-tier third-language solve (`x = 0.3340` ≈ Assamese 0.3339); the PDF-tier surya mean 0.2295 reproducing the plan's 0.229; the traineddata size ratio; the McNemar `p = 1.000` enumeration over discordance 1–100.
- Not opened, per instructions: all 1A/1G/fix-spec files, `DISPATCH_LOG`, and the other `W1_reports/` reviewer outputs.

**URLs opened: none.** I did not fetch anything. Every external claim in this review is either (a) recomputed from the four permitted files, (b) measured on disk, or (c) explicitly marked UNCERTAIN. The arXiv identifiers in the plan's appendix (`2607.00250`, `2604.12978`, `2606.29213`, and `2504.11101` from `EDGE_THESIS:16`) were checked for **format validity only** (month in range; 2026-04/06/07 and 2025-04) — I did not open them and make **no** claim about what they contain. The plan itself supplies no title or authors for the CVPR 2026, DocEng 2026, or GlotOCR Bench items it relies on.

### UNRESOLVED

1. **Which 6 languages the 18 "human-verified" items cover.** I derive bn/hi/sa + as/mni/sat from the plan's own tier table and the exact fit of the third fill-language to Assamese (0.3340 vs 0.3339). Not confirmed against `sheet.csv`/`manifest.json` in this session. **If this reconstruction is wrong, W1's 62% figure collapses and must be recomputed.** This is the single most important open item in the review.
2. **The 0.617 "best local per item" for the fill tier** does not equal the mean of the per-language best-engine means for {as, mni, sat} (which is 0.566). Consistent with a true per-item oracle, but unconfirmed.
3. **The mechanism behind `K2 pa: p=1.00`.** A two-sided exact McNemar cannot return exactly 1.000 with n=90 and discordant pairs > 0. Either the harness is not McNemar, the null is different, or the number is wrong. Load-bearing for the QLoRA scope of Punjabi. Not investigated — read-only wave.
4. **Whether the `kok` McNemar test (K1) was pre-specified.** If it was selected as the maximum over 45 within-language pairwise comparisons, `p=0.0107` needs a multiplicity adjustment. `K2` cites its spec line; `K1` cites none.
5. **The surya `sa` root cause.** I hypothesise unsupported-language coverage (surya is empty 100/100 on `sa` and 0/100 on `hi`/`bn`, all the same GT tier), not a bug. Untested. Determines whether Day 1 is a config change or a day of engineering, and whether the 67%-of-oracle finding is real.
6. **Whether `indic-ocr.github.io` contains `sat`/`mni`/`tam`/`tel`/`kan`/`mal` traineddata, at what size.** Not opened. Requires no download approval to check — it is the free prerequisite to asking the CEO anything.
7. **Sarvam API pricing.** The plan calls $12 unsourced; `COMPETITOR_INTEL:16` prices Bodhan at ₹0.20/image with ₹10 free credit but says nothing about Sarvam. The single highest-value un-asked question has an unknown price.
8. **Whether the per-script routing table already on disk was fitted on any of the 1,683 labelled items.** If it was, the "best local" column is optimistically biased by an unquantified amount and W3 gets worse. Never stated anywhere in the plan or `BENCHMARK_22`.
9. **All four external resources in §3 items 1–8 are unopened.** Existence confidence is marked per item; accuracy claims are not made. If the CEO needs a recommendation on any of them, that requires opening the sources, which this session did not do.
10. **`W6_QLORA_SPEC.md:53` and `:75`** are cited in the plan but were not opened (outside the permitted evidence list), so the Qwen2.5-VL-3B lock and the K2 kill line are taken on the plan's word.
11. **Two questions the plan does not ask and I cannot answer for it:** who the third-party arbiter is (§1 defers the comparison to one), and whether the success criterion can move from "beat Sarvam across 22 languages" given that the plan's own recommendation concedes it.
