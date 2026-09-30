# 1E — LENS A ADVERSARIAL REVIEW: "THE INCUMBENTS ALREADY DO IT"

Agent: adversarial lens (a). Run 2026-09-29, after the W1 STOP.
Web tools available and used: `parallel-search_web_search`, `parallel-search_web_fetch`. **All incumbent checks below are live.**
Mandate: default to REFUTED. Never invent a URL, title, number or benchmark. Honest-empty is correct.

**This file is the only thing I wrote. Nothing in `src/` was run. No download. No Sarvam call. No repo file edited.**

---

## 0. HEADLINE

**0 of 4 theses survive into a CEO meeting as written.** One (C4) survives as a 0.5-day data-hygiene action with a
*corrected and smaller* claim, and its stated value proposition is factually inverted. Two (C1, C2) are killed by
published prior art **plus** by numbers on our own disk that do not reproduce. One (C3) is killed outright by a
**CVPR 2026** paper that is the thesis, generalised.

The answer to the "ALSO ANSWER" question is the single most damaging fact in this report: **on all three of the
cheap-move questions, the field has already published something.**

| Cheap-move question | Answer found live | Consequence |
|---|---|---|
| Anyone scoring Indic OCR **by script block**? | **YES** — Sarvam Indic OCR Bench is explicitly *semantic-block*-level and states it is built to avoid whole-page scoring. MDIW-13 (2024) does script ID at **block** level. UniLipi (Aug 2026) reports **per-script CER** for 13 scripts. | C1's premise is false and its "nobody does it" claim is dead. |
| Anyone reporting an **abstention / error rate**? | **YES** — Sarvam's own scorer emits `missing_prediction_count`, `loop_failure_count`, `valid_samples_cer/wer`. arXiv 2606.29213 (Jun 2026) argues median + catastrophic-rate over the mean. arXiv 2511.19806 measures abstention accuracy on OCR. arXiv 2409.04117 measures OCR error *detection* with calibration metrics. | C3's reporting novelty is nil. |
| Anyone with an **orthography-validity verifier**? | **YES** — Unicode UAX #29 already specifies the Indic grapheme-cluster rules; ICDAR 2017 "Script Grammar Learning" for Brahmic; ICDAR 2017 LSTM error detection *with abstention*; Aksharamukha ships orthographic conventions for 120+ scripts. | C2's "Indic analogue nobody has built" is false. |

---

## 1. VERDICT TABLE

