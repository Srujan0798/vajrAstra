#!/usr/bin/env python3
"""PROTO-80 — the three metrics we currently report NONE of.

For every language x engine on the benchmark scored set:
  1. mean CER with a bootstrap 95% CI (10,000 resamples, seed 20260926)
  2. substitution / deletion / insertion breakdown  (difflib opcode classes -
     LABELLED as an opcode approximation, not a true Levenshtein alignment)
  3. abstention rate (empty predictions) - because an empty prediction scores CER 1.0
Plus per-engine speed in seconds/page, measured from the `ms` field inside each pack.

READ-ONLY on all sources. Writes only level2/benchmark/scores/metrics_80.csv + stdout.
"""
import csv, json, os, sys, importlib.util, collections, statistics as st, time
import numpy as np
from difflib import SequenceMatcher

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = lambda *a: os.path.join(ROOT, *a)
BOOT = 10000
SEED = 20260926

_spec = importlib.util.spec_from_file_location("m", P("level2", "benchmark", "pipeline", "metrics.py"))
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
# the validated numpy Levenshtein (self-validates against _m.edit_distance on import)
_s2 = importlib.util.spec_from_file_location("s2", P("level2", "benchmark", "pipeline", "build_sheet_v2.py"))
_s2m = importlib.util.module_from_spec(_s2); _s2.loader.exec_module(_s2m)
np_lev = _s2m.np_lev

SDI_PER_LANG = 25   # difflib is O(n*m) - sample it, and SAY so


def sdi(ref, hyp):
    """Substitution/delete/insert counts from difflib opcodes. Approximation, tagged."""
    s = d = i = 0
    sm = SequenceMatcher(None, ref, hyp, autojunk=False)
    for tag, a1, a2, b1, b2 in sm.get_opcodes():
        if tag == "equal": continue
        elif tag == "replace":
            s += min(a2 - a1, b2 - b1)
            d += (a2 - a1) - min(a2 - a1, b2 - b1)
            i += (b2 - b1) - min(a2 - a1, b2 - b1)
        elif tag == "delete": d += a2 - a1
        elif tag == "insert": i += b2 - b1
    return s, d, i


def boot_ci(vals):
    if len(vals) < 5: return (float("nan"), float("nan"))
    rng = np.random.default_rng(SEED)
    a = np.asarray(vals, dtype=float)
    means = a[rng.integers(0, len(a), size=(BOOT, len(a)))].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def main():
    t0 = time.time()
    man = {i["image_id"]: i for i in
           json.load(open(P("level2", "benchmark", "manifest_v1.json")))["items"]}
    rows = list(csv.DictReader(open(P("level2", "benchmark", "scores", "sheet_v1.csv"))))

    # speed + per-item CER, per (engine, language)
    speed = collections.defaultdict(list)      # engine -> ms per item
    per = collections.defaultdict(lambda: collections.defaultdict(list))
    sdi_sum = collections.defaultdict(lambda: collections.Counter())
    sdi_count = collections.Counter()
    base = P("level2", "benchmark", "packs")
    for eng in sorted(os.listdir(base)):
        d = os.path.join(base, eng)
        if not os.path.isdir(d): continue
        for lang in os.listdir(d):
            ld = os.path.join(d, lang)
            if not os.path.isdir(ld): continue
            for fn in os.listdir(ld):
                if not fn.endswith(".json"): continue
                try: o = json.load(open(os.path.join(ld, fn)))
                except Exception: continue
                if o.get("ms") is not None and isinstance(o["ms"], (int, float)):
                    speed[eng].append(o["ms"])
                txt = o.get("text")
                iid = o.get("image_id") or fn[:-5]
                gt = man.get(iid, {}).get("gt")
                if txt is None or not gt: continue
                g = _m.normalize_for_scoring(gt); h = _m.normalize_for_scoring(txt)
                per[lang][eng].append(
                    _m._bound_rate(np_lev(g, h) / len(g)) if g else (0.0 if not h else 1.0))
                if sdi_count[lang] < SDI_PER_LANG:
                    sdi_count[lang] += 1
                    s, dd, ii = sdi(g, h)
                k = (lang, eng); sdi_sum[k]["S"] += s; sdi_sum[k]["D"] += dd; sdi_sum[k]["I"] += ii
                sdi_sum[k]["chars"] += len(g)

    out = P("level2", "benchmark", "scores", "metrics_80.csv")
    fh = open(out, "w", newline=""); w = csv.writer(fh)
    w.writerow(["language", "engine", "n", "mean_CER", "median_CER", "boot95_lo", "boot95_hi",
                "empty_rate", "sub_st", "del_st", "ins_st", "sdi_note"])
    print("PROTO-80 metrics — per language x engine (benchmark scored set)")
    print(f'{"lang":5}{"engine":21}{"n":>5}{"mean":>8}{"ci95":>18}{"empty":>7}{"  S/D/I per 1k chars":>22}')
    for lang in sorted(per):
        for eng in sorted(per[lang]):
            v = per[lang][eng]
            n = len(v); mn = st.mean(v); lo, hi = boot_ci(v)
            empt = sum(1 for x in v if x >= 0.999999) / n
            k = sdi_sum[(lang, eng)]; ch = max(1, k["chars"])
            sdi_disp = f'{1000*k["S"]/ch:.0f}/{1000*k["D"]/ch:.0f}/{1000*k["I"]/ch:.0f}'
            w.writerow([lang, eng, n, f"{mn:.4f}", f"{st.median(v):.4f}", f"{lo:.4f}", f"{hi:.4f}",
                        f"{empt:.3f}", k["S"], k["D"], k["I"], f"difflib-opcodes on {min(sdi_count[lang], SDI_PER_LANG)}/{n} sampled items (approximation)"])
            print(f"{lang:5}{eng:21}{n:5}{mn:8.4f}   [{lo:.3f},{hi:.3f}]{empt:7.1%}{sdi_disp:>22}")
    fh.close()

    print(f"\nSPEED (measured from the `ms` field in every pack, seconds/page)")
    print(f'  {"engine":22}{"n":>6}{"median s":>11}{"p90 s":>9}{"est. 5,344 pages":>18}')
    tot = 5344
    for eng in sorted(speed):
        v = sorted(speed[eng]); med = st.median(v) / 1000.0
        p90 = v[int(0.9 * (len(v) - 1))] / 1000.0
        print(f'  {eng:22}{len(v):6}{med:11.2f}{p90:9.2f}{med*tot/3600:15.1f} h')
    print(f"\nwrote {out}  ({time.time()-t0:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
