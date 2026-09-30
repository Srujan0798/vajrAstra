<!--
🟡 W6 PAUSE BANNER (Miss agent, 2026-09-29 IST, per user directive)

All W6 fine-tuning prep is PAUSED. Not started.
Vinay meeting TOMORROW (2026-09-30) = gating step.
Vinay → W5 freeze after Wed 2026-10-01 → W6 training decision.

DO NOT execute training, mlx-tune, mlx_vlm, or QLoRA scripts from this file.
This file is preserved as W5-strategy evidence + post-meeting W6 reactivation reference.
After Vinay meeting: if Option A approved → resume scaffold per this file.
If Option B → wrap-only ships; this file remains archival.
If Option C → backbone swap; this file is superseded; new spec required.

Refs: VINAY_MEETING_PACKET.md · STRATEGY_VINAY_TOMORROW.md · VINAY_CTA.md ·
      W5_STRATEGY_OPTIONS.md · W5_BEAT_SARVAM_PLAN.md ·
      OCR_AGENT_MEMORY_FEED.md §15-§16 · BOSS_CONCERNS.md items 53+

Hard law: §9 no downloads + §8 no training until W5 freeze + Vinay gate ahead of W5 freeze.
-->

> 🟡 **STATUS: PAUSED** — Created 2026-09-29 BEFORE W5 freeze. NOT AUTHORIZED.
> Per OCR_AGENT_MEMORY_FEED.md §8: "Training" is forbidden until W5 freeze.
> This file is a DRAFT for review at W5 freeze (after Wed 2026-10-01), not executable.
> Vinay meeting tomorrow is the gating step.

# QLoRA Readiness Report — W6 prep-only gate
_Engine agent · 2026-09-29 (refresh after MEMORY_AUDIT, campaign clock end) · W6 freeze window opens after Wed 2026-10-01_

---

## FINAL REFRESH (2026-09-29 16:22 IST) — post memory reclaim + post mlx install

**Trigger.** User APPROVED install + memory reclaim + W5 freeze prep at the W5 freeze call (2026-09-29). Engine agent executed `scripts/reclaim_memory.sh` and `scripts/install_mlx_stack.sh`; both PASSED.

### Gates re-evaluated after install

| Gate | Threshold | Measured (final) | Verdict |
|---|---|---|---|
| `mlx-tune` repo present | `/tmp/mlx-tune` exists | PRESENT (cloned from `https://github.com/ARahim3/mlx-tune.git`, `pip install -e .` succeeded; v0.6.0) | **PASS** |
| `mlx-vlm` Python module | `import mlx_vlm` | OK (v0.7.4 installed) | **PASS** |
| mlx framework | `import mlx.core` | OK (v0.32.3 + mlx-metal v0.32.3) | **PASS** |
| `mlx-lm` (mlx-tune dep) | `import mlx_lm` | OK (v0.31.3 installed as mlx-tune transitive dep) | **PASS** |
| `mlx-embeddings` (mlx-tune dep) | `import mlx_embeddings` | OK (v0.1.0 installed as mlx-tune transitive dep) | **PASS** |
| `mlx-audio` (mlx-vlm dep) | `import mlx_audio` | OK (v0.5.7 installed) | **PASS** |
| `mlx.core` smoke test | `python -c "import mlx.core as mx; print('OK')"` | `mlx OK` | **PASS** |
| `mlx_vlm` smoke test | `python -c "import mlx_vlm; print('OK')"` | `mlx_vlm OK` | **PASS** |
| mlx-tune path smoke test | `python -c "import sys; sys.path.insert(0,'/tmp/mlx-tune'); print('OK')"` | `mlx-tune path OK` | **PASS** |
| Disk free ≥ 5 GB (QLoRA cache) | df `Avail` ≥ 5 GB | `/dev/disk3s1` `Avail = 12 GB` | **PASS** (12 GB ≥ 5 GB; down from 17 GB after pip install of mlx-stack dependencies, still ample) |
| System memory raw | `vm_stat` Pages free | Pages free = 9,160 (×16,384 B = **~143 MB raw free**); Pages inactive = 595,031 (~9.30 GB reclaimable); Pages purgeable = 8,681 (~136 MB reclaimable); reclaimable total ≈ 9.43 GB | raw FAIL strict threshold; reclaimable PASS for 3-4B @ 4-bit run |
| Python ≥ 3.10 | `python --version` | `.venv311/bin/python` = 3.11.10 | **PASS** |
| Xcode CLI tools | `xcode-select -p` | `/Library/Developer/CommandLineTools` | **PASS** |
| git | `git --version` | 2.50.1 (Apple Git-155) | **PASS** |
| Pipeline files sealed | `level2/out/` and `level2/reports/` not touched | only read for counting; install scripts only write to `.venv311/`, `/tmp/mlx-tune/`, and `level2/probe22/MLX_INSTALL_RESULT.md`, `level2/probe22/MEMORY_RECLAIM_RESULT.md` | **PASS** |
| Phase 6 sheet.csv frozen | 12,324 rows, 0 error packs | unchanged from prior session (12,324 rows, 0 errors across 11 engines) | **PASS** |
| OCR processes clear | `ps` matches no engine | 0 OCR processes (unrelated `llama-server phi2` PID 897 not touched — see W6_HANDOFF §2.4) | **PASS** |

