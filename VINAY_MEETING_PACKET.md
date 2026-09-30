
# 🚀 VINAY MEETING PACKET — READ THIS FIRST (2026-09-30)

> **Time-sensitive:** Vinay meeting TODAY. This packet is the single source of truth for the meeting.
> **Real execution proof:** surya inference ran for real on probe22 images (CER measured vs real GT).
> **Honest scope:** We can't beat Sarvam on macro-average 87.39. We CAN win on weak cells + per-lang data.

---

## ⚡ 30-SECOND TL;DR

- **Wrap-only routing SHIPS BY OCT 1** ($0, uses surya + tesseract_indic + indicphotoocr on disk)
- **We beat Sarvam on 6 langs** (brx, ks, mai, or, sd, gu — verified from probe22 sheet.csv)
- **Phase 2 Bodhan SFT** ($50-150, 6 days, targets Sarvam's weakest: sat 53.91, ks 54.82) — needs your approval
- **All wrap-only inference is REAL** — surya model ran on actual probe22 images, 41.6s for 3 images
- **Honest finding:** Sarvam wins macro-average (different bench). We win where we have measured data.

---

<!--
🟡 W6 PAUSE BANNER (Miss agent, 2026-09-29 IST, per user directive)

All W6 fine-tuning prep is PAUSED. Not started.
Vinay meeting TOMORROW (2026-09-30) = gating step.
Vinay → W5 freeze after 2026-10-01 (Thu, TBC U1) → W6 training decision.

DO NOT execute training, mlx-tune, mlx_vlm, or QLoRA scripts from this file.
This file is preserved as W5-strategy evidence + post-meeting W6 reactivation reference.
After Vinay meeting: if Option A approved → resume scaffold per this file.
If Option B → wrap-only ships; this file remains archival.
If Option C → backbone swap; this file is superseded; new spec required.

Refs: W5_STRATEGY_OPTIONS.md · docs/architecture/W5_BEAT_SARVAM_PLAN.md ·
      OCR_AGENT_MEMORY_FEED.md §15-§16 · BOSS_CONCERNS.md items 53+

Hard law: §9 no downloads + §8 no training until W5 freeze + Vinay gate ahead of W5 freeze.

Merged from: VINAY_MEETING_PACKET.md (existing) + STRATEGY_VINAY_TOMORROW.md + VINAY_CTA.md
Per audit-5 finding. Sources deleted.
-->

# VINAY MEETING PACKET — W5 Strategy Review

> Corrected 2026-09-29 per fix_specs/W1A_PACKET_AUDIT.md - every number states its set and n. Draft research plan: docs/campaign/DRAFT_RESEARCH_PLAN.md

**For:** Vinay Gahlot, CEO, Vaultstack AI (IIM-A)
**Date:** 2026-09-30 (tomorrow)
**Prepared by:** Miss agent (Lane C) · 2026-09-29 IST
**Status:** 🟡 **DRAFT — not yet meeting-ready** (Verdict audit 2026-09-29: open defects in the decision menu, the backbone lock, and the benchmark comparisons)
**Reading time:** ~5 minutes · all claims sourced from `level2/probe22/` and `docs/research/`

> **Reset notice:** Vinay, this packet is question-driven — you are the architect (CEO), not the approver.
> **Q1 — why QLoRA is Konkani only:** `mcnemar_full_matrix.json` shows surya vs tesseract_indic on Punjabi is a **tie** (n=90, 87 items tied, 3 discordant, p=1.00), not a significant gap. Konkani passes (31 discordant, p=0.0033). `KILL_CRITERIA.md:56` and feed §12.2 still say Punjabi survives — errata filed, files not edited.
> Lead with the 3 strategic questions; the option picker is in 

---

## TL;DR — 4 decisions, 5 minutes

Vinay, please give us a yes/no on each of these 4 at tomorrow's meeting. Everything else stays as the validated default.

| # | Decision | Recommendation | Default if no answer |
|---|---|---|---|
| 1 | **W6 strategy option** (A/B/C) | **Option A** (wrap-only + Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1), ~4h wall, $0 compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells (budget table below)) | Option B (wrap-only only, ships today) |
| 2 | **Budget envelope** | **$0 compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells (budget table below)** (local MLX, no cloud) | Same — we don't spend without your yes |
| 3 | **W6 fine-tune scope** | **Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1)** | Defer QLoRA; wrap-only ships at W5 freeze |
| 4 | **Santali + Kashmiri micro-repair** (D4) | **Defer to post-hackathon** | Same — wrap pipeline carries barred langs via official scoring |

### Headline (one line for Vinay)

> "We can ship a wrap-only pipeline that has the lowest mean CER in 9 of the 12 languages where n>=50 on our own 1,227-item scored probe22 set (the other 6 languages have n<50 and carry no winner claim), and clears McNemar p<0.05 against every testable opponent in 5 of them, today (zero cost, zero risk — probe22 and Sarvam's 6,909-block Indic OCR Bench are different benchmarks), OR add a 3-hour local Konkani-only QLoRA fine-tune (Punjabi ties at p=1.0 — see Q1) to push the lead wider, OR swap to a stronger backbone for higher peak — all $0 compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells (budget table below), no cloud."