| # | Thesis | Verdict | The specific incumbent / publication that already does it (URL opened + date) | Strongest evidence I found | Single best counter-argument to my kill |
|---|---|---|---|---|---|
| **C1** | **Script-block attribution.** "Every Indic OCR benchmark scores a whole page… nobody reports per-script-block accuracy." `sat` is saturated at the 0.457 monolingual floor = surya's 0.459. | **REFUTED as stated** (mechanism survives as a metadata repair) | 1) **`sarvamai/indic-ocr-bench` dataset card, opened 2026-09-29**: "**6,909** curated text-block samples… Samples are curated at the **semantic block level** so that models are evaluated on coherent units of text rather than **full noisy pages**." 2) **Sarvam Vision 2.1 blog, 24 Sep 2026** (`https://www.sarvam.ai/blogs/sarvam-vision-2-1`): "6,909 samples (6,609 spanning 22 Indian languages; 300 in English)"; per-language accuracy table. 3) **MDIW-13**, `https://arxiv.org/pdf/2405.18924`: "the script of the document, **block**, line, or word is estimated, and secondly, the appropriate OCR is used." 4) **UniLipi**, `http://arxiv.org/pdf/2608.28195` (arXiv:2608.28195v1, 28 Aug 2026): Table 1 "**Script-wise performance**… CER (%) for OCR transcription" per script, 13 scripts. 5) **GlotOCR Bench**, arXiv:2604.12978 (14 Apr 2026) + `https://github.com/cisnlp/glotocr-bench`: results are released "per-script, per-language, and tier-level". | **The floor arithmetic does not reproduce on our own data.** `level2/probe22/sheet.csv`, parsed with the `csv` module (12,324 rows, 11 models, 18 langs): across the 20 `sat` items the per-item Ol Chiki character share is **min 0.000, median 0.406, mean 0.443, max 0.815** — so a perfect-Ol-Chiki-recogniser floors at **≈0.557** mean CER, while **surya's `sat` mean CER is 0.7621**. The cell has **≈0.205 of headroom above the floor; it is not saturated.** 1E-hunt's 0.543 / 0.457 / 0.459 triple is not reproducible at item level (per-item floors span 0.185 → 1.000). Second: `sheet.csv` **already has a `script` column and a `mixed_script` column**; `mixed_script` is **`False` on all 12,324 rows**, and 19 of 20 `sat` items are labelled `script=Ol Chiki` while their own `gt` is 56% non-Ol-Chiki. The "1-day mechanism" is a broken-metadata fix plus a groupby on an existing column. | Per-*script* scoring **inside a mixed-script page** is still genuinely unpublished: GlotOCR's per-script numbers are on single-script rendered sentences (its seed data is per-script sentence CSVs), UniLipi and Sarvam score single-script blocks by construction, and MDIW-13 *identifies* script at block level but does not score CER per block. So the measurement is real work — but it is a 0.5-day metadata correction, not an edge, and it yields no "we beat Sarvam" claim. |
| **C2** | **Akshara-validity-gated fusion.** 300 lines of orthography rules turn a character vote into a gated vote, 2 days, no training, no download. | **REFUTED as novel** (an engineering increment on 2016–2017 prior art, with a false cost claim) | 1) **Unicode UAX #29**, `http://www.unicode.org/reports/tr29` (live; the 44th-draft PDF at `unicode.org/L2/L2024/24036-uax29-44-draft-pri494.pdf` is dated 10 Jan 2024): ZWNJ is in the `Extend` class "in Bangla, Khmer, Malayalam, and Odiya"; spacing Indic vowel signs are continuing characters; rule **GB9c** for conjuncts. Implemented in ICU and Python `regex \X`. 2) **Aksharamukha** (IIIT Bangalore), `https://pypi.org/project/aksharamukha`: "implements various script/language-specific **orthographic conventions**… vowel lengths, gemination and nasalization", 120+ scripts incl. **Santali (Ol Chiki)** and **Meetei Mayek**, 21 romanizations. 3) **"Improving Classical OCRs for Brahmic Scripts Using Script Grammar Learning"**, Ganguly/Agarwal/Chaudhury, ICDAR 2017 pp. 37–41, DOI 10.1109/ICDAR.2017.363 — the mechanism, verbatim, published. 4) **"Error Detection and Corrections in Indic OCR using LSTMs"**, Saluja/Adiga/Chaudhuri/Ramakrishnan/Carman, ICDAR 2017 (`https://www.cse.iitb.ac.in/~ganesh/papers/icdar17.pdf`): "For words that need not be corrected in the OCR output, our model simply **abstains**" — i.e. verifier-plus-abstain, published. 5) **"Error Detection in Indic OCRs"**, DAS 2016, RNN word-level error detection. | "The Indic analogue nobody has built" is false **twice**: the grapheme-cluster half of the proposed 300 lines is a **Unicode standard lookup** (UAX #29 C2, GB9c), and the orthographic-conventions half is a **pip-installable library that already covers Ol Chiki and Meetei Mayek** — the two languages C2 exists to help. The **"no download" cost claim is therefore false**: using Aksharamukha is a download and needs boss approval. And the ROI is unverifiable in the window: the 0.4277-vs-0.5229 oracle gap is a seeded n=300 draw (1E-hunt's own UNRESOLVED), and 2 days is spent before any number can be shown. | The one genuinely unbuilt thing is the gate *inside a 10-engine, 22-language fusion with plurality-without-quorum*. No publication does that. But that is a deployment of 2017 prior art to a new ensemble, it costs 2 of our 5 days, and it cannot be validated before the meeting — a bad CEO bet even if it is not plagiarism. |
| **C3** | **Script mismatch as a free abstention signal**, as a per-item per-engine routing feature for a 10-engine local ensemble. | **REFUTED** — strongest kill in this report | **"Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR"**, arXiv:2504.11101 (v3/v4), **CVPR 2026 poster** (`https://cvpr.thecvf.com/virtual/2026/poster/37103`, listed 16 Apr 2026; alphaxiv record 6 May 2026). Its own abstract: "a novel uncertainty metric for OCR, quantifying prediction reliability based on **inter-model agreement**… a **training-free, model-agnostic** metric… a threshold gate determines the next step: low-entropy ensemble predictions are **accepted**, while inputs with entropy exceeding the threshold are **routed** to a stronger VLM." Its CE-Ensemble "selects the best outputs". **Script-agreement is a strictly coarser, strictly weaker special case of inter-model agreement entropy.** Supporting: arXiv:2409.04117 (OCR confidence→error detection, calibrated across Azure/Textract/Google/DocTR/EasyOCR/Paddle, reports CER/BER/ECE/AC/AUB); arXiv:2511.19806 "Reading Between the Lines: Abstaining from VLM-Generated OCR Errors via Latent Representation Probes" (+7.6% abstention accuracy); and **Sarvam's own scorer** (`indic-ocr-bench` card, opened 2026-09-29) already returns `missing_prediction_count`, `loop_failure_count`, `valid_samples_cer/wer`. | A CVPR 2026 paper whose contribution is *training-free inter-model agreement for OCR verification, output selection and thresholded routing* is C3 with the "script" word deleted and the engines made larger. A rival we would have to beat, not a hole we found. | CE is demonstrated on **VLMs**, not on 10 classical local engines. That is a real gap — but it is a *re-implementation* gap: running CE over our 10 engines is a day of work we would spend to reproduce someone else's idea, and the result would be "we reproduced CVPR 2026 on classical engines", which is not an edge a CEO should pay 1 day for. |
| **C4** | **GT script-purity gate.** 18 of 79 scored `mr` items carry Ol Chiki in Devanagari GT, adding ~+0.098 to *every* engine's Marathi score. "Honesty edge: it lowers our own scores." 0.5 day. | **WOUNDED** — the *finding* is real and broader than stated; the *claim* is falsified twice, including the sacrifice narrative | No incumbent found that gates OCR **ground truth** on script purity. Adjacent published work exists and a CEO panel will cite it: **"A survey of OCR evaluation tools and metrics"** (ICDAR HDI, `https://dl.acm.org/doi/fullHtml/10.1145/3476887.3476888`) covering the **OCR-D Ground Truth Guidelines** and Boenig et al. 2019 "Labelling OCR Ground Truth for Usage in Repositories"; **"Disentangling Human Error from Ground Truth in …"** (NeurIPS 2020 proceedings); **"OCR-Quality"** arXiv:2510.21774; **"OCR quality assessment: Beyond ground truth"** (Zenodo 7777486). None is a script-purity gate. | On disk, `sheet.csv`, `mr` + `surya`, the artefact is **wider than 1E-hunt described**: the 18 suspect items are **68.6% Devanagari** vs **92.2%** on the 61 clean items (non-Devanagari residue 31.4% vs 7.8%, including runs that match Balinese / Sundanese / Vedic-name code points). And two claims are **false**: (1) "+0.098 to **every** engine" is falsified by **doctr, which moves 0.847 → 0.873 (+0.026)**, contributing ≈+0.006 to its Marathi mean, not +0.098 — all other 8 engines move ≈+0.42; (2) **"it lowers our own scores" is backwards.** surya `mr`: contaminated 0.540 (n=18) / clean 0.120 (n=61). Dropping the contaminated items moves our Marathi error from 0.228 to **0.120**. The gate makes us *better*, and more honest at the same time. There is no sacrifice to advertise. | The contamination is genuinely ours, genuinely self-inflicted, and genuinely invisible: `mixed_script` is `False` on all 12,324 rows, so no tool we have would ever have flagged it. A 0.5-day gate that catches a real, reproducible defect in our own GT — and which the 2026-09-29 manifest additions (`mr +21`) will keep feeding — is cheap, defensible, and worth doing. Just do not present it as a sacrifice, and do not put "+0.098 to every engine" in a packet. |

