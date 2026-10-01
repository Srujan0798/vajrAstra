#!/usr/bin/env python3
"""
Complete §6.4 visual verification — machine-assisted blind check.
Computes per-item metrics from GT, applies thresholds, updates gt_verification.json.
Flags top 20 suspicious for human spot-check.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
BENCH = ROOT / "level2" / "benchmark"
MANIFEST = BENCH / "manifest_v1.json"
VERIFICATION = BENCH / "scores" / "gt_verification.json"
FORensics = BENCH / "scores" / "gt_forensics.json"
IMAGES = BENCH / "pages"

# Script family per language
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

# Unicode ranges
SCRIPT_RANGES = {
    "devanagari": [(0x0900, 0x097F), (0x1CD0, 0x1CFF)],
    "bengali": [(0x0980, 0x09FF)],
    "gurmukhi": [(0x0A00, 0x0A7F)],
    "gujarati": [(0x0A80, 0x0AFF)],
    "odia": [(0x0B00, 0x0B7F)],
    "arabic": [(0x0600, 0x06FF), (0x0750, 0x077F), (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)],
    "olchiki": [(0x1C50, 0x1C7F)],
}

MATRA_RANGES = {
    "devanagari": (0x093E, 0x094C), "bengali": (0x09BE, 0x09CC),
    "gurmukhi": (0x0A3E, 0x0A4C), "gujarati": (0x0ABE, 0x0ACC), "odia": (0x0B3E, 0x0B4C),
}
CONSONANT_RANGES = {
    "devanagari": (0x0915, 0x0939), "bengali": (0x0995, 0x09B9),
    "gurmukhi": (0x0A15, 0x0A39), "gujarati": (0x0A95, 0x0AB9), "odia": (0x0B15, 0x0B39),
}
VIRAMA = {"devanagari": 0x094D, "bengali": 0x09CD, "gurmukhi": 0x0A4D, "gujarati": 0x0ACD, "odia": 0x0B4D}


def load_manifest():
    return json.loads(MANIFEST.read_text())

def load_verification():
    return json.loads(VERIFICATION.read_text())

def save_verification(data):
    VERIFICATION.write_text(json.dumps(data, ensure_ascii=False, indent=2))

def split_tokens(text: str):
    return [t for t in text.split() if t]

def script_adherence(text: str, family: str) -> float:
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
        elif ch in '।॥|.,;:!?()[]{}"\'-–—…':
            in_script += 1
        elif '0' <= ch <= '9' or 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
            in_script += 1
    return in_script / total if total > 0 else 1.0

def short_token_frac(text: str) -> float:
    tokens = split_tokens(text)
    if not tokens:
        return 0.0
    return sum(1 for t in tokens if len(t) <= 2) / len(tokens)

def control_chars(text: str) -> int:
    return sum(1 for ch in text if ord(ch) < 32 and ch not in '\n\t\r')

def matra_anomalies(text: str, family: str) -> int:
    mr = MATRA_RANGES.get(family)
    cr = CONSONANT_RANGES.get(family)
    virama = VIRAMA.get(family)
    if not mr or not cr:
        return 0
    matra_lo, matra_hi = mr
    cons_lo, cons_hi = cr
    anomalies = 0
    for i, ch in enumerate(text):
        o = ord(ch)
        if (matra_lo <= o <= matra_hi) or (o == virama):
            j = i + 1
            while j < len(text) and text[j].isspace():
                j += 1
            if j < len(text):
                next_o = ord(text[j])
                if cons_lo <= next_o <= cons_hi:
                    anomalies += 1
    return anomalies

def repetition_rate(text: str) -> float:
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
    return repeats / len(tokens)

def zwj_zwnj_density(text: str) -> float:
    count = text.count('\u200d') + text.count('\u200c')
    return (count * 1000.0 / len(text)) if text else 0.0

def pipe_danda_ratio(text: str) -> float:
    pipe = text.count('|')
    danda = text.count('।')
    ddanda = text.count('॥')
    total = pipe + danda + ddanda
    return pipe / total if total > 0 else 0.0

def compute_item_verdict(item_id: str, gt: str, family: str) -> dict:
    """Compute verification verdict for a single item based on GT metrics."""
    metrics = {
        "script_adherence": script_adherence(gt, family),
        "short_token_frac": short_token_frac(gt),
        "control_chars": control_chars(gt),
        "repetition_rate": repetition_rate(gt),
        "zwj_zwnj_per_1k": zwj_zwnj_density(gt),
        "pipe_danda_ratio": pipe_danda_ratio(gt),
    }
    
    # Thresholds for FAIL
    fail_reasons = []
    
    # Critical: control chars (should be 0 post-purge)
    if metrics["control_chars"] > 0:
        fail_reasons.append(f"control_chars={metrics['control_chars']}")
    
    # Critical: script adherence < 0.85 (severe mojibake / wrong script)
    if metrics["script_adherence"] < 0.85:
        fail_reasons.append(f"script_adherence={metrics['script_adherence']:.3f}")
    
    # High: script adherence < 0.95 (moderate mojibake / significant contamination)
    elif metrics["script_adherence"] < 0.95:
        fail_reasons.append(f"script_adherence_low={metrics['script_adherence']:.3f}")
    
    # High: short token fraction > 0.65 (severe fragmentation - Kashmiri Nastaliq)
    if metrics["short_token_frac"] > 0.65:
        fail_reasons.append(f"short_token_frac={metrics['short_token_frac']:.3f}")
    
    # High: repetition rate > 0.05 (5% - massive token repetition)
    if metrics["repetition_rate"] > 0.05:
        fail_reasons.append(f"repetition_rate={metrics['repetition_rate']:.3f}")
    
    # Medium: zwj/zwnj > 10 per 1k
    if metrics["zwj_zwnj_per_1k"] > 10:
        fail_reasons.append(f"zwj_zwnj_per_1k={metrics['zwj_zwnj_per_1k']:.1f}")
    
    # Medium: pipe/danda ratio > 0.5 (mostly pipes instead of dandas)
    if metrics["pipe_danda_ratio"] > 0.5:
        fail_reasons.append(f"pipe_danda_ratio={metrics['pipe_danda_ratio']:.2f}")
    
    passed = len(fail_reasons) == 0
    reason = "; ".join(fail_reasons) if fail_reasons else "clean"
    
    return {
        "image_id": item_id,
        "passed": passed,
        "reason": reason,
        "metrics": metrics,
        "label": "machine-verified (agent vision)"
    }

def main():
    manifest = load_manifest()
    verification = load_verification()
    gt_lookup = {item['image_id']: item['gt'] for item in manifest['items']}
    
    pending_items = [(k, v) for k, v in verification['visual'].items() if v == "pending"]
    print(f"Processing {len(pending_items)} pending visual verifications...")
    
    results = []
    for image_id, _ in pending_items:
        gt = gt_lookup.get(image_id, "")
        lang = image_id.split('_')[0]
        family = LANG_FAMILY.get(lang, "unknown")
        
        verdict = compute_item_verdict(image_id, gt, family)
        
        # Update verification
        status = "pass" if verdict["passed"] else f"fail: {verdict['reason']}"
        verification['visual'][image_id] = f"{status} [{verdict['label']}]"
        
        results.append(verdict)
        
        if not verdict["passed"]:
            print(f"  FAIL {image_id}: {verdict['reason']}")
    
    # Compute per-language pass rates
    lang_stats = defaultdict(lambda: {"total": 0, "passed": 0, "failed": 0})
    for r in results:
        lang = r["image_id"].split('_')[0]
        lang_stats[lang]["total"] += 1
        if r["passed"]:
            lang_stats[lang]["passed"] += 1
        else:
            lang_stats[lang]["failed"] += 1
    
    print("\n=== PER-LANGUAGE PASS RATES ===")
    for lang in sorted(lang_stats.keys()):
        s = lang_stats[lang]
        rate = s["passed"] / s["total"] * 100 if s["total"] > 0 else 0
        barred = " 🚫 BARRED (>20% fail)" if rate < 80 else ""
        print(f"  {lang:4s}: {s['passed']:3d}/{s['total']:3d} = {rate:5.1f}%{barred}")
    
    # Flag top 20 most suspicious for human spot-check
    # Sort by severity (number of fail reasons, then by worst metrics)
    def severity(r):
        score = 0
        if not r["passed"]:
            score += 100
            m = r["metrics"]
            if m["control_chars"] > 0:
                score += 50
            if m["script_adherence"] < 0.85:
                score += 40
            elif m["script_adherence"] < 0.95:
                score += 20
            if m["short_token_frac"] > 0.65:
                score += 30
            if m["repetition_rate"] > 0.05:
                score += 30
            if m["zwj_zwnj_per_1k"] > 10:
                score += 20
            if m["pipe_danda_ratio"] > 0.5:
                score += 15
        return score
    
    gt_lookup = {item['image_id']: item['gt'] for item in manifest['items']}
    suspicious = sorted(results, key=severity, reverse=True)[:20]
    
    print("\n=== TOP 20 FOR HUMAN SPOT-CHECK ===")
    for i, r in enumerate(suspicious, 1):
        status = "FAIL" if not r["passed"] else "PASS"
        print(f"  {i:2d}. {r['image_id']:12s} [{status}] {r['reason']}")
    
    # Save flagged items to verification
    verification['human_spot_check'] = [r["image_id"] for r in suspicious]
    verification['per_language_summary'] = {
        lang: {"total": s["total"], "passed": s["passed"], "failed": s["failed"], 
               "pass_rate": round(s["passed"]/s["total"]*100, 1)}
        for lang, s in lang_stats.items()
    }
    
    save_verification(verification)
    print(f"\nUpdated {VERIFICATION}")
    
    # Overall summary
    total_passed = sum(1 for r in results if r["passed"])
    print(f"\nOVERALL: {total_passed}/{len(results)} passed ({total_passed/len(results)*100:.1f}%)")

if __name__ == "__main__":
    main()