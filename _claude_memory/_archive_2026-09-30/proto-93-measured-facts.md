---
name: proto-93-measured-facts
description: "Numbers the Opus planner measured on disk on 2026-09-29, each with the command that reproduces it — the quick-verify sheet for Sonnet before building on any figure"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:18:08.529Z
---

# MEASURED FACTS (2026-09-29, planner) — re-run the command before relying on a number

| # | Fact | Value | Reproduce with |
|---|---|---|---|
| F1 | probe22 manifest items | 1,283 | `python3 -c "import json;print(len(json.load(open('level2/probe22/manifest.json'))['items']))"` |
| F2 | additions | 56 (sd 25, mr 21, pa 10), created 2026-09-29 | `python3 -c "import json,collections;a=json.load(open('level2/probe22/manifest_additions.json'));print(a['n_total'],collections.Counter(i['language'] for i in a['items']))"` |
| F3 | sheet rows / models | 12,324 rows; 11 models (10 local + sarvam_vision) | `python3 -c "import csv,collections;r=list(csv.DictReader(open('level2/probe22/sheet.csv')));print(len(r),collections.Counter(x['model'] for x in r))"` |
| F4 | Sarvam paired result | 54 items (3/lang); surya mean CER < Sarvam in 10/18 langs (brx gu ks mai mr ne or pa sd ur); item-level surya 21 / Sarvam 28 / tie 5 | snippet in [[proto-11-w1a-packet-audit]] K1 |
| F5 | Sarvam per-lang means (paired items) | e.g. bn 0.089 vs surya 0.341; hi 0.084 vs 0.263; mni 0.023 vs 1.000; sa 0.019 vs surya 1.000 (best local 0.124); ks 0.630 vs 0.560 | same snippet |
| F6 | surya on sa | CER 1.000 on all 3 paired sa items (label "Ol Chiki bug" in EVIDENCE §3 is wrong — sa is Devanagari) | K6 in proto-11 |
| F7 | manifest variance | kok 2 PDFs/100 pages; pa 2/100; ur 38 PDFs, 34 items page≤1; ks 10 PDFs, 15 page≤1; bn/hi/sa pair ids spread (bn 32→3088, hi 18→3461, sa 22→506) | group manifest items by language: distinct `source_pdf`, `source_page`, count `source_page<=1`; pair ids via `os.readlink` on `level2/probe22/images/<lang>/*` |
| F8 | short languages (manifest) | as 19, mni 20, sat 20, gu 24, doi 27, ne 37, brx 67, or 69 | `collections.Counter(i['language'] for i in items)` |
| F9 | gu candidate pool | 220 PDFs, 13,406 pages scanned, 3,567 with text, 3,486 rejected mojibake/wrong script, 71 short/Latin, 10 candidates | `python3 -c "import json;d=json.load(open('level2/probe22/candidates/gu.json'));print({k:v for k,v in d.items() if not isinstance(v,list)})"` |
| F10 | gates | MIN_CHARS 50, MIN_SCRIPT_RATIO 0.5, MAX_LATIN_RATIO 0.6, MAX_CTRL_CHARS 3 | `sed -n '66,69p' level2/probe22/extract_gt.py` |
| F11 | South scored basis | 126 of 400 pages have CER (55 legacy_mojibake + 219 gt_thin nulled); by dominant script Tamil 53, Telugu 6, Kannada 4, Malayalam 4, Devanagari 16, Latin 43 | `sed -n '1,20p' level2/reports/CER_BY_SCRIPT.md \| cut -c1-300` and `level2/reports/CER_STAGE3B.json` |
| F12 | South labelled | 100 GT JSONs per language in `arc_level_1/labeled/{ta,te,kn,ml}/` | `ls arc_level_1/labeled/te \| wc -l` |
| F13 | South pack JSON has no CER | keys: page_id, source, lang, script, modality, domain, quality_tier, missing, unreadable_reason, ocr_engine, image, regions[text,text_nfc…], engine_meta | `python3 -c "import json;print(list(json.load(open('level2/out/easyocr/te/te_029.json')).keys()))"` |
| F14 | `level2/reports/MATRIX.csv` | 400 rows of character counts per engine — NOT CER | `head -2 level2/reports/MATRIX.csv` |
| F15 | sealed counts | level2/out 4,001 · level2/reports 48 · level2/probe22/out 13,289 · arc_level_1 413 | pre-flight loop in [[proto-02-preflight-and-checkpoints]] |
| F16 | engine coverage of additions | surya 43/56; `out/rapidocr` mr 121, pa 110, sd 125 files; easyocr/tesseract_indic 100 each for mr/pa/sd | `ls level2/probe22/out/<engine>/<lang> \| wc -l` |
| F17 | calendar | 2026-09-29 Tue · 09-30 Wed · 10-01 Thu · 10-04 Sun | `date -j -f %Y-%m-%d 2026-10-01 +%A` |
| F18 | duplicate strategy docs | `W5_BEAT_SARVAM_PLAN.md` ×3 (root, docs/architecture, docs/research/level7); `W5_STRATEGY_OPTIONS.md` ×2 (docs/architecture, docs/research/level7); `LIVE_LATEST_2026-09-29.md` ×2 (root, docs/research) | `find . -name 'W5_*.md' -not -path './_archive/*'` |
| F19 | fix_specs folder | did not exist on 2026-09-29 | `ls -d level2/probe22/fix_specs` |
| F20 | untracked src/ tree | `src/{data,evaluation,inference,models,pipeline,training,utils}`; training/trainer.py (QLoRA, GRPO RLVR, SFT), grpo_trainer.py; models: base, bodhan, glm_ocr, lighton_ocr, paddle_vl, qwen_vl; mtimes 19:53–20:07 IST | `git status --short src/; ls src/*` |
| F21 | multi-LLM evaluation | never executed; planned as "W4 — OpenCode + Claude + ChatGPT audit" at `docs/PLAN.md:23` | `grep -rln -E 'ChatGPT' --include='*.md' . \| grep -v _archive` |
| F22 | OpenCode skills | 217 entries in `~/.config/opencode/skills` | `ls ~/.config/opencode/skills \| wc -l` |

