# R6 — Competition Intel: Bhashini AksharDrishti OCR Hackathon 2026

Status: 2026-09-26. Method: official Bhashini pages (JS-rendered, read via browser snapshot on 2026-09-26) + web search for pricing.
Rule used throughout: **VERIFIED** = on the official page; **INFERENCE** = our reading, labeled as such. No official scoring formula,
eval-set spec, or submission spec is published as of this date — §§2–4 say exactly what is verified vs inferred.

## 1. VERIFIED official facts

- Hackathon: BHASHINI AksharDrishti (अक्षरदृष्टि), OCR Hackathon 2026, run by DIBD / National Language Technology Mission.
  Launch 12 Feb 2026, Mode Pan-India, Focus OCR & AI.
  Source: https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon (hero + About sections, snapshot 2026-09-26).
- Problem statement (verbatim core): existing OCR "struggle with Indian-language documents due to challenges like complex layouts,
  low-quality scans, handwritten text, and code-mixed content" and "often fail to preserve structure, accuracy, and multilingual
  adaptability"; goal is "robust OCR models capable of handling diverse document types, improving recognition accuracy, and delivering
  deployment-ready solutions". Source: same page, Problem Statement modal (§§1–3, snapshot 2026-09-26).
- Named open-source baselines to fine-tune/benchmark: **Tesseract, EasyOCR, TrOCR, PaddleOCR**; named architectures: **LayoutLM, Donut,
  DocTR**; "Use of GPU-based fine-tuning environments" is explicitly listed as a focus area.
  Source: same page, Problem Statement modal §§2–3 ("Objectives", "Model Adaptation and Fine-Tuning").
- Post-OCR outputs named: layout-preserving **JSON, searchable PDF**; plus automatic transliteration, language detection,
  context-based correction. Source: same page, modal §3 "Post-OCR Pipeline Innovations".
- Evaluation parameters (VERIFIED, exact table from the Evaluation Process tab): Approach Towards Problem Solving (innovation, novelty,
  scalability) | Business Use Case (USP, vision) | Solution Technical Feasibility (features, scalability, interoperability, stack,
  futuristic orientation) | Product Roadmap (productization, cost, go-to-market, time-to-market) | Team Ability & Culture |
  Addressable Market (deployment/customization cost, 4-year resource-rate evaluation). Source: same page, Evaluation Process tab.
- Eligibility (VERIFIED): Indian company under Companies Act or DPIIT startup definition; unregistered teams may enter but must register
  if selected for final submission; NOC required for employer-associated individuals (company gets no prize/IPR rights).
  Source: same page, Eligibility Criteria tab; general rule also at https://bhashini.gov.in/sahyogi/startup/eligibility.
- Timeline (VERIFIED): Launch 12/02/2026; **Pitch Screening Session 23/07/2026**; every other milestone (registration deadline, Stage 1
  screening/results, Stage 2 prototype submission/evaluation/results, Stage 3 final submission/evaluation, winners) = **TBD**.
  Source: same page, Timeline tab. Registration link reported "active" in Latest Updates rotator (snapshot 2026-09-26).
