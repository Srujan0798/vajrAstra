# COMPETITOR_INTEL — consolidated + live re-verified 2026-09-29

**W1D research subagent.** **PRIMARY** = opened this run · **DERIVED** = arithmetic on PRIMARY · **UNKNOWN** = unconfirmed. `LIVE_LATEST_2026-09-29.md` and `docs/research/LIVE_LATEST_2026-09-29.md`: **byte-identical** (`diff -q` silent).

---
## 0. SIX THINGS THAT CHANGE THE MEETING

**0.1 C12 RESOLVED — bench GT is HUMAN-REVIEWED TWICE.** HF card, verbatim: *"All ground-truth text has been **reviewed twice by human language experts** to ensure linguistic accuracy before inclusion in the final benchmark."* `CAMPAIGN_DIRECTIVE.md:91-93` logged open. Our 158 `sarvam_fill` items carry `gt_source: sarvam_bench` (MEASURED), so the "machine GT" label is wrong; the mni/sat BARRED verdicts are more likely a **verifier-competence artefact**. **§6.4 stays LOCKED** — evidence only.

**0.2 What 87.39 is.** **word accuracy = 100 × (1 − WER)** · **n in the headline = 6,609 (22 Indic languages); English (300) is EXCLUDED** · **unweighted macro over the 22 rows** · per-language n spans 207 (Manipuri) – 471 (Assamese). DERIVED: Sarvam's 22-row mean = **87.3909** → 87.39; Bodhan's = **84.9368** → 84.94; n-weighted Sarvam = 87.84. **The headline is a 22-language macro-average, not a score over 6,909 items** — a model scoring 0 on all 300 English samples still gets 87.39. UNKNOWN: `word_accuracy` or `valid_word_accuracy`.

**0.3 87.39, 87.3 and "OldScan 55.3" are three different things.** 87.39 = Indic OCR Bench, Indic word accuracy, Sarvam's own bench. 87.3 = olmOCR-Bench — blog: *"This benchmark is officially English-only. However, it contains some contaminant samples in Chinese and others"* — pass-fail, not accuracy. **"OldScan 55.3" is a CATEGORY, not a language** (degraded old scans) inside English-only olmOCR-Bench; Bodhan's card scores it 49.8 (Sarvam) / 48.3 (itself) / 42.8 (Surya). `R6:141`'s "**our** OldScan 55.3" is a mislabel: it is Sarvam's.

**0.4 A second vendor bench exists, and 8/22 per-language winners FLIP.** Bodhan publishes **IndicOCR-PR** (printed) and **IndicOCR-HW** (handwriting) — same formula 100×(1−WER), different self-built corpus. Table in §1: headlines move Sarvam 87.39 → **86.6**, Bodhan 84.94 → **86.2**; on Bodhan's own bench the margin is **0.4 pts, not 2.45**.

**0.5 Bodhan is ~0.83B, released 5 Sep 2026, and "84.94" is not Bodhan's number.** **33 M** IndicDocLayout (PP-DocLayoutV3/RT-DETR, 37-class education taxonomy) + **0.8 B** IndicBlockOCR (Qwen3.5-0.8B, bf16) = **~0.83 B**; `LIVE_LATEST:221` and `DEEPER:93` ("~3B") are **wrong**. Release **5 Sep 2026** (vendor X post "Live on Bodhan AI: 05.09.2026"; HF "5 Sep 2026 release"); `LIVE_LATEST:136` (Sep 4) and `DEEPER:222` (Sep 12) are **both wrong**. **84.94 is Sarvam's score for Bodhan on Sarvam's bench**; Bodhan's own number is **86.2**, and "82.85 mni" is Bodhan-on-Sarvam's-bench (on its own bench: Bodhan 83.8, Sarvam 81.9 — sign flips). Price **₹0.20/image** — PRIMARY, `console.bodhan.ai`: "indic-ocr · Document OCR, whole page to markdown · image · **₹0.20 / image**"; "*Every new account starts with ₹10 of credit. No card needed*" = 50 free pages, **but that needs an account → boss decision**. **Indic Open Model License v1.0 — not open source**: attribution + share-alike + "*Ask before hosting it for others*" (API sign-off unless nonprofit/govt/academic or an equal open-sourced in 90 days) + 500M MAU / $250M revenue; access is a **contact click-through gate**; it embeds the **Sarvam-30B tokenizer**. "15M+ docs" is a **vendor tweet**, not a card claim.

