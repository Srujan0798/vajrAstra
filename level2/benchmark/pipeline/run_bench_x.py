"""
run_bench_x.py — proto-104 §X prep

NEW file (per NEXT.md REV 4 T7). Runs one engine on the Sarvam Indic OCR Bench test split
with --skip-existing. Scores via the bench's own metrics.py --normalize. Dry run 5 items; stop.

Supports multiple engines: tesseract_indic, surya (local cached), paddleocr_indic, indicphotoocr.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from level2.benchmark.pipeline.metrics import (
    calculate_cer, normalize_for_metrics,
)


def _load_bench_parquets() -> pd.DataFrame:
    """Load all Sarvam Indic OCR Bench parquet parts."""
    paths = [
        "level2/models_bodhan/indic-ocr-bench/small_representative/small_representative-00000-of-00001.parquet",
        "level2/models_bodhan/indic-ocr-bench/test/test-00000-of-00002.parquet",
        "level2/models_bodhan/indic-ocr-bench/test/test-00001-of-00002.parquet",
    ]
    frames = []
    for p in paths:
        f = Path(p)
        if not f.exists():
            print(f"[warn] bench parquet not found: {f}")
            continue
        frames.append(pd.read_parquet(f))
    if not frames:
        raise FileNotFoundError("no bench parquets found under level2/models_bodhan/indic-ocr-bench/")
    return pd.concat(frames, ignore_index=True)


# Mapping from display language name to tesseract 3-letter code
_LANG_CODE_MAP = {
    "Hindi": "hin", "Telugu": "tel", "Kannada": "kan", "Malayalam": "mal",
    "Tamil": "tam", "Bengali": "ben", "Gujarati": "guj", "Punjabi": "pan",
    "Odia": "ori", "Assamese": "asm", "Marathi": "mar", "Urdu": "urd",
    "English": "eng", "Bodo": "brx", "Dogri": "doi",
    "Kashmiri": "kas", "Maithili": "mai", "Nepali": "nep",
    "Sanskrit": "san", "Santhali": "snd", "Konkani": "kok",
    "Manipuri": "mni",
}


def _recognize_tesseract(img, lang_code: str) -> str:
    """Tesseract OCR on image."""
    import pytesseract
    try:
        return pytesseract.image_to_string(img, lang=lang_code)
    except Exception as e:
        print(f"[err] tesseract failed for {lang_code}: {e}")
        return ""


def _recognize_surya(img) -> str:
    """Surya OCR on image."""
    try:
        from surya.recognition import RecognitionPredictor
        from PIL import Image
        import io
        
        # Initialize predictor (cached after first use)
        if not hasattr(_recognize_surya, "_predictor"):
            print("[info] loading surya predictor (first time, cached after)...")
            _recognize_surya._predictor = RecognitionPredictor()
        predictor = _recognize_surya._predictor
        results = predictor([img])
        if results:
            result = results[0]
            # Extract text
            if hasattr(result, 'text'):
                return result.text
            if hasattr(result, 'text_lines'):
                return ' '.join(result.text_lines or [])
        return ""
    except Exception as e:
        print(f"[err] surya failed: {e}")
        return ""


def _recognize_paddleocr(img, lang: str) -> str:
    """PaddleOCR on image."""
    try:
        from paddleocr import PaddleOCR
        if not hasattr(_recognize_paddleocr, "_ocr"):
            _recognize_paddleocr._ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
        result = _recognize_paddleocr._ocr.ocr(img, cls=True)
        if result and result[0]:
            lines = result[0]
            return '\n'.join([line[1][0] for line in lines if line[1]])
        return ""
    except Exception as e:
        print(f"[err] paddleocr failed: {e}")
        return ""


def _recognize_indicphotoocr(img) -> str:
    """IndicPhotoOCR on image."""
    try:
        import indicphotoocr
        from pathlib import Path
        from PIL import Image
        import tempfile
        
        # IndicPhotoOCR expects file path or bytes
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            img.save(tmp.name, 'JPEG')
            tmp_path = tmp.name
        
        try:
            # Try common APIs
            if hasattr(indicphotoocr, 'OCR'):
                ocr = indicphotoocr.OCR()
                result = ocr.run(tmp_path)
                if hasattr(result, 'text'):
                    return result.text
                return str(result)
            elif hasattr(indicphotoocr, 'ocr'):
                result = indicphotoocr.ocr(tmp_path)
                return str(result)
            return ""
        finally:
            Path(tmp_path).unlink(missing_ok=True)
    except Exception as e:
        print(f"[err] indicphotoocr failed: {e}")
        return ""


_RECOGNIZERS = {
    "tesseract_indic": _recognize_tesseract,
    "surya": _recognize_surya,
    "paddleocr_indic": _recognize_paddleocr,
    "indicphotoocr": _recognize_indicphotoocr,
}


def run_one(
    bench: pd.DataFrame,
    engine: str = "tesseract_indic",
    dry_run_n: int = 5,
    output_dir: Path = Path("level2/benchmark/packs/test_runs/run_bench_x"),
) -> List[Dict[str, Any]]:
    """Dry-run one engine on a few bench items. Returns per-item metrics."""
    from PIL import Image
    import io

    if engine not in _RECOGNIZERS:
        print(f"[err] unknown engine: {engine}; available: {list(_RECOGNIZERS.keys())}")
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    sample = bench.head(dry_run_n)
    results = []
    
    recognizer = _RECOGNIZERS[engine]
    
    for i, row in sample.iterrows():
        img_bytes = row["image"]["bytes"]
        img_name = row["image_name"]
        gt_text = normalize_for_metrics(row["gt"])
        lang = row["language"]
        lang_code = _LANG_CODE_MAP.get(lang, "eng")

        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        
        try:
            if engine == "tesseract_indic":
                pred_text = recognizer(img, lang_code)
            else:
                pred_text = recognizer(img)
            
            pred_text = normalize_for_metrics(pred_text)
            cer = calculate_cer(gt_text, pred_text) if gt_text and pred_text else 1.0
        except Exception as e:
            pred_text = ""
            cer = 1.0
            print(f"[err] {img_name}: {engine} error: {e}")

        result = {
            "image_name": img_name,
            "language": lang,
            "lang_code": lang_code,
            "engine": engine,
            "gt_len": len(gt_text),
            "pred_len": len(pred_text),
            "cer": round(cer, 4),
        }
        results.append(result)
        print(f"[{engine}] {img_name} ({lang}/{lang_code}): CER={result['cer']:.3f} (gt={result['gt_len']}, pred={result['pred_len']})")

    out_path = output_dir / f"dry_run_{engine}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nWrote: {out_path}")

    cers = [r["cer"] for r in results if r["gt_len"] > 0]
    if cers:
        avg_cer = sum(cers) / len(cers)
        print(f"Avg CER ({len(cers)} items with traineddata): {avg_cer:.3f}")
    return results


def main():
    parser = argparse.ArgumentParser(description="run_bench_x — Sarvam bench dry run")
    parser.add_argument("--engine", default="tesseract_indic",
                        choices=["tesseract_indic", "surya", "paddleocr_indic", "indicphotoocr"],
                        help="Engine to use (default: tesseract_indic)")
    parser.add_argument("--n", type=int, default=5, help="Number of items for dry run")
    parser.add_argument("--output-dir", type=Path,
                        default=Path("level2/benchmark/packs/test_runs/run_bench_x"),
                        help="Output directory for results")
    args = parser.parse_args()

    bench = _load_bench_parquets()
    print(f"Loaded {len(bench)} bench items")
    run_one(bench, engine=args.engine, dry_run_n=args.n, output_dir=args.output_dir)


if __name__ == "__main__":
    main()
