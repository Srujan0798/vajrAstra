# A6 — Transcript Recovery of `level2/benchmark/scores/` (proto-102 incident repair)

**Step:** A6 (EXECUTOR). **Date:** 2026-09-30. **Run at:** 18:05 IST.
**Law applied:** recover verbatim or say LOST. Never invent, never reconstruct, never "correct".
**Staging dir:** `docs/campaign/checkpoints/W4_reports/A6_staging/` (nothing written under `level2/`).

## Verdict summary

| class | count | files |
|---|---|---|
| RECOVERED (byte-exact) | **13** | `LEADERBOARD.md`, `mcnemar_summary.md`, `abstention_audit.md`, `FS-VERDICT-H48-001…010.md` |
| PARTIAL | **1** | `santa_method_cross_check.md` (143 of 173 lines) |
| LOST | **0** | — |
| REGENERATED-ELSEWHERE (not attempted) | **12** | `mcnemar_full_matrix.json` + 11 × `metrics_<engine>_normalized.json` |

No target came back LOST. One target is PARTIAL and is labelled PARTIAL in its own banner.

## Recovery table

`bytes` = size of the recovered body **after** stripping the one-line banner.
`nl` = whether the original file ended with a trailing newline (recovered faithfully).

| file | status | source (db part id) | bytes | nl | sha256 (body, first 16) | how we know it is complete |
|---|---|---|---|---|---|---|
| `LEADERBOARD.md` | **RECOVERED** | `prt_0f196d13c0013zLx9Wnyxyp337` (opencode `read`, 2026-09-30 14:43) | 12409 | no | `7ba692bf63e61855` | **Byte count equals the `ls -la` size measured at 09-30 03:40 (12409 B, mtime 2026-09-29T05:22:58.139320).** Read footer says `(End of file - total 181 lines)` and 181/181 lines were captured, sequence 1..181 unbroken. **Six independent full reads of this file (09-29 06:49 ×2, 09-29 07:30, 09-29 17:03, 09-29 18:57, 09-30 14:43) are byte-identical**, and a 7th partial read (lines 1–100, 09-30 03:41) matches the same first 100 lines. Last non-empty line: ``` `openbharatocr` ≡ `tesseract_indic` ≡ `tesseract_bilingual` byte-identical on 1257 packs (verified mcnemar_ful… ``` |
| `mcnemar_summary.md` | **RECOVERED** | `prt_0f196fd3d001KrxmjZEVrHpQW5` (opencode `read`, 2026-09-30 14:43) | 2874 | **yes** | `b761f232dba35574` | **Cryptographic proof.** The on-disk inventory taken 09-28 21:31 (`prt_0e8c05bdb0015jpnKRBO7FxekC`) records `mcnemar_summary.md  2874  b761f232dba35574`. Our recovered body is 2874 bytes with sha256 starting `b761f232dba35574` — an exact match on both size and the recorded 16-hex-char digest. Read footer `(End of file - total 56 lines)`, 56/56 lines captured. Corroborated by `ls -la` 2874 B at 09-30 03:40 (mtime 2026-09-28T21:31:54.912599). Last non-empty line: `Output: \`scores/mcnemar_full_matrix.json\` (raw) + \`scores/mcnemar_summary.md\` (this).` |
| `abstention_audit.md` | **RECOVERED** | `prt_0f196fd40001H00nJ35R0l7c4K` (opencode `read`, 2026-09-30 14:43) | 6683 | no | `eff28cf628b5bb0e` | **Byte count equals the on-disk size, measured 14 separate times** from 09-28 21:45 to 09-30 14:43 (all `6683`, mtime constant at 2026-09-28T21:36:32.577043), including `stat` at 09-29 17:28 (`6683 bytes, mtime 2026-09-28T21:36:32.577043`) and `ls` at 09-30 14:43. Read footer `(End of file - total 141 lines)`, 141/141 lines captured. A second full read at 09-28 22:09 (`prt_0e8e29e0b001yHNytXjXkWGxb8`) is the same 7407-char payload. Last non-empty line: `*Audit complete. Results logged to engine_health_log.jsonl.*` |
| `FS-VERDICT-H48-001.md` | **RECOVERED** | `prt_0eabf872e0013CEHhoqgGw2fTu` (bash `cat`, 2026-09-29 06:50) | 1470 | no | `ac507c85994ef00d` | Triple-sourced and all three agree byte-for-byte: (1) `cat FS-001 FS-010` — segment boundary proven by the next file's `# Fix Spec #10` heading starting immediately after (proves **no** trailing newline); (2) the 10-file loop `prt_0e9d0835c001s9bWoQ2bvveh5V` (18304 B) gives 1464 = content + 1 echo newline; (3) an independent `read` with no limit, `prt_0ef3a00e9001kBGggJvTkeO1jo` (09-30 03:42), footer `(End of file - total 46 lines)`, reconstructs to exactly 1470 bytes — byte-identical to (1) line-for-line. Last non-empty line: `§9 evidence law: every claim must be disk-verified. "ALL 11 ENGINES SCORED" is false per FINAL_VERDICT disk truth.` |
| `FS-VERDICT-H48-002.md` | **RECOVERED** | `prt_0eabfab24001ui2ztFv7aoajD6` (bash `cat`, 2026-09-29 06:50) | 1335 | no | `e2f2f9e3053c4ac7` | Two independent captures agree byte-for-byte. The capture loop is `echo "=========== $f ==========="; cat "$f"` — the marker is emitted **before** the `cat`, so each segment is the file's bytes with no added newline; the following segment's marker starts flush against this file's last character, proving no trailing newline. Second source is the 10-file loop `prt_0e9d0835c001s9bWoQ2bvveh5V` (1335 = 1334 + 1 echo newline). Last non-empty line: `§9 evidence law: engine status must match disk truth. "DONE 19:33" contradicts disk truth at time of CALL_PACKET…` |
| `FS-VERDICT-H48-003.md` | **RECOVERED** | `prt_0eabfab24001ui2ztFv7aoajD6` (bash `cat`, 2026-09-29 06:50) | 1283 | no | `7f3c181e4a494c83` | Same two-source byte agreement as 002. Last non-empty line: `§9 evidence law: engine queue status must match disk truth. "DONE" is false when engine is not even in queue.` |
| `FS-VERDICT-H48-004.md` | **RECOVERED** | `prt_0eabfab24001ui2ztFv7aoajD6` (bash `cat`, 2026-09-29 06:50) | 1286 | no | `1c41e3b41e0d77ac` | Same two-source byte agreement as 002. Last non-empty line: `§9 evidence law: counts must be exact. "6/10" is factually incorrect; actual is 9/9 local engines scored.` |
| `FS-VERDICT-H48-005.md` | **RECOVERED** | `prt_0eabfab24001ui2ztFv7aoajD6` (bash `cat`, 2026-09-29 06:50) | 1233 | no | `faffb548d455869f` | Same two-source byte agreement as 002. Last non-empty line: `§9 evidence law: status must match disk truth. "994/1227 running" is stale; actual is 1257 complete.` |
| `FS-VERDICT-H48-006.md` | **RECOVERED** | `prt_0eabfab2600194r2nAq2rKWRrW` (bash `cat`, 2026-09-29 06:50) | 3430 | no | `247b1ae3c4d52dbb` | Same two-source byte agreement as 002. Last non-empty line: `§9 evidence law: numerical claims must match disk-verified truth. "29/100" contradicts \`gt_forensics.json\` (45…` |
| `FS-VERDICT-H48-007.md` | **RECOVERED** | `prt_0eabfab2600194r2nAq2rKWRrW` (bash `cat`, 2026-09-29 06:50) | 1549 | no | `218ff27f468dfaf6` | Same two-source byte agreement as 002. Last non-empty line: `§9 evidence law: numerical claims must be exact. "10,434" contradicts arithmetic (10,432) and AGENT_PROTOCOL §…` |
| `FS-VERDICT-H48-008.md` | **RECOVERED** | `prt_0eabfab2600194r2nAq2rKWRrW` (bash `cat`, 2026-09-29 06:50) | 2203 | no | `a62f42d7cb2f5c92` | Same two-source byte agreement as 002. Last non-empty line: `§9 evidence law: external numbers require obituary citations (OBITUARIES.md). Transfer obituary law (§9.2) man…` |
| `FS-VERDICT-H48-009.md` | **RECOVERED** | `prt_0eabfab2600194r2nAq2rKWRrW` (bash `cat`, 2026-09-29 06:50) | 1509 | no | `81e1bc83b8e8aa51` | Same two-source byte agreement as 002. Last non-empty line: `§9 evidence law: labels must be accurate. "19/18" misrepresents the probe scope (18 languages, not 19).` |
| `FS-VERDICT-H48-010.md` | **RECOVERED** | `prt_0eabf872e0013CEHhoqgGw2fTu` (bash `cat`, 2026-09-29 06:50) | 2192 | no | `30b394caab10d5d3` | Second source is the 10-file loop `prt_0e9d0835c001s9bWoQ2bvveh5V` (2193 = 2192 + 1 echo newline). Last non-empty line: `§9 evidence law: uncertainty must be quantified, not hidden.` |
| `santa_method_cross_check.md` | **PARTIAL** | `prt_0e8cd58f7001DdwkYkrW3YzcOb` (bash `cat`, 2026-09-28 21:46), cross-checked against `prt_0ef39d98a001sbUvX40pFoAIfh` (`read` limit=60, 2026-09-30 03:42) | 5695 of 8113 | no | `8465dbf3fab6101f` | **NOT COMPLETE — 143 of 173 lines.** See the PARTIAL section below. Recovered prefix ends at `*Consensus: ≥2 reviewers*` (line 143). |