**0.6 The overlap challenge is real, public and unaddressed.** Full Krrish Agarwalla comment on Sarvam's own post: *"…we built one ourselves, and naturally ( because of similar training data ) our model performs very well on it. But this also raises the question… if you build the benchmark and then show that your own model performs best on it, how do you know the benchmark is actually measuring generalization rather than alignment with your training data?"* `LIVE_LATEST:17` quotes only the first sentence. A second commenter independently alleges the headline "is a really cunning idea to hide our real capablity" — **allegations, not facts**. Sarvam calls it "**our own** Indic benchmark"; the blog states **no decontamination procedure**. UNKNOWN whether overlap exists.

---

## 1. COMPETITOR BLOCKS

**Sarvam Vision 2.1** — *Arch:* harness-with-VLM, 3B state-space VLM + semantic layout parser + pointer reading-order network (the "3B" is from `docs.sarvam.ai` via `DEEPER:215`, not the blog). *Training:* SFT → RLVR on new KV-extraction + handwriting corpora. *Numbers:* 87.39 · 87.3 · 94.97 (above). *Self-admitted:* "*-they are saturated*"; "*there is a question of the generality of such evaluations: the correlation between a strong result on a benchmark vs. real-world usefulness*". *Overlooked:* no decontamination statement; every competitor figure is "*a system evaluated by us … under one harness*"; no per-language n or CIs. **Confidence HIGH on the numbers, LOW on external validity.**

**indic-ocr-bench as an instrument** — 6,909 `test` + 1,173 `small_representative` (51/lang, "stratified by word length"); 23 langs; apache-2.0; **semantic-block level** — "PNG crop of the text block", "*coherent units of text rather than full noisy pages*". Scorer `metrics.py`, stdlib-only, NFC/NFKC + whitespace/quote/dash/Indic-punctuation folding, strips HTML, bullets, ZWJ/ZWNJ. **Two self-declared choices:** (1) "*Samples with ambiguous ground truth … are excluded*"; (2) loop-flagged predictions are "**excluded from valid-sample metrics**" — a degenerate output is **dropped, not scored 1.0**. *Overlooked:* vendor-built, released the same day as the model that tops it; block-level — no page layout, reading order, tables-in-context or multi-page; handwriting is a blog **demo**, never benchmarked. **Confidence HIGH that it is well-made; LOW that it is neutral.**

**Bodhan IndicOCR** — §0.5. *Self-admitted:* "*Reading order remains a challenge for complex, multi-column layouts. Handwriting recognition is also still being improved*". Second vendor bench, Sarvam/Bodhan:

| lang | Sarvam-bench | Bodhan-bench | |
|---|---|---|---|
| Kashmiri | 54.82 / 48.04 | 43.3 / **52.2** | **FLIP −8.90** |
| Manipuri | 85.12 / 82.85 | 81.9 / **83.8** | **FLIP** |
| Assamese | 90.88 / 89.41 | 89.5 / **90.2** | **FLIP** |
| Bodo | 90.48 / **90.69** | 91.0 / 86.5 | **FLIP** |
| Hindi | 93.52 / 90.99 | 95.7 / **96.0** | **FLIP** |
| Punjabi | 89.16 / 86.51 | 92.2 / **93.2** | **FLIP** |
| Gujarati, Konkani | 88.87 / 83.26 · 97.41 / 95.99 | 91.6 / **91.7** · 93.6 / **93.7** | **FLIP** |
| Santhali | 53.91 / **68.30** | 71.9 / **74.7** | same sign, 18-pt shift |
| Odia | 80.01 / 75.45 | 77.5 / 75.7 | same sign |

DERIVED: mean |Sarvam_blog − Sarvam_BodhanPR| over 21 languages = **4.49 pts** (Sarvam-only subset; both-models method gives 4.26; max 17.99 Santhali). **Per-language rankings are a property of whose corpus you picked, not of the models.** *Overlooked:* handwriting covers only 12 Indic + EN — **no Santali, Manipuri, Kashmiri, Bodo, Dogri, Konkani, Maithili, Nepali, Sanskrit or Sindhi handwriting is measured at all**; on its own handwriting bench it loses 11 of 13 to Gemini 3.1 Pro (72.0 vs 66.7), and on its own printed bench it loses 14 of 22 to Sarvam Vision. **Confidence HIGH.**

