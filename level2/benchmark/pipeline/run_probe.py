#!/usr/bin/env python3
"""OCR the 20-per-lang probe (already on disk). Writes probe22/out only."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
L2 = ROOT
BENCH = L2 / "benchmark"
MANIFEST = BENCH / "manifest_v2.json"
IMAGES = BENCH / "pages"
OUT = BENCH / "packs"
TESSDATA = BENCH / "tessdata"

TESS_LANG = {
    "en": "eng",
    "as": "asm+eng",
    "bn": "ben+eng",
    "brx": "hin+eng",
    "doi": "hin+eng",
    "gu": "guj+eng",
    "hi": "hin+eng",
    "ks": "urd+hin+eng",
    "kok": "hin+eng",
    "mai": "hin+eng",
    "mni": "eng",
    "mr": "mar+hin+eng",
    "ne": "nep+hin+eng",
    "or": "ori+eng",
    "pa": "pan+eng",
    "sa": "san+hin+eng",
    "sat": "eng",
    "sd": "snd+hin+eng",
    "ur": "urd+eng",
    "te": "tel+hin+eng",
    "ta": "tam+hin+eng",
    "kn": "kan+hin+eng",
    "ml": "mal+hin+eng",
}

# EasyOCR pairwise-valid pairs (engine constraint).
EASY_FOR = {
    # Cached-weights-only mapping (hard rule: no downloads mid-run).
    # ~/.EasyOCR/model holds: arabic, assamese, bengali, craft, devanagari,
    # english_g2, kannada, tamil, telugu, urdu. easyocr has NO upstream models
    # for gu/or/pa/mni/sat/sd — those fall back to en (honest capability limit).
    "en": ["en"],
    "as": ["as", "en"],   # Assamese: assamese.pth cached (user-approved 2026-09-26)
    "bn": ["bn", "en"],
    "hi": ["hi", "en"],
    "mr": ["hi", "mr", "ne", "en"],
    "ne": ["hi", "mr", "ne", "en"],
    "brx": ["hi", "mr", "ne", "en"],
    "doi": ["hi", "mr", "ne", "en"],
    "kok": ["hi", "mr", "ne", "en"],
    "mai": ["hi", "mr", "ne", "en"],
    "sa": ["hi", "mr", "ne", "en"],
    "sd": ["ur", "en"],    # Sindhi: Perso-Arabic; urdu.pth (Nastaliq) closer than arabic
    "ur": ["ur", "en"],    # Urdu: Nastaliq — urdu.pth cached (user-approved 2026-09-26)
    "ks": ["ur", "en"],    # Kashmiri: Perso-Arabic — urdu.pth cached
    "gu": ["en"],
    "or": ["en"],
    "pa": ["en"],
    "mni": ["en"],
    "sat": ["en"],
    "te": ["te", "en"],
    "ta": ["ta", "en"],
    "kn": ["kn", "en"],
    "ml": ["ml", "en"],
}

# Max-power mapping per paddleocr 3.7 _utils/langs.py (verified 2026-09-26):
# te/ta -> PP-OCRv5, kn -> ka (PP-OCRv3), hi/mr/ne/mai/sa/kok(gom) -> v5 devanagari,
# ur/sd -> v5 arabic. Languages without any paddle model (as bn brx doi gu ks or pa
# mni sat ml) return honest-empty — same policy as South-400 ml and rapidocr.
PADDLE_LANG = {
    "te": "te", "ta": "ta", "kn": "ka",
    "hi": "hi", "mr": "mr", "ne": "ne", "mai": "mai", "sa": "sa", "kok": "gom",
    "ur": "ur", "sd": "sd", "en": "en",
}


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "")


SET_EXT = {
    "probe18": ".jpg",
    "official_pair": ".jpg",
    "sarvam_fill": ".jpg",
    "official_pdf": ".png",
    "en_sanity": ".jpg",
}


def image_path(item: dict) -> Path:
    ext = SET_EXT.get(item["set"], ".png")
    base = IMAGES / item["language"] / item["image_id"]
    for e in (ext, ".jpg", ".jpeg", ".png"):
        p = base.with_suffix(e)
        if p.exists() or p.is_symlink():
            return p
    raise FileNotFoundError(base.with_suffix(ext))


def out_path(engine: str, item: dict) -> Path:
    p = OUT / engine / item["language"] / f"{item['image_id']}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def write_pack(engine: str, item: dict, text: str, ms: int, err: str | None = None) -> None:
    pack = {
        "image_id": item["image_id"],
        "image_name": item.get("image_name"),
        "language": item["language"],
        "language_name": item.get("language_name"),
        "script": item.get("script"),
        "engine": engine,
        "text": nfc(text),
        "gt": item.get("gt") or "",
        "ms": ms,
        "error": err,
        "set": item.get("set"),
    }
    out_path(engine, item).write_text(json.dumps(pack, ensure_ascii=False, indent=2))


def ocr_tesseract(item: dict) -> str:
    img = image_path(item)
    lang = TESS_LANG[item["language"]]
    cmd = ["tesseract", str(img), "stdout", "-l", lang, "--psm", "6", "--tessdata-dir", str(TESSDATA)]
    r = subprocess.run(cmd, capture_output=True, timeout=300)
    if r.returncode != 0:
        r = subprocess.run(
            ["tesseract", str(img), "stdout", "-l", "hin+eng", "--psm", "6", "--tessdata-dir", str(TESSDATA)],
            capture_output=True,
            timeout=300,
        )
    return nfc(r.stdout.decode("utf-8", errors="replace"))


_easy = {}


def ocr_easyocr(item: dict) -> str:
    import easyocr

    langs = EASY_FOR.get(item["language"], ["en"])
    key = "+".join(langs)
    if key not in _easy:
        _easy[key] = easyocr.Reader(langs, gpu=False)
    parts = _easy[key].readtext(str(image_path(item)), detail=0, paragraph=True)
    text = "\n".join(str(p) for p in parts) if isinstance(parts, list) else str(parts)
    return nfc(text)


_paddle = {}


def ocr_paddle(item: dict) -> str:
    from paddleocr import PaddleOCR

    lang = PADDLE_LANG.get(item["language"])
    if lang is None:
        return ""  # honest-empty: no paddle model exists for this script
    init_kw = dict(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        # Cap det input: PP-OCRv5 server det on a 4000px scan peaks ~57GB RSS and
        # gets OOM-killed by macOS (verified 2026-09-26). 1600px keeps memory sane
        # without losing line detection on full-page scans.
        text_det_limit_side_len=1600,
        text_det_limit_type="max",
    )
    if lang not in _paddle:
        try:
            _paddle[lang] = PaddleOCR(lang=lang, **init_kw)
        except Exception:
            _paddle[lang] = PaddleOCR(lang="en", **init_kw)
    pipe = _paddle[lang]
    res = pipe.ocr(str(image_path(item)))
    lines = []
    if res:
        page = res[0]
        if isinstance(page, dict) and "rec_texts" in page:
            lines = [str(t) for t in page["rec_texts"] if t]
        elif isinstance(page, list):
            for row in page:
                if row and len(row) >= 2 and row[1]:
                    lines.append(str(row[1][0]))
    return nfc("\n".join(lines))


def ocr_surya(item: dict) -> str:
    sys.path.insert(0, str(L2))
    from run_engine import ocr_surya as _s

    return _s(image_path(item), item["language"])


def ocr_doctr(item: dict) -> str:
    sys.path.insert(0, str(L2))
    from run_engine import ocr_doctr as _d

    return _d(image_path(item), item["language"])


ANUVAAD_TESSDATA = L2 / "research" / "smoke" / "anuvaad_tesseract" / "tessdata"

# Anuvaad's own tessdata ships only South models + hin + eng. Devanagari-family
# probe languages get the hin+eng stack (real attempt); other scripts have no
# anuvaad model -> honest-empty, matching the South-400 ml precedent.
ANUVAAD_FOR = {
    "hi": "hin+eng", "mr": "hin+eng", "sa": "hin+eng", "ne": "hin+eng",
    "mai": "hin+eng", "kok": "hin+eng", "brx": "hin+eng", "doi": "hin+eng",
}


def ocr_tesseract_bilingual(item: dict) -> str:
    """eng + native-language pack from probe22/tessdata (bilingual basis)."""
    parts = ["eng"] + TESS_LANG[item["language"]].split("+")
    seen: set[str] = set()
    stack = []
    for p in parts:
        if p and p not in seen:
            seen.add(p)
            stack.append(p)
    r = subprocess.run(
        ["tesseract", str(image_path(item)), "stdout", "-l", "+".join(stack),
         "--psm", "6", "--tessdata-dir", str(TESSDATA)],
        capture_output=True, timeout=300,
    )
    return nfc(r.stdout.decode("utf-8", errors="replace"))


def ocr_openbharatocr(item: dict) -> str:
    """openbharatocr is a pytesseract wrapper; documented fallback = tesseract_indic."""
    return ocr_tesseract(item)


def ocr_anuvaad_tesseract(item: dict) -> str:
    """Anuvaad-tuned tesseract models; hin+eng from its own dir for Devanagari
    family, honest-empty elsewhere (no anuvaad model for those scripts)."""
    stack = ANUVAAD_FOR.get(item["language"])
    if not stack:
        return ""
    r = subprocess.run(
        ["tesseract", str(image_path(item)), "stdout", "-l", stack,
         "--psm", "6", "--tessdata-dir", str(ANUVAAD_TESSDATA)],
        capture_output=True, timeout=300,
    )
    if r.returncode != 0:
        return ""
    return nfc(r.stdout.decode("utf-8", errors="replace"))


def ocr_indicphotoocr(item: dict) -> str:
    sys.path.insert(0, str(L2))
    from run_engine import ocr_indicphotoocr as _i

    return _i(image_path(item), item["language"])


# RapidOCR: only cached/bundled rec models are used (te/ta/ka; probe18 has none
# of them). DEVANAGARI (hi mr sa ne mai kok brx doi) and ARABIC (ur sd ks) rec
# models exist upstream but are NOT on disk — enabling them triggers a runtime
# model download, which is gated behind explicit user approval.
RAPID_EXTRA_MODELS_APPROVED = True  # user authorized max-power benchmark 2026-09-26 ("make it 100%")

_RAPID_LANGV = {
    "te": ("TE", "PPOCRV5"),
    "ta": ("TA", "PPOCRV5"),
    "kn": ("KA", "PPOCRV4"),
}
if RAPID_EXTRA_MODELS_APPROVED:
    for _l in ("hi", "mr", "sa", "ne", "mai", "kok", "brx", "doi"):
        _RAPID_LANGV[_l] = ("DEVANAGARI", "PPOCRV5")
    for _l in ("ur", "sd", "ks"):
        _RAPID_LANGV[_l] = ("ARABIC", "PPOCRV5")
    # EN-fix applied 2026-09-28 (orchestrator): add "en" to _RAPID_LANGV so EN sanity runs
    _RAPID_LANGV["en"] = ("EN", "PPOCRV4")


_rapid: dict[str, object] = {}


def ocr_rapidocr(item: dict) -> str:
    from rapidocr import RapidOCR
    from rapidocr.utils.typings import LangRec, OCRVersion, ModelType, LangDet

    lang = item["language"]
    if lang not in _RAPID_LANGV:
        return ""  # honest-empty: no cached rapidocr model for this script
    lrec_name, ver_name = _RAPID_LANGV[lang]
    lrec = getattr(LangRec, lrec_name)
    ver = getattr(OCRVersion, ver_name)
    if lang not in _rapid:
        params = {
            "Rec.lang_type": lrec, "Rec.ocr_version": ver, "Rec.model_type": ModelType.MOBILE,
            "Det.ocr_version": OCRVersion.PPOCRV5, "Det.model_type": ModelType.MOBILE,
            "Det.lang_type": LangDet.CH, "Cls.use_cls": False,
        }
        _rapid[lang] = RapidOCR(params=params)
    result = _rapid[lang](str(image_path(item)))
    txts = getattr(result, "txts", None) or []
    return nfc("\n".join(str(t) for t in txts if t))


# Sarvam Vision (doc_ai digitise) — engine #11. Cloud API; key read from env or
# repo-root .env (never hardcoded, never printed). Free-trial credits only:
# runs are gated by --limit-per-lang so agents cannot silently burn credits.
_sarvam_client = None


def _sarvam_key() -> str:
    key = os.environ.get("SARVAM_API_KEY")
    if key:
        return key
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                if k.strip() == "SARVAM_API_KEY" and v.strip():
                    return v.strip()
    raise RuntimeError("SARVAM_API_KEY missing (set env or put it in South/.env)")


def ocr_sarvam_vision(item: dict) -> str:
    global _sarvam_client
    from sarvamai import SarvamAI

    if _sarvam_client is None:
        _sarvam_client = SarvamAI(api_subscription_key=_sarvam_key())
    img_path = image_path(item)
    mime = "image/png" if img_path.suffix.lower() == ".png" else "image/jpeg"
    job = _sarvam_client.doc_ai.digitise(
        file=[(img_path.name, img_path.read_bytes(), mime)],
        output_format="md", content_type="printed",
    )
    deadline = time.time() + 90
    while time.time() < deadline:
        time.sleep(3)
        status = _sarvam_client.doc_ai.get_status(job.job_id)
        st = getattr(status, "status", str(status))
        if st and "COMPLETED" in st.upper():
            break
        if st and st.upper() in ("FAILED", "ERROR"):
            return ""
    res = _sarvam_client.doc_ai.get_results(job.job_id)
    data = res.model_dump() if hasattr(res, "model_dump") else res
    pages = []
    for doc in (data.get("documents") or []):
        for page in (doc.get("pages") or []):
            blocks = page.get("blocks") or []
            blocks = sorted(blocks, key=lambda b: (b.get("reading_order") or 0))
            for b in blocks:
                if b.get("text"):
                    # digitise emits markdown; strip HTML table markup so CER
                    # measures text, not tags (documented engine post-processing)
                    pages.append(re.sub(r"<[^>]+>", " ", str(b["text"])))
    return nfc("\n".join(p for p in pages if p.strip()))


RUNNERS = {
    "tesseract_indic": ocr_tesseract,
    "easyocr": ocr_easyocr,
    "paddleocr_indic": ocr_paddle,
    "surya": ocr_surya,
    "doctr": ocr_doctr,
    "tesseract_bilingual": ocr_tesseract_bilingual,
    "openbharatocr": ocr_openbharatocr,
    "anuvaad_tesseract": ocr_anuvaad_tesseract,
    "indicphotoocr": ocr_indicphotoocr,
    "rapidocr": ocr_rapidocr,
    "sarvam_vision": ocr_sarvam_vision,
}


def pack_needs_retry(p: Path) -> bool:
    """A pack is broken if it has an error or empty text — safe to re-run."""
    try:
        d = json.loads(p.read_text())
        return bool(d.get("error")) or not (d.get("text") or "").strip()
    except Exception:
        return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", required=True, choices=list(RUNNERS))
    ap.add_argument("--skip-existing", action="store_true")
    ap.add_argument("--retry-errors", action="store_true",
                    help="with --skip-existing, re-run packs whose JSON has a non-null error or empty text (protocol §5: never delete, rerun error packs)")
    ap.add_argument("--manifest", type=Path, default=MANIFEST,
                    help="manifest to run against (default: benchmark/manifest_v2.json)")
    ap.add_argument("--limit-per-lang", type=int, default=None,
                    help="run at most the first N items per language (credit guard for cloud engines)")
    args = ap.parse_args()
    items = json.loads(args.manifest.read_text())["items"]
    if args.limit_per_lang:
        kept, counts = [], {}
        for it in items:
            c = counts.get(it["language"], 0)
            if c < args.limit_per_lang:
                kept.append(it)
                counts[it["language"]] = c + 1
        items = kept
    fn = RUNNERS[args.engine]
    done = fail = 0
    t0 = time.time()
    for i, item in enumerate(items, 1):
        dest = out_path(args.engine, item)
        if dest.exists() and args.skip_existing:
            if not (args.retry_errors and pack_needs_retry(dest)):
                done += 1
                continue
        t1 = time.time()
        err = None
        text = ""
        try:
            text = fn(item)
        except Exception as e:
            err = str(e)
            fail += 1
        write_pack(args.engine, item, text, int((time.time() - t1) * 1000), err)
        done += 1
        if i % 20 == 0 or i == len(items):
            print(
                f"{args.engine} {i}/{len(items)} nonempty={sum(1 for _ in [1] if text.strip())} fail={fail} {time.time()-t0:.0f}s",
                flush=True,
            )
    print(f"DONE {args.engine} {done} fail={fail} {time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