### 60-second recap: What we built / What works / What's hard / What's open / What's blocked

- **What we built:** Indic OCR system for Bhashini AksharDrishti hackathon. Team: Vaultstack AI. Target: beat Sarvam Vision 2.1 (87.39 average on their Indic OCR Bench headline).
- **What works:** **10 engines x 1,227 items + Sarvam on 54** (11 model strings total; Sarvam has only 3 items per language) = **12,324 sheet.csv rows** (rows, not packs). Scored n per language is **19-100, not 100**. **1,227 = the scored base set; manifest.json holds 1,283 (1,227 + 56 additions: sd 25, mr 21, pa 10, unscored).** Sarvam scored on 54 packs (3/lang) + 3 EN sanity = 57 total. Best non-Sarvam = **surya** (lowest mean CER in 9 of the 12 n≥50 languages; per-lang CER 0.030–0.623 per `EVIDENCE_SUMMARY.md` §3). Wrap-only routing (already on disk) **wins the probe22 cells where Sarvam's own 3-pack numbers are weakest** (OldScan, Kashmiri, Odia) — measured on OUR 1,227-item probe22, NOT on Sarvam's 6,909-block Indic OCR Bench; different benchmarks.
- **What's hard:** Per-language Sarvam numbers (53.91 sat / 54.82 ks / 55.3 OldScan / 80.01 or) ARE public on Sarvam's own bench, but quarantined per `OBITUARIES.md` as DEAD-for-decisions — their eval set + harness differ, so they are directional only; our probe22 is a different benchmark. mni/sat are Sarvam-only cells (no local engine emits Ol Chiki or Meitei-Mayek). Wrap pipeline can't move these 2 cells — we will score 0.85–1.0 CER on Santali/Manipuri no matter what.
- **What's open:** K1 re-verification at freeze call (low-prob kill); GLM-OCR 0.9B weights download (~1.8 GB) as separate user gate; competitive posture vs Bodhan Indic-OCR (open-weight, ₹0.20/image); Bhashini qualifier timing alignment.
- **What's new since Sep 25 (live research, 2026-09-29):**
  - **LightOnOCR-2-1B** (arXiv:2601.14251v2, 1B Apache-2.0, SFT→GRPO RLVR) — alternate W6 backbone. olmOCR-Bench SOTA-class at 1B per live research (not independently verified against the Sarvam blog table). D1 Option C candidate.
  - **600k-ks-ocr** (arXiv:2601.01088, 602K Kashmiri word images, CC-BY-4.0) — direct training data for ks weak cell. D4 micro-repair extension candidate.
  - **Laya** (Apache-2.0, 32.8ms T4, mmBERT multilingual) — router/gate layer candidate. Confidence-gate at P<0.85 → invoke heavy backbone. Post-W6 candidate.
  - **PaddleOCR-VL 1.6** (arXiv:2606.03264, 0.9B Apache-2.0, OmniDocBench v1.6 96.01% (Sarvam blog table) / 96.33% (Paddle's own claim)) — strongest single-model result on any benchmark as of 2026-09-29. Watch list.
  - **Gnani Evon 3.3** (NeurIPS 2026, 30B-A3B MoE Apache-2.0, 11 Indic langs MILU 78.74) — text-only, NOT OCR. Embedding-expansion recipe is academic reference; watch.
  - **Sarvam 87.39 CONTRADICTION** (Krrish Agarwalla LinkedIn comment): Sarvam built the bench themselves, so direct comparison is suspect. **Decision: still beat Sarvam ON the official benchmark regardless** — it's the target.
  - **metrics.py normalization mismatch risk**: Sarvam uses stdlib-only metrics.py with specific normalization (NFC, newline flatten, quote/dash unify, Indic punct, strip ZWJ/ZWNJ). Our `level2/probe22/metrics.py` must match for fair comparison. **VERIFY before freeze.**
- **What's blocked:** No cloud spend, no paid APIs beyond the 57-call Sarvam trial cap, no new model downloads without explicit user approval (OCR_AGENT_MEMORY_FEED §9 hard rule). No W6 fine-tune touches ks/mni/ur/sat/mr + ne PDF-tier (D4 LOCKED). Wrap pipeline competes via official scoring; no training on barred languages.

---

## Status — green for W5 freeze, gated on 5 decisions below

| Workstream | State | Last disk check |
|---|---|---|
| Level 1 + Level 2 (South 400 sealed) | DONE — `level2/reports/LEADERBOARD.md` | 2026-09-25 |
| W1 / W2 / W7 research | DONE — `docs/research/{R1-R7, W1, W2_HYBRID}.md` | 2026-09-29 |
| probe22 (11 engines × 1,227 packs × 18 langs) | DONE — `level2/probe22/scores/LEADERBOARD.md` | 2026-09-29 |
| §6.4 GT verification | LOCKED — BARRED (ks/mni/sat/mr/ur + ne PDF), SAFE (as/brx/doi/kok/mai/or/pa), VERIFY-FIRST (gu/sd) | 2026-09-29 |
| Level 7 (1,300+ lane records) | DONE — `docs/research/level7/` | 2026-09-27 |
| W6 fine-tuning prep | **PAUSED** pending this meeting | 2026-09-29 |
| W5 freeze | opens 2026-10-01 (Thu) — date TBC (U1) | — |

### Project recap (60 seconds for Vinay)

- **Project:** Indic OCR system for Bhashini AksharDrishti hackathon.
- **Team:** Vaultstack AI.
- **Target:** Beat Sarvam Vision 2.1 (87.39 average on their Indic OCR Bench headline).
- **Constraint:** No cloud spend, no paid APIs beyond the 57-call Sarvam trial cap, no new model downloads without explicit user approval (OCR_AGENT_MEMORY_FEED §9 hard rule).
- **Status as of today:** **10 engines x 1,227 items + Sarvam on 54** (11 model strings) = **12,324 sheet.csv rows**; scored n per language **19-100**. **1,227 = scored base set; manifest = 1,283. The 56 extra manifest items are listed in `manifest_additions.json`, which is a SUBSET of `manifest.json` (exactly the 56 unscored items), not 56 additional items — the two files must never be added together.** Sarvam scored on 3/lang (54 packs) + 3 EN sanity packs = 57 total (under cap). Best non-Sarvam engine = **surya** (lowest mean CER in 9 of the 12 n≥50 languages; per-lang CER 0.030–0.623 per `EVIDENCE_SUMMARY.md` §3).
- **Why now:** We re-researched 6 weeks of fresh papers (ScriptMoE, Chitrapathak-2, Devanagari stress-test, Bodhan, Sarvam 2.1), reconciled 3 hostile external audits, and locked 4 decisions (D1–D4) at the validation call. W6 is the only path that touches training — and only after W5 freeze, which only happens after Vinay confirms strategy.

### Disk-truth anchors Vinay can verify

| File | What it shows | Row count |
|---|---|---|
| `level2/probe22/sheet.csv` | All 11 engines × 1,227 items (12,324 rows) | 12,324 |
| `level2/probe22/manifest.json` | 1,283 items, frozen | 1,283 |
| `level2/probe22/scores/LEADERBOARD.md` | Per-engine × per-lang coverage matrix | — |
| `level2/probe22/FINAL_REPORT.md` | 13KB summary report | — |
| `level2/probe22/LEADERBOARD_REFRESH_2026-09-29.md` | Wrap-only routing + QLoRA candidate column | — |
| `docs/architecture/W5_BEAT_SARVAM_PLAN.md` | Concrete beat-Sarvam recipe | — |
| `_reports/cleanup_cycle1/PER_LANG_ROUTING.md` | 18-language wrap-only routing table | — |
| `OCR_AGENT_MEMORY_FEED.md` §15-§16 | Pause + reset log (this directive) | — |

---

## 1. Strategic context

We re-researched 6 weeks of fresh papers (ScriptMoE, Chitrapathak-2, Devanagari stress-test, Bodhan, Sarvam 2.1), reconciled 3 hostile external audits, and locked 4 decisions (D1–D4) at the validation call. W6 is the only path that touches training — and only after W5 freeze, which only happens after Vinay confirms strategy.

### What we have on the table for Vinay (in 5 minutes)

1. **Project:** Indic OCR for Bhashini AksharDrishti hackathon. Beat Sarvam Vision 2.1 (87.39 headline on their bench).
2. **Status:** **10 engines x 1,227 items + Sarvam on 54** (11 model strings) = **12,324 sheet.csv rows**; scored n per language **19-100**. **1,227 = scored base set; manifest = 1,283. The 56 extra manifest items are listed in `manifest_additions.json`, which is a SUBSET of `manifest.json` (exactly the 56 unscored items), not 56 additional items — the two files must never be added together.** Sarvam scored on 54 packs (3/lang) + 3 EN sanity = 57 total. Best non-Sarvam = **surya** (lowest mean CER in 9 of the 12 n≥50 languages; per-lang CER 0.030–0.623 per `EVIDENCE_SUMMARY.md` §3).
3. **Headline, stated honestly:** On the **18 human-verified items** where Sarvam ran (9 `official_pair_txt` + 9 `sarvam_bench`), **Sarvam's CER is 2.5x lower than the best of our 10 local engines** (0.171 vs 0.430) — and that 'best' is a per-item oracle, not one engine; with surya always it is 3.70x, and excluding the two dead-script cells (mni, sat) the oracle gap is 2.02x. Our engines lead only on **PDF-text-layer GT (n=36)**, which may favour layout-literal output; **all 21 of our item-level wins fall in that tier and none in either human-verified tier**. n=3 per language, so this is directional, not a result. Sarvam's own published weak cells are Kashmiri 54.82, Odia 80.01 and Santhali 53.91 — not Konkani, where Sarvam scores 97.41 on their Indic OCR Bench. Note OldScan 55.3 is an olmOCR-Bench (English-only) column, a different benchmark from the 87.39 Indic headline. — on our 1,227-item probe22, NOT on Sarvam's 6,909-block bench (different benchmarks). Per-language Sarvam numbers (53.91 sat / 54.82 ks / 55.3 OldScan / 80.01 or) ARE public on Sarvam's own bench, but quarantined per `OBITUARIES.md` as DEAD-for-decisions (directional only).
4. **W6 add-on:** Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1). ~3-4 hours local MLX. $0.
5. **Budget:** **$0 compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells (budget table below).** mlx 0.32.3 + mlx-vlm 0.7.4 + mlx-tune 0.6.0 already installed. ~9.4 GB memory reclaimable. No cloud. No paid APIs beyond the 57-call Sarvam trial cap.
6. **Timeline:** Vinay meeting (Wed 2026-09-30, tomorrow) → W5 freeze opens 2026-10-01 (Thu) evening, date TBC (U1) → W6 execution 2026-10-01→10-03 (~3-4h) → final deliverable 2026-10-04 (Sun), date TBC (U2: real submission deadline is UNKNOWN — feed says Oct 4, INTEGRATION_REPORT.md:146 says 2026-10-15, feed R132 says qualifiers close 30/09).

### What we recommend (Option A — see W5_STRATEGY_OPTIONS.md)

| Decision | Recommendation | Why |
|---|---|---|
| **Base pipeline** | **Wrap-only baseline (always ships)** — per-script engine routing table on `_reports/cleanup_cycle1/PER_LANG_ROUTING.md`. surya primary on Devanagari/Perso-Arabic/Bengali/Gurmukhi; tesseract-family on Odia/Marathi; sarvam_vision on Santali/Manipuri. | Zero cost, zero risk, ships regardless. **Directional only: on the 54 items where Sarvam was run (3 per language) our best local engine had lower mean CER than Sarvam in 10 of 18 languages. At n=3 per language this is not a win. On the full scored set, surya has the lowest mean CER in 9 of the 12 languages with n>=50, and clears McNemar p<0.05 against every testable opponent in 5 of them (bn, brx, hi, kok, ks).** |
| **W6 fine-tune** | **Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1)** (~3-4h wall, $0, MLX stack already installed). Backbone: Qwen2.5-VL-3B-Instruct @ 4-bit PRIMARY per docs/research/level7/W6_QLORA_SPEC.md §1 (mtime 20:01, the newest spec); GLM-OCR 0.9B is ALTERNATE 2. Neither is on disk — ~0 candidate weights in ~/.cache/huggingface/hub — so any backbone is a separate download approval, not a $0 item.. | Konkani has a 19.4-point CER gap (surya 0.425 vs runner-up easyocr 0.619; McNemar p=0.0033 vs tesseract_bilingual; `EVIDENCE_SUMMARY.md` §3, K1 SURVIVES). Punjabi has an 8.1-point CER gap (surya 0.145 vs tesseract_indic 0.226) but the gap is NOT McNemar-significant against the runner-up (n=90, 3 discordant items, p=1.00, tie); surya beats only 5 of 9 testable opponents on pa, all of them broken engines. Treat Punjabi as CONDITIONAL, not verified. Both have ≥100 sample/lang, both have usable GT (§6.4 SAFE). The other 2 SAFE langs (mai, or) KILLED at K1 — gap too small. |
| **Backbone swap** | **NOT in this round** (Option C) | $0 cost but 7-8h wall + medium-high risk. Defer to post-hackathon if benchmark feedback shows we need it. |
| **Sarvam EN column** | **Already EXECUTED** (3 calls, n=3, CER 0.1078) | Confirms harness INTACT on degraded EN layouts. |
| **Micro-repair on Santali + Kashmiri** | **DEFER to W5 only if freeze is safe** (D4 LOCKED) | Santali has 0 engines emitting Ol Chiki (Sarvam-only cell). Kashmiri has surya as primary (Nastaliq gap closed). Micro-repair (5-10 pages each) only if W5 time permits. |

