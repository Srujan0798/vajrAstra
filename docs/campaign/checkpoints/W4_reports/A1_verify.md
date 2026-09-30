# A1_verify.md — BLIND VERIFICATION of proto-102 step A1 pre-image

Verifier: blind subagent. Watched nothing. Every number below is my own measurement,
taken 2026-09-30 17:08–17:11 IST. No file was modified, deleted or repaired.
Scratch work: `/tmp/opencode/a1_verify/` (outside the repo).

## Verdicts

| # | Claim | Verdict | My measurement |
|---|-------|---------|----------------|
| a | manifest holds 19,202 lines covering `level2/` + three `_archive/south_*_2026-09-30/` | **VERIFIED** | `wc -l` = **19,202**; last byte is `\n`, so the count is exact |
| b | bundle exists, 151,599,725 bytes, `tar -tzf` lists 230 entries | **VERIFIED** | `stat` = **151,599,725**; tarlist = **230** (23 dirs + 207 files) |
| c | extract + re-hash = 207/207 = 100%, 0 mismatch, 0 missing | **VERIFIED** | my own extraction: **207/207 = 100%** |
| d | tarball sha256 `ac9af7e5…c08444` | **VERIFIED** | `ac9af7e5df989b109baaeb065f3b6d52f1776c3eeca5c0e418df27e481c08444` (recomputed twice, stable) |
| e | `shasum -c` = 19,201 OK / 1 FAILED, failure = `level2/unified/run_bodhan.py` | **VERIFIED** (see note) | **19,201 OK / 1 FAILED**; failure is exactly that file |

Note on (e): the *outcome* and the *identity* of the failing file are verified. The
specific mtime **17:01:15** is **UNVERIFIED** — I cannot read a historical mtime. The
file's current mtime is **2026-09-30 17:03:19**, which corroborates the executor's second
timestamp. The concurrent-rewrite story is consistent with the timeline below.

## 1. Manifest re-hash (claim a) — 151 unique paths, 151/151

Uniform random 60 was useless on its own: 48/60 landed in `level2/benchmark/packs`
(69% of the manifest) and **zero** hit `level2/out`, `engine_docs` or `benchmark/pages`.
So I added a stratified sample and an exhaustive pass.

| Batch | Selection | Match |
|-------|-----------|-------|
| A | uniform random 60 (`shuf`, seed 42) | 60/60 |
| B | stratified 50 from the non-`packs` population (`shuf`, seed 7) | 50/50 |
| C | **exhaustive**: all 30 `engine_docs` + 9 `_archive/south_unified_symlinks` + 4 `training_assets` | 43/43 |
| | **unique paths after de-dup** | **151/151 = 100%** |

Zero mismatches, zero missing. Manifest scope re-derived:
`level2` 18,791 + `_archive/south_renders_shared` 400 + `_archive/south_unified_symlinks` 9
+ `_archive/south_pages_400_symlinks` 2 = **19,202**. Claim (a) is exact.

## 2–3. Bundle identity and size (claims b, d)

```
shasum -a 256 _archive/bundles/2026-09-30_incident_pre_repair.tar.gz
ac9af7e5df989b109baaeb065f3b6d52f1776c3eeca5c0e418df27e481c08444
stat -f %z  -> 151599725
tar -tzf | wc -l -> 230     (tar exit 0)
```
Both claims exact. mtime of the tarball: 17:01:06.

## 4. My own extraction (claim c) — 207/207

Extracted to `/tmp/opencode/a1_verify/extract/`, exit 0, **log empty** (no warnings).
- random 30 files I picked from the extracted tree: **30/30** vs manifest
- then **all 207** extracted files: **207/207 = 100%**, 0 mismatch, 0 not-in-manifest

No mismatch was found, so there is nothing to quote verbatim.

## 5. Readability and subtrees

