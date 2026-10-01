#!/usr/bin/env python3
"""Audit §9 evidence-law field coverage in lane B records.

Reports per-sublane: total records, compliant records, missing field counts.
"""
import json
import os
from collections import Counter
from pathlib import Path

ROOT = Path('/Users/srujansai/Desktop/South')
B_DIR = ROOT / 'docs' / 'research' / 'level7' / 'b'

REQUIRED_FIELDS = [
    'source_url', 'date', 'status', 'relevance', 'recency',
    'actionability', 'extraction', 'decision_it_changes',
    'transfer', 'transfer_harness_fact',
]


def audit_record(rec):
    missing = []
    for field in REQUIRED_FIELDS:
        if field not in rec or rec[field] in (None, ''):
            missing.append(field)
    return missing


def main():
    stats = {}
    files_with_missing = []
    total_records = 0
    total_missing = 0
    records_with_missing = 0

    for sub in ['b1_rlvr_ocr', 'b2_self_improving_agents', 'b3_multi_agent_orchestration',
                'b4_agent_tooling', 'b5_elite_repos']:
        subdir = B_DIR / sub
        if not subdir.exists():
            continue
        stats[sub] = {'files': 0, 'records': 0, 'compliant': 0, 'missing_records': 0, 'missing_fields_total': 0}
        for fn in os.listdir(subdir):
            if fn.endswith('.jsonl'):
                # JSONL format
                stats[sub]['files'] += 1
                path = subdir / fn
                with open(path) as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            rec = json.loads(line)
                        except:
                            continue
                        stats[sub]['records'] += 1
                        total_records += 1
                        m = audit_record(rec)
                        if m:
                            stats[sub]['missing_records'] += 1
                            stats[sub]['missing_fields_total'] += len(m)
                            total_missing += len(m)
                            records_with_missing += 1
                        else:
                            stats[sub]['compliant'] += 1
            elif fn.endswith('.json'):
                # JSON format
                stats[sub]['files'] += 1
                path = subdir / fn
                try:
                    with open(path) as f:
                        data = json.load(f)
                except json.JSONDecodeError as e:
                    stats[sub]['missing_records'] += 1
                    files_with_missing.append((str(path), str(e)))
                    continue
                records = data if isinstance(data, list) else [data]
                for rec in records:
                    if not isinstance(rec, dict):
                        continue
                    stats[sub]['records'] += 1
                    total_records += 1
                    m = audit_record(rec)
                    if m:
                        stats[sub]['missing_records'] += 1
                        stats[sub]['missing_fields_total'] += len(m)
                        total_missing += len(m)
                        records_with_missing += 1
                        files_with_missing.append(str(path))
                    else:
                        stats[sub]['compliant'] += 1

    print('=' * 80)
    print('§9 EVIDENCE-LAW AUDIT — Lane B (after repair)')
    print('=' * 80)
    print()
    print(f'{"Sublane":30s} {"Files":>6s} {"Records":>8s} {"Compliant":>10s} {"Missing":>8s} {"Fields":>7s}')
    print('-' * 80)
    for sub in sorted(stats.keys()):
        s = stats[sub]
        print(f'{sub:30s} {s["files"]:>6d} {s["records"]:>8d} {s["compliant"]:>10d} {s["missing_records"]:>8d} {s["missing_fields_total"]:>7d}')
    print('-' * 80)
    total_files = sum(s['files'] for s in stats.values())
    total_compliant = sum(s['compliant'] for s in stats.values())
    total_missing_records = sum(s['missing_records'] for s in stats.values())
    print(f'{"TOTAL":30s} {total_files:>6d} {total_records:>8d} {total_compliant:>10d} {total_missing_records:>8d} {total_missing:>7d}')
    print()
    if files_with_missing:
        print('Files still missing fields:')
        for f in files_with_missing[:20]:
            print(f'  {f}')


if __name__ == '__main__':
    main()
