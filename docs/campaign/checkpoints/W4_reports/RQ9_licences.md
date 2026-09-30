# RQ-9 — LICENCES STILL OPEN (VERDICT + research lane)

**Agent:** research subagent · **Date all sources opened:** 2026-09-30
**Protocol:** `docs/campaign/protocols/proto-83-licence-verification.md` (U7, U14)
**Harvested first:** `docs/legal/LICENSE_AUDIT.md` read in full (83 lines). Its rows are NOT redone here; this
report only closes what it left open, and §3 below lists where this pass **contradicts** it.
**Constraints honoured:** no download, no training, no Sarvam call, no writes outside this file.
`sat.traineddata` / `mni.traineddata` were **not downloaded** — sizes come from the GitHub contents API.

Evidence tags: **PRIMARY** = file:line on this disk · **MEASURED** = API/metadata returned by a source I opened
· **DERIVED** = inference from a quoted clause · **UNKNOWN** = not found; honest-empty.

---

## Licence table

| Artefact | Version | Licence | The exact clause that matters | Verdict | Source |
|---|---|---|---|---|---|
| `indic-ocr/tessdata` traineddata (**sat**, **mni**, + 9 more) | repo `master`, last push 2018-09-12 | **Apache-2.0** (stock, unmodified) | §2: *"each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work"* | **CLEARED** | `indic-ocr/tessdata` `LICENSE` (11,357 B, SHA `8dada3e`) + API `license.spdx_id = "Apache-2.0"` |
| surya **code** | 0.22.1 | **Apache-2.0** | Shipped `licenses/LICENSE` = verbatim Apache-2.0 (9,135 B, ends `END OF TERMS AND CONDITIONS`) | **CLEARED** | `.venv311/…/surya_ocr-0.22.1.dist-info/licenses/LICENSE:1-3`; `METADATA:7` `License: Apache-2.0` |
| surya **weights** | README-described v0.1 (March 2, 2023, Modified) | **AI Pubs OpenRAIL-M License (MODIFIED)** | Attachment A §2(c): *"for any purpose if You … provides or otherwise makes available any product or service that competes with any product or service offered by or made available by Licensor or any of its affiliates"* — **no funding/revenue threshold** | **NOT CLEARED** for a commercial OCR product; **CONDITIONAL** under $5M for research/eval | `datalab-to/surya` `MODEL_LICENSE` (SHA `5563e27`) |
| surya weights — $ cap | " | " | Attachment A §2(b): *"for any purpose if You … has raised more than five million US dollars ($5,000,000) in total equity or debt funding from any source, except where Your Use is limited to personal use or research purposes"* | **CLEARED** if funding < $5M | same |
| surya weights — output reuse | " | " | §8 Share-a-Like: *"You agree to apply this License (to the exclusion of all others) to any and all copies of the Model, Derivatives of the Model, any changes or improvements to the Model or Derivatives of the Model, **and to the Output and any derivatives, changes or improvements to or of the Output**."* | **NOT CLEARED** for training-on-surya-outputs | same |
| SynthOCR-Gen **tool** (HF Space `Omarrran/OCR_DATASET_MAKER`) | n/a | **UNKNOWN** | — could not be opened (HTTP 401); no GitHub repo exists under the name | **UNKNOWN** | fetch returned `http_status_code: 401`; `github_search_repositories q="synthocr"` → 0 relevant hits |
| 600k Kashmiri OCR dataset (SynthOCR-Gen output) | 2025-12-26 generated, 602k words, 11.1 GB | **CONTRADICTION**: HF tag `cc` / card says `[ CC-BY-4.0]`, but the card's own policy is a **"Controlled Research Access License"** | §4 Prohibited #2: *"Use datasets for commercial products, services, APIs, or SaaS"*; §5: *"May not be commercialized without a separate agreement"* | **NOT CLEARED** (commercial) / **CONDITIONAL** (non-commercial research) | `huggingface.co/datasets/Omarrran/600k_KS_OCR_Word_Segmented_Dataset` card, "Dataset & License Policy (v1.0)" |
| IndicPhotoOCR **script-ID** weights (a.k.a. "CLIP script identifier") | config `transformers_version: 4.48.1` | **MIT** (code+weights release) | *"Copyright (c) 2024 Bhashini Team@IIT Jodhpur"* + full MIT permission grant | **CONDITIONAL** — see detail §4.3 (not a CLIP model; base checkpoint licence not independently verified) | `anikde/STscriptdetect` `LICENSE` (SHA `e36a898`) |
| EasyOCR detector — CRAFT **code** | repo current | **MIT** | *"Copyright (c) 2019-present NAVER Corp."* + full MIT grant | **CLEARED for code** — **refutes** audit's "non-commercial research" claim | `clovaai/CRAFT-pytorch` `LICENSE` (SHA `e101a6c`) |
| EasyOCR detector **weight on our disk** (`craft_mlt_25k.pth`, 83,152,330 B) | fetched pre-v1.1.6 | **UNKNOWN** | local provenance: `'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip'` — a **JaidedAI release asset**, not a CRAFT-pytorch file | **UNKNOWN** | `.venv311/…/easyocr/config.py:13-14`; `~/.EasyOCR/model/craft_mlt_25k.pth` |
| tesseract_indic / tesseract_bilingual / openbharatocr | 5.5.2 / 0.4.3 | Apache-2.0 (pkg) | carried from audit lines 12-15; **tessdata upstream still TODO-VERIFY** | **CONDITIONAL** (pkg CLEARED, weights unverified) | `LICENSE_AUDIT.md:12-15` |
| anuvaad_tesseract traineddata | n/a | **UNKNOWN** | no local licence file; audit TODO-VERIFY #2 not closed in this pass | **UNKNOWN** | `LICENSE_AUDIT.md:14,43-45` |
| rapidocr / paddleocr_indic / doctr | 3.9.2 / 3.7.0 / 1.1.0 | Apache-2.0 (pkg) | carried from audit lines 17-20; weight chains still TODO-VERIFY #4,5,7 | **CONDITIONAL** | `LICENSE_AUDIT.md:17-20` |
| Bodhan IndicOCR (`bodhan-ai/indic-ocr`) | Indic Open Model License **v1.0**, updated 2026-09-05 | **Indic Open Model License v1.0** (custom; HF tag `other`; **gated**) | §2.1 Attribution Notice; §3.1 hosting needs prior written approval; §14 500M MAU / $250M revenue | **CONDITIONAL** | `Bodhan-AI/bodhan-model-info` → `licenses/indic-open-model-license/v1/Indic_Open_Model_License.md` (SHA `db4cdf9`) |
| AksharDrishti hackathon rules | page live 2026-02-12 launch | **UNKNOWN** | no open-source / licence / attribution rule appears on the landing page | **UNKNOWN** | `bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon` |

