#!/usr/bin/env python3
"""Reporting pack — team-facing reports from disk truth.

Writes level2/reports/:
  LANG_LEADERBOARD.md   — per-language + Devanagari-subset leaderboards (item 66)
  SCENARIO_BEST.md      — best-engine-per-scenario table (item 68)
  GAP_ANALYSIS.md       — text volume all free engines miss (item 69)
  SHOWCASE.md           — 10 pages x 10 engines side-by-side snippets (item 70)
  WHATSAPP_WEEKLY.md    — 5-line counts-only weekly update (item 71)
Usage: .venv311/bin/python level2/report_gen.py
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
REPORTS = L2 / "reports"

ENGINES = [
    "tesseract_indic", "openbharatocr", "easyocr", "paddleocr_indic",
    "indicphotoocr", "rapidocr", "tesseract_bilingual", "doctr",
    "surya", "anuvaad_tesseract",
]

LANG_NAMES = {"te": "Telugu", "ta": "Tamil", "kn": "Kannada", "ml": "Malayalam"}


def engine_text(engine: str, page_id: str) -> str:
    d = OUT / engine
    if not d.exists():
        return ""
    for p in d.rglob(f"{page_id}.json"):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
            return "\n".join(r.get("text", "") for r in obj.get("regions", []))
        except Exception:
            return ""
    return ""


def main() -> None:
    REPORTS.mkdir(exist_ok=True)
    manifest = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))

    data: dict[str, dict[str, str]] = {}
    by_lang: dict[str, list[dict]] = defaultdict(list)
    for item in manifest:
        pid = item["page_id"]
        row = {"pid": pid, "lang": item["lang"], "dom": item.get("dominant_script"),
               "mixed": item.get("mixed_book_page", False), "l1": item.get("l1_chars", 0)}
        texts: dict[str, str] = {}
        for e in ENGINES:
            t = engine_text(e, pid)
            texts[e] = t
            row[e] = len(t.strip())
        data[pid] = texts
        by_lang[item["lang"]].append(row)

    # item 66: per-language + Devanagari-subset leaderboards
    def board(rows: list[dict], title: str, key: str) -> list[str]:
        lines = [f"### {title}", "",
                 "| engine | pages | nonempty | median chars | total chars |",
                 "|---|---|---|---|---|"]
        for e in ENGINES:
            vals = [r[e] for r in rows if r[e] is not None]
            checked = len(vals)
            nonempty = sum(1 for v in vals if v > 0)
            sv = sorted([v for v in vals if v > 0])
            med = sv[len(sv) // 2] if sv else 0
            lines.append(f"| {e} | {checked} | {nonempty} | {med} | {sum(vals)} |")
        return lines

    lines = ["# Language Leaderboards (per lang-tag + Devanagari subset)", ""]
    for lang, rows in sorted(by_lang.items()):
        lines += board(rows, f"lang = {lang} ({LANG_NAMES[lang]})", lang)
        lines.append("")
    dev_rows = [r for r in sum(by_lang.values(), []) if r["dom"] == "Devanagari"]
    lines += board(dev_rows, "Devanagari-dominant pages (mixed-book reality)", "dev")
    (REPORTS / "LANG_LEADERBOARD.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # item 68: best engine per scenario
    scen: dict[str, list[dict]] = defaultdict(list)
    for rows in by_lang.values():
        for r in rows:
            if r["mixed"]:
                scen["mixed-book pages"].append(r)
            elif r["dom"] == "Latin":
                scen["Latin-dominant pages"].append(r)
            elif r["dom"] == "Devanagari":
                scen["Devanagari-dominant (unmixed) pages"].append(r)
            else:
                scen["pure-Indic pages"].append(r)
    lines = ["# Best Engine per Scenario (median chars, disk-truth)", "",
             "| scenario | n | best (median chars) | runner-up |", "|---|---|---|---|"]
    for name, rows in sorted(scen.items()):
        med: dict[str, int] = {}
        for e in ENGINES:
            sv = sorted([r[e] for r in rows if r[e] > 0])
            med[e] = sv[len(sv) // 2] if sv else 0
        rank = sorted(med.items(), key=lambda kv: -kv[1])
        best = rank[0]
        second = rank[1] if len(rank) > 1 else ("", 0)
        lines.append(f"| {name} | {len(rows)} | {best[0]} ({best[1]}) | {second[0]} ({second[1]}) |")
    (REPORTS / "SCENARIO_BEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # item 69: gap analysis — text volume engines miss vs strongest consensus
    lines = ["# Gap Analysis — free-engine text volume missed (Vaultstack opportunity)", ""]
    engine_totals = {e: sum(len(data[pid][e].strip()) for pid in data) for e in ENGINES}
    best_total = max(engine_totals.values()) if engine_totals else 0
    union_chars = 0
    for pid in data:
        page_best = max(len(data[pid][e].strip()) for e in ENGINES)
        union_chars += page_best
    lines.append("Per page, the best free engine captures (union-of-best): "
                 f"**{union_chars:,} chars** over 400 pages.")
    lines.append("")
    lines.append("| engine | total chars | vs best engine | vs union-of-best |")
    lines.append("|---|---|---|---|")
    for e, t in sorted(engine_totals.items(), key=lambda kv: -kv[1]):
        lines.append(f"| {e} | {t:,} | {t / best_total * 100 if best_total else 0:.0f}% | {t / union_chars * 100 if union_chars else 0:.0f}% |")
    lines += ["", "Reading: even the union-of-best is an UNDER-count of on-page text",
              "(no free engine reads everything). The full on-page gap is the",
              "Vaultstack opportunity; Level-1 gold `l1_chars` total: "
              f"**{sum(r['l1'] for rows in by_lang.values() for r in rows):,} chars**."]
    # H2 (operator 14 Sep): single quotable gap number — GAP.md owns it.
    # GAP_ANALYSIS.md (raw volume view) retired to _archive/; writer no longer emits it.
    gap_analysis_note = [
        "# GAP_ANALYSIS — retired 14 Sep (H2 decision)",
        "",
        "This raw-volume view is RETIRED: one quotable gap number lives in GAP.md",
        "(7.1% lower bound). Historical copy: _archive/GAP_ANALYSIS_retired_20260914.md",
    ]
    (REPORTS / "GAP_ANALYSIS.md").write_text("\n".join(gap_analysis_note) + "\n", encoding="utf-8")

    # item 70: showcase — 10 pages x 10 engines, first 120 chars each
    show_pids = [m["page_id"] for m in manifest[:10]]
    lines = ["# Side-by-Side Showcase — 10 pages x 10 engines (first 120 chars)", ""]
    for pid in show_pids:
        item = next(m for m in manifest if m["page_id"] == pid)
        lines += [f"## {pid} ({item['lang']}, dominant={item.get('dominant_script')})", ""]
        for e in ENGINES:
            t = data[pid][e].strip().replace("\n", " ⏎ ")[:120]
            lines.append(f"- **{e}**: {t if t else '_(empty/missing)'}")
        lines.append("")
    (REPORTS / "SHOWCASE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # item 62: human-review queue — pages with highest cross-engine disagreement
    spreads = []
    for pid, texts in data.items():
        lens = [len(t.strip()) for t in texts.values()]
        live = [x for x in lens if x > 0]
        if len(live) < 4:
            continue
        spread = max(live) - min(live)
        rel = spread / max(max(live), 1)
        if rel > 0.8 and spread > 500:
            spreads.append((pid, spread, min(live), max(live)))
    spreads.sort(key=lambda x: -x[1])
    lines = ["# Human-Review Queue — top cross-engine disagreement pages", "",
             "Columns: chars(min)→chars(max) across engines. Big gap = one engine missed/fabricated.", ""]
    for pid, spread, lo, hi in spreads[:50]:
        lines.append(f"- {pid}: {lo} → {hi} (gap {spread})")
    if not spreads:
        lines.append("- none above threshold")
    (REPORTS / "REVIEW_QUEUE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # item 63: duplicate content audit — same OCR text across different pages
    import hashlib
    sig: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for pid, texts in data.items():
        for e, t in texts.items():
            tt = t.strip()
            if len(tt) < 100:
                continue
            h = hashlib.sha1((e + "|" + tt[:600]).encode("utf-8")).hexdigest()
            sig[h].append((pid, e))
    dups = {h: v for h, v in sig.items() if len({p for p, _ in v}) > 1}
    lines = ["# Duplicate-Content Audit — same engine text on multiple pages", "",
             "Suspicious pairs (possible engine collapse or dataset duplicates):", ""]
    n = 0
    for h, v in sorted(dups.items(), key=lambda kv: -len(kv[1])):
        pids = sorted({p for p, _ in v})
        lines.append(f"- {', '.join(pids[:4])}{' …' if len(pids) > 4 else ''} — engines: {sorted({e for _, e in v})}")
        n += 1
        if n >= 40:
            break
    if not dups:
        lines.append("- none (no duplicated long OCR texts across pages)")
    (REPORTS / "DUPLICATE_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # item 71: WhatsApp weekly — counts only (CANON rule)
    def n_out(e: str) -> int:
        d = OUT / e
        return len(list(d.rglob("*.json"))) if d.exists() else 0
    tot = sum(n_out(e) for e in ENGINES)
    done = sum(1 for e in ENGINES if n_out(e) >= 400)
    n_reports = len([p for p in REPORTS.iterdir() if p.is_file()]) if REPORTS.exists() else 0
    lines = ["# WhatsApp Weekly (counts only — paste-ready)", "",
             f"South Level-2 benchmark: {done}/10 engines at 400 pages, {tot} total OCR packs on disk.",
             f"Verification: {n_reports} report files, all from disk counts.",
             f"Next: easyocr rerun (open-policy fix), then seal (LEVEL2_SEAL.md).",
             "", "_Generated from disk — no hand numbers. Verify with `orchestrator.py status`._"]
    (REPORTS / "WHATSAPP_WEEKLY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("wrote: LANG_LEADERBOARD.md SCENARIO_BEST.md GAP_ANALYSIS.md SHOWCASE.md "
          "WHATSAPP_WEEKLY.md REVIEW_QUEUE.md DUPLICATE_AUDIT.md")


if __name__ == "__main__":
    main()
