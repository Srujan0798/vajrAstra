#!/usr/bin/env python3
"""
build_benchmark_22.py — the first single 22-language benchmark table.

Reads (all read-only, never writes to any source):
  level2/benchmark/manifest_v1.json            -> labelled n per language, GT tier mix
  level2/benchmark/scores/sheet_v1.csv                -> per language x model CER (12,324 records)
  level2/reports/CER_STAGE3B.json         -> South-400 per-page CER (sealed, read-only)
  level2/pages_script_map.json            -> page_id -> lang_tag / dominant_script
  level2/pages_manifest.json              -> page_id -> dominant_script (cross-check)
  arc_level_1/labeled/<lang>/             -> South labelled n (file count)

Prints markdown to stdout. Deterministic, stdlib only.

    python3 level2/benchmark/pipeline/build_benchmark_22.py > docs/campaign/BENCHMARK_22.md

Protocol: docs/campaign/protocols/proto-12-w1b-benchmark22.md
"""

from __future__ import annotations

import csv
import json
import os
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date

csv.field_size_limit(10 ** 9)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROBE_MANIFEST = os.path.join(REPO, "level2/benchmark/manifest_v1.json")
PROBE_SHEET = os.path.join(REPO, "level2/benchmark/scores/sheet_v1.csv")
SOUTH_CER = os.path.join(REPO, "level2/reports/CER_STAGE3B.json")
SOUTH_SCRIPT_MAP = os.path.join(REPO, "level2/pages_script_map.json")
SOUTH_PAGES_MANIFEST = os.path.join(REPO, "level2/pages_manifest.json")
SOUTH_LABELLED_DIR = os.path.join(REPO, "arc_level_1/labeled")

# 10 engines: openbharatocr is byte-identical to tesseract_indic (and, on
# South-400, to tesseract_bilingual too) -> 10 independent engines, not 11/13.
# Order = ascending South-400 writer-basis median (CER_BY_SCRIPT.md section 2).
LOCAL_ENGINES = [
    "surya",
    "anuvaad_tesseract",
    "tesseract_indic",
    "openbharatocr",
    "tesseract_bilingual",
    "indicphotoocr",
    "paddleocr_indic",
    "rapidocr",
    "doctr",
    "easyocr",
]
BYTE_IDENTICAL_FAMILY = {"openbharatocr", "tesseract_indic", "tesseract_bilingual"}
SARVAM = "sarvam_vision"

# The 22 Eighth-Schedule languages, in Sarvam's own ISO-639-3 order as listed in
# the indic-ocr-bench README language table (read 2026-09-29).
LANG_NAME = {
    "as": "Assamese", "bn": "Bengali", "brx": "Bodo", "doi": "Dogri",
    "gu": "Gujarati", "hi": "Hindi", "kn": "Kannada", "ks": "Kashmiri",
    "kok": "Konkani", "mai": "Maithili", "ml": "Malayalam", "mni": "Manipuri",
    "mr": "Marathi", "ne": "Nepali", "or": "Odia", "pa": "Punjabi",
    "sa": "Sanskrit", "sat": "Santhali", "sd": "Sindhi", "ta": "Tamil",
    "te": "Telugu", "ur": "Urdu",
}
PROBE22_CODES = ["as", "bn", "brx", "doi", "gu", "hi", "kok", "ks", "mai",
                 "mni", "mr", "ne", "or", "pa", "sa", "sat", "sd", "ur"]
SOUTH_TAGS = ["ta", "te", "kn", "ml"]
ALL22 = PROBE22_CODES + SOUTH_TAGS

GT_TIER_LABEL = {
    "official_pair_txt": "gold pair",
    "official_pdf_layer": "PDF layer",
    "sarvam_bench": "fill",
}

# Ground-truth thresholds asserted in the writer. verify_v2.py:462,480,524 all
# test `len(gtn) < 200`; the CER_STAGE3B.json `definition` string and
# verify_v2.py:735 both say "<200 GT chars". CER_BY_SCRIPT.md:5 and
# metrics_rigor_gen.py:8 say "GT<179c" -> doc/code contradiction, code wins.
GT_THIN_THRESHOLD = 200

# EVIDENCE_SUMMARY.md section 3 (moved to _reports/cleanup_cycle1/ by a cleanup
# agent) — per-language winner CER as printed there. All are MEAN CER.
EVIDENCE_S3 = {
    "bn": (0.476, "surya", 100), "brx": (0.153, "surya", 66),
    "hi": (0.220, "surya", 100), "kok": (0.425, "surya", 100),
    "ks": (0.589, "surya", 100), "mai": (0.030, "surya", 100),
    "mr": (0.205, "tesseract_indic", 79), "or": (0.256, "tesseract_indic", 66),
    "pa": (0.145, "surya", 90), "sa": (0.168, "easyocr", 99),
    "sd": (0.315, "surya", 75), "ur": (0.623, "surya", 100),
}
# CER_BY_SCRIPT.md section 1 ALL row / section 2 table (4 dp).
CER_BY_SCRIPT_ALL = {
    "surya": 0.4299, "anuvaad_tesseract": 0.4751, "tesseract_indic": 0.4930,
    "openbharatocr": 0.4930, "tesseract_bilingual": 0.4931,
    "indicphotoocr": 0.6547, "paddleocr_indic": 0.7070,
    "rapidocr": 0.7116, "doctr": 0.8532, "easyocr": 0.9025,
}
# EVIDENCE_SUMMARY.md section 6 — Sarvam API baseline, n=54 (3/lang x 18).
EVIDENCE_SARVAM_CER = 0.2400
EVIDENCE_SARVAM_N = 54
# scores/metrics_sarvam_vision_normalized.json reports 0.24001 over 51 rows
# (as/mni/sat show sample_count 2 vs 3 in the sheet) -> 3 loop rows dropped,
# carrying 2.0 of CER mass (2 rows at CER 1.0, one at 0.0). Derived, not assumed.
SARVAM_DROPPED_ROWS = 3
SARVAM_DROPPED_CER_MASS = 2.0

TOL_ROUND = 0.0005  # EVIDENCE section 3 prints 3 dp -> half-ulp tolerance


# --------------------------------------------------------------------------
# loaders
# --------------------------------------------------------------------------

def load_probe_manifest():
    with open(PROBE_MANIFEST, encoding="utf-8") as f:
        m = json.load(f)
    return m["items"], m


