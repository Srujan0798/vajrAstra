# A1 — Incident Pre-Image (proto-102)

**Role:** EXECUTOR (A1). A different blind agent verifies.
**Repo:** `/Users/srujansai/Desktop/South`
**Run date:** 2026-09-30, 17:00–17:02 IST
**Verdict:** **PASS** — bundle round-trips at 207/207 = 100.00%. One manifest staleness event recorded in (f), caused by a concurrent writer, not by a hashing error.

---

## Artifacts written (only these three)

| Path | Bytes | Notes |
|---|---|---|
| `docs/campaign/audit/incident_pre_repair.sha256` | 2,247,145 | 19,202 lines, `<sha256>␠␠<relpath>`, sorted by path |
| `_archive/bundles/2026-09-30_incident_pre_repair.tar.gz` | 151,599,725 | 230 entries |
| `docs/campaign/checkpoints/W4_reports/A1_preimage.md` | this file | report |

Nothing was moved, deleted, or modified. No commit. No `2>/dev/null` on any mutating command.

---

## (a) Files hashed + per-folder breakdown

**Total regular files hashed: 19,202**

| Root | Files hashed |
|---|---|
| `level2/` | 18,791 |
| `_archive/south_pages_400_symlinks_2026-09-30/` | 2 |
| `_archive/south_renders_shared_2026-09-30/` | 400 |
| `_archive/south_unified_symlinks_2026-09-30/` | 9 |
| **Total** | **19,202** |

Walk used `python3` stdlib (`os.walk(followlinks=False)`, 1 MiB chunks, `hashlib.sha256`). Read errors: **0**. Non-regular files skipped: **0**.

**Pasteable check lines**
```
wc -l < docs/campaign/audit/incident_pre_repair.sha256
# expect: 19202
awk '{p=$2; if (p ~ /^_archive\//) {split(p,a,"/"); print a[1]"/"a[2]} else print "level2/"}' \
    docs/campaign/audit/incident_pre_repair.sha256 | sort | uniq -c
# expect:  18791 level2/
#           400 _archive/south_renders_shared_2026-09-30
#             9 _archive/south_unified_symlinks_2026-09-30
#             2 _archive/south_pages_400_symlinks_2026-09-30
stat -f '%z' docs/campaign/audit/incident_pre_repair.sha256
# expect: 2247145
```

**Hashing policy (stated, not hidden).** The manifest carries `<sha256>  <path>` for every **regular file**. Symlinks and directories are **not** emitted, deliberately, so that `shasum -a 256 -c` stays clean and machine-checkable. No bytes are lost by this:
- every **live** symlink's target bytes are hashed at the symlink's **real path**, which lies inside a covered root (4,000/4,000 confirmed in-root below);
- every **broken** symlink has no bytes to hash at all — it is the incident itself (see (f)).

| Tree | Symlinks | Broken | Live w/ target inside a covered root |
|---|---|---|---|
| `level2/` | 330 | 0 | 0 (point into sealed `Datasets/`, out of scope) |
| `_archive/south_pages_400_symlinks_2026-09-30/` | 400 | **400** | 0 |
| `_archive/south_renders_shared_2026-09-30/` | 0 | 0 | — |
| `_archive/south_unified_symlinks_2026-09-30/` | 17,289 | **13,289** | 4,000 |
| **Total** | **18,019** | **13,689** | 4,000 |

## (b) Bundle bytes + entry count

```
tar -czf _archive/bundles/2026-09-30_incident_pre_repair.tar.gz \
  --exclude='level2/benchmark/pages' --exclude='level2/benchmark/packs' \
  level2/benchmark level2/engine_docs
```

- **Byte size: 151,599,725** (144.5 MiB)
- **Entry count: 230** = 207 regular files + 23 directory entries
- 207 = 177 (`level2/benchmark` minus the two excluded trees) + 30 (`level2/engine_docs`, 10 engines x 3 files)
- Symlinks inside the bundle: **0** (the only 330 symlinks under the payload live in `pages/`, which is excluded)
- Excludes confirmed effective: `tar -tzf … | grep -c '^level2/benchmark/pages/'` → `0`; same for `packs/` → `0`

**Pasteable check lines**
```
stat -f '%z' _archive/bundles/2026-09-30_incident_pre_repair.tar.gz
# expect: 151599725
tar -tzf _archive/bundles/2026-09-30_incident_pre_repair.tar.gz | wc -l
# expect: 230
```

## (c) Verification by extraction — match percentage

