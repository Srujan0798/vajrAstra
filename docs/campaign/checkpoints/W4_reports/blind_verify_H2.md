# Blind verify — §H H2 labelled handwriting eval slice (Gujarati / IIIT-HW)

Verifier: blind subagent (no prior context). Repo: `/Users/srujansai/Desktop/South`.
Scope: only the four checks the orchestrator handed me. No fixes.

## Files read
- `level2/benchmark/handwriting/official_hw_gu_test_manifest.json` (5.0 MB JSON, 164912 lines, 16490 items)
- `Datasets/akshardrishti_official/Bodo/gu/{train,val,test}.txt`
- `Datasets/akshardrishti_official/Bodo/gu/vocab.txt`

`wc -l`: train=82563, val=17643, test=**16490**, vocab=10963 (no trailing newline → 10964 entries when split).

## Check 1 — Manifest reads cleanly & is internally consistent — **PASS**
- Manifest opens as JSON. Top-level fields: `created=2026-10-01`, `generator=level2/benchmark/handwriting/build_h2_slice.py`, `source=Datasets/akshardrishti_official/Bodo/gu/`, `tier=official_hw`, `language=gu`, `script=gujarati`, `n_items=16490`, `n_words=10964`.
- `len(items) == 16490 == n_items`. Every item carries `image_id`, `path`, `language=gu`, `script=gujarati`, `set=official_hw`, `gt_source=iiit_hw`, `vocab_index`, `gt_text`. No null/missing fields.
- `image_id` is a string, 16490 unique, range 1…16513. `image_id` == basename(path) without extension (0 mismatches).
- `vocab_index` values in [0, 10963], 8113 unique (word forms reused across crops). `gt_source` uniformly `iiit_hw`.

## Check 2 — LEAK RULE (writer/page disjoint train vs eval) — **PASS (path-level)**
- Manifest contains 0 paths under `train/` and 0 under `val/` (all 16490 are `…/test/N.jpg`).
- test.txt ∩ train.txt = 0; test.txt ∩ val.txt = 0 (path sets disjoint — splits are namespaced by directory).
- Manifest rel-paths = test.txt paths exactly (16490 ↔ 16490; 0 manifest-only, 0 test-only).
- Caveat the orchestrator should be aware of: the manifest carries no explicit `writer_id` / `page_id` field. Disjointness rests on (a) split-directory namespacing and (b) the upstream IIIT-HW Gujarati writerscript convention. I cannot independently audit IIIT-HW's writer assignment from this slice alone.

## Check 3 — n_items matches test.txt line count — **PASS**
- Manifest `n_items = 16490`. `wc -l test.txt = 16490`. Exact match. `len(items) = 16490` reconciles both.

## Check 4 — Vocab index resolves to vocab.txt — **PASS**
- vocab.txt: 10964 non-empty entries (10963 newlines + no trailing `\n`).
- Manifest `n_words = 10964` == vocab entry count.
- Full sweep: for every one of 16490 items, `vocab_lines[vocab_index] == gt_text`. **0 mismatches, 0 out-of-bounds.** Indices are 0-indexed. Max vocab_index = 10963 = len-1.
- Spot-checks (indices 8831, 3220, 4160, 6697, 4388, 480, 6016, 373, 546, 2049) all resolve to the manifest's `gt_text` exactly.

## Out-of-scope finding the orchestrator may want to know
The manifest `path` field says `Datasets/akshardrishti_official/Bodo/gu/test/{N}.jpg`, but on disk the jpgs live one level deeper at `…/test/test/{N}.jpg`. `train/` and `val/` directories do not exist on disk at all (only `test/test/` with 4645 jpgs). The manifest's path strings are consistent with test.txt and with each other, but the consumer of this manifest will have to resolve the actual on-disk location before scoring. Flagging it; not scoring as a §H H2 fail because none of the four checks I was given asked about on-disk image existence.

## Verdict
**PASS** on all four assigned checks.
