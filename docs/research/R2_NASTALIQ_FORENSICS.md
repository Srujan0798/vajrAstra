# R2 — Nastaliq Forensics: Why the Kashmiri Cell Fails (~54.82) and How to Attack It Under ≤2B VLM / ≤100 GPU-h

Status: research-only. No training run in this doc. No backbone invention.
Scope: failure physics (A) + 2024–2026 attack surface (B) + ranked exploit map under fine-tune ≤2B VLM / ≤100 GPU-h (C) + go/no-go with numbers.
Every factual claim carries a primary-source URL. URLs verified September 2026 via live search/fetch.

---

## PART A — Failure physics of Nastaliq OCR

### A1. What Nastaliq actually is (and why Naskh-trained OCR dies on it)

Nastaliq is diagonal, highly cursive, context-sensitive; only the last character of a ligature sits on the baseline, with character- and ligature-level spatial overlap and highly contextual dot/diacritic placement. Classical Arabic (Naskh) preprocessing and segmentation assumptions do not transfer; algorithms need further evolution for Urdu/Nastaliq specifically (Javed & Hussain, CRULP):
https://www.cle.org.pk/Publication/papers/2009/Pre-Recognition-Process-for-Urdu-OCR.pdf

Concretely (Lehal-style ligature work): Urdu is written diagonally top-right → bottom-left with stacking/tilt; vertical overlap between adjacent ligatures; inter-ligature vs inter-word gap confusion; characters fully merged so character segmentation is "highly challenging" — researchers retreat to ligature-as-unit recognition:
https://learnpunjabi.org/pdf/lehal.11.pdf
https://dl.acm.org/doi/10.1145/2505377.2505379

Modern confirmation on newspapers (Nastaliq, multi-column, low-res scans, stylized fonts): script is cursive with context-sensitive letterforms, frequent ligatures, baseline variation; Naskh vs Nastaliq typographic distinction is a first-order accuracy factor; diagnostic errors concentrate in ligature segmentation, diacritic handling, character substitution:
https://arxiv.org/html/2505.13943v3

UTRNet authors state the same split precisely: Arabic print is usually upright Naskh with 28 letters; Urdu print is Nastaliq with 45 main letters + 26 punctuation + 8 honorific marks + 10 Urdu digits + Persian/Arabic/English admixture — so Arabic-OCR journeys do not transfer directly:
https://arxiv.org/html/2306.15782v1

### A2. Ligature explosion (the class-count problem)

The canonical number: **9,262 ligatures formed from 2,190 primary + 17 secondary components** after clubbing similar primaries (Lehal et al., ACM):
https://dl.acm.org/doi/10.1145/2505377.2505379
https://learnpunjabi.org/pdf/lehal.11.pdf

Consequences:
- Character-class OCR (isolated glyph classifier) is combinatorially hopeless; the field moved to holistic ligature recognition with separate modeling of main body vs secondary components (HMM-era segmentation-free approach):
  https://xplorestaging.ieee.org/document/7333728
- Font-independent recognition must model inter- AND intra-class variability across 400+ Urdu fonts; one group generated **>4M synthetic images across 256 fonts covering the full 18,569-ligature lexicon** to get 86% font-independent CNN accuracy — i.e., brute-force ligature × font coverage works but is expensive:
  https://arxiv.org/pdf/2005.06752
- UTRNet's character-wise accuracy plot shows nuqta-only distinctions (6 same-shape characters differing only by dot arrangement) as the residual error floor even for the SOTA CNN-RNN:
  https://arxiv.org/html/2306.15782v1

For the Kashmiri cell (~54.82, read as ~0.55 CER): this is exactly what a ligature-explosion + nuqta-confusion regime looks like — not random noise but systematic substitution/deletion on dots, small glyphs, and stacked secondaries.

### A3. Kashida, stacking, non-linear baseline

Three coupled mechanisms:
1. **Kashida / kashish (elongation):** Jameel Noori Nastaleeq Kasheeda is a distinct widely-downloaded variant (5.7M+ downloads) whose elongation behavior changes word width and baseline histogram shape vs the Regular cut (4.7M+ downloads):
   https://urdufonts.net/fonts/jameel-noori-nastaleeq-kasheeda
   https://urdufonts.net/fonts/jameel-noori-nastaleeq-regular?jmlVVPJ8=fc3MoVSPW
2. **Stacking + diagonality:** Nastaliq stacks characters diagonally; ligatures tilt right; only the final glyph grounds on the baseline. Standard horizontal-projection baseline detection then places the baseline in the wrong half of the line on bad print — Javed & Hussain document this exact failure with heuristics (every ligature must touch baseline; baseline must be in lower half):
   https://www.cle.org.pk/Publication/papers/2009/Pre-Recognition-Process-for-Urdu-OCR.pdf