---

## 1. indic-ocr tessdata for Ol Chiki / Meetei Mayek — **CLEARED** (this unblocks U7 at licence level)

The premise in the task was that the licence was missing. **It is not missing — it was in a sibling repo, not
the site repo.** Two different repos were being conflated:

- `indic-ocr/indic-ocr.github.io` (the *project site*, `pushed_at: 2016-12-12`) contains **only** `README.md`,
  `index.html`, `params.json`, `images/`, `javascripts/`, `stylesheets/`. **No LICENSE file**, and the API
  returns **no `license` field at all** for this repo. So the landing page indeed states no licence — that
  observation was correct but looked in the wrong repo.
- `indic-ocr/tessdata` (the *weights* repo, `homepage: https://indic-ocr.github.io/tessdata/`, 56★, 10 forks,
  `pushed_at: 2018-09-12`) contains **`LICENSE` (11,357 bytes, blob SHA `8dada3edaf50dbc082c9a125058f25def75e625a`)**.

I opened the full `LICENSE`. It is **stock, unmodified Apache License 2.0**: sections 1–9 with the standard
grants, plus the `APPENDIX: How to apply the Apache License to your work` block whose copyright line is the
**unfilled template** `Copyright {yyyy} {name of copyright owner}`. No use restrictions, no non-commercial
carve-out, no RAIL clause, no revenue cap, no `NOTICE` file in the repo root (so Apache §4(d) is not triggered).
GitHub's own detector agrees — the repo API returns `"license":{"key":"apache-2.0","spdx_id":"Apache-2.0"}`.

The operative clauses, verbatim:
> §2: "each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free,
> irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform,
> sublicense, and distribute the Work and such Derivative Works in Source or Object form."

> §4(a): "You must give any other recipients of the Work or Derivative Works a copy of this License"

**Downloadability and size (MEASURED, not downloaded by me):** both target files exist and are retrievable
from the repo's raw tree — `sat/sat.traineddata` = **1,546,915 bytes** (~1.48 MB);
`mni/mni.traineddata` = **2,843,488 bytes** (~2.71 MB). Direct paths:
`https://raw.githubusercontent.com/indic-ocr/tessdata/master/sat/sat.traineddata` and `…/mni/mni.traineddata`.

**Residual caveat (DERIVED, must be carried, not waved away):** the repo README states
*"We have used [Noto Fonts](https://www.google.com/get/noto/) to train all the scripts."* Noto is SIL OFL.
I did **not** open the Noto/OFL licence in this pass, and traineddata derived from OFL fonts is a second link
in the chain that the Apache-2.0 `LICENSE` file does not itself speak to. **This is UNRESOLVED** — see below.
Note also the repo is dormant (last push 2018) and the README's own quality claim (*"These models are to be
expected to have more accuracy than the ones provided through tesseract site"*) is the author's, unverified.

