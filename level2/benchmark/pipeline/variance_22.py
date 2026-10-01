#!/usr/bin/env python3
"""Wave 2 Part 2 (proto-21-w2-variance-and-resource): per-language variance evidence,
candidate pools for the 8 short languages, and re-source option math.

Read-only on every input: level2/benchmark/manifest_22.json (locked reconciliation, never
written by this script), level2/benchmark/pipeline/candidates/<code>.json, and
arc_level_1/labeled/<lang>/*.json (South GT, `source` field only). Prints markdown to stdout.
Closes CO-022 (first-page-only), CO-023 (one-paper/single-source), CO-024 (clustered)
with measured evidence. Honesty gates live at level2/benchmark/pipeline/extract_gt.py:66-69
(MIN_CHARS=50, MIN_SCRIPT_RATIO=0.5, MAX_LATIN_RATIO=0.6, MAX_CTRL_CHARS=3) and are
never relaxed or re-implemented here.

Run:  python3 level2/benchmark/pipeline/variance_22.py
"""
import json
import os
import re
import statistics
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFEST = os.path.join(ROOT, "level2", "benchmark", "manifest_22.json")
CAND_DIR = os.path.join(ROOT, "level2", "benchmark", "pipeline", "candidates")
SOUTH_LABELED = os.path.join(ROOT, "arc_level_1", "labeled")
OFFICIAL = os.path.join(ROOT, "Datasets", "akshardrishti_official")

SHORT = ["as", "mni", "sat", "gu", "doi", "ne", "brx", "or"]          # manifest n < 100
CONCENTRATED = ["kok", "pa", "ur", "ks"]                              # re-draw proposals
LANG_DIR_NAME = {  # manifest code -> Datasets/akshardrishti_official/<Language>/
    "as": "Assamese", "mni": "Manipuri", "sat": "Santali", "gu": "Gujarati",
    "doi": "Dogri", "ne": "Nepali", "brx": "Bodo", "or": "Odia",
    "kok": "Konkani", "pa": "Punjabi", "ur": "Urdu", "ks": "Kashmiri",
}
PAIR_DIR_HINT = "Images and Tran"


def pct(sorted_vals, p):
    """Nearest-rank percentile of an already-sorted list."""
    if not sorted_vals:
        return None
    k = max(0, min(len(sorted_vals) - 1, round(p / 100 * (len(sorted_vals) - 1))))
    return sorted_vals[k]


def fmt5(vals):
    if not vals:
        return "-"
    s = sorted(vals)
    return "/".join(str(pct(s, p)) for p in (0, 25, 50, 75, 100))


def pair_target(image_path):
    """Symlink target basename for gold_pair images (os.readlink); falls back to path."""
    if image_path and os.path.islink(image_path):
        return os.path.basename(os.readlink(image_path))
    return os.path.basename(image_path) if image_path else "inline"


def south_gt_meta(gt_path):
    """Read one South GT json (read-only) for its `source` and `page_id` fields."""
    if gt_path and os.path.isfile(gt_path):
        with open(gt_path) as fh:
            g = json.load(fh)
        return g.get("source") or "unknown", g.get("page_id")
    return "unknown", None


def load_manifest():
    with open(MANIFEST) as fh:
        data = json.load(fh)
    by_lang = defaultdict(list)
    for it in data["items"]:
        by_lang[it["language"]].append(it)
    return data, by_lang


def variance_row(rows):
    """Compute one language's variance evidence across its tiers."""
    n = len(rows)
    docs, pages, offsets, ids, sources = Counter(), set(), [], [], Counter()
    for it in rows:
        tier = it["tier"]
        if tier == "pdf_layer":
            docs[it["source_pdf"]] += 1
            if it["source_page"] is not None:
                pages.add((it["source_pdf"], it["source_page"]))
                offsets.append(it["source_page"])
        elif tier == "gold_pair":
            tgt = pair_target(it["image_path"])
            docs[tgt] += 1
            pages.add(tgt)
            m = re.search(r"(\d+)", tgt)
            if m:
                ids.append(int(m.group(1)))
        elif tier == "south_label":
            src, page_id = south_gt_meta(it.get("gt_path_or_inline"))
            docs[src] += 1
            sources[src] += 1
            if page_id:
                pages.add(page_id)
        else:  # fill (sarvam_bench)
            docs["sarvam_bench"] += 1
            pages.add(it["image_path"])
    top1_share = (max(docs.values()) / n) if docs else 0.0
    page_le1 = sum(1 for o in offsets if o <= 1)
    return {
        "n": n,
        "tiers": dict(Counter(it["tier"] for it in rows)),
        "distinct_docs": len(docs),
        "top1_share": top1_share,
        "distinct_pages": len(pages),
        "offsets": offsets,
        "page_le1": page_le1,
        "ids": ids,
        "sources": dict(sources),
    }


