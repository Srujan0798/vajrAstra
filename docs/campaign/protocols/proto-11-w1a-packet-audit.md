---
name: proto-11-w1a-packet-audit
description: "Step 1A (Verdict subagent) — hostile claim-by-claim audit of VINAY_MEETING_PACKET.md and its strategy/evidence docs, reproducing the planner's defects K1–K7 with exact commands, producing exact old→new fix-specs"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:11:24.249Z
---

# STEP 1A — HOSTILE AUDIT OF THE MEETING DOCUMENTS (Verdict subagent)

**Dispatch:** one Sonnet subagent, role Verdict. Prompt = shared context block ([[proto-01-law-and-guardrails]] §F) + the TASK block below.
**Writes only:** `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` (lead runs `mkdir -p level2/probe22/fix_specs` first; the folder did not exist on 2026-09-29).

## TASK block (paste)
You are the Verdict agent. Your job is to make sure nothing false reaches Vinay tomorrow. Default to suspicion: a claim is false until a command reproduces it.

**Targets (read all, in slices):** `VINAY_MEETING_PACKET.md` (root, primary) · `EVIDENCE_SUMMARY.md` (root) · `docs/architecture/W5_STRATEGY_OPTIONS.md` ·
`docs/research/level7/W5_STRATEGY_OPTIONS.md` · `W5_BEAT_SARVAM_PLAN.md` (root) · `docs/architecture/W5_BEAT_SARVAM_PLAN.md` · `docs/research/level7/W5_BEAT_SARVAM_PLAN.md` ·
`PER_LANG_ROUTING.md` · `COMPUTE_BUDGET_ESTIMATE.md`. Evidence sources: `level2/probe22/sheet.csv` (cols: image_id, language, script, print_or_hand, quality,
has_table, mixed_script, gt, model, prediction, CER, WER, error_tag; 12,324 rows; 11 models) · `level2/probe22/manifest.json` (dict with `items`, 1,283) ·
`level2/probe22/manifest_additions.json` · `level2/probe22/scores/` · `level2/probe22/gt_verification.json` · `level2/probe22/gt_forensics.json` ·
`level2/reports/` (sealed, read-only) · `OCR_AGENT_MEMORY_FEED.md` §12 (line ~450) and §15–16 (line ~811).

**Part 1 — claim ledger.** Extract every sentence of `VINAY_MEETING_PACKET.md` that contains a digit, a date, a comparative ("beats", "wins", "best",
"SOTA", "only"), or a status word ("DONE", "LOCKED", "READY", "verified"). Starter:
```python
import re; L=open('VINAY_MEETING_PACKET.md').read().splitlines()
for i,l in enumerate(L,1):
    if re.search(r'\d|beats?|wins?|best|SOTA|only|DONE|LOCKED|READY|verif', l): print(i, l[:300])
```
For each claim: ledger row = `id | packet line | claim (≤25 words) | source cited | reproduce command | output | verdict`. Verdicts: VERIFIED · WRONG ·
UNSUPPORTED (no source, cannot reproduce) · STALE (was true, disk changed) · DIRECTIONAL (true but n too small to claim) · DEAD (true but different benchmark).
Group duplicates (the packet repeats claims in TL;DR, recap, §1 — one ledger row, all line numbers).

**Part 2 — reproduce the planner's defects (do not trust the planner; if one does not reproduce, say REJECTED and why).**
- **K1 "Beats Sarvam on 9/18 langs"** (packet §1 "What we recommend" table) and every "9/18" sentence. Run:
```python
import csv,collections,statistics as st
R=list(csv.DictReader(open('level2/probe22/sheet.csv'))); by=collections.defaultdict(dict)
for r in R:
    try: by[(r['language'],r['image_id'])][r['model']]=float(r['CER'])
    except ValueError: pass
res=collections.defaultdict(lambda:{'sv':[],'su':[],'best':[],'w':0,'l':0,'t':0})
for (lang,i),v in by.items():
    if 'sarvam_vision' not in v: continue
    s=v['sarvam_vision']; loc={e:c for e,c in v.items() if e!='sarvam_vision'}; su=loc.get('surya')
    d=res[lang]; d['sv'].append(s); d['best'].append(min(loc.values()))
    if su is not None:
        d['su'].append(su); d['w' if su<s else 'l' if su>s else 't']+=1
for lang,d in sorted(res.items()):
    print(lang,len(d['sv']),'sv',round(st.mean(d['sv']),3),'surya',round(st.mean(d['su']),3),'best',round(st.mean(d['best']),3),'W/L/T',d['w'],d['l'],d['t'])
```
  Planner's result (2026-09-29): 54 paired items (3/lang); surya mean CER < Sarvam in 10/18 (brx gu ks mai mr ne or pa sd ur); item-level surya better 21,
  Sarvam better 28, tie 5. Also establish what "surya wins 9/18" in `EVIDENCE_SUMMARY.md` §3 actually counts (best local engine per language, n≥50) and count it
  yourself from `sheet.csv` per language (mean CER per model, n per language). Write the ONE sentence the data supports, e.g. "On the 54 items where Sarvam
  was run (3 per language), our best local engine had a lower mean CER than Sarvam in 10 of 18 languages; at n=3 per language this is directional only."
