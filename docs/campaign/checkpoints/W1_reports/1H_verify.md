# 1H — VERDICT: `docs/campaign/DRAFT_RESEARCH_PLAN.md`

**Agent:** VERDICT (subagent) · **Run:** 2026-09-30 · **Role:** reviewer. I did not author
`DRAFT_RESEARCH_PLAN.md` and I did not apply any fix.
**Law observed:** read-only on every target. I wrote **this file only**. No `src/` run, no download,
no Sarvam call, no write to `level2/out/`, `level2/reports/`, `level2/probe22/out/`, `arc_level_1/`,
`Datasets/`. No existing repo file edited.

## VERDICT: **FAIL — 7 BLOCKERs.** Not presentable to the CEO in this state.

The document's *architecture* is right: the GT-tier stratification, the "zero edge theses survived",
the "22 languages holds for labelled data only" frame, the sheet.csv provenance note and the
"we do not chase 87.39" verdict are all correct and all reproduced exactly from disk. The failures
are concentrated in the one paragraph a CEO will read first (§3's winner sentence), in §5's option
table, and in four source misattributions. None of the 7 blockers is a rounding problem; four are
plainly false superlatives or false absences that a sharp reader can check in 60 seconds.

---

## 1. The 10 checks

| # | check | result | evidence | exact fix needed |
|---|---|---|---|---|
| 1 | **NUMBERS** (15+ re-derived) | **FAIL** | 67 numeric claims reproduce; **20 do not**. Full list + commands in §2. Hard failures: "the weakest is Konkani at 0.425" (ur 0.6232 / ks 0.5894 / bn 0.4763 are all worse); "the biggest gap we have" (hi 0.2839 > kok 0.1938); "Sarvam 97.41, its **third-best** Indic cell" (**rank 1 of 22**); "four of the 22 languages exist as *labelled* data only" (**zero** languages are labelled-only); "No winner claim (n<50) \| **8** — as 19, mni 20, sat 20, gu 24, te 26, doi 27, ne 37" (**7 listed, `kn 25` missing; `BENCHMARK_22.md:37-58` flags 9**); "**100** of 400 sampled rows reproduce" (**110** at 1e-4, **111** at 5e-4); "~**1,195** lines" (**1,995**); "per-item oracle 0.4277 vs best single 0.5229" (**internally impossible** — surya = 0.4190 on the same sample, better than the stated oracle). | See the per-number fixes in §2. All are one-line replacements; none requires re-analysis. |
| 2 | **n AND METRIC** on every number | **FAIL** | §3:83 states "the 19.4-point Kok gain is McNemar p=0.0033 (n=100)" — the 19.4 pt is surya-vs-**easyocr** (p=**0.0107**); p=0.0033 is surya-vs-**tesseract-family** (gap 0.2196). Two different comparisons welded to one sentence. Separately, the McNemar is a **pass/fail test at CER<0.5** (`mcnemar_full_matrix.json` meta `cer_threshold: 0.5`), not a test on mean CER, and the plan never says so — "significant" is used undefined. §1 states the 87.39 macro as "**6,909** curated text-block samples"; the macro n is **6,609** (6,909 = 6,609 Indic + 300 English, and English is excluded). | (a) Split the sentence: "19.4 pt vs easyocr (McNemar p=0.0107, n=100); 22.0 pt vs the tesseract-family (p=0.0033, n=100)". (b) Add one line to §3: "McNemar here is a per-item pass/fail test at CER < 0.5 (`mcnemar_full_matrix.json` `cer_threshold`), not a test on mean CER." (c) §1: change "6,909 curated text-block samples" to "6,909 samples, of which **6,609 across the 22 Indic languages; the 87.39 macro is over those 6,609 with English excluded**." |
| 3 | **COMPARISONS** (wins/beats/best/SOTA) | **FAIL** | §3:83: "the weakest is Konkani", "the biggest gap we have" — both false superlatives, neither has a named test and both are refuted by the same n≥50 set the sentence cites. §5's option table: the two columns describe the same option (§7, D2 below). §5:132 "GLM-OCR is **absent** from the OmniDocBench v1.6 table it was cited in" — **false**: GLM-OCR is in v1.6 at **94.71 overall, rank 3** (Paddle 96.01 · Sarvam 94.97 · GLM 94.71). §4:113 "LV-ROVER-MLT (**DocEng 2026 winner**)" — the paper says "The held-out DocEng 2026 competition result is under organizer embargo and is not reported" and labels itself a working paper. | (a) Delete "the weakest is Konkani at 0.425" and "the biggest gap we have" from §3:83; replace with the measured order: "our three worst n≥50 cells are ur 0.6232, ks 0.5894, bn 0.4763; the largest winner-to-runner-up gap is **hi 0.2839**, then kok 0.1938." (b) §5:132 replace "absent from the OmniDocBench v1.6 table" with "**ranks 3rd on OmniDocBench v1.6 at 94.71** (behind Paddle 96.01 and Sarvam 94.97); the feed's '(#1 of tested)' claim is v1.5, not v1.6." (c) §4:113 change "(DocEng 2026 winner)" to "(DocEng 2026 Maltese OCR competition entry; **its held-out result is under organiser embargo and unpublished**)". |
| 4 | **SOURCES** (3 URLs + 5 file:line) | **FAIL** | **URLs opened — 6.** `huggingface.co/datasets/sarvamai/indic-ocr-bench` card: all §1 quotes verbatim ✓ ("6,909", "23 languages : all 22 languages listed in the Eighth Schedule…, plus English", "curated at the **semantic block level**", "**reviewed twice by human language experts**", "**Word Accuracy = 100 × ( 1 − WER )**", "Samples with ambiguous ground truth… are excluded", "Predictions that exhibit runaway repetition (tail loops) are flagged separately and excluded from valid-sample metrics"); 23 language rows sum to **6,909** ✓. `sarvam.ai/blogs/sarvam-vision-2-1`: the full 22-row table — Konkani **97.41** ✓, Kashmiri **54.82** ✓, Odia **80.01** ✓, Santhali **53.91** ✓, and the 22-row unweighted mean = **87.3909** → 87.39 ✓ (independently re-derived, §2 #20). `arxiv.org/abs/2504.11101` "Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR" — training-free inter-model agreement, verifies outputs, selects best outputs, adaptive routing ✓ substance confirmed. `arxiv.org/abs/2607.00250` "LV-ROVER-MLT… five deterministic Tesseract configurations… Maltese-specific diacritic-restoration gate" ✓. `arxiv.org/abs/2604.12978` "GlotOCR Bench" ✓ (LMU/cisnlp). `github.com/indic-ocr/indic-ocr.github.io` README: tessdata "include **Ol Chiki (Santali)** and **Meetei Mayek (Manipuri)** scripts too" ✓ — so §4:115's "UNVERIFIED: we did not open its file listing" understates what is now known. **File:line:** the plan's only body `file:line` is `W6_QLORA_SPEC.md:53` → line 53 is `**Backbone:** **Qwen2.5-VL-3B-Instruct @ 4-bit MLX** (primary).` ✓ exists and says what is claimed. **FAIL cause:** the plan's opened-URL list does **not** include `2504.11101`, the only arXiv ID behind its §4 item 3 — so a reader cannot check the one claim that killed an edge thesis. | (a) Add `arxiv.org/abs/2504.11101` to the appendix URL list. (b) §4:115 change "UNVERIFIED: we did not open its file listing" to "README confirms the pack includes Ol Chiki and Meetei Mayek; **the file listing and the licence are still unverified** — verify both before download." |
| 5 | **QUOTES verbatim** | **PASS** | Every quoted string checked against its source: the six HF-card strings in §1 all appear verbatim (see §4 row). §3:101 quotes the proto-61 required phrase: "CER as stored by the probe scoring pass; independent re-derivation is in progress" — carries `CER as stored` + `independent re-derivation is in progress` verbatim ✓. §8:159 quotes the card's "**reviewed twice by human language experts**" ✓. §4:113 "coherent units of text rather than full noisy pages" ✓ card. No invented quote found. | none |
| 6 | **DATES** | **PASS with one defect** | `datetime.date.fromisoformat` → 2026-09-29 Tue · **2026-09-30 Wed** ✓ · 2026-10-07 **Wed** ✓ · 2026-10-01 Thu · 2026-10-04 **Sun** ✓. §8:154 "this Wednesday (2026-09-30) or 2026-10-07" — both weekdays correct, and the plan says "I will not guess" ✓. §8:155 "Oct 4 … Oct 4 is a Sunday" ✓. No stale weekday survives in the body. **Defect:** the title block is dated **2026-09-29** while §1:12 says the benchmark card was "**opened 2026-09-30**" — the document is dated the day before its own newest evidence. §4:108 also says "each with a source opened on 2026-09-29", inconsistent with §1. | Change the title-block date to **2026-09-30**, and change §4:108 to "each with a source opened on 2026-09-29/30". |
| 7 | **SCOPE vs proto-19 + proto-64 step 6** | **PASS-WITH-FIXES** | **All 9 sections exist** with the proto-19 titles and order, plus the appendix. **All six proto-64 mandatory additions present:** (1) §3 GT-tier table, pooled 10/18 explicitly refused — line 87 ✓; (2) §3 "126/400" + "labelled data only" — line 72/78 ✓; (3) §3 sheet.csv proto-61 note verbatim — line 101 ✓; (4) §6 "Four edge theses were drafted… **Zero survived**" + Ol Chiki/Meetei coverage gap + U7 download — lines 136/140/142 ✓; (5) §1+§4 comparability table: 87.39 = word accuracy 100×(1−WER) ✓, macro 22 ✓, **n=6,609 MISSING (says 6,909)** ✗, English excluded ✓, 8/22 flips ✓, "no CER of ours is comparable to 87.39" ✓; (6) §8 adds U6, U7, U8, U9 — Q5/Q6/Q7/Q9 ✓. **Missing from §8 vs `proto-92-boss-decisions.md`:** U3 (folded into U8), U5 (folded into Q9), **U10** (level2 restructure), **U11** (South re-run), **U12** (`.env` out of repo), **U13** (handwriting/low-quality in scope), **U14 (surya's modified OpenRAIL-M "$5M funding/revenue" cap — a CEO question, absent from the document going in front of the CEO)**, **U15** (Punjabi K1 → Option A's QLoRA scope is Konkani only). Word count 2,661 vs proto-19's "~1,800 words + tables" (my count includes table cells; §3 is 669 vs a 250 budget, §8 is 380 vs 150, §2 is 63 vs 150). | (a) Add the missing n (6,609) per check 2(c). (b) Add U14 to §8 as a question — it is a CEO decision and this is the CEO document. (c) Add U13 (the probe set is 100% printed, 0 tables, 983/1,283 quality "unknown"; the hackathon targets handwritten and low-quality documents). (d) Add U15 as a stated correction, not a flowchart node. (e) Trim §3 and §8 to their budgets or raise the stated budgets in the protocol. |
| 8 | **LAW** | **PASS** | `git status --short` shows **no write by me** — the only file this session created is this report (`docs/campaign/checkpoints/W1_reports/1H_verify.md`); the 18 untracked root `.md` files (`VINAY_MEETING_PACKET.md`, `DISPATCH_LOG.md`, `BOSS_CONCERNS.md`, …) pre-date this session. `DRAFT_RESEARCH_PLAN.md` mtime is unchanged at `Sep 30 03:39`. ⚠️ Three files on disk are **not mine** and post-date my read of the tree: `_reports/cleanup_cycle3/DEDUP_CYCLE3_SUPERSEDED.md`, `_reports/cleanup_cycle3/DEDUP_CYCLE2_TOPIC_OVERLAP.md`, `docs/campaign/protocols/proto-82-engine-empty-output-patterns.md` — other agents are writing to this repo right now (`CAMPAIGN_DIRECTIVE.md` A6), so re-verify anything you fix-spec against the current bytes. **No new md at repo root.** The document contains **no instruction to train, download or call Sarvam as a completed action**: every training node is tagged `PAUSED` or `SPEC-ONLY` (§2 T1/T3, P1, L1, L2, R3, S1), the only download (§4:115, §6:142, §8 Q5, §9 Day 2) is explicitly "needs your download approval" / "awaiting your approval (U7)" / "blocked until you approve it", and §9 closes "Everything above assumes **no training** and **$0**." No Sarvam call is proposed anywhere. `level2/out/`, `level2/reports/`, `level2/probe22/out/` are read-only inputs. | none |
| 9 | **CONTRADICTIONS** | **FAIL** | **The packet's new GT-tier sentence AGREES with the plan** — `VINAY_MEETING_PACKET.md:119` reads "**2.5x lower** than our best local engine (0.171 vs 0.430)", and I re-derived 0.1711 vs 0.4296, ratio 2.511 ✓. No contradiction there. **But four unflagged contradictions remain:** (a) §2:60 flowchart node "**K2** pai not significant p=1.00 — FAILS, kills pa from scope" contradicts two sources the plan's own appendix cites — `KILL_CRITERIA.md:56` ("pa K1 SURVIVES, p<0.0001, 88 discordant") and `W6_QLORA_SPEC.md:75` ("pa K1 SURVIVES — McNemar p<0.0001"). **The plan's number is the correct one** (`mcnemar_full_matrix.json`: surya vs tesseract_indic on pa = n 90, ties 87, discordant 3, p=1.0) — but the plan never says its two cited sources are wrong, and the packet still says "Konkani + Punjabi QLoRA". Worse, the node's *conclusion* is wrong: pa's gap vs easyocr / paddleocr_indic / rapidocr / doctr / anuvaad is p=**0.0** (89 discordant, surya 0.1447 vs easyocr 0.8173), so "kills pa from scope" is unsupported. (b) §5:132 "GLM-OCR absent from OmniDocBench v1.6" contradicts the blog table (94.71, rank 3) and `W6_QLORA_SPEC.md:55`'s "(OmniDocBench #1, …)" is v1.5 — both in the plan's own source set. (c) §5's Option A column carries Option D's parts (see check 3 / BLOCKER 2). (d) §3:102 says "219 nulled `gt_thin` at GT<200 chars" while the operative threshold on disk is <179 (`CER_STAGE3B.json` `definition` says "<200 GT chars" but the observed max `gt_chars` on a `gt_thin` page is **178**; `CAMPAIGN_DIRECTIVE.md` A5 says "< 179 chars"). | (a) §2:60 → `K1 pa: surya vs tesseract_indic is a TIE (n=90, 87 ties, 3 discordant, p=1.0). This corrects KILL_CRITERIA.md:56 and W6_QLORA_SPEC.md:75, which both say p<0.0001. pa still beats easyocr/paddleocr/rapidocr at p=0.0, so pa is a *runner-up* question, not a kill. Option A's QLoRA scope is Konkani only.` (b) §3:102 → "219 nulled `gt_thin` (observed max GT length 178 chars; `CER_STAGE3B.json` states the rule as <200)". |
| 10 | **HONESTY** (UNKNOWN / honest-empty) | **PASS** | §6:136 states it plainly and in its own words: "**Four edge theses were drafted. All four were killed by three adversarial reviewers each (12 critiques). Zero survived.**" — matches `EDGE_THESIS.md` §1 (C1 2R+1W, C2 3R, C3 2R+1W, C4 2R+1W, zero survivors) ✓. §1:14 marks 87.39's exact metric as **UNKNOWN**: "**UNKNOWN, do not assert:** the card defines word accuracy as 100 × (1 − WER) but never states that 87.39 *is* that figure" ✓ — correctly UNKNOWN, not asserted. §7:148 is honest-empty on the evaluation: "**PARTIAL, and honestly so**… one could not run (no OpenCode tooling), one could not run (budget), and one is waiting on your paste" ✓ matches `MULTI_LLM_EVAL.md` §1. §4:115 flags its own unverified source. §5:126 flags "the $12 API figure is **unsourced**". §8 Q5 says "**Also worth checking whether** `tam`/`tel`/`kan`/`mal` traineddata exists". No section is padded with generic text; §3:104's "degraded scans (untested)" is an honest gap. | none — this is the document's strongest property. |

---

## 2. Re-derived numbers (each with the command that produced it)

**Not correct as stated — 20 items. These are the fixes.**

| doc claim | line | re-derived | verdict |
|---|---|---|---|
| "the weakest is Konkani at **0.425**" | 83 | `kok 0.4248` ✓ but `ur 0.6232`, `ks 0.5894`, `bn 0.4763` are all worse | **FAIL** — 4th worst of 12 |
| "the **biggest gap we have**" (Kok, 19.4 pt) | 83 | `hi 0.2839` > `kok 0.1938` > `bn 0.1812` > `brx 0.1747` | **FAIL** — Hindi is the biggest |
| "the language **we are worst at**" (Kok) | 83 | ur 0.6232 is worst; ks 0.5894 second | **FAIL** |
| Sarvam "97.41, its **third-best** Indic cell" | 83 | 22-row rank: 1 Konkani 97.41 · 2 Nepali 97.00 · 3 Maithili 96.70 | **FAIL** — it is Sarvam's **best** |
| "**four** of the 22 languages exist as *labelled* data only" | 72 | zero languages have 0 scored pages; min scored = `ml 5` | **FAIL** |
| "No winner claim (n<50) \| **8** — as 19, mni 20, sat 20, gu 24, te 26, doi 27, ne 37" | 81 | 7 items listed; `kn 25` missing; `BENCHMARK_22.md:37-58` flags **9** (incl. ml 5) | **FAIL** — count and list disagree |
| "**100 of 400** sampled rows reproduce the stored CER (66 exact)" | 101 | 66 exact ✓ · **110** at 1e-4 · **111** at 5e-4 (tolerance unstated in the plan) | **FAIL** on 100 |
| "~**1,195** lines of untracked QLoRA/GRPO" | 160 | `src/` **1,834** + `tests/` **161** = **1,995** | **FAIL** — 40% low |
| "GLM-OCR is **absent** from the OmniDocBench v1.6 table" | 132 | v1.6 table: Paddle 96.01 · Sarvam 94.97 · **GLM-OCR 94.71** (rank 3) | **FAIL** — it is present |
| "LV-ROVER-MLT (**DocEng 2026 winner**)" | 113 | "The held-out DocEng 2026 competition result is under organizer embargo and is not reported" · "Working paper" | **FAIL** |
| "the binding constraint on rare scripts is **font availability, not model quality**" (GlotOCR) | 114 | the paper: "Performance broadly tracks **script-level pretraining coverage**, suggesting that current OCR systems rely on **language model pretraining** as much as on visual recognition" | **FAIL** — conclusion reversed; the "median 1 font per family" figure is not in the abstract |
| "5 streams of one recogniser on **57 Maltese pages**" | 113 | 5 streams ✓ · "five deterministic Tesseract configurations" ✓ · abstract says **422-paragraph** dev set | **UNVERIFIED** — 57 has no source |
| "**6,909** curated text-block samples" as the 87.39 macro n | 12 | blog: "6,909 samples (**6,609 spanning 22 Indian languages**; 300 in English)"; card 23 rows sum to 6,909 | **FAIL on n** — macro n is 6,609 (proto-64 step 6 requires 6,609) |
| "K2 **pai** not significant p=1.00 — FAILS, **kills pa from scope**" | 60 | p=1.0 vs tesseract_indic ✓ (n 90, 87 ties, 3 discordant); but pa vs easyocr/paddle/rapidocr/doctr/anuvaad = **p=0.0** | **FAIL** — value right, criterion mislabelled (K2 in `KILL_CRITERIA.md` is the *micro-repair* gate), conclusion wrong |
| "`tessdata/` has none of `sat`, `mni`, `kan`, `mal`, `tam`, `tel`" → 6-file download ask | 140, 158 | true of `level2/probe22/tessdata/` (12 files), but `/opt/homebrew/share/tessdata/` has **kan mal tam tel** and `level2/research/smoke/anuvaad_tesseract/tessdata/` has **anuvaad_kan mal tam tel** | **FAIL as an ask** — 4 of the 6 are already on disk; only `sat` and `mni` need a download |
| "per-item oracle **0.4277** vs best single **0.5229**" | 144 | on the same seeded 300-image sample: surya **0.4190**, tesseract_bilingual **0.5230** ≈ 0.5229, per-item oracle **0.3213** | **FAIL** — surya (0.4190) is *better* than the stated oracle (0.4277), which is impossible for a per-item minimum; 0.5229 is the tesseract-family mean, not the best single |
| "**Four** stages of the PPT pipeline are SPEC-ONLY" | 66 | the flowchart marks **5** nodes SPEC-ONLY (P1, L1, L2, R3, S1) and 2 PAUSED (T1, T3) | **FAIL** (minor, internal) |
| header date **2026-09-29** vs §1 "opened 2026-09-30" | 3, 12 | file mtime 2026-09-30 03:39 | **FAIL** (internal) |
| "19.4-point Kok gain **is** McNemar p=0.0033" | 83 | 19.4 pt = surya-vs-easyocr, p=**0.0107**; p=0.0033 = surya-vs-tesseract-family, gap **0.2196** | **FAIL** — mismatched pair |
| "consensus-entropy OCR verification (**CVPR 2026**)" | 112 | arXiv 2504.11101 record carries **no CVPR comment**; substance ✓ (training-free, inter-model agreement, routing) | **UNVERIFIED venue** |

**Reproduced exactly — 67 numeric claims.** The load-bearing ones, with commands:

| # | claim (line) | value | command |
|---|---|---|---|
| 1 | 12,324 rows (72) | 12324 | `python3 -c "import csv;print(len(list(csv.DictReader(open('level2/probe22/sheet.csv')))))"` |
| 2 | 11 model strings (72) | 11 | same, `len(set(r['model']))` → 10×1227 + sarvam 54 |
| 3 | 1,227 scored (72) | 12270 local + 54 sarvam | per-model counts above |
| 4 | 1,283 manifest (29) | 1283 | `json.load(...)['n_total']`, `len(items)` |
| 5 | 1,683 labelled = 1,283 + 400 (77) | ✓ | arithmetic; South 400 = `len(CER_STAGE3B['per_page'])` |
| 6 | South 126 of 400 (72,78) | 126 scored, 274 all-null | per_page: `all(e['cer'] is None …)` |
| 7 | 219 gt_thin / 55 mojibake (102) | 219 / 55 | `Counter(e['reason'])` over per_page |
| 8 | **13 of 22** n≥50 (79) | 13 = 12 probe22 + ta | per-language distinct `image_id` counts + South counts |
| 9 | 1 below the 5–10 floor = ml n=5 (80) | ✓ | only `ml` < 10 |
| 10 | surya 9 / tess-family 2 / easyocr 1 (83) | 9 / 2 / 1 | per-language argmin of mean CER at n≥50 |
| 11 | 7 of 12 in the 0.10–0.40 band (83) | 7 (brx hi mr or pa sa sd) | 0.10 ≤ min per-language mean ≤ 0.40 |
| 12 | Konkani 0.425 (83) | 0.4248 | `mean` of 100 kok surya CERs |
| 13 | 19.4-pt Kok gap (83) | 0.1938 = 0.6186 − 0.4248 | runner-up easyocr |
| 14 | McNemar p=0.0033, n=100 (83) | 0.003327, n_common 100 | `mcnemar_full_matrix.json` `tesseract_bilingual_vs_surya.kok` |
| 15 | 87.3909 (14) | **87.3909** | mean of the 22 blog rows I re-read from the live page |
| 16 | 6,909 total / 23 languages (12) | 23 rows sum to 6909 | HF card language table |
| 17 | **GT tier × 9** (91-93) | all 9 ✓ | see below |
| 18 | 0.171 vs 0.430, ratio 2.5× (95) | 0.1711 / 0.4296 / 2.511 | pooled `official_pair_txt` + `sarvam_bench` |
| 19 | 21 wins, all PDF-layer, none human-verified (97) | 21 PDF / 0 / 0 (surya) | per-item surya vs sarvam by tier |
| 20 | pooled 10/18 (97) | 10 = brx gu ks mai mr ne or pa sd ur | per-language mean surya vs sarvam |
| 21 | **0 of 200** Santali local predictions with Ol Chiki (140) | 0; sarvam's 3 sat rows carry 316 codepoints | count `0x1C50-0x1C7F` in `prediction`, lang `sat`, 10 local engines × 20 = **200** |
| 22 | 8 of 22 vendor-bench flips (16) | 8 | `COMPETITOR_INTEL.md:34-42` |
| 23 | Kashmiri flips 8.9 pt (16) | 52.2 − 43.3 = 8.9 | same table |
| 24 | 43.7% / 50.3% abstention (130) | 536/1227 = 43.68% · 617/1227 = 50.29% | empty `prediction` share |
| 25 | 564 of 12,324 NFC≠NFKC (117) | 564 (the `gt` column; predictions 0) | `unicodedata` per row |
| 26 | 0 exact-match flips (117) | 0 | compare NFC vs NFKC equality verdict per row |
| 27 | 0.6766 vs 0.4190, "61% worse" (136) | 0.6766 / 0.4190; 0.2576/0.4190 = 61.5% | `EDGE_THESIS.md:23`; 0.4190 independently re-derived |
| 28 | 95–100% precision, 0–5% recall (136) | 0.0–5.2% recall | `EDGE_THESIS.md:25` |
| 29 | routing gain −0.0351 (128) | ✓ | `EDGE_THESIS.md:25` |
| 30 | mixed_script False on all 12,324 (111) | all False | manifest `mixed_script` set = `{False}` |
| 31 | 1 Ol Chiki font, 1 Meetei Mayek font (114) | 1 and 1 | `find /System/Library/Fonts -iname '*OlChiki*' -o -iname '*Meetei*'` |
| 32 | tessdata 12 files, 0 of the 6 (140) | 12, 0 | `ls level2/probe22/tessdata/` |
| 33 | 66 of 400 exact (101) | **66** | `random.seed(20260926); random.sample(rows,400)` + `metrics.calculate_cer` |
| 34 | 54 specs, 19 BLOCKER (181) | 19+28+7 = 54 ✓ | `W1A_PACKET_AUDIT.md:38` |
| 35 | 12 critiques · 7 of 11 accepted · 2 rejected by all three (150) | ✓ | `MULTI_LLM_EVAL.md:35` |
| 36 | `W6_QLORA_SPEC.md:53` (132) | line 53 = Qwen2.5-VL-3B-Instruct @ 4-bit MLX primary | `awk 'NR==53'` |
| 37 | 2026-09-30 Wed · 2026-10-07 Wed · Oct 4 Sun (154-155) | ✓✓✓ | `datetime.fromisoformat` |

**The GT-tier table (check 1d) — all nine numbers reproduce, over the 54 Sarvam-paired items, stratified by `manifest.json` `gt_source`:**

```bash
python3 - <<'EOF'
import csv,json
from collections import defaultdict
rows=list(csv.DictReader(open('level2/probe22/sheet.csv')))
m=json.load(open('level2/probe22/manifest.json'))
gs={i['image_id']:i['gt_source'] for i in m['items']}
P=set(r['image_id'] for r in rows if r['model']=='sarvam_vision')
per=defaultdict(dict)
for r in rows:
    if r['image_id'] in P: per[r['image_id']][r['model']]=float(r['CER'])
L=[x for x in set(r['model'] for r in rows) if x!='sarvam_vision']
mean=lambda v: sum(v)/len(v)
for t in ['official_pair_txt','official_pdf_layer','sarvam_bench']:
    ids=[i for i in per if gs[i]==t]
    print(t,len(ids),
          round(mean([per[i]['sarvam_vision'] for i in ids]),4),
          round(mean([per[i]['surya'] for i in ids]),4),
          round(mean([min(per[i][c] for c in L) for i in ids]),4))
EOF
```

| tier | n | Sarvam | surya | best local | doc | result |
|---|---:|---:|---:|---:|---|---|
| `official_pair_txt` | 9 | 0.0641 | 0.5346 | 0.2425 | 9 / 0.064 / 0.535 / 0.243 | **9/9 PASS** |
| `official_pdf_layer` | 36 | 0.3105 | 0.2295 | 0.2285 | 36 / 0.311 / 0.229 / 0.229 | **9/9 PASS** |
| `sarvam_bench` | 9 | 0.2781 | 0.7296 | 0.6167 | 9 / 0.278 / 0.730 / 0.617 | **9/9 PASS** |

Pooled human-verified (9 + 9 = 18): Sarvam **0.1711**, best local **0.4296**, ratio **2.511** → "0.171 vs 0.430" and "2.5×" **PASS**. surya vs sarvam item-level by tier: PDF **21 win / 13 loss / 2 tie**, pair_txt **0/9/0**, sarvam_bench **0/6/3** → "every one of our 21 item-level wins sits in the PDF-layer tier, and none in either human-verified tier" **PASS**. surya's per-language mean beats sarvam's in **10/18** (brx gu ks mai mr ne or pa sd ur) → "pooled 10/18" **PASS**.

---

## 3. The 7 BLOCKERs, in the order a reader hits them

**BLOCKER 1 — §3:83, four false claims in one sentence.** "the weakest is Konkani at 0.425" (ur 0.6232, ks 0.5894, bn 0.4763 are worse); "the biggest gap we have" (hi 0.2839 > kok 0.1938); "the language we are worst at" (ur is); "Sarvam 97.41, its **third-best** Indic cell" (**rank 1 of 22**). Plus the gap is welded to the wrong p-value. This is the paragraph the CEO reads to decide whether the plan is trustworthy.
*Fix:* replace the whole sentence with the measured order and the split p-values (see check 1 / check 2a).

**BLOCKER 2 — §5:123-128, the Option A / Option D columns describe the same option.** Column A ships "per-script routing **+ R4 restoration + Sarvam API subsidy for sat/mni**" — those are **Option D's** parts per `CAMPAIGN_DIRECTIVE.md` A3/K4 and `proto-86` D2. Column A also **omits QLoRA kok+pa**, which is Option A's defining part per `proto-19` §5 and `proto-92` U4 ("Option A (wrap-only routing + QLoRA on kok+pa)"). Column D is then "same wrap, plus an explicit script-router and R4 restoration" — i.e. also Option D. The plan then **recommends A** and justifies it with the evidence row that belongs to the option with a restoration pre-pass "measured only on English/French/Spanish historical pages". Net: the recommendation rests on the wrong column's risk profile. Root `W5_STRATEGY_OPTIONS.md` (cited by the directive as Option A's source) **does not exist on disk**; only `docs/architecture/W5_STRATEGY_OPTIONS.md` does.
*Fix:* rewrite both columns verbatim from `VINAY_MEETING_PACKET.md:44` (A = wrap-only + kok/pa QLoRA + optional ₹1005 subsidy) and `CAMPAIGN_DIRECTIVE.md` A3 (D = wrap + script-router + R4 restoration + Sarvam-API subsidy); keep the recommendation and re-anchor it.

**BLOCKER 3 — §3:72, "four of the 22 languages exist as *labelled* data only" is false.** Zero languages are labelled-only: all 22 have ≥5 scored pages (min `ml 5`; probe22 min `as 19`). It also contradicts `BENCHMARK_22.md:21-22` ("22 languages, 18 from probe22 (19–100 scored items each) + 4 South tags (ta 70, te 26, kn 25, ml 5 scored of 100 labelled)"). The correct statement is the inverse: all 22 are labelled; 13 are scored at n≥50; 9 at n<50; 1 (ml) below the 5–10 floor.
*Fix:* "All 22 languages are labelled and all 22 have scored pages. Scored n runs 5–100: **13 clear n≥50, 9 sit below it, and 1 (ml, n=5) is below your 5–10 floor**."

**BLOCKER 4 — §5:132, "GLM-OCR is absent from the OmniDocBench v1.6 table it was cited in" is false.** The blog's v1.6 table lists **GLM-OCR at 94.71 overall, rank 3** (Paddle 96.01 · Sarvam 94.97 · GLM 94.71). The claim is used to shore up a backbone recommendation, and it is the exact opposite of the truth: GLM-OCR is competitive, and what is actually stale is `W6_QLORA_SPEC.md:55`'s "(OmniDocBench #1)", which refers to **v1.5**.
*Fix:* see check 3(b).

**BLOCKER 5 — §2:60, the Punjabi kill node.** "K2 pai not significant p=1.00 — FAILS, kills pa from scope" contradicts `KILL_CRITERIA.md:56` and `W6_QLORA_SPEC.md:75` (both "pa K1 SURVIVES, p<0.0001") **without saying so**, and its conclusion is wrong (pa beats 5 of 10 engines at p=0.0). "K2" is also the wrong criterion label — `KILL_CRITERIA.md`'s K2 is the micro-repair time/purge gate. The plan may be right and its sources wrong; that is the most defensible possible finding and it must be **stated as a correction**, not smuggled into a flowchart node. Note `VINAY_MEETING_PACKET.md:44` still says "Konkani + Punjabi QLoRA".
*Fix:* see check 9(a); add a line to §5 and mirror it to the packet (proto-86's "After applying").

**BLOCKER 6 — §4:114, GlotOCR's stated conclusion is reversed.** The plan says GlotOCR "shows the binding constraint on rare scripts is **font availability, not model quality**". The paper says the opposite: "Performance broadly tracks **script-level pretraining coverage**, suggesting that current OCR systems rely on **language model pretraining** as much as on visual recognition." The "low tier: median 1 font per family" figure is not in the abstract. §6:142 then builds the plan's only surviving edge on the reversed claim ("The constraint is fonts — we have one typeface for each").
*Fix:* attribute the finding to the paper: "GlotOCR shows performance tracks script-level **pretraining coverage**; its images are rendered from Google Fonts, so it measures font coverage as a controlled variable, not as the binding constraint. Our font-count observation is ours, not theirs." Keep the 1-font-each fact — it is independently measured and correct.

**BLOCKER 7 — §6:140 + §8 Q5, the single ask is inflated 3×.** "`tessdata/` has none of `sat`, `mni`, `kan`, `mal`, `tam`, `tel`" is true of `level2/probe22/tessdata/` (12 files) but the plan presents a **six-language** download ask to the CEO. `/opt/homebrew/share/tessdata/` already holds **kan, mal, tam, tel**; `level2/research/smoke/anuvaad_tesseract/tessdata/` holds **anuvaad_kan, anuvaad_mal, anuvaad_tam, anuvaad_tel**. Only **`sat` and `mni`** need a download — which is exactly the two dead languages, and makes the ask *stronger*, not weaker.
*Fix:* "Only `sat` and `mni` are missing. `kan`/`mal`/`tam`/`tel` traineddata is already on disk at `/opt/homebrew/share/tessdata/` and in the anuvaad smoke tessdata; the gap is that `level2/probe22/tessdata/` never had them and the scorer did not look there." Drop the "also worth checking whether tam/tel/kan/mal exists in the same pack" clause from Q5 — it is answerable from disk today.

### Non-blocking, but fix before the meeting
- §4:113 "57 Maltese pages" has no source; the abstract says a 422-paragraph dev set. Drop "57" or cite the page.
- §4:112 venue "CVPR 2026" for arXiv 2504.11101 is unverified (no venue in the arXiv record). Write "arXiv 2504.11101, v4 2026-05-06" and add the ID to the appendix URL list.
- §6:144 the oracle pair. On the seeded 300-image sample I get surya **0.4190**, tesseract_bilingual **0.5230**, per-item oracle **0.3213** — so "oracle 0.4277 vs best single 0.5229" cannot both be true, and "best single" is the tesseract-family mean, not surya. The 67% / 0.0332 sa-decomposition inherits the defect. Restate as "surya 0.4190 vs per-item oracle 0.3213 on a seeded 300-image sample, n=300" and re-derive the sa share before keeping 67% / 0.0332.
- §3:81 "8" with 7 items listed; add `kn 25` and reconcile to `BENCHMARK_22.md`'s 9.
- §3:102 "gt_thin at GT<200 chars" — observed max is 178; the JSON's own `definition` field says <200. Quote both.
- §3:101 "100 of 400" → 110 at 1e-4 / 111 at 5e-4, and **state the tolerance**.
- §8 Q7 "~1,195 lines" → 1,995 (1,834 src + 161 tests).
- §3:81 "no winner claim" and §3:80 "below floor" overlap confusingly; merge into one "9 languages below n=50, of which ml=5 is below the floor".
- §8: add **U14** (surya's modified OpenRAIL-M "$5M funding/revenue" cap — a CEO decision, per `docs/legal/LICENSE_AUDIT.md`) and **U13** (handwriting/low-quality scope; our 1,283 items are 100% printed, 0 tables, 983 quality "unknown"). Add U15 as a stated correction.
- §7 could carry proto-86 D13: the OpenCode leg can be run from any session with the `opencode` MCP, or the boss can paste `CHATGPT_EVAL_PROMPT.md` into OpenCode.
- Header date 2026-09-29 → **2026-09-30**; §4:108 "opened on 2026-09-29" → "2026-09-29/30".
- 12 of `proto-86`'s 13 defects are still unapplied (only D1, the GT-tier table, landed). D6 is now answerable: the indic-ocr README **does** state the pack includes Ol Chiki and Meetei Mayek — update the tag from "UNVERIFIED" to "README-confirmed; file listing + licence still to verify".
- Length: 2,661 words vs proto-19's ~1,800. §3 is 669 vs a 250 budget, §8 380 vs 150, §2 63 vs 150.

### What is genuinely strong — protect it in the rewrite
The GT-tier stratification and the "we are 2.5× behind on human-verified GT" one-liner are correct, reproducible, and the single most defensible thing in the campaign. "Zero survived" in §6, the sheet.csv provenance note in §3, the PARTIAL/honest-empty framing in §7, the UNKNOWN tag on 87.39's exact metric, the 0-of-200 Ol Chiki fact, the 87.3909 arithmetic, and the "no CER of ours is comparable to 87.39" verdict all survive scrutiny untouched. §3's option to present the tier-stratified result rather than the pooled one (Q10) is the right instinct.

---

### Sources relied on

**Files read (file:line where a specific claim was checked)**
- `docs/campaign/DRAFT_RESEARCH_PLAN.md` — the deliverable, 183 lines, all sections
- `docs/campaign/CAMPAIGN_DIRECTIVE.md:19-117` (Part A: A1 clock, A2 lead's asks, A3 K1-K7, A4 1,227 vs 1,283, A5 1,683/126/400, A8 barred paths)
- `docs/campaign/protocols/proto-19-w1h-draft-research-plan.md` — 9-section structure + word budgets + honesty rules
- `docs/campaign/protocols/proto-64-meeting-day-finish.md` — step 6, the six mandatory additions
- `docs/campaign/protocols/proto-86-draft-plan-fixes.md` — 13 monitor defects D1-D13 (D2 Option A/D swap, D3 Punjabi K1, D4 McNemar definition, D7 tessdata, D12 Sarvam-97.41 metric mixing)
- `docs/campaign/protocols/proto-92-boss-decisions.md:15-29` — U1-U15
- `docs/campaign/BENCHMARK_22.md:10,14,21,22,25,26,31-58,173,175` — 22-lang table, labelled vs scored, 13 of 22, ml=5, no-winner-claim flags
- `docs/campaign/COMPETITOR_INTEL.md:10,25,34-42,46,56-67` — 87.39 = word accuracy 100×(1−WER), n=6,609, 87.3909, the 9-row flip table, the 10-row comparability table
- `docs/campaign/EDGE_THESIS.md:1-70` — 4 theses / 0 survivors, 0.6766 vs 0.4190, 61% worse, 95-100%/0.0-5.2%, −0.0351, 0 of 200, oracle 0.4277/0.5229, 67%/0.0332, §4 66/400 + 100/400 @5e-4, fonts, URL list
- `docs/campaign/MULTI_LLM_EVAL.md:5-50` — 3 legs (1 NOT RUN tool, 1 NOT RUN budget, 1 PENDING), 11-row disposition, "7 of 11", #2 and #5 rejected, 12 critiques
- `docs/campaign/checkpoints/W1_reports/1G_verify.md:1-20` — 54/54 specs, 62/62 edit pairs
- `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md:38,116,235,246-285` — 54 specs = 19 BLOCKER + 28 MAJOR + 7 MINOR
- `docs/research/level7/KILL_CRITERIA.md:50-60` + §K2 — kok 0.32 stale, pa "SURVIVES p<0.0001, 88 discordant", K2 = micro-repair gate
- `docs/research/level7/W6_QLORA_SPEC.md:53,55,75` — Qwen primary (line 53 ✓), GLM-OCR "(#1 of tested)", pa "SURVIVES p<0.0001", kok gap 0.194
- `docs/architecture/PPT_SPEC.md:11-16,31-36` — the 4-stage / 0-3b pipeline the plan's flowchart mirrors
- `docs/architecture/W5_STRATEGY_OPTIONS.md:79-80` — Option D, K1 risk
- `VINAY_MEETING_PACKET.md:44,119,124,144,226,290,305,313,320` — Option A definition, the "2.5x lower" GT-tier sentence, "Konkani + Punjabi QLoRA"
- `OCR_AGENT_MEMORY_FEED.md:132,1004-1015,1067-1070` — Sarvam 87.39, per-lang table, 6,909 blocks
- `DISPATCH_LOG.md:156-159,184` · `BOSS_CONCERNS.md:373-395,528` · `PAPERTHIN_AUDIT.md:73,87,132-147,199` — 19.4-pt provenance, the 32-pt error's history
- Raw data: `level2/probe22/sheet.csv` (12,324 rows / 11 model strings) · `level2/probe22/manifest.json` (1,283, `gt_source` 825/300/158) · `level2/reports/CER_STAGE3B.json` (400 per_page, 126 scored, 219 gt_thin / 55 legacy_mojibake) · `level2/probe22/scores/mcnemar_full_matrix.json` (kok surya-vs-tess p=0.003327 n=100; pa surya-vs-tess_i p=1.0 n=90 ties 87; pa surya-vs-easyocr p=0.0 n=90) · `level2/probe22/metrics.py:545-565` (`calculate_cer`, capped at 1.0) · `level2/probe22/tessdata/` (12 files) · `/opt/homebrew/share/tessdata/` (kan mal tam tel present) · `level2/research/smoke/anuvaad_tesseract/tessdata/` (anuvaad_kan mal tam tel) · `/System/Library/Fonts/Supplemental/NotoSansOlChiki-Regular.ttf` + `NotoSansMeeteiMayek-Regular.ttf` · `src/` (15 files, 1,834 lines) · `tests/test_basic.py` (161 lines)

**URLs opened (6)**
- `https://huggingface.co/datasets/sarvamai/indic-ocr-bench` — 6,909 / 23 languages / semantic block level / "reviewed twice by human language experts" / `Word Accuracy = 100 × ( 1 − WER )` / ambiguous-GT and runaway-repetition exclusion; 23 language rows sum to 6,909
- `https://www.sarvam.ai/blogs/sarvam-vision-2-1` — full 22-row Indic table; Konkani 97.41 (rank 1) · Kashmiri 54.82 · Odia 80.01 · Santhali 53.91; "6,909 samples (6,609 spanning 22 Indian languages; 300 in English)"; **22-row unweighted mean re-derived = 87.3909**; OmniDocBench v1.6 table including GLM-OCR 94.71; olmOCR-Bench OldScan 55.3
- `https://arxiv.org/abs/2504.11101` — "Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR"; training-free inter-model agreement, verification, best-output selection, adaptive routing; **no CVPR venue in the record**
- `https://arxiv.org/abs/2607.00250` — "LV-ROVER-MLT… five deterministic Tesseract configurations… Maltese-specific diacritic-restoration gate"; 422-paragraph DocEng 2026 dev set; **held-out result under organiser embargo, not reported**; working paper
- `https://arxiv.org/abs/2604.12978` — "GlotOCR Bench"; **"Performance broadly tracks script-level pretraining coverage"** — not font availability
- `https://github.com/indic-ocr/indic-ocr.github.io` — README: tessdata "include **Ol Chiki (Santali)** and **Meetei Mayek (Manipuri)** scripts too"; size and licence not stated

### UNRESOLVED

1. **The fusion-ceiling numbers (§6:144) are not reproducible and the doc is internally impossible as printed.** I cannot recover 0.4277 / 0.5229 by any sampling variant I tried; the variant that reproduces `EDGE_THESIS`'s own 0.4190 gives oracle **0.3213**, surya **0.4190**, tesseract_bilingual **0.5230**. Either the oracle or the "best single" label is wrong, and the 67% `sa` share and 0.0332 ex-`sa` inherit the defect. Needs the original seed and item list from 1E_lensB.
2. **"57 Maltese pages" (LV-ROVER-MLT)** — not in the abstract (422-paragraph dev set). Needs a page cite or deletion.
3. **CVPR 2026 venue for arXiv 2504.11101** — no venue in the arXiv record. Needs the proceedings page.
4. **GlotOCR "median 1 font per family"** — not in the abstract. Needs the paper's low-tier table, or the claim becomes ours-only.
5. **The indic-ocr pack's licence and file listing** — the README names the two scripts; the `~2–4 MB` figure has no source; the licence is unverified and is a hard gate on the download ask.
6. **Who is right about Punjabi?** The matrix (p=1.0 vs tesseract_indic) and `proto-86` D3 say the tie is real and `KILL_CRITERIA.md:56` / `W6_QLORA_SPEC.md:75` are wrong. I confirmed the matrix. I did not re-run McNemar; I read the stored result. `VINAY_MEETING_PACKET.md:44` still carries the superseded "Konkani + Punjabi QLoRA" and needs the mirror fix proto-86 requires.
7. **"43 files carry a wrong weekday" (§8:154)** — inherited from the directive's "at least 43 docs"; my grep for `Wed 2026-10-01` returns **49** files. The plan states 43 as exact. Low risk, but say "at least 43".
8. **`1D` report does not exist on disk** (`docs/campaign/checkpoints/W1_reports/` holds only 1E_hunt, 1E_lensA/B/C, 1F_onepager, 1G_verify). §1 and §4 lean on "1D's comparability table"; that content is in `COMPETITOR_INTEL.md` §2, which the plan does cite. Worth a one-line note so a reader looking for 1D is not left hanging.
9. **The 87.3909 arithmetic is mine and Sarvam's blog does not print it** — the blog prints "Overall accuracy 87.39" only. My 22-row mean matches to 4 dp, so the derivation is sound, but the plan should say "unweighted mean of the 22 rows on their blog table", which is what `COMPETITOR_INTEL.md:10` says, not "on the benchmark card" (§1:12 attaches the card to the surrounding facts and could be read as attaching it to 87.3909 too).