## The one PARTIAL file, in full

`santa_method_cross_check.md` — original on disk: **8113 bytes, 173 lines, mtime 2026-09-28 22:06**.

Timeline reconstructed from the db:

- 09-28 21:36 → 21:46: the audit body existed at **5695 bytes / 143 lines** (no trailing newline). This is the version captured whole by `cat` in `prt_0e8cd58f7001DdwkYkrW3YzcOb`.
- 09-28 22:05: a script appended a `## RESOLVED — 2026-09-28 22:08 IST (orchestrator-applied)` section (`prt_0e8df8162001SgDXNkQ2RuLMs5`, `content += resolved_section` — append only). Its own final `ls -la` line in the same capture reports `-rw-r--r--@ 1 srujansai staff 8113 Sep 28 22:06 … santa_method_cross_check.md`.
- The only later `read` of the final file is `prt_0ef39d98a001sbUvX40pFoAIfh` (09-30 03:42) and it was issued with `limit=60`, so it returns lines 1–60 of 173 and says so: `(Showing lines 1-60 of 173. Use offset=61 to continue.)`.

**Lines 144–173 (the whole RESOLVED section, ~2418 bytes) are LOST verbatim.** I am deliberately *not* writing them. The append script that generated them is preserved in `prt_0e8df8162001SgDXNkQ2RuLMs5` and is a usable *recipe*, but it contains a runtime interpolation — `{datetime.now().strftime('%Y-%m-%d %H:%M IST')}` — so replaying it would produce text that differs from the original in at least one byte. Reconstructing it would be fabrication, which this step forbids. The verifier may read the script and decide; that is a human call, not mine.

