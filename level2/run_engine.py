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
import sys
import time
import unicodedata
from pathlib import Path

# py3.14 removed pkgutil.find_loader; older pytesseract still imports it.
import pkgutil

if not hasattr(pkgutil, "find_loader"):
    import importlib.util

    def _find_loader(name: str):  # type: ignore[misc]
        return importlib.util.find_spec(name)

    pkgutil.find_loader = _find_loader  # type: ignore[attr-defined]

# Editable IndicPhotoOCR install sometimes fails to register; ensure path.
_IPO_ROOT = Path(__file__).resolve().parents[1] / ".deps" / "IndicPhotoOCR"
if _IPO_ROOT.is_dir() and str(_IPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_IPO_ROOT))

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
MANIFEST = L2 / "pages_manifest.json"

SCRIPTS = {"te": "Telu", "ta": "Taml", "kn": "Knda", "ml": "Mlym"}
TESS = {"te": "tel", "ta": "tam", "kn": "kan", "ml": "mal"}
# OPEN POLICY (operator directive): read whatever glyphs are on the page — any language, no restriction.
# Stack every Indic model we have + English so mixed books (Telugu/Marathi/Hindi/English) all get read.
TESS_STACK = {
    "te": "tel+hin+eng",
    "ta": "tam+hin+eng",
    "kn": "kan+hin+eng",
    "ml": "mal+hin+eng",
}
# Fully-open stack: everything installed on the system, for future languages too.
TESS_OPEN = "eng+tel+tam+kan+mal+hin"
# EasyOCR language codes
EASY = {"te": "te", "ta": "ta", "kn": "kn", "ml": "ml"}

# Render dpi used by render_to_png (single source of truth for engine_meta).
_RENDER_DPI = 200
# Mirror of seal_gen.py VERSIONS (read-only there); used for engine_meta.version.
_ENGINE_VERSIONS = {
    "tesseract_indic": "tesseract 5.5.2 (tel+hin+eng open stack)",
    "openbharatocr": "openbharatocr 0.4.3 (tesseract mirror path documented)",
    "easyocr": "easyocr 1.7.2 (all-Indic open reader)",
    "paddleocr_indic": "paddleocr 3.7.0 / paddlepaddle 3.3.1",
    "indicphotoocr": "IndicPhotoOCR IIIT-H (parseq trust-patched)",
    "rapidocr": "rapidocr-onnxruntime 1.4.4",
    "tesseract_bilingual": "tesseract 5.5.2 (eng+stack bilingual)",
    "doctr": "python-doctr 1.1.0 (crnn_vgg16_bn)",
    "surya": "surya-ocr 0.22.1 (surya-2, block-mode html)",
    "anuvaad_tesseract": "anuvaad tessdata + tesseract 5.5.2",
}

_easy_readers: dict[str, object] = {}


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "")


def preprocess_image(image_path: Path) -> Path:
    """Deskew + border-crop + binarize-variant prep (pure PIL, no new deps).

    Returns original path (engines get raw render); binarized variant saved
    alongside for retry use: <stem>_bin.png
    """
    out = image_path.with_name(image_path.stem + "_bin.png")
    if out.exists():
        return out
    try:
        img = Image.open(image_path).convert("L")
        # simple Otsu-ish threshold via histogram
        hist = img.histogram()
        total = sum(hist)
        sum_all = sum(i * h for i, h in enumerate(hist))
        sum_b = 0.0
        w_b = 0
        best_t, best_var = 0, -1.0
        for t in range(256):
            w_b += hist[t]
            if w_b == 0:
                continue
            w_f = total - w_b
            if w_f == 0:
                break
            sum_b += t * hist[t]
            m_b = sum_b / w_b
            m_f = (sum_all - sum_b) / w_f
            var = w_b * w_f * (m_b - m_f) ** 2
            if var > best_var:
                best_var, best_t = var, t
        img = img.point(lambda p: 255 if p > best_t else 0)
        img.save(out)
        return out
    except Exception:
        return image_path


class EngineTimeout(Exception):
    pass


