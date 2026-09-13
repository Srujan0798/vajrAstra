#!/usr/bin/env python3
"""Measure preprocessing uplift (binarize + deskew + 300dpi) on historical empty pages."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
RENDERS = L2 / "renders_shared"

HISTORICAL_EMPTY = [
    "te_011", "te_013", "te_024", "te_065", "te_097",
    "ta_005", "ta_016", "ta_033", "ta_044", "ta_081",
    "kn_005", "kn_020", "kn_033", "kn_050", "kn_075",
    "ml_014", "ml_020", "ml_027", "ml_039", "ml_052",
]

def main():
    import pytesseract
    from PIL import Image
    
    results = []
    for pid in HISTORICAL_EMPTY:
        base = RENDERS / f"{pid}.png"
        bin_ = RENDERS / f"{pid}_bin.png"
        if not base.exists():
            continue
        
        base_text = pytesseract.image_to_string(Image.open(base), lang="tel+hin+eng")
        base_chars = len(base_text.strip())
        
        bin_chars = 0
        if bin_.exists():
            bin_text = pytesseract.image_to_string(Image.open(bin_), lang="tel+hin+eng")
            bin_chars = len(bin_text.strip())
        
        uplift = bin_chars - base_chars
        results.append({
            "page_id": pid, "base_chars": base_chars, "bin_chars": bin_chars,
            "uplift": uplift, "improved": uplift > 0
        })
        print(f"{pid}: base={base_chars}, bin={bin_chars}, uplift={uplift}")

    print("\nSummary:")
    total = len(results)
    improved = sum(1 for r in results if r["improved"])
    avg_uplift = sum(r["uplift"] for r in results) / len(results) if results else 0
    print(f"Total tested: {total}")
    print(f"Improved by binarization: {improved}/{total}")
    print(f"Avg uplift: {avg_uplift:.1f} chars")

    (Path("level2/reports") / "PREPROCESSING_UPLIFT.json").write_text(
        json.dumps({
            "historical_empty_pages": HISTORICAL_EMPTY,
            "engine": "tesseract_indic", "dpi_tested": 200,
            "results": results,
            "summary": {"total_tested": total, "improved_by_binarization": improved, "avg_uplift_chars": round(avg_uplift, 1)}
        }, indent=2, ensure_ascii=False)
    )
    print("Saved to level2/reports/PREPROCESSING_UPLIFT.json")

if __name__ == "__main__":
    import pytesseract
    from PIL import Image
    main()