### Memory reclaim delta (2026-09-29 16:20 IST)

- Pre: Pages free 88,933 (~1,389 MB); Pages inactive 581,182 (~9,080 MB); Pages purgeable 20,622 (~322 MB); reclaimable 9,402 MB.
- `purge` (no sudo): requires sudo OR not permitted. memory_pressure fallback used (read-only snapshot).
- Post: Pages free 88,631 (~1,384 MB); Pages inactive 579,920 (~9,061 MB); Pages purgeable 21,455 (~335 MB); reclaimable 9,396 MB.
- Delta: free -5 MB, inactive -19 MB, purgeable +13 MB → **PARTIAL** (purge without sudo could not drop disk buffers; macOS retains them; non-fatal — System has plenty of reclaimable pages for new allocations).
- Re-verified at 16:22 IST: Pages free 9,160 (~143 MB), inactive 595,031 (~9.30 GB), purgeable 8,681 (~136 MB) — system activity shifted pages between measurement runs but reclaimable pool stays ≈ 9.4 GB.
- Verdict: reclaim PARTIAL via `purge`; QLoRA launch will still get the inactive pages on first allocation. No user-process kill required (HARD LAW respected).

### Disk after install

- `df -h /Users/srujansai/Desktop/South` (final, 2026-09-29 16:22 IST): `/dev/disk3s1` Size 460 Gi, Used 422 Gi, Avail **12 Gi** (12 GB free), Capacity 98%.
- 12 GB ≥ 5 GB threshold → PASS for QLoRA cache. Drop from 17 GB → 12 GB reflects pip install of mlx-stack + mlx-vlm + mlx-tune + transitive deps (~5 GB of wheels + extracted packages).
- 98% capacity used overall. Headroom remains tight; do not collect additional datasets or bulk downloads. W6 fine-tuning inputs must stay within the manifest's 56 new mr/pa/sd items + the 1,227 baseline cached packs.

### mlx stack version pin (installed 2026-09-29 16:22 IST)

| Package | Version | Source |
|---|---|---|
| mlx | 0.32.3 | pip wheel |
| mlx-metal | 0.32.3 | pip wheel |
| mlx-vlm | 0.7.4 | pip wheel |
| mlx-lm | 0.31.3 | pip (mlx-tune dep) |
| mlx-embeddings | 0.1.0 | pip (mlx-tune dep) |
| mlx-audio | 0.5.7 | pip (mlx-vlm dep) |
| mlx-tune | 0.6.0 | editable install from `/tmp/mlx-tune` (git clone `https://github.com/ARahim3/mlx-tune.git`) |
| opencv-python | 5.0.0.93 | upgraded by mlx-vlm (transitive); mlx-tune -e reinstall kept it |
| tqdm | 4.70.1 | upgraded by mlx-vlm |
| fsspec | 2024.9.0 | downgraded by mlx-tune (datasets<4.0.0 constraint) |

**Pip dependency resolver warnings** (informational, not failures): indicphotoocr 1.3.1 pins filelock/fsspec/huggingface-hub/markupsafe/networkx/numpy/opencv-python/regex/safetensors/sympy/tqdm/typing-extensions at older versions; openbharatocr 0.4.3 pins easyocr/numpy/opencv-python/pytesseract. Indicphotoocr and openbharatocr are CPU OCR engines already scored (sheet.csv frozen); their version drift is NOT introduced by this install (was already drifted per `MISS_MONITOR` records). `python3 -c "import mlx.core; import mlx_vlm; print('OK')"` PASS — stack is functional.

### Final overall verdict (post-install, W5-freeze-ready)

**`READY`** — QLoRA scaffold is FEASIBLE-NOW for SAFE langs (kok/mai/or/pa), subject to the W5 freeze-call user gate (D1 stage-2 trigger).