def run_ocr_with_timeout(
    engine: str, image_path: Path, lang: str, timeout_s: int = 120, light: bool = False
) -> str:
    """Run engine call under a wall-clock timeout (thread-based; engines are C-GIL heavy so
    a cooperative soft-kill: we abandon the thread and mark failure upstream)."""
    import concurrent.futures

    ex = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    fut = ex.submit(run_ocr, engine, image_path, lang, light=light)
    try:
        return fut.result(timeout=timeout_s)
    except concurrent.futures.TimeoutError as e:
        ex.shutdown(wait=False, cancel_futures=True)
        raise EngineTimeout(f"{engine} timed out after {timeout_s}s on {image_path.name}") from e
    except BaseException:
        ex.shutdown(wait=True)
        raise
    else:
        ex.shutdown(wait=True)


# Paddle-only wall-clock budgets (all other engines keep the shared 300s).
# Full pipeline keeps the standard 300s; the light retry is the terminal
# fallback and gets a raised paddle-only budget.
_PADDLE_FULL_TIMEOUT = 300
_PADDLE_LIGHT_TIMEOUT = 900
# Modes whose predict thread was abandoned on timeout. Paddle predictors
# are not safe for concurrent predict() calls on one instance, and the
# abandoned thread is still inside the pipeline — never re-enter it; later
# pages in this process fall through to the other mode instead.
_paddle_poisoned: set[tuple[str, bool]] = set()


def _paddle_page_with_fallback(png: Path, lang: str) -> str:
    """Paddle per-page strategy (paddle only; other engines untouched):
    full pipeline (server det + lang rec) first; on timeout, degrade once to
    the light config (mobile det, det input capped at 960) under a longer
    paddle-only budget.

    Timeout handling abandons the worker thread (no join), so the retry
    starts immediately instead of waiting out the zombie; the poisoned-mode
    set guarantees we never call the instance the zombie still occupies.
    """
    import concurrent.futures

    paddle_lang = _PADDLE_LANG.get(lang, "en")

    def _attempt(light: bool, timeout_s: int) -> str:
        key = (paddle_lang, light)
        if key in _paddle_poisoned:
            raise EngineTimeout(
                f"paddleocr_indic{' light' if light else ''} mode unavailable (earlier timeout) on {png.name}"
            )
        ex = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        fut = ex.submit(run_ocr, "paddleocr_indic", png, lang, light=light)
        try:
            return fut.result(timeout=timeout_s)
        except concurrent.futures.TimeoutError as e:
            _paddle_poisoned.add(key)
            raise EngineTimeout(
                f"paddleocr_indic{' light' if light else ''} timed out after {timeout_s}s on {png.name}"
            ) from e
        finally:
            # never join a timed-out paddle thread
            ex.shutdown(wait=False, cancel_futures=True)

    try:
        return _attempt(light=False, timeout_s=_PADDLE_FULL_TIMEOUT)
    except EngineTimeout:
        print("    paddle full timed out/poisoned -> light retry", flush=True)
        return _attempt(light=True, timeout_s=_PADDLE_LIGHT_TIMEOUT)


def render_to_png(raw_path: Path, page_index: int, out_png: Path, dpi: int = 200) -> tuple[int, int]:
    out_png.parent.mkdir(parents=True, exist_ok=True)
    if out_png.exists() and out_png.stat().st_size > 0:
        # render_once guard: shared renders must not be re-rendered (race + churn)
        doc = pymupdf.open(raw_path)
        try:
            if doc.page_count > page_index:
                page = doc[page_index]
                return page.rect.width, page.rect.height
            return 0, 0
        finally:
            doc.close()
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


def ocr_anuvaad_tesseract(image_path: Path, lang: str) -> str:
    """Anuvaad-tuned Tesseract models for Indic (project-anuvaad S3 weights)."""
    import pytesseract

    code = {"te": "anuvaad_tel", "ta": "anuvaad_tam", "kn": "anuvaad_kan", "ml": "anuvaad_mal"}[lang]
    tessdata = str(L2 / "research" / "smoke" / "anuvaad_tesseract" / "tessdata")
    img = Image.open(image_path)
    # OPEN POLICY: stack anuvaad Indic models + system hin/eng for mixed-script pages
    config = f"--tessdata-dir {tessdata}"
    stack = f"{code}+hin+eng"
    try:
        return nfc(pytesseract.image_to_string(img, lang=stack, config=config))
    except Exception:
        return nfc(pytesseract.image_to_string(img, lang=code, config=config))


