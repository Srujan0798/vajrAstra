# A1-PRODUCT: audit of /home/user/boss/product/

Method: full tree walk plus grep of the whole repo for every claim about product/. The snapshot has text files only, so weights, images and the /tmp dry-run outputs are not present. "Absent from the snapshot" is not the same as "never existed", but the git history decides the question below.

## STATE (verified)

- `product/` contains exactly ONE file: `product/docs/B21_SYNTHETIC_LINES_SPEC.md` (151 lines). `find product -type f` returns only that file.
- `git log --all --stat -- product` shows a single commit (afa466c "boss snapshot 3") that added only that spec. No other product file was ever committed.
- None of these exist anywhere in the repo: `product/cli.py`, `schema.py` / `page.schema.json`, `pdf_writer.py`, `script_id.py`, recognisers, `product/requirements.txt`, `product/Dockerfile`, `product/tests/`, `product/__init__.py`. A find for `Dockerfile*` and `*schema*` outside `docs/` returned nothing relevant. (The only schema.json files are `docs/probe/schema.json` and research artifacts.)
- The B21 spec is a DRAFT design. It names a generator, `python -m product.tools.gen_synthetic_lines` (`product/docs/B21_SYNTHETIC_LINES_SPEC.md:101`), and an `audit_licenses` tool (`:127`). Neither exists. The spec also has duplicate section numbers (two section 7s, two G4 gates).
- Root `requirements.txt` has two lines only: `pymupdf>=1.24`, `google-genai>=1.0`. It has no torch, transformers, pytesseract, pillow or numpy.
- What does run today lives in `level2/`, not `product/`:
  - `level2/run_engine.py:249` `ocr_tesseract_indic(image_path, lang)` is pytesseract on a PIL image with NFC normalisation. It returns plain text only, with no boxes, no confidence and no language detection.
  - `level2/engines/__init__.py` is a registry of `BaseEngine.run(png) -> str`. `level2/engines/local/tesseract_indic.py` wraps it.
  - `level2/tests/run_tests.py` (189 lines, stdlib, no pytest) checks the registry (12 engines), the Sarvam dry-run contract, pack schema and NFC. It does not test product code.
  - PyMuPDF is used only for rasterising and reading PDF text (`level2/run_engine.py:203-224`, `scripts/rasterize_page.py`). No PDF writing with a text layer exists anywhere in the repo.
- Bodhan code that exists:
  - `level2/benchmark/run_bodhan_pytorch.py` (169 lines) is an eval runner. It imports `from indic_ocr import IndicOCR` and calls `IndicOCR.from_pretrained(str(MODELS))` (`:115-117`). It calls `parser(str(img_path))` and stores `result` as a string, or `json.dumps(result)` if the result is not a string (`:137-138`). So the return type of the official API is unknown even to the author.
  - `level2/unified/run_bodhan.py` (243 lines) is an MLX path, using `IndicOCRPipeline().process(img).markdown` (`:104-106`) and mlx_vlm.
  - Both hard-code `REPO = Path("/Users/srujansai/Desktop/South")` (`run_bodhan_pytorch.py:30`, `run_bodhan.py:33`).
  - `run_bodhan_pytorch.py:34` hard-codes `DEVICE = "mac-m4-mps"`. It is only a log tag; there is no `.to(device)` or CUDA/CPU selection.
  - Neither script is a product: both are manifest-driven, and neither writes a PDF, MD or page JSON.
  - `level2/models_bodhan/` is absent from this snapshot.
- Script ID: the only existing script identification is IndicPhotoOCR's CLIP identifier at `.deps/IndicPhotoOCR/.../CLIP_identifier.py`, reported at `level2/benchmark/docs/fix_specs/W1H_PLAN_FIXES.md:20`. It is not vendored in the repo (`.deps/` is gitignored). Its sat/mni gap is noted at `docs/campaign/protocols/proto-89-plan-v3-bodhan-base.md:33`, which specifies a Unicode-range script ID instead.

## CLAIMED-BUT-UNPROVEN

