# Lane C3 — Data-Collection Strategy Ledger (quality-first, remaining languages)

Lane: C3 (Miss Agent). Date locked: 2026-09-26. No downloads executed — every URL is a pointer, not a fetch (§9 hard rule).
Record format (campaign-mandatory): `source_url | date | VERIFIED/INFERENCE | relevance/recency/actionability | 3–10 line extraction`.
IDs C3-001…; verdicts that consume them live in STRATEGY.md (same dir). Nothing at root, nothing under level2/research/.

## Scoring note
Weak cells steer ranking (Santali 53.91, Kashmiri 54.82, OldScan 55.3, Odia 80.01). Score = R×R×A; ≥30/125 enters the integrated architecture.
VERIFIED = confirmed against disk truth or live-source excerpt fetched 2026-09-26. INFERENCE = deduced, flagged, never a training license.

---

## S0 — Standing law + disk truth (purge lessons, R5 forensics)

- C3-001 | `level2/probe22/AGENT_PROTOCOL.md §1` (disk) | 2026-09-26 | VERIFIED | 5/5/5
  - Honesty gates that every future GT candidate must pass: length ≥50 chars, target-script ratio ≥0.5, Latin ratio ≤0.6, control chars ≤3 (MAX_CTRL_CHARS=3 hardened after purge).
  - Purge removed 111 control-char-corrupt PDF-layer items (as 11, gu 6, mr 21, ne 29, or 9, pa 10, sd 25); manifest 1340→1229, then 2 noise items (GT<10 chars) → n=1227.
  - Never relax gates to hit a count (§3 gate review). Maps to all weak cells: any new source inherits these gates verbatim.

- C3-002 | `level2/probe22/gt_forensics.json` R5 (disk) | 2026-09-26 | VERIFIED | 5/5/5
  - Machine GT forensics trust scores: ne BARRED 26.6 (GT visibly corrupt, e.g. ne_o037 control chars + broken glyphs); ks 45.0, mr 46.8, gu 51.4, ur 59.0 VERIFY-FIRST.
  - Kashmiri PDF trust ≈ 29–45/100: no ks/ur/sd/gu/mr PDF-layer line trains until §6.4 human verification passes AND §6.2 falsification shows no pair-vs-pdf gap.
  - Maps to ks/ur/sd strategy: synthetic-first (R2 flood) because the only large real ks pool is untrusted.

- C3-003 | `level2/probe22/AGENT_PROTOCOL.md §9` + `docs/research/R7_W6_TRAINING_TREE.md` (disk) | 2026-09-26 | VERIFIED | 5/5/5
  - SFT allow-list: human pairs (10,432 gold: bn 2938/hi 3500/sa 494/en 3500) + synthetic (S6 gold-by-construction) always; PDF-layer GT per-language ONLY on §6.4 pass + §6.2 gap ≤10pp; sarvam_fill NEVER trains; RLVR on human-verified gold ONLY after §6.6 no-inversion.
  - Akshara-aux scoped to Indic abugidas only — undefined for ur/ks/sd (Perso-Arabic), sat (Ol Chiki), mni (Mayek).
  - Mixing ratios (R7): S1 L1 100% ×2ep; S2 L1:L2 70:30 ×1ep; S3 L1:L2:L3 50:20:30 ×1ep; RLVR ≤20 GPU-h; L2-fail share reverts to L1, never to fill.

- C3-004 | `OCR_AGENT_MEMORY_FEED.md §9` + `level2/probe22/AGENT_PROTOCOL.md §0` (disk) | 2026-09-26 | VERIFIED | 5/5/4
  - Hard law: no downloads without explicit user yes; no training before freeze; no 400-page sets for remaining languages; `level2/out/` + `level2/reports/` sealed; count from disk; honest labels (fill declared as fill).
  - `Bodo/gu/` (4,645 jpgs + Gujarati vocab) is a copy of the main test set — NOT GT, never use; `test/test/` 5,344 unlabeled = hackathon eval set, never train.
  - Maps to WHAT-NOT-TO-COLLECT (§S7 STRATEGY.md): provenance violations end the campaign.

- C3-005 | `level2/probe22/AGENT_PROTOCOL.md §1` composition table (disk) | 2026-09-26 | VERIFIED | 5/5/5
  - Final manifest n=1227: bn/hi/sa 100 pairs each; ks/kok/mai/ur 100 PDF; pa 90, mr 79, sd 75, or 69, brx 67 PDF; ne 37, gu 24, doi 27, as 19, mni 20, sat 20 (fill-heavy).
  - 100%-fill cells (as/mni/sat) are agreement-only, never CER claims, never training (§6.2/§6.7; n<50 = no winner claims).
  - Collection implication: as/mni/sat have ZERO trusted real lines — synthetic-only bootstrap (R3) + fresh human gold is the only legal path.

- C3-006 | `docs/research/R2_NASTALIQ_FORENSICS.md §C3` (disk) | 2026-09-26 | VERIFIED | 5/4/5
  - Synthetic-vs-human verdict for Nastaliq VLM-SFT: QARI 0.550→0.061 CER on 50k pure-synthetic SFT of Qwen2-VL-2B (49-pt closure); UTRSet synth-only 75.14% vs real-trained 90.87% (15-pt residual for CTC-era); +500 real lines stack −6.13% relative WER on top.
  - Mixing rule derived: 40–60k synthetic curriculum + 300–500 hand-corrected REAL ks lines; last 5–15 pts need real anchors, not more synth volume.
  - Never a 400-page collection: the real-line budget is hundreds of lines, mined from the probe + hand-corrected.

- C3-007 | `docs/research/R3_OLCHIKI_MAYEK_SYNTHETIC.md §C3` (disk) | 2026-09-26 | VERIFIED | 5/4/5
  - Synthetic-only reaches classical-OCR parity on printed Indic docs (Nayana CER 0.227 ≈ Tesseract 0.206) and rescues zero-corpus scripts (Maltese LV-ROVER); correction-stage synth beats real-data training (Bourne −55% CER) with under- > over-corruption.
  - Counter-guard: synthetic benchmark scores do NOT predict real-scan rank (Devanagari stress-test: 9/10 collapse on real scans) — synth-val is a gate, never a claim; synth NEVER eval (§B0).
  - Mixing rule derived: synthetic SFT base (≥100k renders/script) → human-gold fine-tune/RLVR on verified real lines only.

- C3-008 | `docs/research/R4_OLDSCAN_RESTORATION.md` (disk, per R7 N5d binding refs) | 2026-09-26 | VERIFIED | 4/4/5
  - OldScan cell (55.3) has NO labeled slice on our data — Otsu is the cheap baseline until a manual old-scan ablation passes (A0 none / A1 deskew+Otsu / A2 Sauvola-frozen / A3 DocRes-head pilot n≤8); adopt bar median ΔCER ≤−0.03, 95% bootstrap CI, ≥2/3 frozen engines.
  - DIBCO is Latin/Greek-only — no Indic transfer; methods reference only, never training data for our scripts.
  - Collection implication: do NOT collect a restoration training set; collect only a ~40-page manual old-scan eval slice (human-tagged, P1 §6.8).

---

## S1 — Kashmiri / Urdu / Sindhi (Nastaliq + Perso-Arabic)

- C3-009 | https://arxiv.org/abs/2601.01088 | 2026-01-03 | VERIFIED | 5/5/5
  - 600k-ks-ocr: ~602,000 word-level 256×64 Kashmiri-script images, 3 traditional Kashmiri typefaces, degradation augmentation + diverse backgrounds, GT in CRNN/TrOCR/ML formats, 10 archives ~10.6 GB.
  - License CC-BY-4.0 — hackathon-SFT-safe with attribution; single biggest legal ks fuel found. SFT-safe (synthetic gold-by-construction), NEVER eval.
  - Gap vs R2 flood: word-level only — line/block curriculum still needs R2§C2 rendering from KS-LIT-3M strings.

- C3-010 | https://arxiv.org/pdf/2601.01091 | 2026-01 (INFERENCE: year from arXiv id) | VERIFIED | 5/5/5
  - KS-LIT-3M: 3.1M words / 16.4M chars curated Kashmiri text (literary, journalistic, academic, religious; multi-decade), built via a purpose-built InPage-to-Unicode converter preserving Kashmiri diacritics; released CC-BY-4.0.
  - Usable as R2§C2 render-string source (SFT-safe sampling base, NOT GT labels) — solves the "Kashmiri text corpora, not just Urdu corpora" requirement incl. Kashmiri-Yeh coverage when rendered in Awami ≥3.300/Gulzar.
  - Verify at freeze: script mix (Perso-Arabic vs Devanagari Kashmiri) via the ≥80% script-ratio gate before sampling.

- C3-011 | https://arxiv.org/html/2601.16113v1 | 2026-01 | VERIFIED | 5/5/5
  - SynthOCR-Gen: open-source low-resource synthetic OCR generator (Unicode corpus + fonts in, CRNN/TrOCR/PaddleOCR/Tesseract/HF-compatible sets out); 25+ augmentations; validated by generating the 600k Kashmiri set above.
  - Tool license open (paper claims open-source; confirm MIT/Apache file at freeze before import). Candidate 3rd chassis alongside TRDG/SynthTIGER (R3§B2 decision-at-freeze).
  - Method replicable per weak-cell language: sat/mni need only Unicode corpus + OFL font — matches our R3 spec exactly.

- C3-012 | https://github.com/Faizaniqbal52/Koshur-Pixel | 2026 (repo live at search) | VERIFIED | 4/4/3
  - Koshur-Pixel repo fronts the same 600k Kashmiri synthetic release; dataset card states CC-BY-4.0 with attribution required.
  - Role: access pointer / mirror check at freeze (prefer canonical HF `Omarrran/600k_KS_OCR_Word_Segmented_Dataset` per the paper: 600k samples, 487k words, 89,743 unique, 90/10 split, seed 42).
  - INFERENCE: repo vs dataset-host parity unverified — confirm checksums before any approval request.

- C3-013 | https://huggingface.co/datasets/Omarrran/kashmiri_multilingual_dictionary_dataset | 2024-11-16 | VERIFIED | 3/4/4
  - 16,598-entry EN–ks–ur–zh–tr dictionary, Kashmiri in Perso-Arabic script (avg 10.65 chars, 99.55% complete), UTF-8 CSV, license Apache-2.0.
  - Usable as Kashmiri word-level render strings (SFT-safe sampling base) + rare-word booster for the R2 coverage sampler; example sentences (~42 chars avg) usable as short-line strings.
  - Dictionary-register caveat: not running prose — mix ≤10% of render strings, never a style majority.

- C3-014 | https://arxiv.org/html/2306.15782v1 | 2023-06-27 | VERIFIED | 5/3/4
  - UTRNet paper: only 6 Urdu datasets existed (UPTI, IIITH, UNHD, CENPARMI, CALAM, PMU-UD); only UPTI had train-scale volume and it is synthetic with limited diversity; UTRSet-Real 11k+ real lines + UTRSet-Synth 20k introduced.
  - Key training datum: UPTI-trained → 54.84% on Real (cross-domain collapse); Synth-only → 75.14% vs Real-trained 90.87% — the 15-pt residual that justifies our synth+real mixing rule.
  - UrduDoc line-detection bench included — layout-harness reference, not OCR GT.

- C3-015 | https://huggingface.co/datasets/abdur75648/UTRSet-Real | 2023–2025 | VERIFIED | 4/3/3
  - UTRSet-Real mirror: 11k+ manually annotated printed-Urdu lines, diverse fonts/sizes/colors/orientations; license CC-BY-NC-4.0; HF copy currently near-empty (4.21 kB — actually download from project page / author agreement).
  - Paper states release "subject to request + no-cost license agreement" — approval-gated; NC clause bars product deployment, allows hackathon research. Probe/eval-usable (real human GT), SFT-usable inside hackathon only with agreement on file.
  - Paired UTRNet-Large/Small models same NC license — eval baselines only, never distill into product weights without counsel.

- C3-016 | https://github.com/ZainMunawar01/UTRNet-Updated | 2023–2025 | VERIFIED | 3/3/3
  - Code + Urdu-Synth generator module + links for UTRSet-Real/Synth, IIITH-corrected, UPTI-source; UrduDoc available under the same no-cost agreement (contact authors).
  - Role: generator-recipe reference for the R2 40–60k curriculum (font×degradation matrix), not a data download.
  - Access pattern confirms the lane's rule: gated academic sets need a paper-trail request before freeze, never silent scraping.

- C3-017 | http://www.lrec-conf.org/proceedings/lrec2026/pdf/2026.lrec2026-1.235.pdf | 2026 | VERIFIED | 5/5/4
  - Press-to-Pixels / UNB: 829 manually annotated Nastaliq newspaper blocks (9,982 sentences, 9,758 unique words) + OpenITI 250+250 Naskh/Nastaliq; YOLOv11x block extraction + SwinIR SR (+50% avg accuracy); Gemini-2.5-Pro WER 0.133 UNB; 500-line GPT-4o FT → −6.13% WER.
  - Best REAL Nastaliq eval candidate for ks/ur transfer (human-annotated blocks); license/URL for data release to confirm at freeze (paper says UNB + fine-tuned models are publicly released — locate canonical host before approval request).
  - TrOCR best classical on OpenITI-Nastaliq (WER 0.451/CER 0.177) — honest classical baseline for the falsification comparison.

- C3-018 | https://data.mendeley.com/datasets/mhy5vxnths/1 | 2025-06 | VERIFIED | 4/4/4
  - RAVI: 99,000 Urdu word images, 256×256, Jameel Noori Nastaleeq size-40, black-on-white, alphabet-foldered (arabic_reshaper pipeline), CNN-benchmarked.
  - SFT-safe word-stage fuel for ur (and ks only as style-distractor — Jameel Noori Regular under-renders Kashmiri Yeh per R2§A4; weight accordingly).
  - Mendeley hosting = approval-gated download with dataset DOI — clean provenance for the ledger.

- C3-019 | https://cle.org.pk/clestore/index.htm | live 2026-09-26 | VERIFIED | 4/3/4
  - CLE (KICS/UET Lahore): Urdu Digest corpora 100K/500K/1M + font-size-graded text corpora (14–40pt) + POS/IOB-tagged sets; free for academic non-commercial research, processing fees apply, commercial licensing available on request.
  - Graded font-size text corpora double as render-string sources with size metadata; IMAGE corpora (+corresponding texts) are probe/eval candidates — confirm Nastaliq vs Naskh split at freeze.
  - License posture matches hackathon research use; fees + request paper-trail go in the ledger before any download approval.

- C3-020 | https://112.cachefly.net/urduhack/awesome-urdu | live 2026-09-26 | VERIFIED | 3/4/4
  - awesome-urdu index: UFAL 5.4M-sentence Urdu corpus, OSCAR/CC-100/WMT-Raw crawls, urwiki dumps + WiToKit, Leipzig corpora, Makhzan, U-HAT handwriting, 45k ligature set, Cursive-Text scene bench (2.5k, email-gated), CLE Urdu image corpora.
  - Role: source index for render-string mining (urwiki/CC dumps with script gates), NOT a dataset itself; commercial-licensed corpora (UrduWaC/urTenTen/LDCIL) explicitly excluded from free use.
  - Wikipedia-derived strings inherit CC-BY-SA — share-alike handling per C3-licensing section.

- C3-021 | https://en.wikipedia.org/wiki/Urdu_Wikipedia | 2026-06-22 | VERIFIED | 3/3/4
  - Urdu Wikipedia: active since 2004, CC-BY-SA 4.0 (+GFDL dual), dump-processable; alongside Kashmiri (11,565 articles) and Sindhi (22,194) editions on the same page.
  - Render-string source for ur/ks/sd sampling bases (ks/sd editions small — expect heavy filtering; gate every line, never bulk-assume script).
  - Share-alike flows to renders question — flag for organizer/license check at freeze (see S5).

- C3-022 | https://www.rekhta.org/CMS/about-site | live 2026-09-26 | VERIFIED | 2/3/2
  - Rekhta: 30k+ ghazals/nazms of 2,500+ poets, digitized library ~200k books / 32M pages (per Wikipedia 2026-08-21), Urdu-script primary + Devanagari/Roman mirrors.
  - © commercial foundation, 5-free-pages regime — SAMPLE STRINGS ONLY with permission; bulk scrape/sampling PROHIBITED (what-NOT-to-collect list).
  - Poetry-register caveat even if licensed later: gazal meter ≠ prose OCR domain — style-mix cap applies.

- C3-023 | https://github.com/mirfan899/Urdu | live 2026-09-26 | VERIFIED | 3/3/3
  - MIT-licensed Urdu NLP collection (POS/NER/sentiment/QA/news 1M/spaCy); text-side reusable as render strings where license is MIT; Dropbox-linked subsets need per-file verification.
  - NLP labels (POS/NER) do NOT transfer to OCR GT — text reuse only, never label reuse.
  - 72★/19-fork community maintenance — liveness check at freeze before citing in approvals.

- C3-024 | https://github.com/Nawadiraat/Urdu-OCR/blob/main/README.md | live 2026-09-26 | VERIFIED | 3/4/3
  - Community Tesseract-Urdu retrain (Apache-2.0): custom nawadraat_urdu traineddata beats stock urd; reports BCER 27.1% / BWER 63.1% — honest mid-tier classical baseline.
  - Role: engine/baseline reference + training-dataset pointer (their "Training Dataset" link), not SFT data itself.
  - Validates the R2 structural verdict: LSTM/CTC-era Urdu sits ~27% BCER — autoregressive SFT is the gap-closer, not more CTC tuning.

- C3-025 | https://github.com/H0NEYP0T-466/URDU-OCR-CNN | 2025-11-28 | VERIFIED | 2/4/2
  - MIT Urdu handwriting CNN app indexing Kaggle sets (handwritten-urdu-characters, printed-Urdu-Nastalique/UCOM, UHAT 38-class, CALAM via FAST-NUCES contact).
  - Kaggle-hosted sets inherit Kaggle terms + uploader provenance risk — quarantine: verify uploader + original paper license before any approval request; handwriting char-level ≠ our printed line/block domain anyway.
  - Useful only as a pointer list; no direct collection.