def ocr_tesseract_indic(image_path: Path, lang: str) -> str:
    import pytesseract

    img = Image.open(image_path)
    return nfc(pytesseract.image_to_string(img, lang=TESS_STACK[lang]))


def _patch_easyocr_tamil_charset() -> None:
    """EasyOCR 1.7 tamil.pth has 143 classes; bundled charset is only 126 chars."""
    from easyocr.config import recognition_models

    meta = recognition_models["gen1"]["tamil_g1"]
    chars = meta["characters"]
    if len(chars) >= 142:
        return
    extra = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        ".,;:!?\"'()-/"
    )
    patched = chars
    for ch in extra:
        if len(patched) >= 142:
            break
        if ch not in patched:
            patched += ch
    i = 0
    while len(patched) < 142:
        ch = chr(0xE000 + i)
        if ch not in patched:
            patched += ch
        i += 1
    meta["characters"] = patched


def ocr_easyocr(image_path: Path, lang: str) -> str:
    import easyocr

    _patch_easyocr_tamil_charset()
    # OPEN POLICY (operator directive): read any script on the page, no language restriction.
    # EasyOCR hard constraints (validated 12 Sep): Dravidian models are pairwise-incompatible
    # (te/ta/kn each only work with en); Devanagari family bundles (hi mr ne + en) work.
    # Strategy: run every VALID open reader for scripts plausibly on our pages, keep longest output.
    combos = [
        ("te+en", ["te", "en"]),
        ("ta+en", ["ta", "en"]),
        ("kn+en", ["kn", "en"]),
        ("hi+mr+ne+en", ["hi", "mr", "ne", "en"]),
    ]
    best = ""
    for name, langs in combos:
        key = f"OPEN:{name}"
        if key not in _easy_readers:
            try:
                _easy_readers[key] = easyocr.Reader(langs, gpu=False)
            except Exception:
                _easy_readers[key] = None
        reader = _easy_readers[key]
        if reader is None:
            continue
        try:
            parts = reader.readtext(str(image_path), detail=0, paragraph=True)
        except Exception:
            continue
        text = "\n".join(str(p) for p in parts) if isinstance(parts, list) else str(parts)
        if len(text.strip()) > len(best.strip()):
            best = text
    return nfc(best)


_paddle_by_lang: dict[str, object] = {}
_paddle_light_by_lang: dict[str, object] = {}
_paddle_import_error: Exception | None = None

# OPEN POLICY (operator directive): read any script on the page.
# te/ta: PP-OCRv5; kn->ka: PP-OCRv3; ml unsupported by Paddle -> en stack.
_PADDLE_LANG = {"te": "te", "ta": "ta", "kn": "ka", "ml": "en"}
# Disclose the ml->en fallback once per run so RUN.md authors see it.
_ml_paddle_warned = False


def _warn_ml_paddle_fallback(lang: str) -> None:
    global _ml_paddle_warned
    if lang == "ml" and not _ml_paddle_warned:
        _ml_paddle_warned = True
        print(
            "WARNING: paddleocr_indic has no Malayalam (ml) model; ml pages fall back to the en stack.",
            file=sys.stderr,
            flush=True,
        )
# Graceful-degradation configs: mobile det + det input capped at 960/max,
# same rec model. PP-OCRv5_server_det (ta/te default det) is ~150s/page on
# CPU under load; this light config measured ~15s/page with equal-or-better
# line yield on dense Indic pages.
_PADDLE_LIGHT_REC = {
    "te": "te_PP-OCRv5_mobile_rec",
    "ta": "ta_PP-OCRv5_mobile_rec",
    "ka": "ka_PP-OCRv3_mobile_rec",
}


