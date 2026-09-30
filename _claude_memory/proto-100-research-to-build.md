---
name: proto-100-research-to-build
description: "Added 2026-09-30 evening (boss: 'read all those reports… the results the data they have done, so we need to implement and use those researched details') — the research → build queue: 17 concrete build items the planner extracted by reading R1–R4, R6, R7, B12, MENTOR_PLAYBOOK and both meetings in full (4-bit ban for ks/ur/sd, Perso-Arabic scoring normalization, Kashmiri/Manipuri/Santali tracks, old-scan ablation, product outputs the official jury asks for, Vinay's gates), each tied to a Plan v3 day, owner, gate and approval; proto-95 ADOPTED/BUILD rows append here"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T10:50:43.845Z
---

# PROTO-100 — RESEARCH → BUILD QUEUE: research that must turn into work, not archive

**Boss, 2026-09-30:** "read all those reports… the results, the data they have done, so we need to implement and use those researched details and merge and improve… they should not be here as junk." Concerns: H1, H2 ([[proto-99-concern-crosswalk]] §H) and the meeting rows in §I.

**How this file works:**
- The planner read the decision-grade reports and both meetings in full on 2026-09-30:
  - R1_SOTA_MECHANISM_TEARDOWN, R2_NASTALIQ_FORENSICS, R3_OLCHIKI_MAYEK_SYNTHETIC, R4_OLDSCAN_RESTORATION, R6_COMPETITION_INTEL, R7_W6_TRAINING_TREE;
  - `level2/research/gates/B12_ensemble_voting.md` and `docs/campaign/MENTOR_PLAYBOOK.md`;
  - the Sep 10 sync transcript (`sync - ocr - September 10.docx`) and the Sep 29 meeting (`docs/research/MEETING_2026-09-29_STRUCTURED.md`, raw + structured).
- The queue below is seeded from that reading.
- [[proto-95-research-harvest-decisions]] appends every further ADOPTED finding that needs building (verdict ADOPTED + type BUILD) as B-18, B-19, and so on.
- Findings that only need a plan or document change land where proto-95 says.

**Rules:**
- A build item is done only when its gate metric exists on disk with the command that produced it.
- No item may train or tune on any benchmark split or test image (proto-89).
- Downloads need their U-row approved first.
- Sonnet subagents only.

