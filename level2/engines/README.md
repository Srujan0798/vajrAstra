# level2/engines — Engine Socket

One file per engine. Every engine — local (Level 2) or paid-API (Level 3) —
implements the same `BaseEngine` contract and self-registers into `REGISTRY`.
The harness (orchestrator, seal_gen, dashboards) talks only to `REGISTRY`,
so a Level-3 engine drops in with **zero surgery** on existing files.

Project law: `level2/ULTIMATE_HYBRID_CONCERN.md` §5 — **Level 3 (paid APIs)
is LOCKED until Level 2 seals.** No keys, no calls, no exceptions.

## Layout

```
engines/
  __init__.py          BaseEngine, REGISTRY, register()  (the socket)
  local/               10 Level-2 adapters over run_engine.py
  level3_stub.py       SarvamBatchAPI + BhashiniAPI stubs (raise LOCKED)
  test_registry.py     plain-assert verification (no pytest)
```

## BaseEngine contract

| attribute/method | meaning |
|---|---|
| `name` | engine id; Level-2 ids MUST match `run_engine.py` ids exactly |
| `version` | free-text version string (mirrors `seal_gen.py` VERSIONS) |
| `lang_hint` | optional default page language (`te`/`ta`/`kn`/`ml`) |
| `run(png_path) -> str` | OCR one rendered page PNG → NFC text |

## Add a Level-2 (local) engine

1. Ensure an `ocr_<id>(image_path, lang)` function exists in
   `run_engine.py` (owned by main agent — request, don't edit).
2. Create `engines/local/<id>.py` (~15 lines), mirroring an existing adapter:

```python
from pathlib import Path
from .. import BaseEngine, register

class MyEngine(BaseEngine):
    name = "my_engine"          # == run_engine.py engine id
    version = "my_engine 1.2.3"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine   # lazy: no model loads on import
        return run_engine.ocr_my_engine(Path(png_path), self.lang_hint or "te")

register(MyEngine())
```

3. Add the module to the import list in `engines/local/__init__.py`.
4. Extend `EXPECTED_LOCAL` in `test_registry.py`, then run:

```
.venv/bin/python level2/engines/test_registry.py
```

## Add a Level-3 (paid API) engine — AFTER SEAL ONLY

1. Copy `level3_stub.py`'s class into `engines/sarvam.py` (or new file).
2. Replace `run()` with the real client call (image → API → text).
3. Keep the engine id stable; registry/test/verify flows see it instantly.
4. Keys live in env vars ONLY. Never in code, never committed.

Until then: `run()` must keep raising
`NotImplementedError("Level 3 is LOCKED until Level 2 seals — see ULTIMATE_HYBRID_CONCERN.md §5")`.

## Rules

- Lazy imports inside `run()` — importing `engines` never loads OCR models.
- One file per engine; engine id == class name lowercase == file name.
- No comments; short docstrings only.
- `test_registry.py` must stay green before any commit.
