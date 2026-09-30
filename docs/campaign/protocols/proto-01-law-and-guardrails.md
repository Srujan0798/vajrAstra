---
name: proto-01-law-and-guardrails
description: "The binding law for the lead and every subagent in the South campaign — forbidden actions, sealed/locked files, evidence tags, no-fake-claims rules, tool loading, context hygiene, and the shared context block pasted into every subagent prompt"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:57:01.270Z
---

# LAW AND GUARDRAILS (applies to the lead and to every subagent)

## A. Never (violations end the run)
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
