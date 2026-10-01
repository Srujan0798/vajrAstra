# AksharDrishti by Vaultstack — Project Showcase

**For Vinay and anyone evaluating the project · 1 October 2026**

Every number here carries its source and the benchmark it was measured on. Numbers from different benchmarks are never compared directly.

## 1. In one minute

- **The real test is handwriting.** The official AksharDrishti test set we were given is **5,344 images, and every one we have inspected is a single handwritten Bengali word** (16 viewed across all ID ranges, 16/16).
- **Handwriting is where the big general models are weakest.** On Bodhan AI's own handwriting benchmark, Sarvam Vision scores **58.3** word accuracy on Bengali, Bodhan **71.3**, Gemini 3.1 Pro **74.8**.
- **Specialists do far better.** Specialised handwriting recognisers trained on the public, CC-BY-licensed IIIT-INDIC-HW-WORDS data reach **92–96% word recognition on Bengali**: ICDAR 2023 Indic handwriting competition, best result **96.10%** (PARSeq).
- **Our design is two experts under one router.**
  - A **Handwriting Expert** (PARSeq per script) targets the test the organisers gave us.
  - A **Page Expert** (Bodhan IndicOCR) handles printed and mixed documents. On our machine it reproduces its published Sarvam-benchmark score (≈ **86.4** vs 84.94 published) and beats surya on our human-checked pages (CER **0.40 vs 0.57**).
- **The product is portable, offline and free to run:** layout-preserving JSON, searchable PDF and per-block language detection — the outputs the hackathon's focus areas name.

## 2. What the hackathon actually rewards

**Official evaluation process (BHASHINI AksharDrishti page, read 30 Sep 2026):**

| Dimension | What the jury looks at |
|---|---|
| Approach towards problem solving | product idea, degree of innovation, simplicity, uniqueness and scalability, novelty |
| Technical feasibility | features, scalability, interoperability, enhancement, technology stack, futuristic orientation |
| Product roadmap | productization potential, cost to build, go-to-market, time to market |
| Team ability and culture | leadership, ability to present and market, growth potential |
| Addressable market | channel, deployment cost, customization cost, 4-year resource evaluation |

- **The only evaluation target named on the page:** "accuracy, layout detection, and multilingual text handling".
- **No metric and no deadline are published.**
- **Focus area 5 names our outputs:** "layout-preserving output formats (JSON, searchable PDF)" plus "automatic transliteration and language detection".

## 3. What we have built so far (all on disk, all reproducible)

| Stage | What was done | Result |
|---|---|---|
| Level 1 (Sep 9–14) | South-language labelling system (page JSON schema: meta, layout, transcript, provenance, quality tier) | 400 labelled pages; the schema now drives our product JSON |
| Level 2 (Sep 12–16) | 10 open-source OCR engines × 400 South pages | 4,000 output packs; honest ranking: surya and anuvaad statistically tied (median CER 0.43 / 0.48) |
| 22-language benchmark (Sep 25 – Oct 1) | official hackathon data for 18 languages (1,283 items) + 4 South languages (400 items) | 11 engines; ground-truth tiers, abstention rates, bootstrap confidence intervals |
| Research campaign | 3 Consensus deep searches (≈100 papers), ~50 decision records, competitor intelligence, licence audit | every claim tagged PRIMARY / MEASURED / UNKNOWN |
| Strongest open base | Bodhan IndicOCR run on our machine | ≈ 86.4 word accuracy on Sarvam's benchmark sample (1,173 items); CER 0.40 vs surya 0.57 on our 300 human-gold pages |
| Product layer | portable package: layout JSON + searchable PDF + CLI + Dockerfile | `product/` in the repo |
| The handwriting finding | official test set profiled; public training data and specialist results located | the plan in section 5 |

**Operating model:** one lead plus three AI agents under strict laws:
- disk truth only;
- every number reproducible by a command;
- no training on any test split;
- archive-never-delete.

## 4. Where the field stands (three different benchmarks, never mixed)

**Printed — Sarvam's Indic OCR Bench** (word accuracy, 22 languages; built and run by Sarvam):

| System | Score |
|---|---|
| Sarvam Vision 2.1 | 87.39 |
| Bodhan IndicOCR | 84.94 |
| Gemini 3.6 Flash | 79.35 |
| Google Cloud Vision | 71.76 |
| Surya OCR 2 | 69.96 |

**Handwriting — Bodhan AI's IndicOCR-HW benchmark** (word accuracy; built and run by Bodhan):

| Language | Gemini 3.1 Pro | Bodhan | Sarvam Vision |
|---|---|---|---|
| Overall | 72.0 | 66.7 | 55.4 |
| **Bengali** | **74.8** | **71.3** | **58.3** |
| Hindi | 83.1 | 77.6 | 72.3 |
| Tamil | 80.5 | 76.8 | 60.5 |
| Telugu | 72.0 | 53.5 | 59.1 |
| Gujarati | 60.0 | 55.9 | 39.2 |

**Handwriting specialists — ICDAR 2023 Indic Handwriting Text Recognition** (word recognition rate; 5,000 test words per language from 100 new writers):

