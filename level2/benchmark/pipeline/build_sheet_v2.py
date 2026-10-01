#!/usr/bin/env python3
"""PROTO-61 — independent rebuild of the score sheet.

sheet.csv has no generator on disk and was never committed. This recomputes CER for
every row from the only reproducible inputs:
    gt  : level2/benchmark/manifest_v1.json  (item `gt`)
    pred: level2/benchmark/packs/<engine>/<lang>/<image_id>.json  (field `text`)
with the repo's own normalisation (metrics.normalize_for_scoring) and its BOUNDED rate
(metrics._bound_rate), so the only thing that changes vs the stored column is the
edit-distance *implementation*.

metrics.edit_distance is O(n*m) pure Python (no `Levenshtein` package on this machine),
which is ~14M inner steps per 3.7k-char row. This file adds a numpy anti-diagonal
Levenshtein, VALIDATED against metrics.edit_distance at startup (default 24 rows,
hard-fail on any mismatch), so the comparison stays a comparison of *data*, not of code.
"""
import csv, json, os, sys, time, importlib.util, collections, statistics as st
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = lambda *a: os.path.join(ROOT, *a)

_spec = importlib.util.spec_from_file_location("m", P("level2", "benchmark", "pipeline", "metrics.py"))
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)


def np_lev(a: str, b: str) -> int:
    """Exact Levenshtein, row-vectorised.

    Row recurrence is cur[j] = min(prev[j-1]+sub, prev[j]+1, cur[j-1]+1). The third
    term makes it sequential, but with M[j] = min(prev[j-1]+sub, prev[j]+1) and
    cur[j] = min_{k<=j} (M[k] + (j-k)), which is a prefix minimum:
        P[j] = M[j] - j ; Q = minimum.accumulate(P) ; cur[j] = Q[j] + j
    Validated at startup against metrics.edit_distance; the run aborts on any mismatch.
    """
    n, m = len(a), len(b)
    if n == 0: return m
    if m == 0: return n
    if n > m:                       # keep the row vector short
        a, b, n, m = b, a, m, n
    A = np.frombuffer(a.encode("utf-32-le"), dtype=np.uint32)
    B = np.frombuffer(b.encode("utf-32-le"), dtype=np.uint32)
    prev = np.arange(m + 1, dtype=np.int64)          # dp[0][j]
    j1 = np.arange(1, m + 1, dtype=np.int64)
    for i in range(1, n + 1):
        sub = (A[i - 1] != B).astype(np.int64)       # cost vs each column
        M = np.minimum(prev[:-1] + sub, prev[1:] + 1)
        cur = np.empty(m + 1, dtype=np.int64)
        cur[0] = i
        cur[1:] = np.minimum.accumulate(M - j1) + j1
        prev = cur
    return int(prev[m])


def validate(n=24):
    rows = list(csv.DictReader(open(P("level2", "benchmark", "scores", "sheet_v1.csv"))))
    man = {i["image_id"]: i for i in
           json.load(open(P("level2", "benchmark", "manifest_v1.json")))["items"]}
    import random
    random.seed(20260926)
    bad = 0
    for r in random.sample(rows, n):
        gt = man.get(r["image_id"], {}).get("gt")
        if not gt: continue
        # short prefix keeps metrics.edit_distance fast for the cross-check
        g = _m.normalize_for_scoring(gt)[:600]
        h = _m.normalize_for_scoring(r["prediction"])[:600]
        if _m.edit_distance(list(g), list(h)) != np_lev(g, h):
            bad += 1
    if bad:
        print(f"VALIDATION FAILED: numpy levenshtein disagrees with metrics.edit_distance "
              f"on {bad}/{n} rows - refusing to report.")
        sys.exit(2)
    print(f"validation OK: numpy levenshtein == metrics.edit_distance on {n} rows")


def main():
    validate()
    t0 = time.time()
    man = {i["image_id"]: i for i in
           json.load(open(P("level2", "benchmark", "manifest_v1.json")))["items"]}
    base = P("level2", "benchmark", "packs")
    packs = collections.defaultdict(lambda: collections.defaultdict(dict))
    for eng in sorted(os.listdir(base)):
        d = os.path.join(base, eng)
        if not os.path.isdir(d): continue
        for lang in os.listdir(d):
            ld = os.path.join(d, lang)
            if not os.path.isdir(ld): continue
            for fn in os.listdir(ld):
                if not fn.endswith(".json"): continue
                try:
                    o = json.load(open(os.path.join(ld, fn)))
                except Exception:
                    continue
                if o.get("text") is not None:
                    packs[eng][lang][o.get("image_id") or fn[:-5]] = o["text"]

    rows = list(csv.DictReader(open(P("level2", "benchmark", "scores", "sheet_v1.csv"))))
    outp = P("level2", "benchmark", "scores", "sheet_v2.csv")
    T = collections.Counter(); per = collections.defaultdict(collections.Counter)
    fh = open(outp, "w", newline=""); w = csv.writer(fh)
    w.writerow(["image_id", "language", "model", "stored_CER", "recomputed_CER",
                "delta", "status", "gt_len", "pred_len"])
    for k, r in enumerate(rows):
        lang, iid, mod = r["language"], r["image_id"], r["model"]
        stored = float(r["CER"])
        gt = man.get(iid, {}).get("gt")
        pred = packs.get(mod, {}).get(lang, {}).get(iid)
        if gt is None or pred is None:
            w.writerow([iid, lang, mod, f"{stored:.6f}", "", "", "no_recompute_input",
                        len(gt or ""), len(pred or "")])
            T["norec"] += 1; continue
        g = _m.normalize_for_scoring(gt); h = _m.normalize_for_scoring(pred)
        rec = _m._bound_rate(np_lev(g, h) / max(1, len(g))) if g else (0.0 if not h else 1.0)
        d = rec - stored
        st_ = "exact" if abs(d) < 1e-9 else ("near" if abs(d) < 1e-4 else "MISMATCH")
        T["n"] += 1; T[{"exact": "exact", "near": "near", "MISMATCH": "mis"}[st_]] += 1
        per[mod][st_] += 1; per[mod]["n"] += 1
        w.writerow([iid, lang, mod, f"{stored:.6f}", f"{rec:.6f}", f"{d:+.6f}", st_,
                    len(g), len(h)])
        if (k + 1) % 2000 == 0:
            print(f"  ...{k+1}/{len(rows)} rows  ({time.time()-t0:.0f}s)", flush=True)
    fh.close()
    n = max(T["n"], 1)
    print(f"\nREBUILT {len(rows)} rows -> level2/benchmark/scores/sheet_v2.csv  ({time.time()-t0:.0f}s)")
    print(f"  recomputed {T['n']} · exact {T['exact']} ({100*T['exact']/n:.1f}%) · "
          f"within-1e-4 {T['exact']+T['near']} ({100*(T['exact']+T['near'])/n:.1f}%) · "
          f"MISMATCH {T['mis']} ({100*T['mis']/n:.1f}%) · no-input {T['norec']}")
    print(f'  {"model":22}{"rows":>6}{"exact":>7}{"near":>7}{"MISMATCH":>10}')
    for mod in sorted(per):
        c = per[mod]
        print(f'  {mod:22}{c["n"]:6}{c["exact"]:7}{c["near"]:7}{c["MISMATCH"]:10}')


if __name__ == "__main__":
    main()
