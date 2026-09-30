---
name: proto-105-consensus-results-to-decisions
description: "Added 2026-09-30 ~21:10 IST — the 3 Consensus Deep Search results (stored in docs/sources/consensus/*.tex) read in full by the planner and mapped finding-by-finding to our decisions (C1-1…C3-7): what each supports, contradicts or adds (post-OCR correction B-18, handwriting now central, metric additions), which paper to open before quoting, the owner (Agent 2), done-when, and tomorrow's follow-up searches"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T15:24:20.443Z
---

# PROTO-105 — CONSENSUS RESULTS → DECISIONS (owner: Agent 2; Agent 1 reads the rows before Day 2/3)

**Files:** `docs/sources/consensus/2026-09-30_Q1_model-and-training.tex` · `…_Q2_hard-scripts-handwriting-degraded.tex` · `…_Q3_system-layout-postcorrection-langid-eval.tex` + `README.md` (index) + `MOVE_LOG.txt` (sha256). The bibliography with DOIs sits at the top of each file.
**Law:** a Consensus summary is a LEAD, not evidence. Before a finding becomes a RESEARCH_DECISIONS row, open the paper (DOI/arXiv id below), confirm the number, and quote it (≤15 words). If the paper can't be opened → the row says UNVERIFIED-SUMMARY and nothing is quoted to Vinay from it. No new essays: rows go into `docs/campaign/RESEARCH_DECISIONS.md`, build items into proto-100.

## The findings, mapped (planner read all three files in full, 2026-09-30)
### Q1 — the model
- **C1-1** An OCR-specialised base + LoRA beats a generic VLM. Initialisation dominates: in Indic print, same-language pretraining gave 92% WRR vs cross-lingual 51% vs scratch 6%.
  - Papers: Faraz 2026 arXiv 2602.16430 "Designing Production-Scale OCR for India" (Chitrapathak-2); Manna 2025 doi 10.1145/3774521.3774533.
  - → SUPPORTS Plan v3 (Bodhan base, LoRA per language). Decision unchanged; cite in the plan.
- **C1-2** 4-bit LoRA "often preserves gains" (moderate, 6/10): QARI (arXiv 2506.02295) used optional 4-bit; Elkousy 2026 (doi 10.1016/j.procs.2026.01.043) 4-bit Qwen2.5-VL −29% CER on Arabic print. Few controlled 4-bit vs 8-bit ablations exist.
  - → **CONTRADICTION-CHECK** against proto-100 B-01 ("no 4-bit for ks/ur/sd", from QARI 3.45 vs 0.091). Open QARI: separate 4-bit QLoRA TRAINING from 4-bit INFERENCE.
  - B-01 stays until Day 1's measured 4-bit vs bf16 per script decides it.
- **C1-3** Synthetic data is necessary but insufficient; synthetic + real transfers better.
  - Baseer arXiv 2509.18174: 300k synthetic + 200k real. Singh 2026 arXiv 2606.29213: clean renders make systems look tied; real scans make 9/10 collapse (EasyOCR chrF++ 93.6 → 58.3).
  - → Day 2 data must include real scans.
  - → Our benchmark's `official_pdf` tier is clean renders and can OVERSTATE quality. Report the real-image tiers separately (proto-62) and say so in the plan.
- **C1-4** Data needed: 100–1,000 labelled lines help with cross-script transfer (Al-Azzawi 2026 arXiv 2605.02089); full OCR needs hundreds of lines or thousands of word images unless the base is strong.
  - → Day 3 picks target languages only where we hold ≥ a few hundred real lines/words.
