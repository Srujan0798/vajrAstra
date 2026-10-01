# A10-REDTEAM — hostile review of Plan v4 rev 2 (+proto-111, proto-110, NEXT.md)
Paths relative to /home/user/boss. P108 = _claude_memory/proto-108-plan-v4-final.md. Today = 2026-10-01.

## 1. Date evidence (every one found; deadline is UNKNOWN, not "far")
- Official timeline: 12 rows, only 2 dated: launch 12/02/2026 and "Pitch Screening Session 23/07/2026"; the other 10 are TBD (docs/campaign/checkpoints/W4_reports/RQ1_official_rules.md:113-126; W4.md:15).
- 23/07/2026 is 70 days in the past. The plan never asks which stage we are in (Stage 1 passed? Stage 2 initial prototype due?). Stage 2 "initial prototype" and Stage 3 "final prototype" dates are TBD (RQ1:123,126). The deadline can be tomorrow; no document rules that out.
- Registration was extended to 30 March 2026 (RQ1:380-381), so the process is 6 months old; "no deadline exists" (W4.md:15) means "unpublished", not "none".
- Oct 4, Oct 15, "qualifiers 30/09" are void: 30/09 is Rajasthan (RQ1:133-157); Oct 4/15 have no source (RQ1:169-171). BOSS_CONCERNS.md:511 still carries "#55 W6 training Oct 2-8" as PENDING (stale internal date).
- proto-103: Vinay "expect 10 days" for an unconfirmed subject (proto-103:61); GPU "arriving 2026-10-01" (proto-103:60); next call 2026-10-01 morning (proto-103:63). proto-111:32 shows the call happened.
- W4.md 2026-10-01 dated blocks (A4/A6/S2/S5/GOLD W0) show the team spent 09-30 to 10-01 on repo hygiene (e.g. W4.md:799-806, 172 MB bundle), not on results.
- RQ1 itself says the single highest-value action is emailing gic.dibd@gmail.com for the rubric and Stage-2 date (RQ1:480-482). P108:351 demotes it to a "boss decision U-ORG" behind Vinay's consent. NEXT.md ranks the unknown deadline #4 of 8 blockers (NEXT.md:6).
- Conclusion: plan the whole thing as "ship a demoable submission in ~5-7 days, then extend". Anything not producing a number or a demo in that window is cut.

## 2. What will most likely make the team lose (ranked)
1. NO ARTEFACT TO SUBMIT. NEXT.md:5 says 0 models trained, 0 HW baselines, 0 Bengali HW data, HW0 never run, 16/5,344 images viewed, product dry-run used Tesseract only. A product-weighted jury (P108:26) scores a demo + pitch; the current deliverable is protocols and Claude Docs.
2. Serial gate chain before any result: HW-ID -> HW0 -> HW1 -> G-2.5 -> HW-SMOKE -> HW2 (P108:175-189). G-2.5 (P108:185, :47) = multi-LLM review of the plan + 15-20 min Vinay session + GPU-hour cap, and it is the ONLY training gate. It depends on one human's calendar. Train-able data (IIIT bn, U-HW1) also waits on the boss's download approval. Result: zero training until some unknown date.
3. GPU not in hand: SSH login missing (P108:320, NEXT.md:6 blocker 3). Plan itself says Mac MPS PARSeq is feasible (P108:321) but demotes it to "dev path". That fallback IS the minimal path if GPU slips.
4. Premise risk on the one scoring item: the test file is "5,344 unlabelled handwritten word crops", only 16 viewed, all Bengali (P108:27-29). Whole Track A bets on "Bengali". If it is a mix, HW2 (Bengali-only, P108:189-190) fixes the wrong thing. HW-ID is therefore genuinely P0 and cheap; it is correctly first, but is blocked behind agents' queue.
5. Honest-but-losing pitch: P108:40-41 says Sarvam is 2.51x better than our best local engine on verified printed items; "all four printed edges killed" (P108:108). Track B cannot win; it only exists as a story. The plan does not say what the 3-minute demo shows if HW2 misses G-HW2 (>=85% independent-writer WRR; P108:200). A kill-gated plan with no "failed gate" demo is a plan to show nothing.
6. Process theatre eats the days: proto-110 K0-K8 (146 lines), proto-111 L0-L4, sync A, licence ledger for ~10 weights, 25-question jury drill, EXPLAIN_CARD. Each is defensible; together they are weeks of work for 1 operator.
7. Licences OPEN on exactly what the path ships: Bodhan weights (P108:310), IndicPhotoOCR/STocr weights (P108:313), IIIT licence (P108:314). K-SHIP says an open row blocks shipping (P108:307). Not fatal for a prototype demo, fatal if left to last day.
8. Unverified base: Bodhan PyTorch parity blocked and O-1 (page CER 0.69 vs crop 0.054) unexplained (P108:103-104, 364). The "Page Expert" half of the architecture is unproven; the product pitch rests on it.

