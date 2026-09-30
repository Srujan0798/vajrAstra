---
name: proto-97-research-still-to-do
description: "Added 2026-09-30 — the research still missing, as 11 questions RQ-1…RQ-11, each tied to the decision it changes (U2/U13/U14/U28, Plan v3 days, Gate 1): hackathon rules, test-set profile, Bodhan operating details, Kashmiri, Santali/Manipuri, degraded scans, Sarvam-bench parity, language ID (not Laya), licences, handwriting data, oracle gap; harvest-first rule, owners, done-when; answers land in RESEARCH_DECISIONS.md, never in new essays"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T10:08:18.403Z
---

# PROTO-97 — RESEARCH STILL TO DO (W4 part 3): only questions whose answer changes a decision

**Boss, 2026-09-30:** "we have done a huge research and also some more to do". This file is the "more to do". It stays short on purpose: every item must move a decision. Concern H2 in [[proto-99-concern-crosswalk]] §H.

## Rules
1. **Harvest first.** Before any live search, grep for the question in:
   - `docs/campaign/RESEARCH_DECISIONS.md` ([[proto-95-research-harvest-decisions]])
   - `_archive/INDEX.md`
   - the G3/G5 ledgers

   If the answer is already on disk, it is a harvest row, not new research.
2. **Open every source.** Snippets don't count. Date and quote each source. Search `standard` first; use `extended` only when results are thin. Run `factchk` on every claim before it lands.
3. **Answers land in `RESEARCH_DECISIONS.md`** (new RF rows with a verdict) and in the decision or protocol they change. Never write a new standalone md essay (AGENTS.md law).
4. **Unanswerable after an honest try = UNKNOWN**, plus what was tried. Never infer rules from student repos or blogs (F43).
5. **Sonnet subagents only**, at most 5 in parallel. Downloads, Sarvam calls and training need the boss.

## The questions

### RQ-1 — Official hackathon rules
- **Question:** metric; submission format (files or hosted API); deadline; which external models and data are allowed; test-set description.
- **Changes:** U2 (deadline), U28 (Bodhan written approval if hosted), proto-80, proto-78.
- **Read first:** R6_COMPETITION_INTEL.md; `level7/c/c2/LEDGER.md`; `INTEGRATION_REPORT.md:146` ("2026-10-15 qualifier"); feed §15/16 "Oct 4 (Sat)" (Oct 4 2026 is a Sunday); READMEs in `Datasets/akshardrishti_official/` (sealed: read only).
- **Method:** official Bhashini / AksharDrishti pages, plus organiser mails or PDFs the boss holds (ask once, batched).
- **Owner:** Miss (Lane C), with Verdict factchk. On 2026-09-30 the boss gave RQ-1 and RQ-9 to the Verdict session (`ses_f1233a0a…`); the lane owners are in NEXT.md.
- **Done when:** each item has a URL + quote, or UNKNOWN; U2 and U28 are updated for the boss.

### RQ-2 — Test-set profile of the 5,344 unlabelled JPEGs in `test/test/`
- **Question:** script mix, printed vs handwritten share, degraded share, page vs crop, resolution.
- **Changes:** U13 (handwriting scope), RQ-6, Day-4 routing, the time budget (s/page × 5,344).
- **Read first:** proto-81, proto-78.
- **Method (local only):**
  - image size and DPI from metadata for all 5,344;
  - a seeded random 300, viewed by a Sonnet subagent and labelled for script, printed/handwritten, degraded, table;
  - later, block counts from the Bodhan layout model.
  - Limits: coarse stats only, no per-image tuning, never used for training. Record in W4.md that we looked, and why (mandela pattern 5).
- **Owner:** Engine.
- **Done when:** a profile table exists in proto-81's output, and U13 is answered with numbers.

### RQ-3 — Bodhan operating details
- **Question:** is a language hint needed; which 12 languages handwriting covers; block input spec; max tokens; reading-order output; page throughput on this Mac (layout + recogniser); MLX 4-bit vs bf16 parity.
- **Changes:** Day 1, Day 4, RQ-8.
- **Read first:** proto-89 §A; proto-94 #1–2.
- **Method:** the HF card for `bodhan-ai/indic-ocr` and its code; the `hari31416/indic-ocr-mlx-4bit` README; measurements taken during Day 1.
- **Owner:** Engine (inside Day 1).
- **Done when:** the answers are in BODHAN_BASELINE.md, with rows in RESEARCH_DECISIONS.