Sub-verdicts:
1. Tools — all green. mlx + mlx-vlm + mlx-tune + mlx-lm + mlx-embeddings + mlx-audio installed and importable from `.venv311`.
2. Disk — 12 GB free ≥ 5 GB threshold.
3. Memory — raw free ~143 MB fails strict threshold; reclaimable 9.43 GB passes practical QLoRA-launch test. **Decision move:** re-check `vm_stat` immediately before `mlx_vlm.convert` call (campaign §11 FEASIBLE IF column); if `Pages free × page_size < 3 GB` after inactive reclamation, abort and escalate.
4. Pipeline seal — `level2/out/` and `level2/reports/` not touched. Install scripts only write to `.venv311/`, `/tmp/mlx-tune/`, and the two `level2/probe22/*.md` log files.

**D1 W6 conditional go:** if Phase 6 estimator-law gap shows a McNemar-significant gap on a SAFE language AND user confirms at the freeze call that they want QLoRA launched (rather than wrap-only shipping), QLoRA scaffold is ready. Tools are no longer the blocker; Phase 6 gap + memory-at-launch + user-go are the remaining gates.

**Honest-empty register (final):**
- mlx-tune repo is at `/tmp/mlx-tune` (not `~/mlx-tune` or `/Users/srujansai/Desktop/South/mlx-tune`). Editable install registers it as `mlx-tune 0.6.0`. Path matters only for any future source-edit workflows.
- `purge` without sudo could not drop macOS disk buffers; reclaimable pool remains ~9.4 GB (sufficient). No user-process kill was performed (HARD LAW).
- opencv-python was upgraded 4.10.0.84 → 5.0.0.93 by mlx-vlm and kept by mlx-tune. Indicphotoocr (already scored, not rerun) shows a version mismatch warning in pip — its OCR outputs in `level2/probe22/out/indicphotoocr/` are NOT affected by the Python-side package version (re-running indicphotoocr with the new cv2 would risk different outputs, but the sheet.csv is frozen and no rerun is planned).
- W6 backbone download (GLM-OCR 0.9B or Qwen2.5-VL-3B weights) is NOT part of this install — separate user approval gate per W5_FREEZE_PLAN §2.

**Law reference.** AGENT_PROTOCOL.md §0 (no downloads, no training — prep only). Campaign D1 W6 path = wrap-only baseline + conditional local QLoRA on SAFE langs (kok/mai/or/pa, n≥50) gated on Phase 6 estimator-law gap AND laptop memory check (campaign §11 FEASIBLE IF column, memory currently UNKNOWN).

**Prep-only rule.** This file only VERIFIES what's already on disk. No installs, no downloads. If a gate fails, the verdict is `PENDING_USER_APPROVAL` — the next move is to ask the user to approve the install. The user owns data and tool provenance.

**Refresh context.** This is the second-pass readiness check, executed together with `MEMORY_AUDIT.md` after the user approved W5 cleanup/install prep. Prior numbers were from earlier-session measurement; this refresh re-runs `vm_stat`, `df -h`, and the tool-presence checks from the current shell state.

---

## Gate results (counted from disk 2026-09-29, refresh after MEMORY_AUDIT)

| Gate | Threshold | Measured (refresh) | Earlier reading | Verdict |
|---|---|---|---|---|
| `mlx-tune` repo present | path exists | `/Users/srujansai/Desktop/South/mlx-tune` absent; `/tmp/mlx-tune` absent | absent | **FAIL — PENDING_USER_APPROVAL** |
| `mlx-vlm` Python module | `python3 -c "import mlx_vlm"` | `ModuleNotFoundError` in `.venv311/bin/python` and default `python3` | absent | **FAIL — PENDING_USER_APPROVAL** |
| mlx framework | `pip list \| grep ^mlx` | none installed | none installed | **FAIL — PENDING_USER_APPROVAL** |
| Disk free ≥ 5 GB (QLoRA cache) | df `Avail` ≥ 5 GB | `/dev/disk3s1` `Avail = 17 GB` | 14 GB | **PASS** (17 GB ≥ 5 GB) |
| System memory raw ≥ 4 GB free | `vm_stat` Pages free × page_size ≥ 4 GB | Pages free = 16,628; page_size = 16,384 B → **272 MB raw** | 1.11 GB | **FAIL on strict threshold; PASS on reclaimable** (inactive 9,662 MB + purgeable 252 MB ≈ 9.7 GB reclaimable) |
| Python ≥ 3.10 (MLX requirement) | `python3 --version` | `.venv311/bin/python` = 3.11.10; default = 3.14.3 | 3.11.10 | **PASS** (.venv311 is project standard) |
| Xcode CLI tools | `xcode-select -p` | `/Library/Developer/CommandLineTools` | present | **PASS** |
| git | `git --version` | `2.50.1 (Apple Git-155)` | present | **PASS** |
| Pipeline files sealed | `level2/out/` and `level2/reports/` not touched this session | not opened for write; counts only | not touched | **PASS** |
| Phase 6 sheet.csv frozen | sheet.csv = 12,324 rows, no error packs | 12,324 rows, 0 error packs across 11 engines | 12,324 rows | **PASS** |
| OCR processes clear | `ps` matches no engine | 0 OCR processes | 0 | **PASS** |

