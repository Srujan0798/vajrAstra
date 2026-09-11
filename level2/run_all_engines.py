#!/usr/bin/env python3
"""
Run all Level-2 engines in order until each has 400 JSON outputs (or is skipped as unavailable).

Usage:
  python level2/run_all_engines.py
  python level2/run_all_engines.py --status-only
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
ENGINES = [
    "tesseract_indic",
    "easyocr",
    "openbharatocr",
    "indicphotoocr",
    "paddleocr_indic",  # may be unavailable on py3.14
]
TARGET = 400


def count_json(engine: str) -> int:
    d = L2 / "out" / engine
    if not d.exists():
        return 0
    return sum(1 for _ in d.rglob("*.json"))


def status() -> dict:
    st = {}
    for eng in ENGINES:
        n = count_json(eng)
        st[eng] = {"json_files": n, "complete": n >= TARGET}
    st["all_complete"] = all(v["complete"] for v in st.values() if isinstance(v, dict) and "complete" in v)
    # paddle may never complete on this python — mark separately
    return st


def run_engine(engine: str) -> int:
    cmd = [
        sys.executable,
        str(L2 / "run_engine.py"),
        "--engine",
        engine,
        "--skip-existing",
    ]
    log = L2 / f"{engine}_run.log"
    print(f"=== START {engine} (log={log.name}) ===", flush=True)
    with log.open("a", encoding="utf-8") as f:
        f.write(f"\n--- launch ---\n")
        proc = subprocess.run(cmd, cwd=str(ROOT), stdout=f, stderr=subprocess.STDOUT)
    print(f"=== END {engine} exit={proc.returncode} json={count_json(engine)} ===", flush=True)
    return proc.returncode


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--status-only", action="store_true")
    args = ap.parse_args()

    st = status()
    print(json.dumps(st, indent=2), flush=True)
    if args.status_only:
        return

    for eng in ENGINES:
        n = count_json(eng)
        if n >= TARGET:
            print(f"SKIP {eng}: already {n}/{TARGET}", flush=True)
            continue
        rc = run_engine(eng)
        n2 = count_json(eng)
        if eng == "paddleocr_indic" and n2 < TARGET:
            print(
                f"NOTE {eng}: incomplete ({n2}/{TARGET}). Likely unavailable on this Python. Continuing.",
                flush=True,
            )
            continue
        if n2 < TARGET:
            print(f"WARN {eng}: only {n2}/{TARGET} after run (exit={rc})", flush=True)

    print("FINAL_STATUS", json.dumps(status(), indent=2), flush=True)


if __name__ == "__main__":
    main()
