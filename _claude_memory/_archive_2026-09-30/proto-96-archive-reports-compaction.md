---
name: proto-96-archive-reports-compaction
description: "Added 2026-09-30 (boss: 'after all these I need those archive and reports also to compact, merge them … I am seeing bunch of junk') — runs after proto-95: _archive/ (519 files, ~215 MB, 0 in git) + _reports/ (58 files, 0 in git) become ONE _archive/INDEX.md (a line per original + a ≤5-line digest per bundle) + ≤7 verified .tar.gz bundles + _archive/directives/; delete only exact twins / conversions / git-held / empties (U29); Miss executes, Verdict verifies"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T10:07:50.681Z
---

# PROTO-96 — ARCHIVE + REPORTS COMPACTION (W4 part 2; starts only after [[proto-95-research-harvest-decisions]] is VERIFIED)

**Boss, 2026-09-30:** "after all these I need those archive and reports also to compact, merge them and make some low variants … I am seeing bunch of junk."
Concerns: HC14.9 (archive INDEX, one line per item), HL4 (archive-never-delete; narrowed by U29), CO-002, CO-066, H3 ([[proto-99-concern-crosswalk]] §H).
**The "low variant":** each bundle gets a digest of 5 lines or fewer in `_archive/INDEX.md`, so nobody has to open a bundle to learn what is inside.

## Measured 2026-09-30 ~15:30 IST (re-count in Step 1)
- `_archive/` holds 519 files and `_reports/` holds 58. **0 of them are tracked in git.**
  - So a delete here is permanent. Only a file with an exact twin somewhere else may be deleted.
- Repo-wide there are 69 exact-duplicate md/txt groups (71 redundant copies). Almost all are `_archive/` copies of live files.

| Folder | Files · size | What it is | Fate rule → bundle |
|---|---|---|---|
| `_archive/campaign_drafts_2026-09-30` | 73 · 0.9 MB | protocol copies + W1 papers. **61 are sha-identical to a live file**; 12 have no live twin | DELETE-DUP the 61; the 12 → `2026-09-30_prefix_and_drafts` |
| `_archive/cleanup_2026-09-28` | 335 · ~215 MB | `AUDIT_*.md`, `audit_intermediates/*.txt`, and 45 probe JSONs (194 MB) in `probe22_dups/` + `audit_safety_backup/`. Of those 45: 9 identical to the same-named live file, 20 differ, 16 have no same-named live file | match by sha256 across the whole repo, not by name: twins → DELETE-DUP; the rest → `2026-09-28_cleanup` (JSON compresses well) |
| `_archive/.audit_2026-09-29` (hidden) | 18 · 0.6 MB | subagent audit reports, `sizes_all.txt` | → `2026-09-29_audit` |
| `_archive/cleanup_2026-09-29` | 13 · 68 KB | dead code (`level2_dead_code/*.py`, `src_skeletons/`) | exact blob in git history → DELETE-GIT; else → `2026-09-29_audit` |
| `_archive/root_md_dedupe_2026-09-29` | 1 · 16 KB | `W5_BEAT_SARVAM_PLAN.md` | twin → DELETE-DUP; else → `2026-09-29_audit` |
| `_archive/cleanup_2026-09-30` | 50 · 0.3 MB | `renames/`, `single_file_dups/` (incl. a uni md copy), `dedup_topic_superseded/` | twins → DELETE-DUP; rest → `2026-09-30_prefix_and_drafts` |
| `_archive/pre_fix_2026-09-30` + `_consolidated` | 6 + 21 · 0.5 MB | pre-images of the proto-18/86 fixes (W1 VERIFIED) | → `2026-09-30_prefix_and_drafts` (audit trail) |
| `_archive/directives` | 2 · 80 KB | uni v3 original (.txt) + CAMPAIGN_DIRECTIVE v4 | **KEEP as plain files.** AGENTS.md and the v5 directive cite them, and the boss opens the uni |
| `_reports/cleanup_cycle1/2/3` (+ empty `cycle4/`) | 48 · 0.7 MB | reports about earlier cleanups | → `2026-09-30_cleanup_reports`; delete the empty dir |
| `_reports/analysis` | 5 · 84 KB | DUPLICATE_MAP, FILE_INVENTORY, MEMORY_CONSOLIDATION, MD_CONSOLIDATION_PLAN, MEMORY_FINAL | → `2026-09-30_cleanup_reports` (proto-95 already took their decisions) |
| `_reports/research` | 5 · 116 KB | proto-95 G7 | as proto-95 ruled |
| `docs/campaign/checkpoints/W1_reports`, `W2_reports` | 11 · ~0.3 MB | proto-95 G8 | as proto-95 ruled |