## 3. Over-engineering vs time left (cite = where)
- Statistical apparatus on a set whose metric is unknown: pre-registered kill table with 10 kills (P108:294-307), paired McNemar + >=3 pt promotion rule (P108:201), n>=300 writer-disjoint claim gate (P108:200), CI on everything (P108:286). Good science, but the official metric is "UNKNOWN" (P108:363); thresholds 92/85 are admitted proxies. Keep: one scorer + CER/WRR + n. Defer: paired tests, tiers, sampling proofs.
- Per-cell Track B recipes sat/mni/ks/or/sa/kok/R4 (P108:219-245) with R4 restoration 4 arms, QARI-style Nastaliq synth, Ol Chiki synth. Plan itself says Track B "does not move the test score" (P108:205). This is ~30 lines of roadmap pretending to be a work queue.
- proto-111 layout/LID: its own header says HOLD and "moves nothing on the test file" (proto-111:9-16). Yet NEXT.md:4 lists it as protocol and P108 section 2 routes via Bodhan layout. Correct move: freeze. Do not run L0 either (proto-111:12 allows it): same-script LID is "unsolved research" (proto-111:18).
- proto-110 knowledge canon: 9 waves, sha ledger, blind verify >=15%, 10-question fresh-agent exam, symlink/stub/link fixing (proto-110:92-124). It is a repo-tidy project with zero effect on score or demo, assigned to an agent that could be running HW1. Also conflicts with proto-107 (Agent 3, proto-110:131-134). Cut entirely until after submission; at most keep NEXT.md + proto-108 top section as the "canon".
- Reading overhead: an agent must read P108 top (~345 lines) + proto-104 + 89 + 107 + 106 + 109 + W4 (800+ lines) per task. The paste lines (P108:355-357) are paragraph-long. Plan v4 is too long to be executable; the playbook should be <100 lines.
- Hard-rule density: Sonnet-only, read-only subagents, one mutator, sha manifest + bundle before any move, no `2>/dev/null`, locked files (NEXT.md:14; proto-110:126-135). Each rule is a past-incident fix, but together they make every step cost 2-3x.
- Claim-law R-12/R-7/HL7 etc. matter only if we publish comparisons. For the pitch we can simply publish own-split numbers labelled directional.

## 4. Too heavy for a solo operator + 3 agents
- Operator-bound items (each can stall the chain): U-HW1 download approval, U-HW2, U-HW3 / G-2.5 + Vinay session + GPU-hour cap, U-TESS, U-ORG, O-2, O-3, GO-A/D/G, U14/27/28 (P108:346-352). That is ~12 human decisions; plan has no default-on-timeout rule.
- G-2.5 requires "OpenCode + fresh hostile Sonnet + ChatGPT paste" with a data package (P108:185). Replace by this red-team + one Vinay message; the operator is the gate, not a committee.
- Agent 2 is loaded with: licence rows for 9 artefacts, HW0 script, G-2.5 package, law-chain edit, S5 South scoring, Q GT_DEFECTS.md, blind verification of proto-110 (P108:356; NEXT.md:12; proto-110:105). Agent 2 is the critical path to HW0 and G-2.5 yet is the busiest. Agent 3: proto-107 gold repo W0-W4 + 50-image dry run + rename (P108:357; NEXT.md:12) - repo tidying on the critical path of nothing.
- Agent 1 does HW-ID (300 images vision-checked by eye), HW1, SMOKE, HW2, HW3 and proto-111 L1 (proto-111:109): serial single worker on the only score-moving track.
- 300-image visual audit (P108:176) is heavy by hand; 100 stratified images would settle "mostly Bengali single words" (K-ID threshold 80%) with a CI of about +/-8 pts. Use 100, extend only if borderline.
- Data/privacy: data moves "by rsync, never GitHub" (P108:329) and sync A pushes docs only; fine, but every sync step is operator time.

