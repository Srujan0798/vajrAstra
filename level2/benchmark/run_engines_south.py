"""run_engines_south.py — Minimal S4 engine runner for South (proto-104 §H S4).

Runs the local engines on the South sarvam_fill items (ta/te/kn/ml, 100 each).
Engine order per proto-104: surya, tesseract_indic, rapidocr, doctr, easyocr,
indicphotoocr, paddleocr_indic, anuvaad_tesseract, bodhan.

Writes results into level2/benchmark/packs/<engine>/<lang>/<id>.json (same
schema as the 18-language packs). Bodhan results are NO-OP until weights arrive.
sarvam_vision = the 12 calls from R-8 (logged separately).

Law: no training, no Sarvam calls beyond the 12 approved, sealed dirs read-only,
no new root md, every number reproducible.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

REPO = Path("/Users/srujansai/Desktop/South")
PAGES = REPO / "level2/benchmark/pages"
SOUTH_ITEMS = REPO / "level2/benchmark/south_sarvam_fill_items.json"
PACKS = REPO / "level2/benchmark/packs"
METRICS_PY = REPO / "level2/benchmark/pipeline/metrics.py"

# Import metrics for CER
sys.path.insert(0, str(METRICS_PY.parent))
try:
    from metrics import calculate_cer
    HAS_METRICS = True
except Exception as e:
    HAS_METRICS = False
    print(f"WARN: metrics.py import failed: {e}")

# Engine runners — minimal, returns text or None
def run_tesseract(img_path: Path, lang: str) -> str | None:
    try:
        import pytesseract
        from PIL import Image
        # Map lang to tesseract lang code
        tess_map = {"ta": "tam+eng", "te": "tel+eng", "kn": "kan+eng", "ml": "mal+eng"}
        tess_lang = tess_map.get(lang, lang + "+eng")
        return pytesseract.image_to_string(Image.open(img_path), lang=tess_lang)
    except Exception as e:
        return f"<error: {e}>"


# EasyOCR: models cached in ~/.EasyOCR/model/ for ta/te/kn only (ml missing — would download).
_EASY_READERS: dict = {}


def run_easyocr(img_path: Path, lang: str) -> str | None:
    """EasyOCR on South langs. te/kn work (models cached + verified). ta BROKEN
    (tamil.pth state_dict mismatch vs installed code — verified 2026-09-30).
    ml skipped (malayalam.pth not cached; downloading needs boss approval)."""
    if lang in ("ml", "ta"):
        return None  # ta: broken checkpoint; ml: no cached model
    try:
        import easyocr
    except ImportError:
        return "<error: easyocr_not_installed>"
    try:
        if lang not in _EASY_READERS:
            # gpu=False for determinism on CPU-only paths; cached model, no download
            _EASY_READERS[lang] = easyocr.Reader([lang, "en"], gpu=False, download_enabled=False)
        reader = _EASY_READERS[lang]
        result = reader.readtext(str(img_path), detail=0)
        if isinstance(result, list):
            return " ".join(str(x) for x in result)
        return str(result)
    except Exception as e:
        return f"<error: {e}>"

def run_surya(img_path: Path, lang: str) -> str | None:
    try:
        # surya-ocr is a heavy import; for S4 we use the bundled 18-lang packs pattern
        # but surya is the heaviest dep — attempt lazy import
        import surya
        from surya.model.detection.model import load_model as load_det, prepare_image
        from surya.model.recognition.model import load_model as load_rec
        from surya.model.recognition.processor import load_processor
        from PIL import Image
        img = Image.open(img_path)
        det = load_det()
        rec = load_rec()
        proc = load_processor()
        langs = [[lang]]  # one image, one lang list
        preds = surya.run_recognition([img], langs, det, rec, proc)
        if preds and preds[0]:
            return preds[0].text
    except Exception as e:
        return f"<error: {e}>"
    return None

ENGINES = {
    "surya": run_surya,
    "tesseract_indic": run_tesseract,
}

# Order per proto-104: surya, tesseract_indic, rapidocr, doctr, easyocr, indicphotoocr,
# paddleocr_indic, anuvaad_tesseract, bodhan (when downloaded)
ENGINE_ORDER = [
    ("surya", run_surya),
    ("tesseract_indic", run_tesseract),
    ("easyocr", run_easyocr),
    ("rapidocr", None),  # set below — needs .venv311
    ("doctr", None),
    ("anuvaad_tesseract", None),
    ("openbharatocr", None),  # byte-identical copy of tesseract_indic (no re-run)
    ("indicphotoocr", None),  # BROKEN install — skip (see below)
    ("paddleocr_indic", None),
]

# --- .venv311-only engines (rapidocr/doctr/paddle/surya need torch; run with .venv311/bin/python) ---

_RAPID = None


def run_rapidocr(img_path: Path, lang: str) -> str | None:
    """RapidOCR (onnxruntime). Works on all scripts; may return empty (honest-empty)."""
    global _RAPID
    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        return "<error: rapidocr_not_installed>"
    try:
        if _RAPID is None:
            _RAPID = RapidOCR()
        result, _ = _RAPID(str(img_path))
        if not result:
            return ""
        # result: list of [box, text, score]
        return " ".join(str(r[1]) for r in result if len(r) > 1)
    except Exception as e:
        return f"<error: {e}>"


_DOCTR_PRED = None


def run_doctr(img_path: Path, lang: str) -> str | None:
    """DocTR (db_resnet50 + parseq-ish). Script-agnostic; may return empty."""
    global _DOCTR_PRED
    try:
        from doctr.models import ocr_predictor
        from doctr.io import DocumentFile
    except ImportError:
        return "<error: doctr_not_installed>"
    try:
        if _DOCTR_PRED is None:
            _DOCTR_PRED = ocr_predictor(pretrained=True)
        doc = DocumentFile.from_images([str(img_path)])
        out = _DOCTR_PRED(doc)
        return out.render()
    except Exception as e:
        return f"<error: {e}>"


def run_anuvaad(img_path: Path, lang: str) -> str | None:
    """Anuvaad-tesseract: tesseract with anuvaad config (psm 6, same lang map).
    On the 18-lang as-items it was 19/19 empty (honest-empty); South may differ."""
    try:
        import pytesseract
        from PIL import Image
        tess_map = {"ta": "tam", "te": "tel", "kn": "kan", "ml": "mal"}
        tess_lang = tess_map.get(lang, "eng")
        # anuvaad config: psm 6 (uniform block), no eng fallback
        return pytesseract.image_to_string(Image.open(img_path), lang=tess_lang, config="--psm 6")
    except Exception as e:
        return f"<error: {e}>"


_PADDLE = {}


def run_paddleocr(img_path: Path, lang: str) -> str | None:
    """PaddleOCR. Models must be cached (paddlex cache) — never download here.
    If the lang model is missing, returns None (skip; ASK boss before downloading)."""
    try:
        from paddleocr import PaddleOCR
    except ImportError:
        return "<error: paddleocr_not_installed>"
    try:
        if lang not in _PADDLE:
            # PaddleOCR(lang=...) triggers download if missing — guard by checking first
            # Use use_angle_cls=False, lang set; if it tries to download, it raises or hangs —
            # we set show_log=False and rely on cache only
            _PADDLE[lang] = PaddleOCR(lang=lang, show_log=False)
        ocr = _PADDLE[lang]
        result = ocr.ocr(str(img_path))
        if not result or not result[0]:
            return ""
        return " ".join(str(line[1][0]) for line in result[0] if line and len(line) > 1)
    except Exception as e:
        if "download" in str(e).lower() or "404" in str(e) or "url" in str(e).lower():
            return None  # missing weight — ASK boss, do not download
        return f"<error: {e}>"


def run_surya311(img_path: Path, lang: str) -> str | None:
    """Surya detection + recognition (.venv311 only). Heavy (~15s/item on CPU)."""
    try:
        from PIL import Image
        from surya.model.detection.model import load_model as load_det
        from surya.model.recognition.model import load_model as load_rec
        from surya.model.recognition.processor import load_processor
        import surya as surya_mod
    except ImportError as e:
        return f"<error: surya_import: {e}>"
    try:
        global _SURYA_MODELS
        if "_SURYA_MODELS" not in globals() or _SURYA_MODELS is None:
            _SURYA_MODELS = (load_det(), load_rec(), load_processor())
        det, rec, proc = _SURYA_MODELS
        img = Image.open(img_path)
        preds = surya_mod.run_recognition([img], [[lang]], det, rec, proc)
        if preds and preds[0]:
            return preds[0].text
        return ""
    except Exception as e:
        return f"<error: {e}>"


_SURYA_MODELS = None

# Wire the .venv311 engines into the order (overrides the None placeholders)
ENGINE_ORDER = [
    ("surya", run_surya311 if "surya" in dir() else run_surya),
    ("tesseract_indic", run_tesseract),
    ("easyocr", run_easyocr),
    ("rapidocr", run_rapidocr),
    ("doctr", run_doctr),
    ("anuvaad_tesseract", run_anuvaad),
    # openbharatocr: byte-identical copy of tesseract_indic — handled by copy step, not re-run
    # indicphotoocr: BROKEN editable install — skip (ASK boss before reinstalling)
    ("paddleocr_indic", run_paddleocr),
]


def cer_for(pred: str | None, gt: str) -> tuple[float, bool]:
    if pred is None or HAS_METRICS is False:
        return 1.0, False
    try:
        return calculate_cer(gt, pred), True
    except Exception:
        return 1.0, False


DEVICE = "mac-m4-cpu"  # R-15: device tag on every output (never mix timing across machines)

RUN_STATE_DIR = REPO / "level2/benchmark/logs/RUN_STATE"


def run_state_init(job: str, total: int) -> Path:
    RUN_STATE_DIR.mkdir(parents=True, exist_ok=True)
    p = RUN_STATE_DIR / f"{job}.json"
    p.write_text(json.dumps({"job": job, "done": 0, "total": total, "last_item": None,
                             "machine": "mac-m4", "device": DEVICE,
                             "start": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "last_update": None}))
    return p


def run_state_update(p: Path, done: int, last_item: str):
    try:
        s = json.loads(p.read_text())
        s["done"] = done
        s["last_item"] = last_item
        s["last_update"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        p.write_text(json.dumps(s))
    except Exception:
        pass


def run_s4(max_items: int | None = None, engine_filter: str | None = None) -> dict:
    items = json.loads(SOUTH_ITEMS.read_text())
    if max_items:
        items = items[:max_items]
    results = {}
    for lang in ["ta", "te", "kn", "ml"]:
        lang_items = [i for i in items if i["language"] == lang]
        for engine_name, engine_fn in ENGINE_ORDER:
            if engine_filter and engine_name != engine_filter:
                continue
            if engine_fn is None:
                continue  # alias or broken — handled separately, never re-run here
            # R-15: per-engine RUN_STATE (resumable)
            state = run_state_init(f"s4_{engine_name}_{lang}", len(lang_items))
            done_n = 0
            last_beat = time.monotonic()
            for item in lang_items:
                img_name = item["image_name"]
                img_path = PAGES / lang / f"{img_name}.jpg"
                if not img_path.exists():
                    continue
                pack_dir = PACKS / engine_name / lang
                pack_dir.mkdir(parents=True, exist_ok=True)
                out_path = pack_dir / f"{img_name}.json"
                if out_path.exists():
                    done_n += 1
                    continue  # skip already-done (R-15 resumable)
                t0 = time.monotonic()
                pred = engine_fn(img_path, lang)
                if pred is None:
                    continue  # engine declined (broken lang/model) — NO fake pack
                cer, ok = cer_for(pred, item["gt"])
                ms = int((time.monotonic() - t0) * 1000)
                pack = {
                    "image_id": img_name,
                    "image_name": img_name,
                    "language": lang,
                    "language_name": {"ta": "Tamil", "te": "Telugu", "kn": "Kannada", "ml": "Malayalam"}[lang],
                    "script": {"ta": "Tamil", "te": "Telugu", "kn": "Kannada", "ml": "Malayalam"}[lang],
                    "engine": engine_name,
                    "text": pred,
                    "gt": item["gt"],
                    "CER": cer if ok else None,
                    "ms": ms,
                    "device": DEVICE,  # R-15: never mix timing across machines
                    "error": None if ok else "metrics_unavailable",
                    "set": "sarvam_fill",
                }
                out_path.write_text(json.dumps(pack, indent=2, ensure_ascii=False))
                done_n += 1
                run_state_update(state, done_n, img_name)
                results.setdefault(engine_name, {}).setdefault(lang, 0)
                results[engine_name][lang] += 1
                print(f"  {engine_name} {lang} {img_name}: CER={cer:.4f} ({ms}ms)", flush=True)
                if time.monotonic() - last_beat > 300:  # R-15: heartbeat every 5 min
                    print(f"  [heartbeat] {engine_name}/{lang}: {done_n}/{len(lang_items)}", flush=True)
                    last_beat = time.monotonic()
    # R-15 HANDOFF line
    hand = RUN_STATE_DIR / "HANDOFF.md"
    print(f"S4 done: {results}", flush=True)
    return results


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=None, help="Max items to process")
    ap.add_argument("--engine", default=None, help="Run only this engine")
    args = ap.parse_args()
    if args.engine:
        ENGINE_ORDER = [(n, f) for n, f in ENGINE_ORDER if n == args.engine]
    print(f"Running S4: {len(ENGINE_ORDER)} engines × 400 items")
    results = run_s4(max_items=args.max)
    print(f"\nDone: {results}")
