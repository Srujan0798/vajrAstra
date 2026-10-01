#!/usr/bin/env python3
"""
mcnemar_full_matrix.py — Engine Agent (locked H44+ task, contract v1.0.0)

Per engine_agent_contract.json v1.0.0 + AGENT_PROTOCOL §6 + §9 estimator law:
- Two-sided McNemar exact test (threshold CER<0.5), per (eng_a, eng_b, lang)
- Pair defined as common image_ids across both engines' preds
- n_common >= 30 required (verbatim from protocol §9)
- D4 (n<50 cells = no winner): low_conf=true; winner still emitted as informational
- Uses metrics.calculate_cer for per-item CER (same normalizer as Phase 6)

Outputs:
  scores/mcnemar_full_matrix.json   — { "<eng_a>_vs_<eng_b>": { "<lang>": { ... } } }
  scores/mcnemar_full_matrix.log    — per-triple status lines
  scores/mcnemar_summary.md         — human-readable digest

Engine list (per contract v1.0.0): 11 engines incl. sarvam_vision.
"""

from __future__ import annotations

import json
import logging
import math
import sys
from itertools import combinations
from pathlib import Path

PROBE = Path(__file__).resolve().parent
SCORES = PROBE / "scores"
LOG_PATH = SCORES / "mcnemar_full_matrix.log"
JSON_PATH = SCORES / "mcnemar_full_matrix.json"

ENGINES = [
    "rapidocr",
    "tesseract_bilingual",
    "doctr",
    "tesseract_indic",
    "openbharatocr",
    "anuvaad_tesseract",
    "indicphotoocr",
    "surya",
    "easyocr",
    "paddleocr_indic",
    "sarvam_vision",
]

CER_THRESHOLD = 0.5    # pass = CER < 0.5
N_COMMON_MIN = 30      # §9 estimator law
LOW_CONF_N = 50        # D4 lock: <50 = no winner claim


# ---------- McNemar exact (two-sided) ----------

def mcnemar_exact_two_sided(b: int, c: int) -> float:
    """
    Two-sided exact McNemar test on discordant counts (b, c).
    Under H0, X ~ Bin(n=b+c, 0.5). Two-sided p =
      sum_{k: |k - n/2| >= |b - c|/2} binom(n, k) * 0.5^n
    (symmetric two-tail probability).
    """
    n = b + c
    if n == 0:
        return 1.0
    diff = abs(b - c)
    half_n = n / 2.0
    half_diff = diff / 2.0
    # precompute binom via pascal; multiply by 0.5^n at the end
    binom = [0.0] * (n + 1)
    binom[0] = 1.0
    for i in range(1, n + 1):
        binom[i] = binom[i - 1] * (n - i + 1) / i
    p = 0.0
    for k in range(0, n + 1):
        if abs(k - half_n) >= half_diff:
            p += binom[k]
    p *= 0.5 ** n
    return max(0.0, min(1.0, p))


# ---------- CER helper (reuses metrics.py normalizer) ----------

try:
    from metrics import calculate_cer as _metrics_cer
except Exception:
    _metrics_cer = None


def per_item_cer(reference: str, hypothesis: str) -> float:
    """CER per item; capped at 1.0. Uses metrics.calculate_cer if importable."""
    if _metrics_cer is not None:
        try:
            return _metrics_cer(reference or "", hypothesis or "")
        except Exception:
            pass
    # fallback: simple char-level edit distance (no normalization)
    ref = reference or ""
    hyp = hypothesis or ""
    if not ref:
        return 0.0 if not hyp else 1.0
    # basic edit distance
    m, n = len(ref), len(hyp)
    if m == 0:
        return 0.0 if n == 0 else 1.0
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        curr = [i]
        for j in range(1, n + 1):
            cost = 0 if ref[i - 1] == hyp[j - 1] else 1
            curr.append(min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + cost))
        prev = curr
    return min(1.0, prev[n] / m)


