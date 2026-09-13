#!/bin/bash
# vajrAstra L2 — ONE-COMMAND DEMO
# Usage: ./level2/demo/demo.sh          (refresh reports, print one-screen, open review UI)
#       ./level2/demo/demo.sh --no-refresh   (skip report.py; instant open)
set -euo pipefail
cd "$(dirname "$0")/../.."   # repo root

PY=".venv/bin/python"

echo "=== vajrAstra L2 DEMO ==="
if [ "${1:-}" = "--no-refresh" ]; then
  echo "[demo.sh] --no-refresh: skipping report.py"
else
  echo "[demo.sh] refreshing reports (verify_v2 -> deep_verify x10 -> report_gen -> seal)…"
  "$PY" level2/report.py
fi

echo
echo "[demo.sh] rebuilding review bundle (top 30 disagreement pages)…"
"$PY" level2/research/review_demo_gen.py --top 30

echo
echo "================ SEP16 ONE SCREEN ================"
cat level2/reports/SEP16_ONE_SCREEN.md

echo
echo "[demo.sh] opening Human Review Console…"
if command -v open >/dev/null 2>&1; then
  open level2/demo/review.html          # macOS
else
  xdg-open level2/demo/review.html 2>/dev/null || \
    echo "[demo.sh] open manually: level2/demo/review.html"
fi
echo "[demo.sh] done — verdicts persist in localStorage; 'Export verdicts JSON' copies to clipboard."
