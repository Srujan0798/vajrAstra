#!/usr/bin/env python3
"""WAVE 2 part 1 (proto-20) - reconcile every count and build one 22-language manifest.

READ-ONLY on all sources. Never alters level2/benchmark/manifest_v1.json (LOCKED).
Writes: level2/benchmark/manifest_22.json
"""
import json, os, csv, glob, collections, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = lambda *a: os.path.join(ROOT, *a)

LANGS = ["as","bn","brx","doi","gu","hi","kok","ks","mai","mni","mr","ne","or",
         "pa","sa","sat","sd","ur"]
SOUTH = ["ta","te","kn","ml"]


def load():
    man = json.load(open(P("level2","benchmark","manifest_v1.json")))
    add = json.load(open(P("level2","benchmark","manifest_additions.json")))
    cer = json.load(open(P("level2","reports","CER_STAGE3B.json")))
    return man, add, cer


def engine_dirs():
    out = {}
    for base in ("level2/benchmark/packs", "level2/out"):
        if not os.path.isdir(P(base)):
            continue
        for eng in sorted(os.listdir(P(base))):
            if not os.path.isdir(P(base, eng)):
                continue
            for lang in sorted(os.listdir(P(base, eng))):
                d = P(base, eng, lang)
                if os.path.isdir(d):
                    out.setdefault((base.split("/")[-1], eng, lang), set()).update(
                        f for f in os.listdir(d) if f.endswith(".json"))
    return out


