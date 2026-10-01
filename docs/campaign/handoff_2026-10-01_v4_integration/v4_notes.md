# Plan v4 working notes (planner, 2026-10-01) — survive compaction; every line cites a source

## GOAL (sources)
- uni_v3 E14.2: "COMPLETE the project and BEAT Sarvam (87.39), Vinay's plan, and every India-model competitor — truthfully, via a cracked edge, at full potential."
- uni_v3 C10.1: no fake claims; find THE EDGE (crack) — "Evidence or silence". C10.3 baseline war: Vinay's plan first. C10.4 EDGE THESIS gates freeze. F13.2 bar: integrated, novel, dense.
- HYBRID_CONCERN §2: Vaultstack deck = Stage0 OpenCV → 1 DocLayout-YOLO LoRA → 2 parallel SFT TrOCR+Qwen3-VL-8B+PaddleOCR-VL (akshara-boundary aux loss) → 2b SCST/RL on CER → 3 small-LLM SFT noisy→JSON → 3b SimPO/DPO. FIREWALL: bench data never fine-tuned on.
- HYBRID laws worth carrying: L1 disk truth · L2 one writer · L3 4-page gate · L4 archive never delete · L6 family=1 vote ("9 engines, 7 independent families") · L8 open-script policy · L9 consensus law · L10 agents never edit shared pipeline · L10b audit external plans vs disk (~70% phantoms) · L11 one fact one file.
- HYBRID §7 G-B12: ensemble voting 0/115 beat best single; agreement = precision marker only.
- HYBRID §8: South bench surya 0.430 / anuvaad 0.475 tied; corpus = old-scan class 200 dpi (surya's worst olmOCR category, OldScan 41.8%).
- Boss 2026-10-01: win at any cost (effort, not law-breaking); portable product (Vaultstack main product → organisers/everyone; MLX never assumed); no team mates; free only.
## STATE (disk, 2026-10-01 ~14:00)
- Test set = 5,344 Bengali handwritten WORD crops (13/13 viewed, DISPATCH_LOG §30). Only labelled HW on disk: Bodo/gu (Gujarati words; H2 slice 16,490 writer/page-disjoint).
- Bodhan D1 (MLX): bench small_rep CER 0.054 WER 0.1356 (word-acc ≈86.4 vs published 84.94); 300 gold pairs CER 0.4034 vs surya 0.5660; sample-100 pages CER 0.69 (!); 4-bit≈bf16; PyTorch path needs CUDA. Gate 1 CONDITIONAL PASS.
- Sarvam 2.1 blog (Sep 24): 87.39 overall; ta 87.70 te 91.55 ml 90.24 kn 90.54 bn 93.47 hi 93.52; weak: sat 53.91, ks 54.82, or 80.01.
- South from Sarvam bench fill (official South PDFs 0/23,001 clean). Old Sarvam key dead; new key saved 14:06; 12 South outputs lost.

## THE EDGE (found 2026-10-01 ~15:00, PRIMARY sources opened)
- Official test = Bengali HANDWRITTEN WORD crops (5,344). PPT data slide already names "S2 IIIT-HW / INDIC-HW-WORDS".
- On-disk Datasets/akshardrishti_official/Bodo/gu = IIIT-INDIC-HW-WORDS Gujarati (train 82,563 = paper; val 17,643 = paper).
- IIIT-INDIC-HW-WORDS licence = CC BY 4.0 (AIKosh/IndiaAI page, published via Digital India BHASHINI Division) → commercial OK with attribution. 872K words, 135 writers (CVIT page); Bengali train 82,554 / val 12,947 / test 17,575 (search summary of ilocr/PLATTER; ICDAR'23 Table 1 confirms train 82,554).
- ICDAR 2023 IHTR (Mondal & Jawahar, IIIT-H; PDF read p1–12): train = IIIT-INDIC-HW-WORDS; NEW manually annotated val 1,000 + test 5,000 words/lang from 100 writers; 10 scripts.
  Bengali (Table 2): baseline CRNN (Gongidi&Jawahar) CRR 93.46/WRR 75.34 · Upstage KR 98.99/96.10 (PARSeq + SwinV2 encoder; synthetic Pango 100k/lang pretrain; real pretrain IAM+Korean+Kaggle Bengali.AI; multilingual stage then per-language FT; ensemble) · PERO 98.11/92.02 (CRNN+LSTM LM; used IIIT val/test as extra train) · light 97.54/91.62 (TrOCR) · SRUKR 96.01/88.06 (CRNN EfficientNetV2 + 3-gram LM).
  Others WRR best: Devanagari 93.16 · Gurmukhi 95.28 · Kannada 94.54 · Malayalam 97.16 · Odia 83.38 · Tamil 98.08 · Telugu ~91.4 · Gujarati 62.80 (hard) · avg winner 95.94 CRR / 88.31 WRR.
- Bodhan card IndicOCR-HW (word acc 100×(1−WER), vendor bench): Overall Gemini 72.0 / Bodhan 66.7 / Sarvam 55.4; Bengali 74.8 / 71.3 / 58.3; Gujarati 60.0/55.9/39.2; Telugu Sarvam 59.1 > Bodhan 53.5.
- ⇒ Specialist HTR on in-domain CC-BY data ≈ 92–96 WRR on Bengali HW words vs general doc VLMs 58–75 on HW: a published 20–38 pt gap exactly on the hackathon test distribution. Sarvam weakest at HW.
- MANDELA must-dos: perceptual-hash the 5,344 official test images against IIIT-HW bn train/val/test + ICDAR'23 sets BEFORE any training (if official test ⊂ any training split → exclude; never train on test). Eval on a writer-disjoint set (ICDAR'23 test 100 new writers if obtainable) + Bodhan HW bench as external.

## More facts (2026-10-01 ~15:30)
- LOCAL: .deps/IndicPhotoOCR/IndicPhotoOCR/recognition/models/{bengali,hindi,gujarati,punjabi,marathi,assamese,odia,tamil,telugu,kannada,malayalam}.ckpt = PARSeq scene-text recognisers (Bhashini Team@IIT Jodhpur, repo MIT; weights via github anikde/STocr releases V2.0.0 — weight licence verify).
- PARSeq code Apache-2.0 (github baudm/parseq README). ICFHR/IHTR-2022 dataset page: bn train 82,554 / val 12,947 / test 18,574; "© ICFHR 2022 All Rights Reserved" → eval-only. Research ledger: IHTR-2023/IHDR-2025 sets "academic-use licence" → eval-only; IIIT-INDIC-HW-WORDS via AIKosh = CC BY 4.0 → train OK.
- IIIT-INDIC-HW-WORDS 2021 paper (ledger): 82K train → 4.97% CER in-domain.
- BN-HTRd (Mendeley 743k6dm543): 108,181 Bangla HW words, 150 writers, 786 pages — independent eval candidate (licence check).
- Official Bengali "Images and transcriptions" = 2,938 photographed PRINTED book pages (3000×4000) + paragraph txt → no Bengali HW train data in official set.
- c3 STRATEGY §4 had listed "Bodo-gu/test-test as GT" under WHAT NOT TO COLLECT — superseded: Bodo/gu = IIIT-HW Gujarati (labelled; vocab index) → usable as eval/train per split; test/test stays unlabelled (never GT).
- R7: default backbone Qwen2-VL-2B for weak cells (superseded by Bodhan base in v3); RLVR only on verified gold; no 4-bit recogniser quant unless parity (Day1: 4-bit≈bf16 overall); curriculum word→line→block 50/35/15; sarvam_fill never trains.
- Official judging (RQ1, verbatim tab): Approach (idea, innovation, simplicity, uniqueness & scalability, novelty) · Technical feasibility (features, scalability, interoperability, stack, futuristic) · Product roadmap (productization, cost, GTM, time to market) · Team ability & culture · Addressable market (channel, deployment cost, customization cost, 4-yr resource rate). Named eval target: "accuracy, layout detection, multilingual text handling". Focus area 5: layout-preserving JSON + searchable PDF + transliteration + language detection.
- Prices: Sarvam ₹0.5/page (adapter docs; CIOL); Bodhan API ₹0.20/image (console.bodhan.ai per COMPETITOR_INTEL).