**Consequence:** the proto-83 `factchk` line — *"Unless a licence is found (repo LICENSE file, model headers, or
the authors), treat it as all-rights-reserved: benchmark use only … do not ship it"* — is **no longer
applicable**. The licence was found, and it permits exactly what proto-83's gate wanted to know. U7 is
unblocked at the licence level, subject to the Noto check. `DEEPER_LIVE_RESEARCH_2026-09-29.md:142`'s existing
"Apache-2.0" claim for this repo is **confirmed**, not merely repeated.

---

## 2. Surya — the contradiction is **not** a contradiction; it is two scopes

### 2.1 What is actually on disk (PRIMARY)

`.venv311/lib/python3.11/site-packages/surya_ocr-0.22.1.dist-info/METADATA`
- line 7: `License: Apache-2.0`
- line 8: `License-File: LICENSE`
- line 99 (verbatim): `The Surya code is licensed under Apache 2.0. The model weights use a modified AI Pubs Open Rail-M license (free for research, personal use, and startups under $5M funding/revenue). For broader commercial licensing of the model weights, visit our pricing page [here](https://www.datalab.to/pricing?utm_source=gh-surya).`

`.venv311/…/surya_ocr-0.22.1.dist-info/licenses/LICENSE` — 9,135 bytes, opens `Apache License / Version 2.0,
January 2004`, ends `END OF TERMS AND CONDITIONS`. Pure Apache-2.0. **No RAIL text, no $5M clause in the shipped
file.** That is what the audit's line 21 cited as "`Apache-2.0` … + licenses/LICENSE".

**So: which governs?** Both, for different objects. `License: Apache-2.0` at `METADATA:7` is the SPDX field for
the *packaged artefact*, and the wheel contains **no weights at all** (the RECORD has 0 entries matching
`.safetensors|.pth|.pt`; weights are fetched at runtime — `surya/settings.py:19` `S3_BASE_URL =
"https://models.datalab.to"`, `:40` `SURYA_MODEL_CHECKPOINT: str = "datalab-to/surya-ocr-2"`). A licence
field can only describe what is distributed in the package. The weights are a **separate download** governed by
a separate document. **The audit's framing of this as a self-contradicting package is imprecise** — the code is
Apache-2.0 and the weights are RAIL-M; nothing conflicts. `~/.cache/datalab/` on this machine holds only
`llamacpp_server.{log,json,lock}` — no weights and **no licence file** — consistent with that split.

The RAIL-M **text is not shipped locally** — that half of the audit's TODO-VERIFY #8 was right. I obtained it
upstream.

### 2.2 The full weights licence (opened 2026-09-30)

`datalab-to/surya` root contains both `LICENSE` and a separate **`MODEL_LICENSE`**. The `MODEL_LICENSE`
(blob SHA `5563e2711dd7afba057e1239cd562a31b8979322`) is titled:

> `AI PUBS OPEN RAIL-M LICENSE (MODIFIED)` / `Version 0.1, March 2, 2023 (Modified)` / `http://licenses.ai/`

Its preamble states: *"The "RAIL" nomenclature indicates that there are use restrictions prohibiting the use of
the Model. … This License specifies that the use restrictions in the original License must apply to such
derivatives."*

**Attachment A — USE RESTRICTIONS** (verbatim, the operative part):
> 2. Commercial:
> (a) for any purpose if You (your employer, or the entity you are affiliated with) generated more than five
> million US Dollars ($5,000,000) in gross revenue in the prior year, except where Your Use is limited to
> personal use or research purposes;
> (b) for any purpose if You (your employer, or the entity you are affiliated with) has raised more than five
> million US dollars ($5,000,000) in total equity or debt funding from any source, except where Your Use is
> limited to personal use or research purposes; or
> (c) **for any purpose if You … provides or otherwise makes available any product or service that competes
> with any product or service offered by or made available by Licensor or any of its affiliates.**

**§7 Attribution:**
> "In connection with any Output, or use of Distribution of any Model or Derivatives of the Model, You agree to
> give appropriate credit and attribution to Licensor, provide a link to the original Model or Derivatives of the
> Model, provide a copy of this License, and identify any changes You have made to the Model or Derivatives of
> the Model (collectively, the "Attribution"). The Attribution must not suggest endorsement by any Licensor."

**§4(a) propagation:** "Use-based restrictions in paragraph 5 MUST be included as an enforceable provision by
You in any type of legal agreement … governing the use and/or distribution of the Model or Derivatives of the
Model, and You shall give notice to subsequent users You Distribute to, that the Model and Derivatives of the
Model are subject to paragraph 5."

