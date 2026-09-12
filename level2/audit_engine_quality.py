#!/usr/bin/env python3
"""Audit Level-2 engine outputs for MAX OUTPUT (not fake 100% accuracy)."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "level2" / "out"
TARGET = 400

RANGES = {
    "te": ("\u0C00", "\u0C7F"),
    "ta": ("\u0B80", "\u0BFF"),
    "kn": ("\u0C80", "\u0CFF"),
    "ml": ("\u0D00", "\u0D7F"),
}


def script_chars(text: str, lang: str) -> int:
    a, b = RANGES[lang]
    return sum(1 for c in text if a <= c <= b)


def audit_engine(engine: str) -> dict:
    d = OUT / engine
    files = list(d.rglob("*.json")) if d.exists() else []
    by_lang = Counter()
    empty = []
    short = []
    good = []
    png_backed = []
    missing_ids = []
    for lang in ["te", "ta", "kn", "ml"]:
        present = set()
        for p in (d / lang).glob("*.json") if (d / lang).exists() else []:
            try:
                o = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                empty.append(p.name)
                continue
            pid = o.get("page_id") or p.stem
            present.add(pid)
            by_lang[lang] += 1
            text = "\n".join(r.get("text") or "" for r in o.get("regions") or [])
            chars = len(text.strip())
            rp = str((o.get("image") or {}).get("raw_path") or "")
            if rp.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                png_backed.append({"page_id": pid, "raw_path": rp, "chars": chars})
            if chars == 0:
                empty.append(pid)
            elif chars < 50:
                short.append(pid)
            else:
                good.append(pid)
        for i in range(1, 101):
            pid = f"{lang}_{i:03d}"
            if pid not in present:
                missing_ids.append(pid)

    n = len(files)
    nonempty = len(good) + len(short)
    return {
        "engine": engine,
        "total_json": n,
        "target": TARGET,
        "complete_coverage": n >= TARGET and not missing_ids,
        "by_lang": dict(by_lang),
        "n_good_ge50": len(good),
        "n_short_lt50": len(short),
        "n_empty": len(empty),
        "nonempty_rate": round(nonempty / n, 4) if n else 0.0,
        "max_output_ok": (n >= TARGET) and (nonempty / n >= 0.85 if n else False),
        "missing_ids_sample": missing_ids[:20],
        "n_missing_ids": len(missing_ids),
        "png_backed_count": len(png_backed),
        "png_backed": png_backed,
        "empty_sample": empty[:20],
        "short_sample": short[:20],
        "recommendation": (
            "OK_KEEP"
            if n >= TARGET and nonempty / max(n, 1) >= 0.85
            else (
                "RERUN_EMPTY_ONLY"
                if n >= TARGET
                else "CONTINUE_RUN"
            )
        ),
    }


def write_engine_readme(audit: dict) -> Path:
    eng = audit["engine"]
    d = OUT / eng
    d.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Level 2 OCR outputs — `{eng}`",
        "",
        "## Purpose",
        "Benchmark outputs from this Indic/OSS OCR engine on the same South Dataset pages.",
        "Goal is **max raw output** for later gap analysis / training — not perfect human gold.",
        "",
        "## Counts",
        f"- Total JSON: **{audit['total_json']} / {audit['target']}**",
        f"- By lang: `{audit['by_lang']}`",
        f"- Nonempty (>=1 char): **{audit['n_good_ge50'] + audit['n_short_lt50']}**",
        f"- Good (>=50 chars): **{audit['n_good_ge50']}**",
        f"- Short (<50): **{audit['n_short_lt50']}**",
        f"- Empty: **{audit['n_empty']}**",
        f"- Coverage missing IDs: **{audit['n_missing_ids']}**",
        f"- Recommendation: **{audit['recommendation']}**",
        "",
        "## Folder layout",
        "```",
        f"level2/out/{eng}/",
        "  te/  te_001.json ... te_100.json",
        "  ta/  ta_001.json ... ta_100.json",
        "  kn/  kn_001.json ... kn_100.json",
        "  ml/  ml_001.json ... ml_100.json",
        "```",
        "",
        "## PNG-backed JSON packs (open these + Dataset PNG)",
        f"Count: **{audit['png_backed_count']}**",
        "",
    ]
    if audit["png_backed"]:
        for row in audit["png_backed"]:
            lines.append(
                f"- `level2/out/{eng}/{row['page_id'][:2]}/{row['page_id']}.json` ← `{row['raw_path']}` (chars={row['chars']})"
            )
    else:
        lines.append("- (none for this engine / not finished)")
    lines += [
        "",
        "## How to read one pack",
        "1. Open the JSON",
        "2. `image.raw_path` + `image.page_index` → find page in shared `Dataset/`",
        "3. `regions[].text` = OCR output from this engine",
        "",
        "## Notes",
        "- `Datasets/...` in raw_path maps to shared Drive `Dataset/<Language>/...`",
        "- Empty/short pages are expected on hard scans; we maximize nonempty rate, then improve prompts/runners and re-run weak IDs.",
        "",
    ]
    out = d / "README.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", default="all")
    ap.add_argument("--write-readmes", action="store_true")
    args = ap.parse_args()
    engines = (
        ["tesseract_indic", "easyocr", "openbharatocr", "indicphotoocr", "paddleocr_indic"]
        if args.engine == "all"
        else [args.engine]
    )
    report = {}
    for eng in engines:
        a = audit_engine(eng)
        report[eng] = a
        print(
            f"{eng}: total={a['total_json']} good={a['n_good_ge50']} short={a['n_short_lt50']} empty={a['n_empty']} missing={a['n_missing_ids']} rec={a['recommendation']}"
        )
        if args.write_readmes and a["total_json"] > 0:
            path = write_engine_readme(a)
            print("  wrote", path)
    out = ROOT / "level2" / "QUALITY_AUDIT.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    main()
