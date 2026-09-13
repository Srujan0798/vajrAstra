#!/usr/bin/env python3
"""ONE WRITER ONE TRUTH (law §18 Track B) — regenerates every level2 report in one pass.

Order: verify_v2 -> deep_verify (per engine) -> report_gen -> seal_gen -> stamp.
DASHBOARD.md belongs to orchestrator.py cmd_dashboard; this module stamps only the
artifacts it created under level2/reports/ (incl. MATRIX.csv). All counts from disk.
Usage: .venv/bin/python level2/report.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

VERSION = "v1"
ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
REPORTS = L2 / "reports"
PY = ROOT / ".venv" / "bin" / "python"

ENGINES = [
    "tesseract_indic", "openbharatocr", "easyocr", "paddleocr_indic",
    "indicphotoocr", "rapidocr", "tesseract_bilingual", "doctr",
    "surya", "anuvaad_tesseract",
]

STAMPABLE = {".md", ".json", ".csv"}
MD_MARK = "<!-- generated_at:"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def stamp_line(ts: str) -> str:
    return f"{MD_MARK} {ts} | generator: report.py {VERSION} -->"


def run_step(name: str, cmd: list[str]) -> tuple[float, bool]:
    t0 = time.monotonic()
    r = subprocess.run(cmd, cwd=str(ROOT))
    dt = time.monotonic() - t0
    ok = r.returncode == 0
    print(f"[report.py] {name}: {'ok' if ok else f'FAIL rc={r.returncode}'} {dt:.1f}s",
          flush=True)
    return dt, ok


def stampable_files() -> dict[Path, float]:
    """{path: mtime} for every stampable artifact currently in reports/."""
    if not REPORTS.exists():
        return {}
    return {p: p.stat().st_mtime for p in sorted(REPORTS.iterdir())
            if p.is_file() and p.suffix.lower() in STAMPABLE}


def rewrite(p: Path, text: str) -> None:
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(p)


def stamp_md(p: Path, ts: str) -> bool:
    try:
        txt = p.read_text(encoding="utf-8")
    except Exception:
        return False
    body = "\n".join(l for l in txt.splitlines() if not l.lstrip().startswith(MD_MARK))
    rewrite(p, body.rstrip("\n") + "\n\n" + stamp_line(ts) + "\n")
    return True


def stamp_json(p: Path, ts: str) -> bool:
    try:
        obj = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return False
    if not isinstance(obj, dict):
        return False
    obj["generated_at"] = ts
    obj["generator"] = f"report.py {VERSION}"
    rewrite(p, json.dumps(obj, ensure_ascii=False, indent=1))
    return True


def stamp_csv(p: Path, ts: str) -> bool:
    try:
        txt = p.read_text(encoding="utf-8")
    except Exception:
        return False
    lines = [l for l in txt.splitlines() if not l.startswith("# generated_at:")]
    rewrite(p, "\n".join(lines).rstrip("\n") + "\n"
            + f"# generated_at: {ts} | generator: report.py {VERSION}\n")
    return True


STAMPERS = {".md": stamp_md, ".json": stamp_json, ".csv": stamp_csv}


def main() -> int:
    t0 = time.monotonic()
    before = stampable_files()
    failures: list[str] = []
    timings: list[tuple[str, float]] = []

    steps: list[tuple[str, list[str]]] = [
        ("verify_v2", [str(PY), str(L2 / "verify_v2.py")]),
    ]
    steps += [(f"deep_verify:{e}", [str(PY), str(L2 / "deep_verify.py"), e])
              for e in ENGINES]
    steps += [
        ("gap_report", [str(PY), str(L2 / "research" / "gap_report_gen.py")]),
        ("report_gen", [str(PY), str(L2 / "report_gen.py")]),
        ("seal_gen", [str(PY), str(L2 / "seal_gen.py")]),
    ]
    for name, cmd in steps:
        dt, ok = run_step(name, cmd)
        timings.append((name, dt))
        if not ok:
            failures.append(name)

    ts = utc_now()
    stamped = []
    for p, m in stampable_files().items():
        old = before.get(p)
        if old is not None and m <= old:
            continue
        if STAMPERS[p.suffix.lower()](p, ts):
            stamped.append(p.name)

    total = time.monotonic() - t0
    for name, dt in timings:
        print(f"[report.py]   {name:<30} {dt:6.1f}s", flush=True)
    print(f"[report.py] stamped {len(stamped)} artifacts: {', '.join(stamped)}",
          flush=True)
    print(f"[report.py] total {total:.1f}s, failures: {failures or 'none'}",
          flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