### RQ-4 — Kashmiri (Nastaliq), the worst cell: Bodhan 48.04, Sarvam 54.82
- **Question:** why the cell fails (R2). Can 600K-KS-OCR word images (256×64) train a block recogniser? What are the alternatives: line-level synthetic rendering with Nastaliq fonts, or Urdu/Kashmiri OCR models?
- **Changes:** the Day 3 target list.
- **Read first:** R2_NASTALIQ_FORENSICS.md; proto-94 #6; the 600K-KS-OCR paper.
- **Method:** the paper and data card; a 50-item smoke test after the approved download (U27).
- **Owner:** Engine.
- **Done when:** go/no-go for a Kashmiri adapter, with a data plan.

### RQ-5 — Santali (Ol Chiki) and Manipuri (Meetei Mayek)
- **Question:** invest, or accept Bodhan as it is? Bodhan leads Sarvam on sat (68.30 vs 53.91) and trails on mni (82.85 vs 85.12). Our probe holds only 20 items each.
- **Changes:** the invest-vs-accept decision per language.
- **Read first:** R3_OLCHIKI_MAYEK_SYNTHETIC.md; proto-65 (Ol Chiki injection defect).
- **Method:** Day 1 numbers plus R3.
- **Owner:** Engine.
- **Done when:** a one-line decision per language, with numbers.

### RQ-6 — Degraded and old scans
- **Question:** does a restoration pre-pass (R4) help Bodhan? Run this **only if RQ-2 shows ≥ 10% degraded pages**.
- **Changes:** the Day 4 pre-pass.
- **Read first:** R4_OLDSCAN_RESTORATION.md.
- **Method:** A/B on the degraded subset of **our probe** (not the test set).
- **Owner:** Engine.
- **Done when:** a CER delta with a CI, or "not triggered".

### RQ-7 — Sarvam-bench scoring parity
- **Question:** the word-accuracy definition and normalisation in `metrics.py`; macro over 22 excluding English; whether 87.39/84.94 are on test or small_representative; the sample count (6,609 and 6,909 both appear in our files).
- **Changes:** Gate 1 comparability.
- **Read first:** COMPETITOR_INTEL §0.2; the proto-93 rows.
- **Method:** the dataset card, the blog page and the `metrics.py` source.
- **Owner:** Verdict (factchk), before BODHAN_BASELINE.md is written.
- **Done when:** one cited answer per item, and proto-93 is corrected.

### RQ-8 — Language ID
- **Question:** only needed if RQ-1 says the submission needs a language per image, or RQ-3 says Bodhan needs a hint. If needed:
  - exact script from Unicode ranges;
  - a proper LID for same-script languages (Devanagari: hi/mr/sa/ne/mai/kok/doi/brx; Bengali-Assamese: bn/as/mni), i.e. IndicLID (AI4Bharat) or GlotLID;
  - **not Laya** ([[proto-31-w3-laya-jev-verdict]]).
- **Changes:** Day 4.
- **Read first:** proto-78 (script ID).
- **Method:** model cards and licences; an eval on probe outputs (any download needs the boss).
- **Owner:** Engine.
- **Done when:** triggered or not; if triggered, accuracy per language.