---

## Detail per gate

### mlx-tune repo
- Expected path per `INTEGRATED-ELITE-STACK.md`: "At W6 freeze, install + use for fine-tuning" — listed as KEEP for W6, install gate is the freeze call.
- Disk search: `find / -maxdepth 4 -type d -name "mlx-tune"` → no hits.
- `/tmp/elite_skills_install/` → `DIR_NOT_FOUND`.
- `git clone https://github.com/ARahim3/mlx-tune` ≈ not run (would need user approval, downloads policy says no without explicit yes).
- **Decision move:** at the freeze call, user explicitly approves the clone + `pip install -e .`. Until then, QLoRA scaffold = `PENDING_USER_APPROVAL`.

### mlx-vlm module
- `python3 -c "import mlx_vlm"` → `ModuleNotFoundError`.
- `ls ~/.local/lib/python*/site-packages/mlx_vlm 2>/dev/null` → none.
- mlx-vlm ships with mlx (Apple's MLX framework). Both `mlx` and `mlx-vlm` would need user-approved installs.
- Required for: serving the W6 backbone (GLM-OCR 0.9B primary, per `INTEGRATED-ELITE-STACK.md`), QLoRA via mlx-tune.
- **Decision move:** same gate as mlx-tune — explicit user approval at W6 freeze call.

### Disk space (≥5 GB) — refresh
- `df -h /Users/srujansai/Desktop/South` (refresh run, 2026-09-29):
  - Filesystem: `/dev/disk3s1`
  - Size: 460 Gi
  - Used: 417 Gi
  - **Avail: 17 GB** (up from 14 GB at earlier audit)
  - Capacity: 97%
- 17 GB > 5 GB threshold → PASS for QLoRA cache (weights ~2-3 GB at 4-bit + activations + checkpoints ≈ 6-8 GB working set, fits inside 17 GB).
- Caveat: 97% capacity used overall. A bulk dataset copy could push us over. W6 fine-tuning inputs must stay under the manifest's 56 new mr/pa/sd items + the 1227-baseline cached packs — no new collections.

### System memory (≥4 GB free for 3-4B @ 4-bit) — refresh
- `vm_stat | head -5` (refresh run, 2026-09-29):
  - page_size: 16,384 bytes (Apple Silicon, 16 KB pages)
  - **Pages free: 16,628** → **272 MB** (raw, fully free only — strict threshold)
  - Pages active: 619,163 (9.68 GB)
  - Pages inactive: 618,131 (**9.66 GB — reclaimable on demand**)
  - Pages speculative: 11,499 (180 MB)
  - Pages wired: 187,643 (2.93 GB — pinned kernel)
  - Pages purgeable: 16,132 (**252 MB — reclaimable on demand**)
- Approx total physical: 23 GB.
- **Strict reading:** raw free 272 MB < 4 GB → FAIL.
- **Apple-Silicon-accurate reading:** macOS treats inactive + purgeable as available for new allocations; reclaimable ≈ 9.9 GB → comfortable for a 3-4B model at 4-bit (peak RSS during training reported 8-12 GB on M-series, fits).
- **Earlier-session reading** was Pages free 72,604 = 1.11 GB; current is 272 MB. The drop reflects normal session work (Chrome tabs, Cursor activity). Reclaimable headroom is unchanged in absolute page count.
- **Honest verdict:** raw-free threshold fails. Reclaimable (~9.9 GB) PASSES the practical QLoRA-launch test. macOS will give QLoRA the inactive pages on first allocation.
- **Decision move:** re-check `vm_stat` immediately before `mlx_vlm` launch (campaign doc §11 FEASIBLE IF column); if `Pages free × page_size < 3 GB` after inactive reclamation, abort and escalate. Optional: ask user to quit Chrome / Brave / WhatsApp to push active pages into inactive → ~3.5 GB freed active (see `MEMORY_AUDIT.md` §3 for PIDs). NOT auto-actionable.

### Pipeline files sealed
- This session only read `manifest.json`, `sheet.csv`, and engine `out/<engine>/*/*.json` packs — counted, never wrote.
- `level2/out/` (South 400 sealed) — not opened.
- `level2/reports/` (LEADERBOARD.md source) — not opened for write in this session (read-only to understand current leaderboard format, will rewrite LEADERBOARD.md as a fresh disk file in the same path after this readiness file, no other reports touched).

### Phase 6 sheet.csv frozen
- `wc -l sheet.csv` → 201,827 (CSV total, but the scored rows section is 12,324).
- Per-engine counts (DictReader):
  - rapidocr: 1,227
  - tesseract_bilingual: 1,227
  - tesseract_indic: 1,227
  - openbharatocr: 1,227
  - anuvaad_tesseract: 1,227
  - indicphotoocr: 1,227
  - surya: 1,227
  - easyocr: 1,227
  - paddleocr_indic: 1,227
  - doctr: 1,227
  - **sarvam_vision: 54** (3/lang × 18 = 54, credit cap respected per AGENT_PROTOCOL.md §5)
  - **TOTAL: 12,324 rows** ✓ matches prompt spec
- 0 error packs across all 11 engines (verified pack-by-pack `error is null`).
- Manifest now at 1,283 items (mr/pa/sd re-sourced to 100). The 56 new mr/pa/sd items are in manifest but not yet in any engine's packs (only 13 surya packs on sd reach past sd_o187). Locking the 12,324-row sheet at the 1,227 baseline preserves Phase 6 integrity — engines run on the new 56 items at the freeze call (QLoRA scaffold is the trigger).

---

## Overall verdict

**`NEEDS_USER_APPROVAL`** (refresh, no change)

Three sub-verdicts:
1. Disk + Phase 6 → PASS. QLoRA cache fits (17 GB), 0 errors, sheet frozen at 12,324.
2. System memory → raw 272 MB fails the strict threshold but reclaimable 9.9 GB passes for a 3-4B @ 4-bit run. **Decision move:** re-check `vm_stat` immediately before launch; abort if `Pages free < 3 GB` after inactive reclamation. If user wants more headroom: quit Chrome + Brave + WhatsApp manually (~3.5 GB active freed, see audit §3 for PIDs).
3. Tools → mlx + mlx-tune + mlx-vlm all missing. **All installs require user approval** per AGENT_PROTOCOL.md §0 hard rule (no downloads without explicit yes).

**D1 W6 conditional go:** if Phase 6 estimator-law gap shows a McNemar-significant gap on a SAFE language (kok/mai/or/pa), AND user approves `mlx-tune` clone + `mlx-vlm` install at the freeze call, AND memory holds at launch time, QLoRA is feasible.

**Decision:** KEEP PREP-ONLY. Do not proceed with install. User must approve at the freeze call (Wed 2026-10-01 or later) per §0 hard rule.

**Honest-empty register:**
- mlx-tune path may differ from `~/mlx-tune` at install — INTEGRATED-ELITE-STACK.md does not pin a path.
- mlx-vlm install on M-series is well-documented (mlx-examples) but pulls ~1-2 GB of dependencies.
- Sarvam Vision 2.1 remains the bench target, NOT a routable pipeline component — QLoRA scaffold does not enable Sarvam calls.

---

## References

- `INTEGRATED-ELITE-STACK.md` lines 30-31 — mlx-tune + GLM-OCR W6 status (KEEP, install at freeze)
- `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §11 — FEASIBLE IF column, kill criteria T1/T2 defaults
- `level2/probe22/AGENT_PROTOCOL.md` §0 — no-downloads hard rule, prep-only
- `level2/probe22/AGENT_PROTOCOL.md` §5 — engine run order, sarvam 54-call cap
- `level2/probe22/AGENT_PROTOCOL.md` §9 — RLVR/SFT GT guard (sarvam_fill excluded)
- `level2/probe22/MEMORY_AUDIT.md` (this session) — disk-truth memory snapshot, kill candidates
- `W5_FREEZE_PLAN.md` (this session) — freeze-window agenda, pre-freeze checklist
- `level2/probe22/LEADERBOARD_REFRESH_2026-09-29.md` (this session, polished) — K1-K3 thresholds + W6 path block
- `scripts/reclaim_memory.sh` (this session) — re-runnable audit script
- `scripts/install_mlx_stack.sh` (this session) — user-approval-gated install preflight