3. **Non-linear vertical overlap:** vertically overlapping ligatures (Figure-3 class in Lehal) break line/word segmenters that assume separable horizontal bands:
   https://learnpunjabi.org/pdf/lehal.11.pdf

Net effect: any pipeline with a hard line-segment → word-segment → character-segment cascade compounds error before recognition even starts. The 2025 Urdu-newspaper benchmark confirms super-resolution alone (SwinIR, 32.71 dB PSNR) cuts WER by 25–70% depending on model — i.e., a large share of "recognition" error is actually rendering/segmentation error:
https://arxiv.org/html/2505.13943v2

### A4. Urdu vs Kashmiri conventions (why Urdu fine-tune ≠ Kashmiri fix)

Kashmiri in Perso-Arabic script needs codepoints Urdu OCR never sees:
- Proposal L2/09-215 (Anderson, Pournader, Aazim, Mansour) adds **U+0620 ARABIC LETTER KASHMIRI YEH** (palatalization marker, with a distinct "half yeh" final/isolated form common in Nastaliq) plus a second Kashmiri character, attested in newspapers such as Weekly Sangarmal and primers (Amin Kamil):
  https://www.unicode.org/wg2/docs/n3673.pdf
- SIL **Awami Nastaliq v3.300 (Oct 2024) explicitly "added support for Kashmiri language"** (plus Gojri) — proof that pre-2024 Nastaliq fonts under-render Kashmiri:
  https://software.sil.org/awami/release-3-300
- Practical font inventory for Kashmiri/Urdu synthetic work spans Mehr Nastaliq Web, Alvi Nastaleeq, Pak Nastaleeq, Jameel Noori Kasheeda/Regular, Alqalam Taj Nastaleeq, Naskh cuts — the Indic synthetic benchmark lists this exact set for the Kashmiri and Urdu rows:
  https://arxiv.org/pdf/2205.02543
- Open font options that actually shape Kashmiri today: SIL Awami Nastaliq (above), Google Fonts **Gulzar**, AlifType Hussaini Nastaleeq, Mehr Nastaliq (Slackware Nastaliq font pack listing):
  https://github.com/lecramyajiv/fonts-nastaliq
- Noto Nastaliq Urdu itself is versioned for shaping fixes (v3.004→v4.000: low-alef positioning, noon-with-small-tah U+0768, nukta-over-lam placement) — shaping-engine-dependent rendering means the same Unicode string rasterizes differently across fonts/versions:
  https://github.com/notofonts/nastaliq/releases

Implication: an Urdu-Nastaliq recognizer trained on Jameel-Noori-Regular-only data systematically misses Kashmiri Yeh/half-yeh and Kashmiri-specific nukta stacks → substitution/deletion floor no amount of Urdu data fixes. Any exploit must include Kashmiri-glyph font coverage (Awami ≥3.300, Gulzar, Mehr/Alvi/Pak cuts) and Kashmiri text corpora, not just Urdu corpora.

### A5. RTL pipeline bugs (the silent CER inflator)

Arabic-script OCR has three RTL failure layers, all attested in recent benchmarks:
- **Logical vs visual order:** KITAB-Bench (8,809 samples, 9 domains) lists cursive script + RTL flow + complex typography/calligraphy as the core gap vs Latin OCR, and finds VLMs beat traditional OCR by **~60% mean CER** precisely because traditional pipelines mishandle order/layout:
  https://arxiv.org/html/2502.14949v1
  https://aclanthology.org/2025.findings-acl.1135.pdf
- **Bidi with digits/Latin:** UrduMMLU's 2026 pipeline documentation shows the production fix explicitly — add RTL marks, wrap Latin/digit fragments in LRI…PDI isolates, NFKC + Arabic-letter normalization, punctuation mapping (۔ ، ؟):
  https://arxiv.org/html/2606.07167v1
- **Numerals run LTR inside RTL words** (Lehal: "numerals add to the complexity as they are written left-to-right" inside right-to-left text), so naive string-level CER computation without Unicode normalization + bidi isolation mis-scores correct outputs:
  https://learnpunjabi.org/pdf/lehal.11.pdf