### RQ-9 — Licences still open
- **Question:**
  - indic-ocr tessdata for Ol Chiki / Meetei (no stated licence);
  - SynthOCR-Gen;
  - fallback engines under the real submission format (surya's $5M cap, U14);
  - the Bodhan attribution text in outputs.
- **Changes:** U14, U28, proto-83.
- **Read first:** proto-83.
- **Method:** repo LICENSE files and model cards, quoted.
- **Owner:** Verdict.
- **Done when:** a licence table with quotes.

### RQ-10 — Handwriting training data (only if U13 = yes)
- **Question:** which Indic handwriting sets have a licence that allows training (e.g. IIIT-INDIC-HW-WORDS; check it)? Compare against Bodhan's HW score of 66.7.
- **Changes:** the U13 follow-up.
- **Read first:** proto-81.
- **Method:** cards and licences.
- **Owner:** Engine.
- **Done when:** a list with licences, or "not triggered".

### RQ-11 — Oracle gap on probe22 (moved here from proto-31)
- **Question:** per language, how much lower is the mean CER of the per-item best local engine than that of the per-language best engine? Compute it on `sheet.csv` after proto-61's provenance verdict.
- **Changes:** the Day-4 routing and fallback gate. If the gap is < 0.02 everywhere, no router or gate is worth building.
- **Read first:** proto-61, proto-31.
- **Method:** a script over sheet.csv, reported per GT tier (proto-62).
- **Owner:** Engine.
- **Done when:** a per-language table in RESEARCH_DECISIONS, and the Day-4 plan updated.

### RQ-12 — Consensus.app: 3 combined queries (the lead's L2; boss 2026-09-30 ~18:15: "only 3 chances a day… mix and make ultimate and give 3")
- The 22 single-topic queries are merged into 3 one-line queries; all 22 are covered (map below). Paste each as-is; turn Deep Search on if offered; no year filter.
- FLAG (unconfirmed): third-party reviews (toolsforhumans.ai, costbench.com, 2026) say the free plan has unlimited normal searches and 3 Deep Searches per MONTH; the official pricing page did not render. The boss's own counter decides.
- **Q1 — the model** (old #1–5, #21, #22 → proto-89 Day 3 recipe, B-01, B-13):
  `How do LoRA/QLoRA fine-tuning of small (about 1B-parameter) vision-language OCR models, synthetic rendered text versus real scanned pages, hard-example mining, reinforcement learning with verifiable rewards (GRPO), and 4-bit or 8-bit quantization affect character error rate for low-resource Indic and Arabic-script languages, how much labelled data per script is needed, and how do such models compare with state-of-the-art multilingual OCR systems from 2024 to 2026?`
- **Q2 — the hardest cases** (old #6–12 → B-03/B-04/B-05, B-06, B-12, U13):
  `Which OCR methods report the lowest character error rates on the hardest Indian document cases (Urdu and Kashmiri Nastaliq, Santali Ol Chiki, Manipuri Meitei Mayek and Odia scripts, handwritten Indic text, tables and forms in government documents, and old or degraded scans), and what is the measured effect of image restoration or enhancement before OCR on recognition accuracy?`
- **Q3 — the system and fair proof** (old #13–20 → B-07/B-08, RQ-8, B-11, Gate 1, Gate 2.5):
  `For multilingual Indian document OCR systems, what evidence exists on layout analysis and reading-order detection, combining several OCR engines by confidence versus the best single engine, language-model post-OCR correction, language identification among same-script languages (Hindi, Marathi, Sanskrit, Nepali; Bengali, Assamese), searchable PDF and structured JSON output, and fair evaluation (character error rate versus word accuracy, Unicode normalization, test-set contamination, and multiple LLMs as independent evaluators)?`
- **After each run (boss):** copy the whole answer + paper list into Agent 2 as `RQ-12 Q<n> result (Consensus, <date>): <paste>`.
- **Processing (Agent 2):** save verbatim to `docs/sources/consensus/<date>_Q<n>.md` (source capture, not an essay); open every paper relied on; one RESEARCH_DECISIONS row per finding that moves a decision (verdict + decision + URL + ≤15-word quote); build items → proto-100 B-rows; conflicts with measured facts (4-bit hurts Arabic script; voting 0/115) → CONTRADICTION rows. Next day's runs only for sub-questions that came back UNKNOWN/thin, written by Agent 2 as one-liners in W4.md.
- **Done when:** all three results are RESEARCH_DECISIONS rows.

**Order:**
1. RQ-7 and RQ-3, inside Day 1.
2. RQ-1, now (it gates U2 and U28).
3. RQ-2 (it gates U13, RQ-6 and RQ-10).
4. RQ-11, before Day 4.
5. RQ-4 and RQ-5, before Day 3.
6. The rest, only when triggered.

**Done when:** every RQ has a RESEARCH_DECISIONS row (an answer or UNKNOWN), and the decision it names is updated or sent to the boss as a U# row.

Related: [[proto-95-research-harvest-decisions]], [[proto-89-plan-v3-bodhan-base]], [[proto-92-boss-decisions]], [[proto-81-handwriting-degraded-coverage]], [[proto-83-licence-verification]]