def _paddle_pipeline(lang: str, light: bool = False) -> object:
    """Init-once, module-level per-language pipeline cache (multiple
    PaddleOCR instances coexist fine in one process)."""
    import os

    global _paddle_import_error
    os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")
    if _paddle_import_error is not None:
        raise RuntimeError(
            f"paddleocr_indic unavailable in this Python: {_paddle_import_error}. Use .venv311."
        ) from _paddle_import_error
    cache = _paddle_light_by_lang if light else _paddle_by_lang
    paddle_lang = _PADDLE_LANG.get(lang, "en")
    if paddle_lang not in cache:
        try:
            from paddleocr import PaddleOCR
        except Exception as e:
            _paddle_import_error = e
            raise RuntimeError(
                f"paddleocr_indic unavailable in this Python: {e}. Use .venv311."
            ) from e
        init_kw = dict(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
        )
        if light and paddle_lang in _PADDLE_LIGHT_REC:
            pipe = PaddleOCR(
                text_detection_model_name="PP-OCRv3_mobile_det",
                text_recognition_model_name=_PADDLE_LIGHT_REC[paddle_lang],
                text_det_limit_side_len=960,
                text_det_limit_type="max",
                **init_kw,
            )
        elif light:
            # en stack: keep default models, just cap det input size
            pipe = PaddleOCR(
                lang=paddle_lang,
                text_det_limit_side_len=960,
                text_det_limit_type="max",
                **init_kw,
            )
        else:
            try:
                pipe = PaddleOCR(lang=paddle_lang, **init_kw)
            except Exception:
                pipe = PaddleOCR(lang="en", **init_kw)
        cache[paddle_lang] = pipe
    return cache[paddle_lang]


def ocr_paddleocr_indic(image_path: Path, lang: str, light: bool = False) -> str:
    """Use PaddleOCR when installed (run with .venv311 / PaddleOCR 3.x).

    Pipelines are cached per language at module level. Run with
    --lang te|ta|kn|ml for correct models. light=True switches to the
    fast degraded config (mobile det, capped det input) — used as a
    retry when the full pipeline times out.
    """
    _warn_ml_paddle_fallback(lang)
    pipe = _paddle_pipeline(lang, light)
    path = str(image_path)
    if hasattr(pipe, "predict"):
        result = pipe.predict(path)
    elif hasattr(pipe, "ocr"):
        result = pipe.ocr(path)
    else:
        raise RuntimeError("PaddleOCR has neither predict nor ocr")
    lines: list[str] = []
    if not result:
        return ""

    def _absorb(obj: object) -> None:
        if obj is None:
            return
        if hasattr(obj, "get") and not isinstance(obj, (list, tuple, str)):
            for key in ("rec_texts", "texts", "text"):
                try:
                    val = obj.get(key)  # type: ignore[union-attr]
                except Exception:
                    val = None
                if isinstance(val, list):
                    lines.extend(str(x) for x in val if x is not None)
                    return
                if isinstance(val, str):
                    lines.append(val)
                    return
        if isinstance(obj, dict):
            for key in ("rec_texts", "texts", "text"):
                val = obj.get(key)
                if isinstance(val, list):
                    lines.extend(str(x) for x in val if x is not None)
                    return
                if isinstance(val, str):
                    lines.append(val)
                    return
            return
        if isinstance(obj, (list, tuple)):
            # classic: [box, (text, conf)] or nested blocks
            if (
                len(obj) >= 2
                and isinstance(obj[1], (list, tuple))
                and obj[1]
                and isinstance(obj[1][0], str)
            ):
                lines.append(obj[1][0])
                return
            for item in obj:
                _absorb(item)
            return
        if hasattr(obj, "rec_texts"):
            val = getattr(obj, "rec_texts")
            if isinstance(val, list):
                lines.extend(str(x) for x in val if x is not None)
            return

    _absorb(result)
    return nfc("\n".join(lines))


_ipo_ocr = None


def ocr_indicphotoocr(image_path: Path, lang: str) -> str:
    global _ipo_ocr
    try:
        from IndicPhotoOCR.ocr import OCR  # type: ignore
    except Exception as e:
        raise RuntimeError(f"IndicPhotoOCR not importable: {e}") from e
    # CPU path — init once per process, reuse across pages
    if _ipo_ocr is None:
        _ipo_ocr = OCR(verbose=False, identifier_lang="auto", device="cpu")
    results = _ipo_ocr.ocr(str(image_path))
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


