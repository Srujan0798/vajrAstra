# OCR PROJECT — AGENT MEMORY FEED / PROTOCOL
Paste this entire file into the agent (OpenCode / Cursor / Claude / ChatGPT project) as standing memory.
Do not ask the human to re-explain the meeting. If a fact is marked UNKNOWN, ask once, then store it.

Last updated: 2026-09-25 23:30 IST
Source: voice meeting + research pass the same night. Merged into SOUTH_CANON §P. Agent ingested 2026-09-25; do not re-ask the meeting.

---

## 1. WHAT THIS PROJECT IS

We are building an Indic OCR system. Final output is a trained / hybrid OCR that beats current engines on Indian-language documents.

This is not a literature-review project. Research exists only to choose the training recipe. After the recipe is frozen, we train.

We already got selected into the top five because of a training recipe + architecture. That recipe is ~1.5 months old (designed ~mid-August 2026). Every week the field moves. Before spending compute, we re-research and only then train.

---

## 2. WHAT HAS ALREADY HAPPENED (GROUND TRUTH)

Do not invent extra history.

DONE:
- An architecture PPT exists. It contains the full architecture the team already designed. Human said the PPT is the architecture, not a teaser.
- Free / existing OCR models were run on **South Indian languages only**.
- Those results were collected and stored. That is the current “benchmark.”
- A training-process flowchart was designed ~1.5 months ago and was considered good enough at that time.
- Meeting on 2026-09-25 locked the next process: research again → 22-language probe → hybrid plan vs PPT → 15–20 min human session → freeze → train.

NOT DONE:
- No new model has been trained in this phase.
- No 22-language probe sheet exists yet (schema is locked in `docs/probe/W3_PROBE_SCHEMA.md`; samples not drawn).
- Remaining 18 Eighth-Schedule languages have not been scored by this team.

RESOLVED (2026-09-25, this workspace — do not re-ask):
- Hackathon: BHASHINI AksharDrishti. Team: Vaultstack AI. Repo: https://github.com/Srujan0798/vajrAstra (code only).
- Architecture PPT: `/Users/srujansai/Desktop/South/AksharDrishti_Hackathon_Proposal final.pptx` (4 slides; full architecture). One-page dump: `docs/architecture/PPT_SPEC.md`.
- South result sheet (KEEP, do not rescore 400 unless adding Sarvam 2.1 / Bodhan on a subset):
  - `level2/reports/LEADERBOARD.md`
  - `level2/reports/CER_BY_SCRIPT.md`
  - `level2/reports/LANG_LEADERBOARD.md`
  - `level2/reports/CER_STAGE3B.json`
  - law: `level2/ULTIMATE_HYBRID_CONCERN.md`
- Document mix (South dump): 200-dpi old-scan govt/textbook/exam pages; printed + mixed-script; some Latin/Devanagari misfiled under te/ta; handwriting is in the *product* vision, thin in the South 400.
- Metrics in use: CER/WER vs PDF-layer GT (proxy, n=126 writer basis). Product also wants structured JSON / KV. Pass bar not frozen — W5.
- Compute / APIs: Level 3 paid keys NOT started. Sarvam Vision 2.1 is API. Bodhan Indic-OCR is open-weight (`bodhan-ai/indic-ocr`, Indic Open Model License). Freeze session decides paid runs.
- “For South” = for South Indian languages (te/ta/kn/ml). Not a person.

Probe size LOCK (user 2026-09-25): remaining 18 Eighth-Schedule languages = **20 samples each** (~5% of South 400; user also said remaining work should stay a small fraction of South). Not 400. Not 5. Twenty.

---

## 3. PEOPLE AND CADENCE

- Human lead: busy. Joins after next Wednesday (after 2026-10-01).
- Krishna: asked to support until then.
- Aryan: touch base; exams may not be over.
- Labor rule from lead: extra humans are not required for grunt work. AI is enough for execution. Humans are required only for (a) correct method, (b) correct architecture, (c) someone who understands what is actually going on.
- Mode: human walks a process → agent executes that process → short discussion → execute next layer. Do not skip to training.

---

## 4. HOW THIS TEAM APPROACHES A PROBLEM (STANDING METHOD)

Treat every hard problem like a math problem. Do not start from “build the best model.”

Step order is 1-2-3. The meeting was spoken in reverse. Never reverse it again.

