---
name: proto-78-submission-readiness
description: "Added 2026-09-30 — end goal E14.2 gap: nothing plans how the system runs on the hackathon's 5,344 unlabelled test images (Datasets/akshardrishti_official/test/test); submission format unpublished; language/script ID needed for routing; throughput; dry run without training on test"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:54:43.565Z
---

# PROTO-78 — SUBMISSION READINESS (Engine builds, Verdict verifies; gated on U2 for format)

**Why:** uni E14.2 "COMPLETE the project". `Datasets/akshardrishti_official/test/test/` = 5,344 unlabelled JPGs (numbered `0.jpg`…), described in `FULL TECHNICAL BRIEFING.md:37` as the
hackathon eval set — "NEVER train on it". `docs/research/R6_COMPETITION_INTEL.md:62` "Submission format — NOT published". Every plan so far routes by a KNOWN language label (per-language
routing table); the test images carry no label → the pipeline needs script/language identification first. No protocol covered this.

## Step 1 — requirements (Miss) → `docs/campaign/SUBMISSION_REQUIREMENTS.md`
Collect everything known about the submission: output format, metric, languages in test, deadline, page vs block unit, file naming. Sources: official hackathon pages (live, opened),
`SOUTH_CANON.md`, `FULL TECHNICAL BRIEFING.md`, `R6_COMPETITION_INTEL.md` §4, `_reports/research/VAJRASTRA_INTERROGATION_PROTOCOL.md` F1, the boss (U2). UNKNOWN is allowed; list questions for the boss/Vinay.

## Step 2 — test-set profile (Engine, read-only, no training, no labels created)
Sample 200 test images (seed 20260926): image sizes, colour/greyscale, printed vs handwritten (visual check of 30), and **script distribution** estimated by running the existing engines'
script detection or a Unicode-block vote over 2–3 fast engines' outputs on the sample. Output `docs/campaign/TEST_SET_PROFILE.md`. Never write predictions for the test set into any training asset.

## Step 3 — pipeline dry run (Engine)
For the chosen path (U4): script/language ID → route → engine(s) → normalisation → output writer in the (assumed) format. Run on 50 test images: wall time per image per engine on this Mac,
failure modes, memory. Extrapolate to 5,344. Output `docs/campaign/SUBMISSION_DRYRUN.md` with the exact command, timings, and the gap list (e.g. no engine for Ol Chiki/Meetei Mayek → U7).

## Verdict check
No test image used for training or tuning; timings reproducible; format assumptions labelled ASSUMED until U2 confirms.

Related: [[proto-75-vinay-plan-baseline]], [[proto-51-w5-architecture-freeze]], [[proto-92-boss-decisions]]
