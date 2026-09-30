# LOOP_SPEC_W5_W6_W7 — W5 freeze → W6 training → W7 eval (AGENT-1)
**Date:** 2026-09-29 22:30 IST · **Author:** AGENT-1 · **Skill:** looper (loop-design coach)

**Mode:** Looper scaffolding output (loop.yaml, LOOP.md, RUN_IN_SESSION.md merged into this single doc for review). Per looper SKILL.md step 9 emission: would also emit `loop.yaml`, `loop.resolved.json`, `run-loop.py`, `loop-workspace/` — but for a paper review of the validation-call loop, this single doc is more readable.

---

## A. LOOP HEADER

```yaml
loop_id: W5_W6_W7_INDIC_OCR
version: 0.1
author: AGENT-1
date: 2026-09-29
host: opencode (MiniMax-M3)
companion_skills:
  - paperthin/mandela (eval-leakage audit at gate C)
  - paperthin/factchk (number verification at every measurement)
  - paperthin/hate (load-bearing objection at gate A)
  - ecc/verification-loop (cross-engine verification)
  - ecc/terminal-ops (evidence-first execution)
  - paperthin/sip (auto self-check after each iteration)
privacy:
  redaction_globs: [.env, .env.*, secrets/**, **/*.key, **/*sarvam*]
  cross_vendor_egress: NONE (all models local)
```

---

## B. GOAL STAGE (with goal-rubric applied)

### B1. Goal statement (measurable)

> **Beat Sarvam Vision 2.1's 87.39 average accuracy on the Sarvam Indic OCR Bench (6,909 blocks, 22 langs + EN) on a comparable subset of our probe22 data (1,227 items, 18 langs, 100/lang), with the constraint that we may NOT train on Sarvam's bench or use Sarvam as a wrap target beyond the 54-call cap.**

### B2. Outcome (concrete deliverable)

- **Primary:** A W6-trained model checkpoint (or wrap-pipeline routing) whose per-language CER on probe22's 1,227-item set is **at least 3 percentage points lower** than Sarvam's worst measured cells (KS, mni, sat, or, OldScan).
- **Secondary:** Same model on the public Sarvam Indic OCR Bench (`sarvamai/indic-ocr-bench`) for cross-bench verification (optional, requires user approval for download).
- **Tertiary:** A `W7_FINAL_REPORT.md` + `W7_LEADERBOARD.md` documenting the result with disk-verifiable per-language metrics.

### B3. Scope boundary (what's IN / what's OUT)

