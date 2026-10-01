# P4 Elite Sequencing (Plan Only)

**Cascade plan** for Level-3 and beyond, in strict dependency order. Code only after Srujan approves each gate.

| Step | Description | 4-page gate checkpoint | Dependencies |
|------|-------------|----------------------|------------|
| **C1** | **Cascade: cheap engine → surya → Sarvam**<br>Run cheapest available engine (openbharatocr / rapidocr) on all 400 pages first. Flag any page where CER > 0.6 for escalation. Only then invoke surya on flagged subset. | Gate: on 4 random flagged pages, confirm surya CER < 0.55 before full run. | C1 must pass before C2. |
| **C2** | **Escalaction: Sarvam on low-confidence pages**<br>Sarvam Vision runs on the 66 own-script clean pages (from A3) plus any flagged pages from C1 that lack own-script GT. Cost: ~₹33 for 66 pages + additional for flagged. | Gate: 4-page Sarvam gate (te_087, ta_092, kn_048, ml_019) must pass dry-run with manifest-driven language; no `te-IN` default; `_extract_text` returns `""` on unknown JSON shape. | C2 requires Srujan key + ₹ approve (H-1). |
| **C3** | **Distillation: train compact student on surya+ corrected GT**<br>Only if C2 shows Sarvam clearly beats surya on the 66-page pool. Student uses L1-label definition from SOUTH_CANON §F; training on sft_noisy_to_gold.jsonl gold_text. | Gate: 4-page distillation hold-out set; validate that student CER < surya CER on those 4 pages. | C3 requires C2 PASS + Srujan approval (H2). |
| **C4** | **Active learning loop**<br>Iteratively select the highest-uncertainty pages for human verification, retrain/rinse. | Gate: each loop iteration must show median CER improvement ≥ 0.01 on the validated bench set. | C4 is open-ended; stop when budget exhausted or convergence. |

**Key constraints** (enforced by repo law):
- No new markdown essays at repo root or under `level2/research/`. All sequencing docs go under `docs/campaign/`.
- 4-page gate BEFORE any 400-page run. Each cascade step C1–C3 has its own 4-page gate.
- Archive, never delete. Outputs go to `docs/campaign/P4_ELITE_SEQUENCING.md` + research/ JSON results.
- Spending money (Sarvam calls) is Srujan's call only (H-1). C2 waits on key + spend approval.

**Output**: `docs/campaign/P4_ELITE_SEQUENCING.md` (single file, no essay sprawl). JSON results live in `level2/research/` (per law: code scripts are established pattern; prose memo moves to docs/).