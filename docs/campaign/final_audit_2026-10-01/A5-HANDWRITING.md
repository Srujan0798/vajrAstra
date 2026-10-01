# A5-HANDWRITING — Track A readiness (proto-108 rev 2 §3)

Snapshot: /home/user/boss (text only). Plan source: `_claude_memory/proto-108-plan-v4-final.md:163-201,294-299,494-509`.

## STATE (verified in this snapshot)
- The Track A plan is fully written: HW-ID, HW0, HW1, G-2.5, HW-SMOKE, HW2, gates and kills (`proto-108:174-201`, kill table `:295-299`). No Track A code, output or result exists.
- `level2/benchmark/handwriting/` does NOT exist. The H2 manifest `official_hw_gu_test_manifest.json` and its generator `build_h2_slice.py` are absent. `blind_verify_H2.md` (`docs/campaign/checkpoints/W4_reports/blind_verify_H2.md:7-35`) describes them (16,490 items, vocab index resolves, 0 mismatches), so the verifier PASS is claimed and not re-checkable here.
- `docs/campaign/H1_TEST_PROFILE.json` exists (Tesseract on 70 crops). `TEST_SET_PROFILE.md:35-47` reports 55.7% UNKNOWN; its "35.7% Devanagari" is retired (`proto-108:~58`).
- IndicPhotoOCR code: only the adapter `level2/engines/local/indicphotoocr.py` (calls `run_engine.ocr_indicphotoocr`) and `level2/run_engine.py:474-493`. That function runs the full scene pipeline (`OCR(identifier_lang="auto", device="cpu")`, detect, identify, recognise) on a page. It is NOT a crop-level Bengali-recogniser entry point. There is no word-crop runner, no scorer and no PARSeq training code.
- `level2/models/indicphotoocr/` and `level2/engine_docs/indicphotoocr/` hold only RUN.md, PROMPT.md, metrics.json and quality_20.json from the 400-page printed run (10 empty). No weights, no `.deps/IndicPhotoOCR`, no `bengali.ckpt` (grep finds none).
- doctr PARSeq gate (`level2/research/gates/B1_doctr_parseq.md:63-80`): zoo weights are French vocab; a reinitialised Telugu head gave script ratio 0.53 but Jaccard-5 0.00. Content gate is required (Jaccard-5 >= 0.3).
- Nothing in the snapshot computes pHash, SHA, WRR or CRR. No Datasets/ directory, no images.
- The training stack needs no download for the code (PARSeq Apache-2.0) but everything else does (see DOWNLOADS).

## CLAIMED-BUT-UNPROVEN
- B12 "91% handwritten, 9% mixed, 300 sampled" (`docs/campaign/B12_HANDWRITING_SHARE.md:35-56`) sits beside "script UNKNOWN for all 300" (`:27-30`). That conflicts with the profile's 13/13 Bengali viewed (`TEST_SET_PROFILE.md:47`). There is no per-image file, so HW-ID has NOT been done and K-ID (<80% single Bengali handwritten words) is open.
- "Bengali 0 labelled handwriting on disk" is stated, not checkable here.
- `bengali.ckpt` availability and its licence: UNKNOWN (`proto-108:~190`; Agent 2 task `:356`).
- Gujarati H2 manifest PASS is path-level only (no writer_id; on-disk jpgs are at `gu/test/test/N.jpg`, 4,645 of 16,490).

## PLAN (exact, runnable)

### Shared scaffolding (create first)
- `level2/benchmark/handwriting/hw_common.py`: `nfc()`, `wrr(pred,gt)` (exact match after NFC, strip), `crr` = 1 - CER via a pure-python Levenshtein, `bootstrap_ci(per_item_bool, n=10000, seed=20261001)`, `wilson(k,n)`, `mcnemar_exact(b,c)`, `jaccard5(a,b)`.
- Done-when: `python -m pytest level2/benchmark/handwriting/tests/test_hw_common.py` passes on 10 hand-made pairs (identical, one matra off, empty pred).
- Rule: all numbers go through this one scorer (proto-108 law: one scorer, set, n, metric, CI).