**Out of scope:**
- `.kilo/worktrees` (56 md; another tool's git worktree). [[proto-74-root-hidden-hygiene]] / [[proto-76-workstreams-and-agent-health]] decide: `git worktree list`, remove if stale.
- Sealed `level2/reports`, `level2/out` and `level2/probe22/out`; also `Datasets/` and `arc_level_1/`.
- The Gemma HF cache (the boss keeps it).
- **Primary sources:** `_archive/cleanup_2026-09-28/root_clutter/sync - ocr - September 10.docx` and `Untitled-1.ini` are NOT archive material. [[proto-98-clean-repo-master]] Phase 1 moves them to `docs/sources/` before any bundling; if they are still here, STOP and move them first.

## Target end state
```
_archive/
  INDEX.md      one line per original + a digest (≤5 lines) per bundle
  directives/   unchanged (2 files)
  bundles/      ≤ 7 × .tar.gz:
                  2026-09-30_pre_cleanup_snapshot  (proto-98 Phase 0 global pre-image)
                  2026-09-28_cleanup
                  2026-09-29_audit
                  2026-09-30_prefix_and_drafts
                  2026-09-30_cleanup_reports   (all of _reports)
                  2026-09-30_research_harvest  (from proto-95)
                  2026-09-30_research_pre_harvest
                    (proto-95 snapshot; drop it only if Verdict shows the harvest bundle + git hold every file it covers)
_reports/       gone
```
- Nothing new at the repo root.
- No new report files except `_archive/INDEX.md` and one `DISPATCH_LOG.md` entry. Writing reports about each cleanup is how the junk grew.
- INDEX line format:
  `| bundle or DELETED-DUP/-CONV/-GIT/-EMPTY | original path | sha256[:16] | bytes | fate | why (≤12 words) | live successor or — |`

## Deletion rule (U29, decided by the boss 2026-09-30)
Delete only these four kinds of file:
1. sha256-identical twins of a file that stays.
2. Pure format conversions whose source stays.
3. Files whose exact blob is in git history. Check it: `git hash-object <file>` must equal the blob at the original path in some commit (`git rev-list --all -- <path>`, then `git ls-tree <commit> <path>`).
4. Empty files and empty dirs.
5. OS metadata junk (`.DS_Store`); also add it to `.gitignore`.

Everything else goes into a bundle. Nothing is deleted without an INDEX line.

## Steps
0. **Pre-flight.**
   - proto-95 must be VERIFIED; its fates decide `_reports/research` and the W1/W2 papers.
   - Run the [[proto-02-preflight-and-checkpoints]] checks. No agent may be writing under `_archive/` or `_reports/`.
   - Check free disk: bundling ~215 MB needs ~300 MB of temp space.
   - Set W4.md `STATUS: proto-96 STARTED`.
1. **Inventory** (Miss). Reuse `scripts/research_inventory.py` with `--root _archive --root _reports`, or write a sibling script.
   - For each file record: path, bytes, sha256.
   - `live_twin`: a path outside `_archive/` and `_reports/` with the same sha256, searched repo-wide. Compare the probe JSONs against `level2/` read-only.
   - `git_twin`: yes/no per rule 3.
   - Output: `docs/campaign/audit/archive_inventory.tsv`. Totals must equal `find _archive _reports -type f | wc -l`.
2. **Fates** (Verdict).
   - Apply the deletion rule mechanically; assign every other file to a bundle by the table.
   - grep all live md/py/yaml for references into `_archive/` and `_reports/`. A referenced file stays citable: update the referrer to `<bundle>:<path>`. If the file is actually live (a report a protocol still uses), move it to its live home under `docs/`.
   - Write the fate column into the TSV.
3. **Build bundles** (Miss). For each bundle:
   - Run `tar -czf _archive/bundles/<name>.tar.gz --null -T <list>`.
   - `tar -tzf <bundle> | wc -l` must equal the length of the list.
   - Extract it into the session scratch dir. Every sha256 must match the TSV (100%); otherwise stop and report.
4. **Remove** (Miss). Never `rm -rf` anything until step 3 has passed for its bundle.
   - First the DELETE rows. Re-check the twin or git match immediately before each `rm`.
   - Then the bundled originals.
   - Then run `find _archive _reports -type d -empty -delete`.
5. **Write `_archive/INDEX.md`.** Every line, plus for each bundle: "Holds / Why kept / Still cited by / Digest (≤ 5 lines)".
   - The `DISPATCH_LOG.md` entry records files before → after, MB before → after, and the bundle list with sha256.
6. **Verify** (Verdict). Check that:
   - before-count = deleted + bundled + kept, exactly;
   - every INDEX line resolves (`tar -tzf` finds it, or it is DELETED and its twin is present);
   - no live reference points at a removed path;
   - `_reports/` is gone;
   - `git status` shows nothing changed in sealed dirs.
   - Then give the boss 3 lines: files, MB and bundles, before → after.

**Done when:** W4.md says `proto-96 VERIFIED`, with the commands above.

**Skills:** ECC `terminal-ops` (tar and sha work) · `verification-loop` · `ssotize` (the few live-home moves) · `graphify --update` afterwards (`_archive` leaves the graph).

**Traps:**
- macOS `tar` is bsdtar. Use `--null -T`, because names contain spaces (`FULL TECHNICAL BRIEFING.md`, `OCR_AGENT_MEMORY_FEED copy.md`).
- On the Mac the checksum command is `shasum -a 256`, not `sha256sum`.
- Bundles stay untracked, like today's `_archive/`. Committing them to git is the boss's call; ask only if they want a copy off the laptop.

Related: [[proto-95-research-harvest-decisions]], [[proto-72-per-file-audit]], [[proto-74-root-hidden-hygiene]], [[proto-63-single-canonical-files]], [[proto-92-boss-decisions]]