Related: [[campaign-state]], [[proto-11-w1a-packet-audit]], [[proto-12-w1b-benchmark22]], [[proto-21-w2-variance-and-resource]]

## Addendum 2026-09-29 20:55 IST (Sonnet lead) — paths changed by the cleanup agent
| F23 | 27 root docs moved (nothing lost) | `_reports/cleanup_cycle1/` (EVIDENCE_SUMMARY, PER_LANG_ROUTING, COMPUTE_BUDGET_ESTIMATE, PAPERTHIN_VINAY_AUDIT, LAYA_GATE_DECISIONS, ECC_VERIFICATION, DEEP_REPORT, INTEGRATION_REPORT, W6_HANDOFF…) · `_reports/research/` (MEETING_2026-09-29_STRUCTURED, PPT_FULL_DUMP, PPT_VS_SPEC_DIFF, LEVEL7_RESEARCH_FINDINGS) · `_reports/analysis/` (FILE_INVENTORY, DUPLICATE_MAP…). Root md now 20. Wherever a protocol names one of these at root, use the new path or `find`. | `find . -name '<file>' -not -path './.venv*' -not -path './Datasets/*'` |

## Addendum 2026-09-30 04:00 IST (Opus monitor)
| F24 | engine independence | openbharatocr ≈ tesseract_indic on 1,225/1,227; all three tesseract-family identical on only 370/1,227 (1A) — "10 independent" is not established | `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` |
| F25 | Sarvam paired by GT tier | pair_txt n=9: Sarvam 0.064 vs best local 0.243 · pdf_layer n=36: 0.311 vs 0.229 · sarvam_bench n=9: 0.278 vs 0.617 | proto-62 table command (sheet.csv × manifest gt_source) |
| F26 | sheet.csv provenance | no writer script on disk or in `_archive/`; not in git; CER re-derivable for 66–100/400 sampled rows | `grep -rl "sheet.csv" --include='*.py' .` ; EDGE_THESIS §4 |
| F27 | bench GT | indic-ocr-bench GT "reviewed twice by human language experts" (HF card) | COMPETITOR_INTEL §0.1 |
| F28 | 87.39 | word accuracy 100×(1−WER), unweighted macro over 22 Indic languages, n=6,609, English excluded | COMPETITOR_INTEL §0.2 |
| F29 | Nepali "Images and Transcriptions" | 193 XML files are Pascal-VOC boxes (176 `text` boxes, no transcription) — detection GT only, NOT recognition GT | open any `Datasets/akshardrishti_official/Nepali/Images and Transcriptions/*.xml` |
| F30 | official dataset per language | pairs only for bn (3,108 txt), hi (3,500), sa (496), en (3,500); ta 34 PDF+4 PNG, te 84 PDF, kn 41 PDF, ml 20 PDF+9 PNG; as 40, gu 220, pa 697, ur 106, sd 80 PDFs; doi 6, mni 10, sat 3, kok 3, ks 12, mai 12 PDFs; `test/test` 5,344 unlabelled JPGs (eval set, never train) | python walk of `Datasets/akshardrishti_official/` |
| F31 | level2 layout | 12 root files + 11 dirs; `models/` 4,035 files (4,000 symlinks); `unified/` 17,289 symlinks; `pages_400/` 400 symlinks; `probe22/` 98 loose root items | proto-70 inventory commands |
| F32 | git tracking | tracked: `level2/out/` 4,001, `level2/models/` 35; NOT tracked: `level2/probe22/out`, `images`, `scores`, `level2/reports`, `renders_shared`, `unified`, `pages_400` | `git ls-files <dir> \| wc -l` |
| F33 | path constants | ~30 constants in 25 scripts reference level2 dirs; 3 absolute paths (`engine_health_log.py:5`, `spot_check_engine.py:12`, `verify_engine_readiness.py:12`); `run_probe.py:218` reads `level2/research/smoke/anuvaad_tesseract/tessdata` | grep in proto-70 |
| F34 | two meeting packets | root `VINAY_MEETING_PACKET.md` 30.9 KB (corrected 09-30 01:33) vs `docs/architecture/VINAY_MEETING_PACKET.md` 6.7 KB (stale "tomorrow") | `ls -la` both |
| F35 | `.deps/IndicPhotoOCR` | 4.4 GB engine dependency used by `level2/run_engine.py:31`; `.kilo/worktrees` 31 MB | `du -sh .deps/* .kilo/*` |