1. HOW DO OTHER PEOPLE SOLVE THIS?
   Use Consensus.app (consensus.app) first. Ten free searches/day. Two or three good queries are enough to get the gist of the literature. Papers live on arXiv too; Consensus is the synthesis layer. Then read the actual papers / lab blogs of groups that are winning.

2. WHAT IS THE TRAINING PROCESS?
   Write a flowchart: start → data → preprocess → layout → script ID → recognize → post-correct → eval → iterate. Refresh this flowchart against papers newer than our last recipe.

3. WHAT BROKE THROUGH RECENTLY?
   New models, benches, labs, companies. If a better recipe appeared in the last 6 weeks, we switch. We do not protect the old PPT out of loyalty.

Then, and only then:
4. Hybrid integrations against OUR architecture (not a greenfield model unless the diff demands it).
5. Probe-benchmark existing engines on the languages we actually care about.
6. Multi-LLM audit of the PROCESS (OpenCode + Claude + ChatGPT as evaluators). Human accepts or rejects. Conviction comes from the process, not from the model that spoke.
7. Freeze recipe. Train.

Forbidden:
- “Just train the best OCR.”
- Inventing a novel backbone to look original.
- Trusting an LLM architecture proposal that does not map to a cited method AND a failure slice on our sheet.
- Training on the evaluation split.
- Expanding scope to 22-language full training sets before the probe exists.

Research tool the lead named: Consensus.app — AI academic search, citations tied to real papers, ~10 free searches/day.

---

## 5. LANGUAGE SCOPE

South Indian results already exist (reuse them). South 400-page scores stay. Do not rebuild South at 400.
Remaining 18 Eighth-Schedule languages: **20 samples each** (locked). Probe, not a paper-scale bench. Enough to see which engines fail where.

Languages:
Assamese, Bengali, Bodo, Dogri, Gujarati, Hindi, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Manipuri, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu, Urdu.

South set already scored: Tamil, Telugu, Kannada, Malayalam (400 pages, 10 engines). Do not rescore those unless the model list changed (add Sarvam 2.1 + Bodhan on a 20-page South subset).

Must add to the model list even if the old sheet omitted them:
- Sarvam Vision 2.1 (released 2026-09-24/25)
- Bodhan Indic-OCR (AI4Bharat / IITM, open-weight)

Known weak cells from public SOTA (do not skip):
- Santali, Kashmiri (~54% on Sarvam’s own bench for their best model)
- Old scans
- Handwritten Indic
- Tables / reading order / mixed script

---

## 6. WHAT THE FIELD LOOKS LIKE ON 2026-09-25 (DO NOT GO STALE BLIND)

Use this as the challenger against the PPT.

Default 2026 recipe (unless PPT already is this):
OCR-specialized VLM
+ layout / reading-order harness
+ script routing or script-aware MoE for the long tail
+ progressive SFT (word → line → block → page)
+ RLVR only after SFT plateaus
+ schema / key-value head only if the product is forms or ID docs

Evidence:
- Sarvam Vision 2.1 + Indic OCR Bench (6,909 blocks, 22 languages + EN). Overall 87.39 vs Bodhan 84.94 vs Gemini 3.6 Flash 79.35 vs Google Cloud Vision 71.76. Training disclosed: synthetic+real → SFT → RLVR. Harness = semantic layout parser + pointer reading-order around the VLM. Bench: https://huggingface.co/datasets/sarvamai/indic-ocr-bench
- ScriptMoE, arXiv:2609.24058, 21 Sep 2026. Shared encoder, top-2 script experts + shared expert. Lifts PP-OCRv5 end-to-end F1 65.71 → 80.89.
- Chitrapathak-2, Krutrim, arXiv:2602.16430. Fine-tuning Nanonets-OCR2-3B / Qwen2.5-VL beat LLaVA-from-scratch on accuracy and 3–6× latency. Parichay: 9 Indian govt document types, 89.8% exact match.
- Devanagari VLM stress-test, arXiv:2606.29213. English OCR quality does not predict Indic OCR. Real scans collapse models that look fine on synthetic text.
- Groups to watch: Sarvam, Bodhan/AI4Bharat/IITM, Krutrim, IIIT-H CVIT (Jawahar), Bhashini-IITJ IndicPhotoOCR, IIT Roorkee MoScNet (Modi script only if heritage is in scope), Paddle PP-OCRv5, Surya, olmOCR, Nanonets.

