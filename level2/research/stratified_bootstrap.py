#!/usr/bin/env python3
"""RED (T3): does the sealed ranking survive a stratified, paired bootstrap?

    python3 level2/research/stratified_bootstrap.py

Law §14.6: sealed CIs are page-level (simple resampling). Here pages are
resampled WITH REPLACEMENT INSIDE strata = dominant_script x GT-density tercile,
all engines on the same draw (paired). Statistic = difference of median CER,
the same form as the sealed deck line (surya - anuvaad = -0.045).

Three scopes:
  all_clean   — the sealed basis (n=126, includes mixed-book Latin/Devanagari)
  clean_v2    — sealed basis minus the 26 legacy-font pages that the
                tag-based mojibake gate missed (r1_common.gt_script_mismatch);
                strata use the script the engines actually read
  own_script  — South pages in their own script only (te/ta/kn/ml, non-mixed)
  per_script  — clean_v2 split by observed script (n reported; small n flagged)
Also re-runs the simple (unstratified) bootstrap to check we reproduce the
sealed CI before trusting the stratified one.
Deterministic (seed fixed). Writes research/STRATIFIED_BOOTSTRAP.{json,md}.
"""
from __future__ import annotations

import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r1_common as C  # noqa: E402

SEED = 20260930
REPS = 2000
PAIRS = [("surya", "anuvaad_tesseract"), ("anuvaad_tesseract", "indicphotoocr"),
         ("surya", "indicphotoocr"), ("surya", "tesseract_indic"),
         ("anuvaad_tesseract", "tesseract_indic")]
OWN = {"te": "Telugu", "ta": "Tamil", "kn": "Kannada", "ml": "Malayalam"}
SMALL_N = 20
OUT = HERE / "STRATIFIED_BOOTSTRAP"


def pct(xs, q):
    s = sorted(xs)
    return s[min(len(s) - 1, max(0, int(round(q * (len(s) - 1)))))]


def density_tercile(pids):
    gl = {p: len(C.cer_norm(C.gold_raw()[p])) for p in pids}
    s = sorted(gl.values())
    t1, t2 = pct(s, 1 / 3), pct(s, 2 / 3)
    return {p: ("low" if v <= t1 else "mid" if v <= t2 else "high") for p, v in gl.items()}


def boot(pids, M, strata=None, reps=REPS, seed=SEED):
    rng = random.Random(seed)
    groups = defaultdict(list)
    for p in pids:
        groups[strata[p] if strata else "all"].append(p)
    meds = {e: [] for e in C.ENGINES}
    for _ in range(reps):
        draw = []
        for g in groups.values():
            draw.extend(rng.choice(g) for _ in g)
        for e in C.ENGINES:
            meds[e].append(median(M[p][e] for p in draw))
    point = {e: median(M[p][e] for p in pids) for e in C.ENGINES}
    eng = {e: {"median": round(point[e], 4), "ci95": [round(pct(meds[e], .025), 4),
                                                      round(pct(meds[e], .975), 4)]}
           for e in C.ENGINES}
    pairs = {}
    for a, b in PAIRS:
        d = [x - y for x, y in zip(meds[a], meds[b])]
        lo, hi = pct(d, .025), pct(d, .975)
        pairs[f"{a} - {b}"] = {"delta": round(point[a] - point[b], 4),
                               "ci95": [round(lo, 4), round(hi, 4)],
                               "p_a_better": round(sum(x < 0 for x in d) / len(d), 3),
                               "verdict": ("A better" if hi < 0 else "B better" if lo > 0 else "TIED")}
    rank = sorted(C.ENGINES, key=lambda e: (point[e], e))
    return {"n": len(pids), "strata": len(groups), "engines": eng, "pairs": pairs, "rank": rank}


