"""
SOUTH setup inventory — file counts, PDF page counts, text-layer scout.
Usage: python scripts/inventory.py work
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

EXTS_IMG = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}

try:
    import pymupdf

    HAVE_FITZ = True
except ImportError:
    HAVE_FITZ = False


def scout_pdf(path: Path) -> tuple[int, bool]:
    """Return (page_count, has_text_on_first_pages)."""
    if not HAVE_FITZ:
        return 0, False
    try:
        doc = pymupdf.open(path)
        pages = doc.page_count
        has_text = any(doc[i].get_text().strip() for i in range(min(3, pages)))
        doc.close()
        return pages, has_text
    except Exception:
        return 0, False


def inventory(root: Path) -> dict:
    stats: dict = {}
    for dirpath, _, files in os.walk(root):
        for fn in files:
            p = Path(dirpath) / fn
            if p.name.startswith("."):
                continue
            rel = p.relative_to(root)
            top = rel.parts[0] if rel.parts else "_root"
            e = stats.setdefault(
                top,
                {
                    "files": 0,
                    "images": 0,
                    "pdfs": 0,
                    "pdf_pages": 0,
                    "pdf_with_text": 0,
                    "other": 0,
                    "bytes": 0,
                },
            )
            e["files"] += 1
            e["bytes"] += p.stat().st_size
            ext = p.suffix.lower()
            if ext in EXTS_IMG:
                e["images"] += 1
            elif ext == ".pdf":
                e["pdfs"] += 1
                pages, has_text = scout_pdf(p)
                e["pdf_pages"] += pages
                if has_text:
                    e["pdf_with_text"] += 1
            else:
                e["other"] += 1
    return stats


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/inventory.py <root_dir>", file=sys.stderr)
        sys.exit(2)
    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        sys.exit(1)
    stats = inventory(root)
    print(json.dumps(stats, indent=2))
    total_files = sum(v["files"] for v in stats.values())
    total_bytes = sum(v["bytes"] for v in stats.values())
    total_pages = sum(v["pdf_pages"] for v in stats.values())
    text_pdfs = sum(v["pdf_with_text"] for v in stats.values())
    print(
        f"\nTOTAL: {total_files} files, {total_bytes / 1e9:.2f} GB, "
        f"{total_pages} PDF pages scanned"
    )
    print(f"PDFs with text layer (free GT candidates): {text_pdfs}")
    if not HAVE_FITZ:
        print("WARNING: pymupdf not installed — PDF page/text stats are zero.")


if __name__ == "__main__":
    main()
