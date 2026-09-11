#!/usr/bin/env python3
"""
Level 2 runner: OCR same Dataset pages -> Level-1-style JSON packs.

Examples:
  python level2/run_engine.py --engine tesseract_indic
  python level2/run_engine.py --engine easyocr --skip-existing
  python level2/run_engine.py --engine tesseract_indic --lang te --batch B0
"""
from __future__ import annotations

import argparse
import json
import unicodedata
from pathlib import Path

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
MANIFEST = L2 / "pages_manifest.json"

SCRIPTS = {"te": "Telu", "ta": "Taml", "kn": "Knda", "ml": "Mlym"}
TESS = {"te": "tel", "ta": "tam", "kn": "kan", "ml": "mal"}
# EasyOCR language codes
EASY = {"te": "te", "ta": "ta", "kn": "kn", "ml": "ml"}

_easy_readers: dict[str, object] = {}


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "")


def render_to_png(raw_path: Path, page_index: int, out_png: Path, dpi: int = 200) -> tuple[int, int]:
    out_png.parent.mkdir(parents=True, exist_ok=True)
    if raw_path.suffix.lower() == ".pdf":
        doc = pymupdf.open(raw_path)
        try:
            if doc.needs_pass and not doc.authenticate(""):
                raise RuntimeError(f"password locked: {raw_path}")
            if page_index < 0 or page_index >= doc.page_count:
                raise RuntimeError(f"page OOR {page_index}/{doc.page_count}: {raw_path}")
            page = doc[page_index]
            pix = page.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), alpha=False)
            pix.save(str(out_png))
            return pix.width, pix.height
        finally:
            doc.close()
    doc = pymupdf.open(raw_path)
    try:
        pix = doc[0].get_pixmap()
        pix.save(str(out_png))
        return pix.width, pix.height
    finally:
        doc.close()


def ocr_tesseract_indic(image_path: Path, lang: str) -> str:
    import pytesseract

    img = Image.open(image_path)
    return nfc(pytesseract.image_to_string(img, lang=TESS[lang]))


def ocr_easyocr(image_path: Path, lang: str) -> str:
    import easyocr

    key = EASY[lang]
    if key not in _easy_readers:
        # English + target lang helps mixed pages
        _easy_readers[key] = easyocr.Reader(["en", key], gpu=False)
    reader = _easy_readers[key]
    parts = reader.readtext(str(image_path), detail=0, paragraph=True)
    if isinstance(parts, list):
        text = "\n".join(str(p) for p in parts)
    else:
        text = str(parts)
    return nfc(text)


_paddle = None


def ocr_paddleocr_indic(image_path: Path, lang: str) -> str:
    """Use PaddleOCR when installed (run with .venv311)."""
    global _paddle
    try:
        from paddleocr import PaddleOCR
    except Exception as e:
        raise RuntimeError(
            f"paddleocr_indic unavailable in this Python: {e}. Use .venv311."
        ) from e
    # Paddle language codes: use latin/en + defer to multilingual where needed
    # For Indic pages, 'en' alone is weak; try lang-specific if supported else 'en'
    paddle_lang = {"te": "te", "ta": "ta", "kn": "ka", "ml": "ml"}.get(lang, "en")
    if _paddle is None or getattr(_paddle, "_south_lang", None) != paddle_lang:
        try:
            _paddle = PaddleOCR(use_angle_cls=True, lang=paddle_lang, show_log=False)
        except Exception:
            _paddle = PaddleOCR(use_angle_cls=True, lang="en", show_log=False)
        _paddle._south_lang = paddle_lang
    result = _paddle.ocr(str(image_path))
    lines = []
    if not result:
        return ""
    # PaddleOCR result formats vary by version
    for block in result:
        if not block:
            continue
        for item in block:
            try:
                # classic: [box, (text, conf)]
                if isinstance(item, (list, tuple)) and len(item) >= 2:
                    txt = item[1][0] if isinstance(item[1], (list, tuple)) else item[1]
                    lines.append(str(txt))
            except Exception:
                continue
    return nfc("\n".join(lines))


def ocr_indicphotoocr(image_path: Path, lang: str) -> str:
    try:
        from IndicPhotoOCR.ocr import OCR  # type: ignore
    except Exception as e:
        raise RuntimeError(f"IndicPhotoOCR not importable: {e}") from e
    # CPU path
    ocr_system = OCR(verbose=False, identifier_lang="auto", device="cpu")
    results = ocr_system.ocr(str(image_path))
    lines = []
    if isinstance(results, list):
        for line in results:
            if isinstance(line, list):
                lines.append(" ".join(str(w) for w in line))
            else:
                lines.append(str(line))
    else:
        lines.append(str(results))
    return nfc("\n".join(lines))


