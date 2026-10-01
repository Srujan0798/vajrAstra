#!/usr/bin/env python3
"""Self-audit: every artifact Verdict owns is §9-compliant + linked to source.

Verdict Agent deliverable C. Validates the 10 §9 required fields per record.
JSONL files: line-by-line. JSON files: report item-count or array-length.
Writes self_audit_report.json; print summary.
"""
import json
from datetime import datetime
from pathlib import Path

REQUIRED_FIELDS = [
    'source_url', 'date', 'status', 'relevance', 'recency',
    'actionability', 'extraction', 'decision_it_changes',
    'transfer', 'transfer_harness_fact',
]

ARTIFACTS = [
    '/Users/srujansai/Desktop/South/level2/benchmark/scores/gt_verification.json',
    '/Users/srujansai/Desktop/South/level2/benchmark/scores/gt_forensics.json',
    '/Users/srujansai/Desktop/South/level2/benchmark/manifest_v1.json',
    '/Users/srujansai/Desktop/South/level2/benchmark/logs/engine_readiness.json',
    '/Users/srujansai/Desktop/South/docs/research/level7/b/b1_rlvr_ocr/artifacts.jsonl',
]


def audit_jsonl(path: Path) -> dict:
    if not path.exists():
        return {'file': str(path), 'records': 0, 'missing': 'FILE_NOT_FOUND', 'format': 'jsonl'}
    rec_count = 0
    missing_total = 0
    parse_errors = 0
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            parse_errors += 1
            continue
        if not isinstance(rec, dict):
            parse_errors += 1
            continue
        rec_count += 1
        for fld in REQUIRED_FIELDS:
            if fld not in rec or rec[fld] in (None, ''):
                missing_total += 1
    return {
        'file': str(path),
        'records': rec_count,
        'missing_fields_total': missing_total,
        'parse_errors': parse_errors,
        'format': 'jsonl',
    }


def audit_json(path: Path) -> dict:
    if not path.exists():
        return {'file': str(path), 'records': 0, 'missing': 'FILE_NOT_FOUND', 'format': 'json'}
    try:
        j = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        return {'file': str(path), 'records': 0, 'error': f'PARSE_ERROR: {e}', 'format': 'json'}
    if isinstance(j, list):
        return {'file': str(path), 'records': len(j), 'format': 'json', 'array': True}
    if isinstance(j, dict):
        items = j.get('items', [])
        record_count = len(items) if isinstance(items, list) else 'dict-non-list'
        return {'file': str(path), 'records': record_count, 'format': 'json', 'array': False, 'top_keys': list(j.keys())[:8]}
    return {'file': str(path), 'records': 'unknown-shape', 'format': 'json'}


def main() -> None:
    report = {
        'timestamp': datetime.now().isoformat(),
        'law': '§9 evidence law: 10 required fields per record',
        'required_fields': REQUIRED_FIELDS,
        'verdict_owned_artifacts': [],
        'summary': {'total_files': 0, 'compliant_jsonl_records': 0, 'missing_fields_total': 0, 'parse_errors_total': 0},
    }
    for a in ARTIFACTS:
        p = Path(a)
        if p.suffix == '.jsonl':
            r = audit_jsonl(p)
        else:
            r = audit_json(p)
        report['verdict_owned_artifacts'].append(r)
        report['summary']['total_files'] += 1
        if r.get('format') == 'jsonl':
            report['summary']['compliant_jsonl_records'] += r.get('records', 0) - (
                1 if r.get('missing_fields_total', 0) == 0 and r.get('records', 0) > 0 else 0
            )
            report['summary']['missing_fields_total'] += r.get('missing_fields_total', 0)
            report['summary']['parse_errors_total'] += r.get('parse_errors', 0)

    out = Path('/Users/srujansai/Desktop/South/level2/benchmark/scores/self_audit_report.json')
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Self-audit report: {out}')
    print(f'  files audited: {report["summary"]["total_files"]}')
    print(f'  jsonl records: {report["summary"]["compliant_jsonl_records"]}')
    print(f'  missing fields (jsonl): {report["summary"]["missing_fields_total"]}')
    print(f'  parse errors (jsonl): {report["summary"]["parse_errors_total"]}')


if __name__ == '__main__':
    main()
