# LICENSE AUDIT — model weights + training-data use (R60)

Scope: 10 benchmarked engines. Question is NOT "can we benchmark" (yes, research use) but
"can we use engine OUTPUTS as TRAINING DATA for Vaultstack Stages 2-3b without IP contamination".
Method: local evidence first (pip METADATA, shipped LICENSE files, weight-download URLs in
source). No license is asserted without a local source; unknowns are TODO-VERIFY with URL.

## Table

| Engine | Package license (local source) | Model-weights license (source) | Training-use risk | Outputs as eval vs outputs as TRAINING DATA |
|---|---|---|---|---|
| tesseract_indic (5.5.2) | Apache-2.0 — code binary; pytesseract 0.3.13 Apache-2.0 (.venv METADATA) | tessdata upstream Apache-2.0; NO LICENSE file in /opt/homebrew/share/tessdata — TODO-VERIFY | OK* | eval: fine. training: fine if weights Apache-2.0 (expected; verify) |
| tesseract_bilingual | same as above | same tessdata, same gap | OK* | same as above |
| anuvaad_tesseract | no pip pkg (data only) | anuvaad_*.traineddata: NO local license/readme near files | CAUTION-verify | eval: fine. training: BLOCK until traineddata terms verified |
| openbharatocr 0.4.3 | Apache-2.0 (.dist-info METADATA) | NONE OWN — package is a pytesseract wrapper (ocr/common.py:1 `import pytesseract`); inherits tesseract tessdata | OK* | eval: fine. training: same exposure as tesseract tessdata |
| easyocr 1.7.2 | Apache-2.0 (dist-info METADATA + shipped LICENSE) | ~/.EasyOCR weights (craft_mlt_25k.pth, devanagari.pth, etc.) ship NO LICENSE file. Detector is CRAFT — file name matches clovaai CRAFT release, historically NON-COMMERCIAL research | RISK-noncommercial-or-copyleft (potential) | eval: fine. training: BLOCK until CRAFT + jaided recognition-model terms verified |
| paddleocr_indic (paddleocr 3.7.0) | Apache-2.0 (dist-info METADATA + LICENSE) | PP-OCR weights: not stated in any local file — TODO-VERIFY (historically Apache-2.0, unverified) | CAUTION-verify | eval: fine. training: hold until verified |
| rapidocr 3.9.2 | Apache-2.0 (License-Expression in dist-info METADATA) | PP-OCR ONNX re-hosted at modelscope RapidAI/RapidOCR (default_models.yaml) — no license stated in YAML or METADATA | CAUTION-verify | eval: fine. training: hold until verified (same PP-OCR upstream terms as paddleocr) |
| indicphotoocr (IIIT-H/Bhashini-IITJ, .deps/) | MIT (top-level LICENSE, local) | Recognition/detection/script-ID weights auto-download from anikde/STocr, Bhashini-IITJ/SceneTextDetection, anikde/STscriptdetect — NO LICENSE files local for any ckpt/pth | CAUTION-verify | eval: fine (package MIT). training: BLOCK until those 3 weight repos verified |
| doctr 1.1.0 | Apache-2.0 (python_doctr dist-info METADATA + shipped LICENSE) | weights hosted upstream (HF/mindee serving); nothing local about weight terms | CAUTION-verify | eval: fine. training: hold until verified |
| surya 0.22.1 | Apache-2.0 (dist-info METADATA + licenses/LICENSE) | **"modified AI Pubs Open Rail-M license (free for research, personal use, and startups under $5M funding/revenue)"** — verbatim, surya_ocr-0.22.1.dist-info/METADATA line 99 | RISK-noncommercial-or-copyleft | eval: fine. training: RISK — revenue/funding-capped license + RAIL use-restrictions may travel to outputs |

## Verdict counts (training-data use of outputs)

- SAFE today (Apache/MIT locally, permissive weights chain): **3** — tesseract_indic*, tesseract_bilingual*, openbharatocr* (*tessdata Apache-2.0 needs one quick verify)
- CAUTION — verify before training use: **6** — anuvaad_tesseract, paddleocr_indic, rapidocr, indicphotoocr, doctr, easyocr(easyocr also carries a non-commercial suspicion, see below)
- Likely blocked / conditional for commercial training: **1** — surya (weight license caps use at $5M funding/revenue; not a clean permissive chain)

## Biggest single IP risk

**surya model weights**: the modified OpenRAIL-M license (local evidence: surya METADATA line 99)
(1) terminates free commercial use above $5M funding/revenue — a growth cliff embedded in the
startup's model lineage if trained on surya outputs, and (2) RAIL-family licenses carry
use-restrictions that are designed to attach to the model and derivatives; whether surya OUTPUTS
used as training labels count as a derivative is unverified and the "modified" clauses are not
shipped locally. Second-biggest: easyocr's CRAFT detector weights (craft_mlt_25k.pth in ~/.EasyOCR)
match the clovaai CRAFT release, which historically was released for non-commercial research only.

