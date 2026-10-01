# A6-CONCERNS — K-01..K-30 status vs evidence (read-only audit, snapshot /home/user/boss, 2026-10-01)

Caveat: the snapshot has text only. No data, weights, scores JSON, graphify-out, or product code. Items needing those are marked UNVERIFIABLE-HERE, not assumed. The ledger path in the task (docs/campaign/checkpoints/CONCERN_LEDGER_CLOUD_SESSION_2026-09-30.md) exists only inside /home/user/boss, not in /home/user/vajrAstra.
Status words: CLOSED (evidence) · PARTIAL · OPEN · STALE (register text no longer matches disk) · plus STANDING/PARKED/BLOCKED as the register uses.
Last verified: Part 0 was last synced at ~22:35 IST 09-30; W4/DISPATCH moved on (Sarvam key dead, Plan v4, Gold W0, NEXT REV 8). Many Part 0 rows are STALE for that reason.

## Ranked by impact on winning (open ones, highest first)
1. K-03 (test = 5,344 Bengali handwritten words; 0 HW baselines, 0 Bengali HW data) — NEXT.md REV 8 blocker 1.
2. K-01 (no same-scorer number vs Sarvam/Bodhan) — BENCHMARK_22.md:26, :340-344.
3. K-04/K-16 (G-2.5 not run, no Vinay sign-off; blocks all training).
4. K-26 (GPU SSH missing; PyTorch/Bodhan official path BLOCKED on CUDA, DISPATCH_LOG.md:706).
5. K-25/K-22 (official metric, format, deadline unknown; no 50-image dry run).
6. K-02 (portable product unproven; snapshot has only product/docs/B21_SYNTHETIC_LINES_SPEC.md).
7. K-27 (Sarvam reference column empty; key now dead).
8. K-21, K-19, K-20 (metric set, GT defects, empty-output diagnosis files all missing).
9. K-08/K-06 (leak tiers, 7 short languages).
10. K-17 (licences open), K-29, K-30, K-24, K-09, K-11, K-15, K-23, K-05.