---

## 2. THE THREE DISK NUMBERS THAT DECIDE C1 AND C4

All read-only, run from `/Users/srujansai/Desktop/South`, parse with Python's `csv` module (naive comma splitting is
wrong on this file: quoted fields containing commas make `awk` misreport columns — the "distinct scripts" column
returned engine names). Scripts written to the pre-approved temp dir, **not** the repo.

```
python3 <temp>/1ElensA/chk.py     # schema + row counts
python3 <temp>/1ElensA/sat.py     # sat Ol-Chiki share, mr contamination counts
python3 <temp>/1ElensA/mr.py      # surya sat/mr CER splits, per-engine mr cont vs clean
python3 <temp>/1ElensA/hist.py    # script histogram of contaminated vs clean mr GT
```

| Measurement | Value |
|---|---|
| `sheet.csv` header | `image_id, language, script, print_or_hand, quality, has_table, mixed_script, gt, model, prediction, CER, WER, error_tag` |
| rows / models / languages | 12,324 / 11 / 18 (10 local engines × 1,227 + `sarvam_vision` 54) |
| `mixed_script` values | **`False` × 12,324** (the column exists and is never set) |
| `sat` items | 20; labelled `Ol Chiki` 19, `Bengali-Assamese` 1 |
| `sat` per-item Ol Chiki char share | min 0.000 · **median 0.406** · mean 0.443 · max 0.815 · **0 items ≥ 99.9% Ol Chiki** |
| `sat` surya mean CER | **0.7621** (4 items at CER 1.000) |
| perfect-Ol-Chiki floor | **≈ 0.557** (1 − 0.443) → **headroom ≈ 0.205; cell NOT saturated** |
| `mr` items (surya) | 79 = 18 suspect + 61 clean |
| `mr` surya CER | suspect **0.5396** (n=18) · clean **0.1196** (n=61) |
| `mr` per-engine suspect→clean | surya 0.540→0.120 · easyocr 0.546→0.109 · paddleocr_indic 0.537→0.118 · tesseract_indic 0.541→0.105 · openbharatocr 0.541→0.105 · rapidocr 0.617→0.201 · indicphotoocr 0.575→0.271 · anuvaad 0.556→0.189 · **doctr 0.873→0.847** |
| `mr` GT script share | suspect **68.6% Devanagari** · clean **92.2% Devanagari** |
| Ol Chiki chars in all `mr` GT | **64** (1E-hunt reports 645 — **10× discrepancy, unresolved, must not go in a packet**) |