def flags(row):
    flags = []
    if row["top1_share"] > 0.5:
        flags.append("clustered")
    if row["offsets"] and row["page_le1"] / len(row["offsets"]) > 0.2:
        flags.append("first-page-bias")
    if row["distinct_docs"] == 1:
        flags.append("single-source")
    return flags or ["none"]


def verdicts(row, name):
    """Verdict on the three forbidden shortcuts, with the numbers."""
    n = row["n"]
    le1_share = (row["page_le1"] / len(row["offsets"])) if row["offsets"] else None
    le1_txt = f"{row['page_le1']}/{len(row['offsets'])} ({le1_share:.0%})" if le1_share is not None else "n/a"

    if le1_share is None:
        v_first = "N/A (no page offsets in manifest)"
    elif le1_share > 0.2:
        v_first = f"CONFIRMED (page<=1 {le1_txt})"
    elif le1_share > 0:
        v_first = f"PARTIAL (page<=1 {le1_txt}, under 20% flag line)"
    else:
        v_first = "DISPROVEN (page<=1 0)"

    if row["distinct_docs"] == 1:
        v_one = f"CONFIRMED (1 source: {list(row['sources'] or ['sarvam_bench'])[0]})"
    elif row["top1_share"] > 0.5:
        v_one = f"PARTIAL ({row['distinct_docs']} docs, top-1 {row['top1_share']:.0%})"
    else:
        v_one = f"DISPROVEN ({row['distinct_docs']} docs, top-1 {row['top1_share']:.0%})"

    if row["top1_share"] > 0.5:
        v_clust = f"CONFIRMED (top-1 doc share {row['top1_share']:.0%} > 50%)"
    elif row["distinct_docs"] <= 3:
        v_clust = f"PARTIAL ({row['distinct_docs']} docs only, top-1 {row['top1_share']:.0%})"
    else:
        v_clust = f"DISPROVEN ({row['distinct_docs']} docs, top-1 {row['top1_share']:.0%})"
    return v_first, v_one, v_clust


def candidate_pool(code, drawn_pairs):
    path = os.path.join(CAND_DIR, f"{code}.json")
    if not os.path.isfile(path):
        return None
    with open(path) as fh:
        d = json.load(fh)
    cands = d.get("items", [])
    clean = len(cands) if isinstance(cands, list) else d.get("candidates", 0)
    cand_pdfs = sorted({c["pdf"] for c in cands}) if isinstance(cands, list) else []
    drawn = sum(1 for c in cands if (c["pdf"], c["page"]) in drawn_pairs) if isinstance(cands, list) else 0
    return {
        "pdfs": d.get("pdfs"), "pages_scanned": d.get("pages_scanned"),
        "pages_with_text": d.get("pages_with_text"),
        "rej_moji": d.get("rejected_mojibake_or_wrong_script"),
        "rej_short": d.get("rejected_short_or_latin"),
        "clean": clean, "cand_pdfs": cand_pdfs, "drawn": drawn,
        "remaining": clean - drawn, "pdf_errors": d.get("pdf_errors"),
    }


