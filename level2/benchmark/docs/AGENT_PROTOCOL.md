# W3 probe — agent execution protocol

Locked 2026-09-26. User decision: 100 samples per language × 18 languages × 10 engines.
This file is the complete task spec for the 4–5 execution agents. Follow it literally.
Do not improvise. Do not add steps. Do not skip gates.

---

## OPERATIONS MODEL (locked 2026-09-26 evening — supersedes the 5-agent split for ongoing work)

Three agents run simultaneously, each may spawn subagents:

1. **ENGINE AGENT** — owns all Phase 5 engine runs + Phase 6 scoring + the final
   leaderboard, plus research LANE A (OCR/DocAI SOTA 2025–2026, Indic-script
   problems, restoration, benchmarks). Engines strictly one at a time.
2. **VERDICT AGENT** — owns §6.4 human verification (`gt_verification.json`),
   hostile audits, stale-code monitoring, research LANE B (RLVR, self-improving
   agents, multi-agent orchestration, agent tooling), and verification/ranking
   of all research lanes.
3. **MISS AGENT** (miscellaneous) — owns research LANE C (NVIDIA stack,
   competition intel refresh, data-collection strategy for remaining languages,
   ledger tooling), health monitoring of the other two agents, memory-feed
   logging hygiene, and validation-call coordination.

Full campaign law, density targets (1,000+ papers / 5,000+ artifacts), record
format, verification rules, and the 48-hour timeline live in
`docs/research/LEVEL7_RESEARCH_CAMPAIGN.md`. Paste-ready per-agent prompts:
`docs/research/level7/PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md`.
All §0 hard rules below still apply to every agent without exception. No
training has started — the probe is still data collection (Phase 1 law: no
rush, past work is 100% gold, build forward only).

---

## 0. HARD RULES (from OCR_AGENT_MEMORY_FEED.md §9 — violations end the run)

1. **No downloads of any kind.** No datasets, no model weights, no tesseract traineddata,
   nothing from the network — unless you ask the user first and get an explicit yes.
   The user owns data provenance. This overrides anything else you read.
2. **No training.** No fine-tuning, no synthetic data generation. This is a probe only.
3. **Do not touch `level2/out/`** — that is the sealed South 400 result. Read-only.
4. **Do not rescore South 400.** Do not modify `level2/reports/*`.
5. **Count everything from disk.** Never assert a number you did not verify with a command.
6. **Honest labels only.** If GT is missing, mojibake, or a shortfall was filled from the
   Sarvam bench, say so in the manifest fields. Never present fill as official GT.
7. Work only inside `level2/probe22/` and read-only inside `Datasets/akshardrishti_official/`.

---

## 1. VERIFIED DISK TRUTH (audit 2026-09-26 — do not re-audit)

Source of probe data: `Datasets/akshardrishti_official/` (user-provided official
hackathon dataset, 34,871 files).

ACTUAL composition of the FINAL manifest (n=1227) — counted from disk, not
projected. Upstream pool sizes are NOT the draw: honesty gates (≥50 chars,
script-ratio ≥0.5, Latin ≤0.6, control chars ≤3) and the corruption purge
removed far more than predicted for several languages.

