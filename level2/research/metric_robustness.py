#!/usr/bin/env python3
"""RED P0 (T3): is sealed char-CER measuring recognition, or reading order?

    python3 level2/research/metric_robustness.py

Finding that triggered this: on high-agreement pages the engine text is
near-correct but in a different BLOCK ORDER than the PDF text layer, and the
PDF layer carries extraction artifacts (doubled vowel signs). Plain CER then
charges the engine for the layer's order. Standard remedy in OCR evaluation:
reading-order-independent measures (e.g. flexible character accuracy,
Clausner/Pletschacher/Antonacopoulos 2020). Here, the simplest such measure:

  BoW error = 1 - F1 over word MULTISETS (cer_norm tokens)  — order-invariant

Plus char-3gram error = 1 - F1 over char-3gram multisets (order- and
segmentation-invariant; line matching was tried and rejected, see md).
Reports on clean_v2: per-engine median CER vs median BoW error, the ranking
under each, how often the layer contains doubled dependent vowel signs, and
whether cross-engine pseudo-GT becomes usable once order is factored out.
Writes research/METRIC_ROBUSTNESS.{json,md}. Nothing sealed is modified.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r1_common as C  # noqa: E402
import pseudo_gt as P  # noqa: E402

OUT = HERE / "METRIC_ROBUSTNESS"
# dependent vowel signs (matras) of the five Indic blocks we score
MATRA = "[ा-ौா-ௌా-ౌಾ-ೌാ-ൌ]"
DOUBLED = re.compile(f"({MATRA})\\1")


def bow_err(hyp: str, ref: str) -> float:
    h, r = Counter(C.cer_norm(hyp).split()), Counter(C.cer_norm(ref).split())
    if not r:
        return 0.0 if not h else 1.0
    tp = sum((h & r).values())
    if tp == 0:
        return 1.0
    p, rc = tp / sum(h.values()), tp / sum(r.values())
    return round(1 - 2 * p * rc / (p + rc), 4)


def char3_err(hyp: str, ref: str) -> float:
    """Order- and segmentation-invariant char measure: 1 - F1 over the
    MULTISET of char 3-grams (whitespace removed). Independent of line/block
    splitting (unlike line matching, which fails on block-mode engines — the
    same line-granularity trap as gate G-B12)."""
    def grams(t):
        z = "".join(C.cer_norm(t).split())
        return Counter(z[i:i + 3] for i in range(len(z) - 2))
    h, r = grams(hyp), grams(ref)
    if not r:
        return 0.0 if not h else 1.0
    tp = sum((h & r).values())
    if tp == 0:
        return 1.0
    pr, rc = tp / sum(h.values()), tp / sum(r.values())
    return round(1 - 2 * pr * rc / (pr + rc), 4)


def main() -> None:
    v2 = C.basis()["clean_v2"]
    M = C.cer_matrix()
    gold = C.gold_raw()
    B = {p: {e: bow_err(C.engine_text(e, p), gold[p]) for e in C.ENGINES} for p in v2}
    LM = {p: {e: char3_err(C.engine_text(e, p), gold[p]) for e in C.ENGINES} for p in v2}
    eng = {e: {"cer": round(median(M[p][e] for p in v2), 4),
               "char3_err": round(median(LM[p][e] for p in v2), 4),
               "bow_err": round(median(B[p][e] for p in v2), 4)} for e in C.ENGINES}
    rank_c3 = sorted(C.ENGINES, key=lambda e: (eng[e]["char3_err"], e))
    rank_cer = sorted(C.ENGINES, key=lambda e: (eng[e]["cer"], e))
    rank_bow = sorted(C.ENGINES, key=lambda e: (eng[e]["bow_err"], e))

    gt_doubled = sum(1 for p in v2 if DOUBLED.search(gold[p]))
    eng_doubled = {e: sum(1 for p in v2 if DOUBLED.search(C.engine_text(e, p))) for e in ("surya", "anuvaad_tesseract")}

    A = P.load_all()
    ps = {}
    for tau in P.TAUS:
        q = [p for p in v2 if P.pseudo(A[p], tau)]
        meds = {p: C.engine_text(P.pseudo(A[p], tau), p) for p in q}
        c3 = [char3_err(meds[p], gold[p]) for p in q]
        best = [min(LM[p].values()) for p in q]
        ps[str(tau)] = {"pages": len(q),
                        "pseudo_vs_gold_char3_median": round(median(c3), 4) if c3 else None,
                        "best_single_engine_char3_median": round(median(best), 4) if best else None,
                        "pseudo_vs_gold_bow_err_median": round(median(bow_err(meds[p], gold[p]) for p in q), 4) if q else None}

    res = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "n": len(v2),
           "engines": eng, "rank_cer": rank_cer, "rank_c3": rank_c3, "rank_bow": rank_bow,
           "pages_with_doubled_matra_in_pdf_layer": gt_doubled, "same_in_engine_output": eng_doubled,
           "pseudo_gt_under_bow": ps}
    C.write_json(OUT.with_suffix(".json"), res)
    L = ["# METRIC ROBUSTNESS — char-CER vs order-invariant bag-of-words error",
         f"generated {res['generated_at']} by `research/metric_robustness.py` on clean_v2 (n={len(v2)}); do not hand-edit", "",
         "| engine | CER (sealed, order-sensitive) | rank | char-3gram error (order+segmentation-invariant) | rank | BoW word error (order-invariant) | rank |",
         "|---|---|---|---|---|---|---|"]
    for e in rank_c3:
        L.append(f"| {e} | {eng[e]['cer']:.3f} | {rank_cer.index(e) + 1} | {eng[e]['char3_err']:.3f} | {rank_c3.index(e) + 1} | "
                 f"{eng[e]['bow_err']:.3f} | {rank_bow.index(e) + 1} |")
    L += ["", f"PDF-layer extraction artifact: {gt_doubled}/{len(v2)} GT pages contain a doubled dependent vowel sign "
          f"(e.g. ாா); surya output has it on {eng_doubled['surya']}, anuvaad on {eng_doubled['anuvaad_tesseract']}. "
          "Those characters are charged to the engine by CER.", "",
          "## Pseudo-GT re-tested with the order-invariant metric", "",
          "| τ (CER agreement) | pages | pseudo-GT char-3gram error vs real GT | best single engine on same pages | pseudo-GT BoW error |",
          "|---|---|---|---|---|"]
    for t, v in ps.items():
        L.append(f"| {t} | {v['pages']} | {v['pseudo_vs_gold_char3_median']} | {v['best_single_engine_char3_median']} | {v['pseudo_vs_gold_bow_err_median']} |")
    L += ["", "## Verdict inputs for Srujan / David",
          "- Compare CER rank with char-3gram rank: engines that rise under the order-invariant measure are being charged by CER for reading order, not recognition.",
          "- Line-matched CER was tried and discarded: block-mode engines (surya) emit paragraphs as single lines, so line pairing fails (same trap as G-B12).",
          "- Deck CER numbers stay as sealed (one-writer law) until an H-decision adopts an order-invariant metric; "
          "proposed: add flexible character accuracy (reading-order-independent CER) as a second column in the writer."]
    OUT.with_suffix(".md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[4:4 + len(rank_c3) + 2]))
    print(L[4 + len(rank_bow) + 1])
    print(ps)


if __name__ == "__main__":
    main()