- `BOSS_CONCERNS.md:37`: "`product/` exists (schema, cli, pdf_writer, script_id, tesseract + bodhan recognisers)". No such file is in the snapshot or in git history. Unproven.
- `BOSS_CONCERNS.md:38`: "`product/requirements.txt` and `Dockerfile` EXIST". The same claim appears at `docs/campaign/checkpoints/W4.md:460-461` ("DONE 2026-09-30"; the section is duplicated 2 to 3 times) and in `.ecc/memory/project/handoffs/*`. Absent here. Unproven. The `W4.md` text describes a CUDA base image and an optional MLX install via `MLX_INSTALL=1`, but no file shows it.
- `W4.md:536-560` "P CPU DRY RUN PASS": 6 pages (ta/te/kn) produced JSON, PDF and MD, "schema matches `page.schema.json`", and a PDF of 1.2MB. The outputs went to `/tmp/product_dryrun_out/`, so they are not in the repo.
  - `page.schema.json` does not exist in the snapshot.
  - The Tamil sample reports confidence 0.20.
  - `docs/campaign/checkpoints/NEXT.md:5` itself admits "product dry run used Tesseract only" and "Bodhan PyTorch path + page-gap O-1 unproven".
  - The "Bodhan stub" returns a placeholder block, so Bodhan was never run in the product.
- `DISPATCH_LOG.md:604-605` has timestamps only, with no output.
- `W4.md:5` and `BODHAN_BASELINE.md`: "Bodhan weights ARE on disk, 5.35GB". Not verifiable here. `BODHAN_BASELINE.md` is described as a 403 stub elsewhere (`.ecc` handoffs). No Bodhan CER, latency or parity number exists. Sample-100 and parity are "NOT run".
- `W4.md:455-492` "P — Product layer DONE". Only the B21 spec is verified. "DONE" is false for the product.

## GAPS (ranked)

P0
1. No product code at all: no `product/` package, no CLI, no schema, no PDF writer, no script ID, no recogniser classes. The pipeline image/page -> JSON + PDF + MD does not exist in this repo.
2. No Bodhan inference wrapper that is device-aware (CPU/CUDA/MPS), loads from a configurable path, and returns structured blocks. `run_bodhan_pytorch.py` is Mac-pathed and returns an unknown type. The `from_pretrained` return type and the `.process` / `.markdown` field set are undocumented in the repo. The first real job is to read the weights' `indic_ocr` source and write down the actual output type (text, markdown or blocks with bbox).
3. No Bodhan weights in the snapshot, and no run has ever been verified: 0 CER, 0 latency, 0 CUDA/CPU result. Weights sit on the boss's Mac, gated on HF.
4. No packaging: no `product/requirements.txt`, no `Dockerfile`, no `pyproject.toml`. Root `requirements.txt` lacks torch and transformers.
5. Zero product tests.

P1
6. No searchable-PDF writer. It needs an invisible text layer (PyMuPDF `insert_text` with `render_mode=3`) and an embedded Indic font. Complex-script shaping and ordering are the risk; see RISKS.
7. No script ID. Needed: a Unicode-range classifier, per proto-89, covering Ol Chiki U+1C50-1C7F, Meetei Mayek U+ABC0-ABFF and U+AAE0-AAFF, Devanagari, Arabic (ks, ur, sd), Bengali and so on, plus Latin. This is deterministic and testable without weights.
8. No page JSON schema. Define blocks: `bbox`, `text`, `script`, `lang`, `conf`, `engine`, `reading_order`.
9. Hard-coded `/Users/srujansai/...` paths in both Bodhan scripts block any other machine.
10. The Tesseract recogniser has no boxes or confidence. It needs `pytesseract.image_to_data`. Installed Tesseract langs cover only tam/tel/kan/hin/eng (`W4.md:606-620`; dogri and sanskrit are empty).

P2
11. The B21 generator and `audit_licenses` are not built, and the spec has duplicate numbering. Training-side only, not needed for the pipeline.
12. No MLX/PyTorch parity number (K-02).
13. `product/` is not gitignored, but `.gitignore` excludes `*.pdf` and `*.png`, which would swallow test fixtures. Use `!product/tests/fixtures/**`.

## CONCRETE NEXT ACTIONS (minimum code to a working pipeline)

Single package `product/` (files are new):
1. `product/schema.py`: `Block`, `Page` dataclasses plus `to_json()`; `product/page.schema.json` generated from them. Done when: `python -c "from product.schema import Page"` works and a round-trip test passes.
2. `product/script_id.py`: `detect_script(text) -> {script, lang_hint, ratio}` by Unicode block counts (Ol Chiki, Meetei Mayek, Arabic, Bengali, Devanagari, Latin and the rest). Done when: `tests/test_script_id.py` covers 22 scripts and sat/mni.
3. `product/recognisers/base.py` with `Recogniser.recognise(PIL.Image, lang) -> list[Block]`.
   - `recognisers/tesseract.py`: pytesseract `image_to_data`, grouped by `block_num`, with confidence, reusing the `TESS_STACK` mapping from `level2/run_engine.py`.
   - `recognisers/bodhan.py`: `load(model_dir, device)`, where `device` = `cuda` if `torch.cuda.is_available()` else `cpu` (MPS only by flag), and `recognise()` calls `IndicOCR.from_pretrained` once, then converts the output to `Block`s. Normalise to NFC. If the output is a plain string, emit one full-page block with `bbox=None`. Done when: on any machine with weights, `recognise(img)` returns a non-empty list on CPU (CUDA verified separately on a GPU box).
