# VAJRASTRA PRODUCT DEVELOPMENT — 100+ Future Improvements
Scope: Vaultstack's own model/pipeline (the startup product) — informed by what Level 2 benchmark teaches.
Not now-work. This is the roadmap the benchmark data unlocks. Level 3+ territory.

## A. TRAINING DATA (from Level-2 benchmark outputs)
1. Consensus-GT bootstrapping: ≥6/10 engine agreement → pseudo-labeled training set v1
2. Disagreement mining: pages where engines split = highest-information training examples
3. Error-corpus: every engine mistake logged with page → Stage-3 LLM training data
4. Confidence-weighted fusion: train a text-fusion head that picks best engine per region
5. Weighted ensemble distillation: distill 10 engines into one student model
6. Hard-negative mining: pages all engines fail (bad scans) = curriculum for robustness
7. Script-balanced sampling: ensure te/ta/kn/ml equal share + mixed-script pages kept
8. Akshara-boundary annotations (L2A) on consensus pages → aux-loss training signal
9. Region-type stratified sets: tables/forms/handwriting/stamps as separate eval slices
10. Human-in-loop queue: top-disagreement pages → native reviewers → true gold trickle
11. Synthetic augmentation: render Indic text (Sangraha corpus) onto scanned backgrounds
12. Benchmark-derived difficulty score per page → curriculum learning ordering
13. Keep engine outputs as 10-way "multi-teacher" signals, not just text (rank hypotheses)
14. Native-digit preservation rules baked into training data filters
15. Train/dev/test firewall: consensus pages never leak into eval (per CANON)