## Addendum 2026-09-30 ~05:00 IST (Opus monitor, second pass)
| F36 | Punjabi K1 | `mcnemar_full_matrix.json` pairs/tesseract_indic_vs_surya/pa: n 90, ties 87, discordant 3 (1 vs 2), p=1.0, tie — KILL_CRITERIA.md:56 "p<0.0001, 88 discordant" is wrong (88 = other pairs) | python on `level2/probe22/scores/mcnemar_full_matrix.json` |
| F37 | McNemar pass definition | per-item pass = CER < 0.5 (`meta.cer_threshold: 0.5`); n_common_min 30; 606 of 1,045 triples computed | same file, `meta` |
| F38 | Konkani K1 | surya beats 7 other local engines at p≈0.0033–0.011 (n=100); 5 engines share an identical 7-vs-24 pattern — check for artefact | same file |
| F39 | probe coverage | print_or_hand printed 1,283 · has_table False 1,283 · quality unknown 983 / clean 300 | python on `manifest.json` |
| F40 | empty predictions | paddleocr_indic 100% empty on bn, brx, doi, gu, ks, mni, or, pa, sat (0% on hi/kok/mai/mr/ne); surya 100% on sa, 55% mni; anuvaad 100% on 9 langs; rapidocr 100% on 6 | python on `sheet.csv` (proto-82 table) |
| F41 | Tesseract language models on this Mac | `/opt/homebrew/share/tessdata`: eng hin kan mal tam tel (+osd, snum) · `level2/research/smoke/anuvaad_tesseract/tessdata`: anuvaad_kan/mal/tam/tel + eng hin · `level2/probe22/tessdata`: asm ben eng guj hin mar nep ori pan san snd urd | `ls` those dirs |
| F42 | fonts | macOS ships Noto Sans Meetei Mayek + October Meetei Mayek (several weights); Ol Chiki font not found by `fc-list \| grep -i chiki` — verify | `fc-list` |
| F43 | hackathon facts | CORRECTED: the "CER+CI/WER/S-D-I/sec-per-page" rubric is a STUDENT project's (github.com/Ayush-04-spec/akshardrishti), not the hackathon's — official scoring rules UNKNOWN. Search summaries: launched 12 Feb 2026, ₹1.10 crore pool, registration to 30 Mar 2026, targets handwritten + low-quality docs — all UNVERIFIED (official page not opened) | factchk 2026-09-30 |
| F44 | surya licence | weights "modified AI Pubs Open Rail-M license (free for research, personal use, and startups under $5M funding/revenue)" | `surya_ocr-0.22.1.dist-info/METADATA` line 99 via `docs/legal/LICENSE_AUDIT.md` |
| F45 | script-ID on disk | `.deps/IndicPhotoOCR/IndicPhotoOCR/script_identification/CLIP_identifier.py` (weights from anikde/STscriptdetect; licence TODO) | `ls` path |
| F46 | Wave 2 started before the meeting | `level2/unified/manifest_22.json` (1,683 items / 22 langs) + `reconcile_22.py` created ~03:30 IST 2026-09-30; `_reports/cleanup_cycle3/` dedup run wrote an 8.5 MB md (`DEDUP_CYCLE1_FILENAME_VARIANTS.md`) | `ls -la` |
| F47 | paddle map omission | `run_probe.py:84-88` PADDLE_LANG has no `brx`/`doi` (Devanagari) → 100% empty; comment at :80-83 calls them honest-empty | `sed -n '80,90p' level2/probe22/run_probe.py` |
| F48 | surya ignores language | `level2/run_engine.py` `ocr_surya(image_path, lang)` does not use `lang`; sa emptiness is image/model-side | `grep -n "def ocr_surya" -A 45 level2/run_engine.py` |

