---
name: proto-01-law-and-guardrails
description: "THE LAW (merged 2026-09-30 night): LAW ORDER, the never-list rewritten to current paths and rulings, evidence law, no-fake-claims, tools, context hygiene, shared subagent block — plus, verbatim, pre-flight & checkpoints (ex proto-02), checkpoint discipline (ex proto-60), GT-tier reporting (ex proto-62), council/briefing/prompts (ex proto-79), templates (ex proto-90), Verdict cross-check (ex proto-91), the 3-agent model (ex campaign-law)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:57:01.270Z
---

# PROTO-01 — THE LAW (one file; merged 2026-09-30 night by the planner)

## LAW ORDER (which text wins when two disagree)
1. The boss's latest explicit word in chat. The planner records it the same turn, in proto-104 (rulings) or proto-92 (decisions).
2. **proto-104** rulings, latest revision first (rev 4: R-1…R-15).
3. **This file** (proto-01): the never-list, evidence law, process law.
4. **boss-rules** (how the boss wants the work done).
5. **proto-92** decisions U1…U37, D-a, and the settled conflicts C1–C15.
6. **`level2/ULTIMATE_HYBRID_CONCERN.md`**: the South-era operator law HL1–HL12. Still binding where the lines above do not supersede it. Superseded parts: the language lock te/ta/kn/ml, the team lanes, "South sealed, never merged", Level-3 "locked".
7. **`SOUTH_CANON.md`**: the label definition (§F/§G page schema) and the messages already sent (§J). History otherwise.
8. **`docs/campaign/CAMPAIGN_DIRECTIVE.md` v5, `OCR_AGENT_MEMORY_FEED.md`, `FULL TECHNICAL BRIEFING.md`, `docs/research/level7/*`**: read-only history. Never an active law, whatever their headers say.

When a lower text contradicts a higher one, the planner fixes the lower one (or adds a pointer line). Agents never pick silently.