**Gnani Evon 3.3 — NOT an OCR COMPETITOR.** Card: "*Input: Text — chat messages*". No vision encoder, no document product. 30B / ~3.5B active, `nemotron_h` Mamba2-Transformer MoE, 128K ctx, BF16, **apache-2.0**, Aug 2026. **11 languages total = English + 10 Indic** — `EVIDENCE_SUMMARY:13` and `OCR_AGENT_MEMORY_FEED.md:1008` ("11 Indic langs") are **wrong**. `LIVE_LATEST:40` "**Beats** gpt-5.4-nano … 79.46 vs 79.69" is **wrong**: behind by 0.23; the card says "*statistical parity*", and openly shows **gemma-4-31B beating it** (MILU 85.29 vs 78.74). **Funding/market competitor and Stage-3 normaliser candidate; zero benchmark overlap.** Its two NeurIPS papers (embedding expansion; "*Indic document QA fell up to 11 points*" under English-favouring RL) are W6-cite-worthy. *Overlooked:* the card openly shows its losses (crosssum_in chrF 4.67 vs Sarvam-30B 9.66; MILU Odia 66.94 vs Sarvam-105B 73.70) — honest self-reporting, rare in the field.

**Secondary (precursors only)** — *Surya OCR 2* (650M): Indic **69.96** word-acc macro-22 n=6,609. *PaddleOCR-VL 1.6* (0.9B): OmniDocBench v1.6 **96.01** (Sarvam's table) vs **96.33/96.36** (Paddle's/Bodhan's); **no Indic number exists**. *Chitrapathak-2/Parichay*: Telugu recipe evidence only, no bench number — not a competitor. *Overlooked:* Surya/Paddle run internal suites with no old-scan CER — the degraded-scan column the whole field collapses on (55.3) has no specialist attack shipped.

---

## 2. THE COMPARABILITY TABLE

Our side, MEASURED from `manifest.json` (1,283) + `metrics.py`: **1,283 items, 100% printed, 100% no-table, 100% single-script, 825/1,283 (64%) GT from PDF text layers, 983/1,283 quality "unknown"**. Our metric = **CER**; theirs = **word accuracy on crops of single text blocks**.

| # | Pairing | Verdict | Reason |
|---|---|---|---|
| 1 | our probe22 mean CER vs **87.39** | **NO** | CER vs word-accuracy · page vs block crop · different normalisation, corpus, and averaging (macro-22 of 6,609) |
| 2 | our per-language CER vs their per-language | **NO** | as 1, plus the 8/22 flips and a 4.29-pt mean level shift between benches |
| 3 | our 1,227/1,283 vs their 6,909 | **NO** | disjoint pools; GT = PDF text-layer / pair-txt / Sarvam-bench vs twice-human-reviewed crops |
| 4 | "surya 0.3849 / ~0.45 CER beats 87.39" | **NO** | 0.3849 unverifiable on disk (`PAPERTHIN_VINAY_AUDIT`: ≈0.45); a CER cannot be differenced against a word-accuracy |
| 5 | "we beat Sarvam on 9/18 langs" | **ONLY-DIRECTIONAL** | valid *only* as our CER vs Sarvam's CER on the same 54 items, n=3/lang. **Never state it against 87.39** |
| 6 | "OldScan 55.3" | **NO** | 55.3 is Sarvam's English olmOCR-Bench category pass-rate; we hold no OldScan benchmark |
| 7 | South-400 CER 0.4299 vs any of these | **NO** | old-scan-class renders vs a 1800→present mix; ruled "NOT directly comparable" at `EXTERNAL_BENCHMARK_MAP:25` |
| 8 | Bodhan 84.94 vs 86.2 | **N/A** | same model, two self-built benches; the 1.26-pt "gain" is pure benchmark choice |
| 9 | Sarvam 94.97 (own) vs 90.08 (Bodhan card) | **NO** | 4.89-pt disagreement on OmniDocBench v1.6 for one model; subset/version unspecified |
| 10 | our ko/kn/ml/te vs their ta/te/kn/ml | **NO** | different corpora, units, metrics. Only honest claim: we measure on documents their bench lacks |

**The one sentence that survives cross-examination:** *we have not beaten Sarvam; we measured our own stack on our own items and showed where it fails, and we showed Sarvam's headline is a 22-language macro word-accuracy on a vendor-built, vendor-run, vendor-scored benchmark in which 8 of 22 per-language rankings invert if you change the corpus.*

---

## 3. CONTRADICTIONS WITH PRECURSORS (not already covered above)

`DEEPER:53` "Sarvam reading-order 0.099 (BEST)" → Infinity-Parser2 Pro **0.092** lower, Sarvam ties GLM-OCR, loses TEDS-struct 0.935 vs Paddle 0.961 · PaddleOCR-VL 1.6 = 96.33 (`DEEPER:62/300`) vs **96.01** (Sarvam's table) · Surya OldScan 41.8 (`EXTERNAL_BENCHMARK_MAP:14`) vs **42.8** (Bodhan card) — both PRIMARY, different harness/run, not errors.

---

## 4. TOP 5 WHAT-THEY-OVERLOOKED

1. **Zero handwriting, zero tables, zero code-mixing in Indic OCR Bench.** Sarvam *demos* handwriting but never benchmarks it (§1); our 158 Sarvam-sourced items are 100% printed / 0% table / 0% mixed-script (MEASURED); Bodhan's bench covers 12 Indic + EN, loses to Gemini (66.7 vs 72.0); the field is silent on all four AksharDrishti conditions ("complex layouts, low-quality scans, handwritten text, and code-mixed content", `R6:12-15`).
2. **Macro-22 with English excluded.** A model failing all 300 English samples keeps 87.39; Manipuri (n=207) carries the same 1/22 weight as Assamese (471).
3. **The two vendor benches disagree on 8/22 winners** — Sarvam owns Kashmiri on its bench, loses it by 8.9 pts on Bodhan's.
4. **Self-scored twice over** ("a system evaluated by us … under one harness") — bench we released, model sold as API.
5. **Degenerate outputs are excluded, not scored**; ambiguous GT excluded from the bench. Both self-declared, both move the number.

---

## 5. UNRESOLVED

- **Consensus.app free-tier quota (lead's "10 searches/day"): UNKNOWN.** `/` and `/pricing` are JS-rendered (only schema.org JSON-LD readable: 220M+ peer-reviewed papers, English-only, entry $0); `/home/pricing-plans/` → 404. **Usable as the W1/W4 literature layer only** — no grey literature, no pricing, no press.
- **Bench↔training overlap:** UNKNOWN, unaddressed. Allegation only.
- **87.39 = `word_accuracy` or `valid_word_accuracy`:** UNKNOWN (both emitted).
- **Bodhan IndicOCR-PR unit** (block crop vs page): UNKNOWN. **"Sarvam Vision 90.08"** version/subset: UNKNOWN.
- **Bodhan "15M+ documents":** vendor tweet only. **Sarvam Vision 2.1 param count:** not in the blog; 3B is from `docs.sarvam.ai` per `DEEPER:215`, not re-opened this run.
- **404/dead:** `bodhan.ai/research/blogs/indic-ocr` (the card's own citation), `bodhan.ai/pricing`; `huggingface.co/bodhan-ai/indic-ocr/raw/main/README.md` → 401. Name-collision trap avoided: `bodhaai.com` is an unrelated company.
- **`metrics.py` parity with Sarvam's scorer:** ours is visibly modelled on it but parity is **UNTESTED**.

---

## 6. EVIDENCE LOG

**Opened this run (PRIMARY except the last).** `sarvam.ai/blogs/sarvam-vision-2-1` — 87.39/84.94, per-language 22×13, both global bench tables, architecture, SFT→RLVR, self-admitted limitations. `huggingface.co/datasets/sarvamai/indic-ocr-bench/raw/main/README.md` — **C12 quote**, 6,909+1,173, per-language n, block-level, word-accuracy formula, loop + ambiguous-GT exclusions, `metrics.py`. `…/indic-ocr-bench` — 23 langs, splits. `lnkd.in/p/eFzz2Dtb` — Sarvam's post + **full Krrish comment** + second skeptic. `lnkd.in/p/ewsNXkTs` — Gnani NeurIPS post. `huggingface.co/gnani/gnani-evon-v3.3-30B-A3B` — "Input: Text", 11 langs, gemma beating Gnani. `huggingface.co/bodhan-ai/indic-ocr` — 33M+0.8B, IndicOCR-PR/HW, licence, Sarvam tokenizer, 5 Sep 2026. `console.bodhan.ai/` — ₹0.20/image, ₹10 credit. `x.com/Bodhan_AI/status/2092492598799896582` — 0.8B, 15M+ docs, 05.09.2026. `consensus.app/` — 220M+ papers, EN-only, $0. `analyticsvidhya.com/blog/2026/09/bodhan-ai-indic-models` — SECONDARY, ₹0.20 corroboration.

**Failed:** `consensus.app/pricing` (JS), `consensus.app/home/pricing-plans/` (404), `bodhan.ai/research/blogs/indic-ocr` (404), `bodhan.ai/pricing` (404), `huggingface.co/bodhan-ai/indic-ocr/raw/main/README.md` (401).

