#!/usr/bin/env python3
"""Spot-check engine output: non-empty, plausible structure, resolvable lang.

Verdict Agent deliverable B. Used by Verdict after each engine completion.
Resolves `lang` from manifest.json by image_id (preds files carry image_id only).
"""
import json
import random
import sys
from pathlib import Path

ROOT = Path('/Users/srujansai/Desktop/South/level2/benchmark')
PRED_DIR = ROOT / 'scores'
MANIFEST = ROOT / 'manifest_v1.json'

MIN_TEXT_LEN = 1
SAMPLE_SIZE = 3
RNG_SEED = 42


def load_lang_map() -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    return {item['image_id']: item.get('language', 'UNKNOWN') for item in manifest.get('items', [])}


def main(engine: str) -> None:
    pred_file = PRED_DIR / f'preds_{engine}.json'
    if not pred_file.exists():
        result = {'engine': engine, 'sample_size': 0, 'issues': [f'preds file missing: {pred_file}'], 'pass': False}
        out = PRED_DIR / f'{engine}_spotcheck.json'
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f'{engine}: FAIL (preds missing)')
        sys.exit(1)

    preds = json.loads(pred_file.read_text(encoding='utf-8'))
    if not isinstance(preds, list) or not preds:
        result = {'engine': engine, 'sample_size': 0, 'issues': ['preds file empty or not a list'], 'pass': False}
        out = PRED_DIR / f'{engine}_spotcheck.json'
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f'{engine}: FAIL (empty)')
        sys.exit(1)

    lang_map = load_lang_map()
    rng = random.Random(RNG_SEED)
    sample = rng.sample(preds, min(SAMPLE_SIZE, len(preds)))

    issues = []
    for p in sample:
        # preds files use `image_name`; it matches manifest `image_id` verbatim.
        key = p.get('image_id') or p.get('image_name') or '?'
        text = (p.get('text') or p.get('pred') or '').strip()
        if len(text) < MIN_TEXT_LEN:
            issues.append(f'{key}: empty or whitespace-only text')
        expected_lang = lang_map.get(key, 'UNKNOWN')
        declared_lang = p.get('language') or p.get('lang')
        if expected_lang == 'UNKNOWN':
            issues.append(f'{key}: not resolvable in manifest')
        elif declared_lang and declared_lang != expected_lang:
            issues.append(f'{key}: declared={declared_lang} manifest={expected_lang} (mismatch)')

    result = {
        'engine': engine,
        'sample_size': len(sample),
        'total_predictions': len(preds),
        'sample': [
            {
                'image_id': p.get('image_id') or p.get('image_name'),
                'expected_lang': lang_map.get(p.get('image_id') or p.get('image_name', ''), 'UNKNOWN'),
                'declared_lang': p.get('language') or p.get('lang'),
                'text_len': len((p.get('text') or p.get('pred') or '').strip()),
                'text_head': (p.get('text') or p.get('pred') or '').strip()[:60],
            }
            for p in sample
        ],
        'issues': issues,
        'pass': len(issues) == 0,
    }
    out = PRED_DIR / f'{engine}_spotcheck.json'
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
    status = 'PASS' if result['pass'] else f'FAIL ({len(issues)} issues)'
    print(f'{engine}: {status}')


if __name__ == '__main__':
    main(sys.argv[1])