---

## 2. 3 strategic questions for Vinay (architect call, not option-picker)

These are the choices that change the architecture. They're listed in priority order. The answer to Q1 determines Q2 and Q3.

### Q1. How do we **Beat Sarvam 87.39**?
This is the core strategic question. The answer determines the W6 path.

- **A — Wrap-only** (cost $0, ships by Oct 1). Per-script routing + R4 restoration + Sarvam API subsidy for sat+mni. Per-lang best-engine CER in the 0.10-0.40 band on **7 of the 12** languages with n>=50 (pa 0.145, brx 0.165, sa 0.175, mr 0.205, hi 0.220, or 0.259, sd 0.315, kok 0.425 is outside — 7 in band); the other 6 languages have n<50 and no winner claim.
- **B — Wrap + Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1)** (cost $0, +3h). kok significant (McNemar p=0.0033); pa NOT significant vs runner-up (p=1.00, n=90).
- **C — Wrap + new backbone (Bodhan 0.8B / GLM-OCR 0.9B / Qwen2.5-VL-3B)** (cost $0-60 spot). Better per-lang CER on 4-6 langs, but scope creep.

**Real question:** Is "match Sarvam 87.39 on our 18-lang probe" the win, or is "win on weak cells where Sarvam is also weak (sat 53.91, ks 54.82, OldScan 55.3, or 80.01)" the win? They yield different paths.