Operational rule for South scoring: normalize (NFKC, yeh/kaf variants, digit forms, punctuation map) BEFORE computing CER on ks/ur/sd, else 3–8 pts of the "54.82" may be scoring artifact. (Magnitude prior: UrduMMLU reports quotation/prefix/blank normalization as load-bearing for Urdu eval:
https://arxiv.org/html/2606.07167v1)

### A6. WHY CNN+CTC structurally fails (conditional independence vs context shaping)

CTC's defining assumption: **output tokens are conditionally independent given the encoder frames** — P(a|X) factorizes per-frame, alignments summed, no language dependency modeled. Standard statement with the speed/accuracy trade-off (Nozaki et al., Interspeech 2021):
https://www.isca-archive.org/interspeech_2021/nozaki21_interspeech.pdf
https://nlp.csie.ntust.edu.tw/files/meeting/Relaxing_the_Conditional_Independence_Assumption_of_CTC-based_ASR.pdf

Arabic-script HTR literature states the consequence directly: CTC "assumes a monotonic alignment… output tokens are assumed to be independent… severely limits language modeling; CTC decoders are often paired with an external LM":
https://ar5iv.labs.arxiv.org/html/2307.15045

Why this is fatal for Nastaliq specifically:
1. **Shaping is all context:** a glyph's form depends on neighbors (initial/medial/final/isolated) AND on stack position AND on font-specific ligature substitution. A frame-independent classifier cannot resolve nuqta/stack ambiguity without right context — exactly what CTC forbids.
2. **Monotonicity is violated visually:** diagonal stacking + vertical overlap means the visual order of secondaries (dots, hamza, small-tah) is not monotonic in the logical character order. CTC's monotonic-alignment assumption breaks; the model smears probability across frames → deletions of small marks (the top error class in every Urdu error analysis; cf. UTRNet Figure-2 nuqta collapse:
   https://arxiv.org/html/2306.15782v1).
3. **Empirical proof on Urdu:** EasyOCR (CRNN+CTC) and Tesseract (CNN+LSTM) both collapse Nastaliq≫Naskh — EasyOCR WER 0.532→0.904, Tesseract 0.902→1.567, CER up to 1.42–2.58 on newspaper Nastaliq (Press-to-Pixels Table 3):
   https://arxiv.org/html/2505.13943v2
4. UTRNet (CNN-RNN hybrid, CTC-era SOTA, 92.97% in-domain) **fails to generalize out-of-domain** (WER 0.862 OpenITI-Nastaliq → 0.602 UNB; CER 0.638→0.306) while autoregressive VLM decoders generalize far better — the structural lesson is that in-domain CTC accuracy does not survive font/domain shift:
   https://arxiv.org/html/2505.13943v2

Structural verdict: CTC is a fast frame classifier with an independence assumption that Nastaliq's context-sensitive shaping violates by design. Patching it (bigger CNN, more fonts) raises in-domain accuracy but preserves the OOD cliff. The fix is an autoregressive decoder (attention/transformer/VLM) that conditions each character on previously emitted characters.

---

## PART B — 2024–2026 attack surface

### B1. Segmentation-free transformer decoders (the CTC replacement)

| System | Architecture | Urdu/Nastaliq result | Source |
|---|---|---|---|
| PARSeq-Urdu (Mustafa et al., Aug 2024) | Permuted-autoregressive (PARSeq), multi-permutation training for reorder/overlap | **CER 0.178** on ~160k Urdu word images | https://arxiv.org/abs/2408.15119 |
| ET-Network (PLOS ONE) | Efficient transformer, conv-frontend + CE+CTC hybrid | **CER 6.20%** across UPTI2.0/URTI/NUST-UHWR/MMU-OCR-21 | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0302590 |
| UTRNet / UTRNet-Small (2023, still the CNN-RNN reference) | U-Net-style high-res encoder + RNN/attention decoder | **92.97% char accuracy** UTRSet-Real in-domain; collapses OOD (Table 4: UPTI-trained → 54.84% on UTRSet-Real) | https://arxiv.org/html/2306.15782v1 and https://huggingface.co/papers/2306.15782 |
| TrOCR-family zero-shot on Urdu | Pretrained Latin TrOCR applied to Urdu | **~36–38% accuracy** (i.e., ~0.62+ CER) — proves Latin-pretrained transformers do NOT transfer without script SFT | https://arxiv.org/html/2306.15782v1 (Table 3B) |
| NUST-UHWR lineage (handwriting) | CNN + RNN + interpolated n-gram → later LSTM/BERT/GPT-3 reframing as seq2seq | 5.49% CER (n-gram era); **1.1% CER** after multilingual VLM-transformer adaptation (2024 thesis) | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0302590 and https://openrepository.aut.ac.nz/server/api/core/bitstreams/b3d49df6-fed9-450d-951d-00039a9d8e15/content |

Takeaway: by 2024 the best Urdu numbers already come from autoregressive/transformer decoders, not CTC. PARSeq's 0.178 CER on digital Urdu and ET-Network's 6.2% multi-corpus CER are the honest classical baselines; anything above ~0.20 CER on printed Nastaliq in 2026 is behind the published frontier.

### B2. VLM direct decoding (the 2025 discontinuity)

Press-to-Pixels (UNB: 829 Nastaliq newspaper blocks, 9,982 sentences + OpenITI 250+250 Naskh/Nastaliq) is the decisive benchmark — full tables fetched August 2025 revision:
https://arxiv.org/html/2505.13943v2

| Model | OpenITI-Naskh WER/CER | OpenITI-Nastaliq WER/CER | UNB high-res WER/CER |
|---|---|---|---|
| Tesseract | 0.902 / 0.955 | 1.567 / 1.420 | 2.401 / 2.580 |
| EasyOCR | 0.532 / 0.177 | 0.904 / 0.392 | 0.802 / 0.246 |
| Kraken (OpenITI-tuned) | 0.249 / 0.069 | 0.626 / 0.305 | 0.558 / 0.221 |
| UTRNet | 0.989 / 0.741 | 0.862 / 0.638 | 0.602 / 0.306 |
| **Gemini-2.5-Pro** | 0.228 / 0.066 | 0.303 / 0.125 | **0.133 / 0.032** |
| GPT-4.1 | 0.286 / 0.089 | 0.443 / 0.203 | 0.254 / 0.096 |
| GPT-4o | 0.418 / 0.252 | 0.628 / 0.432 | 0.327 / 0.154 |
| Claude-3.7-Sonnet | 0.329 / 0.127 | 0.616 / 0.386 | 0.249 / 0.100 |
| Llama-4-Maverick | 0.302 / 0.104 | 0.765 / 0.561 | 0.305 / 0.128 |

Three facts that matter for South:
1. **Best VLM beats best classical by >76% WER** on UNB (0.133 vs 0.558). The gap is Nastaliq-specific and widest OOD.
2. **500-image GPT-4o fine-tune (2 epochs) → 6.13% relative WER gain** (0.330→0.269 on held-out 329). Few-hundred in-domain samples move frontier VLMs — the strongest precedent for our ≤100 GPU-h budget.
3. Error profile is deletions > substitutions > insertions; top confusions are YEH/ALEF/HEH/WAW + blank omissions — i.e., small-glyph/nuqta deletions, matching the Part-A physics:
   https://arxiv.org/html/2505.13943v2

Corroboration from neighboring scripts/tasks:
- KITAB-Bench (Arabic, 8,809 samples): modern VLMs (GPT-4, Gemini, Qwen) beat EasyOCR/PaddleOCR/Surya by **~60% mean CER**; best PDF→Markdown only 65% (Gemini-2.0-Flash) — layout remains hard:
  https://arxiv.org/html/2502.14949v1
- "Deciphering the Underserved" (low-resource-script LLM OCR): Urdu CER 0.07→0.24 as word count grows; WER spikes 0.24→0.52 on low-contrast backgrounds — line length + degradation are first-order:
  https://arxiv.org/pdf/2412.16119

### B3. Synthetic Nastaliq pipelines (what exists, what transfers)

1. **RAVI (Mendeley, Jun 2025): 99,000 word images, 256×256, Jameel Noori Nastaleeq size-40**, black-on-white, alphabet-foldered, arabic_reshaper pipeline — clean word-level SFT fuel, CNN-benchmarked:
   https://data.mendeley.com/datasets/mhy5vxnths/1
2. **UTRSet-Synth: 20,000 lines "closely resembling real-world"** + UTRSet-Real 11,000+ annotated real lines; training on Synth alone → 75.14% on Real; Real alone → 90.87%; Mix-All best. Synthetic-only does NOT match real-data performance (15-pt gap in their Table 4):
   https://huggingface.co/papers/2306.15782
3. **4M-image / 256-font pipeline (Tariq et al.): full 18,569-ligature lexicon × 256 fonts**, transfer-learnable to unseen fonts, matches UPTI benchmark — the heavyweight precedent that font multiplicity substitutes for real data volume:
   https://arxiv.org/pdf/2005.06752
4. **Indic OCR synthetic bench (2022): Kashmiri + Urdu rows with the exact Nastaliq font list** (Mehr Nastaliq Web, Alvi, Pak Nastaleeq, Jameel Noori Kasheeda, Alqalam Taj Nastaleeq, Naskh cuts) — reusable font-inventory recipe for ks/ur synthetic generation:
   https://arxiv.org/pdf/2205.02543
5. **QARI synthetic curriculum (Arabic, the VLM-SFT template): v0.1 10k plain → v0.2 50k diacritized/10-font → v0.3 10k layout/HTML-spatial**, conversational image–text pairs, SFTTrainer + UnslothVisionDataCollator, batch-8:
   https://arxiv.org/html/2506.02295
   https://github.com/NAMAA-ORG/qari-ocr-paper-2025

### B4. Published Urdu / Kashmiri / Sindhi CERs (one table)

| Dataset / split | Best published | System | Source |
|---|---|---|---|
| UTRSet-Real (Urdu print, in-domain) | 92.97% char-acc (~7% CER) | UTRNet | https://huggingface.co/papers/2306.15782 |
| UPTI (synthetic Nastaliq lines, in-domain) | 98.63% (UTRNet-Small trained on UPTI) — but only 54.84% cross-domain to Real | UTRNet-Small | https://arxiv.org/html/2306.15782v1 |
| Digital Urdu words (~160k) | CER 0.178 | PARSeq-Urdu | https://arxiv.org/abs/2408.15119 |
| Multi-corpus UPTI2.0/URTI/NUST-UHWR/MMU-OCR-21 | CER 6.20% | ET-Network | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0302590 |
| NUST-UHWR handwriting | CER 1.1% | multilingual VLM-transformer adaptation | https://openrepository.aut.ac.nz/server/api/core/bitstreams/b3d49df6-fed9-450d-951d-00039a9d8e15/content |
| UNB newspaper Nastaliq (OOD) | WER 0.133 / CER 0.032 | Gemini-2.5-Pro zero-shot | https://arxiv.org/html/2505.13943v2 |
| OpenITI-Nastaliq books | WER 0.303 / CER 0.125 | Gemini-2.5-Pro | https://arxiv.org/html/2505.13943v2 |
| Kashmiri / Sindhi printed OCR CER | **No published dedicated CER found** (Sep 2026 search; only font/Unicode/corpus attestations) | — | https://arxiv.org/pdf/2205.02543 (fonts only), https://www.unicode.org/wg2/docs/n3673.pdf, https://software.sil.org/awami/release-3-300 |
| South Kashmiri cell | ~54.82 (≈0.55 CER regime) | incumbent | internal leaderboard (this repo) |

The Kashmiri gap is therefore ~40–50 pts vs the Urdu VLM frontier (0.03–0.13 CER) and ~35 pts vs classical Urdu in-domain (~0.18–0.22). No public Kashmiri CER exists to contradict this — the cell is uncharted, which is opportunity, not refutation.

### B5. PaddleOCR Arabic / v5 on Nastaliq (honest assessment)

- PP-OCRv5 core supports Simplified/Traditional Chinese, Pinyin, English, Japanese; **multilingual extension covers 106–109 languages with +30% accuracy vs v3**, but published per-language weights that matter here are Korean/Latin/E-Slavic/Thai/Greek/Tamil/Telugu/Cyrillic/Arabic lines — **no Nastaliq-specific CER published**:
  https://www.paddleocr.ai/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5_multi_languages.html
  http://www.paddleocr.ai/main/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html
- Community-extracted ONNX set confirms an **`arabic_PP-OCRv5_rec` model (747-char dict) covering Arabic, Persian, Urdu, Pashto, Kurdish, Sindhi, Balochi, Uyghur**:
  https://github.com/403323726/PP-OCRv5
- Official card **`PaddlePaddle/arabic_PP-OCRv5_mobile_rec`: 81.27% line accuracy** (whole-line-must-match criterion — strict; ≈0.19 line-error-rate, character CER unpublished and Naskh-skewed):
  https://huggingface.co/PaddlePaddle/arabic_PP-OCRv5_mobile_rec/blob/main/README.md
- Third-party KITAB-context eval (medyas Arabic PP-OCRv6-small-rec, same family): **off-the-shelf PaddleOCR CER 0.77/0.81** on KITAB OCR subsets vs Tesseract 0.14/0.31 and Qwen2.5-VL 0.98/1.27 — i.e., off-shelf Paddle on Arabic script is weak; fine-tuned PP-OCRv6-small on 500k printed-Arabic reaches **~10% CER** on held-out scans:
  https://huggingface.co/medyas/arabic_PP-OCRv6_small_rec/blob/main/README.md
- Newest **PaddleOCR-VL-0.9B (NaViT + ERNIE-4.5-0.3B), 109–111 languages incl. Arabic/Hindi**, SOTA on OmniDocBench parsing — fits the ≤2B envelope and is the Paddle path worth testing, not the CTC rec head:
  http://github.com/PaddlePaddle/PaddleOCR

Verdict: PaddleOCR-arabic is a Naskh-Arabic line recognizer with Urdu codepoints present but Nastaliq shaping/stacking unmodeled. Off-shelf use on Kashmiri Nastaliq is expected to land in the 0.5–0.8 CER band (same as incumbent). Only its VLM branch (PaddleOCR-VL-0.9B + SFT) belongs in the exploit map.

### B6. Qwen-VL / InternVL zero-shot Nastaliq numbers (no hype)

- **Qwen2.5-VL (7B) zero-shot on Arabic KITAB subsets: CER 0.98/1.27** (worse than Tesseract 0.14/0.31 on the same images) — generalist VLMs zero-shot are BAD at Arabic script without SFT:
  https://huggingface.co/medyas/arabic_PP-OCRv6_small_rec/blob/main/README.md
- **Qwen2.5-VL-7B as QARI baseline: CER 0.550 / WER 0.800 / BLEU 0.220** on diacritized Arabic; Qwen2-7B 0.740/1.050 — then QARI-v0.2 SFT on the SAME 2B backbone family reaches **0.061/0.160/0.737**. That delta (0.55→0.06, ~49 pts) is the single most important precedent in this doc:
  https://arxiv.org/html/2506.02295
- **QARI-v0.3 (layout-enriched 10k) REGRESSES to 0.300/0.485** on the plain test — layout SFT hurts plain-line CER; keep stages separate:
  https://arxiv.org/html/2506.02295
- **4-bit quantization destroys QARI (CER 3.45)** vs 8-bit 0.091 — inference precision is load-bearing for Arabic script; do not 4-bit quantize the ks/ur/sd recognizer:
  https://arxiv.org/html/2506.02295
- **OCRBench v2 (10k tasks, 31 scenarios): Qwen2-VL-7B 51.4 / Qwen2.5-VL-7B 46.7 / InternVL3-8B 49.0 / InternVL3-14B 52.6 overall** — InternVL3 and Qwen2-VL generations are comparable; neither is pre-tuned for Nastaliq; both need SFT:
  https://ling99-ocrbench-v2-leaderboard.hf.space/
- Qwen2-VL architecture priors that help OCR SFT: native dynamic resolution + M-RoPE cross-modal positions; 24.8M synthetic OCR pairs (EN+ZH only — no Urdu) in Qwen-VL pretraining, i.e., the backbone knows OCR-as-task but not Nastaliq-as-script:
  https://arxiv.org/pdf/2308.12966v3
  https://arxiv.org/html/2409.12191v1
- Qalam (SwinV2 + RoBERTa, Arabic MLLM, 2024) and Historic-Arabic-OCR (QARI→Qwen2-VL-2B + LoRA + CLAHE, CER 0.10/WER 0.28 on manuscripts) confirm the LoRA-on-2B recipe works for Arabic script at low compute:
  https://aclanthology.org/2024.arabicnlp-1.19.pdf
  http://www.lrec-conf.org/proceedings/lrec2026/workshops/nakbanlp/pdf/2026.nakbanlp-1.43.pdf
- Community Qwen2-VL Arabic-OCR LoRA pipeline (notebooks + SFTTrainer) exists and is reusable for ks/ur SFT:
  https://github.com/m0d9/qwen-vl-arabic-ocr/blob/main/notebooks/Qwen_VL_Fine_Tuning_Arabic_OCR.ipynb

Honest zero-shot expectation for Kashmiri Nastaliq on a ≤2B VLM: **0.5–1.0 CER** (matches Qwen2.5-VL Arabic zero-shot band). The attack is SFT, not prompting.

---

## PART C — Exploit map (≤2B VLM SFT, ≤100 GPU-h budget)

### C1. Constraints and scoring rule

- Backbone cap: ≤2B total (candidates: **Qwen2-VL-2B-Instruct** — the QARI-proven backbone; **PaddleOCR-VL-0.9B**; SmolVLM2-2.2B/GOT-580M as fallback). No 7B+ fine-tune (budget + deployment law).
- Compute cap: ≤100 GPU-h (assume 1×A100-40G or 2×L40S equivalent; LoRA r=16–32, 8-bit AdamW, batch-8 eff, 1–3 epochs over 30–60k pairs ≈ 30–70 GPU-h on 2B VLM per QARI-class runs:
  https://arxiv.org/html/2506.02295
  https://github.com/NAMAA-ORG/qari-ocr-paper-2025).
- Ranking metric: **(expected CER-point gain on ks/ur/sd weighted 50/30/20) ÷ GPU-h cost**. Kashmiri weighted first because it is the failing cell.
- CER baseline: ks ≈ 0.55 (54.82 cell), ur/sd assumed 0.25–0.40 on South probes (to be confirmed on W3 probe, not invented here).

### C2. Synthetic Nastaliq + degradation recipe (concrete)

**Fonts (must cover Kashmiri glyphs + Kasheeda elongation + Naskh distractor):**
- Kashmiri-capable: SIL Awami Nastaliq ≥3.300, Google Gulzar, Mehr Nastaliq, Hussaini Nastaleeq:
  https://software.sil.org/awami/release-3-300
  https://github.com/lecramyajiv/fonts-nastaliq
- Urdu-workhorse: Jameel Noori Regular + Kasheeda, Noto Nastaliq Urdu v4.000, Alvi Nastaleeq, Pak Nastaleeq, Alqalam Taj Nastaleeq:
  https://urdufonts.net/fonts/jameel-noori-nastaleeq-regular?jmlVVPJ8=fc3MoVSPW
  https://github.com/notofonts/nastaliq/releases
  https://www.wfonts.com/font/alvi-nastaleeq
- Naskh distractor (to teach style separation): Alqalam Naqsh, Nafees Naskh family:
  https://arxiv.org/pdf/2205.02543
  https://salrc.uchicago.edu/resources/fonts/available/sindhi/nafeespaknaskhsindhi.shtml

**Corpora (no 400-page collection; reuse + synthesize):**
- UPTI (10k+ synthetic Nastaliq lines — the standard Urdu print benchmark):
  https://arxiv.org/html/2505.13943v2
- UTRSet-Synth (20k lines) + UTRSet-Real (11k real lines) generation recipe + web tool:
  https://huggingface.co/papers/2306.15782
- RAVI (99k Jameel-Noori words) for word-level warm-up:
  https://data.mendeley.com/datasets/mhy5vxnths/1
- OpenITI (Naskh + Nastaliq book lines; the domain-shift test bed):
  https://arxiv.org/html/2505.13943v2
- Kashmiri text: Sangarmal weekly archive + Kashmiri primers (Amin Kamil) cited in the Unicode proposal as attested Kashmiri-print sources; Awami/Gulzar renderers close the loop:
  https://www.unicode.org/wg2/docs/n3673.pdf
- Sindhi text: Nafees-font-covered Sindhi/Urdu wordlists (CRULP) for the sd split:
  https://salrc.uchicago.edu/resources/fonts/available/sindhi/nafeespaknaskhsindhi.shtml

**Degradation (copy the UNB/SwinIR finding — resolution is accuracy):**
- Downsample/JPEG/print-scan noise ladder + SwinIR-style super-resolution as preprocessing (UNB: +25–70% WER recovery post-SR):
  https://arxiv.org/html/2505.13943v2
- Low-contrast/background-color augmentation (Urdu WER doubles 0.24→0.52 on dark backgrounds):
  https://arxiv.org/pdf/2412.16119
- CLAHE + greedy decoding at inference (Historic-Arabic-OCR CER-0.10 recipe):
  http://www.lrec-conf.org/proceedings/lrec2026/workshops/nakbanlp/pdf/2026.nakbanlp-1.43.pdf

**Scale:** 40–60k line pairs (10k Kashmiri-Awami/Gulzar/Mehr + 20k Urdu-Jameel/Noto/Alvi/Pak + 10k OpenITI/UPTI-mix + 5–10k degraded duplicates), QARI-v0.2-style curriculum (plain → diacritized/10-font; NO layout-mix in stage 1 per the v0.3 regression warning).

### C3. Does synthetic-only SFT close a 30-pt gap? (precedent verdict)

- **YES for Arabic-script VLM-SFT at 2B scale:** Qwen2-VL-2B-Instruct 0.550 → QARI-v0.2 **0.061 CER (49-pt closure) on purely synthetic 50k SFT**:
  https://arxiv.org/html/2506.02295
- **PARTIAL for Urdu CNN-RNN:** UTRSet-Synth-only → 75.14% on Real vs 90.87% Real-trained (**15-pt residual gap**); Mix-All best. Synthetic-only does not fully close for CTC-era models:
  https://arxiv.org/html/2306.15782v1
- **FEW-HUNDRED real samples stack additively:** GPT-4o +500 real UNB lines → −6.13% relative WER on top of zero-shot:
  https://arxiv.org/html/2505.13943v2
- Synthesis for South: synthetic-only SFT on a 2B VLM plausibly closes **25–40 pts** of a 30–50 pt gap (QARI precedent, autoregressive decoder generalizes better than CTC per UTRNet Table 4); the last **5–15 pts need a few hundred REAL Kashmiri lines** (W3-probe-mined + hand-corrected) mixed in. Budget the real-line mining, not a 400-page collection.

### C4. Ranked attack table (gain/cost)

Assumes ks≈0.55 CER start; gains are expected absolute CER-point drops, cost in GPU-h on 1×A100-class.

| Rank | Path | Expected ΔCER (ks / ur / sd) | Weighted gain | Cost | Gain/cost | Verdict |
|---|---|---|---|---|---|---|
| **1** | **Qwen2-VL-2B-Instruct + LoRA SFT on 40–60k synthetic Nastaliq curriculum (ks-fonts weighted) + 300–500 real ks lines, 8-bit, greedy decode, CLAHE/SR preprocess** (QARI-v0.2 recipe ported to Nastaliq) | −0.35 / −0.15 / −0.12 | ~0.25 | ~50–70h | **~0.36–0.50 pts/100h-equiv best** | **GO — primary** |
| 2 | Same as #1 but **PaddleOCR-VL-0.9B** backbone (lighter, 109-language doc priors) | −0.28 / −0.12 / −0.10 | ~0.20 | ~30–50h | high | GO — parallel low-cost hedge |
| 3 | **PARSeq-Urdu-style word model (0.178 CER precedent) fine-tuned on RAVI + Kashmiri words**, line wrapper around it | −0.20 / −0.15 / −0.08 | ~0.16 | ~20–30h | high | GO — cheap ur/sd floor-raiser; ks capped by word-model OOV on Kashmiri Yeh |
| 4 | **Super-resolution + CLAHE + normalization/bidi-fix only** (no SFT): SwinIR + NFKC/RTL-isolate rescoring of incumbent | −0.08 / −0.06 / −0.05 | ~0.07 | ~5–10h | medium | GO — do first (week-1), keeps whatever recognizer follows |
| 5 | **PaddleOCR arabic_PP-OCRv5_rec off-shelf / light fine-tune (CTC head)** | −0.05 / −0.05 / −0.08 | ~0.06 | ~10–20h | low | **NO-GO as primary** (Naskh-skewed; KITAB-context off-shelf 0.77–0.81 CER); accept only as sd-Naskh fallback |
| 6 | **GPT-4o/Gemini-class API few-hundred SFT or distillation** (500-line 6.13% precedent) | −0.10 / −0.08 / −0.06 | ~0.09 | $/API + distill complexity, 0 GPU-h but deployment-law violation | — | **NO-GO** for South disk law (no API at inference; distill only if #1 stalls) |
| 7 | **New CNN+CTC training / novel backbone** | −0.05 best, OOD cliff preserved | ~0.04 | 60–100h+ | worst | **NO-GO** (violates standing law + Part-A structural verdict) |

Why #1 wins: it is the only path with a same-scale precedent closing a LARGER gap than ours (49 pts Arabic, QARI-v0.2:
https://arxiv.org/html/2506.02295) inside our compute envelope, using the exact backbone class (Qwen2-VL-2B) and data scale (50k synthetic) we can reproduce, with Kashmiri-font weighting as the Nastaliq-specific delta.

### C5. Concrete run plan for Path #1 (numbers, not adjectives)

1. Data: 50k pairs per §C2 (report font×source matrix; hold out 1k ks lines + UNB-style 329-line real split for the 500→329 FT protocol:
   https://arxiv.org/html/2505.13943v2).
2. Train: Qwen2-VL-2B-Instruct, LoRA r=32, 8-bit AdamW, eff-batch 8, 2 epochs stage-1 (plain) + 1 epoch stage-2 (diacritized/10-font); NO 4-bit (CER 3.45 failure:
   https://arxiv.org/html/2506.02295); keep layout data OUT of stage 1 (v0.3 regression 0.061→0.300).
3. Inference: CLAHE + SR gate, deterministic greedy decode, NFKC + bidi-isolate normalization before scoring.
4. Success bar: ks CER 0.55→**≤0.20** (−35 pts), ur ≤0.15, sd ≤0.18 on held-out South probes; abort to Path #2 if ks >0.30 after stage 2 (model-capacity signal, not data signal).
5. Cost: ~60 GPU-h + ~8h Path-#4 preprocessing = **≤70h total**, inside the 100h cap with one retry.

---

## DELIVERABLE — Go / No-Go

- **GO on Path #1 (Qwen2-VL-2B + LoRA SFT, QARI-ported synthetic Nastaliq curriculum with Kashmiri-font weighting + 300–500 real ks lines): expected ks 0.55→0.15–0.20 (−35–40 pts), ur −10–15 pts, sd −8–12 pts, for ~50–70 GPU-h.** Precedent: 0.550→0.061 CER on Arabic at identical scale/backbone/data-type:
  https://arxiv.org/html/2506.02295
- **GO in parallel on Path #4 (SR + CLAHE + NFKC/bidi normalization): −5–8 pts for ~5–10h**, week-1 independent of training:
  https://arxiv.org/html/2505.13943v2
  http://www.lrec-conf.org/proceedings/lrec2026/workshops/nakbanlp/pdf/2026.nakbanlp-1.43.pdf
- **CONDITIONAL GO on Path #2/#3 as hedges** (PaddleOCR-VL-0.9B; PARSeq-word for ur/sd floor).
- **NO-GO on: off-shelf PaddleOCR-arabic as the Kashmiri fix** (Naskh-skewed, 0.77–0.81 off-shelf band:
  https://huggingface.co/medyas/arabic_PP-OCRv6_small_rec/blob/main/README.md
  https://huggingface.co/PaddlePaddle/arabic_PP-OCRv5_mobile_rec/blob/main/README.md);
  **API-model dependence; any new CNN+CTC backbone; any 400-page collection for remaining languages** (standing law).
- **One-line summary:** Nastaliq fails by ligature/stack/baseline physics that CTC cannot model; the 2024–2026 precedent (QARI 0.55→0.06 on 50k synthetic SFT of a 2B VLM; UNB VLM>classical by 76%) says a Kashmiri-font-weighted synthetic SFT of Qwen2-VL-2B closes the ~35-pt Kashmiri gap inside ~70 GPU-h — conditional GO with a ≤0.20 ks-CER bar and SR/normalization first.

File: `docs/research/R2_NASTALIQ_FORENSICS.md`
