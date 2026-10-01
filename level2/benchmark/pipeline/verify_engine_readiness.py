#!/usr/bin/env python3
"""Pre-flight check: model availability per engine vs manifest langs.

Verdict Agent deliverable A. Reads manifest.json + per-engine cache locations
and emits status report: GREEN (cache healthy), YELLOW (sparse), RED (missing).
RED engines dispatch to Engine Agent anyway and produce honest-empty by design.
"""
import json
from datetime import datetime
from pathlib import Path

MANIFEST = Path('/Users/srujansai/Desktop/South/level2/benchmark/manifest_v1.json')
OUTPUT = Path('/Users/srujansai/Desktop/South/level2/benchmark/logs/engine_readiness.json')
ENV_FILE = Path('/Users/srujansai/Desktop/South/.env')

ENGINE_CACHES = {
    'rapidocr':            Path.home() / '.cache/huggingface/hub',
    'paddleocr_indic':     Path.home() / '.paddleocr/models',
    'easyocr':             Path.home() / '.EasyOCR/model',
    'tesseract_indic':     Path('/Users/srujansai/Desktop/South/level2/benchmark/pipeline/tessdata'),
    'tesseract_bilingual': Path('/Users/srujansai/Desktop/South/level2/benchmark/pipeline/tessdata'),
    'anuvaad_tesseract':   Path('/Users/srujansai/Desktop/South/.deps/IndicPhotoOCR'),
    'doctr':               Path.home() / '.cache/doctr',
    'indicphotoocr':       Path('/Users/srujansai/Desktop/South/.deps/IndicPhotoOCR'),
    'openbharatocr':       Path('/Users/srujansai/Desktop/South/level2/benchmark/pipeline/tessdata'),
    'surya':               Path.home() / '.cache/huggingface/hub',
}

GREEN_FILE_THRESHOLD = 5


def check_cache(p: Path) -> tuple:
    if not p.exists():
        return ('RED', f'missing: {p}', 0)
    n = sum(1 for x in p.rglob('*') if x.is_file())
    if n == 0:
        return ('RED', 'empty cache dir', 0)
    if n < GREEN_FILE_THRESHOLD:
        return ('YELLOW', f'sparse cache ({n} files)', n)
    return ('GREEN', 'cache healthy', n)


def check_sarvam() -> tuple:
    if not ENV_FILE.exists():
        return ('RED', 'no .env file', 0)
    text = ENV_FILE.read_text(encoding='utf-8', errors='replace')
    if 'SARVAM_API_KEY=' not in text:
        return ('RED', 'no SARVAM_API_KEY= in .env', 0)
    has_value = any(
        line.startswith('SARVAM_API_KEY=') and len(line.split('=', 1)[1].strip()) > 0
        for line in text.splitlines()
    )
    return ('GREEN' if has_value else 'YELLOW', 'SARVAM_API_KEY present' if has_value else 'key value empty', 1 if has_value else 0)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    items = manifest.get('items', [])
    langs = sorted({item['language'] for item in items if 'language' in item})

    readiness = {}
    for eng, cache in ENGINE_CACHES.items():
        status, note, n = check_cache(cache)
        readiness[eng] = {'status': status, 'note': note, 'files': n, 'cache': str(cache)}

    sarvam_status, sarvam_note, sarvam_n = check_sarvam()
    readiness['sarvam_vision'] = {
        'status': sarvam_status,
        'note': sarvam_note,
        'files': sarvam_n,
        'cache': str(ENV_FILE),
    }

    summary = {
        'GREEN': sum(1 for e in readiness.values() if e['status'] == 'GREEN'),
        'YELLOW': sum(1 for e in readiness.values() if e['status'] == 'YELLOW'),
        'RED': sum(1 for e in readiness.values() if e['status'] == 'RED'),
    }

    output = {
        'timestamp': datetime.now().isoformat(),
        'manifest_items': len(items),
        'manifest_languages': len(langs),
        'langs': langs,
        'engine_readiness': readiness,
        'summary': summary,
        'policy': (
            'Engine Agent dispatches ALL 11 engines regardless of readiness. '
            'RED engines yield honest-empty outputs, not failures. YELLOW engines '
            'may complete with partial coverage; Engine Agent must report counts.'
        ),
        'law': '§6.4 benchmark verdicts LOCKED; §9 evidence law applied.',
    }
    OUTPUT.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
    print(
        f'Wrote {OUTPUT}: GREEN={summary["GREEN"]} YELLOW={summary["YELLOW"]} RED={summary["RED"]}'
    )


if __name__ == '__main__':
    main()