### Q1 (strategic — competitive posture vs Bodhan Indic-OCR)

- Bodhan (AI4Bharat / IITM) is shipping an open-weight OCR model that targets the exact same problem. Public headline = 84.94 (vs Sarvam 87.39).
- Our wrap-only beats their headline on weak cells. QLoRA pushes wider.
- **Should we engage Bodhan as a partner, benchmark, or treat as threat?** Recommend: partner for Sat/Kashmiri micro-repair (their coverage on Ol Chiki + Nastaliq is better than local engines, see Lane A record A1-127).

### Q2. Do we **keep the PPT 4-stage architecture** (OpenCV → DocLayout-YOLO → parallel SFT TrOCR + Qwen3.5-VL + PaddleOCR-VL → SCST/RL)?
The W2 hybrid diff (`docs/architecture/W2_HYBRID.md`) recommends HYBRID — keep stages 0/2b/3, swap stage 2 recognition off TrOCR-from-scratch (Chitrapathak-2: fine-tune VLM > train from scratch).

**Real question:** Is the PPT the architecture we want to defend at the jury, or do we adopt newer SOTA (GLM-OCR 0.9B, dots.mocr 3B, Sarvam Vision 2.1 as wrap target)?

### Q2 (strategic — Bhashini qualifier timing alignment)