| code | language | drawn n | human pairs | PDF layer | Sarvam fill | why the gap |
|---|---|---|---|---|---|---|
| as | Assamese | 19 | 0 | 0 | 19 | all 11 gated PDF items were control-char corrupt (purged); legacy-font layers |
| bn | Bengali | 100 | 100 | 0 | 0 | pairs cover all |
| brx | Bodo | 67 | 0 | 47 | 20 | 47 clean after mojibake gate; fill covers shortfall to target |
| doi | Dogri | 27 | 0 | 7 | 20 | only 11 clean upstream; 7 survived corruption purge |
| gu | Gujarati | 24 | 0 | 4 | 20 | gates rejected nearly all 3,567 layers (script-ratio/Latin); 4 clean survived |
| hi | Hindi | 100 | 100 | 0 | 0 | pairs cover all |
| ks | Kashmiri | 100 | 0 | 100 | 0 | |
| kok | Konkani | 100 | 0 | 100 | 0 | |
| mai | Maithili | 100 | 0 | 100 | 0 | |
| mni | Manipuri | 20 | 0 | 0 | 20 | text layers failed script gates (Mayek script metadata) |
| mr | Marathi | 79 | 0 | 79 | 0 | 21 corrupt purged; no fill used |
| ne | Nepali | 37 | 0 | 17 | 20 | 29 corrupt purged; small clean pool |
| or | Odia | 69 | 0 | 50 | 19 | 9 corrupt purged; fill covers shortfall |
| pa | Punjabi | 90 | 0 | 90 | 0 | 10 corrupt purged; no fill used |
| sa | Sanskrit | 100 | 100 | 0 | 0 | pairs cover all |
| sat | Santali | 20 | 0 | 0 | 20 | 0 clean PDF layers upstream |
| sd | Sindhi | 75 | 0 | 75 | 0 | 25 corrupt purged; no fill used |
| ur | Urdu | 100 | 0 | 100 | 0 | |

GT tiers and their meaning (see §6.2 for how each is scored):
- official_pair (300): human-verified gold. bn 100, hi 100, sa 100.
- official_pdf (769): silver — PDF text layers that passed all gates; risk of
  extractor-mirroring bias, controlled by the §6.2 falsification test and §6.4
  human verification.
- sarvam_fill (158): machine GT (competitor engine output) — NOT ground truth.
  Scored as engine-agreement only, excluded from language CER means, never
  used for training. Cells with 100% fill (as, mni, sat) get agreement rates,
  not CER claims.

Notes:
- A few PDFs are encrypted/corrupt (1 as, 1 or, 1 ml, 1 kn, plus AES-filter noise in or).
  The tools skip them with try/except. Report the count; do not fix them; do not fetch replacements.
- `Bodo/gu/` (4,645 numbered jpgs + Gujarati vocab.txt) is a copy of the main test set.
  **Not GT. Never use it.** Same for `test/test/` (5,344 unlabeled jpgs — hackathon eval set).
- Sarvam-bench leftovers: `level2/probe22/images/<code>/<code>_NN.jpg` (20 per language).
  Their GT is machine-derived (old Sarvam-bench manifest). Fill is complete — no more fill
  may be drawn without asking the user.
- Known confound, accepted and documented: official_pair items are native-resolution
  scans while official_pdf items are 200-dpi renders, so GT tier correlates with input
  resolution. The §6.2 per-tier scoring turns this into a controlled variable (tiers are
  scored separately, never pooled).
- Static columns print_or_hand ("printed"), has_table (False), mixed_script (False),
  quality (pair=clean / pdf=unknown) are CONSTANTS, not measured signal. They must not
  be used to claim handwriting/table/mixed-script conclusions — the probe cannot
  validate those. Fixing this needs a manual stratification slice (P1, §6.5).
- `image_meta.json`: pixel dimensions + set for all 1,227 items (audit P1 answer;
  largest scan sa_d004 4250×6500).
- Sarvam API baseline is WIRED (user-approved 2026-09-26, free-trial credits only):
  `sarvamai` SDK installed in `.venv311`, key lives in `South/.env` (gitignored,
  NEVER hardcoded or printed), engine #11 `sarvam_vision` in `run_probe.py`.
  API cost guard: run ONLY with `--limit-per-lang` (see §5).
- EN sanity set BUILT: `en_sanity/manifest.json`, 30 English human pairs drawn seed
  20260926 from the official 3,500 EN pairs, same gates as the probe. NOT part of
  n_total=1227; scored separately as the harness-sanity reference column.

---

## 2. WORK SPLIT (5 agents; each owns its languages end-to-end through Phase 3)