Two consequences the thesis authors must absorb:
1. **C1's "saturated" claim is false.** The cell has 0.205 of headroom above the monolingual floor. The correct
   statement is the opposite of the one we drafted: *no engine we run is anywhere near the Ol Chiki ceiling, and
   the reason is invisible because the cell's metadata says the pages are single-script.*
2. **C4's "lowers our own scores" is false.** Removing the contamination **improves** our Marathi error from 0.228
   to 0.120. The honest move and the flattering move coincide. Do not build a narrative on a sacrifice that does not
   exist — a CEO who asks "what did it cost you?" gets the answer "nothing, it raised our score and made it truer",
   which is a much better answer anyway.

---

## 3. INCUMBENT MAP (all opened live 2026-09-29)

| Incumbent / lab | What they ship that touches these theses | URL | Date seen |
|---|---|---|---|
| **Sarvam AI** | 6,909-block Indic OCR bench, **semantic-block-level** curation, 22 langs + English, per-language word accuracy, GT "reviewed twice by human language experts", stdlib scorer emitting `missing_prediction_count` / `loop_failure_count` / `valid_samples_*`, normalizer that **strips ZWJ/ZWNJ** and applies Indic punctuation rules. Vision 2.1 (24 Sep 2026) is SOTA on it. | `https://huggingface.co/datasets/sarvamai/indic-ocr-bench` · `https://www.sarvam.ai/blogs/sarvam-vision-2-1` · `https://www.sarvam.ai/blogs/sarvam-vision` | card opened 2026-09-29 (card self-dates 2026); Vision 2.1 blog **24 Sep 2026**; Vision 1 blog body **5 Feb 2026** |
| **GlotOCR Bench (LMU/TU Munich)** | 158 scripts, CER + **Acc@0/Acc@5 + ScriptAcc**, released "per-script, per-language, and tier-level"; explicit critique that XDocParse "focuses on **languages rather than scripts**". REAL — 1E-hunt's citation checks out. | `https://github.com/cisnlp/glotocr-bench` · arXiv:2604.12978 | **14 Apr 2026** |
| **CVPR 2026 — Consensus Entropy** | Training-free inter-model **agreement entropy** for OCR; verify / select-best / **thresholded routing** to a stronger model. Kills C3. | arXiv:2504.11101 · `https://cvpr.thecvf.com/virtual/2026/poster/37103` | poster listed **16 Apr 2026**; arXiv v4 live |
| **UniLipi (IIIT Hyderabad)** | Unified multi-script Indic HTR; **Table 1 = per-script CER** over 13 scripts + per-line glyph Count-MAE; explicitly contrasts unified modelling with "multilingual recognition as **routing mechanism**". | `http://arxiv.org/pdf/2608.28195` (arXiv:2608.28195v1) | **28 Aug 2026** |
| **LV-ROVER-MLT** | Anchor-preserving ROVER + lexicon gate + diacritic-restoration gate, Maltese, DocEng 2026 competition. REAL — 1E-hunt's citation checks out; it is the mechanism C2 generalises. | arXiv:2607.00250 (`/abs/2607.00250v3`, `/html/2607.00250v5`) | abs page **30 Jun 2026**, v5 live |
| **Can OCR-VLMs Read Devanagari? (2606.29213)** | Devanagari stress-test bench, 10 systems, "script-aware evaluation protocol (Unicode NFC; CER/WER/chrF++)", **median + catastrophic-rate** argument, negative cross-engine post-correction result. | `https://arxiv.org/html/2606.29213` · mirror repo `https://github.com/Aditya-PS-05/devanagari-ocr-benchmark` | **28 Jun 2026** |
| **MDIW-13** | Multi-lingual multi-script DB for **script identification at document / block / line / word level**. Prior art for block-level script segmentation. | `https://arxiv.org/pdf/2405.18924` | 2024 (arXiv ID) |
| **DAS 2016 (IIIT Hyderabad)** | "Multilingual OCR for Indic Scripts" — script identified at **word level prior to recognition**, 12 Indian languages + English. | `https://www.computer.org/csdl/proceedings-article/das/2016/1792a186/12OmNyoSbc3` · `http://ocr.iiit.ac.in/Hindi100.html` | **2016-04-01** |
| **ICDAR 2017** | "Improving Classical OCRs for Brahmic Scripts Using **Script Grammar Learning**" (Ganguly, Agarwal, Chaudhury), pp. 37–41 · "Error Detection and Corrections in Indic OCR using LSTMs" (Saluja et al.) with explicit **abstention** · "An Empirical Study of Effectiveness of Post-Processing in Indic Scripts". | `https://www.computer.org/csdl/proceedings-article/icdar/2017/3586h037/12OmNwCJOPV` · `https://www.cse.iitb.ac.in/~ganesh/papers/icdar17.pdf` | **2017-11-01** / ICDAR 2017 Kyoto |
| **Unicode** | UAX #29 Indic grapheme-cluster rules (ZWNJ in `Extend` for Bangla/Khmer/Malayalam/Odiya; spacing matras; GB9c conjuncts). | `http://www.unicode.org/reports/tr29` | live; 44th-draft PDF dated **10 Jan 2024** |
| **Aksharamukha (IIIT-B)** | Orthographic conventions for 120+ scripts incl. Ol Chiki + Meetei Mayek; pip-installable. The "Indic validity engine" already exists. | `https://pypi.org/project/aksharamukha` · `https://github.com/virtualvinodh/aksharamukha` | live 2026-09-29 |
| **Confidence-Aware Document OCR Error Detection** | OCR confidence → error detection, calibrated (ECE, AUB) across **Azure / Textract / Google / DocTR / EasyOCR / Paddle**. The established side-channel for OCR routing. | `https://arxiv.org/abs/2409.04117` | ID implies **Sep 2024**; the fetched page displayed 2026-08-24 — **CONTRADICTION, unresolved** |
| **Abstention via latent probes (2511.19806)** | Abstention on VLM-generated OCR errors, +7.6% abstention accuracy over best baseline. | `https://arxiv.org/pdf/2511.19806` | ID implies **Nov 2025** |
| **Datalab (Surya author)** | Live public **indic OCR leaderboard** comparing Datalab Accurate/Balanced/Fast vs dots.ocr, DeepSeek OCR, olmOCR 2, RolmOCR — a single aggregate Score per model, **no per-language table visible in the excerpt I got**. | `https://www.datalab.to/benchmark/indic` | page date not established (fetch returned a bogus 1998 footer; not used) |
| **AI4Bharat / Bhashini-IITJ IndicPhotoOCR** | Detection → **script identification** → recognition, 11 Indian langs + English, **neural confidence scores** (Apr 2026), separate 12-class script-ID models. Scene text, not documents. | `https://github.com/Bhashini-IITJ/IndicPhotoOCR` | README timeline through **Apr 2026** |
| **IndicVisionBench (Faraz et al.)** | 5K images / 37K+ QA, OCR track = **876 document images, 10 Indic languages** from Wikisource; ICLR 2026 slides. **This is the benchmark a Bhashini/qualifier conversation is most likely to name** — and it is a QA benchmark, not a document-CER leaderboard. | `https://arxiv.org/html/2511.04727` · `https://openreview.net/forum?id=LmJoLn04iL` | ID implies **Nov 2025**; ICLR 2026 poster |
| **`yingkitw/ocr`** | Hobby repo shipping `--lang auto` mixed-script pages and an `ocr benchmark` that emits **per-script CER/WER** with 8-script routing and per-script CRNN vocabularies. Not a publication; cited only as evidence the *idea* is already in public code. | `https://github.com/yingkitw/ocr` | live 2026-09-29 |
| **OCR evaluation survey (2603.25761)** | PRISMA review 2006–2025 of OCR evaluation; criticises CER/WER as collapsing fidelity to edit distance. | `https://arxiv.org/html/2603.25761v1` | ID implies **Mar 2026** |
| **ekStep synthetic Indic OCR set (2205.02543)** | 90k images / 23 Indic languages incl. Santali. Outside window; already on 1E-hunt's reject list. | `https://arxiv.org/pdf/2205.02543` | 2022 |
| **Bodhan · Google DocAI · Azure Document Intelligence · Amazon Textract · LightOn · PaddleOCR-VL · Surya · GlotOCR(model) · Chitrapathak** | **No check completed.** I ran out of query budget before individually opening vendor pages for these. Google/Azure/Textract are *indirectly* covered above: Textract/Azure/Google confidence is the subject of arXiv:2409.04117, and Google Document AI is one of the three baselines there. PaddleOCR-VL and Surya appear as *rows in Sarvam's leaderboard* (Sarvam Vision 1 blog table, Feb 2026) rather than as independent checks. **These are UNKNOWN, not cleared.** | — | — |