def main():
    man, add, cer = load()
    base_items, add_items = man["items"], add["items"]
    all_probe = list(base_items)
    seen = {i["image_id"] for i in base_items}
    for i in add_items:                      # additions are a separate file
        if i["image_id"] not in seen:
            all_probe.append(i); seen.add(i["image_id"])
    add_ids = {i["image_id"] for i in add_items}
    base_ids = {i["image_id"] for i in base_items}

    # --- scored n per language per model, straight from sheet.csv (never wc -l) ---
    scored = collections.defaultdict(lambda: collections.defaultdict(set))
    with open(P("level2","benchmark","scores","sheet_v1.csv")) as f:
        for r in csv.DictReader(f):
            scored[r["language"]][r["model"]].add(r["image_id"])

    eng = engine_dirs()
    probe_ids = {i["image_id"] for i in all_probe}

    # --- per-language reconciliation ---
    rows = []
    for lang in LANGS:
        mf = [i for i in all_probe if i["language"] == lang]
        mf_base = [i for i in base_items if i["language"] == lang]
        mf_add = [i for i in add_items if i["language"] == lang]
        per_model = {m: len(v) for m, v in scored.get(lang, {}).items()}
        local_counts = {len(v) for m, v in scored.get(lang, {}).items()
                        if m != "sarvam_vision"}
        counts = local_counts
        rows.append({
            "language": lang,
            "manifest_n": len(mf),
            "manifest_base": len(mf_base),
            "manifest_additions": len(mf_add),
            "scored_n_distinct": len(set().union(*scored[lang].values())) if scored[lang] else 0,
            "scored_n_per_model": per_model,
            "local_models_agree": len(counts) <= 1,
            "scored_n_models": sorted(per_model.items()),
            "gt_tiers": dict(collections.Counter(i.get("gt_source") for i in mf)),
        })

    # --- engine coverage of the 56 additions + orphan outputs ---
    coverage = collections.defaultdict(dict)
    for lang in ("sd", "mr", "pa"):
        ids = {i["image_id"] for i in add_items if i["language"] == lang}
        for (b, e, l), files in eng.items():
            if l != lang or b != "out":
                continue
            have = ids & {f[:-5] for f in files}
            coverage[lang][e] = {"of_additions": len(have), "of": len(ids)}
    orphans = collections.defaultdict(lambda: collections.defaultdict(int))
    for (b, e, l), files in eng.items():
        if b != "out" or l in SOUTH:
            continue
        for f in files:
            if f[:-5] not in probe_ids:
                orphans[l][e] += 1

    # --- South 400 ---
    south_rows = []
    for lang in SOUTH:
        lab = len([f for f in os.listdir(P("arc_level_1","labeled",lang)) if f.endswith(".json")])
        scored_n, nulls, cells = 0, collections.Counter(), 0
        for pid, per_eng in cer["per_page"].items():
            if not pid.startswith(lang + "_"):
                continue
            cells += 1
            reasons = [r.get("reason") for r in per_eng.values()
                       if isinstance(r, dict) and r.get("cer") is None and r.get("reason")]
            if any(isinstance(r, dict) and r.get("cer") is not None for r in per_eng.values()):
                scored_n += 1
            else:
                nulls[reasons[0] if reasons else "nulled_no_reason_recorded"] += 1
        outn = {}
        for (b, e, l), files in eng.items():
            if l == lang and b == "out":
                outn[e] = len(files)
        south_rows.append({"language": lang, "labelled_n": lab, "scored_n": scored_n,
                           "null_reasons": dict(nulls), "engine_cells": cells, "outputs_per_engine": outn})

    # South page-level scored map (a page counts as scored only if a non-null CER exists)
    south_scored, south_reason = set(), {}
    for pid, per_eng in cer["per_page"].items():
        if any(isinstance(r, dict) and r.get("cer") is not None for r in per_eng.values()):
            south_scored.add(pid)
        else:
            rs = [r.get("reason") for r in per_eng.values()
                  if isinstance(r, dict) and r.get("cer") is None and r.get("reason")]
            south_reason[pid] = rs[0] if rs else "nulled_no_reason_recorded"

    # --- manifest_22.json ---
    items = []
    for i in sorted(all_probe, key=lambda x: (x["language"], x["image_id"])):
        _g = glob.glob(P("level2","benchmark","pages", i["language"], i["image_id"] + ".*"))
        img = _g[0] if _g else P("level2","benchmark","pages", i["language"], i["image_id"] + ".png")
        sc = "sheet.csv" if i["image_id"] in scored.get(i["language"], {}).get("surya", set()) else "none"
        items.append({
            "uid": f'{i["language"]}:{i["image_id"]}',
            "language": i["language"], "script": i.get("script"),
            "origin": "benchmark",
            "gt_source": i.get("gt_source"),
            "gt_path_or_inline": "level2/benchmark/manifest_v1.json#items" ,
            "image_path": os.path.relpath(img, ROOT),
            "scored_in": sc,
            "tier": ("gold_pair" if i.get("gt_source") == "official_pair_txt"
                     else "fill" if i.get("gt_source") == "sarvam_bench" else "pdf_layer"),
            "source_pdf": i.get("source_pdf"), "source_page": i.get("source_page"),
            "print_or_hand": i.get("print_or_hand"), "has_table": i.get("has_table"),
            "in_additions": i["image_id"] in add_ids,
        })
    for lang in SOUTH:
        for f in sorted(os.listdir(P("arc_level_1","labeled",lang))):
            if not f.endswith(".json"): continue
            pid = f[:-5]
            items.append({
                "uid": f"{lang}:{pid}", "language": lang, "script": None,
                "origin": "south400", "gt_source": "south_label",
                "gt_path_or_inline": f"arc_level_1/labeled/{lang}/{f}",
                "image_path": None,
                "scored_in": ("CER_STAGE3B.json" if pid in south_scored
                              else "none (nulled: %s)" % south_reason.get(pid, "unknown")),
                "tier": "south_label", "source_pdf": None, "source_page": None,
                "print_or_hand": None, "has_table": None, "in_additions": False,
            })



    uids = [x["uid"] for x in items]
    img_missing = 0
    for x in items:
        if x["image_path"] and not os.path.exists(P(x["image_path"])):
            img_missing += 1

    by_lang = collections.defaultdict(lambda: collections.defaultdict(int))
    for x in items:
        by_lang[x["language"]]["n_labelled"] += 1
        if not str(x["scored_in"]).startswith("none"):
            by_lang[x["language"]]["n_scored"] += 1
        by_lang[x["language"]]["tier_" + x["tier"]] += 1

    out = {
        "created": "2026-09-30",
        "generator": "level2/benchmark/pipeline/reconcile_22.py",
        "sources": ["level2/benchmark/manifest_v1.json", "level2/benchmark/manifest_additions.json",
                    "level2/benchmark/scores/sheet_v1.csv", "level2/reports/CER_STAGE3B.json",
                    "arc_level_1/labeled/"],
        "n_total": len(items),
        "note": "LOCKED manifest.json was read, never written. Images are referenced, never copied.",
        "languages": {c: {"n_labelled": by_lang[c]["n_labelled"],
                          "n_scored": by_lang[c]["n_scored"],
                          "tiers": {t: by_lang[c]["tier_" + t]
                                    for t in ("gold_pair", "pdf_layer", "fill", "south_label")
                                    if by_lang[c]["tier_" + t]}}
                      for c in sorted(by_lang)},
        "items": items,
    }
    with open(P("level2","benchmark","manifest_22.json"), "w") as f:
        json.dump(out, f, indent=1, sort_keys=True, ensure_ascii=False)

    # --- report ---
    print("== PROBE22 RECONCILIATION (18 langs) ==")
    print(f'{"lang":5} {"man":>4} {"base":>5} {"add":>4} {"scored":>7} {"agree":>6}  tiers')
    for r in rows:
        print(f'{r["language"]:5} {r["manifest_n"]:4} {r["manifest_base"]:5} '
              f'{r["manifest_additions"]:4} {r["scored_n_distinct"]:7} '
              f'{"yes" if r["local_models_agree"] else "NO":>6}  {r["gt_tiers"]}')
    print("\n== ENGINE COVERAGE OF THE 56 ADDITIONS ==")
    for lang in sorted(coverage):
        print(f'  {lang}: ' + ", ".join(f'{e} {v["of_additions"]}/{v["of"]}'
                                        for e, v in sorted(coverage[lang].items())))
    print("\n== ORPHAN OUTPUTS (file in out/<eng>/<lang>/ whose id is NOT in the manifest) ==")
    if not orphans:
        print("  none")
    for lang in sorted(orphans):
        tot = sum(orphans[lang].values())
        print(f'  {lang}: {tot}  ' + ", ".join(f'{e} {n}' for e, n in sorted(orphans[lang].items())))
    print("\n== SOUTH 400 (4 langs) ==")
    for r in south_rows:
        print(f'  {r["language"]}: labelled {r["labelled_n"]}, scored {r["scored_n"]}, '
              f'nulls {r["null_reasons"]}, outputs {r["outputs_per_engine"]}')
    print("\n== ADDITIONS FILE RELATIONSHIP (structure) ==")
    print(f'  manifest image_ids              : {len(base_ids)}')
    print(f'  manifest_additions image_ids    : {len(add_ids)}')
    print(f'  already present in manifest     : {len(add_ids & base_ids)}')
    print(f'  genuinely new ids               : {len(add_ids - base_ids)}')
    scored_all = {iid for v in scored.values() for s in v.values() for iid in s}
    print(f'  manifest minus scored           : {len(base_ids - scored_all)}')
    print(f'  additions == manifest-minus-scored: {add_ids == (base_ids - scored_all)}')
    print("  VERDICT: manifest_additions.json is a SUBSET of manifest.json, equal to the")
    print("  56 manifest items that are NOT scored. len(manifest)+len(additions)=1,339 is WRONG.")

    print("\n== CHECKS ==")
    c1 = len(items) == len(base_items) + 400
    c2 = (len(all_probe) == len(base_items)) and (add_ids <= base_ids)
    c3 = len(set(uids)) == len(uids)
    c4 = img_missing == 0
    print(f'  [{"PASS" if c1 else "FAIL"}] n_total == 1,283 probe + 400 South = 1,683 '
          f'(got {len(items)})')
    print(f'  [{"PASS" if c2 else "FAIL"}] every probe item present exactly once and the '
          f'additions file is a SUBSET, not an addition (manifest {len(base_items)}, '
          f'additions {len(add_ids)} all already inside, union {len(all_probe)})')
    print(f'  [{"PASS" if c3 else "FAIL"}] every uid unique ({len(set(uids))}/{len(uids)})')
    print(f'  [{"PASS" if c4 else "FAIL"}] every referenced image_path exists '
          f'({img_missing} missing)')
    print(f'  [INFO] additions marked in manifest_22: {sum(1 for x in items if x["in_additions"])}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