`tar -tzf` exit **0**; `tar -xzf` exit **0** with an empty warning log.
Present: `level2/benchmark/` (docs, logs, logs_killed, pipeline) and `level2/engine_docs/`
(10 engine subdirs, 30 files). Both required subtrees are there.
Tar contains **no symlinks, no hardlinks** (207 `-` regular files + 23 `d` dirs) and
**no absolute or `../` paths** (0 hits) — the bundle is safe to extract.

## 6. Is the manifest self-serving? No — it is not stale

All **19,202** manifest entries were existence-checked: **0 point at paths that no longer
exist.** Every file it claims to hash is really on disk. Combined with 151/151 content
matches, the manifest is a truthful index, not a self-referential receipt.

## 7. Independent `shasum -c` (claim e) — reproduced exactly

```
shasum -a 256 -c docs/campaign/audit/incident_pre_repair.sha256 > check.log
exit 1   |   19,201 ": OK"   |   1 FAILED   |   1 "WARNING: 1 computed checksum did NOT match"
```
Failing entry, verbatim:
```
level2/unified/run_bodhan.py: FAILED
  manifest expects 7e4f315a105ea45ca39a582aea6ca36497e3ca8e67d160b3c03cc26525bb98b9
  disk actually is  803107d65d96da349038a37f2ade60b91e9a66a95980a0bc7bafd288572275e7
  mtime 2026-09-30 17:03:19, 10,680 bytes
```
Timeline supports the executor: manifest frozen 17:00, tar 17:01:06, then the file was
rewritten at 17:01:15 and 17:03:19 — i.e. **after** the snapshot. The snapshot is
self-consistent; the file drifted afterwards. The claim is honest, not a cover-up.

## 8. Coverage judgement — the tar honours A1's exclusions, but the bundle is NOT adequate

**Exclusions honoured, as required:**
| Requirement | Measured |
|---|---|
| `level2/benchmark/pages` absent from tar | **0** entries in tarlist |
| `level2/benchmark/packs` absent from tar | **0** entries in tarlist |
| manifest still hashes them | pages **1,194**, packs **13,289** |

**What the executor did not report, and it matters:** the manifest and the bundle cover
*different scopes*. The manifest hashes **19,202** files; the tar stores **207**. The
tar covers exactly `level2/benchmark` (minus pages/packs) + `level2/engine_docs` and
**zero** of the three `_archive/south_*_2026-09-30/` folders that claim (a) says the
manifest covers — 411 hashed entries / **572 MB** with no byte-level backup anywhere.

- 18,995 of 19,202 manifest files (98.9%) are **not** in the tar
- of those, **14,961** are in **neither the tar nor git** — **1.22 GB** of assets whose
  bytes exist only in the working tree
- **42 `.py` files** are hashed but not in the tar; **18** of those are also untracked in
  git. The tar holds only 20 `.py` files
- the tar is dominated by binaries that are trivially re-downloadable:
  6 `tessdata/*.traineddata` (~70 MB) + `sheet.csv` (21 MB) of its 261 MB extracted

**Verdict: not adequate to recover from a second incident.** It protects the
metrics/config layer (preds, metrics, manifests, engine_docs) and would let you rebuild
`benchmark/`. It would **not** let you restore the code that an incident actually breaks:
`level2/unified/run_bodhan.py` — the very file in the pre-image, the file that drifted —
is untracked in git (`??`) *and* absent from the tar. **Its pre-repair bytes are
unrecoverable.** The manifest stores a hash of content that no longer exists anywhere,
which is exactly the failure mode the pre-image was built to prevent.

**Biggest unprotected asset: `level2/benchmark/pages` — 599,788,380 bytes (600 MB),
1,194 scored GT page PNGs.** In neither the tar nor git. A1 mandated excluding it, so this
is a spec limitation rather than executor error, but it is the single largest thing a
second incident could take. Runner-up: `_archive/south_renders_shared_2026-09-30`,
570,147,487 bytes, 400 files — hashed by the manifest, never intended for the tar, and
also unbacked.

## Recommendation (no action taken)

Re-freeze `level2/unified/` and the `_archive/south_*` folders into a bundle, and
`git add` the currently-`??` scripts, or the next incident will not be recoverable.