## 5. Single minimal winning path (cut list = everything else)
Goal: by day ~5 have (a) a Bengali word-crop recogniser with a number on a held-out set, (b) a running CLI that turns the 5,344 crops into image,text CSV + JSON, (c) a 5-min pitch/demo deck + one-page cost/licence story.
Order, each with a default if the human is silent for 24 h:
1. Today: operator emails gic.dibd@gmail.com (metric, Stage-2 date, which stage we are in) and messages Vinay "which stage are we in / is anything due". Do not wait on answers. (RQ1:480-482)
2. Today, Agent 1: HW-ID on 100 crops (P108:175-177 reduced). Output HW_ID_AUDIT.md. If >=80% single Bengali words -> proceed; else stop and tell operator.
3. Today, operator: approve U-HW1 (IIIT bn from AIKosh, CC-BY, P108:131,347). Agent 2: read the AIKosh licence line + zip README only (1 licence row, not 9). Default = proceed on CC-BY if the page says so.
4. Today/tomorrow, Agent 2: HW0 pHash+SHA script on 5,344 vs IIIT bn (P108:178-180). Drop the code sweep unless time remains.
5. Agent 1: HW1 zero-shot with IndicPhotoOCR bengali PARSeq + Bodhan HW on 200 viewed crops and IIIT bn val subset (P108:181-184). This is the fallback submission and it already exists locally.
6. Replace G-2.5 with a 2-line sign-off: operator writes thresholds (92 / 85 as proxies), and sends the plan top-section + this file to Vinay on WhatsApp. If no reply in 24 h, proceed and say so in the pitch. (Law change recorded in W4.md; P108:47,339.)
7. Agent 1: one fine-tune run, PARSeq from bengali.ckpt on IIIT bn train, on the 24 GB GPU if the login exists, else Mac MPS (P108:189-192, 321). Single run, select on IIIT val, no LM rescoring, no HW3, no synth pretrain.
8. Agent 1/2: if val WRR beats HW1 zero-shot by a visible margin on the same val set (simple CI, skip McNemar) ship the adapter; else ship zero-shot. Write numbers with set/n/CI once (P108:286 items 1-2 only).
9. Agent 3 (stop proto-107 at W2): the product CLI on the 5,344 crops -> `image,text` CSV + per-image JSON (P108:159), CPU dry-run on 50 images with s/image and RAM, pinned torch, Dockerfile, NOTICE (P108:157-158, 259). Page path = Bodhan as is, explicitly labelled "prototype, not claimed".
10. Operator + Claude: demo = handwriting crops -> text with confidence and abstain flag; pitch lead = governance/archive use (P108:258), cost anchors (P108:263), honest claims only (P108:272). One slide per official criterion (P108:257-262).
KEEP from the plan: the evaluation law items 1-2, the claims allowed/never list (P108:271-278), HW0 leak check, HW-ID, licence rows for Bodhan/IIIT/STocr only.
CUT (until after submission): proto-110 entirely; proto-111 entirely (incl. L0); proto-107 W3+ ; Track B per-cell recipes sat/mni/ks/or/sa/kok/R4; HW3, HW-P2, optional RL, post-correction; transfer obituaries/sampling proofs/GT_DEFECTS/South S5; multi-LLM G-2.5 committee; 25-question drill; alternate backbones; Docs/artifact upkeep (NEXT.md:8 "both Docs updated" is effort not progress); 71-file second pass and P49/P50 verification (P108:359-365).
STOP-LOSS: if by day 3 there is no GPU and no IIIT data, ship HW1 zero-shot as the system and put the fine-tune on the roadmap slide (P108:260).

## 6. Smaller defects spotted
- P108 header line 1-3 says "rev 2 INTEGRATED"; NEXT.md has REV 8 on top with REV 7/6 below and REV 6 still names old Plan v4 paths and "W6 freeze"; the agent will read contradictions (NEXT.md:8-13). Rewrite NEXT.md to one lane per agent, <15 lines.
- P108:285 "sheet.csv never presented as checkable (62.9% of rows don't re-derive)" - good, but scorer is a prerequisite for every number; confirm it exists and runs before HW1 (not listed as a step).
- P108:195 "expected-score statement mapping proxies to the unknown metric" is guesswork; drop.
- P108:172 uses Gujarati Bodo/gu as wiring test with paths broken (P108:61); do not spend time fixing it; use IIIT bn val once downloaded.
- P108 section 12 paste lines are truncated in the file view only because of my 380-char cut; verify they hold the cut list above before dispatch.