| IN scope | OUT of scope |
|---|---|
| W5 freeze meeting 2026-09-30 (Vinay) | New backbone invention (§9 hard rule) |
| W6 training Oct 2-8 (post-freeze) | Training on barred langs (§6.4 LOCKED) |
| W7 evaluation Oct 9-10 | Sarvam calls beyond 54-cap (D2 LOCKED) |
| Wrap-pipeline + QLoRA kok+pa (Option A) | Cloud GPU spend without explicit budget (D1 LOCKED) |
| Backbone: GLM-OCR 0.9B primary | Backbone swap to Qwen3.5-9B without QLoRA evaluation |
| Metrics: McNemar + Wilson + Ph6 estimator law | Bench re-definition (use Sarvam's as-is) |

### B4. Context sources (what the loop READS each iteration)

| Source | What it provides | Refresh cadence |
|---|---|---|
| `level2/probe22/scores/LEADERBOARD.md` | Current per-engine × per-lang CER | Each loop iteration |
| `level2/probe22/scores/mcnemar_full_matrix.json` | Pairwise p-values | Each loop iteration |
| `level2/probe22/scores/wilson_ci_*.json` | 95% CI per engine | Each loop iteration |
| `level2/probe22/sheet.csv` | All 12,324 raw predictions | Each loop iteration |
| `docs/research/level7/FINAL_VERDICT_2026-09-27.md` | Decisions D1-D4 + locked verdicts | Read-once at loop start |
| `INTEGRATED-ELITE-STACK.md` | Backbone + tool decisions | Read-once at loop start |
| User (Vinay, then orchestrator) | Strategy option + budget approval | Gate decisions only |

### B5. Done state (when the loop STOPS in success)

- ✅ W7_LEADERBOARD.md exists with per-lang CER, McNemar matrix, Wilson CIs
- ✅ All 18 probe langs have a winner (or n<50 flagged)
- ✅ K1 (McNemar p<0.05 vs Sarvam_on_3_per_lang) is reported per language
- ✅ At least 3 SAFE langs show |Δ CER| ≥ 3pt vs Sarvam
- ✅ User-signed wrap-up email/note archived to `_archive/w7_wrap_*.md`

---

## C. VERIFICATION STAGE (with verification-rubric applied)

### C1. Verification criteria (typed)

| Criterion | Type | Threshold | Cost |
|---|---|---|---|
| Per-engine CER on probe22 sheet.csv | programmatic | Wilson 95% CI upper < next-engine point | $0 (disk read) |
| McNemar pairwise engine comparison | programmatic | p < 0.05 (paired, exact) | $0 (disk read) |
| Per-lang winner determination | programmatic | n≥50, McNemar p<0.05 vs ≥5/10 opponents | $0 (computed) |
| Wrap-only baseline CER | programmatic | Pre-trained (no finetune) | $0 (rerun orchestrator) |
| QLoRA kok+pa improvement | programmatic | McNemar p<0.05 AND \|Δ\| ≥ 3pt | $0 (local mlx-tune) |
| Sat/ks/mni GT integrity | judge (human) | Barred languages: garbage GT flagged | User 10-min spot-check |
| Sarvam per-lang comparison | judge (compute) | 3-pack subset (already in sheet.csv) | $0 |
| Final wrap-up narrative | judge (LLM-as-reviewer) | 1-page summary in W7_FINAL_REPORT.md | $0 |
| User signoff | human | Yes/no email or note | User time |

### C2. Reviewer / Judge split (per looper rule 5)

| Role | Who | What |
|---|---|---|
| **Reviewer** | Verdict agent | Writes notes (PASS/NEEDS-WORK on each criterion) |
| **Judge** | User (final) + paperthin/mandela (eval-leakage) | Returns structured verdict (PROCEED / KILL / PIVOT) |
| **Operator** | Orchestrator (main session) | Tracks progress, manages handoffs |

`revise_until_clean` gate verdict_source: `paperthin/mandela` for eval-gate, `human` for final wrap-up.

---

## D. CONTROL STAGE (with control-rubric applied)

### D1. Termination guards (per looper rule 6, multiple required)

| Guard | Value | Source |
|---|---|---|
| `max_iterations` | 12 (one per week through W7 + buffer) | Per workflow timeline |
| `revise_cap_per_gate` | 3 (revise_until_clean max rounds) | Per looper default |
| `no_progress_stop` | 2 consecutive iterations with no metric improvement → ESCALATE to user | Anti-sprawl guard |
| `wall_clock_cap` | 8 hours total per iteration (W6 budget) | Per mlx-tune estimate |
| `budget_cap` | $0 (D1 LOCKED — no cloud) | Standing law |
| `human_stop_point` | User review at every gate transition | Looper rule 6 explicit |

### D2. Execution boundary (per looper rule 8)

- **Workspace:** `/Users/srujansai/Desktop/South/` (current)
- **Isolation:** Same workspace, but loop writes to `loop-workspace/w5_w6_w7/` (NEW directory) for transient artifacts. Final deliverables land in canonical locations (`level2/probe22/scores/`, `level2/reports/`).
- **No-progress signals:** CER delta on test split < 0.005 across 2 consecutive iterations OR McNemar p-value drift > 0.10.

### D3. State + observability

- **State file:** `loop-workspace/w5_w6_w7/state.json` (per-iteration gate verdicts, McNemar matrix snapshot, metric deltas)
- **Run log:** `loop-workspace/w5_w6_w7/run-log.md` (per-iteration narrative, git-committed at gate transitions)
- **Checkpoint:** Each W5/W6/W7 phase ends with a git commit + pushable to a separate branch `w5_w6_w7_loop` for review.

---

## E. HOST MODEL + COUNCIL STAGE

### E1. Host model

- **Primary:** opencode (this session, MiniMax-M3)
- **Fallback:** Claude Code (if opencode fails), Kimi K2 (if both fail) — but D1 LOCKED says no cloud, so Kimi is out.
- **Detection:** `which opencode` and `which claude` on macOS.

### E2. Council (multi-voice deliberation)

For high-stakes gates (gate B — Vinay strategy approval; gate D — QLoRA go/no-go), use a 4-voice council per paperthin/council skill:

| Voice | Role | Output |
|---|---|---|
| Optimist | "Best-case scenario, what's the upside?" | 1-line vote |
| Skeptic | "What's the load-bearing objection?" (paperthin/hate) | 1-line vote |
| Operator | "What does this cost in time + money + risk?" | 1-line vote |
| Customer (Vinay proxy) | "Does this advance the W6 mission?" | 1-line vote |

Verdict = majority OR user override. Tie → escalate.

---

## F. GATE STRUCTURE (the actual flow)

### F1. Gate A — Vinay Strategy Approval (2026-09-30)

**Inputs:** VINAY_MEETING_PACKET.md (4 decisions)
**Outputs:** User-decision-record.md (Option A/B/C, budget, micro-repair yes/no, downloads yes/no)
**Verdict:** User only.
**Stop conditions:**
- User says "Option A" + QLoRA green-lit → PROCEED to Gate B
- User says "Option B" (wrap-only) → PROCEED to Gate D with QLoRA skipped
- User says "Option C" (new backbone) → ESCALATE to plan redesign
- User defers → LOOP_PAUSE until user returns
- User says "Option A but no QLoRA budget" → PROCEED to Gate D as wrap-only

**No-progress signal:** User doesn't return by Wed 2026-10-01 EOD → loop emits PAUSED.

### F2. Gate B — W5 Freeze (post-meeting, pre-W6)

**Inputs:** User decision, all current disk scores
**Outputs:** `W5_FREEZE_RECORD.md` (D1-D4 re-confirmed; K1-K5 thresholds set; spec for W6 input)
**Verdict:** 4-voice council (Optimist/Skeptic/Operator/Vinay).
**Stop conditions:**
- Council PROCEED → gate C
- Council KILL → W6 abandoned; loop emits W7_WRAP with wrap-only deliverable
- Council PIVOT → strategy revision; loop emits PIVOT.md and re-enters Gate A

**No-progress signal:** 2 consecutive council rounds disagreeing on the same gate → ESCALATE to user with both sides' arguments.

### F3. Gate C — W6 Execution (Oct 2-8)

**Inputs:** Approved recipe (backbone, data, hyperparams)
**Outputs:** `w6_trained_model/` + `w6_metrics.json` + `w6_leaderboard.csv`
**Verdict:** paperthin/mandela (eval-leakage) on the W6 metric chain.
**Stop conditions:**
- mandela: leak detected → ESCALATE to user with leak description
- mandela: clean + McNemar p<0.05 + |Δ| ≥ 3pt → PROCEED to Gate D
- K4: memory peak > 12 GB → KILL QLoRA, fall back to wrap-only

**No-progress signal:** 2 consecutive iterations with no metric improvement → KILL QLoRA, ship wrap-only.

### F4. Gate D — W7 Evaluation (Oct 9-10)

**Inputs:** W6 model (or wrap-pipeline routing)
**Outputs:** `W7_LEADERBOARD.md` + `W7_FINAL_REPORT.md`
**Verdict:** User final signoff.
**Stop conditions:**
- User signs off → loop COMPLETE
- User requests another iteration → loop re-enters Gate C
- User requests strategy revision → loop re-enters Gate A

**No-progress signal:** N/A — this is the final gate.

---

## G. CONFIRMATION FLOW (ASCII)

```
+--------------------------------+
| 1. Gate A: Vinay meeting       |
|    decisions (4 questions)     |
|    USER JUDGMENT               |
+--------------------------------+
               |
               | (Option A/B/C chosen)
               v
+--------------------------------+
| 2. Gate B: W5 freeze           |
|    4-voice council verdict     |
+--------------------------------+
               | PROCEED
               v
+--------------------------------+
| 3. Gate C: W6 train + eval     |
|    paperthin/mandela audit     |
+--------------------------------+
               | McNemar p<0.05 + |Δ|≥3pt
               | AND mandela clean
               v
+--------------------------------+
| 4. Gate D: W7 wrap-up          |
|    USER JUDGMENT               |
+--------------------------------+
               | User signs off
               v
+--------------------------------+
| 5. Loop COMPLETE               |
|    state.json archived         |
+--------------------------------+

Stops:
  - max 12 iterations (4 weeks: W5/W6/W7 + buffer)
  - revise cap 3 per gate
  - no-progress 2 consecutive
  - wall-clock 8h per iteration
  - budget $0 (D1 LOCKED)
  - user stop at every gate transition
```

---

## H. EMIT CHECKLIST (per looper step 9)

- [x] Goal has clear outcome, scope, context, done state
- [x] Verification criteria typed (programmatic + judge + human)
- [x] Each `revise_until_clean` gate has verdict_source (mandela / user / council)
- [x] Every external invocation is argv (no shell strings)
- [x] Cross-vendor egress: NONE (D1 LOCKED, all local)
- [x] Loop control: iteration, revision, no-progress, wall-clock, budget caps
- [x] Execution boundary: current workspace + loop-workspace/
- [x] Observability: state.json + run-log.md per iteration
- [ ] Compile + lint: NOT EXECUTED (would require running looper.py compile — not done in this pass; the spec is paper-review)

---

## I. CRITICAL EDGE CASES (laya + hate + mandela notes)

| Edge case | Detection | Mitigation |
|---|---|---|
| User doesn't return for Vinay meeting | loop-workspace/loop-status.json `last_user_contact` > 7 days | LOOP_PAUSE; emit PAUSED banner |
| mlx-tune install fails mid-iteration | exit code != 0 from mlx-tune run | KILL QLoRA, ship wrap-only |
| Sarvam-Indic-OCR-Bench download refused by user | §9 hard rule | Skip cross-bench verification, document limitation |
| McNemar matrix contradicts itself across iterations | diff > 0.10 on paired p-values | RECOMPUTE from sheet.csv; if still diverges, ESCALATE |
| Wrap-only routing breaks (engine API change) | orchestrator.py smoke test fails | LOOP_PAUSE; restore from orchestrator.py git HEAD |
| User changes Vinay decision mid-loop | User signals "I changed my mind" | Re-enter Gate A |

---

## J. WHY THIS LOOP, NOT A SIMPLER ONE

The simpler loop would be: "train QLoRA, eval, ship." But:
- §6.4 GT verdicts make 6/18 langs BARRED from training.
- D1-D4 LOCKED decisions must be honored.
- §9 forbids downloads without user approval.
- The Sarvam-comparison target is on a DIFFERENT benchmark than our probe.

This loop respects all of that by encoding the gates as user-judgment at strategy transitions and programmatic at execution. **The 4-voice council at Gate B is the only non-trivial addition over a linear flow** — it forces the documenter to write load-bearing objections before approving, which is the paperthin/hate discipline operationalized.

---

**End of LOOP_SPEC_W5_W6_W7.md. 4 gates, 4 termination guards, 2 budget caps, 1 user stop per gate.**