## B. MODEL ARCHITECTURE (Vaultstack OCR model v0→v1)
16. Baseline: fine-tune TrOCR/Qwen-VL small on consensus-GT (fast first win)
17. PaddleOCR-VL 1.6 fine-tune on our 4 South languages (commercial-friendly license check)
18. Surya-style detection + custom South-recognition head (det is solved, rec is the gap)
19. Per-language morphology heads (akshara-aware) — the CANON's differentiator
20. Calibrated confidence head: energy-based OOD scoring per textline
21. Low-confidence → human review routing (the product's core loop, per CANON)
22. Active-learning: only label pages the current model is unsure on
23. Distillation target: beat weakest free engine with a 10× smaller model
24. MoE routing: script-ID gate → per-script expert heads (te/ta/kn/ml/hin)
25. Two-page spread handling as first-class input format (books are our data)
26. Table-structure recognition head (gridformer-style) for exam tables
27. Handwritten-span detector + separate HW model path
28. Stamp/signature detection as separate class (forms pipeline needs it)
29. Multitask: OCR + script-ID + layout (shared backbone, 3 heads)
30. Contrastive pretraining on unlabeled Indic page crops (self-supervised stage)
31. Hard-attention on matras/conjuncts (visual anchoring loss)
32. Curriculum: clean-print → mixed-script → bad-scan → handwriting difficulty ladder

## C. PIPELINE ENGINEERING (production stage design)
33. Stage-0 preprocessing service: deskew/binarize/border-crop (measured: helps all engines)
34. Layout service: YOLO/IndicDLP → region crops → per-region engine routing
35. Script-ID microservice per region (VIT like IPO's — reuse their approach)
36. Recognition ensemble service: 2-3 engines + fusion, per region type
37. Per-region confidence calibration service (temperature scaling)
38. Human-review UI queue with side-by-side image/hypotheses (Vinay demo-ready)
39. Structured-field extraction: forms → JSON (Stage-3 LLM SFT target)
40. Noisy-text→JSON LLM: train small LLM on engine-output→gold-JSON pairs
41. SimPO/DPO on ranked JSON outputs (Stage 3b from CANON)
42. Evaluation harness: CER/WER + akshara-CER + field-F1, all NFC-normalized
43. Speed-tier models: fast draft (rapidocr-class) + strong verify (surya-class)
44. Budget-aware routing: cheap engine first, escalate only on low confidence
45. Batch inference server: ONNX/tensorRT for trained heads
46. Model registry: versioned South-OCR checkpoints with eval-report attached
47. Data-drift monitor: production page stats vs training set alert
48. A/B harness for engine swaps (plug-in interface — same as run_engine.py law)
49. Per-customer domain packs: exam boards / govt forms / land records finetunes
50. 22-language expansion harness: same pipeline, new script heads (product vision)

## D. BENCHMARK & RESEARCH MOAT
51. South-OCR internal eval: 50 human-verified pages, quarterly refresh
52. Publish "Free Indic OCR capacity report" (this Level-2 as content marketing)
53. Weekly AI4Bharat/Sarvam/Bodhan model watch (Level-3 candidate list auto-updated)
54. Community tesseract fine-tune hunt (Telugu forums have custom models)
55. Reproduce published Indic OCR benchmarks on our pages (calibrate our numbers)
56. Akshara-level eval metric (nobody publishes it — we'd own the metric)
57. Per-region-type difficulty analysis (what breaks each engine class)
58. Failure-mode taxonomy as public blog/doc (startup credibility)
59. Cross-lingual leakage study (te-invoked engine reading ta glyphs — calibration issue)
60. Track PaddleOCR-VL/Qwen-VL releases for South-language support drops
61. Hackathon demo: live page → engine comparison → Vaultstack model wins visibly
62. Competitive matrix vs Sarvam/Bhashini published claims (be honest, be specific)
63. License audit table for every engine (startup-safe vs GPL contamination)
64. Cost model: free-engine CPU serving vs paid API break-even analysis
65. Latency table on Apple Silicon + one cloud instance class (real production numbers)

## E. TEAM & OPERATIONS
66. Weekly dashboard to Vinay: counts + wins + blockers (5-line CANON law)
67. GitHub benchmark reports auto-pushed (code + reports, no data)
68. Onboarding doc: new member runs Level-3 harness in <1hr
69. Label ops runbook: native reviewer assignment flow (ta/kn/ml reviewers)
70. David-call method doc: our eval protocol vs his methodology suggestions
71. Krishna/North cross-check: same harness run on North languages (reuse!)
72. Aryan pipeline adapter: our JSON packs plug into his VLM ingest directly
73. Shared eval pages: 10 frozen pages across North/South for team consistency
74. Model card habit: every checkpoint gets eval + intended-use card
75. Meeting artifact rule: every call → 5-line action file (like SOUTH_CANON)

## F. PRODUCT FEATURES (the citizen-document vision)
76. Photo-quality OCR (tilt/glare/shadow robust) — scene-text path via IPO research
77. Handwriting-first mode: forms where handwriting dominates print
78. Mixed-script page explanation UI ("this page is Marathi in a Telugu book")
79. Region-level translation toggle (OCR → translate pipeline, Bhashini APIs later)
80. Confidence heatmap overlay for reviewers (UX trust builder)
81. Field-level validation rules (Aadhaar/date/amount formats — openbharatocr's lesson)
82. Searchable-PDF export with invisible text layer (immediate user value)
83. Structured JSON API endpoint (per CANON L3 object layer)
84. Batch-processing queue UI for multi-page PDFs (govt office workflow)
85. Offline/on-prem packaging (govt data can't leave premises — big differentiator)
86. Model-size tiers: mobile (100MB) / server (1GB) per customer hardware
87. Privacy mode: all local, zero network (contrast vs cloud-only competitors)
88. Dictionary-assisted post-correction per language morphology
89. OCR-feedback loop: user corrections → active-learning training stream
90. Admin dashboard: volume/quality/per-language stats for the customer

## G. LONG-HORIZON RESEARCH BETS
91. Akshara tokenizer for LLMs (pre-tokenization unit = recognition unit)
92. Sandhi-aware decoding (language model re-ranking of OCR hypotheses)
93. Multimodal RAG on OCR'd citizen docs (search your own documents)
94. Federated learning across govt departments (data never centralizes)
95. Neural compression of scanned archives (store once, OCR anywhere)
96. Autonomous label-machine: model proposes labels, humans only approve diffs
97. Self-improving engine router: bandit algorithm picks engine per region live
98. Semi-supervised pseudo-label cycling on the full Datasets/ dump (400 pages was a sample)
99. Adversarial scan augmentation (realistic defect synthesis: ink, fold, glare)
100. Open-source core + paid-enterprise wrapper strategy (benchmark = credibility engine)
101. India-specific RLHF: native-reader preference pairs on OCR corrections
102. On-device CoreML/NNAPI builds of South-OCR (mobile-first India)
103. Academic partnership: IIIT-H/IITGN data collaboration (hackathon → relationship)
104. Standard proposal: "South-OCR Eval" benchmark paper (own the metric, own the field)
105. The 22-language endgame: one model, script-experts, from this exact harness
