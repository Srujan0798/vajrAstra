# R3 — Ol Chiki (Santali) + Meitei Mayek (Manipuri) synthetic-training brief

Status: research for W6. No training. No downloads executed (2026-09-26 hard rule — human owns data provenance; every URL below is a pointer, not a fetch).
Why these two: worst long-tail cells on the public bench our probe inherits — Santali 53.91 (Sarvam 2.1) / 68.30 (Bodhan wins), Kashmiri 54.82, Manipuri 85.12 with frontier VLMs ~0 (`docs/probe/W3_PROBE_SCHEMA.md` §Public SOTA). Our probe confirms the script split is real: `mni` GT verified ~100% Meitei Mayek; `sat_14` verified Bengali-script Santali (memory feed §10). Santali is genuinely multi-script (Ol Chiki / Bengali / Devanagari / Odia / Latin); Manipuri is mid-migration (Bengali → Mayek, mandated switchover — The Hindu 2022-12-03).

---

## PART A — script inventory

### A1. Ol Chiki (Santali) — code points

| Fact | Value | Source |
|---|---|---|
| Block | U+1C50–U+1C7F, 48 code points, **all 48 assigned, 0 reserved** | https://www.unicode.org/charts/PDF/U1C50.pdf · https://en.wikipedia.org/wiki/Ol_Chiki_(Unicode_block) |
| Unicode version | 5.1 (April 2008) | https://en.wikipedia.org/wiki/Ol_Chiki_script |
| ISO 15924 | Olck, 261 | https://en.wikipedia.org/wiki/Ol_Chiki_script |
| Layout | U+1C50–1C59 digits (10) · U+1C5A–1C77 letters (30) · U+1C78–1C7D modifiers (Mu_ttuddag, Gaahlaa_ttuddaag, Mu-Gaahlaa, Relaa, Phaarkaa, Ahad) · U+1C7E–1C7F punctuation (Mucaad, double Mucaad) | https://www.unicode.org/charts/PDF/U1C50.pdf |
| Type | **True alphabet** (not abugida): vowels = full letters, no inherent vowel, no conjuncts, no reordering; syllable-final consonants via absence + Ahad/Phaarkaa marks; uniform letter height, no descenders | https://r12a.github.io/scripts/olck/sat.html (updated 2026-04-28) · https://en.wikipedia.org/wiki/Ol_Chiki_script |
| Direction | Left-to-right, alphabetic baseline (same as Latin) | https://r12a.github.io/scripts/olck/sat.html |
| Creator | Raghunath Murmu, 1925; publicized 1939 | https://www.omniglot.com/writing/olchiki.htm |

Shaping consequence (locks Part B): Ol Chiki needs **no complex shaping** — codepoint order == glyph order. Basic Pillow layout renders it correctly; Raqm/HarfBuzz still recommended for uniformity, not required.

### A2. Ol Chiki — fonts (license + downloadability, approval-gated hosts excluded)

| Font | License | Download (no login, no approval) | Coverage note | Source |
|---|---|---|---|---|
| **Noto Sans Ol Chiki** (Google) | **OFL-1.1** | https://fonts.google.com/noto/specimen/Noto+Sans+Ol+Chiki · https://github.com/notofonts/noto-fonts/blob/main/LICENSE · npm https://cdnjs.com/libraries/fontsource-noto-sans-ol-chiki · distro pkg https://pkgs.alpinelinux.org/package/edge/community/s390x/font-noto-ol-chiki | 4 weights (400–700) variable; 55 glyphs / 53 block chars per Google Fonts page | https://fonts.google.com/noto/specimen/Noto+Sans+Ol+Chiki · https://fontsource.org/fonts/noto-sans-ol-chiki |
| Essenfont (Ribose, universal U17) | check per-release (donor: Noto Sans Ol Chiki for this block) | https://www.essenfont.org/unicode/block/ol-chiki | Whole-Unicode fallback; same glyphs as Noto for this block | https://www.essenfont.org/unicode/block/ol-chiki |
| Community Ol-Chiki fonts (e.g. santaliwiki blogspot lists) | **mixed/unclear — DO NOT USE for training renders** until license verified | https://www.omniglot.com/writing/olchiki.htm (links list) | Approval/blog hosts; violates downloadability bar | — |