Extracted to scratch **outside the repo**: `/var/folders/…/T/opencode/a1_verify` (261 MB, 207 regular files, 0 symlinks, exit 0).
For every manifest entry under `level2/benchmark` / `level2/engine_docs`, minus the two tar-excluded trees, the extracted copy was re-hashed and compared to the manifest sha256.

**Result: 207/207 = 100.00%** — mismatches: 0, missing from extraction: 0.

Denominator 207 exactly equals the extracted regular-file count, so nothing was silently skipped.

**Pasteable check line**
```
207/207 = 100%   # match with its denominator: 207 files in bundle scope, 0 mismatch, 0 missing
```

## (d) Tarball sha256

```
ac9af7e5df989b109baaeb065f3b6d52f1776c3eeca5c0e418df27e481c08444  _archive/bundles/2026-09-30_incident_pre_repair.tar.gz
```

**Pasteable check line**
```
shasum -a 256 _archive/bundles/2026-09-30_incident_pre_repair.tar.gz
# expect: ac9af7e5df989b109baaeb065f3b6d52f1776c3eeca5c0e418df27e481c08444
```

## (e) Exit codes

| Command | Exit code |
|---|---|
| `tar -czf …` (create) | **0** (clean stderr) |
| `tar -tzf …` (list / corruption check) | **0** |
| `tar -xzf … -C $SCRATCH` (extract) | **0** |
| extract-and-rehash verification | **0** (207/207) |

## (f) FAILURES AND GAPS — stated plainly

**1. `shasum -a 256 -c` on the manifest exits 1: 19,201 OK / 1 FAILED.**
```
level2/unified/run_bodhan.py: FAILED
shasum: WARNING: 1 computed checksum did NOT match
```
Cause, measured not guessed: the manifest snapshot was taken at **17:00:46**. `level2/unified/run_bodhan.py` was then rewritten by a concurrent process **at least twice**, so the recorded hash is stale:

| when | sha256 | size |
|---|---|---|
| 17:00:46 (manifest snapshot) | `7e4f315a105ea45ca39a582aea6ca36497e3ca8e67d160b3c03cc26525bb98b9` | — |
| 17:01:15 | `ac0195c11ac2ae1f1bc7458cef4617d7983d5e25398603c6a300756efef99710` | 10,555 B |
| 17:03:19 | `803107d65d96da349038a37f2ade60b91e9a66a95980a0bc7bafd288572275e7` | 10,680 B |

Three distinct states, so this is a file under **active edit by another agent**, not a hashing error on my part. The same window shows `DISPATCH_LOG.md` (16:58:26) and `docs/campaign/checkpoints/W3_reports/inventory.md` (17:02:54) being written by other sessions — the repo has concurrent writers, which is the root condition. `level2/unified/` is **not** in the tar payload, so (c) at 100.00% is unaffected.

The manifest was deliberately **left unmodified**: it is a point-in-time pre-image, and rewriting a line to chase a live writer would corrupt the evidence. **Caveat for the verifier:** any future `shasum -a 256 -c` over the whole manifest will re-report this file for as long as it keeps changing. The 19,201 static entries are the trustworthy part.

**2. 13,689 broken symlinks have no recoverable content — this is the incident, and no manifest can capture it.** Two trees are gone:
- `level2/renders_shared/` — **absent**; all 400 symlinks in `_archive/south_pages_400_symlinks_2026-09-30/` dangle.
- `level2/probe22/out/` — **absent**; 13,289 of 17,289 symlinks in `_archive/south_unified_symlinks_2026-09-30/` dangle (e.g. `…/probe22/out/rapidocr/sd/*`).

The surviving payloads are `level2/benchmark/**` and `level2/engine_docs/**` (now in the bundle) and the 400 real PNGs in `_archive/south_renders_shared_2026-09-30/` (545 MB, hashed, **not** in the bundle — bundle scope was fixed by the task). That 545 MB set is the highest-value un-backed-up data on disk and has **no tarball**; recommend a follow-up bundle for it.

**3. Out-of-scope by design:** 330 live symlinks in `level2/benchmark/pages/` point into the sealed `Datasets/` tree (100 Sanskrit, 100 Hindi, 100 Bengali, 30 English). `Datasets/` is sealed and outside the requested roots, so its bytes are not in the manifest. `pages/` is also tar-excluded, so those 330 links are not in the bundle either.

**4. Not captured:** directory entries (no bytes to hash; file paths are recorded) and symlink target strings. Restore from this manifest therefore recreates *file contents*, not the symlink topology. Given 13,689 of 18,019 symlinks are already dead, topology loss is a lower-order problem than content loss, but it is a real gap.
