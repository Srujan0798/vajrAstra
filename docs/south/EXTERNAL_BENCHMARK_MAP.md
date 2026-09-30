# EXTERNAL_BENCHMARK_MAP — vajrAstra L2 vs the outside world

Compiled 2026-09-13 (all web sources fetched this date). Every external number cites source; local numbers from `level2/reports/CER_STAGE3B.json` + `LEADERBOARD.md` (generated 2026-09-13). VERIFIED = read from official repo/paper/pricing page today. UNVERIFIABLE = page missing, JS-hidden, or no public number exists.

---

## (a) Surya published vs ours — and whether the numbers even compare

Surya 2 official numbers (github.com/datalab-to/surya README + `static/docs/multilingual.md`, VERIFIED 2026-09-13):

| Bench (their metric) | te | ta | kn | ml | OldScan cat. | Overall |
|---|---|---|---|---|---|---|
| 91-lang internal "pass rate" | 79.2% | 89.9% | 79.2% | 84.7% | — | 87.2% (91 langs) |
| olmOCR-bench per-source (default preset, 8,413 tests) | — | — | — | — | **41.8** (OldScan) | 83.3 overall; Base 99.7, ArXiv 88.3, MultCol 82.4 |

Ours (CER vs PDF text-layer GT, dense pages n=50/75/42/9 per script, surya engine):

| Ours (CER-derived) | te | ta | kn | ml | Overall |
|---|---|---|---|---|---|
| surya CER med (lower=better) | 0.890 | 0.346 | 0.835 | 0.820 | 0.633 |
| surya acc ≈ 1−CER | ~11% | ~65% | ~17% | ~18% | ~37% |

**Hypothesis test: CONFIRMED, with a metric caveat.**
1. Our corpus sits in their worst categories: their OldScan pass rate is **41.8** — 58 points below their Base (99.7) and their single worst row. Our 400 pages are old-scan-class renders (200 dpi) of old books/govt docs. Their four Indic scores (79.2/89.9/79.2/84.7) are mid-table, but te/kn are among their weaker languages (only or 60.0, ur 68.7, lo 72.6 score worse in our region).
2. **Comparability verdict: NOT directly comparable — different metrics, different GT.**
   - Their "pass rate" = % of per-page *tests* passed. A test = a checked text snippet (with `first_n`/`last_n`, `max_diffs` edit allowance, `case_sensitive` flag — schema visible in the olmOCR-bench dataset card, fetched 2026-09-13) or a layout/table/math/reading-order check. It is a **lenient binary edit-tolerance test on human-verified snippets**, not a character error rate.
   - Our CER = continuous edit distance over the full page vs the **PDF text layer** (imperfect GT; 176-177 pages have ≥200 GT chars), NFC + lowercase + whitespace-collapsed (CER_STAGE3B definition, local).
   - So "surya 79.2% Telugu" ≠ "surya reads 79% of Telugu chars correctly", and our ~11% te accuracy ≠ "surya fails 89% of their tests". Ordinally, though, the ranking matches: our Tamil (their best South-Indian lang, 89.9) is also our best surya script (acc ~65%); te/kn (their 79.2) are our worst (~11-17%).
3. Even granting the caveat, the residual gap (their te 79.2 pass vs our ~11% char-acc) is explained by compounding: old-scan quality × 200-dpi render × PDF-layer GT noise × snippet-lenience in their metric. Corroborating external anchor: Datalab's own Chandra-2 multilingual bench (HF model card, VERIFIED 2026-09-13) shows even **Gemini 2.5 Flash at te 33.3 / kn 24.5 / ml 23.8** and GPT-5 Mini at te 9.9 / ml 11.9 on their (cleaner) multilingual suite — top commercial VLMs also collapse on te/kn/ml.

---

## (b) olmOCR-bench top-10 + who could be engine #11

Leaderboard (HF `allenai/olmOCR-bench` dataset card, VERIFIED 2026-09-13; 17 models listed):

| # | Model | Score | Free/local? |
|---|---|---|---|
| 1 | infly/Infinity-Parser2-Pro (35.1B) | 87.6 | weights public but 35B; vLLM/CUDA-oriented (local impractical on Mac) |
| 2 | datalab-to/chandra-ocr-2 (~4-5B) | 85.8 | local, weights public (OpenRAIL-M) |
| 3 | dots-studio/dots.mocr (3B) | 83.9 | local, MIT |
| 4 | datalab-to/surya-ocr-2 (0.65B) | 83.3 | local (we already run surya) |
| 5 | onnx-community/Surya-Ocr-2-Onnx | 83.3 | local, ONNX |
| 6 | lightonai/LightOnOCR-2-1B | 83.2* | local; *different methodology (flagged by Datalab) |
| 7 | datalab-to/chandra (9B) | 83.1 | local |
| 8 | infly/Infinity-Parser-7B | 82.5 | local, vLLM/CUDA |
| 9 | tiiuae/Falcon-OCR (1B) | 80.3* | local |
| 10 | baidu/Qianfan-OCR | 79.8 | API/classifier per its eval card |

