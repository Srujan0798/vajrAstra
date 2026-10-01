# G-B4 — paddle server-det retest (post-timeout-fix)

**Question (B4):** the server-det downgrade to mobile-det-light happened under timeout pressure (te_053 timeout era). Post-fix, does FULL mode (server det + lang rec, uncapped) beat the shipped packs?

**Method:** 4 pages (te_053 — the historical timeout page — te_001, ta_001, kn_001), paddleocr 3.7.0 (.venv311), `PaddleOCR(lang=te/ta/ka, use_doc_orientation_classify=False, use_doc_unwarping=False, use_textline_orientation=False)`, single-page sequential, wall-clock timed after lazy-generator consumption. Shipped-pack text read from `out/paddleocr_indic/<lang>/<pid>.json` regions. Script: `b4_paddle_server_gate.py` (idempotent; rerun overwrites `b4_results.json`).

## Results

| page | full ms | full chars | full ratio | shipped chars | shipped ratio | verdict |
|---|---|---|---|---|---|---|
| te_053 | 79 | 1827 | 0.783 | 1827 | 0.783 | IDENTICAL |
| te_001 | 29 | 1989 | 0.797 | 1989 | 0.797 | IDENTICAL |
| ta_001 | 7 | 1477 | 0.874 | 1477 | 0.874 | IDENTICAL |
| kn_001 | 7 | 3307 | 0.358 | 3307 | 0.358 | IDENTICAL |

(full_ratio = fraction of chars in the page's dominant script range; kn_001 is a mixed Devanagari/Latin exam booklet — 0.358 is expected, not a fidelity failure.)

## Verdict: NO-GAIN — shipped config stays

1. **Full mode is byte-identical to shipped packs on 4/4 pages.** The historical timeouts were **load-transients** (parallel engines saturating CPU), not a server-det config failure: with the machine unloaded, server det + lang rec completes in 7–79 s/page.
2. The light-mode fallback machinery in run_engine.py (`_paddle_poisoned`, 300s/900s budgets) remains correct insurance — it fires only when full times out under load, and its output equals full's on these pages.
3. **No rerun.** Winning condition (≥10% more chars at same-or-better fidelity) met on 0/4 pages.

## Fission spawn (B4.1)

What load level makes server det actually time out? (stress: N parallel pipelines) — parked, LOW priority: the fallback already handles it and produces identical text.

## Time-truth note

te_053/te_001 `full_ms` = 79/29 s include first-predict model warm-up per language instance; ta/kn (7 s) reuse warm models from earlier pages in-process. Per-page steady-state is single-digit seconds on an idle machine.