def ocr_tesseract_bilingual(image_path: Path, lang: str) -> str:
    """Official tessdata bilingual: eng+indic (same GitHub tessdata method)."""
    import pytesseract

    img = Image.open(image_path)
    # eng + TESS_STACK already contains eng; dedupe preserving order
    parts = ["eng"] + TESS_STACK[lang].split("+")
    seen: set[str] = set()
    stack_parts = []
    for p in parts:
        if p and p not in seen:
            seen.add(p)
            stack_parts.append(p)
    code = "+".join(stack_parts)
    return nfc(pytesseract.image_to_string(img, lang=code))


def ocr_surya(image_path: Path, lang: str) -> str:
    """Surya multilingual document OCR (OSS 0.22+). Block mode: layout → per-block
    recognition. Blocks carry HTML text (surya-2 model), so we extract text from html."""
    from surya.layout import LayoutPredictor
    from surya.recognition import RecognitionPredictor

    image = Image.open(image_path).convert("RGB")
    if getattr(ocr_surya, "_layout", None) is None:
        ocr_surya._layout = LayoutPredictor()
    if getattr(ocr_surya, "_rec", None) is None:
        ocr_surya._rec = RecognitionPredictor()
    layout = ocr_surya._layout([image])[0]
    preds = ocr_surya._rec(images=[image], layout_results=[layout], full_page=False)

    import re as _re

    def _html_to_text(html: str) -> str:
        # strip tags → text, preserve line structure per block element
        txt = _re.sub(r"<[^>]+>", " ", html or "")
        return _re.sub(r"\s+", " ", txt).strip()

    lines = []
    for p in preds:
        for line in getattr(p, "text_lines", []) or []:
            lines.append(getattr(line, "text", str(line)))
        # surya-2 block mode: text inside blocks[].html
        for attr_src in (p,):
            for block in getattr(attr_src, "blocks", []) or []:
                html = getattr(block, "html", None)
                if html:
                    t = _html_to_text(html)
                    if t:
                        lines.append(t)
                for tl in getattr(block, "lines", []) or []:
                    t = getattr(tl, "text", None)
                    if t and t not in lines:
                        lines.append(t)
    text = "\n".join(lines)
    if len(text.strip()) < 5:
        # full-page fallback
        preds = ocr_surya._rec(images=[image], full_page=True)
        lines = []
        for p in preds:
            for line in getattr(p, "text_lines", []) or []:
                lines.append(getattr(line, "text", str(line)))
            for block in getattr(p, "blocks", []) or []:
                html = getattr(block, "html", None)
                if html:
                    t = _html_to_text(html)
                    if t:
                        lines.append(t)
        text = "\n".join(lines)
    return nfc(text)


def ocr_doctr(image_path: Path, lang: str) -> str:
    """docTR document OCR (OSS)."""
    try:
        from doctr.io import DocumentFile
        from doctr.models import ocr_predictor
    except Exception as e:
        raise RuntimeError(f"doctr unavailable: {e}") from e
    global _doctr
    if "_doctr" not in globals() or globals().get("_doctr") is None:
        globals()["_doctr"] = ocr_predictor(pretrained=True)
    doc = DocumentFile.from_images(str(image_path))
    result = globals()["_doctr"](doc)
    lines = []
    # export nested structure
    data = result.export()
    for page in data.get("pages", []):
        for block in page.get("blocks", []):
            for line in block.get("lines", []):
                words = [w.get("value", "") for w in line.get("words", [])]
                lines.append(" ".join(w for w in words if w))
    return nfc("\n".join(lines))


_rapid: dict[str, object] = {}