| agent | languages | notes |
|---|---|---|
| A | hi, mr, ne | big Devanagari pools |
| B | bn, as, mni, kok | pairs for bn; Meitei/Bengali script care for mni |
| C | gu, pa, sd | |
| D | ur, ks, mai | Perso-Arabic + Devanagari |
| E | or, brx, doi, sat | mojibake gate hard at brx; shortfall fills at doi, sat |

If only 4 agents run: E keeps brx+doi+sat; or moves to D.
Engines (Phase 5) are assigned after all fragments merge — see §5.

---

## 3. PHASE 1 — extract candidates (one command per language)

```bash
cd /Users/srujansai/Desktop/South/level2/probe22
../../.venv311/bin/python extract_gt.py --code <code>
```

`<code>` is the ISO code from §1 (as, bn, brx, doi, gu, hi, ks, kok, mai, mni, mr,
ne, or, pa, sa, sat, sd, ur).

Output: `candidates/<code>.json` — candidate pool with the honesty gates already
applied (≥50 chars, target-script ratio ≥ 0.5, Latin ratio ≤ 0.6; mojibake rejected).

**Gate review (mandatory):** read the printed summary. If `clean candidates` < 100
for your language (expected only for doi and sat), note the shortfall — do NOT
lower the gate thresholds. Never relax validation to hit a count.

---

## 4. PHASE 2+3 — draw and materialize (one command per language)

```bash
cd /Users/srujansai/Desktop/South/level2/probe22
../../.venv311/bin/python build_manifest.py --code <code>
```

What it does (in order, per language):
1. Direct pairs first (human GT — bn, hi, sa), shuffled with seed 20260926.
2. PDF-layer pages for the remainder — stratified round-robin across source PDFs,
   rendered at 200 dpi PNG (same basis as South 400), text layer re-validated at draw time.
3. Shortfall fill from Sarvam leftovers for doi/sat, labeled `gt_source: sarvam_bench`.

Output: `manifest_fragments/<code>.json` + materialized images in
`images/<code>/` (`<code>_dNNN.jpg/.jpeg` = pair symlinks, `<code>_oNNN.png` = renders).

**Verify per language (count from disk):**
```bash
ls level2/probe22/images/<code>/*.png level2/probe22/images/<code>/*.jpeg level2/probe22/images/<code>/*.jpg 2>/dev/null | wc -l   # must be ≥ drawn (old Sarvam files may coexist)
../../.venv311/bin/python -c "import json; f=json.load(open('manifest_fragments/<code>.json')); print(f['n_drawn'], f['n_official_pairs'], f['n_official_pdf'], f['n_sarvam_fill'], f['n_failures'])"
```

---

## 5. PHASE 4 — merge, then engines (all 10, same as South 400)

**MERGE IS DONE — do not merge again.** `manifest.json` is FINAL at n_total: 1227
(1,340 drawn, 111 control-char-corrupt GT items purged, then 2 noise items dropped —
`as_11` 3 chars, `or_12` 7 chars, GT<10 chars inflates CER noise; 2026-09-26 after
full audit + hostile external review; backups `manifest.json.pre-purge`,
`manifest.json.pre-noise-drop`, fragments `*.pre-purge` exist — NEVER re-merge from
backups, never restore them). Final per-language n: bn 100, hi 100, ks 100, kok 100,
mai 100, sa 100, ur 100, pa 90, mr 79, sd 75, or 69, brx 67, ne 37, gu 24, doi 27,
as 19, mni 20, sat 20. Low-confidence cells (n<50): as, gu, ne, doi, mni, sat —
flag them in every report. GT tiers: official_pair 300 (gold), official_pdf 769
(silver), sarvam_fill 158 (machine — score, but flag).