Hard truth: exactly **one verified OFL family** (Noto, single design, 4 weights). Synthetic glyph diversity for Ol Chiki ≈ weight × size × degradation only. No second OFL design found in this pass. Mitigations live in Part B (degradation-heavy diversity + TRDG distortion).

### A3. Santali — text corpora (for sampling render strings, NOT GT labels)

| Corpus | Ol-Chiki-script volume | License/access | Source |
|---|---|---|---|
| **sat.wikipedia.org** | **~15,928 articles**, 11,414 users (launched 2018-08-02; committee approval 2018-06-28) | CC BY-SA (Wikimedia dump, no approval) | https://en.wikipedia.org/wiki/Santali_Wikipedia · dump host https://sat.wikipedia.org |
| **FLORES-200 `sat_Olck`** | **3,001 sentences** (dev+devtest+test-hidden; ~21 words/sent avg → ~60k+ words parallel EN↔sat) | CC BY-SA (Meta) | https://github.com/facebookresearch/flores/blob/main/flores200/README.md?plain=1 |
| MMLoSo 2025 shared-task EN↔Santali (Ol Chiki); IndicTrans2-ft 26.8 BLEU sat→en / 7.3 en→sat on IN22-Gen | test-scale (IN22-Gen + Flores200-dev slices) | task data via AI4Bharat IN22 | https://aclanthology.org/2025.mmloso-1.9 |
| santali-nlp (GitHub): corpus + tokenizer + fastText + MT baselines, Ol Chiki | repo-scale (unquantified here — count on clone approval) | repo license | https://github.com/sami42200/santali-nlp |
| Crúbadán `sat` + `sat-Deva` (Scannell 2018) | web-crawl word lists, both scripts | open | via http://www.language-archives.org/language/sat |
| OLAC Santali: Rosetta Genesis/glossed text, Swadesh, grammar/orthography sketches; Glottolog sant1410 | small, mixed-script | open per-record | http://www.language-archives.org/language/sat |
| santals.in literature blog (native Ol Chiki prose) | site-scale | © site (sample strings only, no bulk scrape without say-so) | https://literature.santals.in/ |
| Wikilangs `sat` playground stats | 104,851-word vocabulary sample from sat.wiki | open | https://wikilangs.org/languages/sat |