## Per theme
- K-01 Win vs Sarvam: OPEN. Evidence: no head-to-head valid; our scorer is harsher; "87.39" metric UNKNOWN (BENCHMARK_22.md:26, :340). The verify grep hits only caveat text. Close: re-score the Sarvam-bench split with one shared scorer (Sarvam's metrics.py) and report Word Accuracy plus CER on our best engine. Owner: agent. Note: the winning target is the Bengali HW test, not Sarvam's bench, so planner should reframe K-01 around K-03.
- K-02 Portable product: PARTIAL, claim unproven here. W4.md:460-461 claims requirements.txt and Dockerfile DONE, but `git ls-files product` shows only product/docs/B21_SYNTHETIC_LINES_SPEC.md; Part 0 itself says cli/pdf_writer exist. No MLX-vs-PyTorch parity (DISPATCH_LOG.md:706 BLOCKED). Close: commit product/ files to the repo and run the Dockerfile CPU build plus one CLI run, paste output in W4.md. Owner: agent (Agent 3), then GPU parity by agent.
- K-03 Handwriting/test set: PARTIAL. CLOSED sub-part: H1 vision check, 13/13 Bengali (DISPATCH_LOG.md:581-587, W4.md ~440-447). STALE: docs/campaign/TEST_SET_PROFILE.md:37 and H1_TEST_PROFILE.json still say 35.7% Devanagari. H2 slice built on Gujarati Bo do/gu (16,490 items, W4.md H2) which is a different script from the Bengali test. Not done: H3 baseline, Bengali HW data (U-HW1), leak check HW0 (NEXT.md REV 8). Close: boss approves U-HW1 (IIIT Bengali), agent runs HW0 then zero-shot baseline on viewed test images. Owner: boss (approval) then agent. Also agent fixes the two stale files.
- K-04 Lead's method: PARTIAL. MULTI_LLM_EVAL.md:6 says 1 of 3 legs ran (ChatGPT leg PENDING BOSS). Plan v4 exists (proto-108-plan-v4-final.md) but G-2.5 not run and no Vinay session evidence. Close: boss pastes CHATGPT_EVAL_PROMPT.md result and runs the Vinay session. Owner: boss.
- K-05 One 22-lang benchmark: PARTIAL. manifest_v2 = 1,683 (DISPATCH_LOG.md:513). S5 section exists (W4.md:761) but only tesseract_indic n=400 CER 0.1450 is clean; easyocr ta broken, rapidocr 0.8427 and doctr 0.8236 look like broken runs; paddle/surya held (DISPATCH_LOG.md:775). S6 not done. Manifest itself is not in snapshot. Close: fix or label the broken engines, then S6. Owner: agent.
- K-06 100 per language: OPEN (no change). Part 0 lists 7 short langs; DISPATCH_LOG.md:513 "all 22 langs now >=100" refers to South draw only, so the register wording is ambiguous. Close: one Counter output pasted in W4.md and a boss re-source decision. Owner: boss + agent.
- K-07 Evidence honesty: STANDING. `grep -c DONE-VERIFIED BOSS_CONCERNS.md` = 6; Part 1 still mostly bare DONE. Evidence of violation: DISPATCH_LOG.md:777 "H3 REVERSED, previous H3 entry unauthorized". Close: n/a (rule); agent audits.
- K-08 Leakage: PARTIAL. S5 claims tiers never pooled (W4.md:761-). Home-ground risk for Sarvam bench unstated in any score table. Close: add per-tier headline table with an independent-set row. Owner: agent.
- K-09 Incident safety: PARTIAL. A4 PASS per W4 (NEXT.md REV 6) but DISPATCH_LOG.md:723 says CONDITIONAL; scores/ holds only mcnemar_summary.md in the snapshot, and DISPATCH_LOG.md:751 says mcnemar_full_matrix.json still running. A7 parked. Gold W0 only CONDITIONAL PASS (W4.md tail; 85 pyc lines in manifest). Close: reconcile A4 status, re-run the verify command on the Mac, re-verify W0 manifest without pyc. Owner: agent.
- K-10 Repo cleanliness: PARKED, partly STALE. Gold repo consolidation (proto-107) overtook it; 18 root .md remain (`ls *.md | wc -l` = 18). Close: boss says "resume cleanup" or GO-A/GO-D at W5. Owner: boss.
- K-11 Research harvest: PARTIAL. RESEARCH_DECISIONS.md has 50 RF rows (grep `^| *RF-`), DISPATCH_LOG.md:753-ish says RF-21..37 added; target met. Not merged into one canon (NEXT.md REV 8; proto-110 just assigned). Close: proto-110 canon merged with a verify grep. Owner: agent.
- K-12 Tools/graphify: STALE/UNVERIFIABLE. graphify-out absent from snapshot; update owed after LAYOUT FROZEN, which has been posted. Close: `graphify update .` on the Mac, paste ls -la. Owner: agent.
- K-13 Agent process: STANDING. Rule breaches visible (DISPATCH_LOG.md:777; Agent 1 §38 notes "12 agent processes active"). Close: n/a.
- K-14 Docs hierarchy: CLOSED for the hierarchy. AGENTS.md has "START HERE" (head -20), docs/INDEX.md exists with "the one map", README exists. Memory in _claude_memory present. Residual: graphify not updated (K-12).
- K-15 Meeting truth: PARTIAL. The verify grep matches MEETING_2026-09-29_STRUCTURED.md and MENTOR_PLAYBOOK.md (docs/PLAN.md exists). No VINAY_PLAN_BASELINE.md file anywhere (only mentioned in BOSS_CONCERNS.md and protos). Close: confirm M1-M10 fixes by grep, create or delete the baseline reference. Owner: agent.
- K-16 No training before validation: STANDING and holding. MULTI_LLM_EVAL.md has no Plan v3/v4 result; no trained model in NEXT.md REV 8. Gate is boss. Note DISPATCH_LOG.md:753 still queues "LoRA on Konkani"; keep gated.
- K-17 Licences: PARTIAL. RQ9_licences.md:19-27 shows CLEARED for tessdata and surya code, surya weights evaluation-only, 600K-KS CONTRADICTION. U27/U28 open (DISPATCH_LOG.md:~745). Close: one ledger row per weight actually shipped, plus Bodhan hosting approval. Owner: agent, boss for Bodhan approval.
- K-18 Sealed dirs: STANDING, UNVERIFIABLE-HERE (no data). Close: run the find counts on the Mac. Owner: agent.
- K-19 GT defects: OPEN. `ls docs/campaign/GT_DEFECTS.md` fails. Close: write the file (step Q). Owner: agent.
- K-20 Empty-output: OPEN. EMPTY_OUTPUT_DIAGNOSIS.md missing; paddle/surya held (DISPATCH_LOG.md:775). Close: write diagnosis for paddle brx/doi and surya sa. Owner: agent.
- K-21 Metric set: OPEN. RUBRIC_REPORT.md and rubric_report.py missing. H2 spec says same scorer reports CER/WER/median/catastrophic but no file proves it. Close: build rubric_report.py and run on S4 packs. Owner: agent.
- K-22 Submission readiness: PARTIAL. SUBMISSION_DRYRUN.md missing. Only a 3-file Tesseract product dry run (W4.md:545) and 5-item X dry run (DISPATCH_LOG.md:648). Close: 50-image run through the product CLI with latency, output saved. Owner: agent.
- K-23 Boss explainer: PARTIAL. BOSS_EXPLAINER.md exists (DISPATCH_LOG.md:300); numbers now stale after S5/Gate 1. Close: refresh after S5. Owner: agent.
- K-24 Concurrent writers: OPEN. Second-writer incident is recorded; NEXT REV 8 notes no sync since push. Close: SYNC A per proto-109. Owner: planner.
- K-25 Deadline: OPEN, confirmed. RQ1_official_rules.md:108-110 "NO official deadline; 10 of 12 rows TBD". Close: boss emails organiser if Vinay agrees. Owner: boss.
- K-26 GPU: BLOCKED, due today (2026-10-01). Bodhan official path BLOCKED on CUDA (DISPATCH_LOG.md:706). Close: boss hands SSH details; agent runs proto-106 §2 day-1 order. Owner: boss then agent.
- K-27 Sarvam: STALE and worse. Register says "try /download-url". Agent 1 already used get_download_links: 12/12 ForbiddenError (DISPATCH_LOG.md:757), then fresh calls 3/3 401, key dead (:?§38). 0/12 predictions retrievable. Close: boss gets a new key and approves re-run of 12 South calls (about Rs 6, NEXT.md REV 6) and saves outputs at submit time; or drop the Sarvam-South column. Owner: boss.
- K-28 Concerns in graph: PARKED. No graphify-out. Owner: agent when unparked.
- K-29 Sep-16 correction: OPEN. Reference only on branch claude/stoic-keller-xwovqu; not reproduced in repo. Close: reproduce the 26-page legacy-font count in S5 and give boss the one-paragraph note. Owner: agent then boss.
- K-30 Time budget: OPEN. RUN_STATE dir absent. Surya 24 s/page, 36 h est. is in the register only. Close: latency table at GPU day 1. Owner: agent.

## Cross-cutting findings
- The register's Part 0 is stale vs W4/DISPATCH (K-27, K-03, K-14, K-09). Planner should re-sync Part 0 or mark verified dates per row.
- 30 themes: CLOSED 1 (K-14), STANDING 5 (K-07, K-13, K-16, K-18, plus K-10 parked), PARTIAL 10, OPEN 11, BLOCKED 1, PARKED 2. Winning is blocked by K-03/K-04/K-26, none of which is agent-closable alone.
- Missing files that Part 0 treats as owed: GT_DEFECTS.md, EMPTY_OUTPUT_DIAGNOSIS.md, RUBRIC_REPORT.md, rubric_report.py, SUBMISSION_DRYRUN.md.