def ocr_rapidocr(image_path: Path, lang: str) -> str:
    """RapidOCR 3.9.x multilingual ONNX, per-language rec models (te/ta v5, ka v4, devanagari v5).
    No Malayalam model exists — ml returns honest-empty (no wrong-script mojibake)."""
    if lang == "ml":
        return ""
    try:
        from rapidocr import RapidOCR
        from rapidocr.utils.typings import LangRec, OCRVersion, ModelType, LangDet
    except Exception as e:
        raise RuntimeError(f"rapidocr 3.x unavailable: {e}") from e
    if lang not in _rapid:
        _LANGV = {"te": (LangRec.TE, OCRVersion.PPOCRV5),
                  "ta": (LangRec.TA, OCRVersion.PPOCRV5),
                  "kn": (LangRec.KA, OCRVersion.PPOCRV4)}
        lrec, ver = _LANGV[lang]
        params = {
            "Rec.lang_type": lrec, "Rec.ocr_version": ver, "Rec.model_type": ModelType.MOBILE,
            "Det.ocr_version": OCRVersion.PPOCRV5, "Det.model_type": ModelType.MOBILE,
            "Det.lang_type": LangDet.CH, "Cls.use_cls": False,
        }
        _rapid[lang] = RapidOCR(params=params)
    result = _rapid[lang](str(image_path))
    txts = getattr(result, "txts", None) or []
    return nfc("\n".join(str(t) for t in txts if t))


def run_ocr(engine: str, image_path: Path, lang: str, light: bool = False) -> str:
    if engine == "tesseract_indic":
        return ocr_tesseract_indic(image_path, lang)
    if engine == "easyocr":
        return ocr_easyocr(image_path, lang)
    if engine == "paddleocr_indic":
        return ocr_paddleocr_indic(image_path, lang, light=light)
    if engine == "indicphotoocr":
        return ocr_indicphotoocr(image_path, lang)
    if engine == "openbharatocr":
        return ocr_openbharatocr(image_path, lang)
    if engine == "tesseract_bilingual":
        return ocr_tesseract_bilingual(image_path, lang)
    if engine == "surya":
        return ocr_surya(image_path, lang)
    if engine == "doctr":
        return ocr_doctr(image_path, lang)
    if engine == "rapidocr":
        return ocr_rapidocr(image_path, lang)
    if engine == "anuvaad_tesseract":
        return ocr_anuvaad_tesseract(image_path, lang)
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
        "engine_meta": {
            "engine": engine,
            "policy": "open_any_script",
            "dpi": _RENDER_DPI,
            "version": _ENGINE_VERSIONS.get(engine, "unknown"),
        },
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
                "provenance": "ocr_engine",
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
            # Level2 +3 free engines
            "tesseract_bilingual",
            "surya",
            "doctr",
            "rapidocr",
            "anuvaad_tesseract",
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

    tmp = L2 / "renders_shared"
    tmp.mkdir(parents=True, exist_ok=True)

    # heartbeat: crash-survivable progress file
    hb = L2 / "HEARTBEAT.jsonl"
    hb.parent.mkdir(exist_ok=True)

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
        t0 = time.monotonic()
        try:
            png = tmp / f"{page_id}.png"
            w, h = render_to_png(raw, pidx, png)
            if args.engine == "paddleocr_indic":
                # graceful degradation: full pipeline -> light retry (paddle only)
                text = _paddle_page_with_fallback(png, lang)
            else:
                try:
                    text = run_ocr_with_timeout(args.engine, png, lang, timeout_s=300)
                except EngineTimeout:
                    raise
                except Exception:
                    # one retry with binarized variant before giving up
                    bpng = preprocess_image(png)
                    if bpng != png:
                        text = run_ocr_with_timeout(args.engine, bpng, lang, timeout_s=300)
                    else:
                        raise
            dur_ms = int((time.monotonic() - t0) * 1000)
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
            with open(hb, "a", encoding="utf-8") as hf:
                hf.write(json.dumps({"t": time.time(), "engine": args.engine,
                                     "page_id": page_id, "dur_ms": dur_ms,
                                     "chars": len(text.strip())}) + "\n")
            ok += 1
        except Exception as e:
            fail += 1
            with open(hb, "a", encoding="utf-8") as hf:
                hf.write(json.dumps({"t": time.time(), "engine": args.engine,
                                     "page_id": page_id, "fail": str(e)[:120]}) + "\n")
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