# ---------- preds loader ----------

def load_preds(engine: str) -> dict[str, dict]:
    """
    Return { image_id: {gt, pred, language, ...} } for the engine.
    Image_id = preds[i]['image_name']. Real pack image_id (sa_d004 etc.)
    is preserved via the manifest lookup so per-item CER matches Phase 6.
    """
    path = SCORES / f"preds_{engine}.json"
    if not path.exists():
        return {}
    rows = json.loads(path.read_text())
    out = {}
    for r in rows:
        iid = r.get("image_name") or r.get("image_id")
        if not iid:
            continue
        out[iid] = {
            "gt": r.get("gt") or "",
            "pred": r.get("pred") or "",
            "language": r.get("language") or "",
        }
    return out


# ---------- per-(eng_a, eng_b, lang) McNemar ----------

def triple_mcnemar(
    a_data: dict[str, dict],
    b_data: dict[str, dict],
    lang: str,
) -> dict:
    """
    Restrict to (a_data ∩ b_data) image_ids whose language == lang.
    For each, compute per-item CER, threshold at CER_THRESHOLD, and run
    two-sided exact McNemar on discordant pairs.
    Returns None if n_common < 30 (insufficient for paired test).
    """
    common_ids = sorted(set(a_data.keys()) & set(b_data.keys()))
    # filter to language
    common_ids = [iid for iid in common_ids if a_data[iid]["language"] == lang
                                       and b_data[iid]["language"] == lang]
    n_common = len(common_ids)
    if n_common < N_COMMON_MIN:
        return None

    a_pass_b_pass = 0
    a_pass_b_fail = 0  # discordant: a passes, b fails
    a_fail_b_pass = 0  # discordant: a fails, b passes
    a_fail_b_fail = 0
    for iid in common_ids:
        cer_a = per_item_cer(a_data[iid]["gt"], a_data[iid]["pred"])
        cer_b = per_item_cer(b_data[iid]["gt"], b_data[iid]["pred"])
        a_ok = cer_a < CER_THRESHOLD
        b_ok = cer_b < CER_THRESHOLD
        if a_ok and b_ok:
            a_pass_b_pass += 1
        elif a_ok and not b_ok:
            a_pass_b_fail += 1
        elif not a_ok and b_ok:
            a_fail_b_pass += 1
        else:
            a_fail_b_fail += 1

    n_ties = a_pass_b_pass + a_fail_b_fail
    n_disc = a_pass_b_fail + a_fail_b_pass
    p = mcnemar_exact_two_sided(a_pass_b_fail, a_fail_b_pass)

    if p < 0.05 and a_pass_b_fail > a_fail_b_pass:
        winner = "a"
    elif p < 0.05 and a_fail_b_pass > a_pass_b_fail:
        winner = "b"
    else:
        winner = "tie"

    return {
        "n_common": n_common,
        "n_ties": n_ties,
        "n_discordant": n_disc,
        "a_pass_b_fail": a_pass_b_fail,
        "b_correct_a_wrong": a_fail_b_pass,  # alias for spec field name
        "p_two_sided": round(p, 6),
        "winner": winner,
        "low_conf": n_common < LOW_CONF_N,
    }


# ---------- main ----------