- Prize pool for AksharDrishti itself: **NOT published** on the page (Prize nav exists; no amounts rendered as of 2026-09-26).
  Analogy only (INFERENCE): sister Bhashini hackathons publish large purses — Sanrakshan total ₹1 Crore
  (https://bhashini.gov.in/sahyogi/hackathon/sanrakshan-hackathon); LEAP prototype-stage ₹50,000/team, winner ₹10 lakhs + 4-year
  deployment contract (https://bhashini.gov.in/sahyogi/startup/leap-hackathon).

## 2. Scoring formula — NOT published (read carefully)

- VERIFIED: **no metric, formula, weighting, or text-normalization rule (CER vs WER, per-script averaging/weighting) appears anywhere on
  the official page** as of 2026-09-26. The page speaks only of "recognition accuracy", "layout detection", and "multilingual text
  handling" (modal §2 objective: "Establishing Standardized Evaluation Pipelines for accuracy, layout detection, and multilingual
  text handling").
- INFERENCE (not a rule): expect hidden-test evaluation dominated by character/word accuracy, likely **CER primary + WER secondary**,
  possibly macro-averaged across languages/scripts, with layout-preservation (JSON structure) checked qualitatively by jury. This is
  standard OCR-hackathon practice, NOT a published formula — do not overfit to any single normalization.
- South implication: keep optimizing true CER/WER on our own renders (level2/reports/LEADERBOARD.md, CER_BY_SCRIPT.md), keep layout
  JSON valid, and keep a normalization note in the submission writeup (e.g. Unicode NFC, strip control chars) so any reasonable official
  normalization still favors us.

## 3. Eval-set composition — official part unpublished; local dataset inventoried read-only

- VERIFIED (official): eval covers "diverse document types": complex/multi-column/nested-table layouts, forms, govt/legal templates;
  blur/fade/folds/stamps/seals/skew/rotation; full-page handwritten, cursive, mixed typed+handwritten, regional handwriting styles;
  multi-script docs (e.g. Hindi–English–Tamil), code-mixing, language switching. Source: modal §3 (snapshot 2026-09-26).
  No published counts, language list, printed/handwritten ratios, or file formats.
- VERIFIED (local, read-only `ls` only — nothing copied): `Datasets/akshardrishti_official/` contains **24 per-language dirs**
  (Assamese, Bengali, Bodo, Dogri, English, Gujarati, Hindi, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Manipuri, Marathi,
  Mixed Languages, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu, Urdu) plus `test/`, and
  `Datasets/akshardrishti_official/test/test` holds **5,344 files** (matches the reported 5,344 unlabeled jpgs).
- INFERENCE: the hidden eval likely overlaps this distribution (same 22-scheduled-languages + English + Mixed Languages shape), so the
  5,344 unlabeled test jpgs are our best proxy for eval — use for internal measurement only, never as training labels.

## 4. Submission format — NOT published; Bhashini-pattern inference

- VERIFIED: nothing on the page specifies weights-vs-API-vs-Docker, time limits, or CPU/GPU at eval. VERIFIED adjacent facts: the
  program is a 3-stage Screening → Prototype → Product Building journey (standard across Bhashini challenges, e.g.
  https://bhashini.gov.in/sahyogi/hackathon/bsv2), and AksharDrishti demands "deployment-ready solutions compatible with Bhashini's
  document stack" with layout-preserving JSON/searchable-PDF outputs (modal §§2–3).
- INFERENCE: prepare (a) a hosted/API demo + (b) a reproducible Docker image with weights or download script, CPU-runnable with optional
  GPU speedup, plus a 10-minute jury pitch. Do not assume internet at eval — vendor all weights/model files.

## 5. Judging beyond the metric (VERIFIED parameters, §1 table)

Jury criteria are product- and team-weighted, not metric-only: innovation/novelty/uniqueness, business case/USP/vision, technical
feasibility + stack + interoperability, productization cost + go-to-market + time-to-market, team effectiveness, 4-year addressable-market
costing. INFERENCE: Bhashini-API integration (Udyat API key flow is the documented hackathon path) and a live citizen-service demo
(governance/education use case) will score under Feasibility + Business Use Case. At least: demo must call or be deployable on the
Bhashini stack; writeup must cover cost-to-build and deployment story, not just CER.

## 6. Timeline vs our Oct 1 freeze

Official: only 12/02/2026 (launch) and 23/07/2026 (pitch screening) are dated; all submission/evaluation/winner dates TBD — so there is
no published conflict with our internal freeze. Our **Oct 1 freeze is internal** (docs/PLAN.md: W3 redraw → free engines → W4 → freeze
after Wed 2026-10-01), and it stands: freeze the wrap-only system first, then treat any announced official deadline as a delta, not a restart.
Demo logistics unpublished — INFERENCE: expect a jury pitch + live prototype demo (10-min format per MoSPI hackathon SOP precedent:
https://www.mospi.gov.in/sites/default/files/announcements/Standard%20Operating%20Procedure(SOP)%20for%20Conducting%20Hackathon.pdf).

## 7. Constraints (VERIFIED vs open)

- VERIFIED: Indian-entity eligibility + NOC rule (§1); deployment-ready + Bhashini-stack-compatible deliverable (§1).
- NOT published: model size caps, license constraints, internet-at-eval policy, per-language coverage minimums. INFERENCE: assume a
  22-scheduled-language (+English) coverage expectation given the dataset's 24-dir shape; prefer permissive licenses (Apache-2.0/MIT)
  for anything we ship; assume offline eval.
- Team note: Vaultstack AI competing — ensure DPIIT/startup registration + employer NOCs are filed before any final submission.

## 8. Competition — no public field

No public team list, leaderboard, or prior AksharDrishti winners found (all result milestones TBD; Devpost/Unstop host no AksharDrishti
listing as of 2026-09-26). The generic "Hackathon 2026 Problem Statements" Scribd doc is unrelated noise. Watch the official page's
Latest Updates rotator + Bhashini portal for Stage-1 qualifier announcements.

## 9. GPU-budget table — ~30 GPU-hours LoRA/QLoRA of a 1–2B VLM (Task 4)

Assumes QLoRA (4-bit) 1–2B VLM ≈ 10–16 GB VRAM → needs ≥16 GB cards; T4 (16 GB) is marginal-but-workable, L4/A10/4090 comfortable.
Prices checked 2026-09-26; spot/marketplace rates move hourly.

| Option | Cost | VRAM / GPU | Session limits | Fits 30 h QLoRA? |
|---|---|---|---|---|
| Kaggle free (https://www.kaggle.com) | $0 — 30 h/wk GPU (T4/P100), 20 h/wk TPU (per AgentDeals 2026-04-05; resourify.com) | T4 16 GB / P100 16 GB | ~9–12 h sessions, 20 GB disk, public notebooks | YES — but split across weeks/sessions; weakest card |
| Colab Free | $0, usage-limited, T4, ≤12 h sessions, GPU not guaranteed (per Thunder Compute 2026-07-01 roundup) | 16 GB | disconnects, no guarantee | MAYBE for smoke runs only |
| Colab Pro / Pro+ (https://aisotools.com/pricing/google-colab) | $11.99 / $49.99 mo, better GPUs + longer sessions | up to A100-class on Pro+ (availability varies) | monthly quota | YES (Pro+ safer) — cheapest paid path |
| Lightning AI (https://lightning.ai/pricing; docs: 5 free credits = $5, "up to 80 free GPU hours" starter) | free credits then ~$0.19/h (T4) → $6.53/h (H200) (per usagepricing.com 2026) | T4 → H200 | Studio restart every 4 h on free tier | YES — free credits cover ~25 h T4-class; top up ~$10 |
| Modal free tier (https://modal.com; ledger 2026-09-04: T4 $0.59/h, A100-40GB $2.10/h, $30/mo free credit) | $30/mo free credit, per-second billing | T4 → B300 | serverless, no long-session issue | PARTIAL — $30 ≈ 50 h T4 or ~14 h A100; good for eval/inference bursts, pricey for 30 h A100 training |
| Lambda on-demand (https://lambda.ai/cloud) | from $0.50/h (small GPUs); A100/H100 on demand (~$1.1–3/h class) | A100/H100/GH200 | on-demand, no session cap | YES — budget ~$35–60 for 30 h A100-class |
| Vast.ai spot 4090 (https://vast.ai/pricing: 4090 from ~$0.13–0.14/h, median ~$0.42–0.49/h; getdeploying.com Sep 2026) | ~$0.15–0.50/h interruptible | 4090 24 GB | interruptible (spot) | YES — 30 h ≈ **$5–15**, best $/VRAM; use checkpointing |
| Vast.ai spot A100 (marketplace, varies ~$0.4–0.9/h) | ~$0.4–0.9/h interruptible | A100 40/80 GB | interruptible | YES — 30 h ≈ **$12–27** |
| Sarvam Vision/Document Digitization API (https://docs.sarvam.ai/api/getting-started/pricing) | **₹0.5/page** (max 10 pages/job) | n/a (API) | per-job page cap | per-1000-pages = **₹500 (~$6)**; 5,344 test pages ≈ ₹2,672 (~$32). Note: 67% price cut Jun 2026 after 35M pages (CNBC-TV18 2026-06-01) — docs price already reflects it |

## 11. REFRESH 2026-09-26 (Lane C2, Level 7 campaign — appended, nothing above rewritten)

Method: web search 2026-09-26 (official Bhashini page is JS-rendered and unreadable to fetchers, same as before — official-page claims below carry forward from the 2026-09-26 snapshot in §1). VERIFIED vs INFERENCE on every claim. Full record ledger: `docs/research/level7/c/c2/LEDGER.md` (100+ records).

### 11.1 Timeline updates (VERIFIED unless marked)

- Registration deadline was **extended to 30 March 2026** (VERIFIED: Bhashini DIBD LinkedIn post 2026-03-14; original last date 12 March 2026 per launch posts 2026-03-02). No registration-date conflict with our internal Oct 1 freeze.
- **Pitch Screening Session 23/07/2026** stands as the only dated post-registration milestone (carried from §1 snapshot). All Stage 1/2/3 submission, evaluation, results, and winner dates remain TBD — no published conflict with our plan.
- No public Stage-1 qualifier list, leaderboard, or OCR-track winner list found as of 2026-09-26 (INFERENCE: field is still dark; watch the official page Latest Updates rotator + Bhashini LinkedIn).

### 11.2 Winner-field correction (VERIFIED — supersedes any loose "Plenome won AksharDrishti" reading)

- Press reports (Times of India 2026-08-10; Blab AI 2026-08-09) say IIT-Madras-incubated **Plenome won "BHASHINI's all-India AI hackathon"** with Ashwin AI (voice-to-prescription, ₹35 lakh pilot prize, AIIMS New Delhi deployment, 90–95% transcription accuracy claim).
- VERIFIED correction from primary sources: Plenome's own site claims "**National winner, Bhashini DIC Hackathon 1.0**" for a **multilingual healthcare transcription and service delivery challenge (Problem Statement 1)** — a voice-to-text challenge, NOT the AksharDrishti OCR track. The Blab piece conflates the two. **There is therefore NO verified AksharDrishti OCR-track winner as of 2026-09-26.**
- INFERENCE for us: (a) do not cite Plenome as the OCR team to beat; (b) the ₹35 lakh pilot prize + AIIMS deployment + 4-year-contract pattern (cf. LEAP §11.4) confirms the win condition is deployment + product story, not CER alone — consistent with §5.

### 11.3 Competitor/team scan (all VERIFIED existence + numbers; threat readings marked INFERENCE)

- **Sarvam Vision 2.1** (2026-09-24): Indic OCR Bench 6,909 samples, overall 87.39 vs Bodhan 84.94 vs Gemini 3.6 Flash 79.35. Weak cells land EXACTLY on ours: **Santali 53.91, Kashmiri 54.82, Odia 80.01**. Bodhan beats Sarvam on Santali (68.30). Training disclosed: synthetic+real → SFT → RLVR; harness = layout parser + reading-order pointer around the VLM. API ₹0.5/page.
- **Bodhan IndicOCR** (AI4Bharat/IITM, Sep 2026): open-weight, 33M layout (PP-DocLayoutV3/RT-DETR) + 0.8B block OCR (Qwen3.5-0.8B), 15M+ docs, 22 langs × 13 scripts printed + 12 langs handwriting; OmniDocBench-en 92.76, internal printed bench 86.2%; API ₹0.20/image; NeMo-trained, TensorRT-LLM/vLLM-served. (INFERENCE: the wrap-or-finetune baseline to beat alongside Sarvam.)
- **Krutrim Chitrapathak-2** (arXiv:2602.16430): fine-tuning an existing OCR VLM beats LLaVA-from-scratch (accuracy + 3–6× latency); Telugu SOTA; Parichay rotation + LoRA recipe hits 89.8% EM on 9 govt doc types. (INFERENCE: recipe evidence for our W6 "fine-tune, don't build" stance.)
- **ScriptMoE** (arXiv:2609.24058, 21 Sep 2026): shared encoder + top-2 script experts + shared expert; PP-OCRv5 end-to-end F1 65.71 → 80.89. (INFERENCE: script-router justification for sat/ks/mni/Nastaliq specialists, post-§6.4 verification only.)
- **PaddleOCR-VL-1.6**: 96.33% OmniDocBench v1.6 (0.9B, Apache-2.0), weak-region-mined data + CPT→SFT→RL post-training; Real5 physical-distortion bench 93.19.
- **Surya OCR 2** (Datalab, 650M): 83.3 olmOCR-bench, 91-lang internal 87.2; code Apache-2.0 / weights OpenRAIL-M; old_scan subscore only 42.8 (INFERENCE: nobody solves old scans — our OldScan 55.3 cell is attackable).
- **NE-OCR** (MWire Labs, Mar 2026, CC-BY-4.0): 86M ViTSTR, 94.99% mean char-acc incl. **Meitei Mayek 95.56%** where EasyOCR scores 2.50% and Tesseract 2.24% — direct precedent that our mni cell needs a specialist, not more shared training.
- **OdiaGenAI Qwen2.5-VL-3B LoRA** (rank 64, H100 ~12.7h, early-stopped, conjunct/matra errors dominate) and **`ori_hist` Tesseract model** (1875 letterpress Odia CER 48.1% → 17.2%) — (INFERENCE: Odia 80.01 is attackable via domain fine-tune + historical-font handling).
- **Koshur Pixel** (arXiv:2606.23144): 500K+ synthetic Kashmiri Nastaliq renders from KS-PRET-5M via SynthOCR-Gen — (INFERENCE: validates our synthetic-render strategy for ks if W6 needs it; no download without approval).
- Scene/general: IndicPhotoOCR (IITJ, 11–13 langs, oracle TD+SI beats Google OCR by 30% WRR), BSTD (6,582 images/100K+ words), Mozhi/Mozhi-LR (CRNN+CTC, low-resource WRR 80–93%), Urdu Newspaper Benchmark (Gemini-2.5-Pro WER 0.133 vs Kraken 0.558; SwinIR SR +25–70%), Devanagari stress-test (real scans collapse synthetic-strong models).

### 11.4 Prize analogy re-verified (all VERIFIED from official pages)

- Sanrakshan: **₹1 Crore** total pool. LEAP: ₹50,000 prototype teams, **₹10 lakhs winner + 4-year deployment contract + ₹10L O&M** per problem statement (PS-2 winner Team Multilipi, Sep 2026). Bhashini Challenge (MyGov): ₹1–2L stage funding, **₹50L winner + 1-year govt deployment**. Samanvay outreach: ~₹3 Cr combined ecosystem pool. INFERENCE unchanged: expect AksharDrishti purse in the ₹10L–₹1Cr band with a deployment contract as the real prize — the submission must demo on / integrate with the Bhashini stack (Udyat OCR endpoint, IIIT-H serviceIds).

### 11.5 What changed for our win condition: nothing structural, two deltas

1. DELTA (INFERENCE): the weak cells are now *confirmed by the vendor's own bench* (Santali 53.91 / Kashmiri 54.82 / Odia 80.01) — our probe's value proposition (independent measurement on official data + specialists for exactly these cells) is stronger, not weaker.
2. DELTA (VERIFIED): Bodhan is open-weight and cheap (₹0.20/image) — the "wrap-only fallback" (§10) now has two wrap targets (Sarvam API, Bodhan weights/API), and any W6 GPU ask competes against ~$5–15 for 30h of 4090 spot (Vast.ai, Sep 2026).

## 10. Recommendation

Minimum viable budget: **~$15–30 total — Vast.ai spot RTX 4090 (~$5–15 for 30 h QLoRA) + $11.99 Colab Pro as fallback + Sarvam API ~₹500/1000 pages for spot-check benchmarking only**; run the free legs first (Kaggle 30 h/wk + Lightning free credits + Modal $30 credit cover all inference/probe work at $0). Zero-budget fallback stays fully viable: ship the wrap-only system (frozen L1/L2 engines + layout-preserving JSON/PDF + Bhashini-stack demo), which matches every VERIFIED judging parameter except raw-accuracy novelty — LoRA is an accuracy booster, not a submission prerequisite, and with no published metric weighting there is no evidence it is the win condition.
