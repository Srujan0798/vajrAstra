# A4-EXECLOG: true status of every dispatched step, and why execution stalls

Sources read in full: `docs/campaign/checkpoints/W4.md` (840 lines), `DISPATCH_LOG.md` (780 lines), `docs/campaign/checkpoints/NEXT.md` (REV 6/7/8). Spot checks: `docs/campaign/checkpoints/W4_reports/blind_verify_*.md`, `docs/campaign/protocols/proto-104/-107/-108`.
Snapshot caveat: the repo copy has text only. Data, weights, `level2/benchmark/**`, and `docs/campaign/gold/` are absent here, so "VERIFIED" below means a blind-verifier report or pasted command output exists in the text. It does not mean I re-ran it.
Timestamps: W4/DISPATCH mix IST and UTC (`...Z` log lines are UTC, so 10:52Z = 16:22 IST). The last timestamped log entry is `GOLD W0 END` at 2026-10-01T10:52:12Z (`DISPATCH_LOG.md:779`). NEXT.md REV 8 is the newest text, written the same day by the cloud planner.

Tags: VERIFIED-DONE (output or blind verifier on text) · CLAIMED-ONLY · STALLED · NEVER STARTED.

## proto-102 (incident repair), Agent 2
- A0 STOP: VERIFIED-DONE. Command output pasted (`W4.md` ~l.250), 2026-09-30 16:58 IST.
- A1 pre-image: VERIFIED on its claims (207/207, sha256 `ac9af7e5…`, blind verifier `W4_reports/A1_verify.md`) but FAILED on adequacy. 0 of 411 `_archive/south_*` entries and 14,961 files (1.22 GB) were in neither tar nor git. Pages were bundled afterwards (577 MB, 1,194 PNGs). The 400 South v1 renders (545 MB, the only copy) are still never tarred. 17:2x IST.
- A2 restore: VERIFIED-DONE. sha256 MATCH on 3 files (`W4.md:309`), 17:2x IST.
- A3 layout: VERIFIED-DONE. Blind report `A3A4_verify.md`; packs 13,289 = 13,289 (`W4.md:334`).
- A4 paths: CLAIMED-ONLY, in conflict with itself. `W4.md:348` says CONDITIONAL, smoke BLOCKED. `W4.md:506/528/530` then say "A4 PASS" at 02:15 and 02:45, while the same text admits the smoke gate fails (`ModuleNotFoundError: surya`). The protocol's own rule (R-3) is "0 old-path hits AND smoke passes". The rewrite is verified (0 grep hits, py_compile green). The smoke is not. DISPATCH §25 (Agent 2) still says CONDITIONAL. NEXT REV 6 reports "A4 = PASS 02:15" and tells the next agent to re-verify the H-1 proof, which leaves the next agent unsure whether A4 is closed.
- A5 regenerate: STALLED. Normalized metrics were copied from the archive (not regenerated). `mcnemar_full_matrix.json` timed out at 6 min and was "restarted in the background"; it is still "in background" at `W4.md:757` and §26. Nothing shows it finished. Last touched 2026-10-01.
- A6 recover docs: CLAIMED-ONLY (partial). 13 files were recovered from the OpenCode DB into `W4_reports/A6_staging/` only. They were not restored to `scores/`. `santa_method_cross_check.md` is PARTIAL (143/173 lines). `mcnemar_full_matrix.json` is not recovered. The earlier "A6 PASS" paste was FALSE (state correction, 17:15 IST 09-30). The 10-01 "A6 PASS" has no blind verifier.
- A7 (destructive clean): NEVER STARTED, parked by the boss, gated on a "go". A8, A9: NEVER STARTED (`W4.md:285`; the A9 blind verify never ran). A10: not a protocol step (`DISPATCH_LOG.md:445`); proto-104 parks A6/A7/A8/A10.
- LAYOUT FROZEN: posted 2026-10-01 (`W4.md:589`). It freezes mv/rm under `level2/` until S6, which has never started, so the freeze has no end date.