### HW-ID (read-only, no download beyond the crops)
- Command: `python level2/benchmark/handwriting/hw_id_sample.py --root Datasets/akshardrishti_official/test/test --seed 20260930 --per-bucket 45 --out level2/benchmark/docs/hw_id_sample_ids.csv`.
  - Buckets: 0-999, 1000-1999, 10000-10999, 11000-11999, 12000-12999, 13000-13999, 14000-14806. Bucket 0-999 has only 56 files, so take min(45, size). 7 x 45 = 315 >= 300, and >= 10 per bucket is satisfied.
  - Writes a CSV of image_id, bucket, path, width, height, sha256.
- Then a vision-capable agent (or the boss) fills `level2/benchmark/docs/HW_ID_AUDIT.md`. One row per image: id | script (Bengali/other/UNKNOWN) | single-word / multi-word / non-text | pen colour | quality (clean/mild/severe). Do not use Tesseract for script ID (no `ben` model; retired method).
- Summary block in the same file: % single Bengali handwritten words with Wilson 95% CI, per-bucket table, list of non-Bengali IDs.
- Done-when: >= 300 rows, >= 10 per bucket, summary computed by `hw_id_summarise.py`. K-ID: if the Wilson lower bound < 0.80 or the point estimate < 0.80, STOP and re-plan the router and data (`proto-108:295`).
- Needs: the 5,344 crops on the boss's Mac (not in this snapshot).

### HW0 — leak gate script spec
- File: `level2/benchmark/handwriting/hw0_leak_gate.py`; stdlib + PIL only; fail-closed.
- CLI: `hw0_leak_gate.py --official Datasets/akshardrishti_official/test/test --candidate NAME=DIR [--candidate ...] --out level2/benchmark/docs/HW0_LEAK_REPORT.json --exclude-out level2/benchmark/handwriting/hw0_exclude_ids.txt`.
- Algorithm:
  1. SHA-256 of raw bytes for every official and candidate image; exact overlap is sha256 equality.
  2. Perceptual: 64-bit pHash (convert L, resize 32x32 LANCZOS, 2D DCT written in pure python or with a small matrix, top-left 8x8, median threshold) plus dHash 9x8. Because crops are ~300 px tall and wide, also hash a fixed-aspect version: resize to 32x128 for dHash. Flag a pair if the Hamming distance of pHash <= 6, or of both pHash <= 10 and dHash <= 10. Report the distance histogram so thresholds can be audited.
  3. Index candidates by 16-bit prefix of the pHash (multi-index, 4 bands of 16 bits, any band match gives a candidate pair, then exact Hamming) to avoid O(N*M) over about 100K images. 5,344 x 100K full compare is also acceptable in numpy (about 5e8 popcounts) if numpy is allowed.
  4. Fail-closed: exit code 2 if any candidate directory is missing, empty, has an unreadable image, or the file count differs from the expected count in `--expect NAME=N`. An unreadable image counts as a failure, not a skip.
  5. Output JSON: per candidate set, n_candidates, n_exact, n_perceptual, list of {official_id, candidate_path, ham_phash, ham_dhash}; a top-level `overlap_total`; and the exclusion ID list.
- Candidate sets (each needs a download or already on disk): IIIT bn train/val/test, ICDAR'23 val/test, BN-HTRd, `Bodo/gu` (the sha256 overlap of 0 is already claimed in `blind_verify_H2.md`, so HW0 re-verifies it).
- Companion sweep: `hw0_code_sweep.sh` with `rg -n "gt_text" level2/orchestrator.py level2/engines level2/benchmark/pipeline | rg -v "tests/"` (no gt_text reads in routers or prompts), plus a `gt_source` guard in the train-file builder: refuse any row with gt_source in {sarvam_fill, machine, ocr}. Done-when: the sweep outputs 0 router hits; builder unit test rejects a sarvam_fill row.
- Done-when (gate G-HW0): `HW0_LEAK_REPORT.json` exists, `overlap_total == 0` after exclusion; any hit goes into `hw0_exclude_ids.txt` and is disclosed (K-HW0).
- Self-test required: a unit test that copies 5 images, rescales them 0.8x and jpeg-recompresses them to q=60, and checks they are flagged (otherwise the gate may be silent).