4. `product/pdf_writer.py`: `write_searchable_pdf(image, blocks, out)` uses PyMuPDF. It draws the image as the page background, then invisible text (`render_mode=3`) at the block bbox using an embedded Noto font file shipped under `product/fonts/`. Done when: `pymupdf.open(out)[0].get_text()` equals the expected text, tested on a Devanagari sample.
5. `product/md_writer.py`: blocks to Markdown, in reading order. Done when: a unit test passes.
6. `product/cli.py` with `python -m product.cli <path|dir> --engine {bodhan,tesseract,auto} --device {auto,cpu,cuda} --lang auto --out DIR`:
   - Rasterise PDFs via `scripts/rasterize_page.py` logic at 200 dpi.
   - Emit `<stem>.json`, `<stem>.pdf`, `<stem>.md`.
   - `auto` = Bodhan first, then fall back to Tesseract when the output is empty.
   - Done when: it exits 0 and writes all 3 files for 1 ta, 1 hi and 1 bn page.
7. `product/requirements.txt`: `torch` (CPU wheel by default, CUDA via an index-url comment), `transformers` (pin to whatever `indic_ocr` requires; read it from the weights repo), `pymupdf>=1.24`, `pytesseract`, `pillow`, `numpy`. Optional `mlx; sys_platform=="darwin"`. Done when: `pip install -r` succeeds in a clean venv.
8. `product/Dockerfile`: python:3.11-slim plus apt `tesseract-ocr tesseract-ocr-all` plus fonts; a CUDA variant via `ARG BASE=nvidia/cuda:12.x-runtime` with the torch cu12x wheel. Weights are mounted at `/models/indic-ocr`, not baked in (the licence needs attribution and a hosting approval, `proto-104:71`). `ENTRYPOINT ["python","-m","product.cli"]`. Done when: `docker build` succeeds and `docker run ... --engine tesseract` produces 3 files.
9. `product/tests/`: schema, script_id, pdf_writer and a CLI smoke test using Tesseract on one fixture. Run with `python -m unittest` (matches the repo's no-pytest convention). Done when: green in CI-less local run.
10. Fix `level2/benchmark/run_bodhan_pytorch.py` and `level2/unified/run_bodhan.py`: replace `REPO = Path("/Users/...")` with `Path(__file__).resolve().parents[2]` or an env var, and replace the hard-coded `DEVICE` with the detected device. Done when: `grep -rn "/Users/srujansai" level2/benchmark/run_bodhan_pytorch.py` returns nothing.
11. Retract the false claims: correct `BOSS_CONCERNS.md:37-38` and the W4.md "P DONE" blocks to "only B21 spec exists". Done when: `ls product/` matches the claim.
12. Measurement (needs the weights): run `product.cli` with Bodhan on 20 pages on CPU and on CUDA, and log seconds/page, CER via `level2/benchmark/pipeline/metrics.py`, and the PyTorch vs MLX parity number. Done when: numbers are written to a file with a reproduce command.

## RISKS

- Bodhan's real API is unverified in this repo (string vs structured output, bbox availability). If it returns Markdown only, there are no per-block bboxes, and a searchable PDF can only carry full-page invisible text, with poor selection alignment. Layout would then need a separate layout model (the Bodhan IndicDocLayout, `proto-104:111`).
- The Bodhan weights are gated on HF (`proto-104:411`), and hosting the weights has a licence limit (`proto-104:71`), so the Docker image cannot bake them in.
- CPU latency of a 0.8B VLM (Qwen3.5-0.8B per `proto-104:112`) is unmeasured. A per-page CPU timing may be too slow for a deadline that is itself unconfirmed.
- Invisible-text PDFs in complex scripts (Arabic RTL, Indic conjuncts) can extract wrongly, with reordered or split glyph text, unless the font has the right cmap/ToUnicode. Validate the extract per script.
- Tesseract ta, te, kn and hi work, but sat, mni, dogri and sanskrit have no traineddata. The fallback is empty for those.
- Process risk: five or more documents record "DONE" for work that is not on disk. The planner should treat any `W4.md` status without a reproducing command as CLAIMED.
