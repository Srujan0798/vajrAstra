import json,sys
S=sys.argv[1]
parts=json.load(open(S+'/partitions.json'))
plan="""Current Plan v4 (memory proto-108, 2026-10-01): official test = 5,344 images, all inspected = single HANDWRITTEN Bengali words. Handwriting Expert (PARSeq per script from local IndicPhotoOCR checkpoints + IIIT-INDIC-HW-WORDS CC-BY-4.0; ICDAR'23 Bengali best 96.10 WRR; Bodhan-HW bench bn Gemini 74.8/Bodhan 71.3/Sarvam 58.3) + Page Expert (Bodhan IndicDocLayout 33M + IndicBlockOCR Qwen3.5-0.8B; ~86.4 word-acc on Sarvam bench small_rep; CER 0.4034 vs surya 0.566 on 300 gold) + Tesseract fallback + post-correction; outputs JSON/searchable PDF/MD; portable PyTorch, MLX Mac-only. Gates: HW0 leak hash gate, HW1 zero-shot, G-2.5 Vinay OK before training, HW2 >=92% IIIT val / >=85% independent writers. KNOWN WEAKNESS (boss): it under-uses the earlier research (printed 22-language plan, weak cells sat/ks/mni/or/sa/doi, R2 Nastaliq, R3 Ol Chiki/Mayek synthetic, R4 OldScan restoration, W6 training tree, kill criteria, eval discipline, product/jury)."""
js = r"""export const meta = {
  name: 'corpus-to-plan-v4',
  description: 'Full-read 320 research files (50 partitions), fact-check every number, merge into 7 theme digests for the integrated Plan v4',
  phases: [
    { title: 'Extract', detail: 'one Sonnet reader per partition, every line read' },
    { title: 'Verify', detail: 'one Sonnet fact-checker per partition' },
    { title: 'Synthesize', detail: '7 theme digests' },
    { title: 'Critic', detail: 'coverage and gaps' },
  ],
}
const PARTS = __PARTS__
const PLAN = __PLAN__
const NOTES = '__S__/corpus_extract.md'
const THEMES = ['handwriting','printed_architecture','weak_cells','training_compute','eval_gt_leakage','product_jury_competition','decisions_ops']
const FIND = {type:'object',properties:{theme:{type:'string',enum:THEMES},claim:{type:'string'},numbers:{type:'string'},source:{type:'string'},status:{type:'string',enum:['PRIMARY','MEASURED','DERIVED','CONTRADICTION','UNKNOWN','REJECTED','DEAD','DECISION','PLAN']},date:{type:'string'},currency:{type:'string',enum:['current','superseded','unclear']},superseded_by:{type:'string'}},required:['theme','claim','source','status','currency']}
const EXTRACT = {type:'object',properties:{partition:{type:'string'},files:{type:'array',items:{type:'object',properties:{path:{type:'string'},total_lines:{type:'integer'},fully_read:{type:'boolean'}},required:['path','total_lines','fully_read']}},findings:{type:'array',items:FIND},plan_v4_gaps:{type:'array',items:{type:'string'}},contradictions:{type:'array',items:{type:'string'}},open_items:{type:'array',items:{type:'string'}}},required:['partition','files','findings','plan_v4_gaps']}
const VERIFY = {type:'object',properties:{checked:{type:'integer'},results:{type:'array',items:{type:'object',properties:{index:{type:'integer'},verdict:{type:'string',enum:['verified','corrected','not_found','superseded']},correction:{type:'string'}},required:['index','verdict']}},missed:{type:'array',items:FIND}},required:['checked','results']}
const DIGEST = {type:'object',properties:{theme:{type:'string'},established:{type:'array',items:{type:'object',properties:{fact:{type:'string'},sources:{type:'string'}},required:['fact','sources']}},decisions_current:{type:'array',items:{type:'string'}},superseded:{type:'array',items:{type:'string'}},contradictions:{type:'array',items:{type:'string'}},recommendations:{type:'array',items:{type:'object',properties:{rec:{type:'string'},evidence:{type:'string'},priority:{type:'string'}},required:['rec','evidence']}},plan_v4_gaps:{type:'array',items:{type:'string'}},open_questions:{type:'array',items:{type:'string'}}},required:['theme','established','recommendations','plan_v4_gaps']}
const CRITIC = {type:'object',properties:{missing_files:{type:'array',items:{type:'string'}},weak_themes:{type:'array',items:{type:'string'}},unverified_load_bearing:{type:'array',items:{type:'string'}},next_round:{type:'array',items:{type:'string'}}},required:['next_round']}
const RULES = 'You are a READ-ONLY worker in /Users/srujansai/Desktop/South. Skip the AGENTS.md START HERE bootstrap. Do NOT run Bash or scripts, do NOT create or edit any file. Use only Read (and Grep).'
const fileList = p => p.files.map(f => f.includes('#') ? `- ${f.split('#')[0]} (ONLY lines ${f.split('#')[1]})` : `- ${f}`).join('\n')
const extractPrompt = p => `${RULES}\nPartition ${p.id}: ${p.focus}\nRead EVERY line of these files (Read caps ~25K tokens/call: page with offset/limit until EOF; fully_read=true only if you reached the last line):\n${fileList(p)}\n\nPlan under test:\n${PLAN}\n\nExtract everything that could change the final plan: findings with exact numbers, decisions/finalisations (ID, date, later superseded?), architecture choices, training/data recipes, compute, licences, benchmark results, kills/obituaries, contradictions, open items. Each finding: one claim <=350 chars, numbers exactly as written, source = path:line. Never invent numbers. currency=superseded when a later erratum/date in these files replaces it (name it in superseded_by). plan_v4_gaps: concrete things this research says matter that the plan lacks or gets wrong (cite path:line). Be exhaustive: typically 20-80 findings.`
const verifyPrompt = (p, ext) => `${RULES}\nAdversarial fact-check of an extraction from partition ${p.id} (${p.focus}). For EVERY finding with a number and at least a third of the rest, open the cited path:line (+-15 lines; grep if the line is off) and judge by 0-based index: verified | corrected (give corrected claim) | not_found (cannot be found: hallucinated) | superseded (file marks it replaced). Add up to 15 important plan-relevant facts the extractor missed to 'missed' (with theme, source path:line).\nEXTRACTION:\n${JSON.stringify(ext)}`
function applyVerify(ext, v) {
  const by = new Map(((v && v.results) || []).map(r => [r.index, r]))
  const kept = ext.findings.map((f, i) => { const r = by.get(i); if (!r) return {...f, verdict:'unchecked'}; if (r.verdict === 'not_found') return null; if (r.verdict === 'corrected') return {...f, claim: r.correction || f.claim, verdict:'corrected'}; if (r.verdict === 'superseded') return {...f, currency:'superseded', verdict:'superseded'}; return {...f, verdict:'verified'} }).filter(Boolean)
  const added = ((v && v.missed) || []).map(f => ({...f, verdict:'verifier-added'}))
  return {...ext, findings: [...kept, ...added], dropped: ext.findings.length - kept.length}
}
const verified = await pipeline(PARTS,
  p => agent(extractPrompt(p), {label:`extract:${p.id}`, phase:'Extract', schema:EXTRACT, model:'sonnet', effort:'high'}),
  (ext, p) => ext ? agent(verifyPrompt(p, ext), {label:`verify:${p.id}`, phase:'Verify', schema:VERIFY, model:'sonnet', effort:'medium'}).then(v => applyVerify({...ext, partition:p.id}, v)) : null)
const ok = verified.filter(Boolean)
log(`${ok.length}/${PARTS.length} partitions extracted+verified; dropped as not_found: ${ok.reduce((a,e)=>a+(e.dropped||0),0)}`)
const gaps = ok.flatMap(e => (e.plan_v4_gaps || []).map(g => `${e.partition}: ${g}`))
const misc = ok.flatMap(e => [...(e.contradictions||[]).map(c=>`${e.partition} CONTRADICTION: ${c}`), ...(e.open_items||[]).map(c=>`${e.partition} OPEN: ${c}`)])
const digests = await parallel(THEMES.map(t => () => agent(`${RULES}\nYou are the '${t}' synthesizer for the final integrated AksharDrishti Plan v4. Inputs: (1) verified findings tagged '${t}' from ${ok.length} partitions (below); (2) the planner's own full-read notes at ${NOTES} (read it; use the parts relevant to '${t}'); (3) all partitions' plan-gap notes and contradictions/open items (filter to '${t}'). Produce a deduplicated, conflict-resolved digest: established facts (latest dated version wins; apply errata; keep the strongest path:line), current vs superseded decisions, contradictions (both sides + resolution or open), recommendations for the final plan (evidence path:line, priority P0/P1/P2, including where Plan v4 must change), plan_v4_gaps, open questions. Each item <=400 chars. Never invent.\nPLAN:\n${PLAN}\nFINDINGS:\n${JSON.stringify(ok.flatMap(e => e.findings.filter(f => f.theme === t).map(f => ({...f, p:e.partition}))))}\nGAPS:\n${gaps.join('\n')}\nCONTRADICTIONS/OPEN:\n${misc.join('\n')}`, {label:`synth:${t}`, phase:'Synthesize', schema:DIGEST, model:'sonnet', effort:'high'})))
const coverage = ok.map(e => ({partition: e.partition, files: e.files}))
const critic = await agent(`${RULES}\nCompleteness critic. Coverage per partition (fully_read flags) and the 7 theme digests are below; the full doc list is /private/tmp/claude-501/-Users-srujansai-Desktop-South/8e7ec69e-22b6-4702-a989-3397b9a99c1e/scratchpad/all_docs.txt (583 paths; intentionally excluded: _archive/pre_fix*, _archive/.audit*, _archive/cleanup*, _reports/cleanup_cycle*, _archive/campaign_drafts_2026-09-30 (older copies)). Report: files not fully read, themes that look thin, load-bearing claims still unverified, and the next round of work.\nCOVERAGE:\n${JSON.stringify(coverage)}\nDIGESTS:\n${JSON.stringify(digests.filter(Boolean))}`, {label:'critic', phase:'Critic', schema:CRITIC, model:'sonnet', effort:'high'})
return {coverage, digests: digests.filter(Boolean), critic, missing_partitions: PARTS.filter(p => !ok.find(e => e.partition === p.id)).map(p => p.id)}
"""
js = js.replace('__PARTS__', json.dumps(parts, ensure_ascii=False)).replace('__PLAN__', json.dumps(plan)).replace('__S__', S)
open(S+'/wf_corpus_to_plan_v4.js','w').write(js)
print(len(js), 'bytes written')
