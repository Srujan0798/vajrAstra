# P4 ELITE SEQUENCING — plan only (no code until operator approval)
Round 1, 2026-09-30. Law: ULTIMATE_HYBRID_CONCERN §13 next-H (P4 elite: cascade / distillation /
Triton / active learning). Every item passes a 4-page gate (te_087, ta_092, kn_048, ml_019) before
any 400-page run (L3), lives in research/ or a new standalone module (L10), and never trains on
bench pages (firewall). Evidence cited is from Round-1 generators in this folder.

## What the Round-1 evidence changes about P4
1. **Reading order is the cheapest big win.** METRIC_ROBUSTNESS.md: paddleocr_indic and rapidocr
   are 7th–8th by sealed CER (≈0.63) but 3rd–4th by the order-invariant char-3gram error (≈0.24–0.25,
   near anuvaad's 0.21). Their loss is block/line ORDER, not glyph recognition. This is the deck's
   Stage-1 (layout) argument, now with numbers.
2. **Consensus/fusion stays dead.** PSEUDO_GT.md + METRIC_ROBUSTNESS.md: a 3-family consensus is
   worse than the best single engine on the same pages at every τ — the third independent
   confirmation after G-B12. Do not build ensemble text fusion.
3. **Tier-1 is a 5-way tie on South scripts.** STRATIFIED_BOOTSTRAP.md: on own-script pages (n=66)
   surya, anuvaad and the whole tesseract family are statistically tied, and the tesseract family runs
   at ~3.3 s/page vs surya ~16 s (LATENCY_SWEEP_PLAN.md). That makes a cheap-first cascade credible.
4. **Evaluation must be fixed before any P4 result is quotable.** 26 of 126 sealed CER pages score
   engines against legacy-font garbage (script_mismatch); CER charges engines for layer order and
   layer artifacts. P4 gains measured on the sealed metric would be partly noise.

## Sequence (dependency-ordered)

| # | Item | Depends on | 4-page gate question | Kill criterion |
|---|---|---|---|---|
| P4.0 | **Evaluation v2 in the writer** — tag-independent mojibake gate + an order-invariant column (flexible character accuracy) next to CER | operator H-decision (writer change, L2 one-writer) | do the 4 gate pages score identically to research/ generators? | none — prerequisite |
| P4.1 | **Reading-order repair (no training)** — re-sort paddle/rapidocr boxes by column-aware XY-cut before joining text | P4.0 | does char-CER drop toward char-3gram error on ≥3/4 pages, with unchanged char-3gram? | CER gain < 0.05 median on gate |
| P4.2 | **Cascade** — tesseract-family first; escalate to surya only on low-confidence pages | P4.0, confidence signal validated on clean_v2 | does cascade CER on the gate equal surya's at < 50% of surya's time? | confidence signal AUC < 0.7 on clean_v2 |
| P4.3 | **Active learning loop** — rank unlabeled pages by engine disagreement for human verification | GT_EXPANSION_QUEUE.md batch 1 verified | do verified pages move any per-script CI? | reviewer throughput < queue assumption by >2× |
| P4.4 | **Distillation (Vaultstack Stage 2, outside L2)** — student trained on NON-bench pages, teacher = best route from P4.2 | P4.2, training data sourced outside the 400 (firewall), budget | gate on bench pages: student within 0.05 of teacher at ≥5× speed | any bench page found in training data |
| P4.5 | **Serving (Triton)** | P4.4 student exists | p99 latency on gate pages under target | only after a model worth serving exists |

## Human decisions needed (batch to Srujan)
- H: adopt evaluation v2 into the writer (P4.0) — changes report numbers; needs a DECISIONS.log entry and a Vinay/David note.
- H: P4.4 training data source outside the bench (licensing H3) and compute (money H2).
- P4.1–P4.3 need no money; they can start as soon as P4.0 is approved.
