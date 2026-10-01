"""run_bodhan_pytorch.py — Official Bodhan PyTorch path (proto-104 D1, R-13).

The PORTABLE product path: bodhan-ai/indic-ocr official weights via
IndicOCR.from_pretrained. Every result here must reproduce on this path
(R-13); the MLX port is Mac-only acceleration.

R-15 night-run rules: device tag, resumable (--skip-existing), RUN_STATE in
level2/benchmark/logs/RUN_STATE/, heartbeat every 5 min.

Usage:
  .venv311/bin/python level2/benchmark/run_bodhan_pytorch.py --sample 100
  .venv311/bin/python level2/benchmark/run_bodhan_pytorch.py --pair-only
  .venv311/bin/python level2/benchmark/run_bodhan_pytorch.py --mode probe  # full 1,227

Outputs: level2/benchmark/packs/bodhan_official/<lang>/<image_id>.json
  (pack schema: image_id, language, engine="bodhan_official", text, gt, CER, ms, device, set)
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/Users/srujansai/Desktop/South")
MODELS = REPO / "level2/models_bodhan/indic-ocr"
MANIFEST = REPO / "level2/benchmark/manifest.json"
PACKS = REPO / "level2/benchmark/packs/bodhan_official"
RUN_STATE_DIR = REPO / "level2/benchmark/logs/RUN_STATE"
DEVICE = "mac-m4-mps"  # torch.backends.mps.is_available() True; fallback mac-m4-cpu

sys.path.insert(0, str(REPO / "level2/benchmark/pipeline"))
try:
    from metrics import calculate_cer
    HAS_METRICS = True
except Exception:
    HAS_METRICS = False


def load_manifest() -> list[dict]:
    m = json.loads(MANIFEST.read_text())
    items = m["items"] if isinstance(m, dict) and "items" in m else m
    return items


def stratified_sample(items: list[dict], n: int, seed: int = 20260926) -> list[dict]:
    import random
    random.seed(seed)
    by_lang: dict[str, list] = {}
    for it in items:
        by_lang.setdefault(it.get("language", "?"), []).append(it)
    out = []
    for lang in sorted(by_lang):
        pool = by_lang[lang]
        k = max(1, round(n * len(pool) / len(items)))
        out.extend(random.sample(pool, min(k, len(pool))))
    return out


def pair_only(items: list[dict]) -> list[dict]:
    return [it for it in items if it.get("gt_source") == "official_pair_txt" or it.get("tier") == "gold_pair"]


def run_state_init(job: str, total: int) -> Path:
    RUN_STATE_DIR.mkdir(parents=True, exist_ok=True)
    p = RUN_STATE_DIR / f"{job}.json"
    p.write_text(json.dumps({
        "job": job, "done": 0, "total": total, "last_item": None,
        "machine": "mac-m4", "device": DEVICE,
        "start": datetime.now(timezone.utc).isoformat(), "last_update": None,
    }))
    return p


def run_state_update(p: Path, done: int, last_item: str):
    try:
        s = json.loads(p.read_text())
        s["done"] = done
        s["last_item"] = last_item
        s["last_update"] = datetime.now(timezone.utc).isoformat()
        p.write_text(json.dumps(s))
    except Exception:
        pass


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=None)
    ap.add_argument("--pair-only", action="store_true")
    ap.add_argument("--ids-file", type=str, default=None,
                    help="JSON list of image_ids to run (for MLX parity; overrides --sample)")
    ap.add_argument("--mode", default="probe", choices=["probe"])
    ap.add_argument("--skip-existing", action="store_true", default=True)
    args = ap.parse_args()

    items = load_manifest()
    if args.ids_file:
        want = set(json.loads(Path(args.ids_file).read_text()))
        items = [it for it in items
                 if it.get("image_id") in want or it.get("uid") in want]
        job = "bodhan_official_parity100"
    elif args.pair_only:
        items = pair_only(items)
        job = "bodhan_official_paironly"
    elif args.sample:
        items = stratified_sample(items, args.sample)
        job = f"bodhan_official_sample{args.sample}"
    else:
        job = "bodhan_official_probe"

    print(f"[{job}] {len(items)} items, device={DEVICE}", flush=True)
    state = run_state_init(job, len(items))

    sys.path.insert(0, str(MODELS))
    from indic_ocr import IndicOCR
    parser = IndicOCR.from_pretrained(str(MODELS))
    print(f"[{job}] model loaded", flush=True)

    done = 0
    last_beat = time.monotonic()
    for it in items:
        lang = it.get("language", "?")
        image_id = it.get("image_id", it.get("uid", "?"))
        out_path = PACKS / lang / f"{image_id}.json"
        if args.skip_existing and out_path.exists():
            done += 1
            continue
        img_path = REPO / "level2/benchmark/pages" / lang / f"{image_id}.jpg"
        if not img_path.exists():
            # fallback: images dir per manifest image_path
            alt = REPO / str(it.get("image_path", ""))
            img_path = alt if alt.exists() else img_path
        t0 = time.monotonic()
        try:
            result = parser(str(img_path))
            text = result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)
            err = None
        except Exception as e:
            text, err = "", f"{type(e).__name__}: {e}"
        ms = int((time.monotonic() - t0) * 1000)
        gt = it.get("gt", "")
        try:
            cer = calculate_cer(gt, text) if HAS_METRICS and gt else None
        except Exception:
            cer = None
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps({
            "image_id": image_id, "language": lang,
            "engine": "bodhan_official", "engine_version": "bodhan-ai/indic-ocr@cd50d301",
            "text": text, "gt": gt, "CER": cer, "ms": ms, "device": DEVICE,
            "error": err, "set": it.get("gt_source", it.get("tier", "unknown")),
            "attribution": "Built with IndicBlockOCR from Bodhan AI / AI4Bharat.",
        }, ensure_ascii=False))
        done += 1
        run_state_update(state, done, image_id)
        if time.monotonic() - last_beat > 300:
            print(f"[{job}] heartbeat: {done}/{len(items)} last={image_id}", flush=True)
            last_beat = time.monotonic()

    # HANDOFF line
    hand = RUN_STATE_DIR / "HANDOFF.md"
    print(f"[{job}] DONE {done}/{len(items)}", flush=True)


if __name__ == "__main__":
    main()
