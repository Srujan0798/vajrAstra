---
name: proto-83-licence-verification
description: "Added 2026-09-30 — execute the 8 never-done TODO-VERIFY items in docs/legal/LICENSE_AUDIT.md plus the new candidates (indic-ocr Ol Chiki/Meetei tessdata, Qwen2.5-VL-3B, GLM-OCR, IndicPhotoOCR script-ID weights); surya (best engine) is under a modified OpenRAIL-M with a $5M funding/revenue cap — a CEO-level business fact"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T22:12:19.592Z
---

# PROTO-83 — LICENCE VERIFICATION (research subagent opens primary sources; Verdict checks; boss/Vinay decide business use)

**Why now:** `docs/legal/LICENSE_AUDIT.md` (R60) lists 8 TODO-VERIFY checks — none executed. It flags **surya weights: "modified AI Pubs Open Rail-M license (free for research, personal use, and startups
under $5M funding/revenue)"** (local evidence: `surya_ocr-0.22.1.dist-info/METADATA` line 99) as the biggest IP risk, and easyocr's CRAFT detector (historically non-commercial). Surya is our best
local engine in 9 of 12 languages at n≥50 and the primary route in the wrap-only plan; the team is pursuing funding → this is a business constraint Vinay (CEO) must see. The boss approved the
Ol Chiki/Meetei Mayek Tesseract download (U7) **after a licence check** — that check lives here.

## Research subagent — TASK (paste after the shared context block; open every URL; quote licence text)
> For each item, open the primary licence source, quote the operative clause, and classify for three uses: (1) benchmarking/eval, (2) shipping the engine in our submission/product,
> (3) using its outputs as training data. Items: the 8 TODO-VERIFY URLs in `docs/legal/LICENSE_AUDIT.md` (tessdata, anuvaad traineddata, EasyOCR/CRAFT, PP-OCR weights, RapidOCR ONNX,
> IndicPhotoOCR weight repos incl. the CLIP script identifier, doctr weights, surya's full modified OpenRAIL-M text — find the $5M clause and whether outputs used as labels are restricted);
> plus: `github.com/indic-ocr/indic-ocr.github.io` tessdata (Ol Chiki, Meetei Mayek) · Qwen2.5-VL-3B-Instruct (model card licence) · GLM-OCR (model card licence) · any backbone named in
> `docs/research/level7/W6_QLORA_SPEC.md`. Also: does the AksharDrishti challenge require open-source components or restrict licences? (search the official material; UNKNOWN if not found).
> Write `docs/legal/LICENSE_VERIFIED.md`: table item · licence · clause quote · URL · eval OK? · ship OK? · train-on-outputs OK? · conditions · confidence. Then a 5-line summary for Vinay.

**factchk 2026-09-30:** the indic-ocr repo page says "Set of highly accurate Tesseract OCR models for Indic Scripts which include Ol Chiki (Santali) and Meetei Meyek (Manipuri) scripts too", hosted at https://indic-ocr.github.io/tessdata/ — and states NO licence. Unless a licence is found (repo LICENSE file, model headers, or the authors), treat it as all-rights-reserved: benchmark use only after the boss accepts that risk; do not ship it.

## Gates
- U7 download proceeds only if the indic-ocr licence permits our use; record URL + sha256 of the downloaded files.
- **U14 (boss/Vinay):** ship surya in the submission/product under the $5M cap, or plan a permissive fallback route per language (the proto-82/80 tables show which engine is next-best per language).

Related: [[proto-86-draft-plan-fixes]], [[proto-78-submission-readiness]], [[proto-92-boss-decisions]]

**2026-09-30 — current licence truth:** RQ-9 (`docs/campaign/checkpoints/W4_reports/RQ9_licences.md`) and RESEARCH_DECISIONS RF-05…RF-11. Where this file's TODO rows differ, RQ-9 wins: indic-ocr tessdata Apache-2.0 (cleared) · surya weights OpenRAIL-M Modified §2(c)/§8 → evaluation-only · 600K-KS-OCR research-only clause → HOLD · Bodhan §2.2/§3.1/§3.2 · IndicPhotoOCR script-ID MIT but no sat/mni · EasyOCR code MIT, `.pth` weight licence UNKNOWN.