Note: the task brief's "Chandra OCR-2 85.9" — actual leaderboard value is **85.8** (85.9 appears in surya's README rounding of the same result). Surya-2 83.3, dots.mocr 83.9, Infinity-Parser2-Pro 87.6, LightOnOCR-2 83.2: **all confirmed as listed**.

**11th-engine candidates (license + Mac-feasibility one-liners):**
- **PaddleOCR-VL-1.6** — Apache-2.0 code+weights (repo states Apache-licensed toolkit); 0.9B; OFFICIAL Apple Silicon tutorial (CPU-Paddle + MLX-VLM paths). Best Mac fit. → see (c).
- **dots.mocr (dots.ocr)** — MIT license, 3B, Kannada demo image on its own model card; runs via HF `transformers` with `trust_remote_code` on CPU/MPS (vLLM path is CUDA-only); est. 30-90 s/page on M-series → 400 pages ≈ 3-10 h. Feasible but slow; no official Mac tutorial.
- **Chandra OCR 2** — weights modified OpenRAIL-M (free <$2M revenue/startups; cannot compete with Datalab API); ~5B BF16; `pip install chandra-ocr`; vLLM recommended (CUDA) — HF-transformers path exists but 5B on MPS is ~40-90 s/page and memory-heavy (~10-12 GB). Feasible, license caveat for productization.
- Falcon-OCR 1B — Apache-2.0, small, but no Indic claims found on its card this session → weak fit for te/ta/kn/ml.

**Recommendation: PaddleOCR-VL-1.6 as engine #11** (only one with official Apple Silicon support + smallest params + Apache).

---

## (c) PaddleOCR-VL-1.6 on Apple Silicon — verdict

Claims (all VERIFIED 2026-09-13):
- OmniDocBench v1.6 = **96.3%** (1−edit-distance), SOTA on v1.5 + Real5-OmniDocBench; **109 languages** (incl. Telugu, Tamil per PP-OCRv5 multilingual release notes in repo README, 2025.10.16 entry); **0.9B params** (NaViT-style encoder + ERNIE-4.5-0.3B LM). Sources: github.com/PaddlePaddle/PaddleOCR README; arXiv:2510.14528 (v1 paper; 1.6 = arXiv:2606.03264 per repo citation block).
- License: repo + models Apache-2.0 ("Apache-licensed open-source toolkit", PaddleOCR 3.0 report §Abstract; repo LICENSE badge). Weights on HF `PaddlePaddle/PaddleOCR-VL-1.6`. VERIFIED for code; HF tag not independently re-opened this session.
- **Apple Silicon: officially supported.** Dedicated tutorial `PaddleOCR-VL-Apple-Silicon.html` (fetched 2026-09-13): two paths — (1) `pip install paddlepaddle==3.2.1` (CPU) + `paddleocr[doc-parser]`, (2) `mlx-vlm>=0.3.11` server (`mlx_vlm.server --port 8111`) + client `--vl_rec_backend mlx-vlm-server --vl_rec_api_model_name PaddlePaddle/PaddleOCR-VL-1.6`. Baidu verified accuracy+speed on **M4**; other chips "not yet confirmed" (their words). Matrix: PaddlePaddle ✅ and MLX-VLM ✅ on Apple Silicon; **llama.cpp = 🚧 in-progress; vLLM/SGLang = ❌**. So "via llama.cpp" = NO, "via MLX" = YES.

