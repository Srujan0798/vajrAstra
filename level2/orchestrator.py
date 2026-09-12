#!/usr/bin/env python3
"""vajrAstra Level-2 one-push orchestrator.

Usage:
  .venv311/bin/python level2/orchestrator.py status        # disk-truth dashboard
  .venv311/bin/python level2/orchestrator.py fill          # restart any stalled/incomplete engine fills (parallel, guarded)
  .venv311/bin/python level2/orchestrator.py migrate       # sync out/<eng> -> models/<eng>/json
  .venv311/bin/python level2/orchestrator.py verify       # run verify_all.py + verify_v2.py
  .venv311/bin/python level2/orchestrator.py dashboard    # regenerate DASHBOARD.md (counts+speed+ETA)
  .venv311/bin/python level2/orchestrator.py guards       # disk + core + spawn-guard status
  .venv311/bin/python level2/orchestrator.py archive-logs  # move finished-engine logs -> logs_archive/
  .venv311/bin/python level2/orchestrator.py cycle          # one full refresh chain, then exit
  .venv311/bin/python level2/orchestrator.py loop [min]    # full chain every N min (daemon)
  .venv311/bin/python level2/orchestrator.py autoloop [min] # full chain + status print, every N min
  .venv311/bin/python level2/orchestrator.py all           # status -> fill -> dashboard -> archive-logs
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
MODELS = L2 / "models"
LOGS = L2 / "logs_active"
ARCHIVE = L2 / "logs_archive"
PY311 = ROOT / ".venv311" / "bin" / "python"
PY314 = ROOT / ".venv" / "bin" / "python"

PY314_ENGINES = {"tesseract_indic", "tesseract_bilingual", "anuvaad_tesseract"}

ENGINES = [
    "tesseract_indic",
    "openbharatocr",
    "easyocr",
    "paddleocr_indic",
    "indicphotoocr",
    "rapidocr",
    "tesseract_bilingual",
    "doctr",
    "surya",
    "anuvaad_tesseract",
]

MANIFEST_IDS = [x["page_id"] for x in json.loads((L2 / "pages_manifest.json").read_text())]


def count(engine: str) -> int:
    return len(list((OUT / engine).rglob("*.json"))) if (OUT / engine).exists() else 0


def model_count(engine: str) -> int:
    d = MODELS / engine / "json"
    return len(list(d.rglob("*.json"))) if d.exists() else 0


def running(engine: str) -> bool:
    out = subprocess.run(["ps", "aux"], capture_output=True, text=True).stdout
    return f"--engine {engine}" in out


def engine_python(engine: str) -> Path:
    return PY314 if engine in PY314_ENGINES else PY311


def cmd_status() -> None:
    print(f"{'engine':<22}{'out':>6}{'models':>8}{'running':>9}  state")
    print("-" * 60)
    total = done = 0
    for e in ENGINES:
        o, m, r = count(e), model_count(e), running(e)
        state = "DONE" if o >= 400 else ("FILLING" if r else "STALLED")
        if o >= 400:
            done += 1
        total += o
        print(f"{e:<22}{o:>6}{m:>8}{('yes' if r else 'no'):>9}  {state}")
    print("-" * 60)
    print(f"engines complete: {done}/{len(ENGINES)}   total packs: {total}/{400*len(ENGINES)}")


FILL_CMD = {
    "paddleocr_indic": ["--engine", "paddleocr_indic", "--skip-existing"],  # per-lang handled below
}


def disk_free_gb() -> float:
    st = os.statvfs(str(ROOT))
    return st.f_bavail * st.f_frsize / 1e9


MAX_PARALLEL_FILLS = 7
DISK_FLOOR_GB = 5.0
_disk_alerted = {"low": False, "cores": False}


def fill_guards_ok(n_pending: int) -> bool:
    free = disk_free_gb()
    if free < DISK_FLOOR_GB:
        if not _disk_alerted["low"]:
            print(f"DISK GUARD: only {free:.1f}GB free (<{DISK_FLOOR_GB}GB) — fills paused")
            _disk_alerted["low"] = True
        return False
    _disk_alerted["low"] = False
    live = sum(1 for e in ENGINES if running(e))
    if live >= MAX_PARALLEL_FILLS:
        if not _disk_alerted["cores"]:
            print(f"CORE GUARD: {live} engines already running (max {MAX_PARALLEL_FILLS}) — skip spawn")
            _disk_alerted["cores"] = True
        return False
    _disk_alerted["cores"] = False
    return True


def cmd_fill() -> None:
    spawn: list[tuple[str, list[str]]] = []
    for e in ENGINES:
        if count(e) >= 400 or running(e):
            continue
        if spawn_guard_active(e):
            continue
        if e == "paddleocr_indic":
            for lang in ["te", "ta", "kn", "ml"]:
                have = len(list((OUT / e / lang).glob("*.json")))
                if have < 100 and not running(f"--lang {lang}"):
                    spawn.append((e, ["--engine", e, "--lang", lang, "--skip-existing"]))
        else:
            spawn.append((e, ["--engine", e, "--skip-existing"]))
    if not spawn:
        print("nothing to fill — all engines complete or already running")
        return
    if not fill_guards_ok(len(spawn)):
        return
    for e, args in spawn:
        LOGS.mkdir(exist_ok=True)
        log = LOGS / f"orch_{e}_{time.strftime('%H%M%S')}.log"
        env = dict(os.environ)
        if e == "surya":
            env["SURYA_GUIDED_LAYOUT"] = "false"  # llama-server grammar 400 fix
        with open(log, "w") as fh:
            subprocess.Popen(
                [str(engine_python(e)), str(L2 / "run_engine.py"), *args],
                stdout=fh,
                stderr=subprocess.STDOUT,
                cwd=str(ROOT),
                env=env,
            )
        print(f"spawned {e}: py={engine_python(e).parent.parent.name} log={log.name}")


def cmd_migrate(replace: bool = False) -> None:
    for e in ENGINES:
        src, dst = OUT / e, MODELS / e / "json"
        if not src.exists():
            continue
        dst.mkdir(parents=True, exist_ok=True)
        have = {p.name for p in dst.glob("*.json")}
        n = 0
        for p in src.rglob("*.json"):
            if p.name not in have or replace:
                (dst / p.name).write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
                n += 1
        print(f"{e}: migrated {n} new, total {len(list(dst.glob('*.json')))}")


def cmd_archive_logs() -> None:
    """Move logs of engines whose run is complete (400 on disk, not running) into logs_archive/."""
    ARCHIVE.mkdir(exist_ok=True)
    moved = 0
    if LOGS.exists():
        for p in sorted(LOGS.glob("*.log")):
            engine = p.stem.split("_")[1] if p.stem.startswith("orch_") else p.stem.rsplit("_", 1)[0].split("_")[0]
            # map log name -> engine id (orch_<engine>_<ts> or <misc>.log)
            matched = None
            for e in ENGINES:
                if e in p.stem:
                    matched = e
                    break
            if matched and count(matched) >= 400 and not running(matched):
                p.rename(ARCHIVE / p.name)
                moved += 1
    print(f"archived {moved} logs to logs_archive/")


REPORTS_DIR = L2 / "reports"
HB_FILE = L2 / "HEARTBEAT.jsonl"


def engine_speed_ms(engine: str) -> int | None:
    if not HB_FILE.exists():
        return None
    durs = []
    try:
        with HB_FILE.open(encoding="utf-8") as f:
            for line in f:
                if engine in line and '"dur_ms"' in line:
                    try:
                        durs.append(json.loads(line)["dur_ms"])
                    except Exception:
                        pass
    except OSError:
        return None
    if not durs:
        return None
    return sorted(durs)[len(durs) // 2]

KNOWN_ERRORS = [
    ("easyocr_lang_combo", "is only compatible with English", "run_engine.py easyocr reader combo invalid for this easyocr version — needs run_engine.py fix"),
    ("tessdata_missing", "Error opening data file", "tessdata model missing — download or fix TESS stack"),
    ("torch_hub_trust", "torch.hub", "trust prompt / checkpoint download issue (IPO)"),
    ("no_module", "No module named", "engine not installed in the venv it was spawned with — check engine_python mapping"),
]

GUARD_FILE = L2 / "logs_active" / "SPAWN_GUARD.json"


def last_spawn_logs(engine: str, n: int = 3) -> list[Path]:
    if not LOGS.exists():
        return []
    logs = sorted(LOGS.glob(f"orch_{engine}_*.log"), key=lambda p: p.stat().st_mtime)[-n:]
    return logs if logs else sorted(LOGS.glob(f"*{engine}*.log"), key=lambda p: p.stat().st_mtime)[-n:]


def classify_failure(engine: str) -> str | None:
    for log in last_spawn_logs(engine):
        try:
            tail = log.read_text(encoding="utf-8", errors="replace")[-4000:]
        except OSError:
            continue
        for tag, sig, fix in KNOWN_ERRORS:
            if sig in tail:
                return f"{tag}: {fix}"
    return None


def spawn_guard_active(engine: str) -> bool:
    if not GUARD_FILE.exists():
        return False
    try:
        g = json.loads(GUARD_FILE.read_text(encoding="utf-8"))
    except Exception:
        return False
    return g.get(engine, 0) >= 3


def note_spawn_failure(engine: str, reason: str) -> None:
    GUARD_FILE.parent.mkdir(exist_ok=True)
    g = {}
    if GUARD_FILE.exists():
        try:
            g = json.loads(GUARD_FILE.read_text(encoding="utf-8"))
        except Exception:
            g = {}
    g[engine] = g.get(engine, 0) + 1
    g[f"{engine}_last_reason"] = reason
    GUARD_FILE.write_text(json.dumps(g, indent=1), encoding="utf-8")
    print(f"GUARD {engine}: {g[engine]} consecutive 400-fail spawns — reason: {reason}")


def cmd_dashboard() -> None:
    """Write DASHBOARD.md — counts + speed + ETA + verification snapshot."""
    lines = ["# Level-2 Dashboard", "",
             f"_auto-generated: {time.strftime('%Y-%m-%d %H:%M')} — regenerate: `orchestrator.py dashboard`_", "",
             "| engine | out | models | running | ms/page | ETA | state |",
             "|---|---|---|---|---|---|---|"]
    total = done = 0
    for e in ENGINES:
        o, m, r = count(e), model_count(e), running(e)
        total += o
        if o >= 400:
            done += 1
        state = "DONE" if o >= 400 else ("FILLING" if r else "STALLED")
        med = engine_speed_ms(e)
        eta = "—"
        if state == "FILLING" and med:
            eta = f"~{(400 - o) * med / 1000 / 60:.0f}m"
        lines.append(f"| {e} | {o} | {m} | {'yes' if r else 'no'} | {med if med else '—'} | {eta} | {state} |")
    lines += ["", f"complete: {done}/{len(ENGINES)}   total: {total}/{400*len(ENGINES)}"]
    lines += ["", "## Reports freshness (age in minutes)", "",
              "| report | age (min) |", "|---|---|"]
    now = time.time()
    fresh = sorted(REPORTS_DIR.glob("*.md")) + [REPORTS_DIR / "VERIFY_V2_SUMMARY.json"]
    stale = []
    for p in fresh:
        if not p.exists():
            continue
        age = int((now - p.stat().st_mtime) / 60)
        if age > 60:
            stale.append(p.name)
        lines.append(f"| {p.name} | {age} |")
    if stale:
        lines += ["", f"STALE (>60m): {', '.join(stale)} — rerun seal_gen / verify_v2"]
    vp = REPORTS_DIR / "VERIFY_V2_SUMMARY.json"
    if vp.exists():
        v = json.loads(vp.read_text(encoding="utf-8"))
        lines += ["", "## Verification v2 (last run)", "",
                  f"- consensus pages: {v['consensus_pages_ge6_engines']}/400",
                  f"- schema violations: {v['schema_violations']}",
                  f"- hallucination events: {v['hallucination_events']}"]
    if GUARD_FILE.exists():
        try:
            gd = json.loads(GUARD_FILE.read_text(encoding="utf-8"))
            blocked = [k for k, v2 in gd.items() if isinstance(v2, int) and v2 >= 3]
            if blocked:
                lines += ["", "## Spawn-guard (engine needs a fix, not respawn-spam)", ""]
                lines += [f"- {k}: {gd.get(k + '_last_reason', '?')}" for k in blocked]
        except Exception:
            pass
    (L2 / "DASHBOARD.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote level2/DASHBOARD.md")


def stall_kill() -> None:
    """Kill engines alive with no new output JSON in 10 minutes."""
    import time as _t
    now = _t.time()
    for e in ENGINES:
        d = OUT / e
        if not d.exists() or count(e) >= 400 or not running(e):
            continue
        files = sorted(d.rglob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            continue
        age = now - files[0].stat().st_mtime
        if age > 600:
            import subprocess as sp
            out = sp.run(["ps", "aux"], capture_output=True, text=True).stdout
            for ln in out.splitlines():
                if f"--engine {e}" in ln and "grep" not in ln:
                    pid = int(ln.split()[1])
                    try:
                        sp.run(["kill", str(pid)], capture_output=True)
                        print(f"STALL-KILLED {e} (pid {pid}, idle {int(age)}s)")
                    except Exception:
                        pass


def check_spawn_outcomes() -> None:
    for e in ENGINES:
        if count(e) >= 400 or running(e):
            GUARD_FILE.parent.mkdir(exist_ok=True)
            if GUARD_FILE.exists():
                try:
                    g = json.loads(GUARD_FILE.read_text(encoding="utf-8"))
                except Exception:
                    g = {}
                if g.get(e, 0) > 0 and count(e) > 0:
                    g[e] = 0
                    g[f"{e}_last_reason"] = "recovered (output appearing)"
                    GUARD_FILE.write_text(json.dumps(g, indent=1), encoding="utf-8")
            continue
        for log in last_spawn_logs(e, 1):
            try:
                body = log.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            n_fail = body.count("FAIL ")
            futile = (n_fail >= 300 or '"fail": 400' in body[-600:]
                      or (n_fail >= 100 and count(e) == 0))
            if futile:
                reason = classify_failure(e) or "spawn produced 0 new packs"
                note_spawn_failure(e, reason)
                break


def cmd_verify_v2() -> None:
    """Run only the light verifier (verify_v2.py, ~36s; stdlib + optional pymupdf)."""
    subprocess.run([str(PY311), str(L2 / "verify_v2.py")], cwd=str(ROOT))


def refresh_chain() -> None:
    """One full disk-truth refresh: stall-kill -> fill -> migrate -> verify_v2 -> seal -> dashboard -> archive."""
    stall_kill()
    cmd_fill()
    time.sleep(60)
    check_spawn_outcomes()
    cmd_migrate()
    cmd_verify_v2()
    subprocess.run([str(PY311), str(L2 / "seal_gen.py")], cwd=str(ROOT))
    cmd_dashboard()
    cmd_archive_logs()


def cmd_cycle() -> None:
    refresh_chain()


def cmd_loop(minutes: int = 30) -> None:
    """Full refresh chain every N minutes (disk-truth only; every report regenerable)."""
    print(f"auto-loop every {minutes}m — Ctrl-C to stop")
    while True:
        refresh_chain()
        try:
            time.sleep(minutes * 60)
        except KeyboardInterrupt:
            print("loop stopped")
            break


def cmd_autoloop(minutes: int = 30) -> None:
    """Same full chain as loop, plus a status print each tick."""
    print(f"full auto-loop every {minutes}m — Ctrl-C to stop")
    while True:
        cmd_status()
        refresh_chain()
        try:
            time.sleep(minutes * 60)
        except KeyboardInterrupt:
            print("loop stopped")
            break


def cmd_guards() -> None:
    print(f"free disk: {disk_free_gb():.1f}GB (floor {DISK_FLOOR_GB}GB)")
    live = [e for e in ENGINES if running(e)]
    print(f"engines running: {len(live)}/{MAX_PARALLEL_FILLS} {live}")
    if GUARD_FILE.exists():
        try:
            print("spawn guard:", json.dumps(json.loads(GUARD_FILE.read_text(encoding="utf-8")), indent=1))
        except Exception:
            print("spawn guard file unreadable")


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "status"
    if mode == "status":
        cmd_status()
    elif mode == "fill":
        cmd_fill()
    elif mode == "migrate":
        cmd_migrate(replace="--replace" in sys.argv)
    elif mode == "archive-logs":
        cmd_archive_logs()
    elif mode == "dashboard":
        cmd_dashboard()
    elif mode == "cycle":
        cmd_cycle()
    elif mode == "loop":
        mins = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        cmd_loop(mins)
    elif mode == "autoloop":
        mins = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        cmd_autoloop(mins)
    elif mode == "verify":
        cmd_verify_v2()
    elif mode == "all":
        cmd_cycle()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
