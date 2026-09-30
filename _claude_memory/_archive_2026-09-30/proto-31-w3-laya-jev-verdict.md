---
name: proto-31-w3-laya-jev-verdict
description: "Laya/JEV ruling — DECIDED 2026-09-30 on verified evidence: Laya is NOT used (not in the OCR pipeline, not as a dev gate) — it reads text not images, its own code says it is near-random on Indic scripts (Hindi 0.100, Tamil 0.113 vs 0.050 random), its script ID is a Unicode lookup, the only install on this Mac that imports belongs to swa-erp (Homebrew py3.14 copy is broken); JEV closed/paid/hosted → no; one measured reopen path (Day-4 fallback gate); Verdict confirms + ECC/graphify verdicts + CO-088"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T10:08:39.302Z
---

# PROTO-31 — LAYA / JEV RULING (W3). DECIDED 2026-09-30: Laya is NOT used. JEV is NOT used.

**The boss's prior:**
- CO-076: "LAYA is almost better and free → LAYA is best; verify and deploy; also check JEV, ECC…".
- CO-077: "could serve as a classifier or some layer in our pipeline".
- 2026-09-30: "can we use or not; if yes, write it in protocols" (H4 in [[proto-99-concern-crosswalk]] §H).

**Answer: no, on the evidence below.** The boss ordered to be countered when the evidence says otherwise; this is that counter. One measured way back in is kept below.

## Evidence (verified 2026-09-30 ~15:30 IST on disk + PyPI; facts F61, F63, F64 in [[proto-93-measured-facts]])
1. **Installed state.**
   - `laya 0.3.5` sits in Homebrew Python 3.14's user site: `~/Library/Python/3.14/lib/python/site-packages/laya`, installed 2026-09-22 23:09 IST.
   - It cannot import there: `ModuleNotFoundError: numpy`; torch and transformers are absent too.
   - A working copy lives in `~/Desktop/swa-erp/.venv-laya` (torch 2.14.0, transformers 5.17.0, MPS available). That is another project; South must not depend on it.
   - Laya is not installed in South's `.venv` / `.venv311`, and there are no Laya weights in `~/.cache/huggingface/hub`.
   - PyPI current version: 0.3.22 (Apache-2.0, Convai Innovations).
2. **It reads text, not images.** It cannot do OCR and cannot tell a page's language from the page.
3. **Its own code says it fails on Indic text.**
   - The `laya/lang.py` docstring (0.3.5) says the English checkpoint is "collapsing to near-random on non-Latin scripts (Hindi 0.100, Korean 0.103, Swahili 0.103, Tamil 0.113 at 20 options, where random is 0.050)".
   - The multilingual checkpoint (mmBERT-base, 322M params) reports MASSIVE 0.657 averaged over 51 languages (PyPI README). There are no per-language numbers for our scripts; Ol Chiki, Meetei Mayek and Nastaliq Kashmiri are unknown.
   - Base typed decisions: 0.362 zero-shot; 0.766 only after fine-tuning (README).
4. **Its script detection is a Unicode-range lookup.** Its own docstring says "Script detection is exact". A 10-line function does the same; no model is needed.
5. **The Claude `laya-gate` skill is not for this project.**
   - It runs swa-erp packs (`swa.inbound_email`, `swa.sheet_row_risk`, `harness.scope_guard`, `harness.prompt_guard`, `controlplane.admission`) through swa-erp's `packages/karna_decisions`.
   - Its own honesty note: "Base LAYA checkpoints are near-chance zero-shot on typed decisions".
   - It forbids irreversible deletes.
   - In South, the boss gates moves, deletes and downloads ([[proto-92-boss-decisions]] U29), not a classifier.
6. **The untracked `src/` "LayaRouter" never imports laya (F63).**
   - It routes on `gt_text`, the answer key: that is leakage.
   - It ignores the engine it picks.
   - It maps Meetei Mayek to `Mend` (Mende Kikakui) instead of `Mtei`.
   - This is a U3 matter; do not fix it without the boss.