## Addendum 2026-09-30 ~06:00 IST (opened sources for Plan v2)
| F49 | market table (Sarvam blog, opened) | Sarvam 87.39 · Bodhan 84.94 · Gemini 3.6 Flash 79.35 · Google Cloud Vision 71.76 · Surya OCR 2 69.96 · Mistral OCR4 69.16 · Opus 5 68.81 · Gemma 4 65.53 · Chandra-OCR2 64.56 · GPT 6 Astra 63.69 · Infinity-Parser2 Pro 49.83 · Azure Vision 4.0 41.29 · AWS Textract 4.64 | https://www.sarvam.ai/blogs/sarvam-vision-2-1 |
| F50 | surya vs Sarvam per language (same page) | bn 81.79/93.47 · hi 86.12/93.52 · kok 90.81/97.41 · pa 83.06/89.16 | same |
| F51 | indic-ocr-bench (HF card, opened) | Apache-2.0; 6,909 test + 1,173 small_representative; 23 langs; GT reviewed twice by human experts; semantic blocks; metrics.py; freely downloadable | https://huggingface.co/datasets/sarvamai/indic-ocr-bench |
| F52 | speed on this Mac | surya median 16.3 s/page; tesseract 0.7–3.5 s; easyocr 30.7 s; paddle 95.2 s → surya on 5,344 test images ≈ 24 h | `level2/reports/LATENCY.md` |
| F53 | indic-ocr tessdata licence | page states none | https://github.com/indic-ocr/indic-ocr.github.io |