def main() -> None:
    M = C.cer_matrix()
    m = C.manifest()
    clean = C.basis()["clean"]
    own = [p for p in clean if m[p]["dominant_script"] == OWN[m[p]["lang"]] and not m[p]["mixed_book_page"]]
    res = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "seed": SEED, "reps": REPS, "statistic": "difference of median CER (paired draws)"}
    dens = density_tercile(clean)
    strat = {p: f"{m[p]['dominant_script']}|{dens[p]}" for p in clean}
    res["all_clean_simple"] = boot(clean, M)
    res["all_clean_stratified"] = boot(clean, M, strat)
    dens_o = density_tercile(own)
    res["own_script_stratified"] = boot(own, M, {p: f"{m[p]['dominant_script']}|{dens_o[p]}" for p in own})
    v2 = C.basis()["clean_v2"]
    Mv2 = {p: M[p] for p in v2}
    dens_v = density_tercile(v2)
    res["clean_v2_stratified"] = boot(v2, Mv2, {p: f"{C.observed_script(p)}|{dens_v[p]}" for p in v2})
    res["clean_v2_excluded"] = C.basis()["script_mismatch"]
    res["per_script"] = {}
    by = defaultdict(list)
    for p in v2:
        by[C.observed_script(p)].append(p)
    for s, ps in sorted(by.items(), key=lambda kv: -len(kv[1])):
        res["per_script"][s] = boot(ps, M)
    C.write_json(OUT.with_suffix(".json"), res)
    write_md(res)
    s, st = res["all_clean_simple"]["pairs"], res["all_clean_stratified"]["pairs"]
    print("surya-anuvaad simple", s["surya - anuvaad_tesseract"], "\nstratified", st["surya - anuvaad_tesseract"])


def ptable(block):
    L = ["| pair | Δ median CER | 95% CI | P(A better) | verdict |", "|---|---|---|---|---|"]
    for k, v in block["pairs"].items():
        L.append(f"| {k} | {v['delta']:+.3f} | [{v['ci95'][0]:+.3f}, {v['ci95'][1]:+.3f}] | {v['p_a_better']} | **{v['verdict']}** |")
    return L


def etable(block):
    L = ["| rank | engine | median CER | 95% CI |", "|---|---|---|---|"]
    for i, e in enumerate(block["rank"], 1):
        v = block["engines"][e]
        L.append(f"| {i} | {e} | {v['median']:.3f} | [{v['ci95'][0]:.3f}, {v['ci95'][1]:.3f}] |")
    return L


def write_md(r):
    a, b, o = r["all_clean_simple"], r["all_clean_stratified"], r["own_script_stratified"]
    L = ["# STRATIFIED BOOTSTRAP — RED verdict on the sealed ranking",
         f"generated {r['generated_at']} by `research/stratified_bootstrap.py` (seed {r['seed']}, {r['reps']} paired draws; do not hand-edit)", "",
         "## 1. Reproduction check (simple page bootstrap, sealed basis)",
         f"n={a['n']}. Sealed deck line: surya−anuvaad Δ −0.045, CI [−0.086, +0.020], TIED.", ""] + ptable(a) + [
         "", f"## 2. Stratified (dominant_script × GT-density tercile, {b['strata']} strata), sealed basis n={b['n']}", ""] + ptable(b) + [
         "", f"## 3. South own-script only (te/ta/kn/ml pages in their own script, non-mixed), n={o['n']}",
         "This is the ranking the South track actually claims; the sealed basis is ~48% Latin/Devanagari mixed-book pages.", ""] + etable(o) + [""] + ptable(o) + [
         "", f"## 4. CORRECTED basis clean_v2 (n={r['clean_v2_stratified']['n']}): sealed basis minus {len(r['clean_v2_excluded'])} legacy-font pages the tag-based gate missed",
         "Excluded (PDF layer <15% Indic while >=4 of 7 independent families read Indic): " + ", ".join(r["clean_v2_excluded"]),
         "Strata = script the engines actually read × GT-density tercile.", ""] + etable(r["clean_v2_stratified"]) + [""] + ptable(r["clean_v2_stratified"]) + [
         "", "## 5. Per observed script on clean_v2 (simple bootstrap within script)", "",
         "| observed script | n | leader | leader CER | runner-up | runner-up CER | surya−anuvaad verdict | small-n |", "|---|---|---|---|---|---|---|---|"]
    for s, v in r["per_script"].items():
        l1, l2 = v["rank"][0], v["rank"][1]
        L.append(f"| {s} | {v['n']} | {l1} | {v['engines'][l1]['median']:.3f} | {l2} | {v['engines'][l2]['median']:.3f} | "
                 f"{v['pairs']['surya - anuvaad_tesseract']['verdict'] if v['n'] >= SMALL_N else '— (n<20)'} | {'YES — no deck claim' if v['n'] < SMALL_N else ''} |")
    L += ["", "Rule: a script with n < 20 carries no ranking claim in any deck/WhatsApp line; quote it only with its n."]
    OUT.with_suffix(".md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