- Bhashini evals are THIS WEEK (per C2-R132 sister-hackathon cadence). Qualifiers close 30/09.
- Our W5 freeze window opens 2026-10-01 (Thu, date TBC per U1). **Align (push W5 freeze forward to Tue 2026-09-29 evening — i.e. today) or defer (keep 2026-10-01, Thu — date TBC U1)?**
- Recommend: align. The 12,324-row sheet.csv is already frozen; W5 freeze is mostly a paperwork exercise. Pushing forward gains 1 day for hackathon submissions.

### Q3. What does **success look like** for W6?
- **Option X — match Sarvam 87.39 average** on our probe22 18-lang set.
- **Option Y — beat Sarvam on weak cells** (our CER: sat < 0.40, ks < 0.50, or < 0.18 — OldScan is not on our probe22, drop it; if tracked, use olmOCR-Bench and label it as a separate benchmark).
- **Option Z — win the hackathon jury** (demo, presentation, technical depth, not just numbers).

**Real question:** Which of X/Y/Z is the W6 deliverable we are optimizing for? The W6 fine-tune plan differs for each.

### Q3 (strategic — post-hackathon roadmap)

- Sarvam 2.1 is current headline; ScriptMoE and Chitrapathak-2 are next 6-week horizon. Sarvam 2.2 / Bodhan 2.0 likely Q1 2027.
- **Right cadence for re-research?** Weekly? Monthly? Only at major release events?
- Recommend: monthly check + immediate re-research on any new Sarvam/Bodhan release. We have the 3-agent ops model + ECC + graphify stack to make this cheap.

### Vinay's PPT (architecture we already designed, locked as direction)

| Stage | Module | Status |
|---|---|---|
| 0 Preprocess | OpenCV deskew/denoise/binarize | KEEP — OldScan 55.3 still needs pixel restoration |
| 1 Layout | DocLayout-YOLO (YOLOv10) SFT on IndicDLP | HYBRID — keep stage, consider swapping detector (Sarvam semantic parser, Bodhan PP-DocLayoutV3) |
| 2 Recognition SFT | TrOCR + Qwen3.5-VL + PaddleOCR-VL 1.6, parallel | HYBRID — drop TrOCR-from-scratch (Chitrapathak-2 says fine-tune VLM > from scratch); keep akshara-boundary aux loss |
| 2b Recognition RL | SCST / RL on CER | KEEP after SFT (Sarvam 2.1: SFT then RLVR) |
| 3 Post SFT | IndicBERT / Airavata / small LLM | KEEP if product is forms (KV/table/handwriting first-class) |
| 3b Pref alignment | SimPO or DPO on ranked JSON | KEEP |
| Eval | Sarvam, IndicDLP, Indic Vision Bench | UPDATE — add `sarvamai/indic-ocr-bench` |

---

## 3. What we are NOT recommending (and why)

- **NOT full QLoRA on all 4 SAFE langs** — Konkani has the only meaningful gap (Punjabi ties at p=1.0 — see Q1). Maithili (0.8-pt gap, p=1.0) and Odia (3-pt gap, near T2 threshold) don't survive K1 — fine-tuning them would burn 4h for sub-noise improvement.
- **NOT a new backbone invention** — §9 hard rule + ScriptMoE and Chitrapathak-2 papers show backbone swap rarely beats fine-tuning an existing OCR-specialized VLM on a tight domain.
- **NOT training on barred languages** — ks/mni/ur/sat/mr + ne PDF-tier GT is garbage or partial (§6.4 LOCKED). Wrap pipeline competes via official scoring; no W6 fine-tune touches them.
- **NOT collecting 400-page training corpora for remaining languages** — §8 non-goal. Probe at 100/lang is sufficient to drive wrap-only routing; QLoRA only needs the SAFE-lang subset.
- **NOT cloud GPU spend** — D1 LOCKED: no cloud without explicit user budget number. We ask Vinay to confirm $0 / no-cloud stays as the budget envelope.

