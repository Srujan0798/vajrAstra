import glob, json, os, sys
R='/Users/srujansai/Desktop/South/'
M='/Users/srujansai/.claude/projects/-Users-srujansai-Desktop-South/memory/'
L7=R+'docs/research/level7/'
C=R+'docs/campaign/'
CK=C+'checkpoints/'
P=[
 ('P01','level7 decision docs A: kill criteria, final verdict, W5 freeze agenda, W6 QLoRA spec, santa method',[L7+x for x in ['KILL_CRITERIA.md','FINAL_VERDICT_2026-09-27.md','W5_FREEZE_AGENDA.md','W6_QLORA_SPEC.md','SANTA_METHOD_FINAL.md']]),
 ('P02','level7 decision docs B: hostile pass, engine spotcheck, human spotcheck, fix specs, agent prompts',[L7+x for x in ['H48_HOSTILE_PASS.md','H48_ENGINE_SPOTCHECK.md','HUMAN_SPOTCHECK_PACKET.md','FIX_SPECS_FOR_MISS.md','FIX_SPECS_R2_LEADERBOARD.md','PROMPT_ENGINE_AGENT.md','PROMPT_MISS_AGENT.md','PROMPT_VERDICT_AGENT.md']]),
 ('P03','validation-call packet (Sep 28-29)',[L7+'CALL_PACKET.md']),
 ('P04','Miss monitor log (campaign monitoring)',[L7+'MISS_MONITOR.md']),
 ('P05','boss directives Sep 28 (handoff, session directives, call cheatsheet/script, parallel work)',sorted(glob.glob(L7+'boss_directives/*.md'))),
 ('P06','Lane A OCR/DocAI SOTA ledger part 1 (lines 1-2360) + manifest',[L7+'a/LEDGER.md#1-2360',L7+'a/MANIFEST.md']),
 ('P07','Lane A OCR/DocAI SOTA ledger part 2 (lines 2361-4720)',[L7+'a/LEDGER.md#2361-4720']),
 ('P08','Lane A OCR/DocAI SOTA ledger part 3 (lines 4721-end)',[L7+'a/LEDGER.md#4721-7069']),
 ('P09','Lane C1 NVIDIA/serving/quant ledger + notes',[L7+'c/c1/LEDGER.md']+sorted(glob.glob(L7+'c/c1/NOTE_*.md'))),
 ('P10','Lane C2 competition ledger + C3 data strategy',[L7+'c/c2/LEDGER.md',L7+'c/c3/STRATEGY.md']),
 ('P11','Lane C3 data-collection ledger',[L7+'c/c3/LEDGER.md']),
 ('P12','Lane C4 tooling ledger + transfer obituaries + format',[L7+'c/c4/LEDGER.md',L7+'c/c4/OBITUARIES.md',L7+'c/c4/LEDGER_FORMAT.md']),
 ('P13','Lane B3 orchestration + B4 agent tooling research',sorted(glob.glob(L7+'b/b3_multi_agent_orchestration/*.md'))+sorted(glob.glob(L7+'b/b4_agent_tooling/*.md'))),
 ('P14','Lane B5 elite repos research',sorted(glob.glob(L7+'b/b5_elite_repos/*.md'))),
 ('P15','campaign core 1: campaign directive v5, 22-language benchmark, competitor intel',[C+'CAMPAIGN_DIRECTIVE.md',C+'BENCHMARK_22.md',C+'COMPETITOR_INTEL.md']),
 ('P16','campaign core 2: edge thesis, mentor playbook, multi-LLM eval, ChatGPT eval prompt, sampling plan',[C+x for x in ['EDGE_THESIS.md','MENTOR_PLAYBOOK.md','MULTI_LLM_EVAL.md','CHATGPT_EVAL_PROMPT.md','SAMPLING_PLAN.md']]),
 ('P17','campaign analyses: test-set profile, B01/B02/B12, Bodhan baseline, Vinay call+GPU, skill stack, sheet forensics, explainer, HF access, monitor, audits, drafts',[C+x for x in ['TEST_SET_PROFILE.md','B01_4BIT_ANALYSIS.md','B02_ARABIC_NORMALIZATION.md','B12_HANDWRITING_SHARE.md','BODHAN_BASELINE.md','VINAY_CALL_AND_GPU_DAY1.md','SKILL_STACK.md','P4_ELITE_SEQUENCING.md','SHEET_V2_FORENSICS.md','VAJRASTRA_SHEET_AUDIT.md','BOSS_EXPLAINER.md','HF_ACCESS_REQUEST.md','H3_ISSUE_CLEANUP.md','MONITOR_2026-09-30.md']]+sorted(glob.glob(C+'audit/*.md'))+sorted(glob.glob(C+'drafts/*.md'))),
 ('P18','draft research plan (Plan v3) + research decisions register + W2/W3 checkpoints + NEXT',[C+'DRAFT_RESEARCH_PLAN.md',C+'RESEARCH_DECISIONS.md',CK+'W2.md',CK+'W3.md',CK+'W2_reports/variance.md',CK+'W3_reports/inventory.md',CK+'NEXT.md']),
 ('P19','W1 checkpoint + 1F one-pager + PROTO86 verify',[CK+'W1.md',CK+'W1_reports/1F_onepager.md',CK+'W1_reports/PROTO86_VERIFY.md']),
 ('P20','W1 edge hunt + 3 adversarial lenses',[CK+'W1_reports/'+x for x in ['1E_hunt.md','1E_lensA.md','1E_lensB.md','1E_lensC.md']]),
 ('P21','W1 multi-LLM eval (Sonnet leg) + 1G apply-verify',[CK+'W1_reports/1F_sonnet.md',CK+'W1_reports/1G_verify.md']),
 ('P22','W1 draft-plan verification rounds 1 and 2',[CK+'W1_reports/1H_verify.md',CK+'W1_reports/1H_verify_round2.md']),
 ('P23','W4 checkpoint (current lane log incl. RQ-1, Gate 1, S5, H2, GOLD W0)',[CK+'W4.md']),
 ('P24','W4 research: RQ-1 official rules + RQ-9 licences',[CK+'W4_reports/RQ1_official_rules.md',CK+'W4_reports/RQ9_licences.md']),
 ('P25','W4 A-step reports + blind verifies + South rerun reports',[CK+'W4_reports/'+x for x in ['A1_preimage.md','A1_verify.md','A3_layout.md','A3A4_verify.md','A4_paths.md','A6_recovery.md','PROTO66_VERDICT_CHECK.md']]+sorted(glob.glob(CK+'W4_reports/blind_verify_*.md'))+sorted(glob.glob(CK+'W_south_reports/*.md'))),
 ('P26','A6 staging (verdict fix specs, leaderboard, abstention, mcnemar, santa cross-check) + cloud-session concern ledger',sorted(glob.glob(CK+'W4_reports/A6_staging/*.md'))+[CK+'CONCERN_LEDGER_CLOUD_SESSION_2026-09-30.md']),
 ('P27','planner handoffs + monitor',[CK+'HANDOFF_PLANNER_2026-09-30.md',CK+'HANDOFF_PLANNER_CLOSE_2026-09-30.md',CK+'MONITOR_2026-09-30.md',M+'handoff-2026-09-30-planner.md',M+'handoff-2026-10-01-planner-close.md']),
 ('P28','root: Vinay meeting packet, live-latest research, paperthin audit',[R+'VINAY_MEETING_PACKET.md',R+'LIVE_LATEST_2026-09-29.md',R+'PAPERTHIN_AUDIT.md']),
 ('P29','root: loop spec, integrated elite stack, W5 freeze plan, project complete, 18-lang sample plan',[R+x for x in ['LOOP_SPEC_W5_W6_W7.md','INTEGRATED-ELITE-STACK.md','W5_FREEZE_PLAN.md','PROJECT_COMPLETE.md','SAMPLE_PLAN_18_LANGS.md']]),
 ('P30','root: full technical briefing, South canon, ultimate hybrid concern',[R+'FULL TECHNICAL BRIEFING.md',R+'SOUTH_CANON.md',R+'level2/ULTIMATE_HYBRID_CONCERN.md']),
 ('P31','root misc: audit report, protocol upgrades, cleanup log, README, HOW_TO_RUN, docs index/plan, PPT spec',[R+x for x in ['AUDIT_REPORT.md','PROTOCOL_UPGRADES.md','CLEANUP_EXECUTION_LOG.md','README.md','HOW_TO_RUN.txt','docs/INDEX.md','docs/PLAN.md','docs/architecture/PPT_SPEC.md']]),
 ('P32','BOSS_CONCERNS (all boss concerns, Part 0 merged list)',[R+'BOSS_CONCERNS.md']),
 ('P33','DISPATCH_LOG (all agent dispatches and results)',[R+'DISPATCH_LOG.md']),
 ('P34','QLoRA/W6 benchmark docs + training assets + synthetic lines spec',sorted(glob.glob(R+'docs/benchmark_docs/*.md'))+[R+'level2/training_assets/README.md',R+'product/docs/B21_SYNTHETIC_LINES_SPEC.md']),
 ('P35','level2 benchmark docs: agent protocol, final report, leaderboard refresh, transfer obituaries, w6 feasible set',[R+'level2/benchmark/docs/'+x for x in ['AGENT_PROTOCOL.md','FINAL_REPORT.md','LEADERBOARD_REFRESH_2026-09-29.md','transfer_obituaries.md','w6_feasible_set.md','w6_set_construction_log.md','verify_unaccounted.md','README.md','orchestrator_briefing_template.md']]+[R+'level2/benchmark/scores/mcnemar_summary.md']),
 ('P36','level2 benchmark docs: memory audit/reclaim, MLX install, W1H plan fixes, W1 round-2 meeting-day fixes',[R+'level2/benchmark/docs/'+x for x in ['MEMORY_AUDIT.md','MEMORY_RECLAIM_RESULT.md','MLX_INSTALL_RESULT.md','fix_specs/W1H_PLAN_FIXES.md','fix_specs/W1_ROUND2_MEETINGDAY.md']]),
 ('P37','W1A packet audit (54 fix-specs)',[R+'level2/benchmark/docs/fix_specs/W1A_PACKET_AUDIT.md']),
 ('P38','level2 README + research gates + South external benchmark map + empty pages + licence audit + probe schema + engines README',[R+'level2/README.md',R+'level2/research/README.md']+sorted(glob.glob(R+'level2/research/gates/*.md'))+[R+'docs/south/EXTERNAL_BENCHMARK_MAP.md',R+'docs/south/EMPTY_PAGES.md',R+'docs/legal/LICENSE_AUDIT.md',R+'docs/probe/W3_PROBE_SCHEMA.md',R+'level2/engines/README.md']),
 ('P39','per-engine docs (PROMPT/RUN for 11 engines)',sorted(glob.glob(R+'level2/engine_docs/*/*.md'))),
 ('P40','reports research: Level7 findings, protocol-1 research (Gemma-4 protocol), vajrAstra interrogation protocol',[R+'_reports/research/LEVEL7_RESEARCH_FINDINGS.md',R+'_reports/research/PROTOCOL_1_RESEARCH.md',R+'_reports/research/VAJRASTRA_INTERROGATION_PROTOCOL.md']),
 ('P41','reports analysis: duplicate map, file inventory, MD consolidation plan, memory consolidation, memory final',sorted(glob.glob(R+'_reports/analysis/*.md'))),
 ('P42','THE 3 CONSENSUS deep searches (~100 papers): model+training, hard scripts/handwriting/degraded, system/layout/post-correction/langid/eval',sorted(glob.glob(R+'docs/sources/consensus/*.tex'))+[R+'docs/sources/consensus/README.md']),
 ('P43','ULTIMATE MASTER DIRECTIVE v3 (uni_v3) + docs dedup research',[R+'docs/research/uni_v3_ORIGINAL_2026-09-29.md',R+'docs/research/DEDUP_DOCS_RESEARCH.md']),
 ('P44','memory: THE plan files — proto-104 project-first rev4, proto-108 plan v4, proto-106 Vinay call+GPU day1, proto-89 plan v3',[M+x for x in ['proto-104-project-first-critical-path.md','proto-108-plan-v4-final.md','proto-106-vinay-call-and-gpu-day1.md','proto-89-plan-v3-bodhan-base.md']]),
 ('P45','memory: research->build B-01..B-21, research still to do RQ-1..12, consensus->decisions, measured facts F1-F82, boss decisions U-rows/C1-C15',[M+x for x in ['proto-100-research-to-build.md','proto-97-research-still-to-do.md','proto-105-consensus-results-to-decisions.md','proto-93-measured-facts.md','proto-92-boss-decisions.md']]),
 ('P46','memory: concern crosswalk K-01..K-30, meetings verbatim, law & guardrails, skill routing, boss rules, user profile, explainer',[M+x for x in ['proto-99-concern-crosswalk.md','proto-103-meeting2-verbatim-truth-and-application.md','proto-01-law-and-guardrails.md','proto-88-skill-routing.md','boss-rules.md','user-profile.md','proto-85-boss-explainer-and-question-bank.md']]),
 ('P47','memory: history of 26 completed protocols (verbatim)',[M+'history-completed-protocols.md']),
 ('P48','memory: clean-repo master proto-98 (parked) + incident repair proto-102 + gold consolidation proto-107',[M+x for x in ['proto-98-clean-repo-master.md','proto-102-incident-repair-and-verdict-fixes.md','proto-107-gold-repo-consolidation.md']]),
 ('P49','memory: small protocols (60-91), runbook, preflight, campaign law, boss standard, model tiering, conflicts register, feedback files',[M+x for x in ['proto-00-runbook.md','proto-02-preflight-and-checkpoints.md','proto-60-monitor-and-checkpoint-discipline.md','proto-62-gt-tier-stratified-reporting.md','proto-65-gt-defects-register.md','proto-71-south-rerun-same-standard.md','proto-75-vinay-plan-baseline.md','proto-76-workstreams-and-agent-health.md','proto-78-submission-readiness.md','proto-79-council-briefing-prompts.md','proto-80-hackathon-metric-alignment.md','proto-81-handwriting-degraded-coverage.md','proto-82-engine-empty-output-patterns.md','proto-90-templates.md','proto-91-verdict-cross-check.md','campaign-law.md','boss-standard.md','model-tiering.md','conflicts-register.md','agent-automation-setup.md','feedback-no-subagents-boss-assigns.md','feedback-no-team-mates.md']]),
 ('P50','ECC memory notes written by agents (decisions, facts, handoffs, runbooks)',sorted(glob.glob(R+'.ecc/memory/**/*.md',recursive=True))),
]
out=[];bad=[]
for pid,focus,files in P:
    fl=[];tot=0
    for f in files:
        path,rng=(f.split('#')+[None])[:2]
        if not os.path.exists(path): bad.append(path); continue
        tot+=os.path.getsize(path) if not rng else 0
        if rng:
            a,b=map(int,rng.split('-')); 
            with open(path,encoding='utf-8',errors='replace') as fh: lines=fh.read().split('\n')
            tot+=sum(len(l.encode())+1 for l in lines[a-1:b])
        fl.append(f)
    out.append({'id':pid,'focus':focus,'files':fl,'bytes':tot})
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False)
for o in out: print(o['id'],len(o['files']),o['bytes'])
print('MISSING:',bad)
print('TOTAL bytes',sum(o['bytes'] for o in out), 'files', sum(len(o['files']) for o in out))
