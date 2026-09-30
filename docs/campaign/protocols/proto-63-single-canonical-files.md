---
name: proto-63-single-canonical-files
description: "Added 2026-09-30 — one canonical copy per document; resolves the two meeting packets, the docs/research copies of uni and the meeting file, the 3 W5_BEAT_SARVAM_PLAN copies; pointer-line method, no raw deletes"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:44:19.647Z
---

# PROTO-63 — SINGLE CANONICAL FILES (Miss applies, Verdict verifies)
> **2026-09-30 evening:** where this protocol differs from [[proto-98-clean-repo-master]] (official tree, `docs/sources/`, topic finals, WORTH score), proto-98 wins.

**Why:** duplicates drift, and the boss (CO-004, CO-010) forbids "misleading parallel versions". Monitor found (2026-09-30 03:25):
| Document | Copies | Canonical (proposed) | Others become |
|---|---|---|---|
| Meeting packet | root `VINAY_MEETING_PACKET.md` (30.9 KB, corrected 09-30 01:33) · `docs/architecture/VINAY_MEETING_PACKET.md` (6.7 KB, Verdict edition, stale "tomorrow") | root (the corrected one) — until `DRAFT_RESEARCH_PLAN.md` exists, then that is the presented doc | architecture copy → archive to `_archive/pre_fix_2026-09-29/` + pointer file |
| uni v3 | `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt` · `docs/research/uni_v3_ORIGINAL_2026-09-29.md` | `_archive/directives/…txt` (superseded law) | docs/research copy → 3-line pointer |
| Meeting 2026-09-29 | `_reports/research/MEETING_2026-09-29_STRUCTURED.md` · `docs/research/MEETING_2026-09-29_STRUCTURED.md` (identical, 17,876 B) | `docs/research/` (agents read there) | `_reports` copy → pointer |
| W5 beat-Sarvam plan | root · `docs/architecture/` · `docs/research/level7/` (+ `_archive/root_md_dedupe_2026-09-29/`) | decided in [[proto-50-w5-repo-map-and-drift]] Part B | — |
| LIVE_LATEST 2026-09-29 | root · `docs/research/` | `docs/research/` | root → pointer (after meeting) |

**State 2026-09-30 ~15:30 (measured):** the `docs/research/` copies of uni and LIVE_LATEST no longer exist (uni copy now in `_archive/cleanup_2026-09-30/single_file_dups/`); `_reports/research/` has no meeting copy — only `docs/research/MEETING_2026-09-29_STRUCTURED.md` remains. Still open: `AGENTS.md` KEY FILES points at both missing paths (fix-spec in proto-95 Step 2). Pointer stubs: only when the referrer cannot be edited (a locked file); otherwise update the referrer (proto-95 Step 4.5) — stub files are junk. Archive copies go into one bundle ([[proto-96-archive-reports-compaction]]), not per-file folders.

## Method (never raw delete)
1. `cmp` / `diff` the copies; if they differ, Verdict decides which content wins and whether anything from the loser must be merged first (fix-spec).
2. Archive the loser to `_archive/dedupe_2026-09-30/<original path with / → __>` and record sha256.
3. Replace the loser with a pointer file: `# MOVED — canonical copy: <path>` + date + reason (so old links still resolve).
4. Log each in `DISPATCH_LOG.md`. Verdict re-runs `cmp`/`ls` to confirm.

**Timing:** the meeting-packet row is meeting-critical (do it in [[proto-64-meeting-day-finish]]); the rest after the meeting. Check the OpenCode cleanup agent is idle first (proto-60 Rule 3).

Related: [[proto-50-w5-repo-map-and-drift]], [[proto-60-monitor-and-checkpoint-discipline]]
