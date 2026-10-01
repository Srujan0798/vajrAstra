---
name: proto-112-execution-playbook
description: "FINAL (2026-10-01, cloud planner, after a 10-auditor deep audit): THE execution playbook. Research/plan are done; execution and product are near zero. One minimal winning path: HW-ID(100) → U-HW1 → HW0 → HW1 zero-shot (= fallback submission) → one PARSeq fine-tune → product CLI on 5,344 crops (CSV+JSON) → pitch. Owners, exact files/commands, done-when, 24-h default-proceed rules, stop-loss, cut list. Overrides proto-108 rev 2 on ORDER and SCOPE (proto-108 stays the reference)."
metadata:
  node_type: memory
  type: project
---

# PROTO-112 — EXECUTION PLAYBOOK (FINAL). Read this, then only your lane.

## 0. Verdict (one paragraph)
- **Research and plan: strong.** 320 files read, checked and synthesised.
- **Execution and product: near zero.**
  - No trained model.
  - No handwriting baseline, no Bengali handwriting data on disk.
  - Leak check (HW0) never run; only 16 of 5,344 test images viewed.
  - Bodhan's PyTorch path has never completed. Its page-vs-crop gap (O-1) is undiagnosed.
  - No single committed scorer: WRR/CRR and Wilson CI do not exist in code.
  - The product/ code is unverified: not in the GitHub snapshot, only claimed in W4.md:455-492.
- **Why execution stalls** (`docs/campaign/final_audit_2026-10-01/A4-EXECLOG.md`):
  - 8 boss gates with no default.
  - A day lost to an agent's own delete incident.
  - Locked files and the layout freeze.
  - Claims without evidence: 35 bare DONE vs 1 DONE-VERIFIED.
  - About 6 instruction changes in 2 days.
  - Agents idle by design, waiting for the planner.
  - No GPU.
  - Verifiers that only check that files exist.
- **The deadline is unknown, not far.** Only "pitch screening 23/07/2026" is dated, and it is 70 days past. Plan to ship a demoable submission in ~5 days, then extend.

## 1. The ONE path (everything else is cut until submission)
- **D0 (today):** organiser + Vinay questions sent; HW-ID on 100 crops; downloads approved; scorer written.
- **D1:** HW0 leak check; HW1 zero-shot on IIIT Bengali val = the fallback system.
- **D2:** the boss signs the training gate; one PARSeq fine-tune (24 GB GPU, or Mac MPS if no GPU).
- **D3:** promote or keep zero-shot; product CLI turns the 5,344 crops into CSV + JSON; 50-image timed dry run.
- **D4–D5:** pitch package and demo. Bodhan page path shown as "prototype".
- **STOP-LOSS:** at D3 with no GPU and no IIIT data → ship the HW1 zero-shot system; the fine-tune goes on the roadmap slide.

## 2. Lanes (one lane per agent; each step ends with its check pasted in W4.md)
### Boss (D0, ~30 min total; each item has a default)
1. **Email gic.dibd@gmail.com:** which stage we are in, Stage-2 date, metric, submission format. Message Vinay the same, plus the layout/LID questions (proto-111 §0). Do not wait for answers.
2. **Downloads, YES/NO** (default YES 24 h after Agent 2 reports licence + size):
   - IIIT-INDIC-HW-WORDS Bengali (AIKosh);
   - Tesseract `ben` traineddata;
   - the baudm/parseq repo (Apache-2.0).
3. **Training gate (replaces the G-2.5 committee; needs YOUR explicit yes):**
   - sign proxy thresholds: IIIT val WRR ≥ 92%, independent writers ≥ 85%;
   - set a GPU-hour cap (default 6 h);
   - WhatsApp Vinay the one-page plan.
   - If he does not reply within 24 h, proceed and record it. His red line "no training before research validation" is answered by this audit plus the plan.
4. **GPU SSH:** ask Vinay for the login. The fallback is Mac MPS (PARSeq is small).

### Agent 1 — Engine (the only score-moving lane)
- **HW-ID** (D0, read-only):
  - create `level2/benchmark/handwriting/hw_id_sample.py`: 7 ID buckets, seed 20260930, about 15 per bucket = 100;
  - view each crop; fill `level2/benchmark/docs/HW_ID_AUDIT.md` (id, script, single/multi-word, quality) with the % single Bengali words and its Wilson CI;
  - kill: < 80% → stop and tell the boss.
- **HW1** (D1, no training):
  - `level2/benchmark/handwriting/hw1_zeroshot.py --system {ipo_bn,tess_ben} --manifest … --out …/HW1_<sys>_<set>.jsonl`;
  - `ipo_bn` loads IndicPhotoOCR's Bengali recogniser directly on the crop, NOT the page pipeline;
  - runs on IIIT bn val (after download) and on 200 official crops (view-only: outputs + s/word, no accuracy claim);
  - Bodhan handwriting mode only if its PyTorch path works;
  - scored with `eval_harness.py --mode crop`;
  - done-when: `HW1_SUMMARY.md` gives WRR/CRR/CER, n and CI per system.