- **C1-5** RLVR/GRPO: moderate (4/10), mostly cuts failure modes and hallucination (LightOnOCR arXiv 2601.14251). → Keep RL last and optional (proto-89 §C).
- **C1-6** Hard-example mining for Indic/Arabic CER: weak (2/10). → Do not build (drop old #22).
- **C1-7** Cleaning labels alone improved CER by up to 1.8 points (Al-Azzawi 2026 doi 10.1016/j.patcog.2026.114621). → Run the proto-65 GT-defect checks on every training set before Day 3.
- **C1-8** Competitors/alternatives to add to `COMPETITOR_INTEL.md`:
  - Chitrapathak-2 (Faraz 2026: near Gemini-2.5-Flash on 9 Indic languages, SOTA Telugu; struggles on forms/index layouts);
  - LightOnOCR-2-1B;
  - HunyuanOCR-1.5 (arXiv 2607.04884);
  - GlotOCR Bench (arXiv 2604.12978: OCR fails beyond a handful of scripts);
  - Qwen3-VL-8B beat GPT-5.5 on real Devanagari scans (Singh 2026).

  Kashmiri synthetic sets: Koshur Pixel (arXiv 2606.23144) and synthocr-gen (arXiv 2601.16113) — licence check for B-03 (600K-KS stays HOLD).

### Q2 — the hardest cases
- **C2-1** Best CERs:
  - Urdu printed Nastaliq 0.91% (Efficient CRNN, Nasir 2024 doi 10.1016/j.ipm.2023.103544; synthetic multi-font corpus);
  - Urdu handwritten 5.27% (ET-Network doi 10.1371/journal.pone.0302590);
  - Hindi handwritten words 2.14% (Kumar 2026 doi 10.1038/s41598-026-46572-0);
  - degraded Sanskrit print 3.71% (Dwivedi 2020 doi 10.1109/cvprw50498.2020.00288).

  **Kashmiri Nastaliq: no CER paper** → our own measurement is the reference (B-03).
- **C2-2** Ol Chiki: digits only (99.13% on a digit set). Meitei Mayek: **no OCR paper**. Odia: character-level accuracy only.
  - → No literature baseline exists for sat/mni/or page OCR; the Bodhan/Sarvam numbers are the only references (B-04/B-05). The honest claim: few published page-level results exist.
- **C2-3** Handwriting:
  - PARSeq-style transfer printed→handwritten is strongest across 10 Indic languages (Lalitha 2025 doi 10.1007/978-3-031-93688-3_17);
  - ICDAR 2023 Indic HTR competition winner 95.94% CRR / 88.31% WRR (Mondal 2023 doi 10.1007/978-3-031-41679-8_25);
  - SemiHastakshar semi-supervised (doi 10.1145/3774521.3774605);
  - PLATTER page-level HTR (arXiv 2502.06172).

  → **Handwriting is now central** (proto-104 rev 3 §H: the official test images are handwritten words). Triggers RQ-10: datasets + models + licences.
- **C2-4**
  - Tables/forms: Parichay 89.8% exact-match fields (Faraz 2026). Adaptive engine SELECTION gave +23.7% over single engines on 15k government documents (Zhang 2026 doi 10.69987/aimlr.2026.70103).
  - → CONTRADICTION-CHECK against our "voting 0/115": selection ≠ voting. RQ-11 (oracle gap) decides whether a router is worth building.
- **C2-5** Restoration:
  - PreP-OCR: −63.9% to −70.3% relative CER on 13,831 real historical pages (restoration + post-correction; arXiv 2505.20429).
  - Super-resolution helped low-res pages but HURT high-res ones (Rawat 2021).
  - → B-06: a gated pre-pass only for low-quality inputs, A/B-tested on our degraded subset (RQ-6).

### Q3 — the system and fair proof
- **C3-1** Layout + reading order, strong (8/10): IndicDLP arXiv 2512.20236 (Indic layout dataset); dots.ocr arXiv 2512.02498. → Justifies Bodhan's layout + reading-order stage; matches the vajrAstra F7 finding.
- **C3-2** LM post-OCR correction, strong (8/10):
  - Bhandari 2026 doi 10.1145/3815575: CER hi 10.20→6.73, gu 6.10→1.39, mr 8.19→3.29;
  - Sanskrit +23 points (Maheshwari 2022 arXiv 2211.07980);
  - RoundTripOCR arXiv 2412.15248: synthetic correction pairs for hi/mr/ne/kok/brx/sa;
  - caveat: a post-corrector did not transfer across engines (Singh 2026).
  - → **NEW build candidate proto-100 B-18:** a post-correction pass trained on BODHAN's own errors, from our training pool only (leak-free), measured on held-out documents with a paired bootstrap. Day 4 experiment; ship only if it wins.
- **C3-3** Multi-engine fusion, moderate (6/10); raw confidence is an unreliable proxy (Jhala 2026 arXiv 2608.07478). → Keep "agreement flag only" (our 0/115).
- **C3-4** Same-script language ID: IndicLID / Bhasa-Abhijnaanam (arXiv 2305.15814; all 22 languages, native script) is strong on text; OCR-page evidence is weak.
  - → RQ-8: the product's per-block language = IndicLID on the RECOGNISED text + script from Unicode ranges. Licence check + an eval on our outputs; the download needs the boss.
- **C3-5** Structured output: IndicOCR pipeline (Tulsyan 2024 doi 10.1145/3632410.3632502) and bbOCR (arXiv 2308.10647); no standard for JSON/PDF evaluation. → Our schema (B-11) is fine; state it plainly.
- **C3-6** Fair evaluation, strong (9/10): report CER AND WER, state the NFC normalisation, test on real scans, report the median + a catastrophic-failure rate, not only means (Singh 2026; Caravani 2026 doi 10.1016/j.ipm.2026.105047).
  - → proto-80 metric set: ADD the median + catastrophic-failure rate (define it, e.g. CER > 0.5) + an NFC statement to every table.
- **C3-7** Tamil references for South: Sivashanth 2026 Tamil OCR benchmark (doi 10.4038/icter.v18i3.7305); Jayatilleke 2025 zero-shot Sinhala/Tamil (arXiv 2507.18264).

## Agent 2's work (in this order, after its current repair step)
1. Open the ~15 papers named above (at minimum: Faraz 2026, QARI, Singh 2026, Bhandari 2026, Lalitha 2025, Mondal 2023, Zhang 2026, PreP-OCR, IndicLID, Manna 2025, Baseer, LightOnOCR, Caravani 2026, Al-Azzawi ×2) → one RESEARCH_DECISIONS row per C-id: verdict ADOPTED / SUPPORTS / CONTRADICTION / UNVERIFIED-SUMMARY + the decision it touches + URL + quote.
2. Add proto-100 rows B-18 (post-correction on Bodhan's own errors) and B-19 (handwriting track: see proto-104 rev 3 §H), planner-approved as candidates, gated by measurement.
3. Update `COMPETITOR_INTEL.md` with C1-8 (numbers only after opening the papers).
4. Put the top 6 findings (C1-1, C1-3, C2-3, C3-1, C3-2, C3-6) into the Plan v3 draft (step G), each with its paper.
5. Tomorrow's follow-ups (normal searches, not Deep Search) written in W4.md as one-liners:
   - "Chitrapathak-2 per-language OCR results for Indian languages";
   - "handwritten word recognition Bengali Gujarati Indic state of the art CER dataset licence";
   - "converting legacy-font Tamil Telugu Kannada PDF text to Unicode" (this could unlock GT for the 23,001 South PDF pages).

**Done when:** `grep -c "C[123]-[0-9]" docs/campaign/RESEARCH_DECISIONS.md` ≥ 20, every row has a URL, and the plan draft cites ≥ 6 opened papers.

Related: [[proto-97-research-still-to-do]], [[proto-100-research-to-build]], [[proto-104-project-first-critical-path]], [[proto-80-hackathon-metric-alignment]], [[proto-62-gt-tier-stratified-reporting]], [[proto-81-handwriting-degraded-coverage]]
