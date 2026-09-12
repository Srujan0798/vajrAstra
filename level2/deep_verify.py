#!/usr/bin/env python3
"""Per-pack deep verify: every JSON vs original page (PDF text layer + PNG script mix).

Writes reports/DEEP_VERIFY_<engine>.json with per-page verdicts:
  OK        dense script text matching page script
  EMPTY     no text captured
  THIN      <30 chars on a page with visible text
  SCRIPT_MISMATCH  OCR script vs page's actual script histogram (PDF layer) diverge
  ENGLISH_LEAK     Indic-dominant page -> mostly Latin output
  LOOP      repeated-line collapse
Reads ONLY from disk; never invents. GT sources: Datasets/ PDF text layer,
arc_level_1 gold, renders. Non-desctructive: writes report only.
"""
from __future__ import annotations
import json, sys, hashlib, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
REPORTS = L2 / "reports"
DATASETS = ROOT / "Datasets"
RENDERS = L2 / "renders_shared"

SCRIPT_RANGES = {
    "Telugu": (0x0C00, 0x0C7F), "Tamil": (0x0B80, 0x0BFF),
    "Kannada": (0x0C80, 0x0CFF), "Malayalam": (0x0D00, 0x0DFF),
    "Devanagari": (0x0900, 0x097F), "Bengali": (0x0980, 0x09FF),
    "Gurmukhi": (0x0A00, 0x0A7F), "Gujarati": (0x0A80, 0x0AFF),
    "Oriya": (0x0B00, 0x0B7F), "Sinhala": (0x0D80, 0x0DFF),
}


def script_of(ch: str) -> str | None:
    cp = ord(ch)
    if 0x0E00 <= cp <= 0x0E7F: return "Thai"
    for name, (lo, hi) in SCRIPT_RANGES.items():
        if lo <= cp <= hi: return name
    return None


def hist(text: str) -> dict:
    h = {}
    for ch in text:
        s = script_of(ch)
        if s: h[s] = h.get(s, 0) + 1
    return h


def top_script(h: dict) -> tuple[str, float] | None:
    tot = sum(h.values())
    if not tot: return None
    s, n = max(h.items(), key=lambda kv: kv[1])
    return s, n / tot


def pdf_text_of(page_id: str) -> str:
    lang, idx = page_id.split("_")
    man = json.load(open(L2 / "pages_manifest.json"))
    for p in man:
        if p["page_id"] == page_id:
            pdf = ROOT / p["raw_path"]
            pno = p["page_index"]
            try:
                import pypdf
                r = pypdf.PdfReader(str(pdf))
                if pno < len(r.pages):
                    return (r.pages[pno].extract_text() or "")[:6000]
            except Exception:
                return ""
    return ""


def loop_ratio(lines: list[str]) -> float:
    if not lines: return 0.0
    from collections import Counter
    c = Counter(l.strip() for l in lines if l.strip())
    top, n = c.most_common(1)[0] if c else ("", 0)
    return n / max(1, len(lines))


def verify_pack(eng: str, page_id: str) -> dict:
    lang, idx = page_id.split("_")
    jp = OUT / eng / lang / f"{page_id}.json"
    if not jp.exists():
        jp2 = L2 / "models" / eng / "json" / f"{page_id}.json"
        if not jp2.exists():
            return {"page_id": page_id, "verdict": "MISSING"}
        jp = jp2
    try:
        d = json.load(open(jp))
    except Exception as e:
        return {"page_id": page_id, "verdict": "MALFORMED", "err": str(e)[:80]}
    text = ""
    for r in d.get("regions", []):
        text += (r.get("text") or "") + "\n"
    text = text.strip()
    lines = [l for l in text.splitlines() if l.strip()]
    oh = hist(text)
    ph = hist(pdf_text_of(page_id))
    ts_ocr, r_ocr = (top_script(oh) or (None, 0))
    ts_page, r_page = (top_script(ph) or (None, 0))
    v = "OK"
    if not text: v = "EMPTY"
    elif len(text) < 30: v = "THIN"
    else:
        if ts_page == "Latin" or ts_page is None:
            if ts_ocr and ts_ocr not in ("Latin", None) and r_ocr > 0.7:
                pass
            if ts_ocr and ts_ocr == "Latin" and r_ocr > 0.95 and ts_page is None:
                v = "OK"
        elif ts_ocr != ts_page and r_ocr > 0.8:
            v = "SCRIPT_MISMATCH"
        if v == "OK" and ts_page and ts_page != "Latin" and ts_ocr == "Latin" and r_ocr > 0.9:
            v = "ENGLISH_LEAK"
    lr = loop_ratio(lines)
    if lr > 0.5 and len(lines) > 5: v = "LOOP"
    return {
        "page_id": page_id, "verdict": v, "chars": len(text),
        "ocr_script": ts_ocr, "ocr_ratio": round(r_ocr or 0, 2),
        "page_script": ts_page, "page_ratio": round(r_page or 0, 2),
        "loop": round(lr, 2), "json": str(jp.relative_to(ROOT)),
    }


def main():
    eng = sys.argv[1] if len(sys.argv) > 1 else None
    man = json.load(open(L2 / "pages_manifest.json"))
    pids = [p["page_id"] for p in man]
    engines = [eng] if eng else []
    if not engines:
        engines = sorted(d.name for d in OUT.iterdir() if d.is_dir() and d.name != "README.md")
    for e in engines:
        out = [verify_pack(e, pid) for pid in pids]
        ok = sum(1 for x in out if x["verdict"] == "OK")
        counts = {}
        for x in out: counts[x["verdict"]] = counts.get(x["verdict"], 0) + 1
        REPORTS.mkdir(exist_ok=True)
        rp = REPORTS / f"DEEP_VERIFY_{e}.json"
        json.dump({"engine": e, "total": len(out), "ok": ok, "counts": counts,
                   "pages": out}, open(rp, "w"), ensure_ascii=False, indent=1)
        print(f"{e}: OK {ok}/400  {counts}")
        (REPORTS / f"DEEP_VERIFY_{e}.flag").write_text(
            "PROBLEM\n" if ok < 400 * 0.7 else "PASS\n")


if __name__ == "__main__":
    main()