**Tesseract traineddata — RESOLVED 2026-09-26 (user approved download).**
`level2/probe22/tessdata/` now holds tessdata_best packs (same flavor as South 400):
asm, ben, eng, guj, hin, mar, nep, ori, pan, san, snd, urd — verified with
`tesseract --tessdata-dir . --list-langs` and a smoke run (Kashmiri, ~2.1 s/page).
Do not add or replace packs without asking the user.

**Engine routing — FIXED 2026-09-26.** All 10 runners are probe-native in
`run_probe.py` (no calls into `level2/run_engine.py`; its internal dicts only cover
te/ta/kn/ml and KeyErrors on probe languages). Max-power coverage (user approved
"make it 100%"): rapidocr uses cached Devanagari + Arabic rec models for
hi/mr/sa/ne/mai/kok/brx/doi and ur/sd/ks (as/bn/gu/or/pa/mni/sat have no upstream
models → honest-empty); paddleocr_indic maps hi/mr/ne/mai/sa/kok(→gom)/ur/sd to
native paddle models, rest honest-empty; anuvaad_tesseract uses hin+eng from its
own tessdata for Devanagari-family, honest-empty elsewhere; openbharatocr mirrors
tesseract_indic (documented path). Honest-empty is a CORRECT result — never "fix" it.