## proto-104 (project-first path) — R, S, H, D, X, C, G, Q, GPU
- R (A4, A5, gitignore of `models_bodhan/`, move strays): CLAIMED-ONLY / STALLED (A4 and A5 above). No evidence of the stray moves or the gitignore.
- S1 South feasibility: VERIFIED-DONE by pasted output (179 PDFs, 23,001 pages, 0 clean). Agent 3, 2026-09-30 (log 15:16Z). The proto-101 P1 Verdict re-check never ran, because P0 never started.
- S2 draw and render: VERIFIED-DONE for the 400 manifest items (`blind_verify_S5` read 100 packs per language). Evidence conflicts: one entry says 400 images, a later one says "800 images, 200 per language" (`W4.md:715`), so the on-disk image count is unverified. No S3 section shows "10 per language viewed". The "Agent 2 verified" line is a restatement, not an S3 report.
- S3 Agent 2 verify: CLAIMED-ONLY.
- S4 local engines on South: VERIFIED-DONE for tesseract_indic, openbharatocr (alias), easyocr te/kn, rapidocr, doctr, anuvaad_tesseract, 2026-09-30 evening to 10-01 (`blind_verify_S5.md` PASS 7/7 against pack JSONs). STALLED: surya (not installed), paddleocr_indic, indicphotoocr, easyocr ta (broken checkpoint) and ml (checkpoint not cached). Runs went through a new `run_engines_south.py`, not the locked `run_probe.py`.
- S4 Sarvam 12 calls: STALLED / FAILED. ₹6 spent and 12 jobs "completed", but predictions were never retrieved (`pred_sample` is empty for all 12). Download returned 403 `invalid_api_key_error`, then fresh calls returned 401 (`DISPATCH_LOG.md:757,761`). No South Sarvam number exists.
- S5 tiered scoring: VERIFIED-DONE (7/7). `BENCHMARK_22` was not regenerated. Bodhan is scored on the pair set only.
- S6 retire v1: NEVER STARTED.
- H1 test-set profile: PARTIAL. The vision check covered 13 images, all Bengali handwritten (`W4.md:427`). The plan (HW-ID) asks for at least 300 (NEXT REV 8 counts 16/5,344 viewed). Image IDs are listed but I cannot confirm the viewing. The old "35.7% Devanagari" claim is retracted. The H2 section still contains the garbled line "Tesseract on 70 samples reads 13/13 as Bengali" (`W4.md:777+`).
- H2 labelled slice: VERIFIED-DONE (`blind_verify_H2` PASS on 4 checks, path-level leak only), but it is the wrong target. It is Gujarati (Bodo/gu, 16,490 items) and only 4,645 of about 116k images are on disk. The official test set is Bengali handwriting.
- H3 handwriting baseline: NEVER STARTED. `H3 REVERSED, previous entry was unauthorized` (`DISPATCH_LOG.md:777`).
- H4 handwriting LoRA: NEVER STARTED (gated on Gate 2.5).
- D1 Bodhan: PARTIAL, CONDITIONAL PASS. Downloads 5.35 GB and Gate 1 numbers (pair 0.4034 4-bit / 0.4010 bf16; bench small_rep 0.0540) are verified by the S5 and gate1 verifiers. The official PyTorch path is BLOCKED (vendor code asserts CUDA). Time to unblock: HF gating (boss clicked "agree" around 21:00 IST 09-30, about 4 h after the 16:35 block).
- D2, D3, D5: NEVER STARTED. D4: only the product skeleton exists (see P below).
- P product layer (Agent 3): CLAIMED/DONE. Requirements, Dockerfile, B21 spec, and a 6-page Tesseract dry run exist as pasted output. Bodhan is a stub. The "50-image dry run on handwriting" is NOT done.
- X external bench (6,909 items): PREP only. `run_bench_x.py` dry run on 5 items. The full run is NEVER STARTED. It loads 8,082 items, which does not match the 6,909 test split in the plan.
- C consensus (proto-105): CLAIMED-ONLY. Row counts conflict: "20 RF rows", "13 new rows RF-21..37", "50 RF rows". No verifier.
- G Plan v3 draft: DONE on paper, now superseded by Plan v4 (proto-108). Gate 2.5 (multi-LLM check plus Vinay session) was never run for v3 or v4.
- Q `GT_DEFECTS.md`: NEVER STARTED (file absent).
- GPU: NEVER STARTED (no SSH details; NEXT blocker 3).

## proto-107 (gold repo), Agent 3
- W0: CONDITIONAL PASS. Agent 3 reports 1,277-entry manifest, 172 MB bundle, 2026-10-01 10:48 to 10:52Z. The planner's disk-verify (`W4.md:833`) found 85 pyc/`__pycache__` lines (protocol exclude violated). Agent 2's verification was never posted. W1 is "blocked until clean PASS or boss go".
- W1 to W9: NEVER STARTED. W5 needs boss GO-A/GO-D/GO-G; W6 is closed. `docs/campaign/gold/` is absent in this snapshot.