7. **JEV is out.** Per §B6 it is closed-source, hosted and paid, with a 236–276 ms p50. That breaks local-first and $0. Its numbers come from vendor-affiliated pages (orcarouter.ai blog, jev-ai.pro), so treat them as vendor claims.

## The only reopen path (measured, not argued)
Reopen only if BOTH hold after Plan v3 Day 4 ([[proto-89-plan-v3-bodhan-base]]):
- (a) the oracle gap ([[proto-97-research-still-to-do]] RQ-11) is ≥ 0.02 CER for some language; AND
- (b) a deterministic bad-output check misses enough recoverable errors to move that language's CER by ≥ 0.02. The check looks for:
  - empty output;
  - a wrong-script share;
  - invalid Unicode sequences (a vowel sign with no base, a double virama);
  - n-gram repetition loops;
  - a low mean token log-prob from the recogniser.

If both hold, a learned gate may be tested. Candidates: Laya-multilingual fine-tuned (RLCD), or a character n-gram language model. That is training, so it needs the boss (the W6 decision) and a leak-free split by source document.
Until then: no install, no download, no code, no new md.

## Boss-requested exception (U31, 2026-09-30 evening): file-triage trial
The boss: "use Laya, it can give the decisions so fast after reading the content". Laya is trialled as an **advisory** file-triage classifier in [[proto-98-clean-repo-master]] §Laya.
- It is measured against full-read fates: bar accuracy ≥ 0.80 and precision ≥ 0.95 at confidence ≥ 0.9.
- It never decides alone and never deletes.
- It runs in swa-erp's working `.venv-laya`, read-only.
- The OCR-model ruling above is unchanged (U30).
- The trial's numbers are written back here.

## What Verdict still does here (W3, short)
> TASK (paste after the shared context block of proto-01). You are Verdict.
> 1. Confirm evidence items 1–5: run the commands, and open https://pypi.org/project/laya/ and `~/.claude/skills/laya-gate/SKILL.md`. Mark any item that no longer holds.
> 2. ECC and graphify verdicts, each keep / tune / drop with a reason:
>    - ECC hook overhead: measure `hook_success` durationMs from a transcript if possible.
>    - ecc-memory MCP: connected.
>    - graphify: navigation use and freshness. The bootstrap reports STALE when md files are newer than graph.json.
> 3. CO-088, one sourced paragraph: how Laya/JEV "crossed into relevance" (typed-decision classifiers distilled for speed and used as routing layers for LLM agents?), and the analogous OCR move, which is the Day-4 deterministic gate above. If you can't source it, write UNKNOWN.
> Write section 4 of `docs/campaign/SKILL_STACK.md` (≤ 800 words). Log the ruling as the answer to CO-076/077 in `DISPATCH_LOG.md`; Miss logs it in `BOSS_CONCERNS.md`.

## History (kept for the audit trail)
- §B6 in `docs/research/DEEPER_LIVE_RESEARCH_2026-09-29.md` (≈ lines 95–115; the file may move into the proto-95 bundle). Its sources: huggingface.co/convaiinnovations/laya, orcarouter.ai/blog/jev-vs-laya (2026-09-23), a daily.dev laya post, jev-ai.pro/compare/jev-vs-laya.
- `LAYA_GATE_DECISIONS.md` (AGENT-1, 2026-09-29) applied the skill's thresholds by hand; the Laya model never ran.
- The Lane-B records `docs/research/level7/b/b4_agent_tooling/laya_{detailed,gates}.md` are handled in proto-95 G6, as REJECTED rows that cite this file.

Related: [[proto-30-w3-skill-inventory]], [[proto-16-w1e-edge-refutation]], [[proto-88-skill-routing]], [[proto-93-measured-facts]], [[proto-95-research-harvest-decisions]]
