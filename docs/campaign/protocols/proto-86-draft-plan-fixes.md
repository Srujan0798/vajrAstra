---
name: proto-86-draft-plan-fixes
description: "Added 2026-09-30 (meeting day, URGENT) — 13 verified defects the Opus monitor found in docs/campaign/DRAFT_RESEARCH_PLAN.md (what the boss presents to Vinay today): GT-tier omission, Option A/D table swap, the Punjabi K1 contradiction, already-answered questions, missing licence/handwriting/submission/rubric facts; Verdict writes fix-specs, Miss applies"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T22:10:57.898Z
---

# PROTO-86 — FIX THE DRAFT RESEARCH PLAN BEFORE THE MEETING (Verdict specs → Miss applies → Verdict verifies; max 2 rounds)

Target: `docs/campaign/DRAFT_RESEARCH_PLAN.md` (written 2026-09-29 03:11 IST, before several monitor findings). The document is strong and honest; these defects remain.
Method: [[proto-18-w1g-apply-verify]] (pre-image to `_archive/pre_fix_2026-09-30/`, exact-string fix-specs in `level2/probe22/fix_specs/W1H_PLAN_FIXES.md`). Keep ≤4 pages: replace, don't pile on.

| # | Section | Defect (monitor-verified 2026-09-30) | Required change |
|---|---|---|---|
| D1 | §3 | Shows "surya lower in 10 of 18" without the GT-tier split | Add the 3-row table from [[proto-62-gt-tier-stratified-reporting]] (human pair n=9: Sarvam 0.064 vs best local 0.243 · PDF layer n=36: 0.311 vs 0.229 · bench n=9: 0.278 vs 0.617) and the one-liner: our engines lead only on PDF-text-layer GT |
| D2 | §5 table | Option A column lists "R4 restoration + Sarvam API subsidy" — those are Option D's parts; A per `docs/architecture/W5_STRATEGY_OPTIONS.md` / packet = wrap-only routing (+ QLoRA kok+pa) | Rewrite both columns from the two strategy docs verbatim; keep the recommendation logic |
| D3 | §2 flowchart K2 node / §5 | Flowchart says Punjabi fails (p=1.00) while `docs/research/level7/KILL_CRITERIA.md:56` and feed §12.2 say "pa SURVIVES K1, p<0.0001, 88 discordant". **Monitor check of `level2/probe22/scores/mcnemar_full_matrix.json`: surya vs tesseract_indic on pa = n 90, ties 87, discordant 3 (1 vs 2), p=1.0 → TIE.** The 88 belong to other engine pairs. KILL_CRITERIA is wrong; Option A's QLoRA scope shrinks to **kok only** | State it plainly in §5: "Punjabi does not pass K1 (tie, p=1.0); QLoRA scope would be Konkani only." Verdict writes an ERRATUM fix-spec for KILL_CRITERIA.md:56 and a feed §11 erratum for §12.2 (append-only) |
| D4 | §3/§5 | "Significant" is used without its definition | Add: McNemar pass = CER < 0.5 per item (`mcnemar_full_matrix.json` meta `cer_threshold: 0.5`) |
| D5 | §8 | Asks questions the boss already answered on 2026-09-30 | Replace with DECIDED lines: download of Ol Chiki/Meetei Tesseract models = YES after licence check (U7); §6.4 mni/sat = re-verify with a human (U6); level2 physical restructure = YES after the meeting (U10); South re-run = YES, feasibility first (U11). Keep U1, U2, U4, U5 as open questions |
| D6 | §4 item 6 | "UNVERIFIED: we did not open its file listing" | Update from 1D/web: the indic-ocr project states its tessdata includes Ol Chiki and Meetei Mayek (github.com/indic-ocr/indic-ocr.github.io); licence still to verify before download |
| D7 | §6 | "tessdata/ has none of sat, mni, kan, mal, tam, tel" and "one typeface each" | Correct: `level2/probe22/tessdata/` lacks them, but `/opt/homebrew/share/tessdata/` has kan/mal/tam/tel and `level2/research/smoke/anuvaad_tesseract/tessdata/` has anuvaad_kan/mal/tam/tel; macOS ships Noto Sans Meetei Mayek + October Meetei Mayek (several weights). Ol Chiki font count: re-check with `fc-list \| grep -i chiki` |
| D8 | new §3 bullet | **CORRECTED 2026-09-30 by factchk:** the "CER + bootstrap CI + WER + S/D/I + seconds/page" rubric came from a STUDENT project repo, not the official hackathon — DO NOT write it as the hackathon's rubric | Write instead: "The official scoring rules are not public; we will report CER with confidence intervals, WER, error types and seconds per page anyway (proto-80) and ask the organisers." |
| D9 | new §3 bullet | Missing: **coverage gap** — all 1,283 probe items are printed (0 handwritten, 0 tables; 983 quality "unknown"); the hackathon's description reportedly mentions handwritten and low-quality documents (UNVERIFIED — official page not opened; the test set itself will tell us, proto-81 step 2) | One sentence, labelled unverified + question U13 in §8 |
| D10 | new §5 bullet | Missing: **surya licence** — our best engine's weights are under a modified OpenRAIL-M "free for research, personal use, and startups under $5M funding/revenue" (`docs/legal/LICENSE_AUDIT.md`, surya METADATA line 99). Vinay is the CEO; this is a business decision | One sentence + question U14 in §8 |
| D11 | §9 | 5-day plan has no submission path for the 5,344 unlabelled test images (script ID → route → engine → output) | Add one row per [[proto-78-submission-readiness]]; note IndicPhotoOCR ships a CLIP script identifier on disk (`.deps/IndicPhotoOCR/.../script_identification/CLIP_identifier.py`, weights licence TODO) |
| D12 | §3 | "Kok … on the one language where Sarvam is 97.41" mixes Sarvam word accuracy with our CER after §1 says they are not comparable | Move to a footnote labelled "different metric, context only" or delete |
| D13 | §7 | OpenCode leg "could not run" | Add: the leg can be run from any Claude Code session that has the `opencode` MCP (proto-17 §2), or by the boss pasting `CHATGPT_EVAL_PROMPT.md` into OpenCode; ChatGPT paste still pending |