**easyocr routing — CORRECTED 2026-09-26.** This easyocr version routes by script
family, not per-language models: there are NO separate urdu.pth/assamese.pth
upstream (the audit's "download urdu.pth + assamese.pth" premise was wrong).
`ur`/`ks`/`sd` load the cached arabic.pth with the Urdu charset; `as` loads the
cached bengali.pth with the Assamese charset (known honest limit: ৰ/র confusion).
`EASY_FOR` now passes the native code (ur→["ur","en"], as→["as","en"], etc.) so the
correct character dictionary is used — same cached weights, no downloads.

**Engine #11 — sarvam_vision (user-approved trial, 2026-09-26).** Cloud OCR via the
Sarvam doc_ai digitise API (the "Sarvam Vision 2.1" class baseline the hackathon
bench references). Key read from env/`South/.env`; free-trial credits ONLY — every
call costs credits, so this engine runs with an explicit subset cap:
```bash
../../.venv311/bin/python run_probe.py --engine sarvam_vision --limit-per-lang 3
```
That is 54 calls (3 × 18 langs, ~5–8s each). Do NOT run it on all 1,227 items and
do NOT raise the cap without asking the user. Verified end-to-end 2026-09-26
(ks_o001/ks_o002/hi_d001: real text, HTML table tags stripped, ~4–8s/call).

Engine runs (one at a time; heavy engines sequential, never parallel), in this order:
```bash
cd /Users/srujansai/Desktop/South/level2/probe22
../../.venv311/bin/python run_probe.py --engine rapidocr --skip-existing --retry-errors
../../.venv311/bin/python run_probe.py --engine tesseract_bilingual --skip-existing
../../.venv311/bin/python run_probe.py --engine doctr --skip-existing
../../.venv311/bin/python run_probe.py --engine tesseract_indic --skip-existing
../../.venv311/bin/python run_probe.py --engine openbharatocr --skip-existing
../../.venv311/bin/python run_probe.py --engine anuvaad_tesseract --skip-existing
../../.venv311/bin/python run_probe.py --engine indicphotoocr --skip-existing
../../.venv311/bin/python run_probe.py --engine surya --skip-existing
../../.venv311/bin/python run_probe.py --engine easyocr --skip-existing
../../.venv311/bin/python run_probe.py --engine paddleocr_indic --skip-existing
../../.venv311/bin/python run_probe.py --engine sarvam_vision --limit-per-lang 3
```
rapidocr first: ~10 min, verifies the pipeline end-to-end (its 1,340 broken packs
all have non-null errors — `--retry-errors` rebuilds them; pack orphans for purged
items stay on disk harmlessly). Wall times measured 2026-09-26 on worst-case
4250×6500 scans: rapidocr ~10m; tesseract-family ~1.5–3h each; doctr ~2h; surya
~4h; easyocr ~6h; indicphotoocr ~12h (5 min/page worst case); paddleocr_indic
~8–20h with det cap (run last, overnight); sarvam_vision ~5–8s/call × 54 calls
(credit-capped, see above). If the process is killed mid-run
(OOM), resume with `--skip-existing` and report the image_id that killed it.

EN sanity column (engine-agnostic): after each local engine finishes, also run
```bash
../../.venv311/bin/python run_probe.py --engine <engine> --manifest en_sanity/manifest.json --skip-existing
```
(30 items, cheap, all local engines). EN CER above ~5 on these clean printed
English pairs means the harness is broken, not the language models.

Outputs: `out/<engine>/<lang>/<image_id>.json` packs (text, ms, error). Re-run with
`--skip-existing` to resume after interruption. Never delete a pack to "retry" —
rerun only packs whose JSON has a non-null error or empty text (`--retry-errors`).

---

## 6. PHASE 5 — score

Per engine, build the gt_pred file and score:
```bash
cd /Users/srujansai/Desktop/South/level2/probe22
../../.venv311/bin/python - <<'EOF'
import json, glob
rows = []
for p in glob.glob('out/<engine>/*/*.json'):
    d = json.load(open(p))
    rows.append({"image_name": d["image_id"], "gt": d.get("gt") or "", "pred": d.get("text") or "", "language": d["language"]})
json.dump(rows, open('preds_<engine>.json', 'w'), ensure_ascii=False)
EOF
../../.venv311/bin/python metrics.py --input preds_<engine>.json --normalize --overwrite
```
Then append one row per (image, model) to `sheet.csv` (columns:
image_id,language,script,print_or_hand,quality,has_table,mixed_script,gt,model,prediction,CER,WER,error_tag).
Use the fragment/manifest fields for the static columns; CER/WER from the metrics
results; error_tag from §6.1.

### 6.1 error_tag assignment (from metrics results + a manual skim of 5 worst rows/lang)
`matra_order | conjunct | old_scan | handwriting | table | reading_order | hallucination | repetition | charset | other`

### 6.2 GT-tier split + falsification test (mandatory in the final report)
Score every engine three times — official_pair only, official_pdf only,
sarvam_fill only — and report per-tier CER/WER per engine. In the headline
per-language means, EXCLUDE sarvam_fill items entirely (report them separately
as engine-agreement rates); cells with 100% fill (as, mni, sat) report
agreement, not CER. The falsification test: if an engine scores
disproportionately well against `official_pdf` GT but poorly against
`official_pair` GT (e.g. CER gap > 10 points), the PDF-layer GT is suspect for
that language — flag it; those languages' PDF-layer GT is barred from W6
training (see §9). Machine GT (sarvam_fill) is never ground truth for training.

### 6.3 Metric for Perso-Arabic scripts
For ur, sd, ks: report WER as the primary metric, CER secondary. Connected-script
glyph joins make CER over-count single visual errors. For all other languages CER
primary, WER tie-breaker.

### 6.4 Human GT verification (one agent, ~2h, run during Phase 5 engine runs)
Blind-verify against the image: (a) all 158 sarvam_fill items, (b) a stratified 10%
random sample of official_pdf items (~77, proportional per language, seed 20260926).
Write results to `gt_verification.json` (`{image_id: "pass"|"fail", ...}` + summary
counts). Any language with >20% verification failures gets its official_pdf GT
flagged in the report and barred from W6 training. Do NOT edit manifest.json.
R5 machine GT forensics (gt_forensics.json, 2026-09-26 21:46) already ran: ne BARRED
(trust 26.6 — e.g. ne_o037 GT contains control chars and broken glyphs); ks 45.0,
mr 46.8, gu 51.4, ur 59.0 VERIFY-FIRST. These verdicts feed this section: ne PDF-tier
GT is BARRED from W6 training (R5 forensics lock: trust 26.6, 32 control chars,
script_adherence 0.933, mojibake — governs over visual sample). The 90.5% visual
pass rate is on a biased sample (20 sarvam_fill + 1 PDF item); R5 full-set
forensics on 17 items is definitive. ks/mr/gu/ur PDF-tier GT must pass this §6.4
human verification before any W6 training use.

**§6.4 RESULT — LOCKED 2026-09-27 04:55 (machine-assisted visual pass, 233 items,
labeled "machine-verified (agent vision)"; 20-item human spot-check still pending
user review — see gt_verification.json human_spot_check):**
- **BARRED from W6 (fail >20% or R5 lock):** ks 0% (Nastaliq fragmentation +
  pipe/danda 1.0), mni 0% (fill GT extracted as garbage, adherence ~0), ur 10%
  (Syriac contamination), sat 15% (Ol Chiki broken), mr 42.9% (repetition +
  mojibake), ne PDF-tier (R5 lock STANDS — the visual sample for ne was 20 fill
  + 1 PDF item and cannot override the full-set forensics; do not re-classify ne
  as SAFE).
- **SAFE-FOR-SFT, pending §6.2 falsification test:** as 100%, brx 95.8%,
  doi 100%, kok 100%, mai 90.0%, or 91.7%, pa 100%.
- **VERIFY-FIRST, pending §6.2:** gu 85.7%, sd 85.7%.
- sarvam_fill tier stays excluded from SFT/RLVR per §9 regardless of pass rates.
- Consequence for reporting: mni and sat GT (fill-only, 0 human pairs) is
  unusable as ground truth — their engine CERs are measured against garbage;
  leaderboard rows for mni/sat must carry this caveat, and no winner claims
  per §6.7 (n=20 cells).
- Open items for the verdict agent: 4 visual items unaccounted (237 pending
  keys → 233 verified) — identify and account for them; update the stale
  summary note inside gt_verification.json.

### 6.5 Scoring rules now enforced by metrics.py (patched 2026-09-26 — no agent action needed, do not revert)
- Empty predictions score CER 1.0 / WER 1.0 and COUNT in every mean. Silence is
  failure, not exemption. (`missing_prediction` rows carry the flag for reporting.)
- Short-GT rows (<50 non-space GT chars — 27 items) are excluded from all means
  and reported separately (`short_gt_count`). They stay in the probe; packs are
  still built and scored.
- The old `equalize_space_only_issues` forgery (pred overwritten with GT → CER 0)
  is removed: word split/merge errors now score honestly.
- Uncapped CER is recorded per row (`cer_uncapped`) and summarized as
  `cer_100_count` so hallucination-grade failures are visible, not hidden by the
  1.0 cap. Means still use capped CER (runaway samples can't dominate).
- ONE denominator: avg_metrics and lang_wise_scores both use scored rows minus
  short-GT rows. Loops count. Loop/missing-excluded "valid_samples_*" fields are
  a secondary quality view only.
- LANG_ORDER now covers all 18 probe codes + the 10 legacy South-400 names; the
  summary TSV reports this probe correctly.

### 6.6 Raw-vs-normalized ablation (mandatory, cheap)
Run metrics.py twice per engine: with `--normalize` and without. Report the CER
delta per engine. If the rank order of engines flips between raw and normalized,
normalization is masking real differences — report both tables and use raw for
the W6 decision. This also gates RLVR (§9).

### 6.7 Statistical power statement (mandatory in the final report)
With CER sd≈0.3, minimum detectable pairwise gap: n=100 → ~8pp; n=70–90 →
~9–10pp; n=37 → ~14pp; n=24–27 → ~16–17pp; n=20 → ~19pp. Therefore: NO
per-language winner claims for n<50 cells (as, gu, ne, doi, mni, sat). Report
95% CIs everywhere. For decisions on small cells, pool script-family aggregates
(Devanagari: hi mr ne mai sa kok brx doi; Perso-Arabic: ur ks sd; Bengali-family:
bn as mni sat).

### 6.8 Baselines — RESOLVED 2026-09-26 (user approved; do not re-ask)
- **DONE — Sarvam Vision 2.1 API**: engine #11 `sarvam_vision`, free-trial key in
  `South/.env` (gitignored), run capped at `--limit-per-lang 3` (54 calls). This is
  the closest thing to a head-to-head with the hackathon bench — report it as
  "Sarvam API on our 3/lang subset through our scorer" and keep the 87.39 bench
  number directional unless the user funds a full 1,227-item API run.
- **DONE — easyocr ur/ks/sd/as upgrade**: EASY_FOR passes native codes; same cached
  script-family weights (arabic/bengali .pth), correct charsets. No download existed.
- **DONE — EN sanity column**: `en_sanity/manifest.json`, 30 official EN pairs,
  seed 20260926, run per §5.
- **NOT APPROVED — Bodhan** (bodhan-ai/indic-ocr): 1.5–2GB download + GPU; user
  chose the free Sarvam trial instead. P2; ask again only if W6 GPU budget appears.
- **NOT APPROVED — PaddleOCR-VL 1.6 / Qwen-VL zero-shot**: download + GPU. P2.
- **STILL MANUAL — old-scan/table stratification slice**: no labels exist; a human
  must tag ~100 pages before any denoiser/table claim (§9 Otsu guard).
Without a user-funded full Sarvam API run, "beat 87.39" stays directional — never
present it as a head-to-head number.

---

## 7. PHASE 6 — verification gates (each agent runs before reporting done)

1. Fragments exist for all 18 languages; merged manifest has `n_total == 1227`.
2. Every item has non-empty `gt` and a truthful `gt_source`; no item has GT <10 chars.
3. Per language: `n_official_pairs + n_official_pdf + n_sarvam_fill == n_drawn`
   (as 19, or 69 after noise-drop).
4. Engine pack counts from disk: `ls out/<engine>/*/*.json | wc -l` == items run;
   failures (non-null `error`) counted and reported, not hidden.
5. No file was written into `level2/out/`, `level2/reports/`, or `Datasets/`.
6. Scored rows in `sheet.csv` == packs with predictions; loops/missing counted by
   metrics.py and reported in the summary.
7. sarvam_vision packs on disk ≤ 3 per language (credit cap respected); en_sanity
   packs = 30 per engine that ran the EN column.

---

## 8. REPORTING (final message per agent)

```
AGENT <X> — <languages>
phase1: candidates per lang (clean/total, mojibake rejected)
phase3: drawn per lang (pairs/pdf/fill/failures)
engines: which ran, wall time, packs, failures
scores: per-engine overall CER/WER + per-lang table (fill excluded) + per-GT-tier
  table (§6.2) + agreement rates for as/mni/sat + raw-vs-normalized delta (§6.6)
verification: gt_verification.json pass/fail counts (§6.4)
power: CIs per cell; no winner claims for n<50 (§6.7)
gaps: encrypted/corrupt PDFs, shortfalls, anything honest-empty
```

Nothing else. No essays. No new markdown files outside the paths in this protocol.

---

## 9. W6 TRAINING GT GUARD (from hostile-audit reconciliation, 2026-09-26)

- SFT: human pairs (10,434 gold: bn 2,938 / hi 3,500 / sa 494 / en 3,500) +
  synthetic renders always allowed. PDF-layer GT allowed per language ONLY if
  §6.4 verification passed for that language AND §6.2 falsification test shows
  no pair-vs-pdf gap for that language.
- RLVR: rewards computed on human-verified gold GT ONLY. Never on unverified
  PDF layers or machine GT — RLVR against flawed GT optimizes the model to mimic
  the extractor's errors. RLVR also WAITS until the §6.6 ablation shows no
  engine rank inversion between raw and normalized scoring (a gameable scorer
  means a gameable reward).
- sarvam_fill GT: probe-scoring only (engine agreement), never training data.
- Akshara-boundary aux loss: scope to Indic-abugida scripts only (Devanagari +
  Bengali-Assamese family). It is undefined for Perso-Arabic (ur/ks/sd), Ol
  Chiki (sat), and Meitei Mayek (mni) — a single global aux loss silently
  misfires on 4+ of 18 languages.
- Preprocessing: "deskew + Otsu beats deep denoisers" is UNVERIFIED on this
  data (no old-scan labels exist — §1). Treat Otsu as the cheap baseline, run a
  denoiser ablation on a manual old-scan slice (§6.8) before claiming it.
- Curriculum granularity: derive per-item level from `set`
  (official_pair = crop/word-ish, official_pdf = page) — the field already
  encodes it; do not add manifest columns.
- Script router (sat/ks/mni/Nastaliq): decide only after §6.4 human
  verification and CIs exist — routing on unverified fill cells is routing on
  noise.
- Structured extraction head: parked until a forms/table slice exists (§6.8).

## 10. HOSTILE-AUDIT RECONCILIATION (2026-09-26 — do not re-litigate)

Three external hostile audits received; all reconciled against disk truth.
Adopted: GT<10 char drop (§5), per-tier scoring + falsification test (§6.2),
fill excluded from language means / agreement-only cells (§6.2), WER primary
for ur/sd/ks (§6.3), human verification (§6.4), scorer integrity patches
(empty=1.0 counted, no space-forgery, uncapped CER, single denominator,
18-lang LANG_ORDER — §6.5), raw-vs-normalized ablation (§6.6), power statement
+ no winners for n<50 (§6.7), baselines needing approval (§6.8), W6 guards
including akshara-aux scoping and Otsu softening (§9), sheet.csv reset
(380-row stale Sarvam-bench sheet archived as sheet.sarvam_bench.discarded.csv).
Rejected as stale/wrong (verified on disk after the fixes of 2026-09-26):
"paddle in en mode", "rapidocr returns empty / no caching", "_rapid NameError",
"control chars not stripped", "no random.seed", "dpi not enforced",
"surya missing", "protocol gate n_total==1800" (already corrected to 1227) —
all fixed/already-true at audit time; SEED=20260926 is used at
build_manifest.py:166, DPI=200 at :43. The proposed 3.5GB download batch is
unnecessary — rapidocr devanagari/arabic and all paddle models are cached;
easyocr's ur/assamese weights are the only real download candidates and they
are P1 (§6.8), not blockers. Qwen2-VL/InternVL2: P2, needs user-approved
downloads + GPU.

Third audit ("FINAL MERGED ULTIMATE VERDICT", verdict RUN AFTER P0) audited a
one-step-stale state (header n=1229, as 20, or 70). Its substantive P0 list was
already fixed on disk before the audit arrived: scorer integrity (§6.5),
per-tier scoring + falsification test (§6.2), power statement (§6.7), W6 guards
(§9), sheet.csv reset, protocol gates at 1227. Its one new claim — an Assamese
merge bug losing 11 official_pdf items — is FALSE, verified from
`manifest.json.pre-purge`: it contains all 31 as items (11 official_pdf + 20
sarvam_fill), identical to `manifest_fragments/as.json.pre-purge`; the 11 PDF
items were removed by the documented control-char corruption purge (GT gates,
§1 row "as"), not by merge. Post-audit resolutions shipped 2026-09-26:
`image_meta.json` (resolution metadata P1), Sarvam API baseline engine #11
(§6.8), EN sanity set, easyocr charset routing correction (§5). Still open:
§6.4 human GT verification, the manual old-scan slice, and the engine runs
themselves.
