#!/usr/bin/env python3
"""Level-3 Sarvam 4-page gate (L3 law) — select, run, score. Standalone (L10).

    python3 level2/research/sarvam_gate.py                 # select + dry-run + score
    SARVAM_API_KEY=... python3 level2/research/sarvam_gate.py --live --confirm-spend
    python3 level2/research/sarvam_gate.py --pages all-own-script --live --confirm-spend

Selection (anti-cherry-pick, deterministic): for each of te/ta/kn/ml take the
clean-basis page (GT dense, not mojibake) written in its OWN script, not a
mixed-book page, whose surya CER is the per-language median (ties -> page_id).
Every live page is sha1-checked against pages_manifest.render_sha1 before any
upload. Live mode needs BOTH a key and --confirm-spend (H2: money is Srujan's).

Outputs (data -> out_level3/, gitignored; memo -> research/):
  level2/out_level3/sarvam_api/<lang>/<page_id>.json   pack + meta
  level2/out_level3/sarvam_api/<lang>/<page_id>.raw.zip raw API payload
  level2/research/LEVEL3_SARVAM_GATE.json / .md

The gate is a HARNESS gate (n=4 cannot rank engines): PASS = every page returned
non-empty own-script text, no unparsed payload, correct language parameter.
Firewall: Sarvam output is a referee, never training food.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r1_common as C  # noqa: E402

from engines import REGISTRY  # noqa: E402  (r1_common put level2/ on sys.path)
from engines.sarvam_api import DRY_RUN_TEXT, PRICE_INR_PER_PAGE  # noqa: E402

LANGS = ("te", "ta", "kn", "ml")
OWN_SCRIPT = {"te": "Telugu", "ta": "Tamil", "kn": "Kannada", "ml": "Malayalam"}
RENDERS = C.L2 / "renders_shared"
OUT3 = C.L2 / "out_level3" / "sarvam_api"
MEMO = HERE / "LEVEL3_SARVAM_GATE"


def own_script_clean() -> dict[str, list[str]]:
    m = C.manifest()
    by: dict[str, list[str]] = {l: [] for l in LANGS}
    for pid in C.basis()["clean"]:
        e = m[pid]
        if e["dominant_script"] == OWN_SCRIPT[e["lang"]] and not e["mixed_book_page"]:
            by[e["lang"]].append(pid)
    return by


def select_gate() -> list[str]:
    M = C.cer_matrix()
    picks = []
    for lang, pids in own_script_clean().items():
        if not pids:
            raise SystemExit(f"no own-script clean page for {lang}")
        med = median(M[p]["surya"] for p in pids)
        picks.append(min(pids, key=lambda p: (abs(M[p]["surya"] - med), p)))
    return picks


def indic_share(text: str, script: str) -> float:
    lo, hi = V_RANGES[script]
    s = "".join(text.split())
    return sum(1 for c in s if lo <= ord(c) <= hi) / len(s) if s else 0.0


V_RANGES = C.V.SCRIPT_RANGES


def run_pages(pids: list[str], live: bool) -> dict[str, dict]:
    eng = REGISTRY["sarvam_api"]
    if live and eng.dry_run:
        raise SystemExit("--live given but SARVAM_API_KEY is not set")
    m = C.manifest()
    res: dict[str, dict] = {}
    for pid in pids:
        png = RENDERS / f"{pid}.png"
        rec = {"page_id": pid, "lang": m[pid]["lang"], "mode": "live" if live else "dry_run"}
        if live:
            if not png.exists():
                raise SystemExit(f"render missing: {png} (run on the full tree)")
            sha = hashlib.sha1(png.read_bytes()).hexdigest()
            if sha != m[pid]["render_sha1"]:
                raise SystemExit(f"{pid}: render sha1 {sha} != manifest {m[pid]['render_sha1']}")
        t0 = time.monotonic()
        try:
            text = eng.run(png)
            rec["error"] = eng.last_meta.get("error")
        except Exception as exc:  # recorded, gate fails, run continues
            text, rec["error"] = "", f"{type(exc).__name__}: {exc}"
        rec["ms"] = int((time.monotonic() - t0) * 1000)
        rec["meta"] = dict(eng.last_meta)
        rec["text"] = text
        if live:
            d = OUT3 / rec["lang"]
            d.mkdir(parents=True, exist_ok=True)
            if eng.last_raw:
                (d / f"{pid}.raw.zip").write_bytes(eng.last_raw)
            pack = {"page_id": pid, "lang": rec["lang"], "ocr_engine": "sarvam_api",
                    "regions": [{"region_id": "r1", "cls": "paragraph", "text": text}],
                    "engine_meta": {"engine": "sarvam_api", "version": eng.version,
                                    "lang_param": rec["meta"].get("lang_param"),
                                    "mixed_book_page": rec["meta"].get("mixed_book_page"),
                                    "job_id": rec["meta"].get("job_id"),
                                    "error": rec["error"]}}
            C.write_json(d / f"{pid}.json", pack)
        res[pid] = rec
    return res


def score(res: dict[str, dict]) -> dict:
    M = C.cer_matrix()
    m = C.manifest()
    rows, ok = [], True
    for pid, rec in res.items():
        live = rec["mode"] == "live"
        text = rec["text"]
        script = m[pid]["dominant_script"]
        s_cer = None
        checks = {}
        if live:
            gtn = C.cer_norm(C.gold_raw()[pid])
            s_cer = (round(C.edit_distance(C.cer_norm(text), gtn) / len(gtn), 4)
                     if text.strip() else 1.0)
            checks = {"nonempty": bool(text.strip()),
                      "own_script_ge_50pct": indic_share(text, script) >= 0.5,
                      "no_parse_error": rec["error"] is None,
                      "lang_param_ok": rec["meta"].get("lang_param") == f"{rec['lang']}-IN"}
            ok &= all(checks.values())
        else:
            checks = {"dry_run_labeled": text == DRY_RUN_TEXT}
            ok &= checks["dry_run_labeled"]
        best = min(C.ENGINES, key=lambda e: (M[pid][e], e))
        rows.append({"page_id": pid, "lang": rec["lang"], "script": script,
                     "gt_chars": len(C.cer_norm(C.gold_raw()[pid])),
                     "sarvam_cer": s_cer, "surya_cer": M[pid]["surya"],
                     "anuvaad_cer": M[pid]["anuvaad_tesseract"],
                     "best_free": best, "best_free_cer": M[pid][best],
                     "ms": rec["ms"], "checks": checks, "error": rec["error"]})
    return {"rows": rows, "pass": ok}


def write_memo(pids, res, sc, live: bool) -> None:
    pool = {l: len(v) for l, v in own_script_clean().items()}
    n = len(pids)
    obj = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "mode": "live" if live else "dry_run", "pages": pids,
           "own_script_clean_pool": pool, "estimated_cost_inr": n * PRICE_INR_PER_PAGE,
           "gate_pass": sc["pass"], "rows": sc["rows"]}
    C.write_json(MEMO.with_suffix(".json"), obj)
    L = [f"# LEVEL-3 SARVAM GATE — {obj['mode'].upper()}",
         f"generated {obj['generated_at']} by `research/sarvam_gate.py` (do not hand-edit)", "",
         f"**Gate verdict: {'PASS' if sc['pass'] else 'FAIL'}** "
         f"({'harness check only — n=' + str(n) + ' cannot rank engines' if live else 'dry-run: zero network, zero cost; proves selection + harness wiring only'})",
         "", f"Selection: own-script, non-mixed, clean-basis page at the per-language median surya CER. "
         f"Pool sizes (own-script clean pages): {pool}. Cost for these pages: ₹{obj['estimated_cost_inr']:.1f}.", "",
         "| page | lang | GT chars | Sarvam CER | surya | anuvaad | best free (CER) | ms | checks |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in sc["rows"]:
        ck = " ".join(f"{k}={'Y' if v else 'N'}" for k, v in r["checks"].items())
        s = "—" if r["sarvam_cer"] is None else f"{r['sarvam_cer']:.3f}"
        L.append(f"| {r['page_id']} | {r['lang']} | {r['gt_chars']} | {s} | {r['surya_cer']:.3f} | "
                 f"{r['anuvaad_cer']:.3f} | {r['best_free']} ({r['best_free_cer']:.3f}) | {r['ms']} | {ck} |")
    L += ["", "Next: on PASS + operator spend OK, run `--pages all-own-script --live --confirm-spend` "
          f"({sum(pool.values())} scorable own-script pages ≈ ₹{sum(pool.values()) * PRICE_INR_PER_PAGE:.0f}); "
          "the full 400 (≈ ₹200) adds capture/agreement data but no extra CER basis.",
          "Firewall: Sarvam output is a referee, never training food."]
    MEMO.with_suffix(".md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--confirm-spend", action="store_true")
    ap.add_argument("--pages", default="gate", choices=["gate", "all-own-script"])
    a = ap.parse_args()
    if a.live and not a.confirm_spend:
        raise SystemExit("--live needs --confirm-spend (H2: Srujan approves money)")
    if not a.live and os.environ.get("SARVAM_API_KEY"):
        os.environ.pop("SARVAM_API_KEY")  # dry-run means dry-run
        REGISTRY["sarvam_api"].dry_run = True
    pids = select_gate() if a.pages == "gate" else sorted(p for v in own_script_clean().values() for p in v)
    res = run_pages(pids, a.live)
    sc = score(res)
    write_memo(pids, res, sc, a.live)
    print(f"{'LIVE' if a.live else 'DRY-RUN'} {len(pids)} pages {pids if len(pids) <= 8 else ''} "
          f"-> gate {'PASS' if sc['pass'] else 'FAIL'}; memo {MEMO.with_suffix('.md').relative_to(C.L2)}")
    sys.exit(0 if sc["pass"] else 1)


if __name__ == "__main__":
    main()