---

## 4. WHAT A SURVIVING CEO PACKET WOULD LOOK LIKE

If the lead insists on taking something from this wave, the only defensible items are:

1. **Repaired `sat` metadata + a `mixed_script` audit (0.5 day, folded into C4's gate).** Fact, not edge: 19 of 20
   `sat` items are labelled `Ol Chiki` while 56% of their characters are not Ol Chiki, and `mixed_script` is
   `False` on all 12,324 rows. This is the kind of defect that, if a CEO finds it themselves, ends the meeting.
2. **The corrected `sat` statement.** Not "the cell is saturated at 0.457". The true statement: *our best local
   engine scores 0.762 on `sat` against a monolingual floor of 0.557 — a 0.205 gap that no metric we currently
   report can see, because the cell is mislabelled as single-script.* That is more interesting than the thesis we
   drafted, and it is true.
3. **The Marathi gate, framed as data hygiene, not sacrifice.** "18 of 79 scored Marathi GT items contain ~31%
   non-Devanagari residue; every engine except one converges to CER ≈0.54 on them; removing them moves our Marathi
   CER 0.228 → 0.120. We found this in our own GT and we are fixing it before it reaches a leaderboard."
4. **C3 as a positioning note, not a build:** "we considered a script-agreement routing feature; CVPR 2026's
   Consensus Entropy already generalises it. If we ever do routing, we do CE." One sentence. Zero days.

**C2 gets zero days.** Two of five development days on a 2017 mechanism, with a false "no download" cost line, an
unverifiable n=300 oracle gap, and no deliverable demonstrable before the meeting.

---

## 5. QUERIES RUN (all via `parallel-search_web_search` / `parallel-search_web_fetch`, 2026-09-29)

Search calls (8), with the queries each carried:
1. *per-script OCR metric / multi-script page* → "OCR benchmark per-script error rate multilingual document"; "script-wise accuracy OCR evaluation Indic multi-script page"; "per-script CER separate Latin Devanagari OCR benchmark"; "multi-script document OCR evaluation script segmentation block"
2. *GlotOCR + LV-ROVER-MLT verification* → "GlotOCR Bench arXiv 2604.12978 ScriptAcc"; "GlotOCR benchmark TU Munich cross-script hallucination"; "LV-ROVER-MLT arXiv 2607.00250 ROVER Maltese"; "ROVER multi-engine OCR voting DocEng 2026 competition"
3. *Indic post-processing / grammar prior art* → "Improving Classical OCRs for Brahmic Scripts Script Grammar Learning ICDAR 2017"; "Error Detection and Corrections in Indic OCR Using LSTMs ICDAR 2017"; "Empirical Study Effectiveness of Post-Processing in Indic Scripts ICDAR"; "script grammar learning OCR valid character sequences Devanagari"
4. *Sarvam's own benchmark* → "Sarvam AI indic-ocr-bench benchmark 22 languages 6909 blocks"; "Sarvam Vision 2.1 Indic OCR benchmark technical report evaluation"; "indic-ocr-bench huggingface Sarvam dataset details"; "Sarvam AI Indic OCR model card language wise CER"
5. *abstention / confidence* → "OCREval end-to-end metric empty prediction penalty under-recognition"; "OCR abstention rate benchmark report refusal empty string"; "document OCR confidence score abstain when unreadable Amazon Textract Azure"; "Google Document AI language script detection OCR"
6. *GT quality / purity* → "OCR ground truth annotation errors quality audit benchmark noisy labels"; "ground truth contamination wrong script characters OCR dataset filter"; "OCR benchmark label noise character error rate evaluation distortion"; "Indic OCR dataset ground truth verification human review quality"
7. *Indic validity libraries* → "indic-nlp-library orthography valid character sequences syllabifier rules"; "Aksharamukha Brahmi transliteration validation Indic text rules"; "Unicode UAX29 grapheme cluster validity check Indic conjunct virama rules library"; "Indic text validation library terminal virama orphan ZWJ ZWNJ check"
8. *IndiaAI/AI4Bharat benchmarks* → "IndicVisionBench OCR Faraz 2025 benchmark IndiaAI 22 languages"; "AI4Bharat IndicPhotoOCR benchmark 22 scripts"; "Indic OCR benchmark IndiaAI Sarvam Datalab comparison 2026"; "IndicVisionBench Bhashini OCR evaluation harness"
9. *within-page multi-script scoring* → "multi-script page OCR evaluation score each script region separately"; "code-mixed document OCR per-script accuracy error rate regional"; "bilingual raster page Indic OCR benchmark script block level error"; "IndicSTR13 scene text script recognition dataset per script"
10. *script agreement as error signal* → "script agreement between OCR engines confidence signal routing ensemble"; "wrong script output detection abstention select best OCR engine"; "selective prediction OCR quality estimation per engine routing"

Fetches (opened, excerpt/full): `https://huggingface.co/datasets/sarvamai/indic-ocr-bench` ·
`https://www.sarvam.ai/blogs/sarvam-vision-2-1` · `https://www.sarvam.ai/blogs/sarvam-vision` ·
`https://www.datalab.to/benchmark/indic` · `https://arxiv.org/abs/2409.04117` · `http://arxiv.org/pdf/2608.28195`.

## 6. UNRESOLVED

- **Ol Chiki char count in `mr` GT: 64 (mine) vs 645 (1E-hunt).** 10× apart. My count is a straightforward scan of
  U+1C50–U+1C7F over all 79 surya `mr` rows. If 1E-hunt's number is right, my contamination *mechanism* (which
  measures 31.4% non-Devanagari residue) may be right while its *labelling* of the residue as "Ol Chiki" is wrong.
  **Must be resolved before any number reaches the packet.**