### HW1 — zero-shot runner spec (no training)
- File: `level2/benchmark/handwriting/hw1_zeroshot.py`.
- CLI: `hw1_zeroshot.py --system {ipo_bn,bodhan_hw,tess_ben} --manifest MANIFEST.json --out level2/benchmark/handwriting/out/HW1_{system}_{set}.jsonl [--limit 200 --view-only]`.
- Manifest format (reuse the H2 schema): items with image_id, path, gt_text, set, gt_source, writer_id (REQUIRED for Bengali eval sets; reject if missing).
- System `ipo_bn`: do NOT call the page pipeline. Load IndicPhotoOCR's Bengali recogniser directly (the STocr PARSeq `bengali.ckpt` under `.deps/IndicPhotoOCR`; exact module path to be read from the repo on the boss's Mac, because it is not in this snapshot). Feed the whole crop to the recogniser, with the resize and normalisation the repo uses, greedy decode. Record the raw string, the confidence, and seconds per word. Record the recogniser input size actually used.
- System `bodhan_hw`: the official PyTorch/CUDA Bodhan path only (MLX parity is blocked per `proto-108:~140`), in handwriting mode; same I/O. System `tess_ben`: `pytesseract --psm 8 -l ben` only after the `ben` traineddata is installed.
- Metrics per (system, set), all from `hw_common.py`: WRR, CRR, CER, WER, median CER, catastrophic rate (CER > 0.5), empty rate, s/word, Wilson/bootstrap 95% CI, Jaccard-5 content gate >= 0.3 (never script ratio).
- Official 200 crops: view-only; output strings + s/word only, no accuracy claim (no labels exist). Done-when: JSONL has 200 rows with no empty-path rows, and the file contains no WRR field for the official set.
- IIIT bn val: WRR/CRR with CI; n must equal the README count after download.
- Done-when (G-HW1): `HW1_{ipo_bn,bodhan_hw}_iiit_bn_val.jsonl` + `HW1_SUMMARY.md` with the numbers and the exact commands.
- Cheap local smoke test before anything: run on the 4,645 Gujarati crops using the gu manifest with `--system tess_ben` replaced by the Gujarati recogniser, to prove the pipeline wiring only. Never count it as Bengali evidence (`proto-108:~167`). The manifest paths need the `test/test/` fix first (`blind_verify_H2.md` out-of-scope note).

### G-2.5 (the boss)
- Not code. Training is blocked until the multi-LLM review package is logged and the Vinay session is done, with the HW2 GPU-hour cap set (`proto-108:185-187,325`). Done-when: verdicts logged in `W4.md`.

### HW2 — PARSeq fine-tune recipe (baudm/parseq, Apache-2.0)
Caveat: key names below are from my knowledge of baudm/parseq (Hydra + PyTorch Lightning) and must be checked against the cloned commit. The snapshot has no copy of that repo.
- Environment: clone `https://github.com/baudm/parseq` at a pinned commit; `pip install -r requirements/core.<torch>.txt -e .`; Python 3.9-3.11; record commit + torch version in `HW2_ENV.txt`.
- Data build:
  - `tools/create_lmdb_dataset.py gt.txt out_lmdb` per split. `gt.txt` = `relative/path.jpg<TAB>label`. Directory layout: `data/train/real/iiit_bn/train/`, `data/val/iiit_bn/`, `data/test/...` (the repo expects `<root_dir>/train/<dataset>/<split>`).
  - Normalise labels to NFC; keep ZWJ/ZWNJ (U+200D/200C) as characters if they occur in Bengali conjuncts. Check this on the data before deciding. Drop labels > max length (see below) and log the count. Label cleaning step before training (up to 1.8 CER points, `proto-108:~160`).
  - Writer-disjoint: keep IIIT's own train/val/test; BN-HTRd and ICDAR'23 are eval-only.
