#!/usr/bin/env bash
# Fresh-machine setup for the vajrAstra Level-2 benchmark (one command).
# Creates venvs, installs engine deps, downloads tessdata + anuvaad weights,
# verifies imports, and prints the first orchestrator status.
# Usage: bash scripts/setup_fresh_machine.sh
set -euo pipefail

cd "$(dirname "$0")/.."
echo "== vajrAstra Level-2 fresh-machine setup =="
echo "Python 3.14 (tesseract family): $(python3.14 --version 2>/dev/null || echo MISSING)"
echo "Python 3.11 (paddle/easyocr/surya/doctr family): $(python3.11 --version 2>/dev/null || echo MISSING)"

if [ ! -d .venv ]; then
  python3.14 -m venv .venv
  .venv/bin/pip install -q --upgrade pip
  .venv/bin/pip install -q pymupdf pillow pytesseract
fi
if [ ! -d .venv311 ]; then
  python3.11 -m venv .venv311
  .venv311/bin/pip install -q --upgrade pip
  .venv311/bin/pip install -q "pymupdf>=1.24" pillow pytesseract \
    "easyocr==1.7.2" "paddleocr==3.7.0" "paddlepaddle==3.3.1" \
    "rapidocr==3.9.2" omegaconf "python-doctr==1.1.0" "surya-ocr==0.22.1" \
    "numpy==1.26.4" "opencv-python==4.6.0.66" scikit-image
  # openbharatocr pins easyocr==1.7.1 (stale; we run 1.7.2 — proven coexisting)
  .venv311/bin/pip install -q --no-deps "openbharatocr==0.4.3"
fi

if command -v tesseract >/dev/null 2>&1; then
  echo "tesseract: $(tesseract --version | head -1)"
else
  echo "install tesseract: brew install tesseract tesseract-lang"
fi

mkdir -p level2/research/smoke/anuvaad_tesseract/tessdata
echo "tessdata present: $(ls /opt/homebrew/share/tessdata/ 2>/dev/null | grep -c traineddata || echo 0) models (need eng tel tam kan mal hin)"

echo "== verifying imports =="
.venv/bin/python - <<'EOF'
import pymupdf, pytesseract, PIL
print("venv 3.14: pymupdf/pytesseract/PIL OK")
EOF
.venv311/bin/python - <<'EOF'
import easyocr, paddleocr, rapidocr_onnxruntime
from doctr.io import DocumentFile
import surya, openbharatocr
print("venv311: all 311-family engines import OK")
EOF

echo "== dataset + manifest check =="
.venv/bin/python - <<'EOF'
import json, os
m = json.load(open("level2/pages_manifest.json"))
missing = [x["raw_path"] for x in m if not os.path.exists(x["raw_path"])]
print(f"manifest: {len(m)} pages, missing raw: {len(missing)}")
if missing:
    print("populate Datasets/ from the team Drive first:", missing[:5])
EOF

echo "== first status =="
.venv311/bin/python level2/orchestrator.py status
echo "setup complete — run: nohup .venv311/bin/python level2/orchestrator.py autoloop 30 &"
