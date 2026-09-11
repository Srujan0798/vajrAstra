#!/bin/zsh
# Continue Level-2 engines until complete (safe to re-run / loop).
set -euo pipefail
cd /Users/srujansai/Desktop/South

PY314="./.venv/bin/python"
PY311="./.venv311/bin/python"

count() {
  local eng="$1"
  find "level2/out/$eng" -name '*.json' 2>/dev/null | wc -l | tr -d ' '
}

echo "=== STATUS $(date) ==="
for eng in tesseract_indic easyocr openbharatocr indicphotoocr paddleocr_indic; do
  echo "$eng: $(count "$eng")/400"
done

# 1) Finish tesseract on py3.14 venv
if [ "$(count tesseract_indic)" -lt 400 ]; then
  echo "CONTINUE tesseract_indic"
  "$PY314" level2/run_engine.py --engine tesseract_indic --skip-existing | tee -a level2/tesseract_indic_run.log
fi

# Need py3.11 for the rest
if [ ! -x "$PY311" ]; then
  echo "WAIT: .venv311 not ready yet"
  exit 0
fi

# 2) easyocr
if [ "$(count easyocr)" -lt 400 ]; then
  echo "CONTINUE easyocr"
  "$PY311" level2/run_engine.py --engine easyocr --skip-existing | tee -a level2/easyocr_run.log
fi

# 3) openbharatocr (full-page fallback uses tesseract path inside runner if needed)
if [ "$(count openbharatocr)" -lt 400 ]; then
  echo "CONTINUE openbharatocr"
  "$PY311" level2/run_engine.py --engine openbharatocr --skip-existing | tee -a level2/openbharatocr_run.log || true
fi

# 4) indicphotoocr
if [ "$(count indicphotoocr)" -lt 400 ]; then
  echo "CONTINUE indicphotoocr"
  "$PY311" level2/run_engine.py --engine indicphotoocr --skip-existing | tee -a level2/indicphotoocr_run.log || true
fi

# 5) paddleocr_indic
if [ "$(count paddleocr_indic)" -lt 400 ]; then
  echo "CONTINUE paddleocr_indic"
  "$PY311" level2/run_engine.py --engine paddleocr_indic --skip-existing | tee -a level2/paddleocr_indic_run.log || true
fi

echo "=== FINAL STATUS $(date) ==="
all_done=1
for eng in tesseract_indic easyocr openbharatocr indicphotoocr paddleocr_indic; do
  n=$(count "$eng")
  echo "$eng: $n/400"
  if [ "$n" -lt 400 ]; then all_done=0; fi
done

if [ "$all_done" -eq 1 ]; then
  echo "ALL_FIVE_ENGINES_COMPLETE"
else
  echo "STILL_RUNNING_OR_BLOCKED"
fi