- C3-026 | https://www.sciencedirect.com/science/article/pii/S1319157818311649 | 2021 (INFERENCE: journal page confirms Dootio, cited 26×) | VERIFIED | 3/2/4
  - Dootio Sindhi text corpus (JKSUCI): feature-distribution + variation + sentiment analysis corpus for Sindhi — render-string candidate for sd sampling base.
  - Script split mandatory at freeze: Sindhi runs Perso-Arabic AND Devanagari — gate every sampled line to the probe's sd script (protocol §1) before rendering.
  - Access/license to confirm (ScienceDirect page; institutional-gated?) — no approval request until host + terms verified.

- C3-027 | https://salrc.uchicago.edu/resources/fonts/available/sindhi/nafeespaknaskhsindhi.shtml | live (via R2 citation) | VERIFIED | 3/3/4
  - Nafees Pakistani Naskh/Sindhi font family + CRULP Sindhi/Urdu wordlists — sd render-string + Naskh-distractor font source for style-separation training (R2§C2).
  - Academic resource page — confirm redistribution terms at freeze; rendering locally for SFT is the conservative posture (no font redistribution).

- C3-028 | http://openslr.org/122 | live 2026-09-26 | VERIFIED | 2/3/2
  - OpenSLR SLR122: transcribed Kashmiri speech (394 MB) + transcripts, license GPL-3.0-or-later, with post-processing scripts at github.com/erstan/kscp.
  - Transcripts are render-string-usable in principle, BUT GPL-3.0 copyleft attaches on distribution — quarantine: counsel/organizer check before any use; speech transcripts also carry spoken-register + transcript-convention noise.
  - Default posture: DO NOT USE unless the license question is affirmatively cleared (what-NOT list).

- C3-029 | https://archive.org/stream/in.ernet.dli.2015.24175/2015.24175.A-Dictionary-Of-The-Kashmiri-Language_djvu.txt | 1932 (Grierson) | VERIFIED | 2/2/3
  - Grierson Kashmiri dictionary full text (public-domain age): documents Kashmiri in Sharada/Nagari/Perso-Arabic with the note that Perso-Arabic spelling is "fairly constant" but the alphabet "quite unsuited" — historical confirmation of the ks Perso-Arabic pain.
  - Render-string value LOW (archaic lexis, mixed transliteration schemes, OCR-of-scan noise in the djvu.txt itself) — allowed (public domain) but down-weighted; never GT.
  - INFERENCE: exact public-domain status per jurisdiction unreviewed — re-confirm before any approval request.

- C3-030 | https://software.sil.org/awami/release-3-300 | 2024-10 | VERIFIED | 5/4/5
  - SIL Awami Nastaliq v3.300 explicitly ADDED Kashmiri (+Gojri) support — proof pre-2024 Nastaliq fonts under-render Kashmiri; OFL-licensed SIL font.
  - Mandatory font in the ks render matrix (R2§C2); Google-Fonts-streamlined Awami may lack coverage — use the SIL release, test with ks Yeh strings (U+0620 per C3-031).
  - License: OFL-1.1 — render-for-SFT safe, bundle-per-§7 rules.

- C3-031 | https://www.unicode.org/wg2/docs/n3673.pdf | 2009 (proposal L2/09-215) | VERIFIED | 4/2/5
  - Kashmiri Yeh U+0620 (+2nd Kashmiri char), palatalization marker with distinct half-yeh Nastaliq form, attested in Weekly Sangarmal + primers.
  - Coverage gate for ks renders: every synthetic batch must include U+0620 strings rendered in ks-capable fonts; zero-ink/tofu clusters fail the batch (R3§B4 shaping-fidelity rule generalized).
  - Sangarmal archive = potential real-ks text pointer (verify host + terms at freeze).

- C3-032 | https://github.com/notofonts/nastaliq/releases | live 2026-09-26 | VERIFIED | 4/4/4
  - Noto Nastaliq Urdu v3.004→v4.000 shaping fixes (low-alef, U+0768 noon-small-tah, nukta-over-lam) — same Unicode string rasterizes differently across versions; pin EXACT font version in the provenance sidecar.
  - OFL Noto workhorse for the ur render matrix alongside Jameel-Noori-class cuts (R2§C2).
  - Version-pinning rule generalizes: every render batch records font+version (R3§B4.6 sidecar).

- C3-033 | https://urdufonts.net/fonts/jameel-noori-nastaleeq-kasheeda + https://urdufonts.net/fonts/jameel-noori-nastaleeq-regular?jmlVVPJ8=fc3MoVSPW | live (via R2 citation) | VERIFIED | 3/3/2
  - Jameel Noori Regular (4.7M+ downloads) vs Kasheeda (5.7M+) differ in elongation/baseline-histogram behavior — both needed for kashida coverage in renders.
  - License UNCLEAR (free-download host, no OFL statement found this pass) — QUARANTINE: render-locally-only posture pending license verification; NEVER redistribute the font files; prefer OFL cuts (Awami/Gulzar/Noto/Alvi-verified) for any shared artifact.
  - INFERENCE: "free download ≈ training-render OK" is NOT established — organizer check at freeze.

- C3-034 | https://github.com/lecramyajiv/fonts-nastaliq | live (via R2 citation) | VERIFIED | 3/3/4
  - Community Nastaliq font pack (Gulzar, Hussaini, Mehr cuts): convenient ks-capable inventory, but per-file licenses must be verified individually (Google-Fonts OFL items safe; others quarantined).
  - Role: inventory pointer, not a download approval — each font needs its own ledger line before use.

- C3-035 | https://arxiv.org/html/2606.07167v1 | 2026-06 (UrduMMLU pipeline doc, via R2 citation) | VERIFIED | 4/4/5
  - Production Urdu normalization fix: RTL marks, LRI…PDI isolates for Latin/digit fragments, NFKC + Arabic-letter normalization, punctuation map (۔ ، ؟) — the exact pre-scoring pipeline our §6.3/§9 mandates.
  - 3–8 pts of ks/ur/sd CER may be scoring artifact without it — normalization is a GT-quality gate (scoring side), not optional post-processing.
  - Adopt verbatim into the verification harness before any ks/ur/sd SFT data decision.

- C3-036 | https://arxiv.org/abs/2408.15119 | 2024-08 (PARSeq-Urdu, via R2 citation) | VERIFIED | 4/3/4
  - PARSeq-Urdu: permuted-autoregressive transformer, CER 0.178 on ~160k Urdu word images — honest classical SOTA and the Path-#3 hedge (word-model + line wrapper for ur/sd floor).
  - Data implication: word-level ur renders (RAVI C3-018 + 600k-style pipeline) feed this hedge; ks capped by Kashmiri-Yeh OOV — documented limit, not a data gap to fill with volume.
  - 160k word-image scale sets the ur word-stage budget reference.

---

## S2 — Santali / Ol Chiki

- C3-037 | https://github.com/facebookresearch/flores/blob/main/flores200/README.md?plain=1 | live 2026-09-26 | VERIFIED | 5/4/5
  - FLORES-200: 3,001 professionally translated sentences (dev/devtest/test-hidden), ~21 words/sent, CC-BY-SA-4.0; sat_Olck slice confirmed in R3 (HF mirrors: Muennighoff CC-BY-SA C3-038, SEACrowd CC-BY-NC variant C3-039 — use the canonical CC-BY-SA source).
  - SFT-safe render-string source for sat (≈60k+ words) + mni slice (verify script tag — historically mni_Beng; gate before sampling).
  - NEVER eval: test split hidden; our renders are synthetic by construction (§B0) — dev/devtest text may seed renders but no rendered line enters any eval split.

- C3-038 | https://huggingface.co/datasets/Muennighoff/flores200/blob/main/flores200.py | live 2026-09-26 | VERIFIED | 4/4/4
  - HF FLORES-200 mirror documents: 842 distinct web articles → 3,001 sentences, formerly EN-sourced with later multi-source translation workflow, license CC-BY-SA-4.0, per-language configs.
  - Confirms volume math for the ledger: per-language slice is small (3k sents) — sufficient as bootstrap + rare-char booster, NOT as sole sampling base (pair with sat.wiki C3-040).
  - Share-alike compliance: keep license file with any derived render set; flag organizer question on model-output share-alike scope (S5).

- C3-039 | https://huggingface.co/datasets/SEACrowd/flores200/blob/main/README.md | 2024-06-20 | VERIFIED | 2/4/2
  - SEACrowd FLORES-200 re-host is CC-BY-NC-4.0 (differs from canonical CC-BY-SA) — DO NOT SOURCE from this mirror; NC + re-host provenance risk.
  - Ledger lesson: mirrors change licenses — always trace to the canonical host (facebookresearch/Open Language Data Initiative) before approval requests.
  - FLORES+ successor (openlanguagedata/flores_plus, CC-BY-SA-4.0, gated) confirms the canonical family stays share-alike, not NC.

- C3-040 | https://en.wikipedia.org/wiki/Santali_Wikipedia | live 2026-09-26 | VERIFIED | 4/3/5
  - Santali Wikipedia: ~15,928 articles, 11,414 users, launched 2018-08-02, CC-BY-SA dumps — largest Ol-Chiki-script running-text pool available without approval-gating.
  - Mandatory §B1 gate (≥80% chars U+1C50–1C7F): most Santali digital text is NOT Ol Chiki (Bengali/Devanagari/Odia/Latin per R3§A3 + ICDAR-2023-HW) — dump + NFC + gate + per-char histogram (N≥500/char) is the first post-approval runnable.
  - Stub-article noise expected — word/line granularity sampling absorbs it; blocks only from long-article filter.

- C3-041 | https://github.com/sami42200/santali-nlp | live 2026-09-26 | VERIFIED | 3/4/4
  - santali-nlp: first dedicated Santali (Ol Chiki) NLP suite — corpus + tokenizer + fastText + MT baselines; repo-scale (unquantified — count post-approval).
  - Render-string candidate + tokenizer prior for rare-char analysis; license per repo file to confirm at freeze (no bulk use until verified).
  - INFERENCE: "first dedicated" is the repo's claim — treat as pointer, verify volume before budgeting sampler share.

- C3-042 | http://www.language-archives.org/language/sat | live (via R3 citation) | VERIFIED | 3/3/3
  - OLAC Santali: Rosetta Genesis/glossed text, Swadesh lists, grammar/orthography sketches, Glottolog sant1410; Crúbadán sat + sat-Deva web-crawl wordlists (Scannell 2018).
  - Word-list scale (10⁴–10⁵ tokens est.) — rare-word/rare-char booster material, not running-prose base; per-record openness varies — check record-level terms.
  - Script-mixed by nature — the §B1 gate decides keep vs route per line, never bulk trust.

- C3-043 | https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2024/Printed-OCR-for-Extremely-Low-resource-Indic-Languages.pdf | 2024-10-04 | VERIFIED | 5/4/5
  - Mozhi-LR paper: synthetic Mozhi-LR(S) + real Mozhi-LR(R) word-level sets for 9 low-resource langs incl. Santali (Ol Chiki), Sindhi, Maithili, Kashmiri, Bodo, Dogri, Konkani, Nepali, Sanskrit; real = 20–25 book pages/lang flatbed-scanned 300 DPI, manually box-annotated; train-on-synthetic → fine-tune-on-real.
  - THE precedent recipe for our lane: synth-train + real-finetune with public code/data at github.com/ALIKSARKAR/Printed-OCR-for-Extremely-Low-resource-Indic-Languages.
  - Script honesty inside: Santali multi-script (Bengali/Odia/Devanagari/Ol Chiki), Kashmiri Devanagari+Perso-Arabic — their real pages for ks are Devanagari-script (NOT our Nastaliq cell) — verify script per file before any eval use.

- C3-044 | https://link.springer.com/chapter/10.1007/978-3-031-93691-3_9 | 2025 (Springer chapter of C3-043) | VERIFIED | 3/3/3
  - Peer-reviewed (Springer) version of the Mozhi-LR work — strengthens citation weight for the validation call; same data artifacts as C3-043.
  - Springer page may sit behind access control — cite the open IIIT PDF (C3-043) as the working copy.
  - No new data beyond C3-043 — listed for provenance completeness, not double-counted in budgets.

- C3-045 | https://arxiv.org/abs/2205.02543 | 2022 (EkStep/Tarento bench, via R3 citation) | VERIFIED | 4/3/4
  - 90k-image 23-Indic-lang synthetic OCR bench WITH Santali-Ol-Chiki charset row (Manipuri row stale Devanagari — pre-Mayek-switch, do not reuse for mni).
  - SFT-safe synth fuel / recipe reference for the sat render matrix; confirms Ol Chiki render feasibility at bench scale since 2022.
  - Access via arXiv + authors — verify current host at freeze.

