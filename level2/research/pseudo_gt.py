#!/usr/bin/env python3
"""A2 lane 1 (T2): can cross-engine agreement serve as pseudo-GT? Tested against real GT.

    python3 level2/research/pseudo_gt.py

Method (L6 family = 1 vote; L7 no invented GT — pseudo-GT is LABELED PSEUDO):
- one representative per independent family (7), text = cer_norm(pack text)
- d(a,b) = edit_distance / max(len) between family outputs
- medoid = family output with the smallest summed distance to the others
- support(tau) = families (incl. medoid) within d <= tau of the medoid
- pseudo-GT(tau, k) exists iff support >= k; its text is the medoid output
Validation on clean_v2 (pages WITH trustworthy PDF-layer GT):
- accuracy: CER(medoid vs gold) for qualifying pages, per tau
- circularity: an engine is scored against a LEAVE-ITS-FAMILY-OUT medoid;
  engine ranking vs pseudo-GT is compared with ranking vs gold (Spearman rho)
Application: count qualifying pages among the pages that have NO usable GT.
Writes research/PSEUDO_GT.{json,md} and research/_pseudo_cache.json (agreement per page).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r1_common as C  # noqa: E402

TAUS = (0.10, 0.20, 0.30, 0.40)
K = 3
CACHE = HERE / "_pseudo_cache.json"
OUT = HERE / "PSEUDO_GT"


def dist(a: str, b: str) -> float:
    if not a and not b:
        return 0.0
    return C.edit_distance(a, b) / max(len(a), len(b))


def page_agreement(pid: str) -> dict:
    texts = {e: C.cer_norm(C.engine_text(e, pid)) for e in C.FAMILY_REPS}
    live = [e for e, t in texts.items() if len(t) >= 20]
    D = {}
    for a, b in combinations(live, 2):
        D[a, b] = D[b, a] = dist(texts[a], texts[b])
    return {"live": live, "D": {f"{a}|{b}": round(v, 4) for (a, b), v in D.items()},
            "chars": {e: len(texts[e]) for e in live}}


def load_all() -> dict[str, dict]:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    res = {pid: page_agreement(pid) for pid in C.manifest()}
    CACHE.write_text(json.dumps(res, ensure_ascii=False) + "\n", encoding="utf-8")
    return res


def medoid(ag: dict, exclude: frozenset = frozenset()):
    live = [e for e in ag["live"] if e not in exclude]
    if len(live) < 2:
        return None, 0.0, {}
    d = lambda a, b: ag["D"][f"{a}|{b}"]  # noqa: E731
    med = min(live, key=lambda a: (sum(d(a, b) for b in live if b != a), a))
    to_med = {b: (0.0 if b == med else d(med, b)) for b in live}
    return med, None, to_med


def pseudo(ag: dict, tau: float, exclude=frozenset()):
    med, _, to_med = medoid(ag, exclude)
    if med is None:
        return None
    support = sum(1 for v in to_med.values() if v <= tau)
    return med if support >= K else None


def spearman(x: list[float], y: list[float]) -> float:
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for pos, i in enumerate(order):
            r[i] = pos
        return r
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    return round(1 - 6 * sum((a - b) ** 2 for a, b in zip(rx, ry)) / (n * (n * n - 1)), 3)


def main() -> None:
    A = load_all()
    b = C.basis()
    v2 = b["clean_v2"]
    no_gt = sorted(set(C.manifest()) - set(v2))
    res = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "k": K,
           "validation_pages": len(v2), "no_gt_pages": len(no_gt), "by_tau": {}}
    for tau in TAUS:
        q = [p for p in v2 if pseudo(A[p], tau)]
        cers = []
        for p in q:
            med = pseudo(A[p], tau)
            gtn = C.cer_norm(C.gold_raw()[p])
            cers.append(round(C.edit_distance(C.cer_norm(C.engine_text(med, p)), gtn) / len(gtn), 4))
        # circularity: score every engine vs leave-its-family-out pseudo-GT on q pages
        eng_pseudo, eng_gold = {}, {}
        for e in C.ENGINES:
            rep = next(r for r in C.FAMILY_REPS if C.family_of(r) == C.family_of(e))
            ps, gs = [], []
            for p in q:
                med = pseudo(A[p], tau, frozenset({rep}))
                if not med:
                    continue
                ref = C.cer_norm(C.engine_text(med, p))
                et = C.cer_norm(C.engine_text(e, p))
                ps.append(C.edit_distance(et, ref) / len(ref) if et else 1.0)
                gs.append(C.cer(e, p))
            if ps:
                eng_pseudo[e], eng_gold[e] = median(ps), median(gs)
        es = sorted(eng_pseudo)
        rho = spearman([eng_pseudo[e] for e in es], [eng_gold[e] for e in es]) if len(es) > 2 else None
        top_p = sorted(es, key=lambda e: eng_pseudo[e])[:3]
        top_g = sorted(es, key=lambda e: eng_gold[e])[:3]
        gain = [p for p in no_gt if pseudo(A[p], tau)]
        res["by_tau"][str(tau)] = {
            "qualifying_validation_pages": len(q),
            "coverage": round(len(q) / len(v2), 3),
            "pseudo_vs_gold_cer_median": round(median(cers), 4) if cers else None,
            "pseudo_vs_gold_cer_p90": round(sorted(cers)[int(0.9 * (len(cers) - 1))], 4) if cers else None,
            "engine_rank_spearman_vs_gold": rho,
            "top3_pseudo": top_p, "top3_gold": top_g,
            "extra_pages_without_gt": len(gain),
            "extra_pages_by_lang": {l: sum(1 for p in gain if p.startswith(l)) for l in ("te", "ta", "kn", "ml")},
        }
    C.write_json(OUT.with_suffix(".json"), res)
    write_md(res)
    for t, v in res["by_tau"].items():
        print(t, {k: v[k] for k in ("qualifying_validation_pages", "pseudo_vs_gold_cer_median",
                                    "pseudo_vs_gold_cer_p90", "engine_rank_spearman_vs_gold", "extra_pages_without_gt")})


def write_md(r):
    L = ["# PSEUDO-GT TEST — does engine agreement give usable ground truth?",
         f"generated {r['generated_at']} by `research/pseudo_gt.py` (do not hand-edit)", "",
         f"Validated on the {r['validation_pages']} clean_v2 pages that HAVE trustworthy PDF-layer GT. "
         f"Pseudo-GT = medoid output of 7 independent families, required support k={r['k']} families within distance τ. "
         "Circularity guard: every engine is scored against a pseudo-GT built WITHOUT its own family.", "",
         "| τ | pages qualifying (coverage) | pseudo-GT CER vs real GT (median / p90) | engine-rank Spearman vs real GT | top-3 by pseudo | top-3 by real GT | extra pages among no-GT pages (te/ta/kn/ml) |",
         "|---|---|---|---|---|---|---|"]
    for t, v in r["by_tau"].items():
        L.append(f"| {t} | {v['qualifying_validation_pages']} ({v['coverage']:.0%}) | "
                 f"{v['pseudo_vs_gold_cer_median']} / {v['pseudo_vs_gold_cer_p90']} | {v['engine_rank_spearman_vs_gold']} | "
                 f"{', '.join(v['top3_pseudo'])} | {', '.join(v['top3_gold'])} | {v['extra_pages_without_gt']} "
                 f"({'/'.join(str(v['extra_pages_by_lang'][l]) for l in ('te', 'ta', 'kn', 'ml'))}) |")
    L += ["", "## Reading this table",
          "- A pseudo-GT is only as good as its CER vs real GT: a median of 0.2 means the 'reference' itself is ~20% wrong, "
          "so it cannot separate engines whose real CERs differ by less than that (tier-1 differs by ~0.03).",
          "- Spearman vs real GT tells whether pseudo-GT would reproduce the true engine order; top-3 tells whether it finds the right leaders.",
          "- Rule (L7): pseudo-GT pages are labeled PSEUDO, never gold, never merged into CER_STAGE3B, and never used to rank "
          "an engine whose family contributed to them. Useful role: coarse tiering and triage, not tier-1 ranking."]
    OUT.with_suffix(".md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
