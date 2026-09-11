"""
Verify labeled/*.json against claimed PDF/image pages.
Usage:
  python scripts/verify_labels.py
  python scripts/verify_labels.py --lang te
  python scripts/verify_labels.py --strict
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

try:
    import pymupdf
except ImportError:
    raise SystemExit("pymupdf required: pip install pymupdf")

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = {"te": "Telu", "ta": "Taml", "kn": "Knda", "ml": "Mlym"}
TKEY = {"te": "tel", "ta": "tam", "kn": "kan", "ml": "mal"}
RANGES = {
    "tel": ("\u0C00", "\u0C7F"),
    "tam": ("\u0B80", "\u0BFF"),
    "kan": ("\u0C80", "\u0CFF"),
    "mal": ("\u0D00", "\u0D7F"),
    "deva": ("\u0900", "\u097F"),
}


def script_counts(text: str) -> dict:
    out = {k: 0 for k in list(RANGES) + ["latn"]}
    for ch in text:
        if ("A" <= ch <= "Z") or ("a" <= ch <= "z"):
            out["latn"] += 1
        for k, (a, b) in RANGES.items():
            if a <= ch <= b:
                out[k] += 1
    return out


def verify_one(path: Path, lang: str) -> dict:
    m = re.match(rf"{lang}_(\d+)\.json$", path.name)
    pid = path.stem
    row = {
        "page_id": pid,
        "path": str(path.relative_to(ROOT)),
        "ok": True,
        "flags": [],
        "chars": 0,
        "file": None,
        "page_index": None,
    }
    if not m:
        row["ok"] = False
        row["flags"].append("BAD_NAME")
        return row
    try:
        o = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        row["ok"] = False
        row["flags"].append(f"BAD_JSON:{e}")
        return row

    img = o.get("image") or {}
    regs = o.get("regions") or []
    text = "\n".join((r.get("text") or "") for r in regs)
    chars = len(text.strip())
    row["chars"] = chars
    row["file"] = Path(str(img.get("raw_path") or "")).name
    row["page_index"] = img.get("page_index")
    row["tier"] = o.get("quality_tier")

    if o.get("page_id") not in (pid, f"{lang}_{int(m.group(1))}"):
        # allow zero-pad variants only if same number
        try:
            if int(re.search(r"(\d+)$", str(o.get("page_id") or "x")).group(1)) != int(m.group(1)):
                row["flags"].append("PAGE_ID_MISMATCH")
        except Exception:
            row["flags"].append("PAGE_ID_MISMATCH")
    if o.get("lang") != lang:
        row["flags"].append("LANG_MISMATCH")
    if o.get("script") != SCRIPTS[lang]:
        row["flags"].append("SCRIPT_MISMATCH")

    w, h = img.get("width"), img.get("height")
    if w in (0, None) or h in (0, None):
        row["flags"].append("ZERO_SIZE")
    for r in regs:
        bb = r.get("bbox_xyxy")
        if not (isinstance(bb, list) and len(bb) == 4 and bb[2] > bb[0] and bb[3] > bb[1]):
            row["flags"].append("BAD_BBOX")
            break

    if chars == 0:
        row["flags"].append("EMPTY_TEXT")
    elif chars < 50:
        row["flags"].append("VERY_SHORT")

    rp = Path(str(img.get("raw_path") or ""))
    if not rp.is_absolute():
        rp = ROOT / rp
    pidx = img.get("page_index")
    if not rp.exists():
        row["flags"].append("RAW_PATH_MISSING")
    elif rp.suffix.lower() == ".pdf":
        try:
            doc = pymupdf.open(rp)
            try:
                if doc.needs_pass and not doc.authenticate(""):
                    row["flags"].append("PASSWORD_LOCKED_TARGET")
                elif not isinstance(pidx, int) or pidx < 0 or pidx >= doc.page_count:
                    row["flags"].append("PAGE_INDEX_OOR")
                else:
                    page_text = doc[pidx].get_text()
                    pt = len(page_text.strip())
                    row["pdf_layer_chars"] = pt
                    # if layer has lots of text but JSON almost empty -> underfill
                    if pt >= 200 and chars < max(50, int(0.1 * pt)):
                        row["flags"].append("UNDERFILL_VS_PDF_LAYER")
                    # multi-page jumble heuristic
                    if "\f" in text and text.count("\f") >= 2 and pt > 0:
                        # only flag if json much longer than this page
                        if chars > max(3000, int(pt * 2.5)):
                            row["flags"].append("MULTI_PAGE_SUSPECT")
            finally:
                doc.close()
        except Exception as e:
            row["flags"].append(f"PDF_OPEN_FAIL:{type(e).__name__}")
    elif rp.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}:
        if pidx not in (0, None) and pidx != 0:
            row["flags"].append("IMAGE_BAD_PAGE_INDEX")

    sc = script_counts(text)
    row["scripts"] = sc
    tkey = TKEY[lang]
    if chars >= 50:
        if sc[tkey] >= 40:
            row["content_kind"] = "target_or_mixed_ok"
        elif sc["deva"] >= 50 and sc["deva"] > sc[tkey]:
            row["content_kind"] = "hindi_dominant_page"
        elif sc["latn"] >= 50 and sc["latn"] > sc[tkey]:
            row["content_kind"] = "english_dominant_page"
        else:
            row["content_kind"] = "other"
    elif chars == 0:
        row["content_kind"] = "empty"
    else:
        row["content_kind"] = "short"

    hard = {
        "BAD_NAME",
        "BAD_JSON",
        "ZERO_SIZE",
        "BAD_BBOX",
        "EMPTY_TEXT",
        "RAW_PATH_MISSING",
        "PAGE_INDEX_OOR",
        "PASSWORD_LOCKED_TARGET",
        "UNDERFILL_VS_PDF_LAYER",
    }
    if any(f.split(":")[0] in hard or f in hard for f in row["flags"]):
        row["ok"] = False
    if "VERY_SHORT" in row["flags"]:
        row["ok"] = False
    return row


def coverage(lang: str) -> dict:
    nums = set()
    for p in Path(ROOT / "labeled" / lang).glob("*.json"):
        m = re.match(rf"{lang}_(\d+)\.json$", p.name)
        if m:
            nums.add(int(m.group(1)))
    holes = [i for i in range(1, 101) if i not in nums]
    return {"present": sorted(nums), "holes": holes, "n_present": len(nums), "n_holes": len(holes)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["te", "ta", "kn", "ml", "all"], default="all")
    ap.add_argument("--strict", action="store_true", help="also fail hindi/english-dominant as warnings in report")
    ap.add_argument("--out", type=Path, default=ROOT / "prompts" / "VERIFY_REPORT.json")
    args = ap.parse_args()
    langs = ["te", "ta", "kn", "ml"] if args.lang == "all" else [args.lang]

    report = {"langs": {}, "todo_missing": [], "todo_weak_or_fail": []}
    for lang in langs:
        cov = coverage(lang)
        rows = []
        for p in sorted((ROOT / "labeled" / lang).glob("*.json")):
            rows.append(verify_one(p, lang))
        fail = [r for r in rows if not r["ok"]]
        short = [r for r in rows if "VERY_SHORT" in r["flags"] or r.get("content_kind") == "short"]
        empty = [r for r in rows if "EMPTY_TEXT" in r["flags"]]
        kinds = Counter(r.get("content_kind") for r in rows)
        report["langs"][lang] = {
            "coverage": cov,
            "n_files": len(rows),
            "n_ok": sum(1 for r in rows if r["ok"]),
            "n_fail": len(fail),
            "content_kinds": dict(kinds),
            "fail_ids": [r["page_id"] for r in fail],
            "short_ids": [r["page_id"] for r in short],
            "empty_ids": [r["page_id"] for r in empty],
            "rows": rows,
        }
        for i in cov["holes"]:
            report["todo_missing"].append(f"{lang}_{i:03d}")
        for r in fail:
            report["todo_weak_or_fail"].append(r["page_id"])

        print(f"\n=== {lang.upper()} ===")
        print(f"files={len(rows)} ok={report['langs'][lang]['n_ok']} fail={len(fail)} holes_001_100={cov['n_holes']}")
        print(f"kinds={dict(kinds)}")
        if cov["holes"]:
            print(f"MISSING: {[f'{lang}_{i:03d}' for i in cov['holes'][:25]]}{'...' if len(cov['holes'])>25 else ''}")
        if fail:
            print("FAIL samples:")
            for r in fail[:15]:
                print(f"  {r['page_id']}: chars={r['chars']} flags={r['flags']} file={r['file']} p{r['page_index']}")

    report["todo_all"] = sorted(set(report["todo_missing"] + report["todo_weak_or_fail"]))
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {args.out}")
    print(f"TODO missing={len(report['todo_missing'])} fail/weak={len(set(report['todo_weak_or_fail']))} union={len(report['todo_all'])}")
    print("NOTE: This verifier checks PDF text-layer / schema / sizes. It does not OCR every scan pixel.")


if __name__ == "__main__":
    main()