- C3-046 | https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2023/icdar2033_tr.pdf | 2023 (ICDAR HW competition, via R3 citation) | VERIFIED | 3/3/3
  - ICDAR-2023 Indic handwriting competition: Santali among 22 langs, multi-script incl. Ol Chiki; confirms "Santali uses Ol Chiki/Bengali/Odia scripts" (the contamination warning's citation).
  - Competition set, organizer-gated access — eval-candidate pointer only; handwriting domain ≠ our printed probe (tag domain before any use).
  - No approval request until terms + script split per file are confirmed.

- C3-047 | https://fonts.google.com/noto/specimen/Noto+Sans+Ol+Chiki | live 2026-09-26 | VERIFIED | 5/4/5
  - Noto Sans Ol Chiki: OFL-1.1, 4 weights (400–700), ~55 glyphs; the ONLY verified OFL Ol-Chiki design — glyph diversity ≈ weight×size×degradation only.
  - Single-design constraint drives the R3 mitigations: degradation-heavy diversity, TRDG distortion, held-weight-700 + held-seed synth-val.
  - Distro packages (Alpine font-noto-ol-chiki) + Fontsource npm give approval-clean install paths — record exact version in sidecar.

- C3-048 | https://www.unicode.org/charts/PDF/U1C50.pdf + https://r12a.github.io/scripts/olck/sat.html | Unicode 5.1 (2008); r12a updated 2026-04-28 | VERIFIED | 4/5/5
  - Ol Chiki block U+1C50–U+1C7F: 48/48 assigned (10 digits + 30 letters + 6 modifiers + 2 punctuation); true ALPHABET (no inherent vowel, no conjuncts, no reordering; uniform height, no descenders); LTR.
  - Shaping consequence locks the pipeline: Pillow BASIC renders correctly; RAQM preferred for uniformity (single code path with Mayek).
  - Gate regex `[\u1C50-\u1C7F]` ≥80% — load-bearing against Bengali-script Santali poisoning (probe sat_14 failure mode).

- C3-049 | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2228697&lang=1&reg=3 | 2026-02-16 | VERIFIED | 2/5/2
  - GoI Ol-Chiki centenary (1925–2025): presidential inaugural, ₹100 commemorative coin + stamp, Santali in Eighth Schedule since 2003; prior scripts Roman/Bengali/Odia/Devanagari.
  - Context only: institutional momentum → more Mayek/Ol-Chiki print volume over time; zero data artifact — not budgeted as a source.
  - Recency 5 (Feb 2026) supports the "Mayek/Ol-Chiki digital volume is young and growing" sampling assumption.

- C3-050 | https://literature.santals.in/ | live (via R3 citation) | VERIFIED | 2/3/2
  - santals.in native Ol-Chiki prose blog: © site — sample strings only, NO bulk scrape without say-so (what-NOT list).
  - Style value (native prose register) IF permission granted later; until then excluded from all volume math.
  - Permission request (if ever) goes through the user, never agent-initiated contact.

- C3-051 | https://github.com/sayantanr/indic-olchiki-transliterator | live 2026-09-26 | VERIFIED | 2/4/3
  - Indic→Ol-Chiki transliterator app (indic-transliteration lib + Roman→Ol-Chiki phonetic map): pipeline candidate for converting Bengali-script Santali (abundant) into Ol-Chiki render strings.
  - VERIFICATION GATE REQUIRED: transliterated strings are machine-derived — sample-verify (native check, ≥95% word accuracy on a 500-line sample) before any render use; failed sample = route stays Bengali-renderer, never Ol-Chiki.
  - Tool license per repo — confirm before pipeline import.

- C3-052 | https://www.omniglot.com/writing/olchiki.htm | live (via R3 citation) | VERIFIED | 2/3/2
  - Omniglot Ol-Chiki page links community fonts with MIXED/UNCLEAR licenses — DO NOT USE for training renders until per-font license verified (R3§A2 quarantine).
  - Reference value only (script background, 1925 Murmu origin cross-check).
  - Ledger rule instantiated: link-lists are not licenses.

---

## S3 — Manipuri / Meitei Mayek

- C3-053 | https://huggingface.co/datasets/DayanandaThokchom/english-TO-meitei-mayek | live 2026-09-26 | VERIFIED | 4/4/4
  - 461,345 EN↔mni_Mtei pairs (train 415k / val 23k / test 23k), MIT license, normalized, tokenizer-ready; example verified Mayek-script (ꯑꯩ ꯆꯥꯛ…).
  - Largest Mayek-script string pool found — SFT-safe render-string base with translationese-style caveat (MT-derived Mayek needs the §B1 gate + histogram check like any other source).
  - MIT = hackathon-safe incl. downstream; gated HF (contact-share accept) — user-side accept at freeze.

- C3-054 | http://agnee.tezu.ernet.in:8082/jspui/bitstream/1994/1707/5/05_chapter%201.pdf | thesis Ch.1 (work started 2017) | VERIFIED | 3/2/4
  - TUMMHCD: 85,124 handwritten Mayek character images (72,330 train / 12,794 test), created because NO public Mayek dataset existed in 2017; CNN 98.70% / KNN-LBP 98.16% on 35-class subsets.
  - Handwriting + char-level + thesis-hosted access — eval-candidate pointer for a future handwriting slice, NOT printed-line SFT; access/terms via Tezpur repository at freeze.
  - Documents the zero-baseline history: our printed-Mayek synth program has almost no real-data predecessor to contradict it.

- C3-055 | https://ieee-dataport.org/documents/meitei-mayek-handwritten-character-dataset-37-classes | 2019 (DOI 10.21227/pjtc-bw69) | VERIFIED | 3/3/3
  - Hijam Mayek HW set: 60,285 character images, 37 classes, 90/10 split, two-phase collection; IEEE DataPort hosted with DOI citation.
  - IEEE DataPort = subscription/terms-gated — eval-pointer only; confirm license + script-coverage (37 vs 55-class Mayek27 vs full modern set) before any request.
  - Handwriting domain — excluded from printed-SFT budgets regardless of access.

- C3-056 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9679442 | 2022 (Khuman et al.) | VERIFIED | 4/3/4
  - Benchmark PRINTED Mayek-script character dataset (open PMC article) + entropy skew-detection/correction work for printed Mayek OCR.
  - Closest thing to a real printed-Mayek eval anchor: locate the dataset host + terms at freeze; char-level granularity → eval-slice use, never line-SFT fuel.
  - Skew-correction method reference for the Mayek preprocess arm (abugida vowel-sign headroom interacts with deskew — R3§B2 line-height rule).

- C3-057 | https://www.semanticscholar.org/paper/An-OCR-system-for-the-Meetei-Mayek-script-Ghosh-Barman/9dbf01dceb5e03119e64c193a1c2d6cb90b1133c | 2013-12-01 (DOI 10.1109/NCVPRIPG.2013.6776228) | VERIFIED | 3/2/3
  - Ghosh et al. Mayek OCR: preprocess→segment→classify, ~96% on a moderate database — classical ceiling reference for the mni cell.
  - 2013 system, closed test set — precedent value only (segmentation-cascade fragility consistent with R2 Part-A physics generalized).
  - No data artifact — listed so the validation call cannot claim "no prior Mayek OCR exists."

- C3-058 | https://www.kaggle.com/datasets/saurabhshahane/manipuri-handwritten-character-recognition/data | live 2026-09-26 | VERIFIED | 2/3/2
  - Kaggle 5k+ handwritten Mayek char set — Kaggle terms + uploader provenance risk + handwriting domain = triple quarantine; pointer only.
  - Same bucket as C3-025: Kaggle sets need uploader→paper license tracing before any approval request.

- C3-059 | https://github.com/galax19ksh/Handwritten-Meitei-Mayek-Recognition | 2024-04-08 | VERIFIED | 2/3/3
  - Community CNN (PyTorch, 90% test) trained on Deena et al. full-charset Mayek HW database (1,200+ images/class, 55 classes) — confirms a 55-class modern-coverage HW source exists behind the paper.
  - Pointer to the Deena et al. 2021 database custodians; access + terms at freeze; printed-SFT excluded (domain), eval-slice candidate (future HW work only).
  - MIT/unspecified repo license — verify before reusing any code.

- C3-060 | https://fonts.google.com/noto/specimen/Noto+Sans+Meetei+Mayek | live 2026-09-26 | VERIFIED | 5/4/5
  - Noto Sans Meetei Mayek: OFL-1.1, 9 weights (100–900), 92 glyphs / 87 chars incl. Extensions block — TRAIN-side design in the font-disjoint split.
  - 9-weight range gives real glyph diversity (unlike Ol Chiki's 4) — weight is a first-class sampler dimension for mni.
  - Distro package (Alpine font-noto-meetei-mayek) = approval-clean install path.

- C3-061 | https://github.com/silnrsi/font-eeyek | live 2026-09-26 | VERIFIED | 5/4/5
  - SIL Eeyek: OFL-1.1 (RFN "Eeyek"), independent second Mayek design (glyphs © 1999–2019 Chingambam/Tabish) — held EXCLUSIVELY for synth-val (font-disjoint generalization test, R3§B4.5).
  - Debian packaged (fonts-eeyek) — approval-clean install; legacy GPL-2.0+ Eeyek-Unicode Windows font (SUSE) is EXCLUDED (copyleft — what-NOT list).
  - Two-OFL-design position is strictly better than Ol Chiki — train-Noto/val-Eeyek is the mni quality edge.

- C3-062 | https://en.wikipedia.org/wiki/Hueiyen_Lanpao + https://www.hueiyenlanpao.com/ | live (via R3 citation) | VERIFIED | 3/3/2
  - Hueiyen Lanpao Mayek edition: daily since 1978, only market Mayek daily, circulation ~21–23k/day — largest modern Mayek prose pool in principle.
  - © newspaper — sample strings only, no bulk scrape (what-NOT list); volume counted only post-permission (never in current budgets).
  - Block-render style reference (column width for the 15% block ladder) even without text reuse — layout observation is not copying.

- C3-063 | https://en.wikipedia.org/wiki/Meitei_language | live (via R3 citation) | VERIFIED | 3/3/3
  - EM Corpus (Huidrom 2021, Waseda, first mni–eng comparable, BENGALI script) + Assam ₹6cr corpus program + govt grants: existence confirmed, contents/script/access unverified.
  - Bengali-script mni usable for LANGUAGE sampling only after transliteration (same verification gate as C3-051); Assam program = ask-don't-assume pointer.
  - mni Wikipedia edition EXISTS but article count NOT verified — TODO-verify at freeze, never quote a number (R3§A7 honesty carryover).

- C3-064 | https://www.unicode.org/charts/nameslist/n_ABC0.html + https://unicode.org/L2/L2008/08239r-n3478r-meetei-mayek-ext.pdf | Unicode 5.2 (2009) | VERIFIED | 4/3/5
  - Mayek modern block U+ABC0–ABFF (56 assigned: 27 Iyek-Ipee + 8 Lonsum ABDB–ABE2 + 7–8 dependent signs ABE3–ABEA + Apun ABED + Lum ABEC + Cheikhei ABEB + digits ABF0–ABF9) + historic Extensions U+AAE0–AAFF.
  - Gate rules locked: modern line kept iff ≥80% ∈ U+ABC0–ABFF; historic quarantined ≤2%; NFC normalization (vowel-sign order sensitive).
  - HarfBuzz MANDATORY (ABE3–ABEA + ABED misplace under Pillow BASIC); `language="mni"` tag; abort run if `features.check("raqm")` false.

- C3-065 | https://unicode.org/cldr/charts/45/summary/mni_Mtei.html | CLDR 45 (via R3 citation) | VERIFIED | 3/3/4
  - CLDR mni_Mtei exemplars (letters ꯀ–ꯪ + Lum/Apun, ABF0–ABF9 default digits) — seed word/number lists for the sampler + digit-booster wordlists.
  - Unicode-terms reuse — safe; seed-scale only, never a volume source.

- C3-066 | https://www.thehindu.com/news/national/newspapers-the-last-holdouts-of-bengali-script-in-manipur-given-ultimatum-to-switch-to-meetei-mayek-next-month/article66214312.ece | 2022-12-03 | VERIFIED | 3/3/3
  - Manipur ordered Bengali→Mayek phase-out (Official Language Act amendment; newspapers off Bengali script Jan-2023) — Mayek print volume growing but young; Bengali-script Manipuri abundant but wrong-script.
  - Sampling consequence: expect Bengali-script contamination in any mni crawl — the Mayek ≥80% gate is load-bearing, not decorative.
  - Recency 3 (2022) — re-check at freeze whether the switchover completed (affects real-Mayek page availability).

---

## S4 — Odia (80.01 cell: weakest NON-fill cell with real GT)

- C3-067 | https://huggingface.co/datasets/OdiaGenAIOCR/odia-ocr-merged | live 2026-09-26 | VERIFIED | 5/4/4
  - 192,000+ merged Odia OCR samples: 64 word-doc + 182,152 char-level 32×32 (47 OHCS chars, MIT tell2jyoti) + 10,000+ Mozhi printed words (academic license).
  - SPLIT-license verdict: char-level MIT slice = SFT-safe for char-stage warm-up ONLY (32px isolated chars ≠ page OCR — granularity mismatch, never line-SFT fuel); Mozhi slice inherits academic terms (eval-side, confirm CVIT terms); 64-sample lipi slice inherits CC-BY-NC-SA (C3-069).
  - Biggest Odia pointer found — but mostly char-level: the or cell needs LINE/BLOCK data (probe or_69 PDF tier + C3-069/070 eval anchors), not more chars.

- C3-068 | https://huggingface.co/datasets/shantipriya/odia-ocr-merged | live 2026-09-26 | VERIFIED | 4/4/3
  - Independent mirror of the same 192k merge (same 3 sources, same split licenses) by Shantipriya Parida — confirms the merge recipe is reproducible; prefer ONE canonical source at freeze (dedupe, never double-count volume).
  - Feeds the Qwen2.5-VL-3B Odia fine-tune (C3-071, 58,720 validated pairs) — mirror→model provenance chain is ledger-clean.
  - License ⊕: respect all three upstream licenses; "Open" ≠ single license — record per-slice terms.

- C3-069 | https://huggingface.co/datasets/OdiaGenAIOCR/Odia-lipi-ocr-data | 2026 | VERIFIED | 5/5/4
  - Odia Lipi Project (with AHRC IIT Bhubaneswar): scanned pages + HUMAN-VALIDATED Odia text, printed focus, extensible to handwriting/multimodal; sources incl. Odia Bibhaba curated old literature (odiabibhaba.in); CC-BY-NC-SA-4.0, gated (contact-share accept).
  - Best REAL Odia eval anchor: human-validated page pairs. NC clause = hackathon-research OK, product/deployment NOT — SFT-use inside hackathon only, deployment retraining excluded.
  - Current size <1K (64-sample root + growth) — eval-slice scale, never SFT-volume; re-check size at freeze (project is extending).

- C3-070 | https://huggingface.co/datasets/OdiaGenAIOCR/odia_ocr_benchmark_data | 2026 | VERIFIED | 4/5/4
  - Same org, 223-row image→GT bench slice (id/image/ground_truth/category), CC-BY-NC-SA-4.0 — second real-Odia eval anchor; category field may support error-tag stratification.
  - 223 rows ≈ our or_69 probe tier scale — combine as eval (probe + lipi + bench) for CI-grade or claims (pooled n≈350+, §6.7 power).
  - Same NC posture as C3-069 — eval-side, hackathon-only.

- C3-071 | https://github.com/shantipriyap/odia-ocr-qwen-finetuned | 2026-02-21 | VERIFIED | 5/5/5
  - Qwen2.5-VL-3B-Instruct Odia FT (Apache-2.0): 58,720 validated pairs, 98/2 split, LR 2e-4, bf16, 3 epochs ≈ 4h on A100-80GB, loss 5.5→0.09, CER 20–40% by doc type, exact-match 40–70%.
  - STRONGEST mixing precedent for our budget: ~59k pairs × 3ep ≈ 4 GPU-h at 3B scale — our S3 stage (50:20:30, ≤30 GPU-h at ≤2B) is conservatively budgeted against this.
  - 98/2 split is eval-thin (1,155 lines) — our protocol keeps probe/eval strictly separate from any such FT eval; never co-mingle.

- C3-072 | https://huggingface.co/datasets/abhilash88/odia-text-corpus | ~2026-02 | VERIFIED | 4/4/4
  - 801 MB Odia text corpus (100K–1M rows), CC-BY-4.0 — SFT-safe render-string base for or synthetic line/block curriculum (attribution only).
  - Text-only (no images) — pairs with OFL Odia fonts (verify Noto Sans Oriya OFL at freeze, C3-078) under the R3-spec pipeline ported to Oriya script.
  - 801 MB scale ≈ 10⁶-line render potential — sufficient or-synth base without any new collection.

- C3-073 | https://aclanthology.org/people/priyanka-pattnaik/unverified (OdiEnCorp 2.0) | 2020–2021 | VERIFIED | 3/3/3
  - OdiEnCorp 2.0: 98,302 EN–OR sentences, 1.69M EN / 1.47M OR tokens, largest EN-OR parallel at release; PARTLY OCR-EXTRACTED from scans; free for non-commercial research.
  - OCR-extracted subset carries extractor-noise risk — quarantine: text-side render strings ONLY, and down-weight/drop lines failing the or script-ratio gate (extractor mojibake filter doubles as quality gate).
  - Translationese + OCR-noise double caveat — ≤20% sampler share, never booster material.

- C3-074 | https://indicnlp.ai4bharat.org/corpora | live 2026-09-26 | VERIFIED | 4/3/4
  - IndicCorp (AI4Bharat): or slice 0.69M articles → 6.94M sentences / 107M tokens (news/magazines/books, deduped, shuffled); license CC-BY-NC-4.0.
  - SFT-safe render-string volume for or inside hackathon research; NC bars product-training reuse — tag every derived render batch NC-lineage in the sidecar.
  - Cross-check C3-072 (CC-BY-4.0, cleaner license) as the default or base; IndicCorp as overflow only.

- C3-075 | https://huggingface.co/datasets/ai4bharat/IndicCorpV2 | 2023 (ACL) | VERIFIED | 3/4/4
  - IndicCorpV2: ACL-2023 pretraining data, datasets CC-0, models+code MIT — the CLEANEST AI4Bharat license in the family; verify or-language coverage at freeze (v1 or = 6.94M sents; v2 coverage per paper).
  - IF or covered under CC-0 → promotes to DEFAULT or render-string base (no NC lineage); else fall back to C3-072/C3-074.
  - INFERENCE: or-in-v2 unconfirmed this pass — flagged TODO-verify, never assumed.

- C3-076 | https://huggingface.co/datasets/ai4bharat/indicdlp | 2025 (ICDAR Oral, Best Student Paper runner-up) | VERIFIED | 4/5/4
  - IndicDLP: 119,806 layout-annotated doc images (COCO JSON via Shoonya/Label-Studio), 12 domains (textbooks, question papers, newspapers…), 42 layout classes, INCL Odia (+10 Indic + EN); MIT license.
  - Layout-harness data (reading-order/block segmentation for the OldScan/table arm), NOT OCR GT — role-separated per §9 (extraction head parked until forms slice exists).
  - MIT + scanned+born-digital mix + or coverage = the single best legal layout prior; verify or-image count at freeze.

- C3-077 | https://openodia.com/ + https://pypi.org/project/openodia | 2026 (openodia 0.1.13, 2026-08-07) | VERIFIED | 3/5/3
  - OpenOdia hub (MIT hub) + openodia PyPI (MIT, py3.11+): live registry of every Odia-tagged HF model/dataset with licenses+sizes+citations; tools/fonts/keyboards/OCR/NLP directory.
  - Role: living index — re-query at freeze for or sources newer than this ledger (project is actively maintained, tutorials via OdiaGenAI/TFUG-Bhubaneswar).
  - Awesome-Odia-AI list (odisha-ml) is the contribution funnel — watch it for new or-OCR drops through the hackathon window.

- C3-078 | https://github.com/AI4Bharat/indicnlp_catalog | live 2026-09-26 | VERIFIED | 3/3/4
  - indicnlp_catalog: Charles Univ EN-OR parallel v1+v2, MTEnglish2Odia 42k, FLORES-101/200 (24 Indic), Samanantar 49.6M (INCL Oriya), ULCA/Bhashini platform pointers.
  - EN–OR parallel rows are render-string candidates (translationese-capped share); catalog itself is the or-source checklist at freeze.
  - INFERENCE: per-item licenses vary (Samanantar/CC, Charles-Univ terms) — verify per item, never inherit the catalog's openness.

---

## S5 — Licensing for hackathon use (verified texts)

- C3-079 | https://spdx.org/licenses/OFL-1.1.html + https://software.sil.org/oflt | OFL 1.1 (2007-02-26); FAQ update7 Nov 2023 | VERIFIED | 5/3/5
  - OFL core: use/study/copy/merge/embed/modify/redistribute/sell copies freely; fonts (incl. derivatives) may bundle/embed/sell WITH software incl. commercial; cannot sell the font BY ITSELF; derivatives renaming rule under RFN.
  - Load-bearing sentence: "requirement for fonts to remain under this license does NOT apply to any DOCUMENT created using the fonts or their derivatives" — rendered training images + trained model weights are not font redistribution (standard reading; counsel-confirmed at freeze for the final packet).
  - Full OFL text must accompany redistribution (or relink per 1.10/1.15 for embeds) — keep OFL.txt with any shared render set.

- C3-080 | https://software.sil.org/fonts/faq | updated 2025-10-15 | VERIFIED | 4/5/4
  - SIL: all fonts OFL, "permits ANY use, electronic or printed"; bundling with commercial apps allowed with restrictions; modifications allowed (glyph add/remove); Google-Fonts versions may support FEWER chars/behaviors — TEST with real language text, prefer SIL originals.
  - Directly actioned: Awami from SIL release page (C3-030), Eeyek from silnrsi GitHub (C3-061) — never the streamlined GF copies for ks/mni renders.
  - "No intention to ever charge" + versions stay free/libre — long-horizon safety for the render pipeline.

- C3-081 | FLORES canonical license (https://github.com/facebookresearch/flores + HF C3-038 + FLORES+ C3-openlanguagedata/flores_plus) | 2022–2026 | VERIFIED | 4/4/4
  - FLORES-200 family license: CC-BY-SA-4.0 (canonical + Muennighoff mirror + FLORES+ gated repo) — attribution + share-alike; FLORES+ adds gated accept + integrity tests + hidden-test protection.
  - OPEN QUESTION for freeze (INFERENCE — no ruling found this pass): does CC-BY-SA attach to (a) synthetic images rendered from BY-SA sentences, (b) model weights trained on them? Conservative posture: attribute + document lineage in sidecars; ask organizers; prefer CC-0/CC-BY/MIT bases (C3-075, C3-053, C3-072) for the MAJORITY share so the question is low-stakes.
  - Never touch the hidden test split; never eval on renders of dev/devtest (synth-never-eval §B0 anyway).

- C3-082 | CC-BY-NC family (UTRSet C3-015, Odia-Lipi C3-069/070, IndicCorp C3-074, SEACrowd mirror C3-039) | various | VERIFIED | 4/3/4
  - NC rule: non-commercial research (hackathon) USE allowed; product deployment, commercial API serving, or weights-transfer-to-product BARRED without re-license.
  - Operational consequence: NC-derived lines (UTRSet SFT inside hackathon, lipi eval, IndicCorp renders) carry an NC-LINEAGE tag in the provenance sidecar; the R7 tree's "L2/L3 always allowed" implicitly means hackathon-scope — the FINAL PLAN must re-derive the product-training allow-list excluding NC lineage.
  - INFERENCE: hackathon = non-commercial is assumed from the event's research framing — confirm in the rules refresh (C2 lane owns competition intel; cross-check before freeze).

- C3-083 | MIT / Apache-2.0 tool+data slice (TRDG C3-087, SynthTIGER C3-088, Augraphy C3-090, openodia C3-077, mni 461k C3-053, Kashmiri dict C3-013, BharatSceneText Apache-2.0 C3-084, IndicDLP MIT C3-076) | various | VERIFIED | 4/4/5
  - MIT/Apache-2.0 = full hackathon + product reuse (preserve copyright/license notices; Apache-2.0 patent grant is a bonus for the model artifacts).
  - Prefer MIT/Apache/CC-0/CC-BY sources for any line that might survive into product training — license-hygiene is a data-selection criterion, not paperwork afterthought.
  - BharatSceneTextDataset (Bhashini-IITJ, Apache-2.0, 13 Indic scene-text langs) = eval-side scene-text anchor where script coverage matches; verify per-language file list at freeze.

- C3-084 | https://github.com/Bhashini-IITJ/BharatSceneTextDataset/blob/main/LICENSE | live 2026-09-26 | VERIFIED | 3/4/3
  - Apache-2.0 large-scale scene-text set, 13 Indic languages (Bhashini-IITJ) — printed-doc domain adjacent; role = robustness eval slice (scene degradations), never SFT core (domain mismatch with 200-dpi scans).
  - Verify ks/sat/mni/or file presence at freeze; absence = honest-empty, never substitution.

- C3-085 | GPL-3.0 / LGPL-3.0 quarantine (OpenSLR-ks C3-028; DocCreator C3-091; legacy Eeyek-Unicode §R3-A6) | various | VERIFIED | 3/3/2
  - GPL-3.0 (SLR122 transcripts): copyleft distribution risk — EXCLUDED unless counsel clears. LGPL-3.0 (DocCreator binary): use as parameter reference + optional standalone degrader binary; keep OUT of the training import chain pending license review (R3§B3.6 carryover).
  - Legacy Eeyek-Unicode (GPL-2.0+ via SUSE): excluded — modern OFL Eeyek (C3-061) supersedes it with zero copyleft.
  - General rule: copyleft in the loop = product-training poison — quarantine list is closed (3 items) unless freeze review adds more.

- C3-086 | https://bhashini.gov.in/vatika | live 2026-09-26 | VERIFIED | 2/4/3
  - Bhashini Model & Data Vatika: structured cards with metadata + licensing + usage guidelines for NLP/ASR/TTS/OCR sets; ULCA upload/discover path (per indicnlp_catalog).
  - Role: license-transparent discovery surface — re-query at freeze for ks/sat/mni/or OCR drops; card terms govern per item.
  - Bhashini OCR API list (iiith scene-text incl. Manipuri, per GitBook C3-search) is INFERENCE-only for our cells until carded datasets (not APIs) are confirmed.

---

## S6 — Synthetic tooling + degradation (licenses + precedents)

- C3-087 | https://github.com/Belval/TextRecognitionDataGenerator + https://pypi.org/project/trdg | MIT; v1.8.0 (2022-08-02) | VERIFIED | 5/3/5
  - TRDG: MIT synthetic,i word/line generator (3,694★/1,014 forks); GeneratorFromStrings/Dict/Random/Wikipedia; CLI flags map 1:1 to R3§B3 (skew `-k/-rk`, distortion `-d/-do`, blur `-bl/-rbl`, backgrounds `-b`, stroke, orientation, margins).
  - `--word_split` per-character split flag MATTERS for ligature scripts (ur/ks Nastaliq) — character-split renders would break ligature shaping; use word/line mode + Raqm for Perso-Arabic.
  - Deps include arabic-reshaper + python-bidi — relevant to the RTL pipeline (C3-035); verify reshaper output against HarfBuzz shaping at freeze (reshaper bugs = synthetic mojibake).

- C3-088 | https://github.com/clovaai/synthtiger + https://pypi.org/project/synthtiger | MIT (NAVER 2021); v1.2.1 (2022-11-11) | VERIFIED | 4/3/5
  - SynthTIGER: MIT, ICDAR-2021, REQUIRES libraqm (= HarfBuzz shaping path) — the R3§B2 RAQM-mandatory rule's reference implementation; mid-ground/noise-text blending + stretch/trapezoidate/skew/rotate.
  - resources/font + docs subdirs re-licensed per NOTICE (origin licenses) — never bundle those fonts; bring our own OFL set (§S1–S4).
  - Alternative chassis if TRDG's line-orientation limits bind on block renders; decision at freeze, both MIT so the choice is technical, not legal.

- C3-089 | https://arxiv.org/html/2601.16113v1 (SynthOCR-Gen) + https://arxiv.org/abs/2601.01088 (600k-ks) | 2026-01 | VERIFIED | 5/5/4
  - Low-resource-generator precedent pair: tool + 600k-word Kashmiri proof (seed 42, 90/10, 89,743 uniques) — the "Unicode corpus + fonts → 10⁵–10⁶ renders" claim is MEASURED, not projected, for our hardest cell.
  - 25+ augmentations incl. shear ≤0.2 (§3.8) — adopt shear cap into R3§B3 geometry row for Mayek vowel-sign safety.
  - Client-side/open design — no service dependency, no data exfiltration surface for the ledger.

- C3-090 | https://github.com/sparkfish/augraphy + https://arxiv.org/abs/2208.14558 | MIT (Sparkfish); 574★; paper 2022, cited 10× | VERIFIED | 5/4/5
  - Augraphy: MIT document-degradation pipeline (ink→paper→post phases; BleedThrough/InkBleed/DirtyDrum/Faxify/Jpeg/Folding/ShadowCast etc.) built FOR training-data fabrication + robustness testing of OCR/form/denoise models.
  - Comparison table (paper Table 1): only document-centric Python-pipeline MIT option vs DocCreator (LGPL, historical-noise focus, no pipeline) — selects Augraphy as the DEFAULT degrader, DocCreator as parameter reference.
  - Ink/paper phase separation matches R3§B3 fixed order (geometry→ink/paper→optical→compression) — adopt phase mapping 1:1.

- C3-091 | https://github.com/DocCreator/DocCreator | LGPL-3.0; 138★/323 commits | VERIFIED | 3/3/3
  - DocCreator: synthetic GT document images + physical degradation models (ink/paper/background, paper deformation ≤2% height for blocks, old-font maker); cmake `-DBUILD_OTHER_PROGS=ON` builds the standalone Degradator binary.
  - LGPL-3.0 → binary-use + parameter-reference posture only (C3-085); historical-degradation focus complements Augraphy's office-noise focus for the OldScan arm.
  - Citation requirement (J. Imaging 2017, 3, 62) — cite in the final packet if the binary is used.

- C3-092 | https://aclanthology.org/2025.lm4uc-1.11 (+ ICCVw-2025 3M-image extension; data https://nayana.cognitivelab.in/) | 2025 | VERIFIED | 5/4/5
  - Nayana-OCR: GOT-OCR + LoRA on PURELY synthetic 850k/10-Indic-lang set → CER 0.227 ≈ Tesseract 0.206, BLEU 0.395 > 0.318 — synthetic-only parity precedent at 10⁵–10⁶ scale; 3M-image ICCVw extension confirms scaling.
  - Sets the volume bar our R3≥100k-renders/script already meets at the low end; Nayana's 10 langs are high-resource scripts — transfer to Ol Chiki/Mayek is analogy (Maltese C3-093 is the closer structural analogue).
  - Data host nayana.cognitivelab.in — verify terms at freeze IF we reference (not collect) their sets.

- C3-093 | http://arxiv.org/abs/2607.00250 | 2026-07 (INFERENCE: date from id) | VERIFIED | 4/4/5
  - LV-ROVER-MLT Maltese: zero public paragraph corpus → synthetic lines → Tesseract-5 LSTM FT + 5-stream arbitration = usable paragraph OCR where NONE existed.
  - Exact structural analogue of sat (Ol Chiki: zero native labeled lines, §R3-A4) — the rescue playbook is published and citable for the validation call.
  - Tesseract-LSTM vehicle differs from our VLM vehicle — recipe transfers, numbers don't; mark INFERENCE on any CER extrapolation.

- C3-094 | https://arxiv.org/html/2506.02295 (QARI paper + https://github.com/NAMAA-ORG/qari-ocr-paper-2025) | 2025–2026 (via R2 citation) | VERIFIED | 5/4/5
  - QARI curriculum: v0.1 10k plain → v0.2 50k diacritized/10-font (CER 0.550→0.061) → v0.3 10k layout/HTML-spatial REGRESSES plain CER 0.061→0.300; 4-bit quant CER 3.45 vs 8-bit 0.091; SFTTrainer + UnslothVisionDataCollator, batch-8.
  - THREE binding rules derived: (1) plain→font/stage order, NO layout-mix in line-CER stage (R7 C2); (2) no 4-bit recognizer quant (R7 C3); (3) 50k-synth/2B-VLM scale reference for the 49-pt closure claim.
  - Community Qwen2-VL Arabic LoRA notebooks (m0d9) exist — pipeline template for ks/ur SFT, verify notebook license at freeze.

- C3-095 | https://arxiv.org/html/2601.14490v1 | 2026-01 (INFERENCE: date from id) | VERIFIED | 3/5/3
  - GutenOCR-7B: grounded VLM OCR front-end; training stages 2.5M core → 0.5M real-spec → 0.3M PMD-exposure → 0.3M PMD-spec; 2,048-sample val for early stopping; held-out pages uniform-random STRATIFIED by source+length; grounded outputs (boxes) make errors spottable → human-in-loop verification + active learning.
  - Stage-mixing precedent for R7 S1→S2→S3 (core-synth → real-spec → target-spec) + stratified-sampling precedent for §6.4 + box-grounded verification workflow for the human pass (render boxes from the synth sidecar where available).
  - 7B scale ≠ our ≤2B envelope — stages transfer, absolute numbers don't.

- C3-096 | https://arxiv.org/abs/2409.19735 (Bourne 2024, CLOCR-C) | 2024 (via R3 citation) | VERIFIED | 4/3/4
  - LM + char-Markov synthetic corruption FT: −55% CER / −32% WER over base; SYNTH-BEATS-REAL-trained; UNDER-corrupt > OVER-corrupt.
  - Degradation-calibration rule: bias every §B3 distribution toward the gentle end; keep ~15% clean anchors (R3§B3) — over-degradation destroys more than it teaches.
  - Correction-stage result — applies to our post-OCR correction head IF built, not to the recognizer directly; tag scope honestly.

- C3-097 | https://aclanthology.org/2024.findings-acl.361 + https://aclanthology.org/2024.emnlp-main.862 (Guan & Greene) | 2024 (via R3 citation) | VERIFIED | 4/3/4
  - Glyph-similarity synthetic post-OCR correction (ByT5, zero manual annotation): CER reductions incl. 68.67% (SCN-TTA); synth beats uniform-corruption baselines especially low-resource.
  - Glyph-confusable augmentation (nuqta-sets for Nastaliq, matra-hooks for Mayek per R4§C5) enters the §B3 ink-phase as targeted confusion pairs — not uniform noise.
  - Same scope tag as C3-096 (correction stage).

---

## S7 — GT-quality gates: verification sampling + falsification

- C3-098 | https://dl.acm.org/doi/fullHtml/10.1145/3476887.3476888 | 2021 (HIP workshop survey) | VERIFIED | 4/2/4
  - OCR-eval survey: GT producible "only ever for very small numbers" → (random) SAMPLING with representativeness (Bernoulli experiment) is the sanctioned method; randomized samples give statistically reliable statements that manual page-picking cannot.
  - Direct license for §6.4 (10% stratified, seed 20260926): our protocol IS the literature method; cite at the validation call against any "verify everything" demand.
  - PAGE XML (structure/layout/reading-order GT) + OCR-D GT guidelines referenced — adopt PAGE-sidecar fields for block renders (reading order = render order, R3§B1.4).

- C3-099 | https://arxiv.org/abs/1307.0426 | 2013 (Lampert et al.) | VERIFIED | 4/2/4
  - Annotator-agreement study: single-annotator GT makes detector RANK order depend on the GT-formation method; consensus-voting ACCENTUATES obvious features → overestimates performance; STAPLE/LSML degrade under few/high-variance annotations.
  - Three consequences for §6.4: (1) blind dual-verify (verifier never sees the PDF-layer string — posthoc-fallibility guard per C3-100); (2) >20% fail-bar is per-language, never pooled (variance differs by script); (3) never "fix" GT by majority vote of engines — human gold only.
  - Confidence-bounds method (paper §5) → adopt for the §6.7 CI reporting on small cells.

- C3-100 | https://aclanthology.org/2022.dadc-1.3.pdf | 2022 (Ding, cited 10×) | VERIFIED | 3/3/4
  - Posthoc verification fallibility: strict re-annotation counts "close enough" as wrong and can DRAMATICALLY change verdicts; GT annotations should be scored like any other model output.
  - Calibrates the §6.4 fail criterion: fail = semantic/character-error vs the IMAGE (matra/conjunct/nuqta/word errors), never whitespace/punctuation-normalization trivia (that class is scorer-side, §6.6).
  - Supports the falsification-test direction (§6.2): suspect GT loses to gold-GT on the same engine, not to an arbitrary strictness bar.

- C3-101 | https://arxiv.org/html/2510.21774v1 | 2025-10-17 | VERIFIED | 3/5/3
  - OCR-Quality (2025): comprehensive HUMAN-ANNOTATED dataset for OCR quality assessment — quality-estimation (predict CER without GT) is a live 2025 track.
  - Application: quality-estimation scores can TRIAGE the §6.4 sample (oversample low-confidence lines) — stratified + uncertainty-weighted sampling beats uniform 10% for finding corrupt GT (ne-class failures).
  - INFERENCE: our-engine confidence as the triage signal needs calibration first — pilot on the ne (barred) tier before trusting it elsewhere.

- C3-102 | https://www.cvat.ai/resources/blog/annotation-quality-assurance | 2026-03-30 | VERIFIED | 2/5/3
  - Industry QA playbook (CVAT 2026): GT-based auto-validation + manual review + sampling strategy + agreement tracking + audit records — the 5-way QA our §6.4 + gt_verification.json + ledger already mirror.
  - Ground-truth-based validation (gold checks injected into annotator queues) → adopt: seed 5 known-gold lines per verifier batch; verifier missing them = batch re-done.
  - Record-keeping requirement matches our sidecar/manifest discipline — no new process, cite as external corroboration.

- C3-103 | Disk: `level2/probe22/gt_verification.json` + protocol §6.4 (task owned by VERDICT agent) | 2026-09-26 | VERIFIED | 5/5/5
  - Verification workload as scoped: all 158 sarvam_fill (blind, agreement) + ~77 stratified PDF lines (10%, seed 20260926); per-language >20% fail → tier barred from W6; ne already barred (R5 26.6), ks/mr/gu/ur verify-first.
  - Falsification arithmetic (§6.2): pair-vs-pdf CER gap >10pp on the same engine = PDF GT suspect for that language — the test that decides whether ANY real line beyond human pairs may train.
  - Cost honesty: ~2h single-agent task — the GT budget is hours, never a collection project (reinforces the no-400-page law).

- C3-104 | https://ilocr.iiit.ac.in/dataset/7 (Mozhi-Hindi card) | live 2026-09-26 | VERIFIED | 3/3/4
  - Mozhi per-language card pattern: 100,049 Hindi words from 1,000 flatbed-scanned 600-DPI book pages, manual GT, train/val/test splits + vocabulary.txt, license CC-BY-4.0 (data_license.doc).
  - Quality-bar template for any future human-gold mining (the 300–500 real ks lines, R2§C3): 600-DPI scans, word-box annotation, vocab list, CC-BY licensing from the start.
  - or/sat/mni Mozhi slices (darknight054 mirror C3-105) inherit THIS methodology — eval-trustworthy to the extent the mirror preserves the GT files (verify checksums at freeze).

- C3-105 | https://huggingface.co/datasets/darknight054/indic-mozhi-ocr | live 2026-09-26 | VERIFIED | 4/3/3
  - HF mirror: 1,211,362 rows / 4.59 GB, 13 langs INCL Manipuri, Oriya (OrIya), Urdu (382 downloads last month); source page cvit.iiit.ac.in/usodi/tdocrmil.php; paper Mathew et al. ICPR-2025 ("Towards Deployable OCR Models"); MeitY/NLTMBhashini-supported.
  - License: "refer to source page" — UNRESOLVED this pass → approval request BLOCKED until CVIT terms confirmed (academic-use likely; verify before eval use of the or/mni/ur slices).
  - Role if cleared: or (Oriya) + ur printed-word eval slices; mni slice script-tag check mandatory (Bengali-script era risk per R3 — gate before use).

---

## S8 — OldScan cell (55.3): restoration references (methods, not training data)

- C3-106 | https://vc.ee.duth.gr/h-dibco2018/benchmark (via H-DIBCO 2018 paper, DOI 10.1109/icfhr-2018.2018.00091) | 2018 | VERIFIED | 3/2/3
  - H-DIBCO 2018: 10 handwritten images + MANUAL binary GT + eval software publicly released post-competition; degradations covered (variable background, shadows, smear, low contrast, bleed/show-through); series runs DIBCO 2009→2019 + H-DIBCO 2010→2018.
  - Method-reference + GT-cost precedent (manual binary GT ≈ 10 images/competition-year ⇒ our 40-page OldScan eval slice is proportionally scoped); Latin/Greek scripts ONLY — zero Indic transfer (R4 binding).
  - Metrics (F-measure/pseudo-FM/PSNR/DRD) are binarization-internal — adopt ONLY for the A1/A2 ablation arms, never as OCR CER substitutes.

- C3-107 | https://link.springer.com/article/10.1186/s13640-021-00556-4 | 2021-05-10 | VERIFIED | 3/3/3
  - H-DIBCO-2018 winning framework (background estimation + energy minimization + CCA denoising); 9-competition-dataset evaluation 2009–2018 — the classical ceiling for the A1/A2 arms.
  - Supports the R7 order (cheap classical first, learned heads only on pilot pass): background-estimation + Otsu/Sauvola bracket the classical space before any DocRes pilot.
  - No artifact for our data — method citation for the restoration ablation sheet.

- C3-108 | Disk R7 N5d binding (Otsu-vs-Sauvola ~2–7 FM; learned ~8–18 FM per https://arxiv.org/pdf/1709.01782v1; DocRes https://github.com/ZZZHANG-jx/DocRes + https://arxiv.org/abs/2405.04408v1; SauvolaNet reserve https://arxiv.org/abs/2105.05521; Nastaliq dot-thinning risk https://www.ijrte.org/wp-content/uploads/papers/v8i5/E6949018520.pdf) | 2026-09-26 | VERIFIED | 4/4/4
  - Numbers that gate the OldScan arm: Otsu trails Sauvola only ~2–7 FM (cheap baseline justified); learned heads +8–18 FM BUT the C5 dot-audit (≥2 smoothed dots/matra-hooks per page ⇒ reject A3) protects Nastaliq/Mayek thin strokes.
  - CPU ≤3 min/page + 40-page expansion rule + diffusion/GAN deferral (CPU-infeasible + glyph risk) — the restoration lane has compute guardrails, not open-ended collection.
  - No new data needed: ablation runs on the EXISTING probe + 40-page manual slice (C3-008).

---

## S9 — Engine/baseline cross-checks (data-adjacent, constrains collection)

- C3-109 | https://huggingface.co/PaddlePaddle/arabic_PP-OCRv5_mobile_rec/blob/main/README.md + https://huggingface.co/medyas/arabic_PP-OCRv6_small_rec/blob/main/README.md | live 2026-09-26 | VERIFIED | 4/4/4
  - Paddle arabic rec: 81.27% whole-line accuracy (strict; Naskh-skewed, Urdu codepoints present, Nastaliq unmodeled); third-party KITAB-context off-shelf CER 0.77/0.81 vs Tesseract 0.14/0.31; fine-tuned PP-OCRv6-small on 500k printed Arabic → ~10% CER.
  - Data consequence: NO off-shelf Paddle-Arabic collection for ks (expected 0.5–0.8 CER band = incumbent); only the VLM branch (PaddleOCR-VL-0.9B + SFT) belongs in the plan — saves a dead-end data request.
  - 500k-printed→10% number sets the Naskh-side (sd fallback) volume reference IF the sd-Naskh arm is ever opened.

- C3-110 | https://ocr.ai4bharat.org/ + https://github.com/AI4Bharat/Indic-OCR | live 2026-09-26 | VERIFIED | 2/4/3
  - AI4Bharat Indic-OCR portal ("building OCR tools for all languages of India — in progress") + Indic-OCR repo (2★, 7 commits, docs skeleton) — the Bodhan/Indic-OCR open-weight line (bodhan-ai/indic-ocr, Indic Open Model License per memory feed) is the probe's P2 baseline, NOT a data source.
  - Bodhan leads sat (68.30) per W3 schema — the sat router question (R7 N5b) may dominate over synth volume; no sat data volume compensates for a missing router decision.
  - No download, no weight pull without GPU-budget approval (§6.8 P2) — noted so C3 is not read as authorizing it.

- C3-111 | https://dibd-bhashini.gitbook.io/bhashini-apis/available-models-for-usage | live 2026-09-26 | VERIFIED | 2/3/3
  - Bhashini API catalog lists OCR/ASR/LID coverage incl. Manipuri, Santali, Kashmiri, Sindhi, Odia across providers (IIIT-H scene-text OCR, AI4Bharat conformer multilingual incl. 24-lang ASR).
  - APIs are NOT data sources and NOT inference paths (no-API-at-inference law, R2 Path-6 NO-GO) — listed only to prevent " unseen Bhashini OCR" gaps at the validation call; any API-derived machine GT would inherit the sarvam_fill NEVER-trains ban.
  - INFERENCE: API existence ≠ usable GT — machine GT from ANY vendor scores agreement-only at best.

- C3-112 | https://pillow.readthedocs.io/en/stable/reference/ImageFont.html + https://harfbuzz.github.io/harfbuzz-hb-shape.html | live (via R3 citation) | VERIFIED | 4/4/5
  - Pillow: "Raqm layout recommended for ALL non-English text" (libraqm = FriBiDi + HarfBuzz); HarfBuzz hb_shape applies script-specific shaping models with BCP-47 language tags.
  - Pipeline law derived: RAQM-assert-or-abort for Mayek (ABE3–ABEA/ABED), RAQM-preferred for Ol Chiki (BASIC glyph-correct), word/line-mode + Raqm for Nastaliq (never per-char split); `language="mni"` tag set.
  - Shaping-fidelity batch gate (zero-ink cluster ⇒ fail batch) generalizes to ALL scripts incl. Oriya/Urdu renders — tofu is silent GT corruption.

---

## S10 — WHAT-NOT-TO-COLLECT (law records; violations end the campaign)

- C3-113 | Disk law (memory feed §9 + protocol §0 + R7 N0) | 2026-09-26 | VERIFIED | 5/5/5
  - NO 400-page sets for remaining languages (any language, any script, any justification — the 300–500 REAL ks-line budget and ≥100k synthetic renders are the ceilings, not floors for negotiation).
  - NO downloads (datasets, weights, traineddata, fonts, dumps) without explicit user yes; NO training before freeze; sealed dirs untouched; fill declared as fill.
  - Any record in this ledger marked QUARANTINE/EXCLUDED needs a re-verdict + user approval before it can move to SFT-safe or probe/eval — the ledger is deny-by-default.

- C3-114 | Disk law (protocol §1 + R3§B0 + R7 N0) | 2026-09-26 | VERIFIED | 5/5/5
  - sarvam_fill (158) NEVER trains (agreement-only scoring); Bodo/gu copy + test/test NEVER GT; synthetic NEVER eval (S6 gold-by-construction); machine GT from ANY vendor (incl. Bhashini APIs, C3-111) inherits the same ban.
  - RLVR rewards on human-verified gold ONLY + waits for §6.6 no-inversion; akshara-aux never on ur/ks/sd/sat/mni; Otsu stays the cheap baseline until the OldScan ablation passes.
  - W6 eligibility is PER-LANGUAGE (verification pass + falsification gap ≤10pp + R5 trust ≥70): failing languages revert share to L1 pairs, never to fill (R7 S-mixing fallback).

- C3-115 | Ledger quarantine roll-up (this file) | 2026-09-26 | VERIFIED | 4/5/4
  - EXCLUDED unless affirmatively cleared: Rekhta bulk (C3-022), santals.in bulk (C3-050), Hueiyen Lanpao bulk (C3-062), Jameel-Noori redistribution (C3-033), community blogspot fonts (C3-052), GPL-2.0+ legacy Eeyek (C3-061 note), OpenSLR-ks GPL transcripts (C3-028), Kaggle-provenance sets (C3-025/058), SEACrowd NC mirror (C3-039), DocCreator import-chain use (C3-091), 4-bit recognizer quant (C3-094), API-at-inference (R2 Path-6).
  - "Allowed but down-weighted" (not excluded): Grierson 1932 (C3-029), dictionary-register strings ≤10% (C3-013), translationese ≤20% (C3-073), OCR-extracted text with gate (C3-073), transliterated strings post-95%-sample-gate (C3-051/063).
  - Count: 115 records total (C3-001…C3-115). Verification sample for the Verdict agent: 10% ≈ 12 records (suggest C3-009/010/030/047/053/061/067/069/076/087/090/098).

## S11 — §9 UPGRADE (2026-09-27; campaign §9 evidence law + AGENT_PROTOCOL §1 purge lessons + §6.4 ne-BARRED lock)

Law: no downloads executed, no training, no rows above rewritten, STRATEGY.md untouched (gold).
Status set is exactly PRIMARY / MEASURED / DERIVED / CONTRADICTION / UNKNOWN / REJECTED / DEAD.
Transfer verdict per record is SURVIVES / DIES / UNKNOWN against OUR harness facts only:
18 Indic langs; weak cells sat 53.91 / ks 54.82 / OldScan 55.3 / or 80.01; 200-dpi citizen docs;
no paid keys; no training until W6 freeze; offline-capable pipeline; no 400-page sets.

### S11.1 — Transfer-status upgrade lines (one per existing record; old VERIFIED/INFERENCE → §9 status)

- C3-001 | PRIMARY (disk law, re-read 2026-09-27) | decision: W6 GT-eligibility gates per language | SURVIVES — gates are harness-native (§1); kills any gate-relaxation proposal.
- C3-002 | MEASURED (computed from disk forensics) | decision: ne-BARRED lock + ks/mr/gu/ur verify-first | SURVIVES — R5 trust scores are our own numbers; ne 26.6 bar stands per §6.4 lock.
- C3-003 | DERIVED (protocol §9 + R7 synthesis, formula: allow-list shown) | decision: W6 SFT allow-list + mixing ratios | SURVIVES — no external dependency.
- C3-004 | PRIMARY (disk law) | decision: collection scope / no-download / sealed dirs | SURVIVES — standing law, kills all bulk-scrape proposals.
- C3-005 | MEASURED (manifest n=1227 counted from disk) | decision: small-cell no-winner claims + zero-trusted-line cells (as/mni/sat) go synthetic-only | SURVIVES.
- C3-006 | DERIVED (QARI 49-pt closure + UTRSet 15-pt residual arithmetic shown) | decision: ks real-line budget = 300–500 hand-corrected lines, never a 400-page set | SURVIVES — mixing rule is harness-scoped.
- C3-007 | DERIVED (Nayana parity + Maltese rescue + Bourne correction precedents) | decision: synth-val is a gate never a claim; synth NEVER eval | SURVIVES.
- C3-008 | DERIVED (R7 N5d bindings) | decision: no restoration training set; 40-page manual OldScan eval slice only | SURVIVES.
- C3-009 | PRIMARY (arXiv span opened) | decision: ks word-stage SFT fuel (600k synth, CC-BY-4.0) | SURVIVES — license + Kashmiri-Yeh-aware fonts fit harness; word-level only, line curriculum still needs R2 renders.
- C3-010 | PRIMARY (content span opened; year from arXiv id is cosmetic) | decision: ks render-string base (KS-LIT-3M) | SURVIVES-IF §B1-equivalent script gate passes (Perso-Arabic vs Devanagari mix unverified at sample level).
- C3-011 | PRIMARY | decision: 3rd synth chassis at freeze (TRDG/SynthTIGER/SynthOCR-Gen) | SURVIVES — open tool, no service dependency; per C3-117 the chassis now has a second 2026 proof (Persian Pixel).
- C3-012 | UNKNOWN (repo↔HF-host parity unverified — the decision-relevant fact) | decision: which ks host to cite in the approval request | UNKNOWN — canonical HF host preferred until checksums compared; successful output, not a hole.
- C3-013 | PRIMARY | decision: ks rare-word booster ≤10% of render strings | SURVIVES — Apache-2.0, dictionary-register cap stands.
- C3-014 | PRIMARY | decision: synth+real mixing rule for ur (15-pt residual) | SURVIVES as method; UTRNet accuracy numbers get obituary C3-122 (CTC-era, Naskh-heavy — DEAD for ks VLM routing).
- C3-015 | PRIMARY | decision: ur real-line eval/SFT-inside-hackathon via gated agreement | SURVIVES-IF agreement on file; NC bars product reuse (sidecar tag).
- C3-016 | PRIMARY | decision: R2 font×degradation matrix recipe reference | SURVIVES — recipe transfers, no data moves without paper trail.
- C3-017 | PRIMARY (spans re-confirmed via arXiv v2 C3-121) | decision: best REAL Nastaliq eval anchor for ks/ur transfer | SURVIVES as eval; vendor WERs get obituary (different harness — DEAD for routing).
- C3-018 | PRIMARY | decision: ur word-stage SFT fuel | SURVIVES — ks use capped as style-distractor (Yeh under-render per R2§A4).
- C3-019 | PRIMARY | decision: ur graded render strings + probe/eval IMAGE candidates | SURVIVES-IF Nastaliq/Naskh split confirmed at freeze; fees + paper trail before approval.
- C3-020 | PRIMARY (index confirmed) | decision: ur render-string mining checklist | SURVIVES as index; commercial corpora on it DIES for free use.
- C3-021 | PRIMARY | decision: ur/ks/sd wiki render-string bases | SURVIVES-IF per-line script gate; share-alike question stays UNKNOWN (C3-081) — majority share stays on CC-0/CC-BY/MIT bases.
- C3-022 | PRIMARY (© + 5-free-pages confirmed) | decision: DO NOT collect Rekhta bulk | DIES — commercial foundation; sample-strings-only with permission, otherwise cut.
- C3-023 | PRIMARY | decision: MIT text-side render strings only | SURVIVES (text reuse); NLP-label reuse DIES (labels don't transfer to OCR GT).
- C3-024 | PRIMARY | decision: classical ur baseline (BCER 27.1%) for falsification comparison | SURVIVES — validates autoregressive-SFT direction, not more CTC tuning.
- C3-025 | PRIMARY (pointer list confirmed) | decision: none until uploader→paper license tracing done | DIES for now — Kaggle provenance risk + handwriting/char-level domain mismatch.
- C3-026 | UNKNOWN (host + license terms unverified — decision-relevant) | decision: whether sd sampling base exists here | UNKNOWN — no approval request until terms verified; script-split gate mandatory if cleared.
- C3-027 | PRIMARY | decision: sd Naskh-distractor fonts + CRULP wordlists | SURVIVES-IF redistribution terms confirmed; render-locally posture until then.
- C3-028 | PRIMARY (GPL-3.0 confirmed on card) | decision: DO NOT USE ks transcripts | DIES — copyleft + spoken-register noise; clears only on counsel sign-off.
- C3-029 | UNKNOWN (per-jurisdiction PD status unreviewed — decision-relevant for approval) | decision: whether Grierson text may seed renders | DIES for volume regardless (archaic lexis + scan noise); allowed-but-down-weighted IF PD clears.
- C3-030 | PRIMARY | decision: mandatory ks render-matrix font (Awami SIL ≥3.300) | SURVIVES — OFL-1.1, Kashmiri support proven; GF-streamlined copy DIES (coverage risk).
- C3-031 | PRIMARY | decision: U+0620 coverage gate for every ks batch | SURVIVES — harness-native shaping gate.
- C3-032 | PRIMARY | decision: font-version pinning rule (Noto Nastaliq v3.004→v4.000 shaping drift) | SURVIVES — sidecar records font+version for every batch.
- C3-033 | UNKNOWN (no OFL statement found; "free download ≈ render OK" NOT established) | decision: whether Jameel Noori cuts may render | DIES until organizer check at freeze — render-locally-only posture, never redistribute; OFL cuts preferred.
- C3-034 | UNKNOWN (per-file licenses unverified) | decision: which pack fonts enter the matrix | UNKNOWN per file — Google-Fonts OFL items SURVIVE individually; rest DIES until verified.
- C3-035 | PRIMARY | decision: adopt Urdu normalization pipeline into scorer before any ks/ur/sd SFT decision | SURVIVES — 3–8 pts of CER may be scoring artifact; gate, not post-processing.
- C3-036 | PRIMARY | decision: Path-#3 hedge (word-model + line wrapper for ur/sd floor) + 160k word-image budget reference | SURVIVES — ks capped by Yeh OOV (documented limit, not a volume gap).
- C3-037 | PRIMARY | decision: sat render-string bootstrap (≈60k words) + mni slice after script-tag gate | SURVIVES — SFT-safe, never eval (hidden test + synth-never-eval).
- C3-038 | PRIMARY | decision: volume math (3k sents = booster, not sole base; pair with sat.wiki) | SURVIVES; share-alike handling per C3-081 (UNKNOWN scope — low stakes by majority-share rule).
- C3-039 | PRIMARY (NC re-host confirmed) | decision: DO NOT SOURCE from SEACrowd mirror | DIES — wrong mirror; canonical CC-BY-SA source only. Ledger lesson (mirrors change licenses) SURVIVES.
- C3-040 | PRIMARY | decision: largest Ol-Chiki running-text pool (sat.wiki dumps + NFC + ≥80% gate + N≥500/char histogram) | SURVIVES — gate is load-bearing against Bengali-script Santali poisoning.
- C3-041 | UNKNOWN (volume unquantified; license per-file unconfirmed — both decision-relevant) | decision: sampler share for santali-nlp corpus | UNKNOWN — count + license at freeze before budgeting; no bulk use until then.
- C3-042 | PRIMARY (index confirmed; per-record terms vary) | decision: rare-char booster material only | SURVIVES-IF per-record terms + per-line gate; never running-prose base.
- C3-043 | PRIMARY | decision: THE precedent recipe (synth-train + real-finetune) for sat/mni/ks cells | SURVIVES — but their ks pages are Devanagari-script: DIES for our Nastaliq cell (verify script per file).
- C3-044 | PRIMARY | decision: citation weight for validation call (Springer peer review) | SURVIVES as citation; no new data (never double-counted).
- C3-045 | PRIMARY | decision: sat render-matrix recipe + Ol-Chiki render feasibility since 2022 | SURVIVES — Manipuri row DIES for mni (stale Devanagari, pre-Mayek-switch).
- C3-046 | PRIMARY | decision: eval-candidate pointer only (organizer-gated, handwriting domain) | UNKNOWN until terms + per-file script split confirmed; handwriting≠printed tag stands.
- C3-047 | PRIMARY | decision: ONLY verified OFL Ol-Chiki design → degradation-heavy diversity + held-weight-700/held-seed synth-val | SURVIVES — single-design constraint drives R3 mitigations.
- C3-048 | PRIMARY (re-anchored to Unicode 17.0 per C3-123; 48/48 assigned unchanged) | decision: Pillow-BASIC-correct / RAQM-preferred pipeline + ≥80% gate regex | SURVIVES.
- C3-049 | PRIMARY (context only, zero artifact) | decision: none — institutional momentum, not budgeted | DEAD for sourcing (recorded so the call doesn't re-litigate "more Mayek print coming" as data).
- C3-050 | PRIMARY (© confirmed) | decision: DO NOT bulk-scrape santals.in | DIES — permission via user only; excluded from all volume math until then.
- C3-051 | UNKNOWN (≥95%/500-line native accuracy gate unrun — decision-relevant) | decision: whether Bengali-script Santali may convert to Ol-Chiki strings | UNKNOWN — failed sample = route stays Bengali-renderer, never Ol-Chiki.
- C3-052 | PRIMARY (mixed/unclear licenses confirmed) | decision: DO NOT USE community fonts for training renders | DIES until per-font license verified; link-lists-are-not-licenses rule SURVIVES.
- C3-053 | PRIMARY | decision: largest Mayek-script string pool (461k MIT, gated accept) | SURVIVES — translationese caveat + §B1 gate + histogram apply like any source.
- C3-054 | PRIMARY | decision: future handwriting-slice eval pointer only | DIES for printed-line SFT (handwriting + char-level + thesis-hosted access).
- C3-055 | PRIMARY | decision: eval-pointer only | UNKNOWN until license + 37-vs-55-class coverage confirmed; printed-SFT excluded regardless (domain).
- C3-056 | PRIMARY | decision: closest real printed-Mayek eval anchor + skew-correction method reference | SURVIVES-IF host + terms located at freeze; char-level → eval-slice, never line-SFT.
- C3-057 | PRIMARY (precedent only, closed set) | decision: none — listed so the call can't claim "no prior Mayek OCR" | DEAD for data (segmentation-cascade era, no artifact).
- C3-058 | PRIMARY (triple quarantine confirmed) | decision: none until uploader→paper tracing | DIES — Kaggle terms + provenance + handwriting domain.
- C3-059 | PRIMARY | decision: pointer to Deena et al. 55-class HW custodians | UNKNOWN (access + terms at freeze); printed-SFT excluded (domain); repo-code reuse UNKNOWN (license unverified).
- C3-060 | PRIMARY | decision: TRAIN-side mni design (9 weights = first-class sampler dimension) | SURVIVES — OFL-1.1, approval-clean install.
- C3-061 | PRIMARY | decision: Eeyek held EXCLUSIVELY for synth-val (font-disjoint test) | SURVIVES — legacy GPL Eeyek DIES (OFL supersedes, zero copyleft).
- C3-062 | PRIMARY (© newspaper confirmed) | decision: DO NOT bulk-scrape Hueiyen Lanpao | DIES for text; SURVIVES as block-render style reference (layout observation ≠ copying).
- C3-063 | UNKNOWN (EM corpus contents/script/access all unverified; mni-wiki count never quoted) | decision: whether Assam-program/Bengali-script mni enters LANGUAGE sampling | UNKNOWN — transliteration gate (C3-051 rule) applies if opened.
- C3-064 | PRIMARY | decision: Mayek gate rules (≥80% U+ABC0–ABFF; historic ≤2%; NFC; HarfBuzz mandatory; raqm-abort) | SURVIVES — harness-native shaping law.
- C3-065 | PRIMARY | decision: sampler seed word/number lists + digit booster | SURVIVES — seed-scale only, never volume.
- C3-066 | PRIMARY | decision: expect Bengali-script contamination in any mni crawl (gate load-bearing) | SURVIVES — re-check switchover completion at freeze (affects real-Mayek page availability, not synth plan).
- C3-067 | PRIMARY | decision: or char-stage warm-up ONLY from MIT slice; Mozhi slice eval-side; lipi slice NC | SURVIVES — split-license verdict stands; or cell needs LINE/BLOCK data, not more chars.
- C3-068 | PRIMARY | decision: dedupe to ONE canonical or-merge source at freeze | SURVIVES — mirror→model provenance chain is ledger-clean.
- C3-069 | PRIMARY | decision: best REAL Odia eval anchor (human-validated pages, <1K scale) | SURVIVES as eval; NC bars product retraining; re-check size at freeze.
- C3-070 | PRIMARY (schema re-confirmed via viewer C3-135: 223 rows, id/image/ground_truth/category) | decision: second real-or eval anchor; pool with probe+lipi for n≈350+ CI-grade claims | SURVIVES as eval, hackathon-only (NC).
- C3-071 | PRIMARY (training config re-confirmed via odiagenai.org C3-131: 58,720 pairs, LoRA, H100) | decision: or budget precedent — our S3 (≤30 GPU-h at ≤2B) is conservative vs ~4 GPU-h at 3B | SURVIVES as budget precedent; its CERs get obituary (word-level, H100 — DEAD for our harness claims).
- C3-072 | PRIMARY | decision: DEFAULT or render-string base (CC-BY-4.0, 801 MB) | SURVIVES — attribution only; pairs with OFL Oriya fonts at freeze.
- C3-073 | PRIMARY | decision: or sampler share ≤20% with extractor-mojibake gate | SURVIVES — translationese + OCR-noise double caveat stands.
- C3-074 | PRIMARY | decision: or overflow render volume inside hackathon only | SURVIVES-IF NC-lineage tagged in sidecar; C3-072 stays default (cleaner license).
- C3-075 | UNKNOWN (or-in-v2 coverage unconfirmed — decision-relevant) | decision: whether IndicCorpV2-CC-0 promotes to DEFAULT or base | UNKNOWN — if covered, promotes; else C3-072/C3-074 stand. Never assumed.
- C3-076 | PRIMARY | decision: layout-harness data (reading-order/block segmentation), NOT OCR GT | SURVIVES — role-separated; verify or-image count at freeze.
- C3-077 | PRIMARY | decision: living or-index — re-query at freeze for drops newer than ledger | SURVIVES as process, not data.
- C3-078 | UNKNOWN (per-item licenses vary — decision-relevant per item) | decision: per-item render-string candidacy | UNKNOWN per item — verify per item, never inherit catalog openness.
- C3-079 | PRIMARY (OFL text) | decision: rendered images + trained weights are not font redistribution (standard reading; counsel-confirm at freeze) | SURVIVES — OFL.txt travels with any shared render set.
- C3-080 | PRIMARY | decision: SIL originals over GF-streamlined copies for ks/mni renders; TEST with real language text | SURVIVES — already actioned (C3-030/061).
- C3-081 | PRIMARY (licenses confirmed) + UNKNOWN (BY-SA→renders/weights scope — no ruling found) | decision: keep BY-SA share a minority; attribute + sidecar lineage; ask organizers | SURVIVES as posture; never touch hidden test; never eval on dev/devtest renders.
- C3-082 | PRIMARY (NC terms confirmed) + UNKNOWN (hackathon=non-commercial assumed — C2 cross-check before freeze) | decision: NC-lineage tags; FINAL PLAN re-derives product allow-list excluding NC | SURVIVES as firewall.
- C3-083 | PRIMARY | decision: prefer MIT/Apache/CC-0/CC-BY for any line that might survive to product | SURVIVES — license-hygiene is a selection criterion.
- C3-084 | PRIMARY | decision: scene-text robustness eval slice where script coverage matches | SURVIVES-IF per-language file list verified at freeze; absence = honest-empty, never substitution.
- C3-085 | PRIMARY (copyleft terms confirmed) | decision: 3-item quarantine stays closed (SLR122-GPL, DocCreator-import, legacy-Eeyek) | SURVIVES — copyleft in loop = product-training poison.
- C3-086 | PRIMARY | decision: license-transparent discovery surface — re-query at freeze | SURVIVES as process; API list is INFERENCE-only until carded datasets confirmed.
- C3-087 | PRIMARY | decision: TRDG as candidate chassis; word/line-mode + Raqm for Perso-Arabic (never per-char split) | SURVIVES — reshaper-vs-HarfBuzz check at freeze.
- C3-088 | PRIMARY | decision: alternative chassis if TRDG line-limits bind; choice is technical not legal (both MIT) | SURVIVES — never bundle resources/font (origin licenses).
- C3-089 | PRIMARY | decision: "Unicode corpus + fonts → 10⁵–10⁶ renders" is MEASURED for ks, not projected | SURVIVES — shear cap ≤0.2 adopted into §B3 for Mayek vowel-sign safety.
- C3-090 | PRIMARY | decision: Augraphy DEFAULT degrader; phase mapping adopted 1:1 | SURVIVES — MIT, document-centric, no exfiltration surface.
- C3-091 | PRIMARY | decision: standalone-binary + parameter-reference ONLY | DIES for import-chain use (LGPL-3.0 pending review); cite J. Imaging 2017 if binary used.
- C3-092 | PRIMARY | decision: volume bar (R3 ≥100k/script meets Nayana's low end) | SURVIVES as scale reference; transfer to Ol Chiki/Mayek is analogy (Maltese is the closer analogue); verify terms IF referenced, never collected.
- C3-093 | PRIMARY (content confirmed; date-from-id cosmetic) | decision: rescue playbook citable for sat at validation call | SURVIVES as recipe; any CER extrapolation = INFERENCE→UNKNOWN (Tesseract-LSTM vehicle ≠ our VLM).
- C3-094 | PRIMARY | decision: THREE binding rules (plain→font order, no layout-mix in line-CER stage, no 4-bit recognizer quant) + 50k-synth/2B scale reference | SURVIVES — notebook reuse UNKNOWN (license at freeze).
- C3-095 | PRIMARY (content confirmed; date-from-id cosmetic) | decision: stage-mixing precedent for R7 S1→S2→S3 + stratified sampling + box-grounded verification | SURVIVES as stages; 7B absolute numbers DIES (outside ≤2B envelope).
- C3-096 | PRIMARY | decision: degradation-calibration rule (gentle bias + ~15% clean anchors) | SURVIVES — scope-tagged to correction head IF built, never the recognizer.
- C3-097 | PRIMARY | decision: glyph-confusable augmentation enters §B3 ink-phase (nuqta-sets, matra-hooks) | SURVIVES — same correction-stage scope tag.
- C3-098 | PRIMARY | decision: §6.4 IS the literature method (Bernoulli sampling) — cite against "verify everything" demands | SURVIVES.
- C3-099 | PRIMARY | decision: blind dual-verify + per-language >20% bar + never-fix-GT-by-engine-vote + §5 confidence bounds for §6.7 CIs | SURVIVES.
- C3-100 | PRIMARY | decision: fail = semantic/character-error vs IMAGE, never whitespace/punctuation trivia | SURVIVES — calibrates §6.4 fail criterion + falsification direction.
- C3-101 | PRIMARY (dataset exists, 2025 track live) + UNKNOWN (our-engine confidence as triage signal needs calibration — pilot on ne-barred tier first) | decision: whether §6.4 sampling goes uncertainty-weighted | UNKNOWN until pilot; stratified 10% seed 20260926 stays default.
- C3-102 | PRIMARY | decision: adopt gold-check injection (5 known-gold lines per verifier batch; miss = re-do) | SURVIVES — no new process, external corroboration.
- C3-103 | PRIMARY (disk verification workload) | decision: GT budget is hours not a collection project; per-language bar + falsification gap ≤10pp gate W6 | SURVIVES — reinforces no-400-page law.
- C3-104 | PRIMARY | decision: quality-bar template for 300–500 real ks lines (600-DPI, word-boxes, vocab list, CC-BY from start) | SURVIVES.
- C3-105 | UNKNOWN (mirror license "refer to source page" UNRESOLVED — approval BLOCKED) | decision: whether or/ur printed-word eval slices exist here | UNKNOWN — verify CVIT terms first; mni slice script-tag mandatory (Bengali-era risk).
- C3-106 | PRIMARY | decision: method-reference + GT-cost precedent (manual binary GT ≈ 10 imgs/competition-year ⇒ 40-page OldScan slice proportional) | SURVIVES; Latin/Greek-only DIES for Indic transfer.
- C3-107 | PRIMARY | decision: classical ceiling for A1/A2 arms; cheap-classical-first order | SURVIVES — citation for ablation sheet, no artifact.
- C3-108 | PRIMARY (disk bindings) | decision: Otsu baseline justified (~2–7 FM gap); C5 dot-audit protects Nastaliq/Mayek; CPU ≤3 min/page; diffusion/GAN deferred | SURVIVES — compute guardrails stand (reinforced by C3-137).
- C3-109 | PRIMARY | decision: NO off-shelf Paddle-Arabic collection for ks (0.5–0.8 CER band = incumbent); VLM-branch only | DIES as data path — saves a dead-end request; 500k→10% sets Naskh-side reference IF sd-Naskh arm opens.
- C3-110 | PRIMARY | decision: Bodhan is P2 baseline not a data source; sat router question (R7 N5b) may dominate synth volume | SURVIVES — no weight pull without GPU-budget approval.
- C3-111 | PRIMARY | decision: APIs are NOT data/inference paths (no-API-at-inference law); any vendor machine GT inherits fill-ban | DIES as source — listed only to close "unseen Bhashini OCR" gaps.
- C3-112 | PRIMARY | decision: RAQM-assert-or-abort (Mayek) / RAQM-preferred (Ol Chiki) / word-line+Raqm (Nastaliq) + `language="mni"` + zero-ink-cluster batch fail | SURVIVES — generalizes to Oriya/Urdu renders.
- C3-113 | PRIMARY (standing law) | decision: deny-by-default — no 400-page sets, no downloads, no pre-freeze training, quarantine needs re-verdict + user yes | SURVIVES — violations end the campaign.
- C3-114 | PRIMARY (standing law) | decision: fill never trains; synth never evals; RLVR on human gold only post-§6.6; akshara-aux never on ur/ks/sd/sat/mni; per-language W6 eligibility with L1 fallback | SURVIVES.
- C3-115 | PRIMARY (roll-up confirmed) | decision: quarantine list stays closed (12 items) + allowed-but-down-weighted caps (Grierson, ≤10% dict, ≤20% translationese, gated transliteration) | SURVIVES — Verdict sample suggestion (12 records ≈ 10%) stands.

### S11.2 — Transfer obituaries (§9.2: tempting external numbers that do NOT transfer)

- C3-141 | Sarvam 87.39 bench number — obituary | 2026-09-27 | DEAD | 5/5/5
  - The number is real on the hackathon bench harness and stays our BENCHMARK TARGET. It DIES for every build decision: different harness (their bench vs our 200-dpi probe + our scorer), unknown per-language cells vs our weak cells (sat 53.91/ks 54.82/OldScan 55.3/or 80.01), and no published per-cell CER/WER we can route on. Decision it can change: none — D2 already skips the EN column on the same logic; no SFT volume, router, or W6-tree choice may cite 87.39.
  - TRANSFER: DIES — the harness fact that kills it is "scores are not comparable across harnesses" (§6.6 ablation owns comparability inside our harness only).
- C3-142 | olmOCR 2026 ACL demo (7B VLM, 260K PDF pages SFT + RL with visual unit tests over synthetic docs) | 2026 (ACL 2026 demo paper) | PRIMARY (excerpt opened 2026-09-27) | 4/5/4
  - Mechanism → result: two-stage recipe (SFT on 260K diverse PDF pages, then RL with verifiable visual unit tests on synthetic documents with known HTML GT) + fully-open release loop. Maps to our RLVR posture (B1): verifiable-reward RL on synthetic gold is the closest 2026 precedent for "RLVR on human-verified gold after §6.6".
  - Numbers DEAD for decisions (Latin PDFs, 7B scale, English docs — none of our weak cells); recipe SURVIVES as the RLVR-stage template. Decision it can change: RLVR reward design post-freeze (visual-unit-test pattern for box-grounded verification, pairs with C3-095).
  - TRANSFER: method SURVIVES / numbers DIES — harness facts: ≤2B envelope, 18 Indic langs, no training until W6 freeze.

### S11.3 — NEW §9-native sourcing records (C3-116…C3-140; quality-first, licensing, GT gates)

Nastaliq (ks/ur/sd):

- C3-116 | https://huggingface.co/datasets/Omarrran/KS-PRET-5M_5_million_kashmiri_Pretrainning_LLM_dataset_12M_tokens_2026 | 2026-04 | PRIMARY (card excerpt opened 2026-09-27) | 5/5/5
  - KS-PRET-5M: 5,090,244 words / ~12.13M subword tokens Kashmiri, 11-stage cleaning pipeline preserving Nastaliq fidelity, script purity 81.3% Nastaliq/Perso-Arabic, CC-BY-4.0, paper arXiv 2604.11066. Largest public ks text pool — supersedes KS-LIT-3M (C3-010) as the DEFAULT ks render-string base (still sampling base, NOT GT labels).
  - Measurement honesty: card admits web-crawl register + minor OCR artifacts from digitized sources — the §B1-equivalent script gate + histogram still mandatory per batch. Decision it can change: ks R2§C2 render-string source selection (5M > 3.1M words, cleaner license story).
  - TRANSFER: SURVIVES — CC-BY-4.0 + Nastaliq-majority + same 200-dpi-print domain intent; harness fact saving it is script-purity reporting (0.9965 mean KS ratio).
- C3-117 | https://arxiv.org/abs/2607.20385 (Persian Pixel: 343k+ high-fidelity synth image-text pairs, sentence/paragraph/full-page, SynthOCR-Gen framework, 25+ stochastic degradations) | 2026-07-22 | PRIMARY (abstract excerpt opened 2026-09-27) | 4/5/5
  - Second 2026 proof that the SynthOCR-Gen chassis (C3-011/089) scales to Perso-Arabic: contextual joining, positional variants, diacritics, 7M-word corpus → sentence→page layouts, TrOCR/Donut-class fine-tuning target.
  - CER/volume numbers DIES for ks (Persian ≠ Kashmiri-Yeh U+0620 coverage; no Yeh claim in abstract); the CHASSIS choice at freeze gains evidence (now 2 independent 2026 proofs: 600k-ks + Persian Pixel). Decision it can change: freeze chassis pick (TRDG vs SynthTIGER vs SynthOCR-Gen).
  - TRANSFER: method SURVIVES / numbers DIES — harness fact: U+0620 gate (C3-031) is ks-specific and untested in this pipeline.
- C3-118 | https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.465 (OpenITI MAKHZAN: 1,497 page images, 286 Nastaliq incl. 73 Urdu; GT + evaluation data, 9 script combinations) | 2025–2026 (journal) | PRIMARY (excerpt opened 2026-09-27) | 4/4/3
  - Largest open Nastaliq GT aggregation found (73 Urdu Nastaliq pages + 200 Persian Nastaliq): candidate ur Nastaliq EVAL anchor alongside UNB (C3-017).
  - Domain mismatch load-bearing: manuscript/print heritage (1420–1873 manuscripts + publications) vs our 200-dpi citizen scans — tag domain before any use; license/access terms to confirm at freeze. Decision it can change: ur eval-anchor pool (UNB + MAKHZAN vs UNB alone).
  - TRANSFER: UNKNOWN — superb GT hygiene, wrong century and wrong domain until a sample passes visual inspection.
- C3-119 | https://arxiv.org/html/2605.01323v2 (SiNFluD: Sindhi figurative-language benchmark; resource survey lists Sindhi Raw Corpus Official 2024, Dootio corpus, POS/NER sets) | 2026-05 | PRIMARY (excerpt opened 2026-09-27) | 3/4/4
  - Confirms the sd text-resource checklist beyond Dootio (C3-026): Sindhi Raw Corpus Official (2024) becomes the first sd sampling-base verification target at freeze; annotation was expert-guided (Docanno, linguist-supervised) — a quality signal for any sd human-gold mining later.
  - Figurative-register caveat: idioms/proverbs ≠ prose OCR domain — sampler share capped like poetry-register (C3-022 rule). Decision it can change: sd render-string source checklist order at freeze.
  - TRANSFER: SURVIVES as pointer / UNKNOWN per item until host + license + script-split verified.
- C3-120 | https://sindhilanguage.org/dataset (Sindhi Open Lexicon Master: 223,342 entries, CSV/JSONL/SQLite, attribution-mandatory, research/AI/NLP use) | live 2026-09-27 | PRIMARY (excerpt opened 2026-09-27) | 4/4/4
  - 88,947 native Sindhi words + Mewaram 1910 (29,514, public-domain age) + official terms 37,599: sd word-level render strings + rare-word booster at ledger-clean provenance (named curator, 1,781 downloads).
  - Load-bearing gates: (1) entry script is MIXED (Devanagari/Sindhi→English 16,519 rows exist) — per-line Perso-Arabic gate mandatory; (2) license is bespoke attribution terms, not SPDX — hackathon-SFT posture with attribution file, product reuse UNKNOWN. Decision it can change: sd word-stage render budget (no longer zero-lexicon).
  - TRANSFER: SURVIVES-IF gated + attributed — harness fact: script gate decides keep vs route per line (C3-042 rule generalized).
- C3-121 | https://arxiv.org/html/2505.13943v2 (Press-to-Pixels: UNB 829 Nastaliq newspaper blocks; OpenITI Naskh/Nastaliq 250+250; Gemini-2.5-Pro WER 0.133 UNB; 500-line GPT-4o FT −6.13% WER) | 2025–2026 (LREC-2026 pp.3013–3021) | PRIMARY (excerpts opened 2026-09-27) | 5/5/5
  - Re-confirms C3-017 spans with pipeline table (article seg 26,830 / column seg 3,969 / SR 38,512 / UNB 829): the +SwinIR SR (+50% avg accuracy) result is a preprocessing-arm input for the OldScan/degraded Nastaliq lane, and the 500-line/−6.13% datum re-anchors the ks 300–500-real-line budget (C3-006) on a second Nastaliq sample.
  - Vendor WERs (Gemini/GPT-4o/Claude/Llama) get obituary: API models on newspaper blocks ≠ our offline ≤2B VLM on 200-dpi citizen docs — DEAD for routing. Decision it can change: ks real-line budget confirmation + SR preprocessing candidacy.
  - TRANSFER: eval anchor + budget datum SURVIVE / vendor numbers DIE.
- C3-122 | https://arxiv.org/html/2306.15782v1 (UTRNet: UTRSet-Real 9,065 train/2,096 val + UTRSet-Synth 20,000; only UPTI had train-scale volume and is synthetic; UPTI-trained → Real collapse) | 2023 | PRIMARY (table excerpt opened 2026-09-27) | 5/3/5
  - Re-confirms C3-014 with the exact split table (vocab 22,964 real / 28,187 synth) + corrected-IIITH detail: the cross-domain collapse number (UPTI-trained → 54.84% on Real per C3-014) is the quantitative spine of the synth+real mixing rule.
  - OBITUARY: UTRNet accuracy/SOTA claims are CTC/CNN-RNN-era on Naskh-heavy lines — DEAD for ks/ur VLM routing and for any "published accuracy ⇒ our CER" inference. Decision it can change: ur mixing rule (reaffirmed), never engine choice.
  - TRANSFER: method datum SURVIVES / accuracy numbers DIES.

Santali / Ol Chiki:

- C3-123 | https://www.unicode.org/charts/PDF/U1C50.pdf (Unicode 17.0 Ol Chiki code chart, 48/48 assigned) | 2025-08-04 | PRIMARY (chart excerpt opened 2026-09-27) | 4/5/5
  - Re-anchors C3-048 to the current standard: block U+1C50–U+1C7F fully assigned (10 digits + 30 letters + 6 modifiers + 2 punctuation), zero reserved — the ≥80% gate regex `[\u1C50-\u1C7F]` covers the complete assigned set with no dead ranges to trip on.
  - Decision it can change: §B1 gate definition freeze (no regex revision needed; alphabet properties — no conjuncts/reordering — re-confirmed, Pillow-BASIC-correct stands).
  - TRANSFER: SURVIVES — standard text, no harness dependency.
- C3-124 | https://aclanthology.org/2025.mmloso-1.9 (EN–Santali MT in Ol Chiki: IndicTrans2 FT 26.8 BLEU sat→en / MMLoSo shared-task dataset + Flores200-dev/IN22-Gen eval) | 2025-12-01 | PRIMARY (abstract excerpt opened 2026-09-27) | 4/4/4
  - New sat string-pool pointer: the MMLoSo shared-task EN–sat dataset (plus IN22-Gen sat slice) joins FLORES + sat.wiki as the third Ol-Chiki render-string source — verify license/access at freeze; MT-derived strings inherit the translationese cap (≤20%, C3-073 rule).
  - BLEU numbers DIES for OCR (translation quality ≠ render suitability); the DATASET EXISTENCE is the record. Decision it can change: sat sampler composition (3-source blend reduces single-source style bias).
  - TRANSFER: UNKNOWN until terms verified — strings are strings, but access + license are unestablished.
- C3-125 | https://github.com/dn143nibaran/Digitization-of-santali-language-Ol-chiki-Script (Ropor: Santali Ol-Chiki digitization + OCR + community verification ambition) | live 2026-09-27 | PRIMARY (excerpt opened 2026-09-27) | 2/4/3
  - Community-ecosystem pointer: confirms live grassroots Ol-Chiki OCR interest (verification/translation systems ambition) — watch at freeze for usable artifacts, but today it is ambition + app scaffolding, not a dataset.
  - No volume, no license, no GT claimed — budgeting zero lines from it. Decision it can change: none today (pointer only); re-check at freeze.
  - TRANSFER: UNKNOWN — honest-empty on all decision-relevant facts; recorded so the call doesn't double-count "community OCR" as coverage.
- C3-126 | https://mozilladatacollective.com/datasets/cmqie985k00cbnr07z9cea5wy (Common Voice Scripted Speech 26.0 — Santali Ol Chiki) | live 2026-09-27 | PRIMARY (listing excerpt opened 2026-09-27) | 2/3/2
  - Speech corpus with Ol-Chiki-script prompts: transcripts are render-string-usable IN PRINCIPLE, but speech-transcript conventions (read-speech register, prompt formatting) + Data Collective access terms make this a low-yield path vs sat.wiki/FLORES/MMLoSo.
  - Default posture DIES for the render plan (audio-first corpus; terms ungated-unknown); revisit only if all three text bases fail gates. Decision it can change: sat fallback-source ordering (ranked last).
  - TRANSFER: DIES — harness fact: we need running prose strings, not read-speech prompts behind new terms.

Manipuri / Meitei Mayek:

- C3-127 | https://huggingface.co/datasets/MWirelabs/meitei-monolingual-corpus (1,766,810 sentences Meitei, Bengali script, CC-BY-SA-4.0, cleaned/deduped 2025) | 2025 | PRIMARY (card excerpt opened 2026-09-27) | 4/4/4
  - 1.77M-sentence mni LANGUAGE base — but explicitly Bengali-script ("does not include Meitei Mayek script"): enters only through the transliteration gate (≥95%/500-line native check, C3-051 rule) or as language-model-side statistics, never as Mayek render strings directly.
  - CC-BY-SA-4.0 → minority-share + attribution + sidecar lineage (C3-081 posture). Decision it can change: mni language-sampling volume (largest mni sentence pool found) IF the transliteration gate passes; else DIES to statistics-only.
  - TRANSFER: SURVIVES-IF transliteration verifies / script itself DIES for Mayek renders.
- C3-128 | https://data.ldcil.org/a-gold-standard-manipuri-raw-text-corpus (LDC-IL: 6,145,278 words / 43M chars, 6 domains, typed+cleaned, Unicode XML+metadata, 2019) | 2019 | PRIMARY (catalog excerpt opened 2026-09-27) | 3/3/4
  - Largest curated Manipuri text pool (aesthetics 61.4% + mass media 12.6% + official 7.2% + science 5% + social science 13.5%): ask-don't-assume pointer — price-gated ("login to see price"), script unverified (2019-era LDC-IL Manipuri is Bengali-script-typical), terms per catalog.
  - No request without user yes (standing no-money + no-download laws); script check precedes any transliteration-gate discussion. Decision it can change: mni source checklist order (ranked behind free MIT/CC-BY bases unless terms are trivially clearable).
  - TRANSFER: UNKNOWN — price + script + license all unestablished; successful output naming exactly what the freeze call must ask.
- C3-129 | http://unicode.org/cldr/charts/43/delta/mni_Mtei.html (CLDR 43: mni_Mtei main letters ꯀ-ꯪ꯬꯭, mtei default numbering ABF0–ABF9, Mayek display names) | 2025 (CLDR 43) | PRIMARY (excerpt opened 2026-09-27) | 3/4/4
  - Corroborates C3-065 with a newer CLDR cut: main-letters range + Lum/Apun + Mayek digits as default numbering — sampler seed lists and the digit-booster wordlists stay valid; no gate change.
  - Decision it can change: none (corroboration) — recorded so the freeze doesn't re-derive exemplar ranges from scratch.
  - TRANSFER: SURVIVES — standard text.
- C3-130 | https://huggingface.co/datasets/DayanandaThokchom/meitei-mayek-to-english (Mayek↔EN parallel, professionally curated per card) | live 2026-09-27 | PRIMARY (card excerpt opened 2026-09-27) | 3/4/4
  - Second Mayek-script parallel pool corroborating C3-053's scale claim (461k EN→Mayek): dedupe against C3-053 at freeze (same curator family — overlap likely, never double-count volume); same MIT-expectation + translationese caveat + §B1 gate.
  - Decision it can change: mni render-string base composition (union-then-dedupe, not sum).
  - TRANSFER: SURVIVES under the same terms as C3-053 once license + overlap verified.

Odia (80.01 cell):

- C3-131 | https://www.odiagenai.org/blog/odia-ocr-qwen2-5-vlm (odia-ocr-qwen-finetuned: Qwen2.5-VL-3B, 58,720 validated pairs, LoRA r=64/α=128, H100-80GB, ~70% accuracy, CER 20–40% by doc type) | 2026-02-25 | PRIMARY (excerpt opened 2026-09-27) | 5/5/5
  - Re-confirms C3-071 with fuller config (early stop step 6,400; eval loss ~5.45; merged 3-source dataset incl. degraded scans/uneven lighting): the ~59k-pairs × LoRA × single-H100 recipe is the binding or-budget precedent — our S3 stage (50:20:30, ≤30 GPU-h at ≤2B) is conservative against a measured 3B precedent.
  - OBITUARY on its CER/accuracy: word/line-level crops on their bench ≠ our 200-dpi citizen-doc harness — DEAD for or-routing claims; SURVIVES for budget + recipe. Decision it can change: W6 GPU-budget ask (H100-class reference cost) + or SFT volume ceiling.
  - TRANSFER: recipe + budget SURVIVE / absolute numbers DIE.
- C3-132 | https://huggingface.co/OdiaGenAIOCR/odia-ocr-qwen-finetuned-merged (merged full model: LoRA r=16/α=32 merged, fp16 7.5GB, ≥16GB VRAM, 73k samples; strip-split ~400px tip for full pages) | 2026 | PRIMARY (card excerpt opened 2026-09-27) | 4/4/4
  - Two harness-actionable facts: (1) ≥16GB VRAM floor for 3B-class or inference → feeds the W6 FEASIBLE-SET table (C3-140: laptop-vs-cloud row); (2) 400px strip-splitting recipe for full-page or OCR → adopt into the or inference harness regardless of training path.
  - Sample outputs show conjunct errors (ସୂଚିପତ୍ର→ସୃଗପତ୍ରା) — honest error display, consistent with CER 20–40% band. Decision it can change: or page-level inference recipe + W6 hardware feasibility column.
  - TRANSFER: SURVIVES — recipe and VRAM floor are harness facts, not bench numbers.
- C3-133 | https://huggingface.co/datasets/tell2jyoti/odia-handwritten-ocr (182,152 imgs, 47 OHCS classes, 32×32 gray, MIT, v1.0.0 Jan 2026, 92 downloads/mo) | 2026-01 | PRIMARY (card excerpt opened 2026-09-27) | 4/4/4
  - Re-confirms the C3-067 MIT slice with version + liveness (Jan 2026, active downloads): char-stage warm-up ONLY verdict stands (32px isolated chars ≠ page OCR); stratified splits with no overlap is a hygiene model for our own synth splits.
  - Decision it can change: or char-stage warm-up source pin (v1.0.0, MIT — approval-clean).
  - TRANSFER: SURVIVES — MIT + versioned + live; granularity mismatch contained by scope tag.
- C3-134 | https://ilocr.iiit.ac.in/dataset/21 (IIIT NLTM Oriya HW words: 101,467 word images + GT transcriptions, form-box collection) | live 2026-09-27 | PRIMARY (excerpt opened 2026-09-27) | 3/3/4
  - 100k-scale or word-image pool with GT — the largest or word-level anchor after Mozhi: eval-slice pointer (handwriting domain → printed-SFT excluded regardless of access); terms/license to confirm at freeze (IIIT NLTM cards vary).
  - Decision it can change: or handwriting-eval slice composition (future work only — never the printed probe).
  - TRANSFER: UNKNOWN — volume and GT practice look right; terms + access unestablished.
- C3-135 | https://huggingface.co/datasets/OdiaGenAIOCR/odia_ocr_benchmark_data (viewer-confirmed: 223 rows, id/image/ground_truth/category, CC-BY-NC-SA-4.0) | 2026 | PRIMARY (viewer excerpt opened 2026-09-27) | 4/4/4
  - Re-confirms C3-070 schema live (category field present → error-tag stratification possible): pooled or-eval (probe or_69 tier + lipi + 223 bench ≈ 350+) reaches §6.7 CI-grade for the or cell specifically.
  - Decision it can change: or eval-pool composition for Phase 6 (pooled-n power claim).
  - TRANSFER: SURVIVES as eval, hackathon-only (NC).

OldScan (55.3 cell) + restoration method references:

- C3-136 | https://www.mdpi.com/2076-3417/15/15/8374 (Tarbă 2025: SOTA binarization, avg F-measure 95.8% vs previous 93.1% across DIBCO sets; DIBCO 2019 beaten) | 2025 (cited 7×) | PRIMARY (excerpt opened 2026-09-27) | 4/4/4
  - Recalibrates the learned-head ceiling inside the C3-108 band (+8–18 FM over classical holds; new top 95.8% avg): NO change to the Otsu-first order (A0/A1 run before any learned pilot) — ceiling moved, floor didn't.
  - OBITUARY: F-measures are binarization-internal on Latin/Greek DIBCO sets — DEAD as OCR CER substitutes and DEAD as Indic transfer (R4 binding stands). Decision it can change: ablation-sheet ceiling reference only.
  - TRANSFER: ceiling reference SURVIVES / everything else DIES.
- C3-137 | https://link.springer.com/chapter/10.1007/978-3-031-41734-4_13 (ColDBin, ICDAR 2023: cold-diffusion binarization, first diffusion work, 9 benchmark sets) | 2023 | PRIMARY (excerpt opened 2026-09-27) | 3/3/4
  - Reinforces the C3-108 diffusion-deferral with the concrete citation: diffusion binarization exists and benchmarks well on 9 sets, but needs GPU training + risks thin-stroke glyph damage (Nastaliq dots / Mayek vowel signs per the C5 dot-audit) — our CPU ≤3 min/page guardrail keeps it parked.
  - Decision it can change: none (deferral reaffirmed) — recorded so the call doesn't reopen "try diffusion" without answering the glyph-risk + compute questions first.
  - TRANSFER: DIES for our pipeline under current rules (FEASIBLE-IF a GPU budget + dot-audit pass ever arrives).
- C3-138 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8320943 (J. Imaging review: binarization-before-OCR architecture; DIBCO metrics; no-GT analysis via downstream OCR impact) | 2021 (review, via PMC) | PRIMARY (excerpt opened 2026-09-27) | 3/3/4
  - Licenses our C3-008 ablation design from the literature: restoration judged by ΔCER on the downstream OCR task (not by binarization FM alone) + "analyze performance without GT via secondary-step impact" is the sanctioned no-GT method — exactly our adopt-bar (median ΔCER ≤−0.03, 95% bootstrap CI, ≥2/3 frozen engines).
  - Decision it can change: OldScan ablation scoring protocol (reaffirmed, now literature-cited for the validation call).
  - TRANSFER: SURVIVES — protocol-level transfer, zero data, zero compute.

Quality-first / licensing / GT-gate law records (§9 items 3–5):

- C3-139 | Campaign §9.3 estimator law adopted for Phase 6 (Wilson 95% intervals on per-language engine CER; McNemar exact on SAME-item paired comparisons, never point deltas; test family pre-declared per §6.7; abstention = coverage + conditional CER) | 2026-09-27 | DERIVED (protocol synthesis — no new data, formula: law stated verbatim) | 5/5/5
  - Kills point-estimate winner claims on n<50 cells (as/gu/ne/doi/mni/sat) and any silent honest-empty handling. Decision it can change: Phase 6 scoring + leaderboard validity (every per-language claim must carry CI; engine routing on small cells uses script-family pools per §6.7).
  - TRANSFER: SURVIVES — pure harness protocol, no external dependency.
- C3-140 | Campaign §9.4–9.5: W6 feasible set (FEASIBLE NOW / FEASIBLE-IF / INFEASIBLE) + pre-declared kill criteria with operator-set thresholds | 2026-09-27 | UNKNOWN (two missing primaries: GPU-budget answer; operator thresholds) | 5/5/4
  - FEASIBLE NOW per D1: wrap-only baseline (hybrid routing + restoration, zero GPU). FEASIBLE-IF: local QLoRA on SAFE langs (needs Phase-6 McNemar-significant gap + laptop-memory check) + ColDBin-class heads (needs GPU + dot-audit pass). INFEASIBLE UNDER CURRENT RULES: cloud GPU spend (no-money law), 4-bit recognizer quant (C3-094), API-at-inference (C3-111).
 - Kill criteria drafted as conditions on MEASURED numbers; thresholds are operator parameters — agents invent none. Decision it can change: validation-call go/no-go inputs + GPU-budget ask.
 - TRANSFER: n/a (internal) — recorded as UNKNOWN so the call sees exactly which primaries are missing instead of a soft guess.

---

## §9 LATEST-REFRESH 2026-09-27 (Lane C3 latestness refresh; append-only — C3-001–142 + STRATEGY.md untouched)

Law: no downloads executed, no training, no rows above rewritten. Each row below is CONFIRM (old row stands, delta noted) or SUPERSEDE (old row ID + delta). Status set is exactly PRIMARY / MEASURED / DERIVED / CONTRADICTION / UNKNOWN / REJECTED / DEAD. Transfer verdict per row is SURVIVES / DIES / UNKNOWN against OUR harness facts only (18 Indic langs; weak cells sat 53.91 / ks 54.82 / OldScan 55.3 / or 80.01; 200-dpi citizen docs; no paid keys; no training until W6 freeze; offline-capable pipeline; no 400-page sets). Live sources only (web_search/web_fetch 2026-09-27).

### Fonts (directive item 1)

- C3-143 | CONFIRM C3-047 — Noto Sans Ol Chiki still current, no 2026 glyph update | https://fonts.google.com/noto/specimen/Noto+Sans+Ol+Chiki + https://pkgs.alpinelinux.org/package/edge/community/x86_64/font-noto-ol-chiki + https://github.com/notofonts/ol-chiki (fetched 2026-09-27) | PRIMARY | 5/4/5
  - Delta: Google Fonts specimen still "~55 glyphs / multiple weights"; Alpine edge rebuild `2026.09.01-r0` (build 2026-09-01, commit aca62ae) is a PACKAGING rebuild, not a glyph-coverage release; notofonts/ol-chiki repo static (16 commits, created 2022-06-20, OFL-1.1). No 2026 version bump with new Ol-Chiki coverage found.
  - Decision it can change: sat render-matrix single-design constraint stands (degradation-heavy diversity + held-weight-700/held-seed synth-val, C3-047).
  - TRANSFER: SURVIVES — OFL-1.1 re-confirmed; harness fact saving it is the approval-clean Alpine install path (sidecar still records exact distro version).
- C3-144 | CONFIRM C3-060 — Noto Sans Meetei Mayek still current, no 2026 glyph update | https://pkgs.alpinelinux.org/package/edge/community/s390x/font-noto-meetei-mayek + https://github.com/notofonts/meetei-mayek (fetched 2026-09-27) | PRIMARY | 5/4/5
  - Delta: Alpine edge rebuild `2026.09.01-r0` (2026-09-01) mirrors C3-143 (packaging only); notofonts/meetei-mayek static (18 commits, OFL-1.1). 9-weight TRAIN-side verdict unchanged; no 2026 weight/coverage addition found.
  - Decision it can change: mni TRAIN-side design pin (Noto) vs Eeyek-held-for-val split unchanged.
  - TRANSFER: SURVIVES.
- C3-145 | CONFIRM C3-061 — SIL Eeyek latest is v2.000, no newer 2026 release | https://github.com/silnrsi/font-eeyek/releases (fetched 2026-09-27) | PRIMARY | 5/4/5
  - Delta: latest release shown is "Eeyek 2.000 … Latest" (rebuilt workflow; joining-underline change; U+003F reencoded as U+AAF1 AHANG KHUDAM; ADDED U+ABE2 LETTER I LONSUM; Latin FULL STOP U+002E + basic Latin added). No 2026-dated successor found this pass. U+ABE2 addition corroborates the C3-064 Lonsum range.
  - Decision it can change: Eeyek stays held EXCLUSIVELY for synth-val (font-disjoint test); legacy GPL Eeyek stays EXCLUDED.
  - TRANSFER: SURVIVES — OFL-1.1 (RFN "Eeyek") re-confirmed.

### Unicode blocks (directive item 2)

- C3-146 | CONFIRM C3-048 + C3-123 — Ol Chiki block unchanged under current Unicode 17.0 | https://www.unicode.org/versions/Unicode17.0.0 + https://en.wikipedia.org/wiki/Ol_Chiki_(Unicode_block) + https://codepoints.net/ol_chiki (fetched 2026-09-27) | PRIMARY | 4/5/5
  - Delta: Unicode 17.0 (announced 2025-09-09; +4,803 chars → 159,801 total; 4 new scripts) is the CURRENT standard — no Unicode 18.0 exists as of 2026-09-27. Ol Chiki U+1C50–U+1C7F still 48/48 assigned ("As of Unicode version 17.0", block intro v5.1/2008). Zero 2026 chart changes.
  - Decision it can change: §B1 gate regex `[\u1C50-\u1C7F]` ≥80% frozen — no revision needed.
  - TRANSFER: SURVIVES — standard text, no harness dependency.
- C3-147 | CONFIRM C3-064 — Meitei Mayek blocks unchanged under Unicode 17.0 | https://www.unicode.org/versions/Unicode17.0.0 + https://github.com/silnrsi/font-eeyek/releases (U+ABE2 evidence) (fetched 2026-09-27) | PRIMARY | 4/4/5
  - Delta: no 2026 Mayek-block delta found (modern U+ABC0–ABFF + historic U+AAE0–AAFF assignments stand; Eeyek v2.000's U+ABE2 addition tracks the existing Lonsum range, not a new encoding). CLDR C3-065/C3-129 exemplars unaffected.
  - Decision it can change: Mayek gate rules (≥80% U+ABC0–ABFF; historic ≤2%; NFC; HarfBuzz mandatory; raqm-abort) frozen.
  - TRANSFER: SURVIVES.

### Corpora sizes 2026 vs cited (directive item 3)

- C3-148 | CONFIRM C3-040 — Santali Wikipedia size static vs cited | https://en.wikipedia.org/wiki/Santali_Wikipedia + https://wikiq.net/santali-wikipedia (fetched 2026-09-27) | PRIMARY | 4/4/4
  - Delta: EN page still shows 11,414 users / 15,928 articles (matches C3-040's ~15,928); WikiQ profile: ~14.5k articles, 44 active users, peak creation Feb 2025 (1.3k). No 2026 dump-size jump established — sampling plan (dump + NFC + ≥80% gate + N≥500/char histogram) unchanged.
  - Decision it can change: sat.wiki stays the largest Ol-Chiki running-text pool; first post-approval runnable unchanged.
  - TRANSFER: SURVIVES — CC-BY-SA dumps; share-alike posture per C3-081 (minority share).
- C3-149 | CONFIRM C3-037/C3-038 — FLORES-200 sat_Olck slice stable; mni still Bengali-script-tagged | https://github.com/ripingit/NLLB-200-Dataset/tree/main/flores200 (fetched 2026-09-27) | PRIMARY | 4/4/5
  - Delta: composition still 842 articles → 3,001 sentences, dev/devtest/test-hidden; listing confirms `Santali | sat_Olck` present and `Meitei (Bengali script) | mni_Beng` — mni Mayek slice STILL absent, so the C3-037 script-tag gate for mni stands. No FLORES-200 v-change in 2026 found.
  - Decision it can change: sat bootstrap (≈60k words) + mni-slice gate unchanged; synth-never-eval stands.
  - TRANSFER: SURVIVES (canonical CC-BY-SA source only; SEACrowd NC mirror still DIES per C3-039).
- C3-150 | CONFIRM C3-062 — Hueiyen Lanpao Mayek-daily pointer static; bulk ban reaffirmed | https://en.wikipedia.org/wiki/Hueiyen_Lanpao (page last edited 2026-05-17, fetched 2026-09-27) | PRIMARY | 3/3/2
  - Delta: only change since citation is a May-2026 page edit (Bengali-script + Meetei Mayek editions noted); no 2026 bulk-release or license change — © newspaper posture unchanged.
  - Decision it can change: none — DO NOT bulk-scrape (what-NOT list); layout-observation-only role stands.
  - TRANSFER: DIES as text source (reaffirmed) / SURVIVES as block-render style reference.

### Kashmiri corpora availability + license re-confirm (directive item 4)

- C3-151 | CONFIRM C3-116 — KS-PRET-5M live, CC-BY-4.0 re-confirmed | https://huggingface.co/datasets/Omarrran/KS-PRET-5M_5_million_kashmiri_Pretrainning_LLM_dataset_12M_tokens_2026 + https://arxiv.org/abs/2604.11066 (fetched 2026-09-27) | PRIMARY | 5/5/5
  - Delta: card live (Tasks: Text Generation/Fill-Mask; 5,090,244 words · ~12.13M subword tokens · 295,433 vocab · April 2026; License: cc-by-4.0; arXiv 2604.11066; 11-stage pipeline; script purity 0.9965 KS ratio). Matches C3-116 exactly — no takedown, no license flip.
  - Decision it can change: DEFAULT ks render-string base stays KS-PRET-5M (supersedes KS-LIT-3M on volume + purity reporting); still sampling base, NOT GT labels.
  - TRANSFER: SURVIVES.
- C3-152 | CONFIRM C3-009/C3-012 — 600k-ks-ocr live; Koshur Pixel (June 2026) corroborates | https://www.alphaxiv.org/abs/2601.01088 + https://www.alphaxiv.org/abs/2606.23144 (fetched 2026-09-27) | PRIMARY | 5/4/5
  - Delta: 600K-KS-OCR datum re-confirmed (~602k word-level 256×64 images, 3 Kashmiri typefaces, CRNN/TrOCR/ML formats); Koshur Pixel paper (Malik/Iqbal/Nissar, submitted 2026-06-22, arXiv 2606.23144) is the same team's June-2026 synthesis write-up — second 2026 proof of the pipeline, not a new host. CC-BY-4.0 chain intact; repo↔HF parity (C3-012 UNKNOWN) still unverified — canonical HF host preferred.
  - Decision it can change: ks word-stage SFT fuel unchanged (word-level only; line/block curriculum still needs R2§C2 renders from KS-PRET-5M strings).
  - TRANSFER: SURVIVES.
- C3-153 | SUPERSEDE C3-010 (license header) — KS-LIT-3M card shows cc-by-sa-4.0, contradicting the paper's CC-BY-4.0 | https://huggingface.co/datasets/Omarrran/3.1Million_KASHMIRI_text_Pre_training_Dataset_for_LLM_2026_by_HNM + https://arxiv.org/abs/2601.01091 (fetched 2026-09-27) | CONTRADICTION | 4/4/4
  - Delta: HF card header License field reads `cc-by-sa-4.0` (with bespoke PART A terms incl. "Model Training Restrictions") while the paper (arXiv 2601.01091, 2026-01-03) releases under CC-BY-4.0. Both quotes stored; no winner picked. Dataset live (tasks Text Generation/Table QA/Fill-Mask, <1K size-class).
  - Decision it can change: KS-LIT-3M drops to share-alike-quarantined backup (minority share + attribution + sidecar lineage per C3-081) until the freeze resolves header-vs-paper; DEFAULT stays KS-PRET-5M (clean CC-BY-4.0).
  - TRANSFER: UNKNOWN — harness fact deciding it (which license the freeze approval cites) is unestablished; successful output, not a hole.

### Bodhan Indic-OCR since Sept 2026 (directive item 5)

- C3-154 | SUPERSEDE C3-110 (release-dated) — Bodhan September 2026 collection (5 Sep 2026, 5 items) live on HF | https://huggingface.co/bodhan-ai/indic-ocr + https://huggingface.co/bodhan-ai/collections (fetched 2026-09-27) | PRIMARY | 5/5/4
  - Delta: "Bodhan September 2026 Collection … released as part of 5 Sep 2026 release • 5 items • Updated 18 days ago" — the P2 baseline now has a dated release where C3-110 recorded an undated probe baseline. Citation `@misc{indicocr2026, title={IndicOCR: Multilingual Document Parsing for English and 22 Indian Languages}, author={Bodhan AI and AI4Bharat}}` + bodhan.ai research blog pointer new vs ledger. No pricing/weight-pull terms established this pass.
  - Decision it can change: sat router question (R7 N5b, Bodhan leads sat 68.30) gains a dated artifact to cite; or/Indic cross-bench (C3-155) joins the falsification comparison. Still BASELINE-NOT-DATA-SOURCE — no weight pull without GPU-budget approval (§6.8 P2).
  - TRANSFER: SURVIVES as baseline / UNKNOWN on weights reuse until license + VRAM terms verified at freeze.
- C3-155 | NEW — Sarvam Vision 2.1 blog tables give the first Bodhan-vs-Sarvam cross-bench numbers | https://www.sarvam.ai/blogs/sarvam-vision-2-1 (2026-09-24, fetched 2026-09-27) | PRIMARY | 4/4/4
  - Delta: olmOCR-Bench Overall — Sarvam Vision 2.1 87.3 (OldScan cell 55.3) vs Bodhan Indic-OCR 78.8 (OldScan 45.8); OmniDocBench v1.6 Overall — PaddleOCR-VL 1.6 96.01 vs Sarvam 2.1 94.97 vs Bodhan 92.17 vs DeepSeek-OCR2 87.91. New vs ledger (no cross-table existed).
  - Decision it can change: engine shortlist / falsification-comparison inputs only — absolute numbers get obituary (their harness ≠ our 200-dpi probe + scorer; C3-141 rule extended).
  - TRANSFER: numbers DIES for CER-routing / existence-proof SURVIVES (Bodhan parses 22 Indian languages per collection title).

### Sarvam Vision since 2.1 (directive item 6)

- C3-156 | CONFIRM (no 2.2) — Sarvam Vision 2.1 (2026-09-24/25) is latest; no 2.2+ or bench refresh found | https://www.sarvam.ai/blogs/sarvam-vision-2-1 + https://m.economictimes.com/tech/artificial-intelligence/sarvam-ai-updates-vision-model-doubles-down-on-indic-language-push/amp_articleshow/134480718.cms + https://www.sarvam.ai/ (fetched 2026-09-27) | PRIMARY | 5/5/5
  - Delta: 2.1 released 2026-09-24 (blog "Pushing the Pareto frontier"; ET 2026-09-25 02:37 PM IST); Indic bench 6,909 samples (6,609 × 22 langs + 300 EN), scores olmOCR-Bench 87.3 / Indic 87.39; API ₹1.50/page; harness = VLM + semantic layout parser + pointer reading-order net. Sarvam homepage "Research & Updates" lists nothing newer (latest 2026-08-11 DiarBench). Epoch-2026 items (Vision 2.0, Bulbul 4, 105B, 1T-param ambition) are older/superseded context, not a 2.2.
  - Decision it can change: benchmark target stays Vision 2.1; D2 EN-skip + 54-call cap unaffected; C3-141 obituary extends verbatim to the 87.3/87.39 pair (different harness, unknown per-weak-cell CERs).
  - TRANSFER: target SURVIVES / numbers DIES for every build decision.

### New Sept-2026 ur/ks/or datasets or benchmarks (directive item 7)

- C3-157 | NEW — Urdu OCR Multi Source Dataset (Proxima AI, 2026-08-05) pointer only | https://mozilladatacollective.com/datasets/cmsgbzj8d00nlnq08a90220nd (listing excerpt opened 2026-09-27) | UNKNOWN | 2/3/2
  - Delta: listing exists (Aug 2026) — the only ur-OCR-dataset-class item newer than UNB found this pass. Card terms, volume, script split (Nastaliq vs Naskh), license, and host access ALL unverified (listing excerpt only).
  - Decision it can change: freeze verification target (terms + per-file script split before any eval/SFT use); budgeted ZERO lines until cleared.
  - TRANSFER: UNKNOWN — recorded so the freeze doesn't miss it, never assumed.
- C3-158 | CONFIRM (negative result) — no Sept-2026 ks/or OCR bench newer than ledger anchors found | web_search sweep 2026-09-27 (Kashmiri OCR Sept 2026; Odia OCR bench 2026; Urdu OCR 2026) | DERIVED (negative-result synthesis from PRIMARY sweep — formula: 3 directed queries, newest hits = Aug-2026 ur listing / June-2026 Koshur Pixel / May-2026 UNB-LREC) | 3/4/3
  - Delta: newest ur anchor remains UNB (829 blocks, LREC-2026 pp.3013–3021, ACL Anthology page live); newest ks anchor remains Koshur Pixel/600k (June 2026); or anchors remain lipi + 223-row bench (C3-069/070/135). LREC-2026 ur TTS bench (shahid-izharuddin-2026-benchmark) and UQuAD+ are non-OCR — explicitly NOT counted.
  - Decision it can change: eval-anchor pool frozen (UNB for ur Nastaliq; lipi+223+probe-or_69 pooled n≈350+ for or); no new approval request triggered.
  - TRANSFER: n/a (internal negative result) — SURVIVES as "no new source" for the validation call.
- C3-159 | CONFIRM C3-069/070/135 — Odia bench slice live and unchanged | https://huggingface.co/datasets/OdiaGenAIOCR/odia_ocr_benchmark_data (listing live, fetched 2026-09-27) | PRIMARY | 4/4/4
  - Delta: dataset page live; schema/count (223 rows, id/image/ground_truth/category, CC-BY-NC-SA-4.0) matches C3-070/135 — no growth, no license flip, no Sept-2026 successor found.
  - Decision it can change: or eval-pool composition (probe or_69 + lipi + 223 bench) frozen for Phase 6 power claims.
  - TRANSFER: SURVIVES as eval, hackathon-only (NC).
- C3-160 | CONFIRM licensing posture — OFL-1.1 across all three fonts; Sept-2026 distro rebuilds change nothing legal | Alpine + notofonts + SIL Eeyek pages (fetched 2026-09-27, same evidence as C3-143–145) | PRIMARY | 4/3/5
  - Delta: OFL-1.1 confirmed on Alpine packages (both Noto fonts), notofonts repos (OFL-1.1), SIL Eeyek (OFL/RFN). 2026.09.01 distro rebuilds are packaging commits, not relicenses; rendered-images/model-weights-are-not-redistribution reading (C3-079) unchallenged by any 2026 source found.
  - Decision it can change: render-for-SFT posture unchanged for all W6 synthetic plans; OFL.txt travels with any shared render set.
  - TRANSFER: SURVIVES.

(End of §9 LATEST-REFRESH 2026-09-27 — 18 rows C3-143…C3-160: 15 CONFIRM, 2 SUPERSEDE (C3-153 KS-LIT-3M license contradiction; C3-154 Bodhan Sept-2026 dated release), 1 NEW-pointer + 1 negative-result + 1 NEW cross-bench folded into the 18. Ledger total: 158 records. Next: Verdict 10% sample of S11.3 + this section; STRATEGY.md consumes deltas at integration, not here.)

(End of §9 upgrade — 115 transfer lines + 2 obituaries + 25 new records C3-116…C3-140. Ledger total: 140 records. Next: Verdict 10% sample of S11 + STRATEGY.md verdicts consume S11.3; no downloads, no training, nothing outside this dir.)