## TODO-VERIFY (exact upstream checks; no local license file exists for each)

1. Tesseract tessdata (all engines using it): https://github.com/tesseract-ocr/tessdata_fast and
   https://github.com/tesseract-ocr/tessdata — confirm "All data in the repository is licensed under Apache-2.0".
2. Anuvaad traineddata (anuvaad_tel/kan/mal/tam.traineddata): no local metadata at all; check the
   project-anuvaad GitHub org for the traineddata source and license — https://github.com/project-anuvaad
   (org-level guess; find the actual S3/repo the download came from).
3. EasyOCR weights: CRAFT detector — https://github.com/clovaai/CRAFT-pytorch (license section:
   non-commercial research clause); recognition models — https://github.com/jaidedai/easyocr and
   https://github.com/jaidedai/models (weight-release terms).
4. PaddleOCR PP-OCR weights: https://github.com/PaddlePaddle/PaddleOCR (Home-page in local METADATA) —
   confirm models incl. Indic/multilingual rec are Apache-2.0, no NC carve-outs on any specific model card.
5. RapidOCR re-hosted PP-OCR ONNX: https://github.com/RapidAI/RapidOCR and the modelscope repo named in
   default_models.yaml (RapidAI/RapidOCR) — confirm re-hosting under Apache-2.0.
6. IndicPhotoOCR actual weights (package MIT does NOT cover these):
   https://github.com/anikde/STocr (parseq recognizers), https://github.com/Bhashini-IITJ/SceneTextDetection
   (TextBPN++ detectors), https://github.com/anikde/STscriptdetect (CLIP script-ID) — each repo's LICENSE.
7. Doctr pretrained weights: https://github.com/mindee/doctr (Project-URL in local METADATA) — weight
   hosting/HF terms for parseq/mdb/ocr models.
8. Surya: read the FULL text of the modified AI Pubs OpenRAIL-M (linked from
   https://github.com/datalab-to/surya and https://www.datalab.to/pricing) — determine (a) whether
   outputs-as-training-data is a "use" that carries restrictions, (b) the exact $5M threshold terms.

## Evidence paths (all local)

- .venv311/lib/python3.11/site-packages/easyocr-1.7.2.dist-info/METADATA (License: Apache License 2.0) + LICENSE
- .venv311/lib/python3.11/site-packages/paddleocr-3.7.0.dist-info/METADATA + LICENSE (Apache-2.0)
- .venv311/lib/python3.11/site-packages/paddlepaddle-3.3.1.dist-info/METADATA (Apache Software License)
- .venv311/lib/python3.11/site-packages/rapidocr-3.9.2.dist-info/METADATA (License-Expression: Apache-2.0)
- .venv311/lib/python3.11/site-packages/rapidocr/default_models.yaml (weight URLs → modelscope RapidAI)
- .venv311/lib/python3.11/site-packages/python_doctr-1.1.0.dist-info/METADATA + LICENSE (Apache)
- .venv311/lib/python3.11/site-packages/surya_ocr-0.22.1.dist-info/METADATA line 99 (code Apache-2.0; weights = modified OpenRAIL-M, $5M cap) + licenses/LICENSE (Apache-2.0)
- .venv311/lib/python3.11/site-packages/openbharatocr-0.4.3.dist-info/METADATA (Apache) + ocr/common.py (pytesseract wrapper, no own weights)
- .venv/bin pip show pytesseract 0.3.13 (Apache License 2.0)
- .deps/IndicPhotoOCR/LICENSE (MIT, Bhashini Team@IIT Jodhpur); BharatSceneTextDataset/LICENSE (Apache-2.0)
- .deps/IndicPhotoOCR/IndicPhotoOCR/recognition/parseq_recogniser.py, script_identification/CLIP_identifier.py, detection/east/east_utils.py, detection/textbpn/textbpnpp_detector.py (weight URLs → STocr / SceneTextDetection / STscriptdetect)
- ~/.EasyOCR/model/craft_mlt_25k.pth, devanagari.pth, kannada.pth, tamil.pth, telugu.pth, english_g2.pth (no LICENSE file alongside)
- level2/research/smoke/anuvaad_tesseract/tessdata/*.traineddata (no license/readme nearby)
- /opt/homebrew/share/tessdata/*.traineddata (no local LICENSE file)

Honesty note: every "CAUTION-verify" above reflects missing local weight-license evidence, not
license knowledge. Nothing above should be read as legal advice; the TODO-VERIFY list is the
pre-training checklist. Priorities for Stage 2-3b: clear surya and easyocr-CRAFT first (highest
contamination probability), anuvaad and IndicPhotoOCR weight repos second, PP-OCR chain third
(historically permissive, low risk).