Challenger hybrid list (ranked). Pick one primary + at most one add-on.
1. Fine-tune or wrap Sarvam / Bodhan / Nanonets-OCR if we cannot beat them zero-shot on our domain.
2. Layout harness around the recognizer.
3. Script router + specialists for Santali, Kashmiri, Meitei, Urdu Nastaliq.
4. ScriptMoE decoder if we insist on one model for 10+ scripts.
5. Progressive curriculum if the PPT trains full pages from epoch 1.
6. RLVR after SFT saturates. Do not start there.
7. Schema head only for forms.

---

## 7. WORKSTREAMS — DO THESE, IN THIS ORDER

### W0. Intake
Get PPT + South result sheet. Dump PPT to a one-page text spec. Do not guess the old architecture.

### W1. Re-research (allowed now)
Consensus queries (3 is enough):
1. What training strategies work best for multilingual Indic OCR with vision-language models?
2. Does fine-tuning an existing OCR VLM outperform training a multilingual OCR model from scratch?
3. How should script identification and mixture-of-experts be used in multilingual document and scene OCR?

Output: flowchart (old vs new) + one-page “what changed since mid-August 2026.”

### W2. Architecture diff
Score every box of the PPT against Section 6.
Label each box: KEEP / REPLACE / HYBRID / DROP.
Do not redesign boxes that already match the default recipe.

### W3. 22-language probe bench (before any training)
5–10 real blocks per language.
Prefer: our domain pages if they exist; else slices of Sarvam Indic OCR Bench.
Keep existing South scores; add missing models (Sarvam 2.1, Bodhan) on those same South samples if possible.

Sheet columns:
image_id | language | script | print_or_hand | quality | has_table | mixed_script | gt | model | prediction | CER | WER | error_tag

Error tags: matra_order | conjunct | old_scan | handwriting | table | reading_order | hallucination | repetition | charset | other

### W4. Multi-LLM process audit
Only after W3 sheet exists.
Packet: PPT text spec + this file + probe sheet + 5 paper/blog abstracts (Sarvam 2.1, ScriptMoE, Chitrapathak-2, Devanagari stress-test, Bodhan).
Same four questions to OpenCode, Claude, ChatGPT:
1. Which PPT boxes are obsolete after Sep 2026?
2. Smallest change that should beat the current leader on OUR probe set?
3. Which languages need a specialist instead of more shared training?
4. What would make this plan fail?

Accept a suggestion only if it cites a method AND a failure slice on our sheet.

### W5. 15–20 min human session
Agenda:
- Confirm scope in one sentence (2 min)
- Challenger vs PPT box by box (8 min)
- Freeze probe model list + sample source (4 min)
- Freeze non-goals (2 min)
- Staffing (2 min)

### W6. Freeze recipe, then train
Training starts only after W5. Not before.

---

## 8. NON-GOALS UNTIL FREEZE

- Training runs
- Collecting full 22-language training corpora
- Hiring for labeling unless real in-domain pages are missing
- New backbone “to overlead existing architectures”
- Using LLM-as-architect instead of LLM-as-evaluator

---

## 9. AGENT BEHAVIOR RULES

- Process first. If the human says “research,” do not open a training script.
- Every claim about SOTA needs a paper, blog, or our own sheet. No vibes.
- Do not overwrite the existing PPT. Diff it.
- Do not drop South results. Extend them.
- Short answers. Load-bearing words only. No generic OCR tutorials.
- When blocked by UNKNOWN items in Section 2, ask for the file/path once, then continue with public benches.
- After each workstream, write what changed back into this memory file.
- PPT and South sheet are now in this workspace. Continue W1 + W3. Do not stall. Do not train.

---

## 10. ONE-SENTENCE STATE

We have South-language scores (`level2/reports/`) and the architecture PPT (`AksharDrishti_Hackathon_Proposal final.pptx`). We have not trained the new model. Next work is the Sep-2026 recipe refresh, a 20-sample×18-lang probe, a hybrid diff against the PPT, a short human freeze after Wednesday 2026-10-01, then training.

## 11. WORKSTREAM LOG (append, do not fork)

- 2026-09-25: Ingested feed into SOUTH_CANON §P. Docs hierarchy: `docs/INDEX.md`. Superseded history deleted (SPEC_100, interrogation, synth-leak archive, duplicate Sep-16 package). No training.