- **1E-hunt's `sat` 0.543 / 0.457 / 0.459 triple does not reproduce.** I measure mean Ol Chiki share 0.443 → floor
  0.557, and surya `sat` = 0.7621. Their sat n, engine set, or block range differs from mine. Until reconciled, the
  "monolingual floor equals the observed score" coincidence should be treated as **CONTRADICTION, not fact** — it
  happens to be the rhetorical centre of C1.
- **Sarvam Indic OCR Bench version churn.** Blog of 5 Feb 2026 says "20,267 samples"; Vision 2.1 blog of 24 Sep 2026
  and the HF card say "6,909 (6,609 + 300 English)". The team's brief (6,909 blocks, 22 langs + English) matches the
  **current** card. I did not find a changelog explaining the 20,267 → 6,909 change. **UNKNOWN.**
- **Does any Sarvam block contain more than one script?** The card exposes only `image`, `image_name`, `gt`,
  `language`. If their blocks are script-pure, their per-language table is a proxy for per-script and C1's
  measurement is still additive to *their* bench. Not established. **UNKNOWN.**
- **Datalab's indic benchmark internals.** The excerpt shows one aggregate Score per model and nothing else. Whether
  it has a per-language breakdown, an empty-output policy, or a hidden corpus is **UNKNOWN** — worth one fetch
  before the meeting because a third-party public Indic leaderboard is a positioning risk.
