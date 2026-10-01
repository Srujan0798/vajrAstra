# GATE G-B1 — doctr 1.1.0: PARSeq vs CRNN (+ detect_layout) — 4-PAGE GATE

Date: 2026-09-13 · Runner: EXEC (opencode) · Env: `.venv311` (py3.11, torch 2.14.0, doctr 1.1.0, MPS available)
Pages: te_001 / ta_001 / kn_001 / ml_001 (level2/renders_shared/, 200-dpi renders)
Gate law: 4-page gate BEFORE any 400-page claim. Verdict rule: win = script-fidelity
ratio not dropped AND chars +≥10%. Latin mojibake on Indic page = instant fail.
Raw data: `research/gates/b1_results.json`, `b1_parseq_telugu_vocab.json`, `b1_quality_jac.json`.
Scripts: `research/gates/b1_doctr_parseq_gate.py`, `research/gates/b1_parseq_telugu_vocab_gate.py`
(standalone; no shared .py touched).

## 1. Architecture availability (doctr 1.1.0, .venv311)

- Recognition zoo ARCHS: `crnn_vgg16_bn`, `crnn_mobilenet_v3_small/large`, `sar_resnet31`,
  `master`, `vitstr_small/base`, **`parseq`**, `viptr_tiny`. PARSeq IS shipped — no extra install needed.
- Weights: `parseq` zoo checkpoint = `doctr-static.mindee.com .../parseq-56125471.pt` (95 MB),
  downloaded fresh during the gate (cached `~/.cache/doctr/models/parseq-56125471.pt`).
  A second unrelated `~/.cache/torch/hub/checkpoints/parseq-bb5792a6.pt` (95 MB) pre-existed
  (IndicPhotoOCR's, different checkpoint — do not confuse them).
- **Vocab trap (the real finding):** BOTH crnn_vgg16_bn AND parseq zoo checkpoints are trained
  with `VOCABS["french"]` (Latin script). doctr 1.1.0 *defines* telugu/tamil/kannada/malayalam/
  hindi vocabs (`doctr/datasets/vocabs.py` lines 554-610) but **ships NO pretrained weights for any
  Indic script** for any reco arch. So "PARSeq, doctr's accuracy leader" is accuracy leader
  **on Latin text only** — it cannot read Telugu/Tamil/Kannada/Malayalam any more than CRNN can.

## 2. Main gate table: CRNN vs PARSeq (zoo weights, French vocab)

| page | arch | chars | script chars | latin | script ratio | ms |
|---|---|---|---|---|---|---|
| te_001 | crnn_vgg16_bn | 1481 | **0** | 967 | 0.000 | 2435 |
| te_001 | parseq | 1584 | **0** | 1082 | 0.000 | 1960 |
| ta_001 | crnn_vgg16_bn | 1510 | **0** | 1199 | 0.000 | 1701 |
| ta_001 | parseq | 1550 | **0** | 1282 | 0.000 | 1505 |
| kn_001 | crnn_vgg16_bn | 3441 | **0** | 2603 | 0.000 | 4720 |
| kn_001 | parseq | 3560 | **0** | 2746 | 0.000 | 3903 |
| ml_001 | crnn_vgg16_bn | 2081 | **0** | 1566 | 0.000 | 2132 |
| ml_001 | parseq | 2260 | **0** | 1774 | 0.000 | 2004 |

Both archs = 100% Latin mojibake on all 4 Indic pages (**instant-fail clause**). PARSeq emits
~7% more characters than CRNN — all of them wrong-script. Quality check (char 5-gram Jaccard vs
surya GT, te_001): crnn 0.0118, parseq 0.0106, parseq-telugu-vocab 0.0000 — all ~zero,
i.e. no real reading either way.

## 3. Canon-side probe: PARSeq with VOCABS["telugu"] (te_001 only)

Building `parseq(pretrained=True, vocab=VOCABS["telugu"])` works mechanically (heads reinit;
backbone loads). Result: chars 9009, script chars 4808, **script ratio 0.5337** — LOOKS like a
huge fidelity win. Eyeball + Jaccard kill it: output is glyph salad (`ఒఒఒఒౠౠ...` repetitions),
Jaccard-5 vs GT = **0.0000**. The reinit head hallucinates valid-Unicode Telugu junk: script-ratio
alone would have awarded a fake PASS. This is exactly the mojibake-class failure the verdict
rule exists for (fake fidelity, worse than Latin mojibake because it games the ratio metric).
Note: `ocr_predictor(..., reco_arch="parseq")` does NOT forward vocab kwargs in 1.1.0 — the
probe had to assemble `OCRPredictor(det, reco)` manually.

## 4. detect_layout=True (te_001, crnn default)

- Output TEXT: **byte-identical** to non-layout run (1481 chars, same lines). No text change.
- Structure: adds `page["layout"]` — a list of {geometry, type, confidence} regions
  (te_001: mostly "List-item" conf ~0.53-0.61). Adds `layout` + `tables` keys to page export.
- Cost: 2556 ms vs 2435 ms baseline (+~5%, plus one-time lw_detr_s download 59 MB).
- Verdict for the benchmark: detect_layout adds region metadata but zero OCR text; not worth
  rerunning 400 pages for. Could matter later for region-aware GT alignment, not for packs.

## 5. VERDICT — G-B1: **CRNN vs PARSeq = NO CONTEST / BOTH INDIC-DEAD (ARCH SHIPPED, SCRIPT NOT)**

- PARSeq does NOT beat CRNN on script-fidelity × char-volume: both are 0.000 fidelity on all
  4 pages. PARSeq's +7% char volume is 100% wrong-script noise (fails the mojibake clause).
- Gate result is NOT "architecture-not-shipped" (PARSeq IS in doctr 1.1.0) — it is
  **"Indic weights not shipped"**: zoo has no Telugu/Tamil/Kannada/Malayalam checkpoint for any
  reco arch. doctr's Indic vocab definitions without Indic weights = dead end for L2 South pages.
- parseq-telugu-vocab probe: fake-fidelity trap documented (ratio 0.53, quality 0.00).
- detect_layout: text-identical, +5% time, adds layout regions only. Not benchmark-relevant.
- CONSEQUENCE: doctr stays as-is in the engine matrix (Latin-only mojibake engine, already
  honestly graded in LEADERBOARD). No 400-page rerun justified by B1. Zero machine-hours.

## Conflicts found / spawned (fission duty)

- C1: metric-gaming risk — script-ratio alone can be fooled by valid-Unicode junk
  (parseq-telugu case). Proposal: any PASS-grade needs ratio + Jaccard-5 floor (e.g. ≥0.3)
  or human eyeball. → feeds RED/verification lane.
- Q-B1.1 (deeper): would fine-tuning parseq heads on our training_assets (export_training_data.py)
  give a real Indic doctr? Cost/benefit vs surya (already wins)? → parked; L3 candidate, not L2.
- Q-B1.2 (inverted): is our doctr LEADERBOARD row (Latin mojibake) being fairly weighted in
  consensus voting, or is it dragging consensus GT down? → audit question, C-track.