## The queue (status on 2026-09-30: all OPEN unless stated)
| ID | Finding (source) | Build / change | Plan v3 day | Owner | Gate (done when) | Approval |
|---|---|---|---|---|---|---|
| **B-01** | **4-bit quantisation destroys Arabic-script OCR**: QARI (same 2B backbone class) CER 3.45 at 4-bit vs 0.091 at 8-bit (R2 §B6; R7 N3 "No 4-bit quant of recognizer") | Day 1 reports Bodhan 4-bit vs bf16 **per script, Perso-Arabic (ks/ur/sd) separately**. For ks/ur/sd blocks, inference AND the LoRA base use bf16 (or 8-bit), unless Day 1 shows 4-bit within 1 CER point on those scripts | 1 → 3 | Engine; Verdict checks | per-script precision table in `BODHAN_BASELINE.md` | none (U23 covers both builds) |
| **B-02** | **Up to 3–8 pts of the Kashmiri "failure" may be a scoring artifact**: without NFKC + yeh/kaf variants + digit forms + punctuation map + LRI/PDI bidi isolation (R2 §A5, R7 N4, UrduMMLU pipeline) | Check whether `level2/probe22/metrics.py` `--normalize` covers these. If not, add an opt-in `--normalize-arabic` in a NEW scorer module (never change the default; the locked files stay locked). Report raw AND normalized for ur/ks/sd in `BENCHMARK_22.md` (proto-62 tiers). Sarvam-bench numbers always use Sarvam's unchanged `metrics.py` | 1 | Verdict specifies, Engine builds | raw vs normalized table; no hidden rank inversion (AGENT_PROTOCOL §6.6) | none |
| **B-03** | **Kashmiri track** (the worst cell for everyone): QARI recipe 0.55→0.061 CER with 50k synthetic lines on a 2B VLM. Needs Kashmiri-capable fonts (Awami Nastaliq ≥3.300, Gulzar, Noto Nastaliq Urdu v4) + 300–500 real lines; SR + CLAHE + normalization first; greedy decode; no layout data in stage 1 (R2 §C; R6 §11.3 Koshur Pixel; U27 600K-KS-OCR approved) | Day 2: line-level ks synthetic set (OFL fonts only; Jameel Noori excluded until its licence is verified) (600K-KS-OCR is on HOLD — its card embeds a research-only licence, U27/RF-07). Real ks lines only if hand-verified (the ks PDF tier is BARRED at trust ~29, R7). Day 3: LoRA on the B-01 base. Cheap arm first: SR + CLAHE + normalization on Bodhan output | 2 → 3 | Engine; Verdict audits GT + leakage | ks CER on held-out real lines ≤ 0.20 (abort if > 0.30 after stage 2, R2 §C5) | U34 (fonts) |
| **B-04** | **Manipuri specialist exists**: NE-OCR (MWire Labs, CC-BY-4.0, 86M ViTSTR) reports 95.56% char-acc on Meitei Mayek where EasyOCR 2.50% / Tesseract 2.24% (R6 §11.3; verify the card before download) | Evaluate NE-OCR vs Bodhan on the 20 mni probe items (same GT tier). If NE-OCR wins, the Day-4 router sends Meetei-Mayek-script blocks to it (script from Bodhan's output text by Unicode range U+ABC0–ABFF; no image script classifier covers mni/sat — RF-09). Synthetic Mayek (Noto train / Eeyek val, RAQM mandatory, R3 §B) only if both fail | 1 → 4 | Engine | paired per-item CER table | U34 (NE-OCR) |
| **B-05** | **Santali: Bodhan already beats Sarvam** (68.30 vs 53.91); Ol Chiki has one OFL font (R3 §A2) | Accept Bodhan for sat, unless Day 1 shows charset errors on the 20 sat items. Only then run synthetic Ol Chiki (R3 §B, script-ratio gate ≥ 80%) | 1 | Engine | Day-1 sat row + charset-error count | U34 only if triggered |
| **B-06** | **Old scans are the field-wide worst column** (Sarvam OldScan 55.3; surya 42.8). The pre-registered ablation exists (R4 §C: A0 none / A1 deskew+Otsu / A2 deskew+Sauvola / A3 DocRes enhancement-head pilot n ≤ 8; adopt iff median ΔCER ≤ −0.03, CI excludes 0, on ≥ 2/3 engines, no dot regression, CPU ≤ 60 s/page) | Run it with Bodhan + 2 fallback engines frozen, on old-scan pages of OUR probe/South (never the test set) | 4 (if triggered) | Engine; Verdict pre-registers | R4 §C6 verdict row | U34 (DocRes weights, only if A3 runs) |
| **B-07** | **Frozen detector + per-block fallback** (R1 steal #3; R7 N6): Sarvam and Paddle both run layout → crop → VLM → reading-order merge | Day-4 routing runs every fallback engine on Bodhan's layout crops (same blocks), triggered by the deterministic bad-output check (proto-31 signals: empty · wrong-script share · invalid sequences · repetition loop · low log-prob) | 4 | Engine | fallback on/off CER per language (paired) | none |
| **B-08** | **Voting is not a text source** (B12: full ensemble beats all singles on 0/115 pages; ≥ 3-family agreement is 1.7× cleaner per character but covers ~5%) | REJECT ensemble text. ADOPT the agreement signal only as a per-block confidence / human-review triage flag | 4 | Engine | flag precision measured on the probe | none |
| **B-09** | **Weak-region mining** (R1 steal #1, PaddleOCR-VL §3): cluster documents, find sparse tail clusters | Embed probe + a test-profile sample, cluster, list tail clusters. Output: what Day 2/3 data should cover; no training | 2 (optional) | Engine | tail-cluster list with sizes | none |
| **B-10** | **RL only after SFT, with validity-gated rewards** (R1 §4.3.2; R7 N4): reward = Valid × Struct × Sim; degeneration/truncation/repetition → 0; rollouts only on human-verified gold; NFKC/bidi before reward on ur/ks/sd | Wording lands in proto-89 §C's RL clause; nothing runs unless SFT passes Gate 3 | 3+ | Engine | — | training = W6 decision |
| **B-11** | **The jury scores a product, and no accuracy metric is published** (R6 §1–§5, VERIFIED from the official Bhashini page snapshot 2026-09-26): innovation · business use case · technical feasibility (stack, interoperability) · product roadmap (cost, go-to-market) · team · addressable market. Named outputs: layout-preserving JSON, searchable PDF, language detection, transliteration, context-based correction; "deployment-ready", Bhashini-stack compatible | Day 4–5 builds: (a) output JSON schema — page meta + blocks (type, bbox, reading order, language, script, text, handwritten flag, confidence), reusing the boss's Sep 10 layer design; (b) searchable-PDF writer (page image + invisible text layer, PyMuPDF); (c) per-block language detection (RQ-8 becomes REQUIRED); (d) offline package with vendored weights + Bodhan attribution; (e) throughput and cost numbers for 5,344 pages; (f) pitch deck (business case, roadmap, market), drafted by Miss with the boss/Vinay | 4 → 5 | Engine (a–e), Miss (f) | a 50-image dry run emits JSON + PDF + language tags | U35 |
| **B-12** | **Handwriting is in the official eval scope** (R6 §3: full-page handwritten, cursive, mixed typed+handwritten) | Attach this to U13. Day 1 records Bodhan's handwriting languages (RQ-3); RQ-2 measures the handwriting share of the 5,344 test images. If material: handwriting fallback plan (RQ-10) | 1 → 4 | Engine / Verdict | handwriting share + Bodhan HW coverage table | U13 |
| **B-13** | **The "refinement layer" Vinay asked for** (Sep 10: add tokenizer / refinement / semantic layers where the VLM lags) + "context-based correction" named officially (R6) + synthetic-trained correctors −55% to −69% CER (R3 §C1 #4–5) | Post-OCR corrector (ByT5-class, trained on synthetic corruptions of OUR training text only) | after Day 5 (stretch) | Engine | paired CER on held-out docs | training = W6 decision |
| **B-14** | **The Sep 10 labelling pipeline** (free-tier VLM APIs label layout + text; one page = one sample; language-wise paragraph boxes; 100/lang) | Ruling for MENTOR_PLAYBOOK (T8) + RESEARCH_DECISIONS: layout labelling SUPERSEDED (Bodhan's IndicDocLayout gives layout); LLM labels REJECTED as ground truth (unverified GT; B12 shows consensus ≠ truth); KEEP the principles: page = sample, own benchmark on own data, lab-style records | now | Verdict | ruling rows written | none |
| **B-15** | **"Maintain proper records like a lab"** (Sep 10: data vs working_experiments, named experiments, sample tracking) | Every run gets one experiment home (inputs + hashes, config, outputs, metrics) plus one registry row (id · question · data · result · verdict). Proto-70 Phase 1 decides the path inside the level2 target tree | 1 onward | Miss (structure), Engine (per run) | registry lists every run since Day 1 | none |
| **B-16** | **Vinay's first method step: "how to train an OCR" as a flowchart** (Sep 29, method step c); the only flowchart is MENTOR_PLAYBOOK §2 (old recipe) | `docs/PLAN.md` (proto-98 T1) opens with a Plan v3 flowchart (data → layout → recogniser → fallback → outputs → eval), each node coloured BUILT / SPEC / PAUSED from disk | Phase 3 of proto-98 | Miss writer, Verdict checks | flowchart present, every node's status backed by a file | none |
| **B-17** | **Vinay's gates before execution** (Sep 29 D4 + D5; red line "No training before research validation"): multi-LLM evaluation of the plan, judged "by the process", then a 15–20 min cross-question session on a DRAFT plan. Done for the Plan v2 draft (MULTI_LLM_EVAL.md), **not for Plan v3** | Gate 2.5 in proto-89: run the proto-17 method on `docs/PLAN.md` (OpenCode + a fresh Sonnet reviewer + a ChatGPT paste), then the boss holds the D5 session with Vinay. No Day-3 training before both | before Day 3 | Verdict (eval), the boss (session) | eval report + session outcome recorded as U-rows | boss |
| **B-18** | **Post-correction on Bodhan's own errors** (proto-104 R-rulings; Consensus Q2) | A small text-level corrector trained only on Bodhan's train-split error pairs; never on bench items | after D1 | Engine (runs), Verdict (leak check) | Word Accuracy gain on a held-out split, 0 bench overlap | boss (GPU) |
| **B-19** | **Handwriting LoRA** (RQ-10 TRIGGERED; test set = handwritten words, F73/F74) | LoRA on the recogniser with IIIT-HW-format data (Bodo/gu on disk) + any licensed handwriting set; word-crop input | after H1 + Gate 2.5 | Engine, Verdict | handwriting split score vs zero-shot | boss (GPU, data licence) |
| **B-20** | **Legacy-font → Unicode South GT** (F75: 76% of South PDFs are legacy encodings) | Font-map converters to recover South official GT; only then compare against Sarvam-bench South | parked until S6 | Miss | ≥1 language converted with spot-check CER | none |
| **B-21** | **Synthetic lines (GlotOCR-style)** | Render licensed Unicode text in many fonts/degradations for low-resource scripts (ks, sat, mni) | before D3 | Miss (builder), Verdict | synthetic set card + no bench text reused | boss |

## Order
1. **Now:** B-01, B-02, B-12 run inside Day 1; B-14 is a Verdict write-up.
2. **Day 2:** B-03 data, B-09, B-15.
3. **Before Day 3:** B-17.
4. **Day 3:** B-03 training, B-10.
5. **Day 4:** B-04 routing, B-06, B-07, B-08, B-11 (a–e).
6. **Day 5:** B-11 (f), B-16 refreshed.
7. **Stretch:** B-13.

**Done when** every row has its gate artifact on disk or a written REJECTED/DEFERRED verdict with the reason, and `docs/PLAN.md` lists the adopted items in its build table.

Related: [[proto-89-plan-v3-bodhan-base]], [[proto-95-research-harvest-decisions]], [[proto-97-research-still-to-do]], [[proto-98-clean-repo-master]], [[proto-31-w3-laya-jev-verdict]], [[proto-92-boss-decisions]]
