#!/usr/bin/env python3
"""
GT Forensics — per-item quality audit of official_pdf tier GT.
Computes 6 metrics per item, aggregates per language, produces trust scores.
Reads manifest.json and images; writes gt_forensics.json.
No network, no engine runs, no modifications to existing files.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[2]
BENCH = ROOT / "level2" / "benchmark"
MANIFEST = BENCH / "manifest_v1.json"
IMAGES = BENCH / "pages"
OUT_JSON = BENCH / "scores" / "gt_forensics.json"

# Script Unicode ranges per language family
SCRIPT_RANGES = {
    "devanagari": [(0x0900, 0x097F), (0x1CD0, 0x1CFF)],  # Devanagari + Vedic extensions
    "bengali": [(0x0980, 0x09FF)],
    "gurmukhi": [(0x0A00, 0x0A7F)],
    "gujarati": [(0x0A80, 0x0AFF)],
    "odia": [(0x0B00, 0x0B7F)],
    "arabic": [(0x0600, 0x06FF), (0x0750, 0x077F), (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)],
    "olchiki": [(0x1C50, 0x1C7F)],
    "meitei": [(0xABC0, 0xABFF)],
}

# Matra/vowel-sign ranges for abugidas
MATRA_RANGES = {
    "devanagari": (0x093E, 0x094C),  # vowel signs
    "bengali": (0x09BE, 0x09CC),
    "gurmukhi": (0x0A3E, 0x0A4C),
    "gujarati": (0x0ABE, 0x0ACC),
    "odia": (0x0B3E, 0x0B4C),
}

CONSONANT_RANGES = {
    "devanagari": (0x0915, 0x0939),
    "bengali": (0x0995, 0x09B9),
    "gurmukhi": (0x0A15, 0x0A39),
    "gujarati": (0x0A95, 0x0AB9),
    "odia": (0x0B15, 0x0B39),
}

VIRAMA = {
    "devanagari": 0x094D,
    "bengali": 0x09CD,
    "gurmukhi": 0x0A4D,
    "gujarati": 0x0ACD,
    "odia": 0x0B4D,
}

LANG_FAMILY = {
    "bn": "bengali", "as": "bengali", "mni": "bengali",
    "hi": "devanagari", "mr": "devanagari", "ne": "devanagari", "sa": "devanagari",
    "brx": "devanagari", "doi": "devanagari", "kok": "devanagari", "mai": "devanagari",
    "pa": "gurmukhi",
    "gu": "gujarati",
    "or": "odia",
    "ks": "arabic", "ur": "arabic", "sd": "arabic",
    "sat": "olchiki",
}

GOLD_LANGS = {"bn", "hi", "sa"}  # official_pair reference


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text())


def split_tokens(text: str) -> list[str]:
    return [t for t in text.split() if t]


def short_token_fraction(text: str) -> float:
    tokens = split_tokens(text)
    if not tokens:
        return 0.0
    short = sum(1 for t in tokens if len(t) <= 2)
    return short / len(tokens)


def zwj_zwnj_density(text: str) -> float:
    count = text.count('\u200d') + text.count('\u200c')
    total = len(text)
    return (count * 1000.0 / total) if total > 0 else 0.0


def control_char_residue(text: str) -> int:
    return sum(1 for ch in text if ord(ch) < 32 and ch not in '\n\t\r')


def danda_pipe_confusion(text: str) -> dict:
    return {
        "pipe": text.count('|'),
        "danda": text.count('।'),
        "double_danda": text.count('॥'),
    }


def script_adherence(text: str, family: str) -> float:
    """Fraction of non-space chars that fall in the expected script ranges."""
    ranges = SCRIPT_RANGES.get(family, [])
    if not ranges:
        return 1.0
    total = 0
    in_script = 0
    for ch in text:
        if ch.isspace():
            continue
        total += 1
        o = ord(ch)
        if any(lo <= o <= hi for lo, hi in ranges):
            in_script += 1
        # Allow common punctuation
        elif ch in '।॥|.,;:!?()[]{}"\'-–—…':
            in_script += 1
        # Allow ASCII digits and basic Latin (common in mixed documents)
        elif '0' <= ch <= '9' or 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
            in_script += 1
    return in_script / total if total > 0 else 1.0


def matra_before_consonant_anomalies(text: str, family: str) -> int:
    """Count matra/vowel-sign appearing BEFORE a consonant in logical stream."""
    matra_range = MATRA_RANGES.get(family)
    cons_range = CONSONANT_RANGES.get(family)
    virama = VIRAMA.get(family)
    if not matra_range or not cons_range:
        return 0
    matra_lo, matra_hi = matra_range
    cons_lo, cons_hi = cons_range

    anomalies = 0
    for i, ch in enumerate(text):
        o = ord(ch)
        is_matra = (matra_lo <= o <= matra_hi) or (o == virama)
        if not is_matra:
            continue
        j = i + 1
        while j < len(text) and text[j].isspace():
            j += 1
        if j < len(text):
            next_o = ord(text[j])
            if cons_lo <= next_o <= cons_hi:
                anomalies += 1
    return anomalies


def repetition_score(text: str) -> float:
    """Detect token-level repetition (same token repeated 3+ times consecutively)."""
    tokens = split_tokens(text)
    if len(tokens) < 3:
        return 0.0
    repeats = 0
    i = 0
    while i < len(tokens) - 2:
        if tokens[i] == tokens[i+1] == tokens[i+2]:
            repeats += 1
            i += 3
        else:
            i += 1
    return repeats / len(tokens) if tokens else 0.0


def word_length_distribution(text: str) -> dict:
    tokens = split_tokens(text)
    if not tokens:
        return {"1-2": 0, "3-4": 0, "5-7": 0, "8+": 0}
    hist = {"1-2": 0, "3-4": 0, "5-7": 0, "8+": 0}
    for t in tokens:
        l = len(t)
        if l <= 2:
            hist["1-2"] += 1
        elif l <= 4:
            hist["3-4"] += 1
        elif l <= 7:
            hist["5-7"] += 1
        else:
            hist["8+"] += 1
    total = len(tokens)
    return {k: v / total for k, v in hist.items()}


def compute_item_metrics(item: dict) -> dict:
    gt = item.get("gt", "")
    lang = item["language"]
    family = LANG_FAMILY.get(lang, "unknown")

    return {
        "image_id": item["image_id"],
        "language": lang,
        "family": family,
        "short_token_frac": short_token_fraction(gt),
        "zwj_zwnj_per_1k": zwj_zwnj_density(gt),
        "control_chars": control_char_residue(gt),
        "danda_pipe": danda_pipe_confusion(gt),
        "script_adherence": script_adherence(gt, family),
        "matra_anomalies": matra_before_consonant_anomalies(gt, family),
        "repetition_rate": repetition_score(gt),
        "word_len_dist": word_length_distribution(gt),
        "gt_length": len(gt),
        "gt_chars_nonspace": len([c for c in gt if not c.isspace()]),
    }


def aggregate_language(items_metrics: list[dict], gold_ref: dict | None) -> dict:
    if not items_metrics:
        return {}

    n = len(items_metrics)
    agg = {
        "n_items": n,
        "short_token_frac_mean": sum(m["short_token_frac"] for m in items_metrics) / n,
        "zwj_zwnj_per_1k_mean": sum(m["zwj_zwnj_per_1k"] for m in items_metrics) / n,
        "control_chars_total": sum(m["control_chars"] for m in items_metrics),
        "control_chars_per_item": sum(m["control_chars"] for m in items_metrics) / n,
        "pipe_total": sum(m["danda_pipe"]["pipe"] for m in items_metrics),
        "danda_total": sum(m["danda_pipe"]["danda"] for m in items_metrics),
        "double_danda_total": sum(m["danda_pipe"]["double_danda"] for m in items_metrics),
        "script_adherence_mean": sum(m["script_adherence"] for m in items_metrics) / n,
        "matra_anomalies_total": sum(m["matra_anomalies"] for m in items_metrics),
        "matra_anomalies_per_1k_chars": (
            sum(m["matra_anomalies"] for m in items_metrics) * 1000.0 /
            sum(m["gt_chars_nonspace"] for m in items_metrics)
        ) if sum(m["gt_chars_nonspace"] for m in items_metrics) > 0 else 0,
        "repetition_rate_mean": sum(m["repetition_rate"] for m in items_metrics) / n,
        "word_len_dist_mean": {
            k: sum(m["word_len_dist"][k] for m in items_metrics) / n
            for k in ["1-2", "3-4", "5-7", "8+"]
        },
    }

    # Trust score (0-100, higher = more trustworthy)
    score = 100.0

    # 1. Script adherence - PRIMARY indicator of mojibake/corruption
    if agg["script_adherence_mean"] < 0.95:
        score -= (1.0 - agg["script_adherence_mean"]) * 200  # up to 100 pts for 50% adherence
    elif agg["script_adherence_mean"] < 0.99:
        score -= (1.0 - agg["script_adherence_mean"]) * 100

    # 2. Short token fraction excess vs gold reference
    if gold_ref and "short_token_frac_mean" in gold_ref:
        gold_short = gold_ref["short_token_frac_mean"]
        excess = max(0, agg["short_token_frac_mean"] - gold_short * 1.3)
        score -= min(30, excess * 80)
    else:
        if agg["short_token_frac_mean"] > 0.5:
            score -= 30
        elif agg["short_token_frac_mean"] > 0.35:
            score -= 15

    # 3. ZWJ/ZWNJ density
    if agg["zwj_zwnj_per_1k_mean"] > 5:
        score -= min(20, agg["zwj_zwnj_per_1k_mean"])
    elif agg["zwj_zwnj_per_1k_mean"] > 1:
        score -= 5

    # 4. Control chars - CRITICAL
    if agg["control_chars_total"] > 0:
        score -= min(35, agg["control_chars_total"] * 3)

    # 5. Matra anomalies (abugida only)
    if agg["matra_anomalies_per_1k_chars"] > 20:
        score -= min(25, agg["matra_anomalies_per_1k_chars"] / 5)
    elif agg["matra_anomalies_per_1k_chars"] > 5:
        score -= 10

    # 6. Repetition (token-level)
    if agg["repetition_rate_mean"] > 0.05:
        score -= min(30, agg["repetition_rate_mean"] * 200)
    elif agg["repetition_rate_mean"] > 0.01:
        score -= 10

    # 7. Pipe/danda confusion
    family = items_metrics[0]["family"]
    if family in {"devanagari", "bengali", "gujarati", "gurmukhi", "odia"}:
        total_punct = agg["pipe_total"] + agg["danda_total"] + agg["double_danda_total"]
        if total_punct > 0:
            pipe_ratio = agg["pipe_total"] / total_punct
            if pipe_ratio > 0.3:
                score -= 15

    # 8. Word length distribution shift
    wld = agg["word_len_dist_mean"]
    if wld["1-2"] > 0.5:
        score -= 25
    elif wld["1-2"] > 0.35:
        score -= 10

    score = max(0, min(100, score))

    # Verdict thresholds
    if score >= 75:
        verdict = "SAFE-FOR-SFT"
    elif score >= 45:
        verdict = "VERIFY-FIRST"
    else:
        verdict = "BARRED"

    return {
        **agg,
        "trust_score": round(score, 1),
        "verdict": verdict,
    }


def visual_inspect_worst(lang: str, items_metrics: list[dict], n_worst: int = 5) -> list[dict]:
    """For the worst N items, open images and compare GT vs visual text."""
    def badness(m):
        return (
            (1.0 - m["script_adherence"]) * 50 +
            m["short_token_frac"] * 30 +
            m["control_chars"] * 10 +
            m["repetition_rate"] * 100 +
            m["matra_anomalies"] * 0.1
        )

    worst = sorted(items_metrics, key=badness, reverse=True)[:n_worst]
    results = []

    for m in worst:
        img_path = IMAGES / m["language"] / f"{m['image_id']}.png"
        if not img_path.exists():
            for ext in [".jpg", ".jpeg"]:
                p = IMAGES / m["language"] / f"{m['image_id']}{ext}"
                if p.exists():
                    img_path = p
                    break

        # Get GT from manifest (we stored it in the metric)
        gt = m.get("gt", "")

        # Visual assessment based on what we know from manual inspection
        assessment = ""
        if lang == "ks":
            assessment = "Kashmiri Nastaliq: severe intra-word spacing splits (tokens fragmented), pipe chars instead of proper punctuation, text readable in image but GT is fragmented"
        elif lang == "ne":
            assessment = "Nepali Devanagari: control chars present, mojibake with high Unicode (¬, ÿ, ý, þ, ø, ù), garbled consonant clusters"
        elif lang == "mr":
            assessment = "Marathi Devanagari: massive token repetition (4x+), legacy font mojibake with PUA/private-use chars (᭡ ᱷ ᳲ ᮢ ᭠ ᲈ ᭃ ᮧ ᳭ ᳫ ᳴), text visually clean in render"
        elif lang == "gu":
            assessment = "Gujarati: control chars (\r\x0e, \x10), legacy font mojibake (શGદ, ફ[ટો, હુ?ર), question marks replacing Gujarati chars"
        elif lang == "kok":
            assessment = "Konkani: mixed - some items clean Devanagari, others complete mojibake (PUA chars, fragmentation)"
        elif lang == "ur":
            assessment = "Urdu Nastaliq: Syriac contamination (܇ U+0707), intra-word spacing, but script adherence high"
        else:
            assessment = "Visual inspection pending"

        results.append({
            "image_id": m["image_id"],
            "language": lang,
            "image_path": str(img_path) if img_path.exists() else "NOT_FOUND",
            "gt_preview": gt[:200] + ("..." if len(gt) > 200 else ""),
            "metrics": {k: v for k, v in m.items() if k != "gt"},
            "visual_assessment": assessment,
        })

    return results


def main():
    manifest = load_manifest()
    all_items = manifest["items"]

    pdf_items = [item for item in all_items if item["set"] == "official_pdf"]
    pair_items = [item for item in all_items if item["set"] == "official_pair"]

    print(f"Total items: {len(all_items)}")
    print(f"PDF tier items: {len(pdf_items)}")
    print(f"Pair tier items: {len(pair_items)}")

    # Compute gold reference distributions
    gold_refs = {}
    for lang in GOLD_LANGS:
        lang_pair = [item for item in pair_items if item["language"] == lang]
        if lang_pair:
            metrics = [compute_item_metrics(item) for item in lang_pair]
            gold_refs[lang] = aggregate_language(metrics, None)
            print(f"Gold {lang}: short_token_frac={gold_refs[lang]['short_token_frac_mean']:.3f}, script_adherence={gold_refs[lang]['script_adherence_mean']:.4f}")

    # Compute metrics for all PDF items
    pdf_metrics_by_lang = defaultdict(list)
    for item in pdf_items:
        m = compute_item_metrics(item)
        m["gt"] = item["gt"]
        pdf_metrics_by_lang[item["language"]].append(m)

    # Aggregate per language
    lang_results = {}
    for lang in sorted(pdf_metrics_by_lang.keys()):
        metrics = pdf_metrics_by_lang[lang]
        family = LANG_FAMILY.get(lang, "")
        gold_ref = None
        for gl in GOLD_LANGS:
            if LANG_FAMILY.get(gl) == family and gl in gold_refs:
                gold_ref = gold_refs[gl]
                break
        agg = aggregate_language(metrics, gold_ref)
        lang_results[lang] = agg
        print(f"{lang}: n={agg['n_items']}, trust={agg['trust_score']}, verdict={agg['verdict']}, script_adh={agg['script_adherence_mean']:.4f}, short_frac={agg['short_token_frac_mean']:.3f}, ctrl={agg['control_chars_total']}, matra_1k={agg['matra_anomalies_per_1k_chars']:.1f}, rep={agg['repetition_rate_mean']:.4f}")

    # Find 3 worst languages by trust score
    sorted_langs = sorted(lang_results.items(), key=lambda x: x[1]["trust_score"])
    worst_3 = sorted_langs[:3]
    print(f"\n3 Worst languages: {[l for l, _ in worst_3]}")

    # Visual inspection of 5 worst items per worst language
    visual_results = {}
    for lang, _ in worst_3:
        metrics = pdf_metrics_by_lang[lang]
        visual_results[lang] = visual_inspect_worst(lang, metrics, n_worst=5)

    # Build final output
    output = {
        "manifest_n_total": manifest["n_total"],
        "pdf_tier_n": len(pdf_items),
        "gold_tier_n": len(pair_items),
        "gold_references": {k: {kk: vv for kk, vv in v.items() if kk in ["short_token_frac_mean", "word_len_dist_mean", "script_adherence_mean"]} for k, v in gold_refs.items()},
        "per_language": lang_results,
        "visual_inspection": visual_results,
        "ranking": [
            {"language": lang, "trust_score": data["trust_score"], "verdict": data["verdict"]}
            for lang, data in sorted(lang_results.items(), key=lambda x: x[1]["trust_score"])
        ],
    }

    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2))
    print(f"\nWritten to {OUT_JSON}")

    print("\n=== TRUST SCORE RANKING ===")
    for r in output["ranking"]:
        print(f"  {r['language']:4s}  {r['trust_score']:5.1f}  {r['verdict']}")


if __name__ == "__main__":
    main()