Script-contamination warning (load-bearing for sampling): most Santali digital text is **not** Ol Chiki — Bengali, Devanagari, Odia, Latin all in use (https://en.wikipedia.org/wiki/Ol_Chiki_script; ICDAR-2023-HW confirms "Santali uses Ol Chiki/Bengali/Odia scripts", https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2023/icdar2033_tr.pdf). Every sampled string MUST pass the §B1 regex gate (U+1C50–1C7F ratio), or Bengali-script Santali poisons the Ol-Chiki renderer. (This is the same failure mode as our probe's `sat_14`.)

### A4. Santali — labeled OCR data (what exists: ~nothing native)

| Dataset | Santali content | Verdict |
|---|---|---|
| Mozhi printed-word OCR (CVIT IIIT-H; HF mirror 1,211,362 rows, 13 langs: as/bn/gu + 9) | **No Ol Chiki cell on the card's language list** | https://huggingface.co/datasets/darknight054/indic-mozhi-ocr · source https://cvit.iiit.ac.in/usodi/tdocrmil.php |
| ICDAR 2023 Indic handwriting competition | Santali listed among 22 langs (multi-script incl. Ol Chiki) — competition set, access/terms via organizers | https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/ConferencePapers/2023/icdar2033_tr.pdf |
| EkStep/Tarento synthetic OCR bench (90k images, 23 Indic langs, arXiv:2205.02543) | **Santali listed with Ol Chiki charset**; Manipuri listed as Devanagari (stale — pre-Mayek-switch) | https://arxiv.org/abs/2205.02543 · https://arxiv.org/pdf/2205.02543 |
| Official hackathon dataset (ours) | Santali: **3 PDFs, 0 extractable GT layers** (memory feed §2) | disk truth, no URL |

Net: zero native labeled Ol-Chiki OCR lines available to us today. Synthetic is not optional here — it is the only SFT fuel until a human labels real pages.

### A5. Meitei Mayek (Manipuri) — code points

| Fact | Value | Source |
|---|---|---|
| Blocks | **U+ABC0–U+ABFF (Meetei Mayek, 64 cps, 56 assigned, 8 reserved)** + **U+AAE0–U+AAFF (Extensions, historic orthographies)** | https://en.wikipedia.org/wiki/Meetei_Mayek_(Unicode_block) · https://codepoints.net/meetei_mayek |
| Unicode version | 5.2 (October 2009) | https://www.unicode.org/charts/nameslist/n_ABC0.html |
| ISO 15924 | Mtei, 337 | https://en.wikipedia.org/wiki/Meetei_Mayek_(Unicode_block) |
| Type | **Abugida**: 27 Iyek-Ipee consonants (15 native + vowels + 9 Indic-loan) · 8 Lonsum finals (ABDB–ABE2) · **7–8 dependent vowel signs ABE3–ABEA** · Apun Iyek killer ABED (→ U+103A analogue) · Lum Iyek tone ABEC · Cheikhei double-danda ABEB · digits ABF0–ABF9 | https://www.unicode.org/charts/nameslist/n_ABC0.html · https://www.everyalphabet.com/meitei |
| Extensions | Independent vowels AAE0–AAE1, extra consonants AAE2–AAEA, extra vowel signs AAEB–AAEF + visarga AAF5, virama AAF6, cheikhan/ahang-khudam/anji/repetition marks AAF0–AAF4 — historic/puya orthographies only | https://unicode.org/L2/L2008/08239r-n3478r-meetei-mayek-ext.pdf |

Shaping consequence: Mayek **requires complex shaping** (vowel-sign reordering/positioning around base consonants, Apun Iyek suppression). Pillow BASIC layout will misplace ABE3–ABEA signs. **HarfBuzz (Raqm) is mandatory**, not advisory.

### A6. Meitei Mayek — fonts

| Font | License | Download (no login) | Coverage note | Source |
|---|---|---|---|---|
| **Noto Sans Meetei Mayek** (Google) | **OFL-1.1** | https://fonts.google.com/noto/specimen/Noto+Sans+Meetei+Mayek · distro https://pkgs.alpinelinux.org/package/edge/community/armhf/font-noto-meetei-mayek | 9 weights (100–900) variable; **92 glyphs, 2 OT features, 87 chars across Meetei Mayek + Extensions** | https://fonts.google.com/noto/specimen/Noto+Sans+Meetei+Mayek |
| **Eeyek** (SIL, glyphs © 1999–2019 Chingangbam/Tabish, Latin © SIL) | **OFL-1.1** (Reserved Font Name "Eeyek") | https://github.com/silnrsi/font-eeyek · Debian https://packages.debian.org/sid/fonts/fonts-eeyek | Independent second design — the diversity donor Noto lacks | https://github.com/silnrsi/font-eeyek |
| Eeyek Unicode (legacy Windows font, tabish) | GPL-2.0+ per SUSE packaging — **copyleft; keep out of training container unless counsel clears** | http://tabish.freeshell.org/eeyek/ via https://packagehub.suse.com/packages/eeyek-fonts | legacy only | https://packagehub.suse.com/packages/eeyek-fonts |

Mayek font position is strictly better than Ol Chiki: **two independent OFL designs** (Noto + Eeyek) → font-disjoint train/val splits are possible (train Noto, hold Eeyek for the synthetic val — §B4).

### A7. Manipuri — text corpora (script-split matters more than volume)

| Corpus | Mayek-script volume | License/access | Source |
|---|---|---|---|
| **Hueiyen Lanpao Mayek edition** (hueiyenlanpao.com, daily since 1978; only market Mayek daily) | large, modern prose (unquantified — count post-approval) | © paper (sample strings only) | https://en.wikipedia.org/wiki/Hueiyen_Lanpao · https://www.hueiyenlanpao.com/ |
| mni Wikipedia edition | exists; **article count NOT verified in this pass — TODO-verify, do not quote a number** | CC BY-SA dump | https://en.wikipedia.org/wiki/Meitei_language (edition link) |
| EM Corpus (Huidrom 2021, Waseda): first mni–eng comparable corpus | **Bengali script**, not Mayek — usable for *language* sampling after transliteration, NOT direct Mayek rendering | paper terms | https://en.wikipedia.org/wiki/Meitei_language |
| Assam govt ₹6 cr Meitei corpus program + ₹5 lakh/yr Parishad grant | existence confirmed; contents/script/access unverified — ask, don't assume | govt | https://en.wikipedia.org/wiki/Meitei_language |
| FLORES-200 / IN22 Manipuri slices | script tag unverified in this pass (historically Bengali-script `mni_Beng`) — verify before sampling | CC BY-SA | https://github.com/facebookresearch/flores/blob/main/flores200/README.md?plain=1 |
| CLDR `mni_Mtei` locale (letters ꯀ–ꯪ + Lum/Apun, mtei digits ABF0–ABF9 as default numbering) | seed word/number lists only | Unicode terms | https://unicode.org/cldr/charts/45/summary/mni_Mtei.html |

Context that sets sampling strategy: Manipur mandated Bengali→Mayek phase-out (Official Language Act amendment; newspapers ordered off Bengali script Jan-2023; The Hindu 2022-12-03 — https://www.thehindu.com/news/national/newspapers-the-last-holdouts-of-bengali-script-in-manipur-given-ultimatum-to-switch-to-meetei-mayek-next-month/article66214312.ece). Consequence: Mayek digital volume is **growing but young**; Bengali-script Manipuri is abundant but renders the wrong script. Same regex-gate discipline as Santali (§B1), with the Mayek range.

### A8. Corpus census table (render-usable strings, conservative lower bounds)

| # | Source | Lang/script | Usable volume (lower bound) | How counted | URL |
|---|---|---|---|---|---|
| 1 | sat Wikipedia dump | sat / Olck | ~15.9k articles (many stubs; chars TBD by dump count) | article count | https://en.wikipedia.org/wiki/Santali_Wikipedia |
| 2 | FLORES-200 sat_Olck | sat / Olck | 3,001 sentences ≈ 60k+ words | spec avg 21 w/sent | https://github.com/facebookresearch/flores/blob/main/flores200/README.md?plain=1 |
| 3 | santali-nlp + Crúbadán sat + OLAC | sat / mixed | word-list scale (10⁴–10⁵ tokens est.) | repo/crawl claims | https://github.com/sami42200/santali-nlp · http://www.language-archives.org/language/sat |
| 4 | Hueiyen Lanpao Mayek ed. | mni / Mtei | large daily (count post-approval) | circulation 21–23k copies/day implies volume, not chars | https://en.wikipedia.org/wiki/Hueiyen_Lanpao |
| 5 | EM Corpus + Assam corpus | mni / Beng (transliterate) | paper/govt scale | publications | https://en.wikipedia.org/wiki/Meitei_language |
| 6 | CLDR mni_Mtei exemplar set | mni / Mtei | seed-scale (letters+digits+punct) | chart | https://unicode.org/cldr/charts/45/summary/mni_Mtei.html |
| 7 | Extensions/puya texts | mni / Mtei-historic | tiny; EXCLUDE from modern training (render a small robustness slice only) | proposal attestations | https://unicode.org/L2/L2008/08239r-n3478r-meetei-mayek-ext.pdf |

**Quantified floor for synthetic training (both scripts, no approval needed): FLORES slices (3k sent sat + mni slice TBD) + 15.9k sat.wiki articles + Mayek news sampling.** At word/line granularity with the §B2 sampler this is 10⁵–10⁶ renderable lines per script before augmentation multipliers — enough for SFT bootstrap (precedent §C trains on 10⁵–10⁶ synthetic). Exact char counts = first runnable step post-approval (`wc` over NFC-filtered dumps; script-ratio gate §B1).

---

## PART B — synthetic pipeline spec for W6 (implementable as written)

### B0. Non-goals / guards (from standing law, restated so the spec can't drift)

1. Synthetic is **S6: gold by construction, never eval** (`SOUTH_CANON.md` §E). No synthetic line enters any probe/eval split. Violating this = P0.
2. Machine GT never trains a product model; RLVR rewards on **human-verified gold only**; PDF-layer GT is SFT-only where verification passes (`AGENT_PROTOCOL.md` §9 per memory feed §10).
3. No downloads until human approves each source (2026-09-26 hard rule).

### B1. Stage 1 — text sampling

1. Pull UTF-8 sources from §A8 (post-approval). Normalize **NFC** (Python `unicodedata.normalize`; Mayek vowel-sign order is normalization-sensitive).
2. Script gate (discard-or-route, never silently keep):
   - Ol Chiki line kept iff ≥80% of cased chars ∈ U+1C50–1C7F: `[\u1C50-\u1C7F]`. Bengali-script Santali routed to a *separate* Bengali-renderer queue (reuses existing bn pipeline), never the Ol-Chiki renderer.
   - Mayek line kept iff ≥80% ∈ U+ABC0–ABFF (modern); U+AAE0–AAFF lines quarantined to the historic slice (≤2% of volume).
   - Strip control chars (`Cc/Cf` except ZWJ/ZWNJ where the font uses them); this mirrors the hardened `MAX_CTRL_CHARS=3` probe gate.
3. Coverage-forced sampler: uniform draw **plus** a rare-char booster — every one of the 48 Ol-Chiki codepoints and every Mayek letter/sign/digit appears ≥N times (N=500 word-renders; digits/punct get their own booster since wiki text starves them). Log a per-char histogram; the run FAILS if any assigned codepoint < N (same spirit as the probe's script-validation gate for Bodo mojibake).
4. Granularity ladder (matches challenger curriculum word → line → block, `W1_RECIPE_REFRESH.md`): 50% words (1–3 tokens), 35% lines (5–15 tokens), 15% blocks (3–6 lines, Hueiyen-style column width). Blocks keep reading order = render order (GT alignment §B4).
5. Seeds: `seed=20260926` stream-split (train/val by article-id hash, font-disjoint val for Mayek per §B4). Deterministic resample.

### B2. Stage 2 — font rendering + HarfBuzz flag

| Script | Engine | Flag | Why (cited) |
|---|---|---|---|
| Ol Chiki | Pillow `ImageFont.truetype` **BASIC acceptable; RAQM preferred** | `layout_engine=ImageFont.Layout.RAQM` when `PIL.features.check("raqm")` else BASIC with a logged warning | Alphabet, no reordering (r12a notes §A1); BASIC is glyph-correct. RAQM uniformity keeps one code path for both scripts. Pillow RAQM = libraqm = FriBiDi+HarfBuzz shaping: https://pillow.readthedocs.io/en/stable/reference/ImageFont.html · https://github.com/HOST-Oman/libraqm |
| Meitei Mayek | Pillow **RAQM/HarfBuzz MANDATORY**; assert `features.check("raqm")` or abort run | same call + `language="mni"` BCP-47 tag so HarfBuzz picks Mayek shaping (`hb_shape` script-specific models: https://harfbuzz.github.io/harfbuzz-hb-shape.html) | Abugida vowel signs ABE3–ABEA + Apun Iyek ABED misplace under BASIC. Pillow docs: "Raqm layout is recommended for all non-English text" (https://pillow.readthedocs.io/en/stable/reference/ImageFont.html) |

Render params: canvas 200 dpi to match our South-400 domain (memory feed §2: 200-dpi old-scan renders); sizes 18–36 px body with 10% headline 40–64 px; fg `#000–#333`, bg `#FFF–#F5F0E1` (aged paper tint range); line-height 1.4–1.8× (Mayek vowel signs need headroom — clip check in §B4); fonts: Ol Chiki = Noto Sans Ol Chiki 4 weights (only donor); Mayek = Noto (train) / **Eeyek held for synth-val** (font-disjoint generalization test).
Preferred generator chassis: **TRDG** (`GeneratorFromStrings`, MIT — https://github.com/Belval/TextRecognitionDataGenerator · https://pypi.org/project/trdg) for word/line volume + a Pillow-direct block renderer for multi-line pages (TRDG is line-oriented). Alternative chassis: SynthTIGER (MIT — https://github.com/clovaai/synthtiger) if mid-ground/noise-text blending is wanted; SynthOCR-Gen (2026, low-resource-targeted — https://arxiv.org/pdf/2601.16113) as the 2026-default template. Decision at freeze; all three are MIT/open.

### B3. Stage 3 — degradation stack (parameterized, DocCreator-style + PaddleOCR recipes)

Order (fixed): geometry → ink/paper → optical → compression. Each op has a skip probability so ~15% of lines stay clean (anchors the CER floor).

| # | Effect | Params | Cites |
|---|---|---|---|
| 1 | Perspective / skew / rotate / stretch / trapezoidate | TRDG `-k 5 -rk` (skew ≤5°), `-d/-do` distortion; SynthTIGER stretch+trapezoidate+skew+rotate w/ random margins; shear ≤0.2 (SynthOCR-Gen §3.8) | https://github.com/Belval/TextRecognitionDataGenerator · https://arxiv.org/abs/2107.09313 · https://arxiv.org/pdf/2601.16113 |
| 2 | Adaptive/optical blur | Gaussian σ ∼ U(0.5, 2.0); motion-blur kernel k∈{3,5,7} angle ∼U(0,2π); TRDG `-bl/-rbl` radius {0,1,2,4} | DocCreator adaptive-blur (dichotomic kernel vs real blur exemplar — https://www.mdpi.com/2313-433X/3/4/62 · https://doc-creator.labri.fr/); Genalog `blur radius 3–7` (https://microsoft.github.io/genalog/doc_degradation.html) |
| 3 | Bleed-through | DocCreator physical-model iterations 1–3 w/ random verso line image; Augraphy `BleedThrough(intensity 0.1–0.3, ksize 17, sigmaX 0–1, alpha 0.2–0.3, offsets 10–20)`; Genalog `bleed_through alpha 0.8–0.9` | https://www.mdpi.com/2313-433X/3/4/62 · https://augraphy-doc.readthedocs.io/en/latest/doc/source/augmentations/bleedthrough.html · https://microsoft.github.io/genalog/doc_degradation.html |
| 4 | Ink aging / print defects | DocCreator ink model: splotches + white specks + streaks at char-boundary neighborhoods; Genalog morphology open/erode (overflow) kernel (9,9)-plus, close/dilate (9,1); salt/pepper amount 0.005–0.15; TRDG `-b {0,1,2}` backgrounds (gauss-noise/white/quasicrystal) | https://www.mdpi.com/2313-433X/3/4/62 · https://microsoft.github.io/genalog/doc_degradation.html · https://github.com/Belval/TextRecognitionDataGenerator |
| 5 | JPEG + resize | quality ∼ {30, 50, 70, 90} (10% each) + 60% quality 95; downscale to 150 dpi then back to 200 (1 pass, mimics our thin-scan pipeline) | SynthTIGER post-proc (gauss noise/blur/resize/median-blur/JPEG — https://arxiv.org/abs/2107.09313); PaddleOCR doc-recipe (font/size/grayscale/blur/perspective/stretch — https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/datasets/datasets.en.md) |
| 6 | Paper deformation (blocks only) | gentle cylindrical warp ≤2% height (DocCreator paper-deformation family); skip for word/line crops | https://doc-creator.labri.fr/ · https://github.com/DocCreator/DocCreator (LGPL-3.0 — use as parameter reference + optional degrader binary, keep out of training import chain if license review pending) |

PaddleOCR recipe anchor (why this stack is sufficient): Paddle's own 3.64M-image Chinese doc-recognition synth uses exactly corpus × {font, size, grayscale, blur, perspective, stretching} (https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/datasets/datasets.en.md) — our stack is that recipe **plus** bleed-through + ink-aging + JPEG, i.e. the old-scan defects our South-400 hardness analysis says dominate (ULTIMATE_HYBRID_CONCERN §8: our EASY = their worst OldScan category).

### B4. Stage 4 — GT alignment guarantees (the part that makes synthetic "gold by construction")

1. **Render-then-degrade, never re-label**: GT string frozen at sampling time (NFC); degradations are pixel-only transforms. The only GT edits allowed are deterministic geometric box transforms (rotation/perspective matrices applied to word boxes, same matrix as the image).
2. Shaping-fidelity check (Mayek): after render, `hb-shape`-equivalent advance-width assertion — rendered ink-pixel count > 0 per expected sign cluster; zero-ink clusters (tofu) → fail the batch, never ship silent tofu as "clean GT".
3. Clip check: ascender/descender overflow (Mayek vowel signs at 1.4× line-height) — bounding-box vs canvas intersection = 100% or the sample is re-rendered, not patched.
4. Legibility floor (SynthTIGER rule): foreground/background contrast ratio threshold; below-threshold renders discarded, not kept as "hard negatives" (https://arxiv.org/abs/2107.09313).
5. Font-disjoint synth-val (Mayek): val split rendered **only in Eeyek**; train only in Noto. Ol Chiki (single design): val = held weight (700) + held degradation seed. A model that memorizes Noto-Regular artifacts cannot pass val.
6. Provenance sidecar per image: `{source_id, script_ratio, font, weight, size_px, dpi, degradations+params, seed}` — the same auditability our probe manifest carries (`manifest.json` + `image_meta.json` pattern).
7. Volume target: ≥100k word/line renders per script (matches the 100k-scale multilingual synth precedent §C; Nayana runs 45.7k pages/lang and 850k/10-lang OCR SFT).

---

## PART C — precedent: synthetic-only → usable OCR (2023–2026)

### C1. Direct precedent table (synthetic-only or synthetic-first training, real-data eval)

| # | Case | Synthetic → real setup | Result (real eval) | Gap survivable? | Source |
|---|---|---|---|---|---|
| 1 | **Nayana-OCR (2025)**: GOT-OCR + LoRA, **purely synthetic** 850k images / 10 Indic langs | synth SFT, real bench eval (160 multilingual samples) | **CER 0.227** vs Tesseract 0.206 (near-parity), BLEU 0.395 vs 0.318 (beats), ANLS 0.796 ≈ 0.797 | **Yes for printed docs** — synthetic-only reaches classical-OCR parity + semantic win | https://aclanthology.org/2025.lm4uc-1.11 · https://aclanthology.org/2025.lm4uc-1.11.pdf · ICCVw-2025 3M-image extension https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/papers/Kolavi_Nayana_A_Foundation_for_Document-Centric_Vision-Language_Models_via_Multi-Task_Multimodal_ICCVW_2025_paper.pdf · data https://nayana.cognitivelab.in/ |
| 2 | **EkStep/Tarento Indic synth bench (2022)**: 90k synth images, 23 Indic langs (incl. Santali-OlChiki charset) | synth as train/bench fuel | Established synth as the default OCR bootstrap for Indic coverage | Yes as bootstrap | https://arxiv.org/abs/2205.02543 |
| 3 | **LV-ROVER-MLT Maltese (2026)**: zero public paragraph corpus → synthetic lines → Tesseract-5 LSTM fine-tune + 5-stream arbitration | synth-only fine-tune, real eval | Usable paragraph OCR where none existed (low-resource template case closest to ours) | Yes — the exact zero-labeled-script playbook | http://arxiv.org/abs/2607.00250 |
| 4 | Guan & Greene post-OCR correction (ACL Findings 2024; EMNLP 2024): glyph-similarity synth, **no manual annotation** | synth-trained ByT5 on real OCR outputs, low-resource langs incl. | CER reductions incl. **68.67%** (SCN-TTA ByT5); synth beats uniform-corruption baselines esp. low-resource | Yes (correction stage) | https://aclanthology.org/2024.findings-acl.361 · https://aclanthology.org/2024.emnlp-main.862 |
| 5 | Bourne 2024 (CLOCR-C): LM + char-Markov synthetic corruption | synth-ft vs real-ft | **−55% CER / −32% WER over base; synth beats real-trained**; under-corrupt > over-corrupt | Yes, with the under-corruption caution | https://arxiv.org/abs/2409.19735 |
| 6 | SynthTIGER (ICDAR 2021): synth beats MJ+ST combo on STR benchmarks | synth-only STR training | SOTA-synth at the time; recipe still the field default | Yes | https://arxiv.org/abs/2107.09313 · https://github.com/clovaai/synthtiger |

### C2. Counter-evidence (do not overclaim)

- **Devanagari VLM stress-test (2026-06-28)**: synthetic chrF++ 91–98 hides all differences; **9/10 systems collapse on real Hindi scans**. Synthetic-benchmark scores do not predict real-scan rank. Our synth-val (§B4.5) is a gate, never a claim. (https://arxiv.org/abs/2606.29213 — id per `W1_RECIPE_REFRESH.md`; re-verify at freeze.)
- **ScriptMoE (2026-09-21)**: Ol Chiki / Meitei Mayek are **outside its 10 scripts** — no free MoE ride for our two cells; the specialist must be data (this spec), not that decoder. (arXiv:2609.24058 per W1.)
- Nayana's 10 langs are all high-resource scripts (bn/gu/hi/kn/ml/mr/or/pa/ta/te) — transfer to Ol Chiki (alphabet, isolated) and Mayek (abugida, thin data) is analogy, not measurement. The Maltese case (#3) is the closer structural analogue (zero corpus → synth → usable).
- FaithC4 (2026-09-02): general VLMs rewrite imperfect text (WER +6.9); OCR-specialized VLMs stay faithful. Our synth SFT target must be the OCR-specialized arm (Bodhan/Qwen/PaddleOCR-VL family per W1), not a chat VLM. (arXiv:2607.21617 per W1.)

### C3. Precedent verdict

**Survivable for printed Ol Chiki + Mayek SFT bootstrap; not sufficient as a product claim without real anchors.** The 2023–2026 record says: synthetic-only reaches classical-OCR parity on printed Indic docs (Nayana CER 0.227 ≈ Tesseract 0.206), rescues zero-corpus scripts to usability (Maltese), and beats real-data training for the correction stage — provided degradation matches the target domain and corruption is under- rather than over-applied. It also says synthetic scores don't transfer to real old-scans (Devanagari collapse). For W6 that means exactly the standing plan: **synthetic SFT base (this spec) → human-gold fine-tune/RLVR on verified real lines only** (memory-feed §10 guards), with the falsification test (official-pair GT vs PDF-layer GT) deciding whether any PDF-derived line may join SFT. Santali expectation should be set below Mayek: single-font renders + multi-script competition (Bodhan already leads sat at 68.30 — the router/specialist question in W4, not more synth volume, may be the binding constraint).

---

## Deliverables checklist

- [x] Corpus census table (§A8) with URLs and quantified floor
- [x] Implementable W6 spec: sampling (§B1) → rendering + HarfBuzz flags (§B2) → degradation params (§B3) → GT guarantees (§B4)
- [x] Precedent verdict (§C3): survivable as SFT bootstrap, gated by real-gold fine-tune
- [ ] Post-approval first runnable: dump char counts (FLORES + sat.wiki + Mayek news), per-char histogram gate, RAQM assert smoke-test on ABE3–ABEA strings

*No root files added. No `level2/research/` writes. South scores untouched.*