## STATUS 2026-09-30 05:15 (monitor-verified) — do the OPEN rows now, before the meeting
DONE: D1 (plan line 91), D2 in the plan, D13 (OpenCode mentioned). **OPEN:** D2 in the packet · **D3 — RESOLVED by evidence, not "UNRESOLVED": write "Punjabi fails K1 (tie, p=1.0, 3 discordant of 90) → QLoRA scope Konkani only" in the plan (line 50/60) AND fix every packet line that says Konkani + Punjabi survive/recommended (VINAY_MEETING_PACKET.md lines 44, 120, 129, 195, 218, 220, 226) AND erratum for KILL_CRITERIA.md:56 (append-only note)** ·
D4 · D5 (write the DECIDED U6/U7/U10/U11 lines) · D6 · D7 · D8 · D9 · D10 · D11 · D12.

## STATUS 2026-09-30 05:12 — spec written (`fix_specs/W1H_PLAN_FIXES.md`), NOTHING APPLIED yet
Apply every row now (pre-image → exact-string edits → Verdict re-verify) to the plan AND the packet (lines 44, 120, 129, 195, 218, 220, 228 → Konkani-only), then append ERRATUM-K1 (KILL_CRITERIA note) and
ERRATUM-F1 (feed §11 line). Correct D11 in the spec: the test set is `Datasets/akshardrishti_official/test/test/` = 5,344 JPEGs (`find … -type f`); 20,656 was the whole dataset.
"Done" = the grep checks in the monitor report return hits in the plan and 0 remaining "Konkani + Punjabi" recommendations in the packet.

## After applying
Verdict re-verifies every changed number against its source; re-run the word count; add one line at the top: "Revised 2026-09-30 per fix_specs/W1H_PLAN_FIXES.md". Mirror the Punjabi finding into `VINAY_MEETING_PACKET.md` (fix-spec) because the packet's Option A still says "Konkani + Punjabi".
**Deadline guard (ULTIMATE_HYBRID_CONCERN L12/D12):** inside 4 hours of the meeting, only these fixes — no new scope.

Related: [[proto-64-meeting-day-finish]], [[proto-62-gt-tier-stratified-reporting]], [[proto-80-hackathon-metric-alignment]], [[proto-83-licence-verification]], [[proto-92-boss-decisions]]