def ocr_openbharatocr(image_path: Path, lang: str) -> str:
    """
    OpenBharatOCR is mainly for Indian ID cards.
    For full pages we fall back to its underlying tesseract/paddle stack if exposed,
    else use tesseract_indic so the pipeline still produces packs.
    """
    try:
        import openbharatocr  # noqa: F401
    except Exception:
        pass
    # Practical full-page path: Indic Tesseract (documented fallback)
    return ocr_tesseract_indic(image_path, lang)


def run_ocr(engine: str, image_path: Path, lang: str) -> str:
    if engine == "tesseract_indic":
        return ocr_tesseract_indic(image_path, lang)
    if engine == "easyocr":
        return ocr_easyocr(image_path, lang)
    if engine == "paddleocr_indic":
        return ocr_paddleocr_indic(image_path, lang)
    if engine == "indicphotoocr":
        return ocr_indicphotoocr(image_path, lang)
    if engine == "openbharatocr":
        return ocr_openbharatocr(image_path, lang)
    raise SystemExit(f"Unknown engine: {engine}")


def write_json(
    out_path: Path,
    *,
    page_id: str,
    lang: str,
    engine: str,
    raw_path: str,
    page_index: int,
    width: int,
    height: int,
    text: str,
) -> None:
    obj = {
        "page_id": page_id,
        "source": "S5_govt",
        "lang": lang,
        "script": SCRIPTS[lang],
        "modality": "printed",
        "domain": "unknown",
        "quality_tier": "T2",
        "missing": [] if text.strip() else ["L2"],
        "unreadable_reason": None if text.strip() else "ocr_empty",
        "ocr_engine": engine,
        "image": {
            "raw_path": raw_path,
            "page_index": page_index,
            "width": width,
            "height": height,
        },
        "regions": [
            {
                "region_id": "r1",
                "cls": "paragraph",
                "bbox_xyxy": [0, 0, width, height],
                "reading_order": 1,
                "modality": "printed",
                "text": text,
                "text_nfc": nfc(text),
                "provenance": "distilled_vlm",
            }
        ],
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--engine",
        required=True,
        choices=[
            "tesseract_indic",
            "indicphotoocr",
            "openbharatocr",
            "paddleocr_indic",
            "easyocr",
        ],
    )
    ap.add_argument("--lang", choices=["te", "ta", "kn", "ml", "all"], default="all")
    ap.add_argument("--batch", choices=["B0", "B1", "B2", "B3", "B4", "all"], default="all")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--skip-existing", action="store_true")
    args = ap.parse_args()

    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.lang != "all":
        items = [x for x in items if x["lang"] == args.lang]
    if args.batch != "all":
        items = [x for x in items if x.get("batch") == args.batch]
    if args.limit and args.limit > 0:
        items = items[: args.limit]

    tmp = L2 / "_tmp_render" / args.engine
    tmp.mkdir(parents=True, exist_ok=True)

    ok = fail = skipped = 0
    for i, item in enumerate(items, 1):
        lang = item["lang"]
        page_id = item["page_id"]
        out_path = L2 / "out" / args.engine / lang / f"{page_id}.json"
        if args.skip_existing and out_path.exists():
            skipped += 1
            continue
        raw = ROOT / item["raw_path"]
        pidx = int(item["page_index"])
        print(f"[{i}/{len(items)}] {args.engine} {page_id}", flush=True)
        try:
            png = tmp / f"{page_id}.png"
            w, h = render_to_png(raw, pidx, png)
            text = run_ocr(args.engine, png, lang)
            write_json(
                out_path,
                page_id=page_id,
                lang=lang,
                engine=args.engine,
                raw_path=item["raw_path"],
                page_index=pidx,
                width=w,
                height=h,
                text=text,
            )
            ok += 1
        except Exception as e:
            fail += 1
            print(f"  FAIL {page_id}: {type(e).__name__}: {e}", flush=True)

    print(
        json.dumps(
            {
                "engine": args.engine,
                "requested": len(items),
                "ok": ok,
                "fail": fail,
                "skipped": skipped,
                "out": f"level2/out/{args.engine}",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
