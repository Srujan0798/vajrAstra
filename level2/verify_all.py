#!/usr/bin/env python3
"""Mass verifier: every engine JSON vs page reality.

Reality sources (no vision needed):
  1. PDF text layer (free GT) — script histogram + char count
  2. Level-1 gold labels (labeled/<lang>/<id>.json)

Checks per engine x page:
  A. GT has visible text but engine output is empty/short  -> MISSED_TEXT
  B. GT script (e.g. Devanagari) != engine input lang (te) -> SCRIPT_MISMATCH page (expected mixed-book page)
  C. Engine output volume vs GT volume ratio               -> capture fraction
Outputs:
  level2/reports/VERIFY_<engine>.json  (full detail)
  level2/reports/VERIFY_SUMMARY.json   (cross-engine table)
"""
from __future__ import annotations

import json
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
REPORTS = L2 / "reports"

SCRIPTS = {
    "Telugu": (0x0C00, 0x0C7F),
    "Tamil": (0x0B80, 0x0BFF),
    "Kannada": (0x0C80, 0x0CFF),
    "Malayalam": (0x0D00, 0x0D7F),
    "Devanagari": (0x0900, 0x097F),
    "Latin": (0x0041, 0x007A),
}

ENGINES = [
    "tesseract_indic", "openbharatocr", "easyocr", "paddleocr_indic",
    "indicphotoocr", "rapidocr", "tesseract_bilingual", "doctr",
    "surya", "anuvaad_tesseract",
]

_gt_cache: dict[str, dict] = {}


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def script_histogram(text: str) -> dict[str, int]:
    h: dict[str, int] = {}
    for ch in text:
        cp = ord(ch)
        for name, (lo, hi) in SCRIPTS.items():
            if lo <= cp <= hi:
                h[name] = h.get(name, 0) + 1
                break
    return h


def page_gt(page_id: str) -> dict:
    if page_id in _gt_cache:
        return _gt_cache[page_id]
    item = next((x for x in MANIFEST if x["page_id"] == page_id), None)
    out = {"page_id": page_id, "gt_chars": 0, "gt_scripts": {}, "gt_sample": ""}
    if item:
        try:
            import pymupdf
            doc = pymupdf.open(ROOT / item["raw_path"])
            txt = doc[int(item["page_index"])].get_text()
            out["gt_chars"] = len(txt.strip())
            out["gt_scripts"] = script_histogram(txt)
            out["gt_sample"] = txt.strip()[:80]
        except Exception as e:
            out["error"] = str(e)
    _gt_cache[page_id] = out
    return out


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


MANIFEST = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))


def verify_engine(engine: str) -> dict:
    report = {"engine": engine, "n_checked": 0, "MISSING_JSON": [], "MISS_EMPTY": [],
              "MISS_SHORT": [], "SCRIPT_MISMATCH_PAGES": [], "CAPTURE_RATIO": []}
    for item in MANIFEST:
        pid = item["page_id"]
        txt = engine_text(engine, pid)
        report["n_checked"] += 1
        if txt == "" and True:
            # could be missing file OR empty output — distinguish
            found = any(True for _ in (OUT / engine).rglob(f"{pid}.json")) if (OUT / engine).exists() else False
            if not found:
                report["MISSING_JSON"].append(pid)
                continue
            report["MISS_EMPTY"].append(pid)
        gt = page_gt(pid)
        if gt["gt_chars"] >= 100 and len(txt.strip()) < 20:
            if pid not in report["MISS_EMPTY"] and pid not in report["MISSING_JSON"]:
                report["MISS_SHORT"].append(pid)
        # script mismatch: GT dominant script not the manifest lang script
        lang_script = {"te": "Telugu", "ta": "Tamil", "kn": "Kannada", "ml": "Malayalam"}[item["lang"]]
        dom = max(gt["gt_scripts"], key=gt["gt_scripts"].get) if gt["gt_scripts"] else None
        if dom and dom != lang_script and gt["gt_scripts"].get(dom, 0) > 30:
            report["SCRIPT_MISMATCH_PAGES"].append(f"{pid}:{dom}")
        if gt["gt_chars"] > 0:
            report["CAPTURE_RATIO"].append(round(len(txt.strip()) / gt["gt_chars"], 3))
    return report


def main() -> None:
    REPORTS.mkdir(exist_ok=True)
    summary = {}
    for eng in ENGINES:
        if not (OUT / eng).exists():
            continue
        rep = verify_engine(eng)
        (REPORTS / f"VERIFY_{eng}.json").write_text(
            json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
        ratios = [r for r in rep["CAPTURE_RATIO"] if r >= 0]
        med = sorted(ratios)[len(ratios)//2] if ratios else 0
        summary[eng] = {
            "checked": rep["n_checked"],
            "missing_json": len(rep["MISSING_JSON"]),
            "empty_output": len(rep["MISS_EMPTY"]),
            "short_output": len(rep["MISS_SHORT"]),
            "script_mismatch_pages": len(rep["SCRIPT_MISMATCH_PAGES"]),
            "median_capture_ratio": med,
        }
        print(f"{eng:<22} miss={summary[eng]['missing_json']:>3} empty={summary[eng]['empty_output']:>3} "
              f"short={summary[eng]['short_output']:>3} scriptMM={summary[eng]['script_mismatch_pages']:>3} medCap={med}")
    (REPORTS / "VERIFY_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\nfull detail: level2/reports/VERIFY_<engine>.json + VERIFY_SUMMARY.json")


if __name__ == "__main__":
    main()