- Charset for Bengali (`configs/charset/bengali.yaml`): `model.charset_train: "<all unique code points in the cleaned IIIT bn train+val labels, sorted>"`, `model.charset_test: ${.charset_train}`. Compute with `python -c` from `gt.txt`; typically this includes the 11 independent vowels, 39 consonants (plus ড় ঢ় য় ৎ), vowel signs, hasanta U+09CD, chandrabindu, anusvara, visarga, nukta U+09BC, Bengali digits U+09E6-U+09EF, and the Latin digits and punctuation that occur. PARSeq predicts per code point (not per grapheme), so a conjunct is a sequence ending in U+09CD. There is no way to reuse the 94-char head, so the output embedding and head are re-initialised. Remember the doctr trap: a re-initialised head without enough training emits glyph salad; always check Jaccard-5 on val after epoch 1.
  - Set `data.normalize_unicode: false` (the default NFKD normalisation in baudm/parseq is meant for Latin and would break Bengali; do NFC ourselves), `data.remove_whitespace: true`, `data.max_label_length: 25` (Bengali words with conjuncts need many code points: histogram the train labels first, then use p99.9 + margin, e.g. 32, and make `model.max_label_length` match).
- Config keys to override (CLI): `python train.py +experiment=parseq dataset=real data.root_dir=data model.charset_train=... model.charset_test=... data.charset_train=... data.charset_test=... model.max_label_length=32 data.max_label_length=32 data.img_size=[32,128] model.img_size=[32,128] model.batch_size=256 data.batch_size=256 model.lr=<see below> model.warmup_pct=0.075 model.weight_decay=0.0 model.decode_ar=true model.refine_iters=1 trainer.max_epochs=<see below> trainer.val_check_interval=1.0 trainer.precision=16 trainer.accelerator=gpu trainer.devices=1 ckpt_path=null pretrained=null data.augment=true data.num_workers=8`. Dataset folder name must match `dataset=real` (set via `data.train_dir=iiit_bn`).
- Initialisation order (`proto-108:~189`): (1) synthetic Bengali pre-train (optional, pre-registered, never evaluation, B21 forbids IIIT text as seed); (2) real IIIT bn train. For a first working run, initialise from the PARSeq scene-text checkpoint (`pretrained=parseq` weights, then load with `strict=False` and drop `head.*` and `text_embed.embedding.*` keys, since the vocabulary size changes). If `bengali.ckpt` clears its licence, load that instead: same-script initialisation is worth 92% vs 51% cross-lingual vs 6% scratch in the ledger.
- Image size: Bengali word crops are ~300 px tall and 445-1,630 px wide (aspect 1.5-5.5). 32x128 squashes the width heavily and destroys matras. Run two arms with the same data: A = [32,128] (the scene baseline); B = [64,256] with patch_size [8,16] (bilinear interpolation of the pos-embeds when loading). Choose by IIIT bn val WRR. Pad-and-resize preserving aspect is out of scope for the first pass.
- Augmentation: the repo's `data.augment=true` RandAugment set (rotate, shear, perspective, brightness/contrast, gaussian blur, sharpness, invert, posterize...) is Latin-tuned but fine. Do not enable `invert`, because it is a pen-colour change on a white page. Add ink/colour jitter on blue pen and Otsu binarisation with p=0.2 through a custom transform in `strhub/data/aug.py`. No horizontal flip, no vertical flip, no crop that cuts conjuncts.
- Epochs and batch on a 24 GB GPU: batch 256 at 32x128 fp16 (parseq-base uses far less than 24 GB; try 384 at 32x128 and 128 at 64x256; reduce if OOM). Dataset ~82.5K words, so one epoch is ~322 steps at 256. Run 40 epochs for arm A (about 13K steps; the original scene-text recipe is 20 to 100 epochs on far larger data) and 60 for arm B; cosine/OneCycle via the repo's `lr` scheduler; peak lr `model.lr = 7e-4` for from-scratch heads, 1e-4 for a full fine-tune from a pretrained backbone, `model.lr` is scaled by batch size in the repo (`lr = lr * batch_size / 256`; check this in `train.py`). Early-stop on val WRR (`val_NED`/`val_accuracy` monitor, `ModelCheckpoint(monitor="val_accuracy", mode="max")`).
- HW2 GPU budget: cap set by the boss at G-2.5 (`proto-108:325`). Ballpark 1 to 3 GPU-hours per arm; that is my estimate, not measured.
- Smoke first (HW-SMOKE): 5 items, <= 10 min, abort if disk < 20 GB free; 3 failures abort to baseline; at most 2 re-attempts.
- Eval: `read.py`/`test.py --checkpoint X --data_root data --test_on iiit_bn_val,bn_htrd,icdar23` or reuse `hw1_zeroshot.py --system parseq_ft` for identical scoring. Report WRR/CRR/CER/WER/median/catastrophic/empty/s-per-word + 95% CI. The G-HW2 proxy: IIIT bn val WRR >= 92%. The claim gate: independent-writer WRR >= 85%, n >= 300 words, writer-disjoint, CI reported (`proto-108:198-201`).
- Promotion: paired McNemar exact (or paired bootstrap) on the same items vs the HW1 zero-shot, p < 0.05 AND >= +3 points, else ship zero-shot (K-HW2). Kill: < 85% IIIT val after 2 epoch-equivalents leads to switching the recipe (CRNN+LM, or the PARSeq base init).
- Optional LM rescoring with the train lexicon: only kept if WRR rises. Expectation: ~91-92% for a single model; do not promise 96.10.
- Files to create: `level2/benchmark/handwriting/hw2/{build_lmdb.py,charset_bn.py,train_cmd.sh,eval_cmd.sh,HW2_ENV.txt}` and `level2/benchmark/docs/HW2_RESULT.md`. Done-when: checkpoint + `HW2_RESULT.md` with the numbers, commands, CI, and the paired test vs HW1.