- **K2** "1,227 items" vs manifest 1,283: count manifest items, sheet rows per model, `manifest_additions.json` (56: sd 25, mr 21, pa 10). Fix = name the set every time.
- **K3** weekdays: `grep -n -E 'Tue 2026-09-30|Sat 2026-10-04|Wed 2026-10-01|Oct 4 \(Sat\)' VINAY_MEETING_PACKET.md EVIDENCE_SUMMARY.md PER_LANG_ROUTING.md COMPUTE_BUDGET_ESTIMATE.md`.
  Calendar: 09-29 Tue, 09-30 Wed, 10-01 Thu, 10-04 Sun (`date -j -f %Y-%m-%d 2026-10-01 +%A`). Fix = ISO date + correct weekday; where the date itself is uncertain
  (lead-joins, freeze, submission), write "date TBC (U1/U2)" — never invent.
- **K4** Option A (packet; Miss) vs Option D (Verdict; `docs/architecture/W5_STRATEGY_OPTIONS.md`; feed §15 Verdict entry ~line 890). Diff the two options docs.
  Lay out each option: what ships, cost, risk, evidence, what it wins. Fix = packet presents both with evidence; add your recommendation, labelled as such.
- **K5** backbone: `grep -n -E 'Qwen2.5-VL-3B|GLM-OCR' OCR_AGENT_MEMORY_FEED.md VINAY_MEETING_PACKET.md docs/research/level7/W6_QLORA_SPEC.md COMPUTE_BUDGET_ESTIMATE.md`.
  Feed §12.2 says Qwen2.5-VL-3B PRIMARY; packet says GLM-OCR 0.9B primary. Establish which is the latest locked decision and whether weights are on disk
  (`ls ~/.cache/huggingface/hub 2>/dev/null | grep -i -E 'qwen|glm'` — read-only).
- **K6** `EVIDENCE_SUMMARY.md` §3 sa row "surya all-empty (Ol Chiki bug)": sa = Sanskrit (Devanagari). Measure surya on sa: mean CER over all sa items and
  count of empty predictions (`prediction.strip()==''`). Fix the label; keep the fact.
- **K7** kok gap: feed §12.2 "gap 0.32" and "kok 32pt → 5pt" vs `EVIDENCE_SUMMARY.md` §3 0.194 vs DISPATCH_LOG P5. Recompute kok mean CER for surya, easyocr,
  tesseract_bilingual from `sheet.csv`; state which figure is right.
- **Also check:** "11 OCR engines" (10 independent — tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr); "12,324 packs" (= rows, not packs); "Sarvam overall
  CER 0.2400 (n=54)"; "$0"; "mlx stack installed"; "9.4 GB reclaimable"; per-language Sarvam-bench numbers (53.91 sat, 54.82 ks, 55.3 OldScan, 80.01 or) — these are
  Sarvam's own benchmark **scores**, not CER; flag every place the packet compares them to our CER as DEAD-for-comparison.
- **Also check dates of status claims:** "W5 freeze opens Wed 2026-10-01 evening", "final deliverable Sat 2026-10-04" → U1/U2.

**Part 3 — fix-specs.** For every non-VERIFIED row: `FS-nn | file | line | exact old text (verbatim, unique in file) | exact new text | evidence (command + output) | severity (BLOCKER = false
claim Vinay could catch / MAJOR = misleading / MINOR = wording)`. Old text must be copy-exact so the Miss agent can apply it with an exact string replace.
Do not propose edits to sealed/locked files; for those write an ERRATUM line instead.

**Part 4 — recommendation block** (≤200 words): the 3 biggest risks in front of Vinay and what the packet should say instead; your Option A vs D recommendation with reasons.

**Output file layout:** `# W1A PACKET AUDIT` → summary counts by verdict → K1–K7 results → claim ledger table → fix-specs (BLOCKER first) → recommendation → sources.
Final message to the lead: counts, the BLOCKER list, and the path.

## Lead's acceptance check (before marking 1A DONE)
- Spot-check 5 random ledger rows by re-running their commands. Any mismatch → return to the subagent (round 2).
- Every fix-spec's old text is found exactly once: `python3 -c "import sys;t=open(F).read();print(t.count(OLD))"` == 1.
- K1–K7 each has a verdict. Then hand fix-specs to [[proto-18-w1g-apply-verify]].

Related: [[proto-10-w1-overview]], [[proto-18-w1g-apply-verify]], [[proto-93-measured-facts]], [[proto-91-verdict-cross-check]]