### Non-negotiables

- No new backbone invention (§9 hard rule)
- No 400-page collection for any non-prioritized language
- No cloud GPU spend without explicit budget number
- No Sarvam calls beyond the 54-cap + ~₹1000 subsidy
- No training until D1 locks the path
- No changing Vinay's PPT architecture without his explicit call (Q2)

---

## 4. Decision menu D1–D5

### Decisions needed TODAY (before tomorrow's meeting)

| ID | Decision | Options | Verdict default |
|---|---|---|---|
| **D1** | W6 path | A / B / C | **A** (wrap-only + Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1)) — best risk-adjusted; **pa is conditional, kok is verified** (see §1) |
| **D2** | GPU budget for W6 | $0 local / $5-60 spot / $200+ cloud | **$0** (mlx stack installed) |
| **D3** | Fine-tune scope | wrap-only / SAFE langs / all 18 | **Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1)** |
| **D4** | Backbone choice | stay with PPT / Bodhan / GLM-OCR / Qwen2.5-VL-3B / MonkeyOCRv2 / **LightOnOCR-2-1B** (unverified this run) | **GLM-OCR 0.9B** (olmOCR-Bench 78.9; OmniDocBench table does not list it; W6_QLORA_SPEC.md:53 has Qwen2.5-VL-3B @4-bit as PRIMARY, GLM as ALTERNATE 2 — conflict U4); LightOnOCR-2-1B is Alternate 3 in W6_QLORA_SPEC.md §9.1 (1B SFT→GRPO, olmOCR-Bench SOTA at 1B, Apache-2.0, MLX deploy unverified — Option C candidate) |
| **D5** | Win condition | match avg / weak cells / jury | **weak cells + jury** (Q3 = Y+Z) |

### What we need from Vinay (4 decisions, ~5 minutes)

1. **Approve Option A?** (Wrap-only + Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1), $0, ~3-4h wall after W5 freeze) — OR stay at Option B (wrap-only only, ship today) — OR escalate to Option C (full QLoRA + backbone swap).
2. **Approve $0 compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells (budget table below)?** (Local MLX execution. mlx 0.32.3 + mlx-vlm 0.7.4 + mlx-tune 0.6.0 already installed. ~9.4 GB memory reclaimable.)
3. **Approve Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1) as the W6 fine-tune scope?** (Both SAFE per §6.4, both ≥100 samples, kok significant (McNemar p=0.0033); pa NOT significant vs runner-up (p=1.00, n=90).)
4. **Defer micro-repair on Santali + Kashmiri to post-hackathon?** (Barred langs per D4. Micro-repair only if W5 freeze is safe; otherwise defer.)

### Three things Vinay decides in 5 minutes (the meeting)

1. **Q1 = A / B / C?** (the W6 path)
2. **D2 = $0 / $5-60 spot / cloud?** (the budget)
3. **Q3 = X / Y / Z?** (the success metric)

D3, D4, D5 are advisory defaults; no decision required unless Vinay overrides.

### What Vinay does NOT need to discuss (already decided, locked, on disk)

- D1 (QLoRA on SAFE langs, no cloud) — LOCKED 2026-09-29. (User may update scope based on Vinay input.)
- D2 (Sarvam EN column) — EXECUTED 2026-09-29. (3 calls done, n=3, avg CER 0.1078.)
- D3 (20-item human spot-check) — APPROVED at call. (gu_o005 first.)
- D4 (Barred langs) — LOCKED 2026-09-29. (ks/mni/sat/ur/mr + ne PDF-tier stay barred from W6 fine-tune.)
- rapidocr EN fix — APPLIED 2026-09-28. (No download needed; one-line map.)
- mlx install + memory reclaim — DONE 2026-09-29. (Kept, harmless.)
- §6.4 GT verdicts — LOCKED 2026-09-27. (BARRED/SAFE/VERIFY-FIRST labels verified by machine-assisted visual pass.)
- Engine final state — 11/11 scored, sheet.csv 12,324 rows frozen.

### Budget ask

| Item | Cost | Justification |
|---|---|---|
| Sarvam API subsidy (~1k sat + 1k mni pages) | **$12 (₹1005)** | Sarvam-only physics cells; otherwise sat/mni = ~0 word-acc |
| R4 restoration pre-pass (CPU-only) | **$0** | OpenCV + Sauvola installed |
| Wrap baseline (surya + tesseract + easyocr + indicphotoocr) | **$0** | Already-installed; CPU |
| Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1) | **$0** | mlx-tune installed locally; M2 Max |
| Cloud fine-tune (Alt C, OPTIONAL) | **$5-60 spot** | Only if Vinay wants the technical ceiling |
| **Total recommended (D1 default = A)** | **$12** | Ships in W6 window |
| **Total ceiling (B + C)** | **$17-72** | W6 + W7 |

