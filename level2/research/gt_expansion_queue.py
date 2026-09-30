#!/usr/bin/env python3
"""A2 lane 2 (T2): which pages without usable GT should humans verify first?

    python3 level2/research/gt_expansion_queue.py

Pool = every page NOT in clean_v2: gt_thin (no usable PDF layer),
mojibake (tag-based gate), script_mismatch (tag-independent gate, Round-1).
Classes:
  contentless  — no independent family emits >= 50 chars (300-dpi probe: not recoverable) -> dropped
  legacy_font  — a PDF layer exists but is a legacy encoding -> lane B: font-map conversion
                 (no human typing if a verified map exists) with human fallback
  scan_only    — no usable layer -> lane A: human verification of an engine draft
Priority inside lane A: South pages in their own script (observed by the engines), scripts
furthest below n=20 first (te/kn/ml today), then best draft agreement (cheapest to verify).
Draft = medoid of the 7 independent families (see PSEUDO_GT.md: ~14-19% char error — a
starting point for a reviewer, never GT until a human signs it; L7).
Effort uses an EXPLICIT assumption: REVIEW_CHARS_PER_MIN chars of draft verified per minute.
Writes research/GT_EXPANSION_QUEUE.{json,md}.
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r1_common as C  # noqa: E402
import pseudo_gt as P  # noqa: E402

TARGET_N = 20
REVIEW_CHARS_PER_MIN = 100  # assumption: careful verification of an OCR draft, Indic script
OWN = {"te": "Telugu", "ta": "Tamil", "kn": "Kannada", "ml": "Malayalam"}
REVIEWER = {"te": "Srujan (can gold-check Telugu, SOUTH_CANON §D)",
            "ta": "native reviewer — NOT NAMED (H-2)", "kn": "native reviewer — NOT NAMED (H-2)",
            "ml": "native reviewer — NOT NAMED (H-2)"}
OUT = HERE / "GT_EXPANSION_QUEUE"


def main() -> None:
    b = C.basis()
    m = C.manifest()
    A = P.load_all()
    v2 = set(b["clean_v2"])
    reason = {**{p: "gt_thin" for p in b["thin"]}, **{p: "mojibake" for p in b["mojibake"]},
              **{p: "script_mismatch" for p in b["script_mismatch"]}}
    have = Counter(m[p]["lang"] for p in v2 if C.observed_script(p) == OWN[m[p]["lang"]])
    need = {l: max(0, TARGET_N - have[l]) for l in OWN}

    rows = []
    for pid, why in sorted(reason.items()):
        ag = A[pid]
        maxc = max(ag["chars"].values(), default=0)
        obs = C.observed_script(pid)
        lang = m[pid]["lang"]
        if maxc < 50:
            cls = "contentless"
        elif why in ("mojibake", "script_mismatch"):
            cls = "legacy_font"
        else:
            cls = "scan_only"
        med, _, to_med = P.medoid(ag)
        support = sum(1 for v in to_med.values() if v <= 0.2) if med else 0
        spread = round(sum(to_med.values()) / max(1, len(to_med) - 1), 3) if med else None
        draft_chars = ag["chars"].get(med, 0) if med else 0
        rows.append({"page_id": pid, "lang": lang, "reason": why, "class": cls,
                     "observed_script": obs, "own_script": obs == OWN[lang],
                     "mixed_book_page": m[pid]["mixed_book_page"], "l1_chars": m[pid].get("l1_chars"),
                     "draft_engine": med, "draft_chars": draft_chars, "support_tau02": support,
                     "draft_spread": spread,
                     "review_min": round(draft_chars / REVIEW_CHARS_PER_MIN, 1),
                     "reviewer": REVIEWER[lang]})

    def prio(r):
        return (not r["own_script"], -need[r["lang"]], -r["support_tau02"],
                r["draft_spread"] if r["draft_spread"] is not None else 9, r["page_id"])

    for cls in ("scan_only", "legacy_font"):
        ranked = sorted((r for r in rows if r["class"] == cls), key=prio)
        for i, r in enumerate(ranked, 1):
            r["rank_in_class"] = i
    # batch 1 per language = the pages that close the n>=20 gap (own-script, best drafts)
    batch1 = defaultdict(list)
    for r in sorted((r for r in rows if r["class"] in ("scan_only", "legacy_font") and r["own_script"]), key=prio):
        if len(batch1[r["lang"]]) < need[r["lang"]]:
            batch1[r["lang"]].append(r["page_id"])
            r["batch"] = 1

    res = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "target_n_per_script": TARGET_N, "own_script_scored_now": dict(have), "need": need,
           "review_chars_per_min_assumption": REVIEW_CHARS_PER_MIN,
           "class_counts": dict(Counter(r["class"] for r in rows)),
           "class_by_lang": {c: dict(Counter(r["lang"] for r in rows if r["class"] == c))
                             for c in ("scan_only", "legacy_font", "contentless")},
           "batch1": {k: v for k, v in batch1.items() if v}, "pages": rows}
    C.write_json(OUT.with_suffix(".json"), res)
    write_md(res)
    print(res["class_counts"], "need", need, "batch1", {k: len(v) for k, v in batch1.items()})


def write_md(r):
    rows = {p["page_id"]: p for p in r["pages"]}
    L = ["# GT EXPANSION QUEUE — human verification worklist",
         f"generated {r['generated_at']} by `research/gt_expansion_queue.py` (do not hand-edit)", "",
         f"Scored own-script pages today (clean_v2): {r['own_script_scored_now']}. Target n≥{r['target_n_per_script']} per script "
         f"to allow any per-script claim → need {r['need']}.", "",
         "| class | pages | by lang | route |", "|---|---|---|---|",
         f"| scan_only | {r['class_counts'].get('scan_only', 0)} | {r['class_by_lang']['scan_only']} | lane A: human verifies engine draft |",
         f"| legacy_font | {r['class_counts'].get('legacy_font', 0)} | {r['class_by_lang']['legacy_font']} | lane B: identify font (pymupdf font names), verified font-map conversion, 4-page gate vs human text; human fallback |",
         f"| contentless | {r['class_counts'].get('contentless', 0)} | {r['class_by_lang']['contentless']} | dropped (no family ≥50 chars; 300-dpi probe 0/10) |",
         "", f"## Batch 1 — closes the n≥{r['target_n_per_script']} gap (effort at {r['review_chars_per_min_assumption']} chars/min, an assumption)", ""]
    for lang, pids in r["batch1"].items():
        mins = sum(rows[p]["review_min"] for p in pids)
        L += [f"### {lang} — {len(pids)} pages, ≈{mins / 60:.1f} h — reviewer: {rows[pids[0]]['reviewer']}",
              "| page | class | draft engine | draft chars | families agreeing (τ≤0.2) | est. min |", "|---|---|---|---|---|---|"]
        for p in pids:
            x = rows[p]
            L.append(f"| {p} | {x['class']} | {x['draft_engine']} | {x['draft_chars']} | {x['support_tau02']} | {x['review_min']} |")
        L.append("")
    short = {l: n - len(r["batch1"].get(l, [])) for l, n in r["need"].items() if n - len(r["batch1"].get(l, [])) > 0}
    L += [(f"Shortfall after batch 1: {short} — not enough own-script candidates in the 400; closing it needs NEW pages (scope bet, H4)."
           if short else "Shortfall after batch 1: none — batch 1 alone brings every South script to n≥20."),
          "", "## Rules",
          "- The draft is a review aid. The reviewer types/corrects the verified text; nothing is pre-accepted.",
          "- Verified pages become a NEW tier-stamped GT file (reviewer, date, tier). L1-frozen labels are never edited.",
          "- Bench firewall: verified pages are referee data, never training food.",
          "- Full ranked list (all classes) in GT_EXPANSION_QUEUE.json."]
    OUT.with_suffix(".md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
