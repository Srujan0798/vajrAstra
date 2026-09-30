# Research store — primary sources (W1)

Living recipe: `docs/research/W1_RECIPE_REFRESH.md`. Hybrid: `docs/architecture/W2_HYBRID.md`. This file is the citation shelf only.

| Date | Source | Load-bearing fact |
|---|---|---|
| 2026-09-24 | [Sarvam Vision 2.1](https://www.sarvam.ai/blogs/sarvam-vision-2-1) | SFT then RLVR. Layout parser + pointer reading-order. Indic bench 87.39 overall. OldScan 55.3. Santali 53.91 / Kashmiri 54.82 / Manipuri 85.12. |
| 2026-09-24 | HF [`sarvamai/indic-ocr-bench`](https://huggingface.co/datasets/sarvamai/indic-ocr-bench) | 6,909 blocks, 22 scheduled langs + EN. Word accuracy = 100×(1−WER). Our probe is 20/lang from `small_representative`. |
| 2026-09 | HF [`bodhan-ai/indic-ocr`](https://huggingface.co/bodhan-ai/indic-ocr) | 33M PP-DocLayoutV3 + 0.8B Qwen3.5 block OCR. Printed 22 langs. Santali 68.30 on Sarvam’s bench (beats Sarvam). Open weights. |
| 2026-09-21 | [ScriptMoE arXiv:2609.24058](https://arxiv.org/abs/2609.24058) | Scene STR MoE. PP-OCRv5 F1 65.71→80.89. Ol Chiki / Meitei Mayek outside its 10 scripts. Not a document backbone. |
| 2026-02 | [Chitrapathak-2 arXiv:2602.16430](https://arxiv.org/abs/2602.16430) | Fine-tune Nanonets-OCR2-3B beats CLIP+LM train. Telugu char ANLS 6.69 vs 11.00, 3–6× faster. Parichay 89.8% EM on 9 EN govt docs. |
| 2026-06 | [PaddleOCR-VL-1.6 arXiv:2606.03264](https://arxiv.org/abs/2606.03264) | CPT→SFT→GRPO from 1.5 ckpt. PP-DocLayoutV3 frozen. OmniDocBench v1.6 96.33. Already in the PPT. |
| 2026-06 | [Devanagari stress-test arXiv:2606.29213](https://arxiv.org/abs/2606.29213) | Synthetic hides gaps. Real Hindi scans: Qwen3-VL-8B 75.2 beats GPT-5.5 58.5. olmOCR-7B 40.5. |
| 2026-09 | [FaithC4 arXiv:2607.21617](https://arxiv.org/abs/2607.21617) | General VLMs rewrite imperfect text. OCR-specialized VLMs stay faithful. |
| 2026-10 | [Nanonets OCR 2](https://nanonets.com/research/nanonets-ocr-2/) | Qwen2.5-VL-3B, synth then manual FT. Chitrapathak-2 init. |
| 2025-10 | [olmOCR 2 arXiv:2510.19817](https://arxiv.org/html/2510.19817v1) | SFT then GRPO with HTML unit-test rewards. English-centric. |

Consensus.app was named in the meeting (10 free searches/day). This store used official blogs, HF cards, and arXiv because Consensus is JS-gated here. Human can still paste Consensus cards into W1.