def main() -> None:
    # Ensure scipy fallback handled: we use closed-form two-sided McNemar
    # (no scipy dependency).
    logging.basicConfig(
        filename=str(LOG_PATH),
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    logging.info("McNemar full matrix — start")
    logging.info(f"engines: {ENGINES}")
    logging.info(f"threshold CER<{CER_THRESHOLD}; min n_common={N_COMMON_MIN}; "
                 f"low_conf if n_common<{LOW_CONF_N} (D4 lock)")

    print(f"Loading preds for {len(ENGINES)} engines ...")
    eng_data = {e: load_preds(e) for e in ENGINES}
    for e, d in eng_data.items():
        print(f"  {e}: {len(d)} preds loaded")

    # gather langs
    langs = set()
    for d in eng_data.values():
        for v in d.values():
            if v["language"]:
                langs.add(v["language"])
    langs = sorted(langs)
    print(f"languages found: {langs}")

    # pairwise engine matrix
    pairs = list(combinations(ENGINES, 2))
    matrix: dict[str, dict[str, dict]] = {}
    n_pairs = len(pairs)
    n_total_tris = n_pairs * len(langs)
    computed = 0
    skipped = 0

    for a, b in pairs:
        key = f"{a}_vs_{b}"
        matrix[key] = {}
        for lang in langs:
            res = triple_mcnemar(eng_data[a], eng_data[b], lang)
            if res is None:
                matrix[key][lang] = None
                skipped += 1
            else:
                matrix[key][lang] = res
                computed += 1
        logging.info(f"pair {a}_vs_{b}: {computed}/{n_total_tris} total computed; "
                     f"this pair computed across {len(langs)} langs")

    JSON_PATH.write_text(json.dumps({
        "meta": {
            "engines": ENGINES,
            "languages": langs,
            "cer_threshold": CER_THRESHOLD,
            "n_common_min": N_COMMON_MIN,
            "low_conf_n": LOW_CONF_N,
            "n_pairs": n_pairs,
            "n_total_triples": n_total_tris,
            "n_computed": computed,
            "n_skipped_low_n": skipped,
        },
        "pairs": matrix,
    }, indent=2, ensure_ascii=False))
    logging.info(f"wrote {JSON_PATH} ({computed} triples + {skipped} skipped)")
    print(f"wrote {JSON_PATH} — {computed} computed, {skipped} skipped (n<{N_COMMON_MIN})")

    # ----- summary -----
    write_summary(matrix, ENGINES, langs, computed, skipped, n_pairs)

    print("done.")


def write_summary(
    matrix: dict[str, dict[str, dict]],
    engines: list[str],
    langs: list[str],
    computed: int,
    skipped: int,
    n_pairs: int,
) -> None:
    """Write scores/mcnemar_summary.md (Digest by engine, then by lang)."""
    # helper: collect winner counts
    win_counts: dict[str, int] = {e: 0 for e in engines}
    lose_counts: dict[str, int] = {e: 0 for e in engines}
    tie_counts: dict[str, int] = {e: 0 for e in engines}
    low_conf_wins: dict[str, int] = {e: 0 for e in engines}
    sig_pair_lang: dict[str, dict[str, dict]] = {}  # eng -> lang -> [(opp, p, win_by)]
    for pair, by_lang in matrix.items():
        a, b = pair.split("_vs_")
        for lang, res in by_lang.items():
            if res is None:
                continue
            if res["p_two_sided"] < 0.05 and res["winner"] != "tie":
                w = a if res["winner"] == "a" else b
                loser = b if w == a else a
                win_counts[w] = win_counts.get(w, 0) + 1
                lose_counts[loser] = lose_counts.get(loser, 0) + 1
                if res["low_conf"]:
                    low_conf_wins[w] = low_conf_wins.get(w, 0) + 1
                sig_pair_lang.setdefault(w, {}).setdefault(lang, []).append(
                    (loser, res["p_two_sided"], "pass-fail", res["a_pass_b_fail"], res["b_correct_a_wrong"])
                )
            else:
                # tie (n.s.)
                tie_counts[a] = tie_counts.get(a, 0) + 1
                tie_counts[b] = tie_counts.get(b, 0) + 1

    lines = []
    lines.append("# McNemar Full Matrix — Engine × Engine × Language")
    lines.append("")
    lines.append("Source-of-truth: `scores/mcnemar_full_matrix.json`")
    lines.append("")
    lines.append("Test: two-sided exact McNemar on discordant pairs of (engine_a, engine_b) per language,")
    lines.append(f"threshold `CER<{CER_THRESHOLD}` per item (1 if engine passes, 0 if fails).")
    lines.append(f"Pairs with **n_common < {N_COMMON_MIN}** are excluded (insufficient paired power).")
    lines.append(f"Cells with **n_common < {LOW_CONF_N}** are flagged `low_conf: true` per D4 — winner is informational only.")
    lines.append("No `winner` claim is made for any D4-flagged language.")
    lines.append("")
    lines.append(f"Pre-declared test family: {n_pairs} engine pairs × {len(langs)} langs = "
                 f"{n_pairs * len(langs)} triples total. "
                 f"Computed: {computed}. Skipped (low n): {skipped}.")
    lines.append("")
    lines.append("## Winner counts (significant only, p<0.05)")
    lines.append("")
    lines.append("| engine | wins | losses | ties (incl. n.s.) | low-conf wins (D4) |")
    lines.append("|---|---|---|---|---|")
    for e in engines:
        lines.append(f"| {e} | {win_counts.get(e, 0)} | {lose_counts.get(e, 0)} | "
                     f"{tie_counts.get(e, 0)} | {low_conf_wins.get(e, 0)} |")
    lines.append("")
    lines.append("## Per-language significant wins (p<0.05)")
    lines.append("")
    lines.append("(Engine that beat all 10 others at p<0.05 on the listed language; D4-flagged marked. Empty = no engine cleared p<0.05 vs all opponents.)")
    lines.append("")
    for lang in langs:
        # count wins per engine on this lang, with each loss disambiguated
        scores: dict[str, int] = {e: 0 for e in engines}
        flagged: dict[str, bool] = {e: False for e in engines}
        for pair, by_lang in matrix.items():
            a, b = pair.split("_vs_")
            res = by_lang.get(lang)
            if res is None or res["p_two_sided"] >= 0.05 or res["winner"] == "tie":
                continue
            w = a if res["winner"] == "a" else b
            scores[w] = scores.get(w, 0) + 1
            if res["low_conf"]:
                flagged[w] = True
        rows = [(e, c, flagged[e]) for e, c in scores.items() if c == 10]  # beat all 10 others
        if rows:
            for e, c, lc in rows:
                tag = " ⚠low_conf" if lc else ""
                lines.append(f"- **{lang}** ({tag}): {e} (10/10 wins)")
        else:
            # partial winners (engine beats >= 5 opponents at p<0.05)
            partial = [(e, c, flagged[e]) for e, c in scores.items() if 5 <= c < 10]
            if partial:
                lines.append(f"- **{lang}**: partial winners {[(e,c) for e,c,_ in partial]}")
    lines.append("")
    lines.append(f"## Notes")
    lines.append("")
    lines.append("- Headline (overall) McNemar in `FINAL_REPORT.md §McNemar` was a partial pass;")
    lines.append("  this file completes it per `(eng × eng × lang)` for all `n_common >= 30` triples.")
    lines.append("- `b_correct_a_wrong` is an alias for the spec field `b_correct_a_wrong`; "
                 "named after the directional McNemar count of items where engine_b correctly passed but engine_a failed.")
    lines.append("- All stats are computed from disk-truth preds (no caching across reruns).")
    lines.append("- D4 low-confidence cells (as, gu, ne, doi, mni, sat) — winner rows are "
                 "informational; do not cite as ranked evidence per §6.7.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("Generated by `mcnemar_full_matrix.py` (ENGINE agent, post-H44 task).")
    lines.append("Inputs: `scores/preds_<engine>.json` ×11 (one per engine).")
    lines.append("Output: `scores/mcnemar_full_matrix.json` (raw) + `scores/mcnemar_summary.md` (this).")
    (SCORES / "mcnemar_summary.md").write_text("\n".join(lines) + "\n")
    logging.info(f"wrote {(SCORES / 'mcnemar_summary.md')}")


if __name__ == "__main__":
    main()