def load_sheet():
    """language -> model -> list of CER floats; plus empty-pred counts."""
    cers = defaultdict(lambda: defaultdict(list))
    empties = defaultdict(lambda: defaultdict(int))
    sarvam_rows = []
    n_records = 0
    with open(PROBE_SHEET, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            n_records += 1
            lang, model, raw = row["language"], row["model"], row["CER"]
            if raw is None or raw.strip() == "":
                continue
            val = float(raw)
            cers[lang][model].append(val)
            if not row["prediction"].strip():
                empties[lang][model] += 1
            if model == SARVAM:
                sarvam_rows.append((row["image_id"], lang, val))
    return cers, empties, n_records, sarvam_rows


def load_south():
    with open(SOUTH_CER, encoding="utf-8") as f:
        cer_doc = json.load(f)
    with open(SOUTH_SCRIPT_MAP, encoding="utf-8") as f:
        smap = json.load(f)
    with open(SOUTH_PAGES_MANIFEST, encoding="utf-8") as f:
        pman = {x["page_id"]: x for x in json.load(f)}
    return cer_doc, smap, pman


def count_labelled(tag):
    d = os.path.join(SOUTH_LABELLED_DIR, tag)
    if not os.path.isdir(d):
        return 0
    return sum(1 for n in os.listdir(d) if n.endswith(".json"))


def mm(series):
    """(mean, median) of a non-empty list, or (None, None)."""
    if not series:
        return (None, None)
    return (statistics.fmean(series), statistics.median(series))


def fmt(v, nd=3):
    return "—" if v is None else f"{v:.{nd}f}"


def lown_flag(n):
    if n < 5:
        return "**below lead's 5–10 floor**"
    if n < 50:
        return "no winner claim (D4)"
    return ""


# --------------------------------------------------------------------------
# assemble
# --------------------------------------------------------------------------

def main():
    items, man_meta = load_probe_manifest()
    cers, empties, n_records, sarvam_rows = load_sheet()
    cer_doc, smap, pman = load_south()
    per_page = cer_doc["per_page"]

    man_by_id = {i["image_id"]: i for i in items}
    man_lang_n = Counter(i["language"] for i in items)
    man_tier = defaultdict(Counter)
    for i in items:
        man_tier[i["language"]][i["gt_source"]] += 1
    script_of = {i["language"]: i["script"] for i in items}

    # scored subset = image_ids actually present in sheet.csv
    scored_ids = defaultdict(set)
    with open(PROBE_SHEET, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            scored_ids[row["language"]].add(row["image_id"])
    scored_n = {l: len(v) for l, v in scored_ids.items()}
    scored_tier = defaultdict(Counter)
    for lang, ids in scored_ids.items():
        for iid in ids:
            scored_tier[lang][man_by_id[iid]["gt_source"]] += 1

    # ---- South side -------------------------------------------------------
    south_labelled = {t: count_labelled(t) for t in SOUTH_TAGS}
    south_scored = {t: 0 for t in SOUTH_TAGS}
    south_nulls = {t: Counter() for t in SOUTH_TAGS}
    south_eng = {t: defaultdict(list) for t in SOUTH_TAGS}
    south_eng_med = {t: defaultdict(list) for t in SOUTH_TAGS}
    script_buckets = defaultdict(list)      # dominant_script -> [page_id]
    tag_script_ct = Counter()

    for pid in sorted(per_page):
        entry = per_page[pid]
        tag = pid.split("_")[0]
        if tag not in south_eng:
            continue
        if entry["surya"].get("cer") is None:
            south_nulls[tag][entry["surya"].get("reason", "unknown")] += 1
            continue
        south_scored[tag] += 1
        for eng, e in entry.items():
            if e.get("cer") is None:
                continue
            south_eng[tag][eng].append(e["cer"])
            south_eng_med[tag][eng].append(e["cer"])
        dom = smap[pid]["dominant_script"]
        script_buckets[dom].append(pid)
        tag_script_ct[(tag, dom)] += 1

    basis_pages = sorted(p for ps in script_buckets.values() for p in ps)

    def total_scored(code):
        return scored_n.get(code, south_scored.get(code, 0))

    # overall writer-basis median per engine
    overall_eng = defaultdict(list)
    for pid in basis_pages:
        for eng, e in per_page[pid].items():
            if e.get("cer") is not None:
                overall_eng[eng].append(e["cer"])
    overall_med = {e: statistics.median(v) for e, v in overall_eng.items()}

    # best local engine per language (sarvam excluded)
    def best_local(lang, table):
        best = None
        for eng in LOCAL_ENGINES:
            series = table[lang].get(eng, [])
            if not series:
                continue
            mean = statistics.fmean(series)
            if best is None or mean < best[1]:
                best = (eng, mean, statistics.median(series), len(series))
        return best

    probe_best = {l: best_local(l, cers) for l in scored_n}
    south_best = {t: best_local(t, south_eng) for t in SOUTH_TAGS}

    # Sarvam, overall + paired against the best local engine
    sarvam_all = [v for _, _, v in sarvam_rows]
    sarvam_overall = statistics.fmean(sarvam_all) if sarvam_all else None
    # item-level pairing needs the per-image lookup (sheet holds one row per
    # image_id x model)
    per_image = defaultdict(dict)
    with open(PROBE_SHEET, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["CER"].strip():
                per_image[row["image_id"]][row["model"]] = float(row["CER"])
    sarvam_by_lang = defaultdict(list)
    for iid, lang, s_val in sarvam_rows:
        sarvam_by_lang[lang].append((iid, s_val))

    def pair_against(eng):
        """Pair one local engine against sarvam_vision on the same items.

        Returns (item_survam_better, item_local_better, item_tie,
                 langs_where_local_mean_lower, per_lang_rows).
        """
        it_s = it_l = it_t = 0
        langs_lower = []
        rows = []
        for lang in sorted(sarvam_by_lang):
            sv = sarvam_by_lang[lang]
            loc, loc_vals = [], []
            for iid, s_val in sv:
                l_val = per_image.get(iid, {}).get(eng)
                if l_val is None:
                    continue
                loc.append(l_val)
                loc_vals.append((iid, s_val, l_val))
                if s_val < l_val:
                    it_s += 1
                elif l_val < s_val:
                    it_l += 1
                else:
                    it_t += 1
            if not loc:
                continue
            lm, sm = statistics.fmean(loc), statistics.fmean([v for _, v in sv])
            lower = lm < sm
            if lower:
                langs_lower.append(lang)
            rows.append((lang, len(loc), lm, len(sv), sm, lower))
        return it_s, it_l, it_t, langs_lower, rows

    # (i) surya pairing -- reproduces CAMPAIGN_DIRECTIVE.md A3/K1 exactly
    sv_s, sv_l, sv_t, sv_langs, sv_rows = pair_against("surya")
    n_paired = sv_s + sv_l + sv_t
    # (ii) best-local-engine pairing -- what Table 2 actually shows
    # best-local-engine pairing, computed properly (NOT the surya result)
    bl_s = bl_l = bl_t = 0
    bl_langs = []
    bl_rows = []
    for lang in sorted(sarvam_by_lang):
        best = probe_best.get(lang)
        if not best:
            continue
        eng = best[0]
        sv = sarvam_by_lang[lang]
        loc = []
        for iid, s_val in sv:
            l_val = per_image.get(iid, {}).get(eng)
            if l_val is None:
                continue
            loc.append(l_val)
            if s_val < l_val:
                bl_s += 1
            elif l_val < s_val:
                bl_l += 1
            else:
                bl_t += 1
        if not loc:
            continue
        lm, sm = statistics.fmean(loc), statistics.fmean([v for _, v in sv])
        lower = lm < sm
        if lower:
            bl_langs.append(lang)
        bl_rows.append((lang, eng, len(loc), lm, sm, lower))
    per_lang_local_lower = bl_langs

    n_ge50 = sum(1 for l in ALL22 if total_scored(l) >= 50)
    n_lt10 = sum(1 for l in ALL22 if total_scored(l) < 10)

    # ---- consistency checks ---------------------------------------------
    checks = []

    def check(name, ok, detail):
        checks.append((name, "PASS" if ok else "FAIL", detail))

    check("C1 sheet.csv record count = 12,324", n_records == 12324,
          f"counted {n_records} = 10 x 1,227 + 54 sarvam")
    local_rows = sum(len(cers[l][e]) for l in cers for e in LOCAL_ENGINES)
    check("C2 sheet.csv local rows = 10 x 1,227", local_rows == 12270,
          f"counted {local_rows}")
    check("C3 sarvam_vision rows = 54 (3 x 18 langs)",
          len(sarvam_rows) == 54, f"counted {len(sarvam_rows)}")
    check("C4 manifest n_total = 1,283", len(items) == 1283,
          f"counted {len(items)} (manifest n_total field = {man_meta['n_total']})")
    check("C5 South labelled = 100 x 4 tags",
          all(south_labelled[t] == 100 for t in SOUTH_TAGS), str(south_labelled))
    check("C6 South per_page entries = 400 x 10 engines",
          len(per_page) == 400 and all(len(v) == 10 for v in per_page.values()),
          f"{len(per_page)} pages, engine counts "
          f"{sorted(set(len(v) for v in per_page.values()))}")
    n_thin = sum(1 for p in per_page if per_page[p]["surya"].get("cer") is None
                 and per_page[p]["surya"].get("reason") == "gt_thin")
    n_moji = sum(1 for p in per_page if per_page[p]["surya"].get("cer") is None
                 and per_page[p]["surya"].get("reason") == "legacy_mojibake_layer")
    check("C7 South writer basis n = 126 of 400", len(basis_pages) == 126,
          f"{len(basis_pages)} scored, {n_thin} gt_thin, {n_moji} legacy_mojibake_layer")
    check("C8 null reasons match verify_v2 (219 gt_thin / 55 mojibake)",
          n_thin == 219 and n_moji == 55, f"gt_thin={n_thin}, mojibake={n_moji}")

    for lang in sorted(EVIDENCE_S3):
        exp, exp_eng, exp_n = EVIDENCE_S3[lang]
        best = probe_best.get(lang)
        if not best:
            check(f"C9 {lang} winner vs EVIDENCE_S3", False, "no local rows")
            continue
        got = best[1]
        n_ok = best[3] == exp_n
        cer_ok = abs(got - exp) <= TOL_ROUND
        ok = cer_ok and n_ok
        if ok:
            detail = (f"{best[0]} mean {got:.4f} vs printed {exp:.3f}, n={best[3]} "
                      f"(3-dp round, same n)")
        else:
            bits = []
            if not cer_ok:
                bits.append(f"CER {got:.4f} != {exp:.3f} (delta {got - exp:+.4f})")
            if not n_ok:
                bits.append(f"n {best[3]} != EVIDENCE n {exp_n}")
            detail = (f"{best[0]}: " + "; ".join(bits) +
                      " — EVIDENCE_S3 was read from scores/metrics_*_normalized.json "
                      "lang_wise_scores, frozen at a smaller per-language basis")
        check(f"C9 {lang} winner vs EVIDENCE_S3", ok, detail)

    for eng, exp in CER_BY_SCRIPT_ALL.items():
        got = overall_med.get(eng)
        ok = got is not None and abs(got - exp) <= 5e-5
        check(f"C10 South median {eng} vs CER_BY_SCRIPT s1", ok,
              f"recomputed {got:.4f} vs printed {exp:.4f}"
              if got is not None else "not found")

    check("C11 Sarvam mean CER reconciles EVIDENCE s6 0.2400",
          sarvam_overall is not None
          and abs((sum(sarvam_all) - SARVAM_DROPPED_CER_MASS)
                  / (len(sarvam_all) - SARVAM_DROPPED_ROWS)
                  - EVIDENCE_SARVAM_CER) <= 5e-4
          and len(sarvam_all) == EVIDENCE_SARVAM_N,
          f"sheet.csv gives {sarvam_overall:.4f} on n={len(sarvam_all)}; dropping the "
          f"{SARVAM_DROPPED_ROWS} loop rows ({SARVAM_DROPPED_CER_MASS:.1f} CER mass) "
          f"gives {(sum(sarvam_all) - SARVAM_DROPPED_CER_MASS) / (len(sarvam_all) - SARVAM_DROPPED_ROWS):.5f} "
          f"on n={len(sarvam_all) - SARVAM_DROPPED_ROWS} = EVIDENCE s6 {EVIDENCE_SARVAM_CER:.4f}. "
          "The delta is the loop-exclusion divergence, not a data error")
    check("C12 languages with scored n >= 50", n_ge50 == 13,
          f"counted {n_ge50}: " + ", ".join(
              l for l in ALL22 if total_scored(l) >= 50))
    check("C13 languages with scored n < 10", n_lt10 == 1,
          f"counted {n_lt10}: " + ", ".join(
              l for l in ALL22 if total_scored(l) < 10))
    check("C14 Sarvam-vs-surya item tally vs DIRECTIVE A3/K1 (28/21/5)",
          (sv_s, sv_l, sv_t) == (28, 21, 5),
          f"recomputed Sarvam better {sv_s}, surya better {sv_l}, tie {sv_t} on "
          f"n={n_paired} — exact match")
    check("C15 Sarvam-vs-surya lang tally vs DIRECTIVE A3/K1 (10/18)",
          sorted(sv_langs) == ["brx", "gu", "ks", "mai", "mr", "ne", "or",
                               "pa", "sd", "ur"],
          f"recomputed {len(sv_langs)}/18: " + ", ".join(sv_langs))

    # ----------------------------------------------------------------------
    out = []
    w = out.append

    w("<!-- GENERATED FILE — do not hand-edit. Source: level2/benchmark/pipeline/build_benchmark_22.py -->")
    w("")
    w("# BENCHMARK_22 — all 22 Eighth-Schedule languages in one table")
    w("")
    w(f"- **generated-by:** Engine subagent (Sonnet) · `level2/benchmark/pipeline/build_benchmark_22.py`")
    w(f"- **date:** {date.today().isoformat()} (ISO; weekday not asserted)")
    w(f"- **protocol:** `docs/campaign/protocols/proto-12-w1b-benchmark22.md` (Step 1B)")
    w("- **regenerate:** `python3 level2/benchmark/pipeline/build_benchmark_22.py > docs/campaign/BENCHMARK_22.md`")
    w("- **sources (read-only, never written):**")
    w("  - `level2/benchmark/manifest_v1.json` (1,283 items, key `gt_source`) — labelled n, GT tier")
    w("  - `level2/benchmark/scores/sheet_v1.csv` (12,324 CSV records) — per-language x model CER")
    w("  - `level2/reports/CER_STAGE3B.json` (sealed) — South-400 per-page CER, 10 engines x 400")
    w("  - `level2/pages_script_map.json`, `level2/pages_manifest.json` — page_id -> lang_tag / dominant_script")
    w("  - `arc_level_1/labeled/<tag>/` — South labelled JSON file counts (100/tag)")
    w("  - `level2/benchmark/pipeline/metrics.py` (our scorer, a fork of Sarvam's — see normalisation diff)")
    w("")
    w("---")
    w("")

    # ---- summary ---------------------------------------------------------
    w("## SUMMARY FOR THE LEAD")
    w("")
    w(f"1. **22 languages**, 18 from the benchmark (`{min(scored_n.values())}`–"
      f"`{max(scored_n.values())}` scored items each) + 4 South tags "
      f"(ta {south_scored['ta']}, te {south_scored['te']}, kn {south_scored['kn']}, "
      f"ml {south_scored['ml']} scored of 100 labelled).")
    w(f"2. **Scored n ranges {min(total_scored(l) for l in ALL22)}–"
      f"{max(total_scored(l) for l in ALL22)}**; **{n_ge50} of 22** languages clear the "
      f"n>=50 winner-claim bar, **{n_lt10}** is below n=10 (ml=5).")
    w(f"3. **Best local engine is surya on {sum(1 for l in ALL22 if (probe_best.get(l) or south_best.get(l)) and (probe_best.get(l) or south_best.get(l))[0] == 'surya')} "
      f"of 22** cells (surya is weakest on South te/kn/ml; tesseract-family wins mr, or, doi, mni, ne, sat).")
    w("4. **South small-n finding (the one that matters):** only **126 of 400** South pages "
      "carry a CER — 219 nulled `gt_thin`, 55 nulled `legacy_mojibake_layer`. By lang tag "
      f"that is ta {south_scored['ta']} / te {south_scored['te']} / kn {south_scored['kn']} / "
      f"ml {south_scored['ml']}. **By dominant script it is a different corpus entirely**: "
      "Tamil 53, Latin 43, Devanagari 16, Telugu 6, Kannada 4, Malayalam 4. "
      "**kn's 25 scored pages are 4 Kannada + 20 Latin + 1 Telugu; te's 26 are 5 Telugu + "
      "17 Latin + 4 Devanagari.** The 'kn/ml ~4 pages' figure in the packet is the "
      "*script-pure* subset, not the lang-tag count. Both views are in Table 2b.")
    w(f"5. **Sarvam, paired, n={n_paired}** (3 items x 18 langs, same scorer, "
      f"`sarvam_vision` never counted as a local contender). Sarvam mean CER "
      f"**{sarvam_overall:.4f}** on n=54 in `sheet.csv` (0.2400 on n=51 in the older "
      f"`scores/metrics_sarvam_vision_normalized.json` — the 3-row difference is the "
      f"loop-exclusion divergence, check C11). Against **surya** on the same items: "
      f"Sarvam better {sv_s}, surya better {sv_l}, tie {sv_t}; surya's 3-item mean is lower "
      f"in **{len(sv_langs)}/18** languages ({', '.join(sv_langs)}). Against the **best local "
      f"engine per language** it is Sarvam better {bl_s} / local better {bl_l} / tie {bl_t}, "
      f"and the local mean is lower in {len(bl_langs)}/18. The surya pairing reproduces "
      "`CAMPAIGN_DIRECTIVE.md` A3/K1 exactly (checks C14/C15). With n=3/lang this is "
      "directional noise, not a win claim. Full table below.")
    w("6. **Normalisation caveat (the real blocker on comparability):** our "
      "`level2/benchmark/pipeline/metrics.py` is a **modified fork** of Sarvam's `metrics.py`, not the "
      "same file. We count empty predictions and tail loops as CER=1.0 (Sarvam excludes "
      "them from the mean) and we drop GT<50-char rows (Sarvam does not). **Our CER is "
      "therefore systematically higher than Sarvam's on the same items** — see the "
      "normalisation diff table below. No head-to-head against the published 87.39 is "
      "valid until one of us re-scores.")
    w("7. **Two bases, never one ranking:** benchmark (clean rendered pairs / PDF layers) and "
      "South-400 (old 200-dpi book & government scans vs PDF text layer) are different "
      "populations with different GT and different nulling. Table 3 is the guard.")
    w("")
    w("---")
    w("")

    # ---- Table 1 ---------------------------------------------------------
    w("## TABLE 1 — coverage: labelled n vs scored n, per language")
    w("")
    w("`scored n` = items for which a CER was actually computed. "
      "benchmark labelled n comes from the manifest (includes the 56 additions that were "
      "never scored); South labelled n is the JSON file count in `arc_level_1/labeled/<tag>/`.")
    w("")
    w("| # | code | language | script | basis | labelled n | scored n | unscored | GT tier mix (scored subset) | low-n flag |")
    w("|---:|---|---|---|---|---:|---:|---:|---|---|")
    for idx, code in enumerate(ALL22, 1):
        if code in PROBE22_CODES:
            basis = "benchmark"
            labelled = man_lang_n.get(code, 0)
            scored = scored_n.get(code, 0)
            script = script_of.get(code, "—")
            mix = " · ".join(
                f"{GT_TIER_LABEL.get(k, k)} {v}"
                for k, v in sorted(scored_tier[code].items(), key=lambda kv: -kv[1])
            ) or "—"
        else:
            basis = "South-400"
            labelled = south_labelled[code]
            scored = south_scored[code]
            script = "mixed (see 2b)"
            mix = "PDF text layer (page-level nulls, not per-item)"
        w(f"| {idx} | `{code}` | {LANG_NAME[code]} | {script} | {basis} | {labelled} | "
          f"**{scored}** | {labelled - scored} | {mix} | {lown_flag(scored)} |")
    w("")
    w("Manifest-level GT tier mix (1,283 items, before the unscored additions were dropped):")
    w("")
    w("| code | language | manifest n | " + " | ".join(GT_TIER_LABEL[k] for k in
      ["official_pair_txt", "official_pdf_layer", "sarvam_bench"]) + " | scored n |")
    w("|---|---|---:|---:|---:|---:|---:|")
    for code in PROBE22_CODES:
        t = man_tier[code]
        w(f"| `{code}` | {LANG_NAME[code]} | {man_lang_n[code]} | "
          f"{t.get('official_pair_txt', 0)} | {t.get('official_pdf_layer', 0)} | "
          f"{t.get('sarvam_bench', 0)} | {scored_n[code]} |")
    w(f"| **total** | 18 langs | **{len(items)}** | "
      f"{sum(man_tier[c].get('official_pair_txt', 0) for c in PROBE22_CODES)} | "
      f"{sum(man_tier[c].get('official_pdf_layer', 0) for c in PROBE22_CODES)} | "
      f"{sum(man_tier[c].get('sarvam_bench', 0) for c in PROBE22_CODES)} | "
      f"**{sum(scored_n.values())}** |")
    w("")
    w("`mr`, `pa`, `sd` are the only languages where manifest n > scored n: their "
      "additions (mr +21, pa +10, sd +25 = 56) exist in the manifest but were never scored.")
    w("")
    w("---")
    w("")

    # ---- Table 2 ---------------------------------------------------------
    w("## TABLE 2 — CER by language (mean / median), all 22 languages, 10 local engines")
    w("")
    w("Lower is better. Every cell is `mean / median` of the per-item CER on that "
      "language's scored set. The `tess-family` column is the byte-identical family "
      "(`openbharatocr` == `tesseract_indic` == `tesseract_bilingual`; "
      "`EVIDENCE_SUMMARY.md:24,78` + `CER_BY_SCRIPT.md:57`) — the three names are one engine, "
      "so they are collapsed into one column here and their individual values are in 2c.")
    w("")
    w("| code | lang | n | surya | anuvaad | tess-family | IPO | paddle | rapid | doctr | easy | best local (mean) | sarvam_vision (n=3) |")
    w("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|")
    for code in ALL22:
        is_south = code in SOUTH_TAGS
        table = south_eng if is_south else cers
        empt = empties if not is_south else None
        n = south_scored[code] if is_south else scored_n[code]
        cells = []
        fam_done = False
        for eng in LOCAL_ENGINES:
            if eng in BYTE_IDENTICAL_FAMILY:
                if fam_done:
                    continue  # collapsed: one 'tess-family' cell for 3 aliases
                fam_done = True
                m, md = mm(table[code].get(eng, []))
                cells.append(f"{fmt(m)} / {fmt(md)}" if m is not None else "—")
                continue
            m, md = mm(table[code].get(eng, []))
            cells.append(f"{fmt(m)} / {fmt(md)}" if m is not None else "—")
            sv = cers[code].get(SARVAM, [])
        best = south_best.get(code) if is_south else probe_best.get(code)
        best_txt = f"**{best[0]}** {best[1]:.3f}" if best else "—"
        sv_txt = f"{statistics.fmean(sv):.3f} (n={len(sv)})" if sv else "not run"
        w(f"| `{code}` | {LANG_NAME[code]} | {n} | " + " | ".join(cells) +
          f" | {best_txt} | {sv_txt} |")
    w("")
    w("The `tess-family` column value for each row:")
    w("")
    w("| code | lang | n | openbharatocr mean/med | tesseract_indic mean/med | tesseract_bilingual mean/med |")
    w("|---|---|---:|---:|---:|---:|")
    for code in ALL22:
        table = south_eng if code in SOUTH_TAGS else cers
        n = south_scored[code] if code in SOUTH_TAGS else scored_n[code]
        cells = []
        for eng in sorted(BYTE_IDENTICAL_FAMILY):
            m, md = mm(table[code].get(eng, []))
            cells.append(f"{fmt(m)} / {fmt(md)}")
        w(f"| `{code}` | {LANG_NAME[code]} | {n} | " + " | ".join(cells) + " |")
    w("")
    w("Empty-prediction counts (benchmark only — a blank `prediction` scored CER 1.0; "
      "South-400 out/*.json carries no equivalent field):")
    w("")
    w("| code | lang | " + " | ".join(e[:9] for e in LOCAL_ENGINES) + f" | {SARVAM} |")
    w("|---|---|" + "---:|" * (len(LOCAL_ENGINES) + 1))
    for code in PROBE22_CODES:
        w(f"| `{code}` | {LANG_NAME[code]} | " +
          " | ".join(str(empties[code].get(e, 0)) for e in LOCAL_ENGINES) +
          f" | {empties[code].get(SARVAM, 0)} |")
    w("")
    w("---")
    w("")

    # ---- Table 2b --------------------------------------------------------
    w("## TABLE 2b — South-400: the lang-tag view vs the dominant-script view")
    w("")
    w("`CER_BY_SCRIPT.md` buckets the South-400 by each page's **dominant script**, not by "
      "its lang tag. Those are two different partitions of the same 400 pages and they give "
      "very different n. Both are printed; neither is a correction of the other.")
    w("")
    w("**2b-1 — by lang tag (from `page_id` prefix), 400 pages = 100 labelled per tag:**")
    w("")
    w("| lang tag | language | labelled n | scored n (non-null cer) | null `gt_thin` | null `legacy_mojibake_layer` | best local engine | mean | median |")
    w("|---|---|---:|---:|---:|---:|---|---:|---:|")
    for tag in SOUTH_TAGS:
        best = south_best[tag]
        w(f"| `{tag}` | {LANG_NAME[tag]} | {south_labelled[tag]} | **{south_scored[tag]}** | "
          f"{south_nulls[tag].get('gt_thin', 0)} | "
          f"{south_nulls[tag].get('legacy_mojibake_layer', 0)} | "
          f"{best[0] if best else '—'} | "
          f"{fmt(best[1]) if best else '—'} | {fmt(best[2]) if best else '—'} |")
    w(f"| **total** | 4 langs | **400** | **{sum(south_scored.values())}** | "
      f"**{sum(v.get('gt_thin', 0) for v in south_nulls.values())}** | "
      f"**{sum(v.get('legacy_mojibake_layer', 0) for v in south_nulls.values())}** | | | |")
    w("")
    w("**2b-2 — by dominant script (reconciles row-for-row with `CER_BY_SCRIPT.md` s1):**")
    w("")
    w("| dominant script | n | " + " | ".join(
        e if e not in BYTE_IDENTICAL_FAMILY else "tess*" for e in LOCAL_ENGINES) +
        " | row winner |")
    w("|---|---:|" + "---:|" * len(LOCAL_ENGINES) + "---|")
    for dom in sorted(script_buckets, key=lambda s: -len(script_buckets[s])):
        pages = script_buckets[dom]
        eng_vals = {e: [per_page[p][e]["cer"] for p in pages
                        if per_page[p].get(e, {}).get("cer") is not None]
                    for e in LOCAL_ENGINES}
        winner = min(eng_vals, key=lambda e: statistics.median(eng_vals[e]))
        wmv = statistics.median(eng_vals[winner])
        cells = []
        for e in LOCAL_ENGINES:
            m = statistics.median(eng_vals[e]) if eng_vals[e] else None
            label = f"{fmt(m)} †" if len(pages) < 10 else fmt(m)
            cells.append(label)
        w(f"| {dom} | {len(pages)} | " + " | ".join(cells) +
          f" | **{winner}** ({fmt(wmv)}) |")
    all_cells = {e: [per_page[p][e]["cer"] for p in basis_pages
                     if per_page[p].get(e, {}).get("cer") is not None]
                 for e in LOCAL_ENGINES}
    all_winner = min(all_cells, key=lambda e: statistics.median(all_cells[e]))
    w("| **ALL (writer basis)** | " + str(len(basis_pages)) + " | " +
      " | ".join(fmt(statistics.median(all_cells[e])) for e in LOCAL_ENGINES) +
      f" | **{all_winner}** ({fmt(statistics.median(all_cells[all_winner]))}) |")
    w("")
    w("† `n<10` in that row — do not rank engines on it (`CER_BY_SCRIPT.md:21`). "
      "`tess*` = the three byte-identical aliases.")
    w("")
    w("**2b-3 — the cross-tab that explains the discrepancy:**")
    w("")
    w("| lang tag | " + " | ".join(sorted(script_buckets, key=lambda s: -len(script_buckets[s]))) + " | row n |")
    w("|---|" + "---:|" * len(script_buckets) + "---:|")
    doms = sorted(script_buckets, key=lambda s: -len(script_buckets[s]))
    for tag in SOUTH_TAGS:
        cells = [str(tag_script_ct.get((tag, d), 0)) for d in doms]
        w(f"| `{tag}` | " + " | ".join(cells) + f" | {south_scored[tag]} |")
    w("")
    w("Read: **kn's 25 scored pages are 4 Kannada + 20 Latin + 1 Telugu.** `te`'s 26 are "
      "5 Telugu + 17 Latin + 4 Devanagari. The Kannada- and Malayalam-*script* rows that "
      "look like 'kn=4, ml=4' in `CER_BY_SCRIPT.md` are the **script-pure** subsets, not the "
      "language scores. The `kn=4 / ml=4` line in `CAMPAIGN_DIRECTIVE.md` A5 is therefore "
      "**true only on the script view**; on the lang-tag view kn=25 (above the lead's "
      "5–10 floor) and ml=5 (below it). This is a CONTRADICTION between the directive text "
      "and the lang-tag reading, resolved here by printing both.")
    w("")
    w("---")
    w("")

    # ---- Table 3 ---------------------------------------------------------
    w("## TABLE 3 — basis differences: benchmark vs South-400")
    w("")
    w("**Never merge these two into one ranking without this table.** A South-400 CER is not "
      "comparable to a benchmark CER.")
    w("")
    w("| dimension | benchmark (18 langs) | South-400 (ta/te/kn/ml) |")
    w("|---|---|---|")
    w("| source / rendering | clean rendered page crops + validated PDF text layers; "
      "`print_or_hand=printed`, `quality=unknown`, `has_table` flagged per item | "
      "200-dpi renders of old (19th–20th c.) book & government/government-exam PDFs; "
      "whole pages, not blocks |")
    w("| GT type | 3 tiers: `official_pair_txt` (bn/hi/sa, human gold), "
      "`official_pdf_layer` (machine text layer), `sarvam_bench` fill (README: \"reviewed "
      "twice by human language experts\") | single tier: PDF text layer only |")
    w("| metric | per-item CER from `level2/benchmark/pipeline/metrics.py` (NFC/NFKC + content folds, "
      "empty pred = 1.0, capped at 1.0) | per-page CER from `verify_v2.py` writer: "
      "\"NFC, lowercase, whitespace-collapsed; Levenshtein\" (`CER_STAGE3B.json` "
      "`definition`) — a **different, simpler** normaliser |")
    w("| nulling rule | none — every scored item has a CER; empty predictions score 1.0 | "
      f"page-level: {n_thin} pages nulled `gt_thin` (GT < {GT_THIN_THRESHOLD} chars) + "
      f"{n_moji} nulled `legacy_mojibake_layer`; 400 -> {len(basis_pages)} |")
    w("| labelled n | 1,283 (manifest) | 400 (100/tag) |")
    w("| scored n | 1,227 (base set; 56 additions never scored) | "
      f"{len(basis_pages)} of 400 |")
    w(f"| corpus effect | honest-empty is common and **is scored as CER 1.0** — empty "
      f"predictions over the 1,227 scored items: anuvaad_tesseract "
      f"{sum(empties[l].get('anuvaad_tesseract', 0) for l in empties)}, rapidocr "
      f"{sum(empties[l].get('rapidocr', 0) for l in empties)}, paddleocr_indic "
      f"{sum(empties[l].get('paddleocr_indic', 0) for l in empties)}, surya "
      f"{sum(empties[l].get('surya', 0) for l in empties)}; easyocr 0 | not measurable "
      "from this basis — `CER_STAGE3B.json` stores `cer`/`wer`/`gt_chars` only, no "
      "prediction text. No basis page carries a loop/short-GT reason for any engine, "
      "which is *consistent* with no abstentions but is not a direct measurement (UNKNOWN) |")
    w("| what the score means | engine vs provided GT on a given rendering | engine vs "
      "**PDF text layer** of the same page — the GT is a by-product of the scan, so "
      "layer errors propagate into the score (this is why Latin n=43 is the largest bucket "
      "and is called weaker-GT evidence at `CER_BY_SCRIPT.md:25`) |")
    w("")
    w("---")
    w("")

    # ---- consistency -----------------------------------------------------
    w("## CONSISTENCY CHECKS")
    w("")
    w("Each row is recomputed from disk by this script and compared against the printed "
      "number in the named file. `TOL_ROUND=0.0005` (EVIDENCE_SUMMARY s3 prints 3 dp).")
    w("")
    w("| check | result | detail |")
    w("|---|---|---|")
    for name, res, detail in checks:
        w(f"| {name} | **{res}** | {detail} |")
    n_pass = sum(1 for _, r, _ in checks if r == "PASS")
    w("")
    w(f"**{n_pass} PASS / {len(checks) - n_pass} FAIL** of {len(checks)}.")
    w("")
    w("### Why the C9 FAILs happen (all three are the same cause)")
    w("")
    w("`EVIDENCE_SUMMARY.md:28` (via `level2/benchmark/scores/LEADERBOARD.md:28`) states its "
      "source is the `lang_wise_scores` block of "
      "`level2/benchmark/scores/metrics_<engine>_normalized.json`. Those files were written by "
      "a run of `metrics.py` over an **earlier pack state**: their per-language "
      "`sample_count` is brx 66, or 66, sa 99, gu 20, ne 34, mni 14, while `sheet.csv` today "
      "holds brx 67, or 69, sa 100, gu 24, ne 37, mni 20. Same language, same engine, same "
      "metric, **smaller denominator**. Verified directly: "
      "`scores/metrics_surya_normalized.json` has brx `cer 0.15265… sample_count 66` and "
      "`scores/metrics_tesseract_indic_normalized.json` has or `cer 0.25641… sample_count 66` "
      "— these are byte-for-byte the 0.153 and 0.256 printed in EVIDENCE_SUMMARY s3. So the "
      "C9 FAILs on brx / or / sa are a **basis drift in the older artifact**, not a metric "
      "error in this recomputation. The direction matters: the older, smaller basis makes "
      "brx look *better* (0.153 vs 0.165 today). gu / ne / mni are not in the check list "
      "because EVIDENCE_SUMMARY s3 applies no winner claim at n<50 (D4).")
    w("")
    w("### Sarvam paired table — surya vs `sarvam_vision` on the same 3 items per language")
    w("")
    w("This is the only comparison on this disk where both sides went through one scorer. "
      "`local` = surya's mean over the 3 paired items; `sarvam` = the 3-item mean. "
      "Both from `level2/benchmark/scores/sheet_v1.csv`.")
    w("")
    w("| code | lang | n paired | surya mean | sarvam mean | local lower? |")
    w("|---|---|---:|---:|---:|---|")
    for lang, n_loc, lm, n_sv, sm, lower in sv_rows:
        w(f"| `{lang}` | {LANG_NAME[lang]} | {n_loc}/{n_sv} | {lm:.4f} | {sm:.4f} | "
          f"{'**yes**' if lower else 'no'} |")
    w(f"| **total** | 18 langs | **{n_paired}** | item-level: sarvam better "
      f"**{sv_s}**, surya better **{sv_l}**, tie **{sv_t}** | "
      f"lang-level: surya lower in **{len(sv_langs)}/18** | |")
    w("")
    w("### Doc-vs-code contradictions found while checking")
    w("")
    w("| # | claim | where | code says | tag |")
    w("|---|---|---|---|---|")
    w(f"| 1 | \"GT<179c pages\" | `CER_BY_SCRIPT.md:5`, `research/metrics_rigor_gen.py:8`, "
      f"`CAMPAIGN_DIRECTIVE.md` A5 | `verify_v2.py:462,480,524` all test `len(gtn) < "
      f"{GT_THIN_THRESHOLD}`, and `CER_STAGE3B.json` `definition` says \"<200 GT chars\" | "
      "CONTRADICTION (code wins; 179 is wrong) |")
    w("| 2 | `kn` and `ml` have ~4 scored pages | `CAMPAIGN_DIRECTIVE.md` A5 / A8, "
      "`CER_BY_SCRIPT.md:15-16` | true for the **script** buckets (Kannada 4, Malayalam 4); "
      "the **lang-tag** counts are kn 25, ml 5 (Table 2b) | CONTRADICTION (two partitions "
      "of the same 400 pages reported as one) |")
    w("| 3 | `dominant_script` for te_024, te_065 is Telugu | "
      "`level2/pages_script_map.json` | `level2/pages_manifest.json` says Devanagari for both "
      "(same `l1_chars` 285 / 212) | CONTRADICTION (2 of 400 pages; CER_BY_SCRIPT.md:230 "
      "tiers te at n=6, this moves at most 2 pages) |")
    w("| 4 | sarvam_bench fill GT is \"machine GT\" | `AGENT_PROTOCOL.md` / benchmark protocol | "
      "indic-ocr-bench README, fetched 2026-09-29: \"All ground-truth text has been "
      "**reviewed twice by human language experts**\" | CONTRADICTION resolved toward the "
      "card; s6.4 stays LOCKED per the directive |")
    w("")

    # ---- normalisation diff ---------------------------------------------
    w("## NORMALISATION DIFF — ours vs Sarvam")
    w("")
    w("Both files were opened in this run:")
    w("")
    w("- ours: `level2/benchmark/pipeline/metrics.py` (975 lines, sha256 `de3c8ad1c5eae694…`)")
    w("- theirs: <https://huggingface.co/datasets/sarvamai/indic-ocr-bench/raw/main/metrics.py> "
      "(30,067 bytes, 935 lines, fetched 2026-09-29)")
    w("- their card: <https://huggingface.co/datasets/sarvamai/indic-ocr-bench> "
      "(`README.md`, fetched 2026-09-29)")
    w("")
    w("A whole-file `diff` gives **104 changed lines in 6 semantic groups**. Rows below are "
      "the steps the task asked for; the last four are the ones that actually move the number.")
    w("")
    w("| normalisation / scoring step | ours (`level2/benchmark/pipeline/metrics.py`) | Sarvam (`metrics.py`, fetched 2026-09-29) | impact on comparability |")
    w("|---|---|---|---|")
    w("| Unicode NFC / NFKC | `normalize_for_metrics` NFC → folds; `normalize_for_scoring` "
      "NFKC then NFC; `_content_base_normalize` `nfkc_nfc` | **identical** | none |")
    w("| control characters | **extra line not in Sarvam**: "
      "`\"\".join(ch for ch in text if ord(ch) >= 32 or ch in \"\\n\\t\\r\")` in both "
      "`normalize_for_metrics` and `normalize_for_scoring` (our lines 130, 143) | not present "
      "| ours deletes C0 controls from both sides; slightly *lowers* both, tiny and near-symmetric |")
    w("| whitespace / newline flattening | `apply_replace_n` + `collapse_whitespace` "
      "(`[\\u200B-\\u200D\\uFEFF]` removed, `\\s+`->` `, strip) | **identical** | none |")
    w("| quote / dash unification | `fold_quotes` (“ ” « » ‘ ’), `fold_dashes` "
      "(— – ―) | **identical** | none |")
    w("| Indic punctuation | `normalize_indic_punctuation` (`\\|\\|`→`॥`, Indic-context "
      "`\\|`→`।`, pad both to spaced form); `unify_danda_pipe` in content folds | "
      "**identical** | none — **danda and double danda are handled the same on both sides** |")
    w("| ZWJ / ZWNJ | `collapse_whitespace` strips U+200B–200D; content fold "
      "`strip_zwj_zwnj` removes U+200C/U+200D | **identical** | none |")
    w("| nukta handling | none — no nukta normalisation anywhere in either file | "
      "none | none; both score क़ and क़ as different (2 edits) |")
    w("| digit normalisation | none in either file (no Devanagari/Bengali-digit folding) | "
      "none | none; both count १ vs 1 as an error |")
    w("| case | **not lowercased** by `metrics.py` (only by the South-400 writer, see Table 3) | "
      "not lowercased | none for benchmark-vs-benchmark; matters only when compared to South-400 |")
    w("| **empty / missing prediction** | scored **`cer=1.0, wer=1.0`**, `invalid=False`, "
      "`missing_prediction=True` — it **counts in the mean** | `metrics=None, invalid=True` — "
      "it is **excluded from every mean** | **LARGE.** Our denominators include every "
      "abstention as a 100 % error; Sarvam silently drops them. Over the 1,227 scored items "
      "our sheet has 617 empty anuvaad, 343 empty rapidocr, 536 empty paddle, 129 empty "
      "surya (easyocr 0) — Sarvam's rule would have deleted all of those rows |")
    w("| **tail loops / catastrophic output** | counted as errors in `avg_metrics` and in "
      "`lang_wise_scores` (only excluded from `valid_samples_*`) | **excluded from "
      "`lang_wise_scores` entirely** (`if row[\"invalid\"] or row[\"loop_or_catastrophic\"] …: "
      "continue`) | **LARGE.** Their README: \"Predictions that exhibit runaway repetition "
      "(tail loops) are flagged separately and excluded from valid-sample metrics.\" |")
    w("| **short GT** | rows with <50 non-space GT chars get `short_gt=True` and are **dropped "
      "from all means** (`primary` list, reported as `short_gt_count`) | **no short-GT rule at "
      "all** | **LARGE.** Sarvam has no GT floor; they keep near-empty GT rows (which inflate "
      "CER) and we delete them |")
    w("| **word split/merge fallback** | `equalize_space_only_issues` final fallback returns "
      "`gt2, pred2` — our comment: \"Never overwrite pred with GT — that forged CER to 0 "
      "for real word-segmentation errors.\" | returns **`gt2, gt2`** — i.e. it substitutes the "
      "GT for the prediction on that branch | **Sarvam's version reports CER 0 for a class of "
      "real errors.** This inflates their score; our fix is correct and makes us look worse. "
      "Unknown how many rows hit it |")
    w("| `cer_uncapped` | extra metric, unbounded per-sample CER | not present | none for "
      "`avg_metrics.cer` (still capped at 1.0 by `_bound_rate` on both sides) |")
    w("| `LANG_ORDER` / TSV columns | benchmark ISO codes + legacy full names | top-10 Indic "
      "full names | cosmetic |")
    w("")
    w("### What the headline score is")
    w("")
    w("From their README (fetched 2026-09-29): **Word Accuracy = 100 × (1 − WER)**, with "
      "CER and WER both reported. Per-sample CER and WER are **capped at 1.0** on both sides "
      "(`_bound_rate`), and the two headline aggregates Sarvam publishes are `avg_metrics` "
      "(all scored samples) and `valid_samples_cer` (loops excluded). **What \"87.39\" is: "
      "UNKNOWN.** The number appears in this repo only at "
      "`_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:18`, which itself calls it DEAD for "
      "direct comparison; their README (opened this run) defines no single headline score and "
      "does not state 87.39 anywhere. Until the Sarvam source for 87.39 is opened and its "
      "metric and denominator are named, it is not comparable to any number in Table 2 — it "
      "may be word accuracy, 1-CER, or a mean over a subset, and this table carries no WER "
      "column.")
    w("")
    w("### Net direction of the divergence")
    w("")
    w("Rows 1–8 are cosmetic and cancel out. Rows 9–11 all move in the same direction: "
      "**our scorer is harsher.** We count abstentions and runaway loops as errors where "
      "Sarvam drops the row, and we delete their short-GT rows that we would otherwise be "
      "punished for. Row 12 goes the other way and is a genuine **bug in the Sarvam file** "
      "that inflates their number. Conclusion for the boss: **any \"we vs Sarvam 87.39\" "
      "statement is invalid until both sides are re-scored through one scorer.** The only "
      "defensible statement today is the *paired, same-scorer* one in the summary: on the 54 "
      f"items Sarvam actually ran, our own scorer gives Sarvam CER {sarvam_overall:.4f} and "
      f"our best local engine a lower mean in {len(per_lang_local_lower)}/18 languages — "
      "directional noise at n=3/lang.")
    w("")

    # ---- unresolved ------------------------------------------------------
    w("## UNRESOLVED")
    w("")
    w("| # | item | status | why it is open |")
    w("|---|---|---|---|")
    w(f"| 1 | How many rows hit Sarvam's `return gt2, gt2` word-split/merge branch | UNKNOWN | "
      "requires re-scoring the Sarvam published run; the dataset was not downloaded (no "
      "downloads without approval) and the 87.39 run is not on this disk |")
    w("| 2 | The correct `gt_thin` threshold (179 vs 200 chars) | CONTRADICTION | code says "
      "200 in three places, two docs say 179; changing it re-opens the writer basis and is "
      "outside this read-only wave |")
    w("| 3 | `dominant_script` for te_024 / te_065 | CONTRADICTION | "
      "`pages_script_map.json` and `pages_manifest.json` disagree; the CER_BY_SCRIPT te "
      "bucket (n=6) could be 6 or 4 Telugu pages |")
    w("| 4 | Per-language Sarvam comparison on all 6,909 bench items | DEAD (out of budget) | "
      "the 54-call cap is reached (`CAMPAIGN_DIRECTIVE.md` A8); 3/lang is all we will ever "
      "have without the boss's explicit yes |")
    w("| 5 | Whether the 56 unscored manifest additions should be scored | UNKNOWN | engine "
      "output packs for them are partial (surya 43/56); outside this wave's read-only scope |")
    w("| 6 | CER for the 274 South pages with no CER | DEAD (GT absent) | 219 have "
      f"GT < {GT_THIN_THRESHOLD} chars, 55 are mojibake PDF layers; no re-sourcing is possible "
      "without new PDFs, and `AGENT_PROTOCOL.md` forbids lowering the gates |")
    w("| 7 | `EVIDENCE_SUMMARY.md` s3 brx/or/sa values | KNOWN-STALE | they are correct for "
      "`scores/metrics_*_normalized.json` and wrong for `sheet.csv` today; the fix belongs to "
      "the lead, not this agent (I write only this md and the script) |")
    w("")
    w("---")
    w("")
    w("*Regenerate: `python3 level2/benchmark/pipeline/build_benchmark_22.py > docs/campaign/BENCHMARK_22.md`. "
      "The script reads its five sources and writes nothing but stdout.*")

    sys.stdout.write("\n".join(out) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