def official_pairs(code):
    """Count image+transcription pairs under the official dir (read-only listing).
    A transcription pair = image whose sibling .txt exists, or XML carrying <Unicode>
    text (Nepali's XMLs are Pascal-VOC bbox annotations with no text — counted out)."""
    base = os.path.join(OFFICIAL, LANG_DIR_NAME.get(code, ""))
    if not os.path.isdir(base):
        return 0, 0
    pairs = images = 0
    for dirpath, _, files in os.walk(base):
        names = set(files)
        for f in names:
            low = f.lower()
            if not low.endswith((".jpg", ".jpeg", ".png")):
                continue
            images += 1
            stem = f.rsplit(".", 1)[0]
            if f"{stem}.txt" in names:
                pairs += 1
            elif f"{stem}.xml" in names:
                xml_path = os.path.join(dirpath, f"{stem}.xml")
                with open(xml_path, encoding="utf-8", errors="replace") as fh:
                    if "<Unicode>" in fh.read():
                        pairs += 1
    return pairs, images


def stratified_redraw(rows, threshold=0.3):
    """How many items a stratified re-draw would replace.
    - strict: items in docs over the per-document share threshold (30% cap), plus page<=1
      items (page<=1 excluded from any redraw). Not always achievable — a 2-doc pool can
      never get under 50% per document.
    - achievable: rebalance to the floor imposed by the number of available documents
      (ceil(n / distinct_docs)), plus page<=1 items."""
    docs = Counter()
    le1_docs = Counter()
    for it in rows:
        if it["tier"] != "pdf_layer":
            return None, None
        key = it["source_pdf"]
        docs[key] += 1
        if it["source_page"] is not None and it["source_page"] <= 1:
            le1_docs[key] += 1
    n = len(rows)
    le1 = sum(le1_docs.values())
    over = {doc: c for doc, c in docs.items() if c / n > threshold}
    over_keep = max(0, max(over.values()) - round(threshold * n)) if over else 0
    strict = sum(over.values()) - over_keep + le1
    floor = -(-n // len(docs))  # ceil
    achievable = sum(max(0, c - floor) for c in docs.values()) + le1
    detail = {"over_share_docs": {os.path.basename(d): c for d, c in over.items()},
              "page_le1": le1, "threshold": threshold, "docs_available": len(docs),
              "floor": floor, "strict": strict, "achievable": achievable}
    return strict, detail


def main():
    data, by_lang = load_manifest()
    print(f"# variance_22.py output — generated {data.get('created')}, manifest n_total={data.get('n_total')}")
    print(f"# gates: level2/benchmark/pipeline/extract_gt.py:66-69 MIN_CHARS=50 MIN_SCRIPT_RATIO=0.5 MAX_LATIN_RATIO=0.6 MAX_CTRL_CHARS=3\n")

    # ---- 1+2. variance table + shortcut verdicts (all 22) ----
    print("## Variance table (all 22 languages)\n")
    print("| lang | n | tiers | distinct docs | top-1 share | distinct pages | page offsets min/q25/med/q75/max | page<=1 share | pair id min/med/max | flags |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    rows_by_lang = {}
    for lang in sorted(by_lang):
        row = variance_row(by_lang[lang])
        rows_by_lang[lang] = row
        tiers = "+".join(f"{k}:{v}" for k, v in sorted(row["tiers"].items()))
        off = fmt5(row["offsets"])
        le1 = (f"{row['page_le1']}/{len(row['offsets'])} ({row['page_le1']/len(row['offsets']):.0%})"
               if row["offsets"] else "-")
        idspread = fmt5(row["ids"]) if row["ids"] else "-"
        print(f"| {lang} | {row['n']} | {tiers} | {row['distinct_docs']} | {row['top1_share']:.0%} | "
              f"{row['distinct_pages']} | {off} | {le1} | {idspread} | {','.join(flags(row))} |")

    print("\n## Shortcut verdicts (CO-022 first-page-only / CO-023 one-paper-single-source / CO-024 clustered)\n")
    print("| lang | first-page-only | one-paper/single-source | clustered |")
    print("|---|---|---|---|")
    for lang in sorted(rows_by_lang):
        vf, vo, vc = verdicts(rows_by_lang[lang], lang)
        print(f"| {lang} | {vf} | {vo} | {vc} |")

    south = {lang: rows_by_lang[lang]["sources"] for lang in ("kn", "ml", "ta", "te") if lang in rows_by_lang}
    print("\n## South sources distribution (from arc_level_1/labeled/<lang>/*.json `source` field)\n")
    for lang, dist in sorted(south.items()):
        print(f"- {lang}: " + ", ".join(f"{k}={v}" for k, v in sorted(dist.items())))

    # ---- 3+4. candidate pools + re-source options ----
    print("\n## Candidate pools (8 short languages) + re-source options\n")
    total_remaining = 0
    for code in SHORT:
        drawn_pairs = {(it["source_pdf"], it["source_page"]) for it in by_lang.get(code, [])
                       if it["tier"] == "pdf_layer"}
        pool = candidate_pool(code, drawn_pairs)
        pairs, images = official_pairs(code)
        used_pairs = sum(1 for it in by_lang.get(code, []) if it["tier"] == "gold_pair")
        n = rows_by_lang[code]["n"]
        if pool is None:
            print(f"- {code}: NO candidates/<code>.json on disk")
            continue
        total_remaining += max(0, pool["remaining"])
        why = {
            "as": "PDF text layers fail gates (898 mojibake + 1600 short/Latin); 11 clean pages all from 1 PDF",
            "mni": "PDF text layers fail gates (689 mojibake + 664 short/Latin); 0 clean of 1353 with text",
            "sat": "NO text layer at all (0 of 207 pages with text); 3 PDFs image-only",
            "gu": "Legacy font encodings: 3,486 of 3,567 text pages rejected as mojibake; 10 clean all from 1 PDF",
            "doi": "Only 11 of 446 pages carry any text layer; 7 clean (3 PDFs), all drawn",
            "ne": "Only 464 of 4,146 pages have text; 411 mojibake rejections; 17 clean all from 1 PDF (PDF-tier BARRED, A8/R5)",
            "brx": "Text layers fail gates (886 mojibake + 1495 short/Latin); 47 clean (7 PDFs), all drawn",
            "or": "Text layers fail gates (74 mojibake + 1508 short/Latin); 50 clean (1 PDF), all drawn",
        }[code]
        opts = []
        if pool["remaining"] > 0:
            opts.append(f"(a) +{pool['remaining']} from remaining clean candidates")
        if pairs - used_pairs > 0:
            opts.append(f"(b) {pairs - used_pairs} unused official image+transcription pairs (of {pairs})")
        if not opts:
            opts.append("(c) nothing available -> accept low-n with permanent caveat")
        print(f"- {code} (n={n}): pdfs={pool['pdfs']} scanned={pool['pages_scanned']} with_text={pool['pages_with_text']} "
              f"rej(moji/short)={pool['rej_moji']}/{pool['rej_short']} clean={pool['clean']} "
              f"cand_pdfs={len(pool['cand_pdfs'])} drawn={pool['drawn']} remaining={pool['remaining']} "
              f"official_pairs={pairs} (used {used_pairs}); why short: {why}; options: {'; '.join(opts)}")
    print(f"\nTotal closable from remaining clean candidates alone: +{total_remaining} items "
          f"(need 517 to reach 100 x 22 -> not closable from PDFs alone)")

    # ---- concentrated re-draw proposals ----
    print("\n## Stratified re-draw proposals (kok, pa, ur, ks) — PROPOSALS ONLY, boss decision U5\n")
    for code in CONCENTRATED:
        replaced, detail = stratified_redraw(by_lang[code])
        if detail is None:
            print(f"- {code}: not a pdf_layer language, no re-draw applicable")
            continue
        pool_c = candidate_pool(code, set())
        print(f"- {code} (n={rows_by_lang[code]['n']}): strict-30%-cap re-draw replaces {replaced} items, "
              f"achievable rebalance (floor {detail['floor']}/doc with {detail['docs_available']} docs available) "
              f"replaces {detail['achievable']} items, page<=1 excluded {detail['page_le1']}; "
              f"over-share docs {detail['over_share_docs']}; candidate pool: {pool_c['clean'] if pool_c else 0} clean pages, "
              f"{len(pool_c['cand_pdfs']) if pool_c else 0} PDFs")

    print("\n# end variance_22.py")


if __name__ == "__main__":
    main()