Estimates (honest, derived — labeled as estimates):
- VRAM: 0.9B BF16 ≈ 1.8-2 GB weights + NaViT vision tiles + KV → **~4-6 GB peak**; fits any 16 GB M-series comfortably, 8 GB tightly.
- Model download: ~2-3 GB (HF).
- Speed: no published M-series s/page for the full pipeline → estimate **8-20 s/page** on the CPU-Paddle path (layout + VLM), i.e. 400 pages ≈ **1-2.5 h** overnight; MLX path likely faster but adds server-integration risk. (Anchor: their published Apple throughput numbers don't exist for VL; PP-OCRv6-tiny M4 "6.1× CPU" claim is a different, tiny model.)
- Integration cost into `engines/` socket: one `ocr_paddleocrvl` wrapper around `paddleocr doc_parser` CLI/Python API (~2-4 h) + smoke page + verify_v2 CER pass.

**Verdict: FEASIBLE before Sep 16 (today Sep 13)** — budget ~0.5 day integration + overnight 400-page run. Risks: (i) M-series-not-M4 unverified upstream, (ii) CPU-paddle speed uncertainty, (iii) venv conflicts with existing paddleocr_indic install → use a fresh venv (repo itself mandates isolated venv).

---

## (d) Engine-paper Indic claims vs ours — where they match, where they diverge, why

| Engine | Published Indic claim (source, fetched 2026-09-13) | Our CER (med) te/ta/kn/ml | Match/diverge |
|---|---|---|---|
| surya | te 79.2 / ta 89.9 / kn 79.2 / ml 84.7 pass-rate (repo, VERIFIED) | 0.89/0.35/0.84/0.82 | Diverge in absolute (metric+GT); match in **ordinal** direction (ta best both sides) |
| Chandra 2 (not ours; context) | te 58.6 / ta 77.7 / kn 63.2 / ml 64.3 local; Datalab API te 69.4 (HF card, VERIFIED) | — | Even SOTA-adjacent local VLMs sit in 60-80s on te/kn/ml → our corpus is plausibly harder still |
| PaddleOCR 3.0 (arXiv:2507.05595) | **NO Indic per-language scores in the paper** — eval sets are zh/en/ja/pinyin self-built + OmniDocBench (VERIFIED by full-text read). Indic comes from PP-OCRv5 multilingual rec models (109 langs, "some +40% vs prev gen", no per-lang table) | paddle: 0.89/0.64/0.92/0.87 | **No published number to diverge from** — our paddle scores are the only te/ta/kn/ml numbers that exist for this stack. ml fallback-to-en + thin capture (175 med chars) matches repo-known multilingual-rec-model behavior |
| doctr | Vocabs exist: tamil 98 / telugu 119 / kannada 114 / malayalam 116 chars (docs, VERIFIED) — but **"most of our recognition models were trained on our french vocab"**; published accuracies (CRNN 88.2, SAR 88.1, PARSeq 88.5 exact-match on FUNSD/CORD, English) contain **zero Indic claims** | doctr: 0.86/0.86/0.84/0.91 (best CER of our 10 on te/kn despite that) | Divergence explained: default pretrained checkpoint can't emit most Indic glyphs; its "better" CER on te/kn is partly fewer-characters-emitted vs GT length, not better reading |
| easyocr | "80+ languages incl. all popular scripts"; per-lang accuracy **not published** anywhere official (repo, VERIFIED) | easyocr: 0.90/0.93/0.91/0.90 — our worst CER | No claim → no contradiction; CRNN trained on synthetic data, no Indic accuracy published ever |
| tesseract | tessdata te/ta/kn/ml traineddata exist; community accuracy notes are forum anecdotes, **no official per-script numbers** (UNVERIFIABLE — nothing citable on official pages) | tess_indic: 0.89/0.38/0.84/0.89 | Our ta 0.38 (62% acc) shows tesseract's Tamil model is genuinely the strong one — consistent with community lore that ta/te tessdata are the best-maintained South packs |

**Why published claims diverge from ours, honestly:** (1) **nobody publishes te/ta/kn/ml full-page CER on old scans** — the published multilingual suites (Surya 91-lang, Chandra 43/90-lang, PaddleOCR-VL 109-lang) are internal, mostly cleaner documents, snippet/pass-rate metrics; (2) our GT is the PDF text layer, not human transcription, so absolute CER is inflated by GT noise (misalignment, layer gaps — see `research/PUBLISHED_BENCHMARKS.md` C10 caveat); (3) our corpus concentrates exactly the two known worst-case axes — scan age and Dravidian scripts — which each published table independently confirms is where everyone's scores fall off (OldScan 41.8; te/kn ≤ 79.2; Gemini-Flash te 33.3).

---

## (e) Metric science + the ONE metric to add before Sep 16

What the big benches actually report (VERIFIED 2026-09-13):
- **olmOCR-bench** (allenai/olmocr + dataset card): a **pass-rate**, not CER. Per-page tests carry `checked` snippet, `first_n`/`last_n`, `max_diffs` (edit allowance), `case_sensitive`, `check_disallowed_characters`; GT = human-selected snippets on real PDFs across 7 sources (arxiv_math, old_scans, old_scans_math, tables, headers_footers, multi_column, long_tiny_text, base). Score = % tests passed (±~1.1 MoE).
- **OmniDocBench** (opendatalab; as used by PaddleOCR 3.0 report + dots.mocr card): **1−edit-distance** on normalized page text (plus TEDS for tables, per-category formulas; v1.5/v1.6 variants). GT = human-annotated pages. "96.3%" = averaged 1−EditDist.
- **SarvamBench**: not retrievable this session (no public methodology page found via docs.sarvam.ai) → **UNVERIFIABLE — do not cite its numbers without fetching the repo yourself.**

**Is our suite defensible? (3 bullets, honest)**
- Yes for *ranking our 10 engines on our 400 pages*: capture-ratio (volume honesty, exposes empty/hallucination) + Jaccard/5-gram consensus + CER-vs-PDF-layer as proxy is internally consistent and fully reproducible from disk truth.
- No for *external comparability*: our CER normalization (NFC + lowercase + whitespace-**collapse**) differs from OmniDocBench-style (which strips punctuation/space effects more aggressively), and our GT (PDF layer) is noisier than human-verified benches — so our absolutes will always look worse even if engines are equal.
- The fix is one cheap addition, not a re-run.

**THE ONE metric to add before Sep 16: `CER_omni` — CER recomputed on OmniDocBench-equivalent normalization (NFC → casefold → strip ALL whitespace → strip markdown/HTML punctuation) on the same 176-177 dense pages.** It needs zero engine re-runs: one script pass over the already-stored per-page OCR text + GT in `CER_STAGE3B` inputs. It makes our headline directly comparable to every published 1−EditDist table (PaddleOCR-VL 96.3, dots.mocr 0.969, MinerU 0.953, etc.), at ~1-2 h of work.

---

## (f) Indian-OCR pricing sanity (all fetched 2026-09-13)

| Vendor / product | Price per page | INR-equiv/page* | Status |
|---|---|---|---|
| **Sarvam Document Digitization API** | **₹0.50/page** (max 10 pages/job) | ₹0.50 | VERIFIED — docs.sarvam.ai/api/getting-started/pricing.md |
| Google Cloud Document AI — Enterprise OCR | $1.50 / 1,000 pages (1K-5M tier; $0.60 ≥5M; first 1K/mo free) | ~₹0.13 | VERIFIED — cloud.google.com/document-ai/pricing |
| Google Vertex AI Gemini (token-priced, not per-page) | e.g. Gemini 3 Flash Preview $0.50/1M input tok (image+text) + $3/1M output; per-page varies with density | ~₹0.02-0.10 (est., density-dependent) | VERIFIED token prices — cloud.google.com/vertex-ai/generative-ai/pricing; per-page figure is OUR estimate, not Google's |
| Mistral OCR 4.1 | $4 / 1,000 pages; Document AI mode $5/1K | ~₹0.35 | VERIFIED — mistral.ai/pricing/api |
| Azure Document Intelligence (Read) | page exists but per-1K-page values are JS-rendered placeholders ("$-") in fetch | — | **UNVERIFIABLE this session** (commonly cited $1.50/1K Read S0 — not re-verified, do not cite) |
| **Bhashini / ULCA OCR** | no public per-page pricing found anywhere on ULCA marketplace/Bhashini pages | — | **UNVERIFIABLE (as expected)** — procurement/partnership-gated, nothing public to cite |
| Bodhan AI (bodhan.ai) | site is a JS app; /pricing 404; no public OCR rate | — | **UNVERIFIABLE** |
| Datalab (Surya/Chandra) hosted API | pricing page is plan/credit-based, no public per-page OCR rate | — | UNVERIFIABLE (playground free tier exists) |

*INR-equiv at ~₹88/$ (indicative conversion, not a vendor quote).*

**Sanity read:** Sarvam ₹0.50/page is the only *Indian* per-page OCR price that is public and citable — and it is ~4× Google Document AI's OCR (~₹0.13) and ~1.4× Mistral OCR (~₹0.35), while being the only one with Indic-first claims. Our 10-engine OSS fleet amortizes to ₹0/page compute on an idle M-series — that contrast (free-local vs ₹0.13-0.50/page API) is the benchmark's economic headline.

---

## Source index (all fetched 2026-09-13)

- Surya README + multilingual.md — github.com/datalab-to/surya (raw master)
- olmOCR-bench leaderboard — huggingface.co/datasets/allenai/olmOCR-bench; olmocr repo — github.com/allenai/olmocr
- Chandra-2 card — huggingface.co/datalab-to/chandra-ocr-2 · dots.mocr card — huggingface.co/dots-studio/dots.mocr
- PaddleOCR repo README — github.com/PaddlePaddle/PaddleOCR · VL usage + Apple Silicon tutorials — paddlepaddle.github.io/PaddleOCR/latest/en/version3.x/pipeline_usage/{PaddleOCR-VL,PaddleOCR-VL-Apple-Silicon}.html · papers arXiv:2510.14528, arXiv:2507.05595 (full HTML read)
- doctr docs — mindee.github.io/doctr (using_models, datasets/vocabs) · EasyOCR — github.com/JaidedAI/EasyOCR
- Pricing — docs.sarvam.ai/api/getting-started/pricing.md · cloud.google.com/document-ai/pricing · cloud.google.com/vertex-ai/generative-ai/pricing · mistral.ai/pricing/api · azure.microsoft.com/en-us/pricing/details/ai-document-intelligence (values hidden)
- Local — level2/reports/CER_STAGE3B.json, LEADERBOARD.md, research/PUBLISHED_BENCHMARKS.md