## DOWNLOADS (boss; each needs a go per the law)
- 5,344 official crops, local on the Mac (HW-ID, HW0, HW1). Not in the snapshot.
- IIIT-INDIC-HW-WORDS Bengali from AIKosh (U-HW1). The size and the test-split count (17,575 vs 18,574) are unconfirmed. Licence discrepancy: CC BY 4.0 vs academic-use (`proto-108:336`). Confirm first.
- IndicPhotoOCR repo + STocr `bengali.ckpt` and its licence (UNKNOWN, `RQ9_licences.md:199-201`).
- Bodhan weights (PyTorch/CUDA path) under the Indic Open Model License.
- Tesseract `ben` traineddata.
- BN-HTRd (licence check) and ICDAR'23 val/test (eval-only, if obtainable) (U-HW2).
- baudm/parseq repo (Apache-2.0) and the PARSeq scene-text pretrained weights, plus the 24 GB GPU environment.
- Synthetic-Bengali fonts (OFL) if the pre-train step is run.

## GAPS (ranked)
- P0: HW-ID was never done; K-ID is open and gates the whole of Track A. The B12 "300 sampled" is a claim with no per-image evidence and contradicts itself.
- P0: No HW0 script exists; with no candidate sets downloaded the gate cannot close.
- P0: No word-crop recogniser entry point; the existing adapter runs the page pipeline.
- P1: The H2 manifest and builder are not in the repo snapshot (are they uncommitted on the Mac?).
- P1: `bengali.ckpt` licence/availability and the IIIT licence are unresolved; G-2.5 is not scheduled.
- P1: No writer_id in the Gujarati manifest; independent-writer evaluation needs it for Bengali.
- P2: Gujarati smoke path fix; label-cleaning tooling.

## RISKS
- A glyph-salad head passes a script-ratio gate; use only the content gate (Jaccard-5).
- Wrong NFKD normalisation in the repo default corrupts Bengali labels silently.
- 32x128 squash may cap WRR well below 92%.
- Leakage via a different scan of the same page will evade a hash gate with a loose threshold; the report must show distance histograms.
- The 96.10 figure was an ensemble with large pre-training; a single model is expected near 91-92.