**§6 vs §8 — the outputs question, now answered (the audit called it "unverified"):**
> §6: "Except as set forth herein, Licensor claims no rights in the Output you generate using the Model. You are
> solely responsible for the Output you generate and its subsequent uses. **No use of the Output can
> contravene any provision as stated in the License.**"
> §8: "You agree to apply this License (to the exclusion of all others) to any and all copies of the Model …
> **and to the Output and any derivatives, changes or improvements to or of the Output.**"

### 2.3 The operational answer, stated plainly

**For a company with funding under $5M: yes, surya weights may be used commercially — but not for this
company's actual product, and not as training labels.** Three reasons, in order of severity:

1. **§2(c) is the blocker, and it has no threshold.** The audit only ever flagged the $5M cap. But §2(c)
   prohibits *"any purpose"* where you *"provide … any product or service that competes with any product or
   service offered by … Licensor."* Datalab sells Surya as its OCR product. Shipping a commercial Indic OCR
   service is competing with it. There is no funding exemption and no research exemption attached to §2(c) — the
   *"except where Your Use is limited to personal use or research purposes"* carve-out appears only in §2(a) and
   §2(b). So under-$5M clears (a) and (b) and still trips (c). **This was not in the audit at all.**
2. **§8 share-alike reaches the Output, so training on surya outputs is not clean.** §8 requires the modified
   RAIL-M to be applied to *"the Output and any derivatives, changes or improvements to or of the Output."* A
   model fine-tuned on surya transcriptions is, on its face, a derivative of that Output, and would inherit the
   $5M cap **and** the §2(c) restriction. The audit's line 33-35 posed this as an open question ("whether surya
   OUTPUTS used as training labels count as a derivative is unverified"); the licence text answers it in the
   affirmative. (DERIVED — this is my reading of §8 applied to our use, not a statement by Datalab.)
3. **If we do use it anyway**, §4(a) forces us to ship the use-restrictions as an enforceable clause in our own
   terms, and §7 forces attribution + link + licence copy + change notice.

**U14, as this evidence bears on it:** "ship surya in the submission/product under the $5M cap" is **not** a
live option for a commercial product, because §2(c) is independent of the cap. A permissive fallback route per
language (proto-82/80 tables) remains the only clean path, and a **Datalab commercial licence is a real option
worth pricing** — the RAIL-M itself says *"Commercial and broader use licenses may be available from Licensor at
the following URL: https://www.datalab.to/"*. **Boss decision, not mine.** Note the counter-evidence too: for
*research/benchmark-only* use under $5M, the licence is plainly permissive, and our probe22 evaluation use sits
there.

---

## 3. Corrections to `docs/legal/LICENSE_AUDIT.md` (this pass contradicts it in 3 places)

