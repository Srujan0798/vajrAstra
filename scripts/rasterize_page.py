"""
Rasterize one PDF page to PNG for labeling/review.
SETUP TOOL ONLY — does not write label JSON.

Usage:
  python scripts/rasterize_page.py work/te/s_telugu0001pro_raw.pdf --page 0 --out /tmp/te_001.png
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pymupdf


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--page", type=int, default=0, help="0-based page index")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    doc = pymupdf.open(args.pdf)
    if args.page < 0 or args.page >= doc.page_count:
        raise SystemExit(f"page {args.page} out of range 0..{doc.page_count - 1}")
    page = doc[args.page]
    zoom = args.dpi / 72.0
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    pix.save(str(args.out))
    doc.close()
    print(f"OK {args.pdf.name} p{args.page} -> {args.out} ({pix.width}x{pix.height} @{args.dpi}dpi)")


if __name__ == "__main__":
    main()