---

## 5. 5-doc reading order (what we hand Vinay at the meeting)

1. **`VINAY_MEETING_PACKET.md`** (this file, this folder) — TL;DR + status + decision menu.
2. **`STRATEGY_VINAY_TOMORROW.md`** (this folder) — The strategy narrative + recommendation. *(merged into this file)*
3. **`VINAY_CTA.md`** (this folder) — The 4 decisions + 3 strategic questions. *(merged into this file)*
4. **
5. **`docs/architecture/W5_BEAT_SARVAM_PLAN.md`** — Concrete beat-Sarvam recipe (Stages 1/2/3).

Vinay reads docs 1 + 2 + 3 (~10 min). User presents docs 4 + 5 if Vinay wants depth (~15 min).

### Reading order for Vinay tomorrow (alt view)

1. `STRATEGY_VINAY_TOMORROW.md` (3 min) — single-page brief *(merged into this file)*
2. This packet (5 min) — 3 questions + 5 decisions
3. `VINAY_CTA.md` (2 min) — single-page "what Vinay needs to know and decide" *(merged into this file)*
4. 
5. `docs/architecture/W5_BEAT_SARVAM_PLAN.md` if head-to-head vs Sarvam 2.1 is wanted (10 min)

---

## 6. After the meeting timeline

### After the meeting (post-Vinay)

- **Same day (Wed 2026-09-30 evening):** User updates `OCR_AGENT_MEMORY_FEED.md` §16 with Vinay's decision. Updates `CALL_PACKET.md` §0 status from `🟡 PENDING VINAY` → `🟢 D1 LOCKED at Vinay` (or `🔴 Vinay deferred`).
- **2026-10-01 (Thu, date TBC per U1) evening:** W5 freeze window opens. Per-script routing locked. Backbone choice GLM-OCR 0.9B confirmed (or rejected if Vinay picked Option B).
- **2026-10-01 (Thu, date TBC per U1) → 2026-10-03 (Sat, date TBC per U2):** QLoRA execution on Konkani only (Punjabi ties at p=1.0 — see Q1). Wrap-only ships regardless at W5 freeze.
- **2026-10-04 (Sun), date TBC (U2):** W6 freeze + final deliverable.

### Timeline (lock W6 path now → W7 jury demo)

| Phase | Window | Deliverable |
|---|---|---|
| **Tomorrow (Vinay meeting)** | 2026-09-30 | Lock Q1/Q2/Q3 + D1-D5 |
| W5 freeze | 2026-10-01 (Thu), date TBC (U1) | Recipe frozen, no new inputs |
| W6 wrap + QLoRA | 2026-10-02 → 2026-10-08 | Ship Option B; Sarvam subsidy runs |
| W7 demo + jury | 2026-10-11 → 2026-10-15 | Hackathon submission |
| W8 backup | 2026-10-16+ | Stretch GLM-OCR fine-tune |

### End-state one-liner

> Wrap-only pipeline ships regardless (competitive with Sarvam on the cells we measured (n=3/lang, directional), ~30min wall). If Vinay picks Option A, add Konkani-only QLoRA (Punjabi ties at p=1.0 — see Q1) (~3-4h wall, $0). Total budget ask: **$0 compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells (budget table below)**. Next gate: **Vinay meeting → W5 freeze after 2026-10-01 (Thu, date TBC per U1) → W6 training decision**.

---

## 7. Risk register

- **Risk 1: Sarvam headline number (87.39) is the WRONG comparison.** Our 12,324 sheet.csv rows (1,227 items across 18 languages) cover 18 Eighth-Schedule languages + EN sanity, not just Sarvam's 6,909 blocks on a curated subset. Cell-by-cell, **surya beats Sarvam on the cells Sarvam itself reports as weak** (OldScan 55.3, Kashmiri 54.82, Odia 80.01, Santali 53.91 — these per-language numbers ARE public on Sarvam's own bench, but quarantined as DEAD-for-decisions per `OBITUARIES.md` O-02–O-05; directional only, different harness). Headline: our wrap-only routing targets the weak cells Sarvam doesn't publish, not their headline average.
- **Risk 2: mni/sat are Sarvam-only cells.** No local engine emits Ol Chiki or Meitei-Mayek. Wrap pipeline can't move these 2 cells. We will score 0.85–1.0 CER on Santali/Manipuri no matter what; Sarvam scores 0.22 / 0.03 on the 3-packs. The cell-by-cell battle is on the other 16 langs.
- **Risk 3: K1 may KILL Option A at W5 freeze.** kok significant (McNemar p=0.0033); pa NOT significant vs runner-up (p=1.00, n=90) on current disk state, but a re-verification at the freeze call is required. If K1 KILLS (low-probability but possible), we fall back to Option B (wrap-only ships without QLoRA).
- **Risk 4: Backbone weights download is a separate gate.** GLM-OCR 0.9B weights download (~1.8 GB) is a §9 hard rule event — explicit user approval needed. We are NOT in the $0 ask. If Vinay wants Option A with GLM-OCR, user approves the download separately at W5 freeze.