## Addendum 2026-09-30 ~14:45 IST (Plan v3 sources, opened)
| F54 | Bodhan vs Sarvam per language (Sarvam page) | ks 48.04/54.82 · or 75.45/80.01 · gu 83.26/88.87 · bn 90.87/93.47 · hi 90.99/93.52 · pa 86.51/89.16 · mni 82.85/85.12 · kok 95.99/97.41 · sat 68.30/53.91 (Bodhan ahead) | https://www.sarvam.ai/blogs/sarvam-vision-2-1 |
| F55 | Bodhan card | IndicDocLayout 33M + IndicBlockOCR 0.8B (Qwen3.5-0.8B, Sarvam-30B tokenizer); printed EN+22, handwriting EN+12; IndicOCR-PR 86.2, IndicOCR-HW 66.7; Indic Open Model License v1.0 (commercial + fine-tune OK, attribution, same-licence derivatives, hosted API needs written approval, commercial licence above 500M MAU/$250M revenue) | https://huggingface.co/bodhan-ai/indic-ocr |
| F56 | MLX port | 4-bit 636 MB, ~391 ms/crop; 8-bit 1.0 GB; bf16 1.6 GB; input = block crops | https://huggingface.co/hari31416/indic-ocr-mlx-4bit |
| F57 | mlx-vlm LoRA | supports Qwen2/3/3.5-VL LoRA/QLoRA on Apple Silicon; dataset needs `images` + `messages` | context7 /blaizzy/mlx-vlm (LORA.MD) |
| F58 | 600K-KS-OCR | ~602k Kashmiri word images 256×64, CC-BY-4.0, ~10.6 GB | https://arxiv.org/abs/2601.01088v1 |
| F59 | unread strategy doc | docs/research/DEEP_RESEARCH_STRATEGY_2026-09-29.md proposed Bodhan base; errors: licence "Apache 2.0", cloud budget, unsourced P(beat), RL on the benchmark split (leakage) | local file |
| F60 | HF MCP | `claude mcp add hf-mcp-server -t http https://huggingface.co/mcp?login` | https://github.com/huggingface/hf-mcp-server |
| F61 | Laya install state (corrected 2026-09-30 ~15:30) | South: not in `.venv`/`.venv311`. Machine: `laya 0.3.5` in Homebrew Python 3.14 user site since 2026-09-22 23:09 IST but `import laya` fails (no numpy/torch/transformers); the only working copy is `~/Desktop/swa-erp/.venv-laya` (torch 2.14.0, transformers 5.17.0, MPS); no Laya weights in `~/.cache/huggingface/hub`; no real Laya call in the OCR pipeline ("laya" hits in level2 = "Malayalam") | `/opt/homebrew/bin/python3 -c 'import laya'`; `~/Desktop/swa-erp/.venv-laya/bin/python -c 'import laya, torch'`; `grep -rnE '^\s*(import\|from) laya' --include='*.py' .` |
| F62 | PyPI laya | 0.3.22 (Sep 29 2026), Apache-2.0, Convai Innovations, text classifier ("System 1 decision engine"), `pip install laya` | https://pypi.org/project/laya/ |
| F63 | src/ LayaRouter defects | no `import laya`; routes from gt_text (leak); ignores chosen engine; Meetei Mayek mapped to 'Mend' (should be 'Mtei') | `src/inference/laya_router.py`, `src/pipeline/end_to_end.py:58-75` |
| F64 | Laya's own Indic accuracy note | English checkpoint "collapsing to near-random on non-Latin scripts (Hindi 0.100 … Tamil 0.113 at 20 options, where random is 0.050)"; "Script detection is exact" (Unicode ranges) | `sed -n '1,12p' ~/Library/Python/3.14/lib/python/site-packages/laya/lang.py` |
| F65 | research volume | `docs/research/` = 571 files, 4.7 MB: 86 md + 446 json + 36 jsonl + 3 other; `level7/a/LEDGER.md` 655 KB / 7,070 lines; 34 of the 35 md in `level7/b` are "converted from X.jsonl" copies | `find docs/research -type f \| wc -l`; `du -sh docs/research` |
| F66 | archive + report volume | `_archive/` 519 files (~215 MB), `_reports/` 58 files — 0 tracked in git; `_archive/campaign_drafts_2026-09-30`: 61/73 sha-identical to live files; 45 probe JSONs (194 MB) in `_archive/cleanup_2026-09-28`: 9 identical to the same-named live file, 20 differ, 16 no same-named live file; repo-wide 69 exact-dup md/txt groups (71 redundant copies) | `git ls-files _archive \| wc -l`; `find _archive -type f \| wc -l`; `shasum -a 256` compares |
| F67 | AGENTS.md dead pointers | KEY FILES cites `_reports/research/MEETING_2026-09-29_STRUCTURED.md` and `docs/research/uni_v3_ORIGINAL_2026-09-29.md` — both missing; live copies: `docs/research/MEETING_2026-09-29_STRUCTURED.md`, `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt` | `ls` each path |
| F68 | competing plan/claim docs | written 2026-09-30 14:46–15:09: `docs/research/W6_STRATEGY_UNIFIED.md` ("Final Plan"), `PROBE22_EDGE_ANALYSIS.md` ("Where We Beat Sarvam Vision 2.1", STRATEGY-AGENT-1), `ACTUAL_PROBE22_RESULTS.md` ("vs Sarvam" column), `SURYA_LIVE_INFERENCE_RESULTS.md` (n = 3 brx) — not reconciled with proto-89 or proto-62 | `ls -l docs/research/*.md`; `head` each |
| F69 | official judging (R6, VERIFIED official page snapshot 2026-09-26) | jury criteria: approach/innovation · business use case · technical feasibility · product roadmap · team · addressable market; no metric or formula published; named outputs: layout-preserving JSON, searchable PDF, language detection, transliteration, context-based correction; eval scope includes handwriting, forms, multi-script, degraded scans | `docs/research/R6_COMPETITION_INTEL.md` §1–§5 |
| F70 | 4-bit vs Arabic script | QARI (2B VLM): CER 3.45 at 4-bit vs 0.091 at 8-bit | `docs/research/R2_NASTALIQ_FORENSICS.md` §B6 (arxiv 2506.02295) |
| F71 | ensemble voting (B12, 115 South pages) | full ensemble beats all single engines on 0/115 pages; ≥3-family agreement: 5-gram precision 0.598 vs 0.355 but recall 0.046 | `level2/research/gates/B12_ensemble_voting.md` §1, §3 |
| F72 | Vinay's GPUs | "Anyhow, we have our own GPU resources. So we'll be able to do that." (Sep 10 sync, closing) | `textutil -convert txt -stdout "_archive/cleanup_2026-09-28/root_clutter/sync - ocr - September 10.docx" \| tail -5` |