| Language | Best specialist | Organisers' baseline |
|---|---|---|
| **Bengali** | **96.10** (PARSeq) | 75.34 |
| Devanagari | 93.16 | 74.72 |
| Tamil | 98.08 | 88.48 |
| Malayalam | 97.16 | 77.20 |
| Kannada | 94.54 | 56.08 |
| Gujarati | 62.80 | 23.75 |

**What the tables show together:**
- General document models trail on handwriting.
- Specialists trained on in-domain handwriting are far stronger.
- No vendor benchmark is independent: each was built by the company that tops it. That is why our proof step uses evaluation sets none of us built.

## 5. Our plan (Plan v4) in one picture

1. **Quality gate:** restoration only for low-quality images.
2. **Router:** single word/line crop or full page? Handwritten or printed? Which script?
3. **Handwriting Expert:** PARSeq per script.
   - It starts from Bhashini/IIT-Jodhpur PARSeq checkpoints already on our machine (MIT).
   - It is fine-tuned on IIIT-INDIC-HW-WORDS (CC BY 4.0; Bengali: 82,554 training words).
   - That is the same recipe that won ICDAR 2023.
4. **Page Expert:** Bodhan layout model (blocks + reading order) + Bodhan recogniser, with light fine-tuning only where it trails.
5. **Fallback:** Tesseract with Indic models when an output is empty or in the wrong script.
6. **Post-correction:** a language-model corrector trained on our own errors (ships only if it measurably helps).
7. **Outputs:** layout-preserving JSON, searchable PDF, Markdown, per-block language; CLI, Python API and Docker image, offline.

**How it relates to the PPT architecture we presented:**
- **Kept:** every stage — preprocessing, layout, recognition fine-tuning, RL last, structured JSON.
- **Upgraded:** stage 1 now uses an Indic-trained layout model. Stage 2 adds a handwriting specialist, because measured evidence shows specialists beat general models on handwriting.

## 6. Why we expect to lead — and how we will prove it

- **Measured on our machine:**
  - Bodhan reproduces its published score (≈86.4 vs 84.94);
  - it beats surya on our human gold (CER 0.40 vs 0.57).
- **Published third-party evidence:** specialists reach 92–96% word recognition on Bengali handwriting (ICDAR 2023). The best general models reach 58–75 on vendor handwriting benchmarks.
- **Next proof (this week):**
  - fine-tune the Bengali handwriting expert;
  - report its word recognition on writers it has never seen;
  - score Bodhan, Sarvam and our system on the same independent sets.
- **Pre-registered targets:** ≥ 92% on the IIIT validation set and ≥ 85% on independent writers.
- **Leak control:** every official test image is hash-checked against every training set before training; overlaps are excluded and disclosed.

We do not claim certainty. We claim a measured advantage on the exact task the organisers set, with a proof step anyone can re-run.

## 7. Product and business

- **Outputs:** layout-preserving JSON (blocks, reading order, script, language, confidence, provenance), searchable PDF, Markdown — all named in the hackathon's focus areas.
- **Runs anywhere:** a PyTorch package and a Docker image for GPU or CPU servers. No per-page API fees. For comparison: Sarvam ₹0.5 per page; Bodhan API ₹0.20 per image.
- **Licences are clean for a product:**
  - Bodhan (Indic Open Model License, attribution; shipped as an internal component);
  - IIIT-INDIC-HW-WORDS (CC BY 4.0);
  - PARSeq (Apache-2.0);
  - Indic Tesseract models (Apache-2.0).
- **Roadmap:**
  - handwriting experts for the remaining scripts;
  - forms and tables;
  - transliteration;
  - active learning from user corrections;
  - a BHASHINI-compatible API.

## 8. Risks we track

| Risk | Control |
|---|---|
| Official test images overlap public training data | hash gate before training; exclude and disclose |
| Specialist does not generalise to new writers | headline numbers only on independent-writer sets |
| Gujarati handwriting is hard (best 62.80 at ICDAR 2023) | treated separately; no claim until measured |
| Bodhan errors on full pages (CER 0.69 on pages vs 0.054 on crops) | reading-order diagnosis first |
| Submission format not published | we produce per-image JSON + CSV + searchable PDF |

## 9. What we ask from you

1. **Your OK to start training** the handwriting expert, after you have seen this plan. We follow your rule: no training before the plan session.
2. **GPU access over SSH** for the PyTorch runs and faster training.
3. **Any detail you have on the submission format,** stage dates and how the test set was collected.

## Sources

- AksharDrishti official page, Evaluation Process and Problem Statement (bhashini.gov.in, read 30 Sep 2026).
- Sarvam Vision 2.1 blog (sarvam.ai, 24 Sep 2026).
- Bodhan IndicOCR model card (Hugging Face, bodhan-ai/indic-ocr), performance tables.
- ICDAR 2023 Competition on Indic Handwriting Text Recognition (Mondal and Jawahar, IIIT Hyderabad), Tables 1–2.
- IIIT-INDIC-HW-WORDS (CVIT, IIIT Hyderabad; IndiaAI AIKosh, CC BY 4.0).
- Our repo: 22-language benchmark tables, Bodhan baseline log, research decision register.