**Why the recovered 143 lines are safe to treat as the file's true opening:** (a) the append was `+=`, which cannot modify existing bytes; (b) lines 1–60 of the *final* 173-line file, from the independent 09-30 read, are **identical** to lines 1–60 of the recovered 21:46 `cat`; (c) a probe22-wide scan at 09-28 22:07 (`prt_0e8e133c6001TZ5QOmrBJ9IGQ6`) reports `newest_file=2026-09-28 22:06 (santa_method_cross_check.md)`, so nothing else wrote the file between the `cat` and the deletion.

## REGENERATED-ELSEWHERE — not attempted, per instruction

`mcnemar_full_matrix.json` and `metrics_<engine>_normalized.json` (11 engines) are rebuilt in step A5, so no recovery was attempted. Recorded for A5's benefit only:

- `mcnemar_full_matrix.json` = **154605 B** (09-28 22:00 §11 log; also 154605 B quoted in the 09-28 19:33 / 21:55 / 22:00 log entries). A generator `mcnemar_full_matrix.py` = 14266 B also existed. The only db capture is a `read` with `limit=30` (`prt_0ecc82f5b001xPaPoEWOR0FrrS`) — a fragment, not usable, and not used.
- `metrics_*_normalized.json` (11): rebuilt by `build_leaderboard.py` (16761–18830 B across three revisions) from `preds_*.json`.

## Exact searches run (so the next agent does not repeat them)

**Source 1 — OpenCode db** `~/.local/share/opencode/opencode.db`, opened strictly read-only via
`sqlite3 "file:$HOME/.local/share/opencode/opencode.db?mode=ro"` / `sqlite3.connect(..., uri=True)`.
**The db was never written to.** Note for the next agent: the file is 29.8 GB on disk but
`SELECT sum(length(data)) FROM part` is only **327,751,550 bytes** across 46,405 rows — the size is
free space, so a full `part` table scan takes ~3 s, not hours. Do not copy this db to /tmp.

