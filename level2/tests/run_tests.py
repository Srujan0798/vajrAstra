#!/usr/bin/env python3
"""Code-only CI suite (stdlib only, plain asserts — repo convention, no pytest).

    VAJRA_CODE_ONLY=1 python3 level2/tests/run_tests.py

Runs on a bare clone (no renders/reports/Datasets): everything here uses only
tracked files — engines/, out/ (4000 packs), pages_manifest.json, training_assets/.
  T1 engine registry (engines/test_registry.py)
  T2 Sarvam adapter contract (no network)
  T3 every out/ pack: parses, schema keys, NFC text, 10 engines x 400 pages
  T4 the checker in T3 catches deliberate corruption (self-test: proves CI goes red)
  T5 sealed CER basis reproduces (n=126, surya 0.4299, anuvaad 0.4751, DPO labels)
  T6 L10 guard: protected pipeline files unchanged vs base (CI only, BASE_REF set)
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import tempfile
import time
import unicodedata
import zipfile
from pathlib import Path

L2 = Path(__file__).resolve().parents[1]
ROOT = L2.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(L2))
sys.path.insert(0, str(L2 / "research"))

PROTECTED = ["level2/verify_v2.py", "level2/report.py", "level2/run_engine.py",
             "level2/seal_gen.py", "level2/report_gen.py"]
REQUIRED_KEYS = {"page_id", "source", "lang", "script", "quality_tier", "image", "regions", "ocr_engine"}
REGION_KEYS = {"region_id", "cls", "bbox_xyxy", "text"}


def t1_registry():
    os.environ.setdefault("VAJRA_CODE_ONLY", "1")
    from level2.engines import test_registry
    test_registry.main()


def t2_sarvam_adapter():
    os.environ.pop("SARVAM_API_KEY", None)
    from level2.engines import REGISTRY
    from level2.engines.sarvam_api import DRY_RUN_TEXT, SarvamBatchAPI, collect_text
    eng = REGISTRY["sarvam_api"]
    assert eng.dry_run and eng.run(Path("te_001.png")) == DRY_RUN_TEXT
    fresh = SarvamBatchAPI()
    assert fresh.language_for(Path("te_001.png")) == "te-IN"
    assert fresh.language_for(Path("ml_019.png")) == "ml-IN"
    try:
        fresh.language_for(Path("zz_999.png"))
        raise AssertionError("unknown page must raise, not default to te-IN")
    except ValueError:
        pass
    fresh.lang_hint = "kn"
    assert fresh.language_for(Path("te_001.png")) == "kn-IN"
    nested = {"pages": [{"blocks": [{"text": "அ"}, {"text": "ஆ", "bbox": [1]}]}, {"text": "இ"}]}
    assert collect_text(nested) == ["அ", "ஆ", "இ"]

    def zipped(obj) -> bytes:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as z:
            z.writestr("page.json", json.dumps(obj))
        return buf.getvalue()

    fresh.last_meta = {"error": None}
    assert fresh._extract_zip(zipped(nested)) == "அ\nஆ\nஇ"
    fresh.last_meta = {"error": None}
    assert fresh._extract_zip(zipped({"status": "ok", "blocks": [{"bbox": [0, 0]}]})) == ""
    assert fresh.last_meta["error"] == "unparsed_output", "unparsed payload must be flagged, never str()-dumped"
    print("[T2] sarvam adapter: manifest language, no silent default, text-only parse — OK")


def check_packs(out_dir: Path, manifest_ids: set[str], engines: list[str]) -> list[str]:
    errs = []
    for e in engines:
        seen = set()
        for p in (out_dir / e).glob("*/*.json"):
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
            except Exception as exc:
                errs.append(f"{e}/{p.name}: bad json ({exc.__class__.__name__})")
                continue
            miss = REQUIRED_KEYS - set(obj)
            if miss:
                errs.append(f"{e}/{p.name}: missing keys {sorted(miss)}")
                continue
            if obj["page_id"] != p.stem:
                errs.append(f"{e}/{p.name}: page_id {obj['page_id']!r} != filename")
            for r in obj.get("regions", []):
                if REGION_KEYS - set(r):
                    errs.append(f"{e}/{p.name}: region missing {sorted(REGION_KEYS - set(r))}")
                t = r.get("text", "")
                if unicodedata.normalize("NFC", t) != t:
                    errs.append(f"{e}/{p.name}: text not NFC")
            seen.add(p.stem)
        if seen != manifest_ids:
            errs.append(f"{e}: {len(seen)} packs, missing {sorted(manifest_ids - seen)[:5]} extra {sorted(seen - manifest_ids)[:5]}")
    return errs


def t3_packs():
    from level2.verify_v2 import ENGINES
    ids = {m["page_id"] for m in json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))}
    assert len(ids) == 400
    errs = check_packs(L2 / "out", ids, ENGINES)
    assert not errs, f"{len(errs)} pack errors, first: {errs[:5]}"
    print(f"[T3] out/: {len(ENGINES)} engines x {len(ids)} pages = {len(ENGINES) * len(ids)} packs, schema + NFC clean — OK")


def t4_checker_catches_corruption():
    from level2.verify_v2 import ENGINES
    ids = {"te_001", "ta_001"}
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        for e in ENGINES[:1]:
            for pid in ids:
                src = L2 / "out" / e / pid[:2] / f"{pid}.json"
                dst = td / e / pid[:2] / f"{pid}.json"
                dst.parent.mkdir(parents=True)
                dst.write_bytes(src.read_bytes())
        e = ENGINES[0]
        assert not check_packs(td, ids, [e]), "clean copy must pass"
        bad = td / e / "te" / "te_001.json"
        obj = json.loads(bad.read_text(encoding="utf-8"))
        obj["regions"][0]["text"] = "\u0B95\u0BC6\u0BBE"  # decomposed கொ: not NFC
        bad.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
        assert any("not NFC" in x for x in check_packs(td, ids, [e])), "NFC corruption not caught"
        del obj["ocr_engine"]
        bad.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
        assert any("missing keys" in x for x in check_packs(td, ids, [e])), "schema corruption not caught"
        bad.write_text("{not json", encoding="utf-8")
        assert any("bad json" in x for x in check_packs(td, ids, [e])), "broken JSON not caught"
        bad.unlink()
        assert any("missing" in x for x in check_packs(td, ids, [e])), "missing pack not caught"
    print("[T4] checker goes red on NFC / schema / broken-JSON / missing-pack corruption — OK")


def t5_sealed_basis():
    import r1_common as C
    b = C.basis()
    assert (len(b["dense"]), len(b["mojibake"]), len(b["clean"])) == (176, 50, 126), {k: len(v) for k, v in b.items()}
    M = C.cer_matrix()
    from statistics import median
    med = {e: round(median(M[p][e] for p in M), 4) for e in ("surya", "anuvaad_tesseract")}
    assert med == {"surya": 0.4299, "anuvaad_tesseract": 0.4751}, med
    bad = 0
    for line in C.DPO.open(encoding="utf-8"):
        r = json.loads(line)
        for side in ("chosen", "rejected"):
            bad += abs(M[r["page_id"]][r["engine_" + side]] - float(r["cer_" + side])) > 1e-4
    assert bad == 0, f"{bad} DPO CER labels no longer reproduce"
    print(f"[T5] sealed basis reproduces: n=126, surya {med['surya']}, anuvaad {med['anuvaad_tesseract']}, 252/252 DPO labels — OK")


def t6_l10_guard():
    base = os.environ.get("BASE_REF")
    if not base:
        print("[T6] SKIP L10 guard (no BASE_REF; runs in CI on pull requests)")
        return
    if "L10-OVERRIDE" in os.environ.get("PR_TITLE", ""):
        print("[T6] L10 guard overridden by operator (PR title contains L10-OVERRIDE)")
        return
    changed = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD", "--", *PROTECTED],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    assert not changed, f"L10: protected pipeline files changed: {changed} (operator may override with L10-OVERRIDE in PR title)"
    print("[T6] L10 guard: protected pipeline files unchanged — OK")


def main() -> None:
    t0 = time.time()
    for t in (t1_registry, t2_sarvam_adapter, t3_packs, t4_checker_catches_corruption, t5_sealed_basis, t6_l10_guard):
        t()
    print(f"ALL PASS in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