## A. Never (violations end the run) — rewritten 2026-09-30 night to current paths and rulings (the 2026-09-29 text is kept at the end of this section)
1. **Subagents.** The planner runs NO subagents at all (boss-rules). Agents 1–3 may use Sonnet-class subagents, ≤5 in flight. Never Opus.
2. **No training** (LoRA, QLoRA, GRPO/RL, mlx-vlm train) before Gate 2.5 has passed (the Plan v3 multi-LLM evaluation + the boss's session with Vinay, B-17) AND the boss says go. Never train or tune on any benchmark split, bench item or test image.
3. **Downloads** only for an approved U-row (U7, U23, U24, U34 items as triggered) and only after the boss's go for that item. Log repo @ revision + size + sha256.
4. **Sarvam:** free credit only (₹67 at 2026-09-30). Only the calls a ruling approves (R-8: 12 South calls, submitted 2026-09-30). One DISPATCH_LOG ledger line per call. Nothing more without the boss.
5. **Sealed (read-only):**
   - `level2/out/` (South v1, until step S6);
   - `Datasets/` (incl. `akshardrishti_official/`, and `test/test/` = the eval set, never training);
   - `arc_level_1/`;
   - `_archive/bundles/*.tar.gz` (write-once).
   - `level2/benchmark/packs/` is append-only: new files only; an existing pack changes only by a versioned re-run (`out_archive/<engine>_vN/`, HL5).
6. **Locked (errata only, via a fix-spec with a pre-image):**
   - `level2/benchmark/docs/AGENT_PROTOCOL.md`;
   - `level2/benchmark/manifest_v1.json`;
   - `level2/benchmark/scores/sheet_v1.csv`;
   - `level2/benchmark/pipeline/run_probe.py` (R-2: the base-path constant fix is an approved erratum);
   - `level2/benchmark/pipeline/metrics.py`: scorer default behaviour never changes; new options live in a new module (B-02).
7. **`src/`, `tests/`, `configs/`:** U3 = archive (proto-102 A10 after A9). Do not run or edit them.
8. **No new md at the repo root.** New deliverables go in `docs/campaign/`, scripts in `level2/benchmark/pipeline/` or `level2/unified/`, product code in `product/`.
9–21. As in the 2026-09-29 text below (no deletion without verdict + bundle; no re-litigating locks; one session per task; no copies; read BOSS_CONCERNS Part 0 first; status words are claims; register before writing; research lands as decisions; destructive commands need proof; DONE only with check output in W4.md; archive = verified bundle + INDEX line; NEXT.md planner/boss only; one inventory script; a looping subagent is dead).
22. **No git commit/push/merge/issue edits without the boss** (R-6). PR #12 (vajrAstra cloud session) is a reference only. The one-off `boss/campaign-docs` branch exists only so the cloud planner can read the docs.
23. **Secrets:** `.env` holds the Sarvam key. Never print it, never commit it, never paste it into chat or logs. GPU credentials go in env vars on the server only.
24. **Portable product** (R-13): nothing we claim may exist only on the MLX path.

### A (2026-09-29 text, kept for audit; superseded where item 1–8 above differ)

1. **No subagent on Opus.** Every Agent call sets `model: "sonnet"`.
2. **No training.** Do not run, import-test or "smoke" anything in `src/training/`, mlx-tune, mlx_vlm, QLoRA or GRPO code. W6 is PAUSED (feed §15).
3. **No downloads** of weights, datasets, traineddata or packages. Reading a web page with WebFetch is allowed; saving a dataset/model is not.
4. **No Sarvam calls.** The 57-call cap is spent.
5. **Sealed (read-only, never write):** `level2/out/`, `level2/reports/`, `level2/probe22/out/`, `arc_level_1/`, `Datasets/akshardrishti_official/`.
6. **Locked (never edit; errata only via the feed):** `level2/probe22/AGENT_PROTOCOL.md`, `level2/probe22/manifest.json`, `level2/probe22/sheet.csv`, `level2/probe22/run_probe.py`.
7. **Untouchable pending U3:** the untracked `src/` tree. Do not run, edit, move or delete it.
8. **No new md at repo root** and none under `level2/research/`. New deliverables go in `docs/campaign/`; scripts in `level2/unified/`; fix-specs in `level2/probe22/fix_specs/`.
9. **No deletion** without a KEEP/MERGE/DELETE verdict + reason logged first; archive before delete (`_archive/`).
10. **Do not re-litigate locks:** §6.4 GT verdicts, D1–D4, §10, the 2026-09-25 meeting, C1–C12 in the directive's Part B.
11. **Do not run two sessions on one task.** If `ps` shows another Claude session working on this campaign, stop and tell the boss.
12. **No copies "for discoverability", no new parallel versions.** One canonical file per document; elsewhere a pointer line. Moves only inside an approved protocol step (proto-63/70/74). (Added 2026-09-30 after duplicates of `uni` and the meeting file were created.)
13. **Read `BOSS_CONCERNS.md` first every turn** (uni T3.2) and update the rows your step closes — with evidence — before reporting done.
14. **Status words are claims.** Never write DONE / COMPLETE / FINAL / READY / LOCKED / "0 remaining" in a file name, title or status line unless a command reproduces it now. (Added after `PROJECT_COMPLETE.md`, "0 duplicates remain", "KEEP BOTH" overclaims.)
15. **Register before writing.** Every agent/workstream adds a DISPATCH_LOG line (who, which files, until when) before it writes to the repo (proto-76).
16. **Research lands as decisions, not essays.** Research results go into `docs/campaign/RESEARCH_DECISIONS.md` rows (proto-95) and the decision they change; no new md file under `docs/research/` without a KEEP reason in `RESEARCH_FATES.csv`. (Added 2026-09-30: 86 research md files existed and the plan cited almost none.)
17. **Destructive commands need proof first** (`rm`, `rm -rf`, `git rm`, `find -delete`, `mv` of untracked data, `>` overwrites): a pre-op sha256 manifest of the targets + (untracked) a bundle verified by extract+sha + a CLEANUP_EXECUTION_LOG line naming the verdict. Forbidden: the `mv X X_tmp; rm -rf X_tmp` pattern and `2>/dev/null` on mv/rm/cp/tar. (Added 2026-09-30 after an agent deleted the untracked probe scores folder — proto-102.)
18. **A phase is DONE only when its check output is pasted into W4.md.** A phase that finishes in seconds without its check is NOT DONE; the next phase starts only after the previous check (+ a Verdict PASS where a gate is named).
19. **Archive = a verified bundle in `_archive/bundles/` + an `_archive/INDEX.md` line**, never a new per-folder directory or copied symlinks. **NEXT.md is written only by the planner or the boss;** agents write W4.md + DISPATCH_LOG.
20. **One inventory, one script:** `scripts/repo_inventory.py` writes all four inventories (proto-102 C4); no parallel inventory scripts.
21. **A looping or truncated subagent is dead** (finish = length, repeated reasoning): re-dispatch a smaller task, never the same prompt.

## B. Evidence law (every record, every claim)
Tag each claim: **PRIMARY** (opened the source; quote/number seen) · **MEASURED** (command output on disk, command recorded) · **DERIVED** (computed from
PRIMARY/MEASURED, show the arithmetic) · **CONTRADICTION** (two sources disagree — cite both) · **UNKNOWN** (could not establish — say what you tried) ·
**REJECTED** (checked and false) · **DEAD** (true but unusable for decisions, e.g. different benchmark). Each record names the decision it can change.

## C. No fake claims (CO-086) — concrete rules
- Never write a URL you did not open in this run. Never write a number you did not see or compute. Never paraphrase a quote as a quote.
- Every number states its **set and n** ("CER 0.145 on pa, n=90 scored items"), and its **metric** (CER mean vs median; Sarvam score vs our CER are not the same unit).
- "Wins" require: same items, same metric, n ≥ 50 per language (D4), and a significance test or an explicit "directional" label.
- Honest-empty is correct. "0 survivors", "UNKNOWN", "could not open" are valid, complete answers.
- **Done = reproduced.** Nothing is DONE without a command whose output reproduces the claim, pasted into the checkpoint.

## D. Tools
- Web: load with ToolSearch `select:WebSearch,WebFetch` before use. WebSearch mode "standard" first; "extended" only when thin. Record every query.
- OpenCode: MCP tools `mcp__opencode__*` (start with `opencode_setup`, then `opencode_provider_list`).
- Library docs: context7 MCP. GitHub: github MCP (read-only use).
- Repo knowledge graph: `graphify-out/GRAPH_REPORT.md` (read by section) for locating files by concept.
- Prefer python3 one-offs for counting; print compact results only.

## E. Context hygiene (the 2026-09-29 planner session died at ~390K tokens)
- Read big files in slices: `sed -n 'A,Bp' file | cut -c1-800`. Many repo lines are thousands of chars long — always `cut`.
- Never paste whole JSON/CSV into context; aggregate with python.
- Keep the lead session under ~250K tokens. If near it: write the checkpoint, tell the boss, continue in a fresh session with the same one-line prompt.

## F. Shared context block — paste verbatim at the top of EVERY subagent prompt
> You are a subagent on the South / AksharDrishti Indic OCR campaign, repo `/Users/srujansai/Desktop/South`. Before working, read
> `docs/campaign/CAMPAIGN_DIRECTIVE.md` Part A (lines 19–117) — it is verified disk truth and overrides any older doc.
> LAW: No fake claims — every claim carries a file:line or a URL you opened in this run, with its set, n and metric. Never invent a URL,
> number, title or quote. Honest-empty is correct; a sharp UNKNOWN beats a soft guess. Tag claims PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD.
> NEVER: train or run anything in `src/`; download weights/data; call Sarvam; write to `level2/out/`, `level2/reports/`, `level2/probe22/out/`,
> `arc_level_1/`, `Datasets/`; edit `AGENT_PROTOCOL.md`, `manifest.json`, `sheet.csv`, `run_probe.py`. Write ONLY the files this prompt names.
> Read big files in slices with `cut -c1-800`; aggregate data with python, never dump it. End with: (1) your structured result, (2) a list of every
> file:line and URL you relied on, (3) anything you could not verify, under UNRESOLVED.

Related: [[proto-00-runbook]], [[boss-standard]], [[model-tiering]], [[proto-91-verdict-cross-check]]

---

## G. (verbatim from proto-02-preflight-and-checkpoints, merged 2026-09-30 night; original in _archive_2026-09-30/)
> Path note (planner 2026-09-30): the sealed-count loop and locked-file stat below name the 2026-09-29 paths (`level2/reports`, `level2/probe22/*`). Use the §A item 5–6 paths above; the reference counts are history.

### Pre-flight (run at the start of every session and every wave; paste outputs into the checkpoint)
```bash
cd /Users/srujansai/Desktop/South
date '+%Y-%m-%d %a %H:%M IST'
# 1. Who else is running? (two OpenCode agents were live on 2026-09-29)
ps aux | grep -E 'claude|opencode' | grep -v grep | awk '{print $2, $9, substr($0, index($0,$11), 110)}'
# 2. What did other agents just do?
tail -30 DISPATCH_LOG.md | cut -c1-300
# 3. Working tree
git status --short | head -40
# 4. Sealed-dir counts (must match; any change = stop and report)
for d in level2/out level2/reports level2/probe22/out arc_level_1; do printf "%-24s %s\n" $d "$(find $d -type f | wc -l | tr -d ' ')"; done
# 5. Locked files unchanged since the planner's read
stat -f '%Sm %N' -t '%Y-%m-%d %H:%M' level2/probe22/manifest.json level2/probe22/sheet.csv level2/probe22/AGENT_PROTOCOL.md
```
Reference values at planning time (2026-09-29): manifest.json mtime 2026-09-29 02:45; sealed counts per feed §17: `level2/out/` 4,001 · `level2/reports/` 48 ·
`level2/probe22/out/` 13,289 · `arc_level_1/` 413. If a sealed count differs from the previous checkpoint, STOP and report — do not "fix" it.

**Concurrency rule:** if `ps` shows OpenCode or another Claude session and `DISPATCH_LOG.md`/`git status` shows them editing a file your step will edit
(e.g. `VINAY_MEETING_PACKET.md`), do not edit it. Tell the boss in one line and continue with steps that touch other files.

### Checkpoint scheme
- Folder: `docs/campaign/checkpoints/` (create on first use: `mkdir -p docs/campaign/checkpoints`).
- One file per wave: `W1.md`, `W2.md`, … Template in [[proto-90-templates]].
- Each step has one line: `- [ ] 1A packet audit` → `- [x] 1A DONE 2026-09-29 23:10 — fix_specs/W1A_PACKET_AUDIT.md (42 specs) — verified by <subagent id>`.
- A step in progress records its last completed sub-step, so a fresh session resumes mid-step: `1E-refute: candidates C1,C2 refuted; C3 in progress (lens b done)`.
- Subagent raw reports that the lead needs later go into `docs/campaign/checkpoints/W<n>_reports/<step>.md` (evidence trail; not deliverables).
- The wave file ends with `STATUS: COMPLETE` only when every step is DONE and verified.

### Resume logic for a fresh session
1. `ls docs/campaign/checkpoints/` → first `W<n>.md` without `STATUS: COMPLETE` is the current wave; if none exist, current = W1.
2. Inside it, the first unchecked step is next. If a step shows partial progress, resume from its last sub-step; do not redo finished sub-steps.
3. Re-run pre-flight before continuing.

Related: [[proto-00-runbook]], [[proto-90-templates]], [[proto-01-law-and-guardrails]]

---

## H. (verbatim from proto-60-monitor-and-checkpoint-discipline, merged 2026-09-30 night; original in _archive_2026-09-30/)

**Why:** between 09-29 21:00 and 09-30 03:10 the executing agents produced 1A–1E and most of 1F/1G, but `docs/campaign/checkpoints/W1.md` was never updated
(last write 20:58, all steps unchecked, "STOPPED"). A fresh session following [[proto-02-preflight-and-checkpoints]] would redo finished work. Monitor report:
`docs/campaign/checkpoints/MONITOR_2026-09-30.md`.

### Rule 1 — the checkpoint is written after EVERY step, before the next dispatch
Tick the step line with output path, verdict (PASS / PASS-WITH-FIXES / FAIL), verifier, and one evidence line. No tick = the step did not happen.

### Rule 1b — NEXT.md (added 2026-09-30)
`docs/campaign/checkpoints/NEXT.md` holds the ONE next step for any agent; the SessionStart hook prints it. Whoever finishes a step rewrites NEXT.md (what is next, which protocol) in the same turn.

### Rule 2 — reconcile a stale checkpoint from disk (do this NOW for W1)
1. For each step, check its output file exists and its mtime (`stat -f '%Sm %z %N' -t '%m-%d %H:%M' <file>`).
2. Output exists + a verify report exists → tick as DONE with both paths. Output exists, no verify → tick as `DRAFT (unverified)` and run [[proto-91-verdict-cross-check]].
3. Replace the "STOPPED" footer with `RESUMED <time> by <agent>`; keep the history lines (append, don't erase).
State on 2026-09-30 03:25 (monitor-measured): 1A DONE · 1B DONE (7 UNRESOLVED) · 1C DONE · 1D DONE · 1E DONE (0 survivors) · 1F IN PROGRESS (no MULTI_LLM_EVAL.md) ·
1G PARTIAL (round 1 54/54 PASS, 1 defect introduced by FS-50, 39 round-2 specs; packet re-edited 09-30 01:33; round-2 verify NOT on disk) · 1H NOT STARTED.

### Rule 3 — one executing lead at a time per wave
Before dispatching, list running agents (`ps aux | grep -E 'claude|opencode' | grep -v grep`) and the last 10 DISPATCH_LOG lines. If another lead is working the same wave,
write `LEAD-CONFLICT` in the checkpoint and ask the boss which one continues.

### Rule 4 — no file moves, copies or duplicates during a wave
Cleanup/reorganisation is Wave 5 work ([[proto-63-single-canonical-files]]). Copies made "for discoverability" are duplicates; use a pointer line instead.

### How the Opus monitor audits (for future monitor passes)
Read-only: (1) mtimes of every deliverable vs checkpoint ticks; (2) grep deliverables for known-false patterns (proto-93); (3) re-derive 3 headline numbers per
deliverable; (4) check sealed counts + locked mtimes; (5) look for new untracked trees (`git status --short | grep '^??'`); (6) write `MONITOR_<date>.md` and new
protocols; never edit deliverables, never spawn subagents.

Related: [[proto-00-runbook]], [[proto-02-preflight-and-checkpoints]], [[proto-91-verdict-cross-check]]

---

## I. (verbatim from proto-62-gt-tier-stratified-reporting, merged 2026-09-30 night; original in _archive_2026-09-30/)

**Monitor measurement (2026-09-30, `sheet.csv` × `manifest.json` `gt_source`, the 54 Sarvam-paired items):**
| GT tier | n | Sarvam mean CER | surya | best local (per item) |
|---|---|---|---|---|
| official_pair_txt — human gold (bn/hi/sa) | 9 | **0.064** | 0.535 | 0.243 |
| official_pdf_layer — PDF text layer | 36 | 0.311 | 0.229 | **0.229** |
| sarvam_bench — human-reviewed twice (per 1D) | 9 | **0.278** | 0.730 | 0.617 |

**Meaning:** the "our best local engine is ahead of Sarvam in 10/18 languages" signal comes entirely from PDF-text-layer GT. PDF text layers can encode reading order,
hyphenation, headers and legacy-font artefacts that line up with Tesseract-style output and penalise a VLM that reads the page naturally. On both human-verified tiers
Sarvam is 2–4× better. Hypothesis to test, not conclusion: PDF-layer GT favours layout-literal engines.

### Rule (all agents, all deliverables, effective now)
1. Never report an engine-vs-engine or us-vs-Sarvam comparison pooled across GT tiers. Show per tier with n.
2. The honest one-liner for Vinay: "On the 18 human-verified items where Sarvam ran, Sarvam's CER is 2–4× lower than our best local engine; our engines only lead on
   PDF-text-layer ground truth (n=36), which may favour layout-literal output. n is small (3 per language)."
3. Any "winner" claim at n≥50 (D4) must state its tier mix; winners decided mostly on PDF-layer GT are labelled "PDF-layer GT".

### Engine subagent — TASK (paste after the shared context block)
> Using `sheet.csv` (and `level2/unified/sheet_v2.csv` if [[proto-61-sheet-provenance-forensics]] produced it — report both):
> 1. Reproduce the table above. 2. For all 1,227 items: per language × tier × model mean CER and n; per-language winner per tier. 3. PDF-layer GT bias test:
> for 30 PDF-layer items where surya beats Sarvam by > 0.2 CER, show GT snippet vs both predictions (first 200 chars each) and classify the cause
> (reading order / hyphenation / header-footer / legacy font / true Sarvam error). 4. Write `docs/campaign/GT_TIER_ANALYSIS.md` with the tables, the 30-item
> classification counts, and the corrected one-liner. Writes only that file.

### Verdict check
Re-derive the 3-row table; confirm the 30 examples are quoted exactly; confirm the one-liner matches the data. Then Miss propagates the one-liner into
`DRAFT_RESEARCH_PLAN.md` §3 and the root packet (fix-spec, not free editing).

Related: [[proto-61-sheet-provenance-forensics]], [[proto-19-w1h-draft-research-plan]], [[proto-64-meeting-day-finish]]

---

## J. (verbatim from proto-79-council-briefing-prompts, merged 2026-09-30 night; original in _archive_2026-09-30/)

### 1. Briefing format (uni T7.2e; CO-026 Verdict must stop asking "what next")
Every report to the boss or the lead: a table with exactly these rows — **DECISIONS** (made, with reason) · **DELIVERED** (files, with verification) · **BLOCKERS** (only boss-level, each with a
recommendation) · **RISKS** · **NEXT** (what the agent does next without asking). ≤2,000 tokens, file:line refs. The ≤10-line boss report in [[proto-90-templates]] §7 is this table compressed.
Never end with "what should I do?" — end with NEXT (uni R0.10, CO-063).

### 2. Prompt maintenance (uni T7.4; CO-037 "fix the flow so improvement requests stop coming back as our fault")
If a subagent re-asks, misreads, or returns off-scope work twice: the lead rewrites that step's protocol file (memory + `docs/campaign/protocols/` mirror) with the missing instruction,
records `PROMPT-FIX: <step> — <what was missing>` in the checkpoint, and re-dispatches. Relaying the confusion upward unchanged is a failure.

### 3. Council deliberation (uni T7.5; CO-081 "deliberate like a council")
For load-bearing documents — `DRAFT_RESEARCH_PLAN.md`, `EDGE_THESIS.md`, `ARCHITECTURE_FREEZE.md`, `BOSS_CONCERNS.md` rebuild, level2 `MOVE_PLAN.md`, any §6.4 reopening:
three independent Sonnet reviewers (lenses: evidence/truth · feasibility/time · boss-concern coverage), each blind to the others; the lead writes a synthesis listing agreements, disagreements and
the resolution with reasons, appended to the document's checkpoint report. A disagreement the lead cannot resolve by evidence goes to the boss with a recommendation.

### 4. Verdict autonomy (CO-027/028)
Verdict acts within scope without asking, counters the boss with evidence when a directive is wrong, and its recommendations are adopted by default unless they need boss authority (uni T7.3).

Related: [[proto-91-verdict-cross-check]], [[proto-90-templates]], [[proto-60-monitor-and-checkpoint-discipline]]

---

## K. (verbatim from proto-90-templates, merged 2026-09-30 night; original in _archive_2026-09-30/)

### 1. Wave checkpoint — `docs/campaign/checkpoints/W<n>.md`
```markdown
# W<n> CHECKPOINT — <wave name>
Started: 2026-MM-DD HH:MM IST · Lead: Sonnet session <id if known> · Protocol: memory proto-<nn>…
### Pre-flight
<paste pre-flight outputs from proto-02, trimmed>
### Steps
- [ ] <step id> <name> — output: <path> — verified by: <subagent> — evidence: <command → result>
### Partial progress (for resume)
<step id>: <last completed sub-step>
### Deviations
PROTOCOL-DEVIATION: <what> — <evidence>
### Open issues / boss decisions needed
STATUS: IN PROGRESS | COMPLETE
```

### 2. Footer every subagent report must end with
```markdown
#### Sources relied on
- file:line — what it supports
- URL (opened <date>) — what it supports
#### UNRESOLVED
- <claim I could not verify> — what I tried
```

### 3. Fix-spec row (Verdict) — `level2/probe22/fix_specs/<name>.md`
```markdown
#### FS-07 · BLOCKER · VINAY_MEETING_PACKET.md:124
- OLD (exact, occurs once): `…`
- NEW (exact): `…`
- EVIDENCE: `<command>` → `<output>`
- WHY: <one line>
```

### 4. Evidence record (research)
`ID · claim · tag (PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD) · source (file:line or URL + date opened) · set/n/metric · decision it can change`

### 5. `DISPATCH_LOG.md` entry (append at wave end; Miss owns the file — the lead may append when no Miss subagent is running)
```markdown
### <date> <HH:MM IST> — W<n> <wave name> (Sonnet lead, protocol: memory proto files)
| step | owner | output | verified | status |
|---|---|---|---|---|
**Hard laws held:** no training, no downloads, no Sarvam calls, sealed dirs untouched (counts: out 4001 / reports 48 / probe22-out 13289 / arc 413), locked files untouched.
**Open:** <items> · **Boss decisions pending:** <U-ids>
```

### 6. `OCR_AGENT_MEMORY_FEED.md` §11 log line (append-only, never rewrite earlier lines)
`- 2026-MM-DD HH:MM (Sonnet lead, W<n>): <what happened in one sentence>; outputs <paths>; verified <yes/partial>; open <n>.`

### 7. Boss report (≤10 lines, plain words, send at every wave end)
```
W<n> <name>: COMPLETE | PARTIAL (<what was cut and why>)
Done: <3 lines max, each with the file>
Found: <the 1–3 facts that change a decision, each with n>
Not done / risks: <1–2 lines>
Need from you: <U-questions with the recommended answer> + <any paste request, e.g. ChatGPT prompt at docs/campaign/CHATGPT_EVAL_PROMPT.md>
Next: W<n+1> <name> starts unless you say stop.
```

Related: [[proto-00-runbook]], [[proto-02-preflight-and-checkpoints]], [[proto-91-verdict-cross-check]]

---

## L. (verbatim from proto-91-verdict-cross-check, merged 2026-09-30 night; original in _archive_2026-09-30/)

### Dispatch
A fresh Sonnet subagent, role Verdict. Prompt = shared context block ([[proto-01-law-and-guardrails]] §F) + this block + the path of the deliverable + the path of the author's report.

### Reviewer block (paste)
> You are the Verdict agent reviewing `<deliverable>`. Your default is FAIL until evidence says PASS. Do not rewrite the document; list defects with exact fixes.
> Check, and report each as PASS/FAIL with evidence:
> 1. **Numbers:** pick every number (or at least 15 at random if there are more). Re-derive each from its cited source with a command or by opening the URL. Mismatch = FAIL.
> 2. **n and metric:** every performance number states its set, n and metric (CER mean/median, Sarvam score ≠ CER). Missing = FAIL.
> 3. **Comparisons:** every "wins/beats/best/SOTA" has same items + same metric + n ≥ 50 (D4) + a named test, or is labelled directional. Otherwise FAIL.
> 4. **Sources:** every URL was opened by the author (spot-open 3); every file:line exists and says what is claimed (spot-check 5). Invented = FAIL (severity BLOCKER).
> 5. **Quotes:** quoted text appears verbatim in the source (`grep -F`).
> 6. **Dates:** weekday matches the ISO date; uncertain dates are "TBC", not guessed.
> 7. **Scope:** the document does what its protocol file asked (compare against the protocol's section list); nothing required is missing, nothing duplicates a precursor's content.
> 8. **Law:** no writes to sealed/locked paths (`git status --short`), no training/downloads/Sarvam traces, no new md at root.
> 9. **Contradictions:** the deliverable does not contradict directive Part A or another Wave deliverable without saying so explicitly (CONTRADICTION tag).
> 10. **Honesty:** UNKNOWN/empty sections are stated as such, not filled with generic text.
> Output: a table `check · PASS/FAIL · evidence · exact fix` and an overall verdict: PASS / PASS-WITH-FIXES (list) / FAIL.

### Fix loop
Round 1: author (or Miss) applies the exact fixes → a reviewer (may be the same Verdict subagent via SendMessage) re-checks only the failed items.
Round 2: same. Still failing after round 2 → the item goes to the boss in the wave report as "unresolved, here is why"; the deliverable is marked PARTIAL.

### What the lead records in the checkpoint
`<step> verified: PASS | PASS-WITH-FIXES (n fixes, round k) | FAIL → escalated` + the reviewer's subagent id/description.

Related: [[proto-00-runbook]], [[proto-01-law-and-guardrails]], [[proto-90-templates]]

---

## M. (verbatim from campaign-law, merged 2026-09-30 night; original in _archive_2026-09-30/)
> Update 2026-09-30: agent names are Agent 1 = Engine (`ses_f12a7b89…`), Agent 2 = Verdict + repair lead (`ses_f1233a0a…`), Agent 3 = Miss/builder (`ses_f16bc20e…`); the interface files moved with the restructure (`level2/benchmark/…`); fix-specs live next to the file they fix.

The campaign runs as exactly **three top-level agents**, simultaneous. No fourth. Each may spawn subagents freely.

**AGENT 1 — Engine.** Owns OCR engines, model execution, probe runs, scoring pipelines, downloads (only with explicit boss approval), GPU/compute, engine queues, kill/restart of stuck processes. Must not edit protocol docs owned by others, or call a result final without Verdict sign-off.

**AGENT 2 — Verdict.** Owns GT verification, forensics, scorer rules, hostile audits, fix-specs, leaderboards, and the TRUTH-status of every other agent's output. Must counter-check every Engine and Miss output. Has standing authority — and obligation — to counter the boss with evidence.

**AGENT 3 — Miss (Miscellaneous).** Owns everything else: file hygiene, doc merges, protocol edits, dispatch logistics, integration glue, `BOSS_CONCERNS.md`, `DISPATCH_LOG.md`, cleanup execution via fix-specs. Must not overwrite Engine/Verdict work or apply fix-specs touching truth-bearing artifacts without Verdict verification.

**Interfaces — file-based, append-only:**
- `level2/probe22/engine_health_log.jsonl` — Engine writes, all read
- `level2/probe22/fix_specs/` — anyone proposes, Miss applies, Verdict verifies
- `DISPATCH_LOG.md` — Miss maintains, all obey
- `BOSS_CONCERNS.md` — Miss maintains, every agent reads at every turn
- `PROTOCOL_UPGRADES.md` — Verdict drafts, boss approves

**CROSS-CHECK LAW:** every agent's output is checked by at least one other agent before it counts as truth. Nothing reaches the boss unverified.

**Orchestration, not labor.** Top-level agents dispatch and monitor; labor goes to subagents. Work belonging to an existing lane joins that lane's queue — new agents only for genuinely unowned work. Anything the lead cannot cover goes into `DISPATCH_LOG.md` for the boss to assign; the lead does the *higher* work, subagents do the *broad* work.

**Cycle-graph workflow:** dispatch → subagent reports → monitors verify → lead implements → re-audit → next cycle. A subagent's report is evidence, not a verdict. Monitors re-open a random sample of every subagent's verdicts and link-check every MERGE/DELETE before it executes.

**Council deliberation:** load-bearing md/audit decisions get a structured multi-reviewer pass. No single-agent fiat on documents the campaign depends on.

**Why:** The boss watched agents stall, duplicate each other, and silently drop work. Lane ownership plus file-based interfaces means state survives any individual agent dying, and no two agents can silently disagree about the same artifact.

**How to apply:** Before dispatching, ask which lane owns the work. Before writing to a shared file, check the owner above. Never let a subagent's self-report stand as truth — it needs a second pass.

Related: [[boss-standard]], [[campaign-state]], [[open-front]]