1. `SELECT count(*) FROM part` → 46,401. `SELECT count(*), sum(length(data)) FROM part` → 46,405 / 327,751,550.
2. Broad net over `data LIKE` for `mcnemar_summary` / `abstention_audit` / `santa_method_cross_check` / `FS-VERDICT-H48-%` / `LEADERBOARD.md` → **1,468 parts**. Most are other files that merely *mention* the names.
3. `json_extract(data,'$.type')='tool' AND json_extract(data,'$.tool')='bash'` → **424** bash parts naming a target; filtered to those whose `input.command` mentions a target, then bucketed by whether the command truncates (`| head`, `| tail`, `sed -n`, `cut -c`, `head -N`).
4. `json_extract(data,'$.tool')='read'` **filtered on `state.input.filePath`** (not on file content — the content filter alone yields 596 false positives) → **78** reads, of which the target-path reads are 17 and only 4 are untruncated full-file reads.
5. Full inventory of every capture of every target, with part id, timestamp, byte length, and truncation flag — this is the table the verdict above is built from. Latest capture of anything before the 16:38 deletion: **09-30 14:43**.
6. Size/hash archaeology: every `part` output line matching a target filename together with a 3–6 digit number, to recover the on-disk byte sizes used as the completeness oracle. Also searched for any `sha256` inventory line naming a target (only one exists and it is from the superseded 09-28 21:31 state).

**Source 2 — Claude transcripts** `~/.claude/projects/-Users-srujansai-Desktop-South/*.jsonl` (14 files, one empty). Grepped for all target names. **Result: mentions only, no full file content.**
- `8e7ec69e-22b6-4702-a989-3397b9a99c1e.jsonl` (13.8 MB) has 12 matching lines, 48 `LEADERBOARD` hits.
- Parsed all `tool_result` blocks and classified by size/structure: the largest are `BOSS_CONCERNS.md` at line 3241 (45690 chars, a `cat -n` dump) and various grep/ls listings. The only `cat -n` dumps present are of `BOSS_CONCERNS.md`, not of any target.
- No `tool_use` block in any transcript has a `file_path` or command targeting `scores/LEADERBOARD.md`, `mcnemar_summary.md`, `abstention_audit.md`, `santa_method_cross_check.md` or any `FS-VERDICT-H48-*`.
- The only transcript commands touching these files are `python3 json.load` snippets against `mcnemar_full_matrix.json` (prints a few keys — a fragment) and a `find` sweep for the filenames. **Do not re-grep these; the answer is no.**

**Source 3 — `_archive/cleanup_2026-09-28/probe22_dups/`** — not needed. Every target was recovered from the db, so the last-resort archive was not consulted.

## Reproduce this result

```
sqlite3 "file:$HOME/.local/share/opencode/opencode.db?mode=ro" \
  "SELECT id, length(data) FROM part
   WHERE json_extract(data,'\$.tool')='read'
     AND json_extract(data,'\$.state.input.filePath') LIKE '%scores/LEADERBOARD%'
     AND json_extract(data,'\$.state.input.limit') IS NULL
     AND json_extract(data,'\$.state.input.offset') IS NULL;"
```

→ `prt_0f196d13c0013zLx9Wnyxyp337|13354`-class rows; the 12409-byte body is the payload with the
`N: ` line-number prefixes and the `<path>/<type>/<content>` wrapper removed.

Verify what was written (banner stripped, then hashed):

```
cd docs/campaign/checkpoints/W4_reports/A6_staging
for f in *.md; do python3 -c "
import hashlib,sys
b=open('$f','rb').read().partition(b'\n')[2]
print('$f', len(b), hashlib.sha256(b).hexdigest())"; done
```

## Handling notes for the verifier

- The one-line `<!-- RECOVERED … -->` / `<!-- PARTIAL … -->` banner is the **only** addition to each file. No line inside any recovered body was edited, re-wrapped, re-indented or "corrected". Bodies are byte-identical to the source capture.
- Trailing-newline presence was a real finding and is preserved per file: `mcnemar_summary.md` **has** one (2874 B on disk = 2873 + `\n`); `LEADERBOARD.md`, `abstention_audit.md` and all ten `FS-VERDICT-H48-*` files **do not**. The ten fix-specs are mutually consistent on this across three independent captures.
- These are recovered *copies for the record*. They are **not** a substitute for putting the files back in `level2/benchmark/scores/` — that is a separate, gated move and A6 did not make it.