| Audit line | Audit says | This pass found |
|---|---|---|
| 21 | surya "package **contradicts itself**" / `RISK-noncommercial-or-copyleft` | Not a contradiction — two scopes. Code Apache-2.0, weights RAIL-M. Risk is real but the mechanism is different and worse (§2(c), not the $ cap). |
| 27, 31 | surya is the one "likely blocked / conditional" item, on the $5M cap | Still not clean, but the cap is survivable at <$5M. **The real blocker is §2(c) competing-product, which the audit missed entirely.** |
| 36-37, 46-47 | CRAFT detector "historically was released for non-commercial research only" (TODO-VERIFY #3: "license section: non-commercial research clause") | **REFUTED for the code.** `clovaai/CRAFT-pytorch` LICENSE is **MIT, "Copyright (c) 2019-present NAVER Corp."** There is no non-commercial clause in the repo. *But* the `.pth` on our disk is fetched from a JaidedAI release asset, so the **weight's** terms are still genuinely open — see §4.2. |

---

## 4. Fallback engines under the real submission format

Per instruction, local audit first; web only for gaps. All ten named engines confirmed present on disk
(`level2/out/<engine>/` and `level2/unified/probe22/<engine>/` all exist).

### 4.1 Carried unchanged from the local audit (not redone)
- `tesseract_indic` 5.5.2, `tesseract_bilingual`, `openbharatocr` 0.4.3 — Apache-2.0 packages; tessdata
  upstream still unverified (`LICENSE_AUDIT.md:12-15`, TODO #1).
- `rapidocr` 3.9.2, `paddleocr_indic` (paddleocr 3.7.0), `doctr` 1.1.0 — Apache-2.0 packages; PP-OCR /
  RapidOCR-ONNX / doctr weight chains unverified (`:17-20`, TODO #4, #5, #7).
- `anuvaad_tesseract` — traineddata with no licence file anywhere local; **UNKNOWN** (`:14`, TODO #2). I did
  not close this one; it remains open.
- `indicphotoocr` — package MIT (`/Users/srujansai/Desktop/South/.deps/IndicPhotoOCR/LICENSE`);
  `BharatSceneTextDataset/LICENSE` Apache-2.0. Recognition/detection weight repos (STocr, SceneTextDetection)
  still unverified (`:19`, TODO #6).

### 4.2 EasyOCR detector weight — the one I could narrow, not close
`craft_mlt_25k.pth` (83,152,330 B, `~/.EasyOCR/model/`, dated 11 Sep) is downloaded per
`.venv311/lib/python3.11/site-packages/easyocr/config.py:13-14`:
> `'filename': 'craft_mlt_25k.pth',` / `'url': 'https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip',`

So the binary on our disk is a **JaidedAI/EasyOCR release asset**, *not* a file from `clovaai/CRAFT-pytorch`.
CRAFT-pytorch's MIT licence therefore covers CRAFT *code* and does not, by itself, clear the *weight*. EasyOCR's
own package licence is Apache-2.0 per `LICENSE_AUDIT.md:16`; the release-asset terms were not opened.
**Verdict: UNKNOWN for the weight; the audit's non-commercial suspicion is refuted for the code but not
discharged for the binary.** The six Indic recognition `.pth` files (215 MB each, e.g. `devanagari.pth`) ship
with no adjacent licence, as the audit records.

### 4.3 IndicPhotoOCR script-identifier weights — **the on-disk TODO is now resolved to MIT**
`.deps/IndicPhotoOCR/IndicPhotoOCR/script_identification/vit/models/12_classes/` holds `model.safetensors`
(343,254,736 B), `config.json`, `preprocessor_config.json`, `training_args.bin` — and **no licence file**; a
recursive `find` under `script_identification/` for `*licen*|*readme*|*copying*` returns nothing. `proto-93-
measured-facts.md:67` flagged this as "licence TODO".

Two facts now on record:
1. **It is not CLIP.** `config.json` states `"_name_or_path": "google/vit-base-patch16-224-in21k"`,
   `"architectures": ["ViTForImageClassification"]`, `"model_type": "vit"`, 12 classes (hindi, english,
   gujarati, punjabi, assamese, bengali, kannada, malayalam, marathi, odia, tamil, telugu). Calling it "the CLIP
   script identifier" is a misnomer; it is a ViT fine-tune. (The class list also does **not** include Ol Chiki
   or Meetei Mayek — 12 classes, no `sat`, no `mni` — so it cannot route those two languages.)
2. **The release repo is MIT.** `anikde/STscriptdetect` (the weight source named in `LICENSE_AUDIT.md:19,74`)
   ships a `LICENSE` (blob SHA `e36a8980`): `MIT License` / `Copyright (c) 2024 Bhashini Team@IIT Jodhpur` /
   full MIT permission grant. **This closes the `proto-93` TODO for the script-ID weights.**

Residual: the base checkpoint `google/vit-base-patch16-224-in21k` is named in the config but I did **not** open
its model card, so the upstream link in the chain is **UNKNOWN** (§16.2-style problem — see Bodhan, which has the
same structural gap and says so explicitly). Verdict **CONDITIONAL**, not CLEARED.

---

## 5. Hackathon rules on attribution / open-source / permitted licences — **UNKNOWN**

I opened `https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon` (JS-rendered SPA; needed
`full_content` to get past a generic 2-line blurb). **The entire page text contains no statement about
open-source requirements, attribution, code-licence obligations, or permitted model licences.** The only
adjacent words are descriptive, in the Bhashini mission paragraph: *"Bhashini, the National Language Technology
Mission, aims to make digital content accessible in all Indian languages through AI and open-source language
tools. With 1000+ pre-trained models on its platform…"* — that describes Bhashini's own platform, it is not a
rule on entrants.

What the page *does* contain: launch date `12 Feb 2026`; a `Structured Journey` timeline whose every
substantive date is `TBD` (`Last date of registration - submission of ideas | TBD`, `Last date for initial
prototype submission (for Stage 2) | TBD`, `Last date for final prototype submission (for Stage 3) | TBD`); and
tab labels `Timeline | Evaluation Process | Eligibility Criteria | Contact Us`, plus a `View Full Details →`
link and a `Process & Criteria` nav item. **The contents of those tabs / the full-details page did not render
into the fetched HTML**, so the rules most likely to carry an open-source or licensing clause —
`Evaluation Process`, `Eligibility Criteria`, `Process & Criteria` — are exactly the parts I could **not** read.

**Verdict: UNKNOWN.** Not "no rule exists" — I could not read the rule-bearing sections. Per the honesty law I
am not inferring a permission from their absence. The dated claim in `INTEGRATION_REPORT.md:146`
("2026-10-15 Bhashini qualifier deadline") is **not corroborated** by this page, which shows `TBD` for every
qualifier date; that is a separate open contradiction (boss decision U2) and I neither confirmed nor refuted
it here. **Gate 1 cannot be closed on licensing from the public page.** Recommend a human open the
`Process & Criteria` / `Evaluation Process` tabs in a browser and paste the text, or email
the listed contact.

---

## 6. Bodhan IndicOCR — **CONDITIONAL**; attribution is *not* an in-output requirement

Authoritative licence opened: `Bodhan-AI/bodhan-model-info` →
`licenses/indic-open-model-license/v1/Indic_Open_Model_License.md` (blob SHA `db4cdf9bd2a1d09f2c6406958d2c9362561a5256`).
Header: `# INDIC OPEN MODEL LICENSE` / `Version: 1.0` / `Updated: 05 September 2026` /
`Copyright © 2026 IITM BODHAN-AI FOUNDATION.`

**Direct answer to the question asked — does it require attribution text in outputs? No.** The obligation is
placement-scoped to the interface/documentation, not to recognized text:

> **2.1** Whenever the Software or a Derivative is Made Available to a Third Party, You must include the
> following notice (the "Attribution Notice"), or a substantially similar notice pre-approved in writing by
> Licensor:
> > "Built with [Model Name] from Bodhan AI / AI4Bharat."
>
> **2.2** The Attribution Notice must appear in **the user-facing interface of the product or service through
> which the Software or Derivative is Made Available** or, if there is no user interface, in the top-level
> documentation accompanying it. It must be at least as prominent as any credit given to any other third-party
> model, technology, or component.
>
> **2.4** This Section 2 does not apply to Internal Use.
> **2.5** No removal or alteration.

So: a credit line in our README/UI is required; a `"Built with IndicOCR from Bodhan AI / AI4Bharat."` string
**inside the OCR text output** is **not** required by any clause I read. The model's own `Output` is defined
(§0) as *"transcriptions, translations, synthesized audio, or transliterations"* — and §2 governs "the Software
or a Derivative … Made Available", not the Output.

**Four conditions that do bind us, and that change a wrap decision:**
- **§3.1 Third-Party Hosting:** *"you must obtain Licensor's prior written approval, and enter into a separate
  written commercial agreement with Licensor on terms to be agreed, before You Host the Software or a Derivative
  for a Third Party."* A hackathon submission that exposes an API or hosted endpoint to judges is plausibly
  "Hosting". **§3.2** carves out *"providing a product or service in which the Software or Derivative is used
  solely as an internal component, where no Third Party is given direct access to the model's inference or
  fine-tuning interface, its inputs, or its raw Output as such (as distinct from the product's own outputs)"* —
  that carve-out is the shape our submission should take. **§3.5** forbids structuring around it.
- **§4 Open-Release Waiver:** hosting approval is waived *if* within 90 days we publicly release the Derivative
  under the same licence, substantially as capable (§4.2 blocks deliberate degradation).
- **§5:** a Derivative Made Available must carry this exact licence; no relicensing. **§5.2** exempts
  internal-only use.
- **§14:** *"If Your own product or service — other than through Third-Party Hosting under Section 3 — is powered
  by the Software or a Derivative and exceeds 500 million monthly active users or US$250 million in annual
  revenue, You must obtain a separate license."* Irrelevant at our size; the deed version states it
  *"Doesn't apply to nonprofit, government, or academic users."*
- **§0 "Derivative" explicitly includes** a model *"trained substantially on Output of the Software"* — so
  training on Bodhan outputs drags the whole licence (§2, §3, §5) onto our model.

**Also note:** the HF repo is **gated** — *"You need to agree to share your contact information to access this
model … Please provide your details and agree to the LICENSE … to request access."* HF metadata tag is
`License: other`. Contacts for approvals: `support@bodhan.ai` (§15.6). Governing law: laws of India (§12.1).

**Incidental but load-bearing for the campaign (from the competitor's own card, quoted):** its
IndicOCR-PR printed-accuracy table gives **Surya OCR 2 → Manipuri 0.1, Santhali 0.1**, and **Gemini 3.1 Pro →
Manipuri 0.8, Santhali 0.2**. That is third-party corroboration that surya is effectively unusable for `mni`/`sat`
— consistent with our own local finding that Santali has no working local engine, and it means the
indic-ocr tessdata backstop (§1) is the *only* candidate for those two cells. Licence-clean, but quality
untested. (Out of licence scope; recorded because it changes the value of the §1 clearance.)

---

## 7. SynthOCR-Gen — **UNKNOWN for the tool, NOT CLEARED for the dataset**

Searched: `web_search` ("SynthOCR-Gen model licence huggingface", "SynthOCR synthetic OCR dataset github"),
`github_search_repositories q="synthocr"` → 3 hits, **none relevant** (`AnimeshSingh747/Synthocraft-Production`,
`pitabasdev/Synthocraft-Production` = Delmia Apriso water-tank projects; `vickybudhiraja/synthocrdata1` = unrelated
2024 toy). **There is no GitHub repository for SynthOCR-Gen.** A secondary source
(`emergentmind.com/topics/synthocr-gen`) asserts *"Open-source implementations are available for broad reuse
(notably OmniPrint and SynthOCR-Gen on GitHub)"* — **I could not corroborate this and am not relying on it.**

What exists, per the papers themselves (arXiv:2601.16113 §"Deployment and Reproducibility"):
> "The SynthOCR-Gen tool is deployed on HuggingFace Spaces at https://huggingface.co/spaces/Omarrran/OCR_DATASET_MAKER,
> enabling researchers to generate custom datasets for any Unicode-supported language without local installation."

- **The tool: UNKNOWN.** `https://huggingface.co/spaces/Omarrran/OCR_DATASET_MAKER` returned
  `error_type: "http_error", http_status_code: 401` on both attempts (excerpt mode and full-content mode), and
  the HF API endpoint `/api/spaces/Omarrran/OCR_DATASET_MAKER` also returned 401. I could not read its licence
  tag, and there is no repo to fall back on. **The generator's licence is unestablished.**

- **The dataset it produced: NOT CLEARED for commercial use, on an internal contradiction.** The paper
  releases *"a 600,000-sample word-segmented Kashmiri OCR dataset, which we release publicly on
  HuggingFace"*. Artefact: `Omarrran/600k_KS_OCR_Word_Segmented_Dataset` — 602,000 word images, 11.1 GB,
  Kashmiri Perso-Arabic, RTL, generated 2025-12-26, paper arXiv:2601.01088 (distinct from the tool paper
  2601.16113), author of record Haq Nawaz Malik.

  The HF sidebar tag reads `License: cc` and the card prints a bare `[ CC-BY-4.0]` under `## License`. But the
  same card then embeds a completely different instrument, headed:
  > `# Dataset & License Policy (v1.0)` … `## PART A — DATASET LICENSE` … `**(Controlled Research Access License )**`

  whose operative clauses are:
  > **3. Permitted Uses** — Users **may** use the datasets for: "1. Non-commercial research and experimentation
  > 2. Academic publications and benchmarking 3. Training AI models for Kashmiri language research 4. Open
  > scientific collaboration aligned with language preservation 5. Internal evaluation and analysis"
  >
  > **4. Prohibited Uses** — Users **must NOT**: "1. Redistribute, mirror, or re-host datasets … 2. Use datasets
  > for commercial products, services, APIs, or SaaS 3. Train proprietary or closed-source models without
  > permission 4. Attempt dataset reconstruction via model outputs 5. Combine datasets into other datasets for
  > redistribution"
  >
  > **5. Model Training Restrictions** — "May not be commercialized without a separate agreement"; "Weights may
  > be: Open / Gated / Restricted at the discretion of the maintainer."
  >
  > **6. Attribution Requirements** — Required in: "Research papers / Model cards / GitHub repositories /
  > Public demos or reports. **Failure to attribute constitutes a license violation.**"
  >
  > **8. Commercial Licensing** — "Any commercial use requires: Explicit written permission / A separate
  > licensing agreement / Possible royalties or revenue-sharing. **Commercial inquiries must be made before use**."
  >
  > **7. Access Control** — "Dataset access may be: Revoked at any time / Limited by scope or duration / Subject to
  > additional conditions. No guarantee of permanent access is implied."
  >
  > **10. Termination** — "Upon termination, all copies must be deleted."

  The dataset is also **gated** (*"You need to agree to share your contact information to access this
  dataset"*).

  **Verdict: the operative text is a Controlled Research Access License, not CC-BY-4.0.** CC-BY-4.0 would
  permit commercial reuse with attribution; this policy forbids it outright and demands a separate agreement.
  I record the contradiction rather than resolving it in our favour: **NOT CLEARED for any commercial purpose**,
  CONDITIONAL for non-commercial Kashmiri research only, and unusable if we ever commercialise a model trained
  on it. **Relevance:** `ks` is one of our §6.4-BARRED languages, so this was a plausible-looking unblock for
  Kashmiri that would have poisoned the lane. It also shows a licensing failure mode worth watching: the HF
  machine-readable tag can be flatly wrong about the human-readable policy beside it.

---

### Sources relied on

Local (all opened 2026-09-30):
- `/Users/srujansai/Desktop/South/docs/legal/LICENSE_AUDIT.md` (83 lines, full)
- `/Users/srujansai/Desktop/South/docs/campaign/protocols/proto-83-licence-verification.md` (32 lines, full)
- `/Users/srujansai/Desktop/South/docs/campaign/protocols/proto-93-measured-facts.md:67`
- `/Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages/surya_ocr-0.22.1.dist-info/METADATA:7,8,97-99`
- `/Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages/surya_ocr-0.22.1.dist-info/licenses/LICENSE` (head + tail, 9,135 B)
- `/Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages/surya_ocr-0.22.1.dist-info/RECORD` (0 weight entries)
- `/Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages/surya/settings.py:19,21,40,41,108,153,161`
- `/Users/srujansai/Desktop/South/.venv311/lib/python3.11/site-packages/easyocr/config.py:13-14`
- `/Users/srujansai/Desktop/South/.deps/IndicPhotoOCR/IndicPhotoOCR/script_identification/vit/models/12_classes/config.json`
- `/Users/srujansai/Desktop/South/.deps/IndicPhotoOCR/LICENSE`, `.deps/IndicPhotoOCR/BharatSceneTextDataset/LICENSE`
- `~/.EasyOCR/model/craft_mlt_25k.pth` (ls), `~/.cache/datalab/surya/` (ls)
- `find` for LICENSE/COPYING/NOTICE repo-wide; `find` under `script_identification/`

Remote (all opened 2026-09-30):
- `github.com/indic-ocr/indic-ocr.github.io` — root contents + repo metadata (**no license field**)
- `github.com/indic-ocr/tessdata` — `LICENSE` (full text), `README.md`, `sat/`, `mni/`, repo metadata
  (`spdx_id: Apache-2.0`)
- `github.com/datalab-to/surya` — `MODEL_LICENSE` (full text); `README.md` "Commercial usage" via code search
- `github.com/anikde/STscriptdetect` — `LICENSE`
- `github.com/clovaai/CRAFT-pytorch` — `LICENSE`, `test.py`/`craft.py` via code search
- `github.com/Bodhan-AI/bodhan-model-info` — `licenses/indic-open-model-license/v1/Indic_Open_Model_License.md` (full text)
- `huggingface.co/bodhan-ai/indic-ocr` (full model card)
- `huggingface.co/datasets/Omarrran/600k_KS_OCR_Word_Segmented_Dataset` (full dataset card)
- `huggingface.co/spaces/Omarrran/OCR_DATASET_MAKER` — **401, could not open**
- `bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon` (full page)
- `arxiv.org/abs/2601.16113`, `arxiv.org/abs/2601.01088` (via search excerpts + PDF excerpt)
- Search log: `github_search_repositories org:indic-ocr`; `q=synthocr`; `q="synthocr-gen"`; `q="license model weights pretrained repo:clovaai/CRAFT-pytorch"`; `q="Commercial usage repo:datalab-to/surya"`; `parallel-search_web_search` ×3 (Bodhan licence, SynthOCR-Gen licence, hackathon rules)

### UNRESOLVED

1. **Noto Fonts (OFL) as the training-font provenance of the indic-ocr traineddata.** The repo README names
   Noto; the Apache-2.0 `LICENSE` does not address the font. Second link in the chain, unexamined. Affects §1
   clearance. UNKNOWN.
2. **`google/vit-base-patch16-224-in21k` base-checkpoint licence** for the IndicPhotoOCR script-ID fine-tune.
   Named in `config.json`; card not opened. UNKNOWN.
3. **EasyOCR weight terms for the JaidedAI release asset** (`craft_mlt_25k.zip`, pre-v1.1.6) and the six Indic
   recognition `.pth` files. CRAFT *code* is MIT; the *binary* provenance is JaidedAI. UNKNOWN.
4. **Hackathon `Process & Criteria` / `Evaluation Process` / `Eligibility Criteria` tab contents** — the rule-
   bearing sections, not rendered into the fetched HTML. **Gate 1 stays open on licensing.** UNKNOWN.
5. **SynthOCR-Gen tool licence** — HF Space 401, no GitHub repo exists. UNKNOWN.
6. **Which instrument governs the Kashmiri dataset: the `cc`/CC-BY-4.0 tag or the "Controlled Research Access
   License"?** Both sit on the same card. I recorded the contradiction and ruled on the conservative side; the
   maintainer has not been asked. UNRESOLVED (author contact is "open an issue on the repository").
7. **Carried, not attempted:** `anuvaad_tesseract` traineddata (audit TODO #2), tessdata upstream (TODO #1),
   PP-OCR / RapidOCR-ONNX / doctr weight chains (TODO #4/#5/#7), IndicPhotoOCR STocr + SceneTextDetection repos
   (TODO #6). Out of the four prioritised items; unchanged from `LICENSE_AUDIT.md`.
8. **`Datalab.to` pricing terms not opened.** The RAIL-M points there for "Commercial and broader use
   licenses"; whether a commercial licence would waive §2(c) is unknown and is a boss-level commercial question.

**Not legal advice.** These are verbatim clause readings against primary sources, not counsel. Items 1-4 and
7 need a human sign-off before any ship decision.
