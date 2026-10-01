# probe22 — remaining-language probe (100×18×10)

- Law: `docs/probe/W3_PROBE_SCHEMA.md`
- Execution protocol for agents: `AGENT_PROTOCOL.md` (this directory)
- Source (user decision 2026-09-26): `../../Datasets/akshardrishti_official/` (official hackathon dataset, 34,871 files)
- Size (user lock 2026-09-26): **100 samples per language × 18 languages × 10 engines**

## Tools (verified working 2026-09-26)

- `extract_gt.py --code <code>` — Phase 1: scan official PDFs, apply honesty gates (≥50 chars, script-ratio ≥ 0.5, Latin ≤ 0.6), collect direct pairs (`.jpg`/`.jpeg` + `.txt`), write `candidates/<code>.json`.
- `build_manifest.py --code <code>` — Phase 2+3: draw 100/lang (pairs first, then stratified PDF pages at 200 dpi, then Sarvam fill for shortfalls), materialize images, write `manifest_fragments/<code>.json`.
- `build_manifest.py --merge` — Phase 4: merge all fragments into `manifest.json` (expect 1,800 items).
- `run_probe.py --engine <e> --skip-existing` — all 10 engines ported. Packs in `out/`.
- `metrics.py` — scoring (CER/WER with Indic normalization + loop detection).

## Verified state (2026-09-26)

- **Manifest FINAL: n_total = 1229** (1,340 drawn, 111 control-char-corrupt GT purged; backups `manifest.json.pre-purge`, fragments `*.pre-purge` — never re-merge from backups). Per-lang n: bn/hi/ks/kok/mai/sa/ur 100, pa 90, mr 79, sd 75, or 70, brx 67, ne 37, gu 24, doi 27, as 20, mni 20, sat 20. Low-confidence (n<50): as, gu, ne, doi, mni, sat.
- All 10 engine runners are probe-native in `run_probe.py` (zero calls into `run_engine.py` — its dicts cover only te/ta/kn/ml and KeyError on probe langs). `--retry-errors` retries error/empty packs without deletion (protocol §5).
- Max-power coverage (user authorized "make it 100%"): rapidocr devanagari+arabic rec models cached (real output for 11/18 langs; as/bn/gu/or/pa/mni/sat honest-empty — no upstream models exist); paddleocr native models for hi/mr/ne/mai/sa/kok/ur/sd, det capped at 1600px (uncapped server det OOM-killed at 57GB on 4250×6500 scans); anuvaad hin+eng for Devanagari family; openbharatocr mirrors tesseract_indic (documented path).
- Full audit passed: no dup image_ids/sources, all 1,229 images resolve, `image_path()` handles `.jpeg` pairs (would have crashed all engines on the 100 Sanskrit pairs), metrics.py normalizers strip control chars, sat_14 verified Bengali-script Santali (surya cross-check), mni metadata corrected to Meitei-Mayek.
- GT audit: PDF text layers cover 100/lang for 15/18 languages. Shortfalls: Dogri (11 clean text pages), Santali (0) → filled from leftover Sarvam images (user approved).
- Bodo PDF layers are legacy-font mojibake; gate rejects them. `Bodo/gu/` is a copy of the main test set — NOT GT.
- Kashmiri fragment verified: 100/100 from validated PDF layers (198 clean, 116 mojibake rejected). Sanskrit fragment verified: 100/100 from human pairs (494 found — `.jpeg` under `Images and Transcription/`).
- Encrypted/corrupt PDFs: 1 as, 1 or, 1 ml, 1 kn — skipped, reported, not replaced.
- Tesseract traineddata: 12 tessdata_best packs in `tessdata/` (asm, ben, eng, guj, hin, mar, nep, ori, pan, san, snd, urd), verified + smoke-tested.
- Old Sarvam-bench run (2026-09-25) discarded; its 360 images kept as fill.
- Do not write probe JSON into `level2/out/` (South 400 seal).