- **HW2** (D2, after the boss's gate):
  - one run, PARSeq (baudm/parseq), recipe in `final_audit_2026-10-01/A5-HANDWRITING.md` §HW2:
    - Bengali charset computed from the labels; `data.normalize_unicode=false` (NFC done by us);
    - `max_label_length` from the label histogram;
    - two image sizes, [32,128] and [64,256], chosen on val;
    - init from `bengali.ckpt` if its licence clears, else PARSeq base with the head re-initialised;
  - 5-item smoke test first;
  - check Jaccard-5 after epoch 1 (a re-initialised head can emit glyph salad);
  - done-when: `level2/benchmark/docs/HW2_RESULT.md` with val WRR, CI, commands.
- **Promote** (D3): ship the fine-tune only if val WRR beats HW1 on the same items with a CI that does not overlap; else ship zero-shot.

### Agent 2 — Verdict / tools (unblocks Agent 1; nothing else first)
1. **D0 — scorer:** `level2/benchmark/pipeline/eval_harness.py` with `score | compare | selftest` (spec in `A3-SCORER.md` actions 1–2).
   - Metrics: CER, WER, WRR, CRR, median, empty and catastrophic rates, Wilson + bootstrap CI, exact McNemar.
   - `--mode crop` has no short-GT exclusion.
   - Done-when: `selftest` exits 0 and is wired as T7 in `level2/tests/run_tests.py`.
2. **D0 — licence rows, 3 only:** the AIKosh IIIT page + zip README (counts, size); the STocr `bengali.ckpt` licence; the PARSeq LICENSE. Write them as RESEARCH_DECISIONS rows.
3. **D1 — HW0:** `level2/benchmark/handwriting/hw0_leak_gate.py` (sha256 + pHash/dHash, fail-closed, self-test on rescaled/recompressed copies; spec in `A5-HANDWRITING.md` §HW0).
   - Run the 5,344 crops against IIIT bn train/val/test and `Bodo/gu`.
   - Done-when: `HW0_LEAK_REPORT.json` shows `overlap_total` = 0 after exclusion.
4. **D2 — Bodhan unblock (parallel, low priority):**
   - grep the CUDA assert in `level2/models_bodhan/indic-ocr`;
   - device auto-select in `run_bodhan_pytorch.py`; loud failures;
   - then the O-1 diagnostic (6 steps in `A2-BODHAN.md`) → `docs/campaign/O1_PAGE_GAP.md`.
5. **Every round:** proto-109 sync A at the end. Verify numbers by re-running commands, not by checking that files exist.

### Agent 3 — Product (stop proto-107 at its current wave)
1. **D0 — truth check:** `ls -R product scripts | head -100` and `git status --short product scripts`. Report in W4.md whether the CLI, schema, requirements.txt, Dockerfile and `agent_bootstrap.sh` really exist. They are NOT in the GitHub snapshot.
2. **D1–D3 — `python -m product.cli`:**
   - (a) `--crops DIR` → `image,text,confidence` CSV + per-image JSON, using the Track A recogniser (zero-shot first, swapped for the fine-tune when promoted);
   - (b) `--page FILE` → JSON + searchable PDF + MD via Bodhan (PyTorch; Tesseract fallback recorded in the JSON), labelled prototype;
   - pinned `requirements.txt` (torch), Dockerfile (CPU/CUDA), NOTICE (Bodhan attribution, Apache tessdata, PARSeq, IIIT CC-BY);
   - done-when: a 50-crop timed CPU run (s/image, peak RAM) logged, extrapolated to 5,344.
3. **D4 — pitch package from `A7-JURY.md`:**
   - 10-slide outline, 5-min demo script, cost/TCO sheet, 4-year costing;
   - one slide per official criterion;
   - only the allowed claims (proto-108 rev 2 §5);
   - blanks marked NEEDS BOSS INPUT.

### Planner (cloud; one turn per sync)
- Read the synced W4.md lines.
- Check each number against its done-when and kill rule.
- Write the next paste lines (≤ 5 lines each).
- Update the two Claude Docs only with measured numbers.

## 3. Default-proceed rule (kills the stall pattern)
- Any boss decision unanswered 24 h after it is asked → the recommended default applies, logged in W4.md as `DEFAULT-PROCEED <item>`.
- Exceptions (never default): deletions, money/Sarvam spend, hosting Bodhan, pushing to `main`.

## 4. CUT until submission (do not run, do not assign)
- proto-110 knowledge canon beyond K0 (K0 = manifest + bundle only, safe, may finish). The Vigilante stops after K0.
- proto-111: ACTIVE since Vinay's answer, but only as Agent 3's product-side bake-off after D0 (see proto-111 UPDATE). It never takes Agent 1 off Track A.
- proto-107 waves after the current one.
- Track B per-cell recipes (sat/mni/ks/or/sa/kok/R4), HW3, HW-P2, RL, post-correction.
- The multi-LLM committee, 25-question drill, transfer obituaries, sampling proofs, GT_DEFECTS, South S5/S6.
- Alternate backbones, the 71-file second pass, P49/P50 verification, Docs polish without new numbers.

## 5. Claims (pitch and Docs)
- **Allowed:**
  - "test = handwritten word crops (n viewed)";
  - our measured WRR on IIIT val / independent writers, with n and CI;
  - offline, ₹0 per image, portable;
  - the per-language honesty layer.
- **Never:**
  - beating 87.39;
  - cross-bench comparisons;
  - "we lead 10/18";
  - "96% on the test";
  - any number without its command;
  - product features that don't run.

## 6. Snapshot caveat (read before trusting the audit)
The cloud planner saw text files only. `product/` code, `scripts/agent_bootstrap.sh`, `docs/campaign/gold/`, weights, data and preds were not in the snapshot. Every "missing" for those paths means "unverified here". Agent 3's D0 truth check settles it.

Evidence: `docs/campaign/final_audit_2026-10-01/A1…A10*.md`. Related: [[proto-108-plan-v4-final]], [[proto-109-github-mac-sync]], [[proto-110-knowledge-canon]], [[proto-111-layout-and-language-id]], [[proto-107-gold-repo-consolidation]].
