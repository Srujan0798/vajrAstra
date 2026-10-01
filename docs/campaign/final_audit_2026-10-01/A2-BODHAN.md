# A2-BODHAN — Bodhan integration audit

Snapshot limits: `level2/models_bodhan/` (weights, vendor code, READMEs/cards), `level2/unified/out/`, `level2/benchmark/{pages,packs,manifest.json}` and `product/` code are NOT in /home/user/boss. `find` shows `product/` holds only `docs/B21_SYNTHETIC_LINES_SPEC.md`. So the vendor CUDA assert cannot be quoted by file:line from here; I give the grep that finds it.

## STATE (verified = code present; numbers verified only as text copies)
- Code path that produced every Bodhan number is MLX, not PyTorch. `level2/unified/run_bodhan.py:99-123` `run_pages_mlx` does `sys.path.insert(0, port_dir)`, `from pipeline import IndicOCRPipeline` (the hari31416 MLX port's own pipeline), and scores `result.markdown` (l.116). Crop path `run_bench_crops_mlx` (l.126-155) uses `mlx_vlm.load/generate`, prompt "Transcribe the text in this image.", max_tokens=512, recogniser only.
- Scoring path (l.158-184): writes `preds_bodhan_<tag>.json`, runs `level2/benchmark/pipeline/metrics.py` twice (`--replace-n`, `--normalize`), but the per-tier table reads ONLY the `--normalize` file (l.171). CER = whole-string Levenshtein over NFKC/NFC chars, capped at 1.0 (`metrics.py:554-559`, `_bound_rate`), so it is order-sensitive.
- Official PyTorch script exists but never completed: `level2/benchmark/run_bodhan_pytorch.py`. Load = `from indic_ocr import IndicOCR; IndicOCR.from_pretrained(str(MODELS))` (l.117-119); call = `parser(str(img_path))` (l.138). `DEVICE = "mac-m4-mps"` is a hard-coded label only (l.33); nothing selects a device. Output pack `packs/bodhan_official/<lang>/<id>.json` (l.150-156). 0 packs claimed anywhere.
- Weights on disk on the Mac (claimed in text only): 4-bit 30 files, bf16 30, official `bodhan-ai/indic-ocr@cd50d301` 39 files, bench 29 files, 5.35 GB total (`DISPATCH_LOG.md:590-599`). `BODHAN_BASELINE.md:3-11` lists 8-bit and bench as "on disk" with 0 safetensors/0 MB, which is a placeholder, not a model.
- Licence constraints recorded: attribution string in outputs (`run_bodhan.py:51`, `run_bodhan_pytorch.py:155`); hosted endpoint needs written approval, U28 pending (`DISPATCH_LOG.md:736`, W4.md:31,48).

## CLAIMED-BUT-UNPROVEN
- "Gate 1 CONDITIONAL PASS" (`BODHAN_BASELINE.md:22`; `DISPATCH_LOG.md:708`). The blind verify (`W4_reports/blind_verify_gate1.md`) only greps that the same strings appear in two text files (Checks 1-3) and `ls` of dirs. It never reran a script or opened a pred file. VERIFIED = copy fidelity, not measurement.
- The pass threshold in proto-89 was "reproduces ~84.9 +-2 on the bench AND beats surya on the 300 pairs" (`proto-89:29`). 0.0540 CER / 0.1356 WER was converted to "~86.4" by proto-108 (:104,:436); that conversion is not in any script (WER 0.1356 gives 86.4 only if word-accuracy = 1-WER, never checked against the official scorer, which the log says is unknown, `DISPATCH_LOG.md:429`). Also the run used `metrics.py`, not the official Sarvam scorer.
- "beats surya 0.5660": `surya_pair_comparison()` (`run_bodhan.py:200-202`) only returns `n_surya_preds`; no code computes the 0.5660. Source unrecorded. The 0.1514 surya figure in `DISPATCH_LOG.md:432` and 0.3956 (l.496) are different populations.
- "4-bit ~ bf16 (B-01 PASS)": only on the 99 pages and 300 pairs, whole-script mix; no per-script table, no Perso-Arabic split (the B-01 requirement, `B01_4BIT_ANALYSIS.md:5-9`). `--mode parity` is just `sys.exit(...)` (l.232-233).
- The 99-item sample: `stratified_sample` (l.73-82) takes `pool[:k]` per GT tier in manifest order (not random, not per language), so the 99 are whatever sits first in the manifest; it rounds to 99 not 100.
- Reproducibility defects: sample, pair and full probe runs all write the same file name when not `--pair-only` (`tag`, l.218) so a full run overwrites the sample's preds; `REPO` is hard-coded `/Users/srujansai/Desktop/South` (l.35, and pytorch l.28); l.1-9 docstring still says weights are AUTH-BLOCKED and 1,283 items while the PyTorch script says 1,227. `run_bodhan.py` was rewritten by concurrent writers and its pre-repair bytes are unrecoverable (`DISPATCH_LOG.md:265,297`).

## O-1: page CER 0.69 vs crop 0.054 (unexplained; nobody ran a diagnostic)
Facts that constrain the cause. (1) 4-bit vs bf16 differ by 0.0015 (`BODHAN_BASELINE.md:17`), so quantisation is not it. (2) Even the 300 human-gold PAIRS (cleanest GT) are 0.40, still 7x the crop number, so bad silver PDF-text-layer GT is only part. (3) The two numbers are different data: crops are Sarvam bench block images (already segmented, `run_bodhan.py:126`), pages are our probe pages whose GT is a flat page string (`manifest items[].gt`).
Likely causes from the code, in suspected order:
- Reading order and block concatenation. The scorer compares one flat string. Bodhan returns layout-ordered Markdown (blocks, reading order from IndicDocLayout); GT is a PDF text layer or pair txt in its own order (columns, headers, footers, page numbers, running titles). Char Levenshtein with a different block order costs near 100% on the misordered span. This is the favoured hypothesis (also raised in `proto-111:21`).
- Markdown/layout markup counted as errors. `run_bodhan.py:116` scores `result.markdown`; `--normalize` strips HTML tags and `**` (`metrics.py:171,215`) but not `#` headings, `|` tables, list markers or image tags. Bodhan emits 37 layout classes (proto-111:6).
- Failures counted as text. Exceptions become `"[ERROR: ...]"` strings (l.117-118) that are scored (CER ~1.0 each, capped); `empty_or_error` is computed (l.180-182) but its value is not reported anywhere. A handful of OOM/timeouts on 3000x4000 pages could drag the mean.
- Page content outside the recogniser's training: GT-forensics already flags ks/mr/gu/ur GT as VERIFY-FIRST and ne as barred (`OCR_AGENT_MEMORY_FEED.md:245`); 983 of 1,283 items have unknown quality (`W4.md:106`). A pooled mean over such tiers is not the Bodhan error.
- Mean is unweighted over a manifest-order sample; one bad script (Perso-Arabic or Ol Chiki, no engine emits it) can dominate 99 items.
Exact diagnostic (CPU/MPS-safe, one afternoon, needs only the saved preds):
1. Re-load `level2/unified/out/preds_bodhan_4bit_probe.json` (the 99) and `..._pair.json` (300). Report count of `[ERROR:` / empty preds and CER with those removed.
2. Order-invariant page CER: split GT and pred into lines/blocks, then compute (a) bag-of-lines CER via best-match assignment (Hungarian on per-line edit distance), (b) CER after sorting both sides' lines by (y, x) if bboxes exist, (c) a character-multiset F1 (order-free). If (a)/(c) is near 0.05-0.10 and plain CER is 0.69, the gap is ordering/concatenation.
3. Strip markdown (`#`, `|`, `-`, `*`, image tags) from pred and re-score; delta isolates markup.
4. Per-script and per-tier table (language from the manifest, tier from `gt_source`), median alongside mean, plus the `_bound_rate` cap count (`cer_uncapped`, `metrics.py:545`).
5. Eyeball 10 pages: GT vs pred side by side for 3 gold-pair, 3 PDF-layer, 4 worst. Record in a file under `docs/campaign/`.
6. Control: run the MLX recogniser on crops cut from the SAME probe pages using the Bodhan layout boxes and score block-wise against `page.get_text("blocks")` text (proto-89 §B method). Block-level CER near 0.05 confirms the layout/ordering story.
Done-when: a table with plain CER, order-invariant CER, markup-stripped CER and error-excluded CER for the same 99 + 300, and one sentence naming the dominant cause.

## GAPS
- P0 Official PyTorch path never run (R-13 says every result must reproduce on it). Blocker text: "vendor code asserts CUDA" (`DISPATCH_LOG.md:706`; `BODHAN_BASELINE.md:20`). Exact assert location is in the vendor tree `level2/models_bodhan/indic-ocr/` (`idp_*.py`, `app.py`, `config.json`, `ARCHITECTURE.md` per `blind_verify_gate1.md:52`), not in this snapshot; `run_bodhan_pytorch.py` imports `indic_ocr` and its failure is swallowed per item (l.141-143) so a wrong API would produce 99 empty packs silently.
- P0 O-1 unexplained; the "Page Expert" claim is blocked on it (`proto-108:364`, `NEXT.md:5`).
- P0 Product has no Bodhan: the CLI dry run used Tesseract and Bodhan is a "stub/placeholder block" (`DISPATCH_LOG.md:542,560`); `product/` has no code in the repo snapshot.
- P1 No handwriting number for Bodhan at all (`gaps_misc.txt:312`), yet the official test is 5,344 Bengali handwritten words; Bodhan is the Page Expert only.
- P1 Parity (MLX vs PyTorch) unmeasured; GPU SSH missing (`NEXT.md:6`); no per-script 4-bit/bf16 (B-01) table.
- P1 Scoring mismatch: the 84.94/87.39 headline is word accuracy on a scorer we do not have; our 0.054 is CER on `metrics.py`.
- P2 Script hygiene: collision of output file names, hard-coded Mac paths, stale docstring, `--skip-existing` flag that cannot be turned off (`action=store_true, default=True`, pytorch l.96), stratified sampler not random, `parity` mode a stub, no seeds recorded in run_bodhan.py.

## CONCRETE NEXT ACTIONS
1. Locate the assert. On the Mac: `cd level2/models_bodhan/indic-ocr && grep -n -E "cuda|is_available|assert|\.to\(|device|flash|bfloat16" *.py config.json`. Record file:line in `BODHAN_BASELINE.md`. Done-when: the file:line and the exact assert text are quoted.
2. Smallest unblock without GPU: do not edit the vendor tree; in `run_bodhan_pytorch.py` set `device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"`, pass it to the loader if `from_pretrained` accepts `device`/`device_map`, else monkeypatch `torch.cuda.is_available`/`.cuda()` at import time for the run only. Replace hard-coded `DEVICE` (l.33) with the detected value in the pack's `device` field. Done-when: one image returns non-empty text on the PyTorch path.
3. Make failures loud: in `run_bodhan_pytorch.py` abort if the first 3 items error; log the traceback. Add `--no-skip-existing`.
4. Fix `run_bodhan.py` (tag includes sample N / mode; `REPO = Path(__file__).resolve().parents[2]`; real `surya_pair_comparison` that prints the 0.5660 and its source file; save the 99 ids to `level2/unified/out/ids_sample99.json`). Done-when: re-run of sample-100 reproduces 0.6878 +-0.001 and writes distinct files.
5. Run O-1 diagnostic above; write `docs/campaign/O1_PAGE_GAP.md`.
6. Parity: `python level2/benchmark/run_bodhan_pytorch.py --ids-file level2/unified/out/ids_sample99.json` then `--pair-only`; score both with the same `metrics.py --normalize`. Done-when: MLX vs PyTorch CER delta table (overall and per script) in `BODHAN_BASELINE.md`; target |delta| <= 0.01.
7. GPU day (when SSH lands): same command on CUDA (device tag `cuda`), then full manifest with tiers; record seconds/page.
8. Product wiring: add `product/engines/bodhan_page.py` implementing the same contract as the Bodhan stub (`DISPATCH_LOG.md:560`): `recognise(image) -> blocks[{bbox, text, order, script}]` from the PyTorch parser (NOT MLX); emit the attribution line in the output NOTICE; select device automatically; fall back to Tesseract only on exception, with the fallback recorded in the output JSON. Add `torch`, `transformers` pins to `requirements.txt` and the CUDA/CPU Docker target. Done-when: `python -m product.cli --engine bodhan page.jpg` produces JSON + searchable PDF + MD from Bodhan on a laptop CPU and on the GPU, and the 6 dry-run pages (ta/te/kn) are re-run with it.
9. Licence: keep Bodhan as an internal component of the submission (U28; do not offer a hosted endpoint without written approval) and ship the attribution notice.

## RISKS
- Page CER stays high after the diagnostic (real model weakness on our pages): then "Page Expert" cannot be sold as a score claim; sell layout/Indic coverage only.
- CPU latency on the 0.8B recogniser plus layout model may be impractical for the product demo; MLX numbers (0.52 s/crop) do not transfer.
- Vendor assert may hide more than device selection (flash-attention, bf16 kernels); patching may change numerics, so parity must be re-measured, not assumed.
- Single-writer hazards in `level2/` already caused one incident (`DISPATCH_LOG.md:265`); edit via a copy and keep out of sealed dirs.
- Numbers reused by the plan (86.4, 0.5660, "CONDITIONAL PASS") currently have no script behind them; quoting them to Vinay before step 4-6 is a credibility risk.