- **arXiv:2409.04117 date contradiction.** The identifier implies September 2024; the abstract page I fetched
  displayed 2026-08-24. Not resolved. Content is unambiguous either way; only the date is uncertain.
- **Not individually checked (UNKNOWN, not cleared):** Bodhan, Google Document AI product page, Azure Document
  Intelligence product page, Amazon Textract product page, LightOn, PaddleOCR-VL, Surya (as a product), the GlotOCR
  *model*, Chitrapathak, and IndicPhotoOCR's per-script metrics. Two of these (Google/Azure/Textract confidence) are
  covered only *indirectly* via arXiv:2409.04117, which treats them as baselines.
- **GlotOCR's images are single-script by construction** (per-script sentence CSVs → rendering pipeline), so its
  per-script tables cannot be read as within-page per-script scoring. I inferred this from the repo's dataset README;
  I did not read the paper's evaluation section. **INFERRED, not PRIMARY.**
- **The C2 ROI is unmeasured.** The 0.4277 oracle / 0.5229 surya / 0.5519 ROVER-lite figures come from 1E-hunt's
  seeded n=300 draw, which 1E-hunt itself lists as UNRESOLVED. I did not re-run it. The fusion gap is the entire
  justification for spending 2 days and I cannot vouch for it.
- **`quality` and `print_or_hand` are `unknown`/`printed` on all 79 `mr` rows**, so I could **not** test the obvious
  confound for C4 (are the 18 suspect items simply harder scans?). The `doctr` flatness (0.847 → 0.873) is partial
  evidence that contamination is *not* uniform across engines, but the difficulty confound is **not excluded** —
  the non-Devanagari residue could be a symptom of a different, harder source document rather than a decoding
  artefact. The gate is still correct; the *causal story* is not proven.