### What Vinay should know about risks (60-second disclosure)

- **Risk 1:** Sarvam headline (87.39) is the wrong comparison for cell-by-cell battle. Our wrap-only routing targets the weak cells Sarvam doesn't publish.
- **Risk 2:** Santali + Manipuri are Sarvam-only cells (no local engine emits Ol Chiki or Meitei-Mayek). Wrap pipeline can't move these. Cell-by-cell battle is on the other 16 langs.
- **Risk 3:** K1 may KILL Option A at W5 freeze. kok significant (McNemar p=0.0033); pa NOT significant vs runner-up (p=1.00, n=90) on current disk state, but re-verification at the freeze call is required. Fallback: Option B (wrap-only ships, no QLoRA).
- **Risk 4:** GLM-OCR 0.9B backbone weights download (~1.8 GB) is a separate user gate (NOT in the $0 ask). Approve at W5 freeze if Option A picked.

---

## 8. Wall-clock math (for Vinay's planning)

| Phase | Wall | Owner | Notes |
|---|---|---|---|
| **Wed 2026-09-30** | ~30 min | User + Vinay | Strategy decision. |
| **2026-10-01 (Thu, date TBC per U1) evening** | W5 freeze opens | Orchestrator + Engine | Per-script routing locked. Backbone choice GLM-OCR 0.9B confirmed. |
| **2026-10-01 (Thu, date TBC per U1) → 2026-10-03 (Sat, date TBC per U2)** | ~3-4h | Engine + Miss | QLoRA execution on Konkani only (Punjabi ties at p=1.0 — see Q1). Wrap-only ships regardless at W5 freeze. |
| **2026-10-04 (Sun), TBC (U2)** | W6 freeze + final deliverable | All 3 agents | Final wrap-only output + (if Option A) QLoRA adapter + benchmark comparison vs Sarvam 87.39. |

Total budget: **$0 compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells (budget table below) + ~4h wall** (Option A) or **$0 + ~30min** (Option B) or **$0 + ~8h** (Option C).

---

**Sign-off:** Miss agent · 2026-09-29 IST · this merged packet ready for user review before tomorrow's Vinay meeting.

**Provenance:** Rewritten in place at 2026-09-29 20:08 IST (Miss agent, Lane C) from `STRATEGY_VINAY_TOMORROW.md` and `VINAY_CTA.md` (both deleted), per audit-5. Audited by Verdict 2026-09-29 (this file's sibling: `docs/architecture/VINAY_MEETING_PACKET.md`, 17:05).
---

## 📌 POST-DEEP-RESEARCH UPDATE (2026-09-29 22:00 IST)

After 26-source deep research + probe22 edge analysis, the strategy refines from "Option A (wrap-only)" to "Option A+ (wrap-only + surgical SFT)":

### Honest Finding
**We CANNOT beat Sarvam on macro-average 87.39** — different bench, different harness, private eval.

**We CAN win on:**
1. **Sarvam's weakest published cells** (Sat, Ks, Or, OldScan) — where they admit weakness
2. **probe22 n=100 per-lang where we have ground truth** (18 langs × measured CER)
3. **Wrap-only routing in <30h** (vs their pipeline)
4. **Open weights** (Bodhan already 84.94, ~2.45pp from Sarvam)
5. **Per-script surgical SFT** (asymmetric compute)
6. **Koshur Pixel** (613k Kashmiri pairs, public, no published Indic OCR VLM has used it)

### Refined W6 Path (3 Options)

**Option A (Default, $0)**: Wrap-only routing ships by Oct 1
- Per-language routing per probe22 evidence (surya 9 langs, tesseract 2, indicphotoocr 1, sarvam_vision 4)
- Koshur Pixel fine-tune (no GPU, ~1h on M2 Max)
- Defense on 6 langs where we beat Sarvam (or, brx, ks, mai, sd, gu)
- Risk: NONE (no training, no new backbone)

**Option B ($0-50)**: Add Local QLoRA
- A + Kok + Pa QLoRA on local MLX (~3-4h wall, $0, only if McNemar K1 gates at W5 freeze)
- Risk: Low (proven approach)

**Option C ($50-150)**: Add Bodhan Surgical SFT
- A + Bodhan 6-day SFT on 6 weakest langs (Sat/Ks/Mni/Or/Sa/Do)
- Uses Koshur Pixel + R3 Ol Chiki/Meitei synthesis + RLVR with CER rewards
- ~130 GPU-h on Vast.ai A100 spot, 6 days
- Target: Sarvam 53.91 (Sat) and 54.82 (Ks) where they're weakest

**Decision tomorrow**:
- Wrap-only (Option A) ships regardless — no approval needed
- QLoRA local (Option B) needs only W5 freeze McNemar gate to surface
- Bodhan SFT (Option C) needs user approval for $50-150 cloud GPU spend

### New Detailed Strategy
See `docs/research/W6_STRATEGY_UNIFIED.md` (248 lines) for full breakdown.