## proto-108 Plan v4 (HW0/HW1/P1/R1/E1) and HW-ID/G-2.5/HW2
- HW-ID (≥300 crops viewed), HW0 leak gate, HW1 zero-shot baselines, G-2.5, HW2, P1, R1, E1, PITCH: all NEVER STARTED. The plan was written 2026-10-01 (rev 2 mtime 12:11) and NEXT REV 8 itself states 0 models trained, 0 baselines, 0 Bengali HW data on disk, and "no agent results synced since the push". The paste lines for Agents 1, 2, 3 were issued but there is no log line showing any of them started. Agent 1 logged IDLE (`DISPATCH_LOG.md:775`) and Agent 3 logged "STOP, idle, awaiting planner" three times.

Earlier waves (1A to 1H, Wave 2 sampling, proto-86): DONE with verifiers. They are all research and documents, not product.

## Why execution stalls: root causes, with evidence
1. Waiting on the boss (largest single cause). Open gates: HF gating (blocked D1 for about 4.5 h), Sarvam key dead, U10 (locked `run_probe.py`), U9/U24 (S2 "PAUSED, STOPPED for boss", `W4.md:366`), U-HW1 and U-HW2 downloads, Vinay OK (G-2.5), GPU SSH, A7 "go", proto-107 GO-A/D/G, 1F ChatGPT paste (open since 09-29). NEXT REV 6's "WAITING ON THE BOSS" lists eight. Almost every step that moves toward a model sits behind one of them.
2. Self-inflicted incident consumed the lane. Agent 3's P2/P4 (11:06 to 11:08Z) moved `probe22` to `benchmark`, deleted `scores/`, and mis-nested packs. P0 was marked "DONE (deferred)" with no pre-image. Agent 2 then spent proto-102 A0 to A6 (about 17:00 IST 09-30 to 10-01) repairing that, while the target (handwriting) went unstarted. A second writer (`run_bodhan.py` rewritten 17:01 and 17:03) repeated the same failure mode during the repair.
3. Locked files and freezes block the verification path. `run_probe.py` is LOCKED, which is why the A4 smoke cannot pass without U10. LAYOUT FROZEN until S6, and S6 waits on a guard. A7 is parked. Protocol-101 and -98 gates (P0, inventories) sat unmet and froze the Phase 2 and B-17 work.
4. Claims without evidence, then reversals. A6 "PASS" paste was false (17:15 09-30). A4 "PASS" sits beside "smoke BLOCKED". A5 "no regeneration needed". The concern register had 35 bare `DONE` and 1 `DONE-VERIFIED` (`PROTO66_VERDICT_CHECK`). "All 22 langs ≥100" had to be struck. The "35.7% Devanagari" test-set claim was wrong. The orchestrator's "All technically feasible work is complete" (`DISPATCH_LOG.md:641`) was written while no model, baseline, or handwriting data existed.
5. Conflicting and changing instructions. The strategy changed about six times in two days (proto-87 v2, proto-89 v3, proto-104 rev 1 to 4, proto-108 v4). The handwriting target was only found at 21:30 to 22:00 IST 09-30 (H1), after printed-22-language benchmark and South work. Protocol numbering collides (two proto-107 files, two proto-108 files; DISPATCH §23/§24/§25/§36 numbered more than once). NEXT rev 5 contained errors (H-6). The mentor's red line "no training before research validation" conflicts with the engine ladder (Day 3 = training) until the planner added "no training before G-2.5". Concurrent editors overwrote each other (proto-86 breach; another agent moved the whole `docs/campaign` tree unlogged).
6. Agents idle by design. Rule 19 says agents never edit NEXT.md, and work arrives as one paste line per agent. After finishing, Agents 1 and 3 log "idle, awaiting planner" and Agent 2 "awaiting go". Nobody self-assigns the next item from the plan.
7. Environment and data gaps. The surya package is not installed, Bodhan's PyTorch path needs CUDA, there is no GPU access, the Sarvam key is dead, easyocr ta/ml weights are broken or missing, and the Bengali handwriting data is not on disk.
8. Verification effort aimed at paper. Of 8 `blind_verify_*` reports, only `blind_verify_S5` (and partly gate1) recompute numbers from artifacts; `blind_verify_archive` and `_100strike` check that files exist or strings are absent. W4.md carries triple duplicates (S2 ×3, P ×2, copy-back ×2), which hides the real state (see the 17:15 "STATE CORRECTION").

## Bottom line
Verified and real: the Wave 1 to 2 research docs, the South tesseract/rapidocr/doctr/anuvaad/easyocr-te-kn scores, Bodhan Gate 1 numbers on the printed pair set, the incident restore (A0 to A3), and the Gujarati slice manifest. Everything on the critical path (HW-ID, HW0, HW1, G-2.5, HW2, GPU, product integration, E1) is NEVER STARTED.
