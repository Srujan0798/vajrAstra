#!/usr/bin/env python3
"""proto-89 §A Gate 1 — Bodhan (MLX 4-bit / bf16) vs surya on probe22 + Sarvam bench.

PREREQUISITE: Bodhan weights must be on disk first. All four approved assets
(bodhan-ai/indic-ocr, hari31416/indic-ocr-mlx-{4bit,bf16}, sarvamai/indic-ocr-bench,
Omarrran/600k_KS_OCR_Word_Segmented_Dataset) were AUTH-BLOCKED on 2026-09-30:
gated HF repos + no HF token on this Mac. See docs/campaign/BODHAN_BASELINE.md.
Re-run this script the moment a token is provided and weights land in
level2/models_bodhan/ (pinned revisions below).

Laws: eval only (no training); scores with level2/benchmark/pipeline/metrics.py UNCHANGED
(Sarvam parity; moved here from level2/probe22/metrics.py by the proto-70 restructure
2026-09-30 — verify sha256 before scoring); GT-tier stratified reporting per proto-62;
attribution notice on outputs: "Built with IndicBlockOCR from Bodhan AI / AI4Bharat."

Usage:
  python run_bodhan.py --port 4bit --mode probe                # all 1,283 probe items
  python run_bodhan.py --port 4bit --mode probe --sample 100   # stratified sample
  python run_bodhan.py --port 4bit --mode probe --pair-only    # 300 human gold pairs
  python run_bodhan.py --port 4bit --mode bench                # bench small_representative
  python run_bodhan.py --port 4bit --mode parity               # 4-bit vs bf16 on the sample
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

REPO = Path("/Users/srujansai/Desktop/South")
PROBE22 = REPO / "level2/benchmark"
MODELS_DIR = REPO / "level2/models_bodhan"
OUT_DIR = REPO / "level2/unified/out"
METRICS_PY = PROBE22 / "pipeline/metrics.py"
MANIFEST_JSON = PROBE22 / "manifest.json"

REVISIONS = {
    "hari31416/indic-ocr-mlx-4bit": "6882ee7a21bfc3d2cfb384ce669f2bfdcea3a36e",
    "hari31416/indic-ocr-mlx-bf16": "bb091d3a6366a0defe79f0f252c16a790fc8d74b",
    "bodhan-ai/indic-ocr": "cd50d301d0e17e8ecb32fc49c8ccbd7914dcfc25",
    "sarvamai/indic-ocr-bench": "84ce7ce447456a92bcbf25f3c0a55d6a5a44a24b",
    "Omarrran/600k_KS_OCR_Word_Segmented_Dataset": "3ee5d7950d1f0efa8fc51912fd79fdb3bd77b67f",
}
PORT_DIRS = {"4bit": MODELS_DIR / "indic-ocr-mlx-4bit", "bf16": MODELS_DIR / "indic-ocr-mlx-bf16"}

ATTRIBUTION = "Built with IndicBlockOCR from Bodhan AI / AI4Bharat."
TRANSCRIBE_PROMPT = "Transcribe the text in this image."


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def require_weights(port: str) -> Path:
    d = PORT_DIRS[port]
    if not (d / "model.safetensors").exists() and not list(d.glob("model*.safetensors")):
        sys.exit(
            f"Weights missing: {d}. Download first (gated; see BODHAN_BASELINE.md) "
            f"with revision {REVISIONS['hari31416/indic-ocr-mlx-' + port]}."
        )
    return d


def stratified_sample(items: list[dict], n: int) -> list[dict]:
    tiers = defaultdict(list)
    for it in items:
        tiers[it["gt_source"]].append(it)
    total = len(items)
    out: list[dict] = []
    for tier, pool in tiers.items():
        k = round(n * len(pool) / total)
        out.extend(pool[:k])
    return out[:n]


def select_items(args) -> list[dict]:
    manifest = json.load(open(MANIFEST_JSON))
    items = manifest["items"]
    if args.pair_only:
        return [it for it in items if it["gt_source"] in ("official_pair_txt", "official_pair")]
    if args.sample:
        return stratified_sample(items, args.sample)
    return items


def page_image_path(it: dict) -> Path:
    return PROBE22 / "pages" / it["language"] / f"{it['image_id']}.jpg"


def run_pages_mlx(port_dir: Path, items: list[dict]) -> tuple[list[dict], dict]:
    sys.path.insert(0, str(port_dir))
    from pipeline import IndicOCRPipeline  # noqa: PLC0415

    t_load = time.perf_counter()
    ocr = IndicOCRPipeline()
    load_s = time.perf_counter() - t_load

    preds, timings = [], []
    for it in items:
        img = page_image_path(it)
        if not img.exists():
            preds.append({"image_name": it["image_id"], "gt": it["gt"], "pred": "[ERROR: image missing]"})
            continue
        t0 = time.perf_counter()
        try:
            result = ocr.process(str(img))
            text = result.markdown or ""
        except Exception as e:  # noqa: BLE001
            text = f"[ERROR: {type(e).__name__}: {str(e)[:120]}]"
        dt = time.perf_counter() - t0
        timings.append({"image_id": it["image_id"], "kind": "page", "seconds": dt})
        preds.append({"image_name": it["image_id"], "gt": it["gt"], "pred": text})
    meta = {"load_seconds": load_s, "n": len(items)}
    return preds, {"timings": timings, **meta}


def run_bench_crops_mlx(port_dir: Path, parquet_path: Path, limit: int | None) -> tuple[list[dict], dict]:
    import pandas as pd  # noqa: PLC0415
    from mlx_vlm import generate, load  # noqa: PLC0415
    from mlx_vlm.prompt_utils import apply_chat_template  # noqa: PLC0415
    from PIL import Image  # noqa: PLC0415

    df = pd.read_parquet(parquet_path)
    if limit:
        df = df.head(limit)
    model, processor = load(str(port_dir))

    preds, timings = [], []
    for _, row in df.iterrows():
        img_bytes = row["image"] if isinstance(row["image"], (bytes, bytearray)) else row["image"]["bytes"]
        gt = row.get("gt") or row.get("ground_truth") or ""
        import io  # noqa: PLC0415

        image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": TRANSCRIBE_PROMPT}]}]
        prompt = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
        t0 = time.perf_counter()
        try:
            _gen = generate(model, processor, prompt, image, max_tokens=512)
            text = _gen.text if hasattr(_gen, "text") else str(_gen)
        except Exception as e:  # noqa: BLE001
            text = f"[ERROR: {type(e).__name__}: {str(e)[:120]}]"
        dt = time.perf_counter() - t0
        timings.append({"kind": "crop", "seconds": dt})
        preds.append({"image_name": str(row.get("id", row.name)), "gt": gt, "pred": text})
    return preds, {"timings": timings, "n": len(preds)}


def score_with_unchanged_metrics(preds: list[dict], tag: str) -> dict:
    raw_in = OUT_DIR / f"preds_bodhan_{tag}.json"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(raw_in, "w", encoding="utf-8") as f:
        json.dump(preds, f, ensure_ascii=False, indent=2)
    for mode, extra in (("replace_n", ["--replace-n"]), ("normalized", ["--normalize"])):
        out_json = OUT_DIR / f"preds_bodhan_{tag}.metrics.{mode}.json"
        cmd = [sys.executable, str(METRICS_PY), "--input", str(raw_in), "--output", str(out_json),
               "--overwrite", "--model-name", f"preds_bodhan_{tag}", *extra]
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    manifest = {it["image_id"]: it["gt_source"] for it in json.load(open(MANIFEST_JSON))["items"]}
    tier_scores: dict[str, list[float]] = defaultdict(list)
    empty = 0
    with open(OUT_DIR / f"preds_bodhan_{tag}.metrics.normalized.json", encoding="utf-8") as f:
        results = json.load(f)["results"]
    for r in results:
        name = r.get("image_name") or r.get("sample_id")
        cer = (r.get("metrics") or {}).get("cer")
        tier = manifest.get(name, "bench")
        if cer is not None:
            tier_scores[tier].append(cer)
        pred = (r.get("pred") or "")
        if pred.startswith("[ERROR:") or pred.strip() == "":
            empty += 1
    tier_table = {t: {"n": len(v), "mean_cer": sum(v) / len(v)} for t, v in sorted(tier_scores.items())}
    return {"metrics_py_sha256": sha256_file(METRICS_PY), "per_tier": tier_table,
            "empty_or_error": empty, "n_scored": len(results)}


def summarize_speed(timings: list[dict]) -> dict:
    pages = [t["seconds"] for t in timings if t["kind"] == "page"]
    crops = [t["seconds"] for t in timings if t["kind"] == "crop"]
    out = {}
    if pages:
        out["s_per_page"] = {"n": len(pages), "mean": sum(pages) / len(pages),
                             "median": sorted(pages)[len(pages) // 2]}
    if crops:
        out["s_per_crop"] = {"n": len(crops), "mean": sum(crops) / len(crops),
                             "median": sorted(crops)[len(crops) // 2]}
    return out


def surya_pair_comparison() -> dict:
    surya = {p["image_name"]: p["pred"] for p in json.load(open(PROBE22 / "scores/preds_surya.json"))}
    return {"n_surya_preds": len(surya)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", choices=["4bit", "bf16"], default="4bit")
    ap.add_argument("--mode", choices=["probe", "bench", "parity"], default="probe")
    ap.add_argument("--sample", type=int, default=None)
    ap.add_argument("--pair-only", action="store_true")
    ap.add_argument("--bench-limit", type=int, default=None)
    args = ap.parse_args()

    port_dir = require_weights(args.port)
    if args.mode in ("probe", "parity"):
        items = select_items(args)
        preds, run_meta = run_pages_mlx(port_dir, items)
        tag = f"{args.port}_{'pair' if args.pair_only else 'probe'}"
        scoring = score_with_unchanged_metrics(preds, tag)
        report = {"mode": args.mode, "port": args.port, "revision": REVISIONS[f"hari31416/indic-ocr-mlx-{args.port}"],
                  "attribution": ATTRIBUTION, "run": run_meta, "scoring": scoring,
                  "speed": summarize_speed(run_meta["timings"]), "surya": surya_pair_comparison()}
    elif args.mode == "bench":
        parquet = MODELS_DIR / "indic-ocr-bench/small_representative/small_representative-00000-of-00001.parquet"
        if not parquet.exists():
            sys.exit(f"Bench parquet missing: {parquet} (U24 download; see BODHAN_BASELINE.md)")
        preds, run_meta = run_bench_crops_mlx(port_dir, parquet, args.bench_limit)
        scoring = score_with_unchanged_metrics(preds, f"{args.port}_bench")
        report = {"mode": "bench", "port": args.port, "revision": REVISIONS[f"hari31416/indic-ocr-mlx-{args.port}"],
                  "attribution": ATTRIBUTION, "run": run_meta, "scoring": scoring,
                  "speed": summarize_speed(run_meta["timings"])}
    else:
        sys.exit("parity: run --mode probe --port 4bit and --port bf16 on the same sample, then diff the per_tier tables.")

    out = OUT_DIR / f"bodhan_{args.port}_{args.mode}_report.json"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
