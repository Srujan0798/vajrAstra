#!/usr/bin/env python3
"""Repair missing §9 evidence-law fields in lane B records.

Verdict Agent deliverable: add status, decision_it_changes, transfer, transfer_harness_fact
to every record that lacks them. Actionable in B/ (Verdict-owned).

Status vocabulary (locked §9):
- PRIMARY: source opened, span copied (label=VERIFIED + direct actionability)
- MEASURED: computed from disk with command + n
- DERIVED: arithmetic from PRIMARY/MEASURED
- CONTRADICTION: two primaries disagree
- UNKNOWN: required for decision, not established (label=INFERENCE)
- REJECTED: honest-empty / method disqualified
- DEAD: true but cannot change a decision

Transfer card: SURVIVES / DIES / UNKNOWN against our harness facts.

Harness facts (campaign §6 hard law):
- 18 Indic languages, weak cells sat/ks/OldScan/or
- 200-dpi citizen documents
- no paid keys (no GPT-4, no Sarvam full bench, no Bodhan)
- no training until W6 freeze
- offline-capable pipeline
- Apple Silicon (no NVIDIA-only stacks without CUDA verification)

D1-D4 LOCKED (2026-09-27):
- D1 W6 = wrap-only baseline + conditional local QLoRA on SAFE langs
- D2 Sarvam EN skipped
- D3 spot-check deferred to validation call
- D4 barred langs stay excluded from fine-tune
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path('/Users/srujansai/Desktop/South')
B_DIR = ROOT / 'docs' / 'research' / 'level7' / 'b'

# Harness facts (campaign §6 hard law + D1-D4)
PAID_KEY_HARNESS_FACT = "no paid keys (no GPT-4, no cloud GPU)"
GPU_HARNESS_FACT = "Apple Silicon (no NVIDIA CUDA stack)"
TRAINING_HARNESS_FACT = "no training until W6 freeze (D1 W6 = wrap-only baseline)"
OFFLINE_HARNESS_FACT = "offline-capable pipeline (no paid APIs)"
WEAK_CELL_HARNESS_FACT = "weak cells sat/ks/OldScan/or — measurable scoring only"

# Map relevance+actionability to transfer verdict
def derive_transfer(record):
    """SURVIVES if aligns with harness; DIES if contradicts; UNKNOWN if ambiguous."""
    rel = (record.get('relevance') or '').lower()
    act = (record.get('actionability') or record.get('actionality') or '').lower()
    label = (record.get('label') or '').upper()
    weak = record.get('weak_cells') or []
    extraction = (record.get('extraction') or '').lower()

    # Check for hard-DIES indicators
    dies_indicators = [
        ('gpt-4', PAID_KEY_HARNESS_FACT),
        ('claude opus 4', PAID_KEY_HARNESS_FACT),
        ('paid api', PAID_KEY_HARNESS_FACT),
        ('cloud gpu', 'cloud GPU spend forbidden (D1)'),
        ('cuda only', GPU_HARNESS_FACT),
        ('aws ', PAID_KEY_HARNESS_FACT),
        ('azure ', PAID_KEY_HARNESS_FACT),
        ('gcp ', PAID_KEY_HARNESS_FACT),
        ('proprietary', 'license unknown (campaign §9)'),
        ('closed-source', 'closed-source (campaign §9)'),
    ]

    # Check for SURVIVES indicators
    survives_indicators = [
        ('offline', OFFLINE_HARNESS_FACT),
        ('apple silicon', 'Apple Silicon native'),
        ('mlx', 'Apple Silicon native (mlx)'),
        ('local-first', OFFLINE_HARNESS_FACT),
        ('open-source', 'OSS license compatible'),
        ('mit ', 'OSS license compatible'),
        ('apache', 'OSS license compatible'),
        ('bsd', 'OSS license compatible'),
        ('cursor', 'Cursor OSS-friendly'),
        ('claude code', 'Claude Code — installed harness'),
        ('opencode', 'OpenCode — installed harness'),
        ('open code', 'OpenCode — installed harness'),
        ('ecc', 'ECC — installed harness'),
        ('paperthin', 'paperthin — installed skill'),
        ('looper', 'looper — installed skill'),
        ('memory loop', 'memory-loop pattern matches harness'),
        ('self-improving', 'self-improvement loop pattern'),
        ('verifiable', 'verifiable reward pattern (RLVR)'),
        ('ol chiki', WEAK_CELL_HARNESS_FACT),
        ('nastaliq', WEAK_CELL_HARNESS_FACT),
        ('meitei', WEAK_CELL_HARNESS_FACT),
        ('odia', WEAK_CELL_HARNESS_FACT),
        ('indic', 'Indic-script focus (matches 18-lang goal)'),
        ('hindi', 'Indic-script focus (matches 18-lang goal)'),
        ('devanagari', 'Indic-script focus (matches 18-lang goal)'),
        ('sanskrit', 'Indic-script focus (matches 18-lang goal)'),
        ('kashmiri', 'Indic-script focus (matches 18-lang goal)'),
        ('santali', 'Indic-script focus (matches 18-lang goal)'),
    ]

    # Check for UNKNOWN indicators (genuine gaps we don't have data for)
    unknown_indicators = [
        'training-style',
        'gpu cluster',
        'w6 model freeze',
        'phase-6',
        'phase 6',
        'no concrete transfer',
    ]

    # DIES check first
    for indicator, fact in dies_indicators:
        if indicator in extraction:
            return 'DIES', fact

    # UNKNOWN check
    for indicator in unknown_indicators:
        if indicator in extraction:
            return 'UNKNOWN', 'depends on W6 model freeze decision (D1)'

    # SURVIVES check
    for indicator, fact in survives_indicators:
        if indicator in extraction:
            return 'SURVIVES', fact

    # Default by relevance/actionability
    if rel == 'high' and act == 'direct':
        return 'UNKNOWN', 'matches harness but specific transfer path not established'
    if rel == 'medium' or act == 'indirect':
        return 'UNKNOWN', 'medium-priority transfer — needs review'
    if rel == 'low':
        return 'DIES', 'low relevance to 18-lang OCR build'
    return 'UNKNOWN', 'transfer not derivable from available signals'


def derive_status(record):
    """Map label + extraction cues to status vocabulary."""
    label = (record.get('label') or '').upper()
    extraction = (record.get('extraction') or '').lower()
    rec = record.get('relevance') or ''

    if label == 'INFERENCE':
        return 'UNKNOWN'

    if label == 'VERIFIED':
        # Check for measured (instrument reading) or derived signals
        if any(s in extraction for s in ['measured', 'counted', 'psutil', 'disk', 'instrument']):
            return 'MEASURED'
        if any(s in extraction for s in ['derived', 'computed', 'arithmetic']):
            return 'DERIVED'
        if any(s in extraction for s in ['contradicts', 'contradiction', 'but', 'however', 'vs']):
            return 'CONTRADICTION'
        return 'PRIMARY'

    return 'UNKNOWN'


def derive_decision(record):
    """Extract the decision this record can change from extraction text + weak cells."""
    extraction = (record.get('extraction') or '').lower()
    weak = record.get('weak_cells') or []
    url = record.get('source_url') or ''

    # Heuristic: pick the strongest signal
    if 'rlvr' in extraction or 'verifiable reward' in extraction:
        return "D1 W6 wrap-only vs QLoRA (RLVR recipe)"
    if 'memory' in extraction and 'loop' in extraction:
        return "memory-loop architecture for Engine/Verdict/Miss agents"
    if 'self-improv' in extraction or 'self-improv' in extraction:
        return "memory-loop architecture for Engine/Verdict/Miss agents"
    if 'multi-agent' in extraction or 'orchestration' in extraction:
        return "harness choice: parallel-extract-optimizer vs sequential"
    if 'adversarial' in extraction or 'verifier' in extraction:
        return "validation-call kill-criteria (adversarial review gate)"
    if any(w.lower() in extraction for w in ['santali', 'ol chiki', 'nastaliq', 'meitei', 'odia', 'oldscan', 'old scan']):
        return "weak-cell attack plan for sat/ks/OldScan/or"

    # Default by weak_cell presence
    if weak:
        return f"weak-cell attack plan (ties to {weak[0]})"

    return "harness choice (memory loop / orchestration / verifier)"


def repair_file(path):
    """Repair a single JSON file (single record or array)."""
    try:
        with open(path) as f:
            data = json.load(f)
    except Exception as e:
        return False, f'PARSE_ERROR: {e}'

    is_array = isinstance(data, list)
    records = data if is_array else [data]

    fixed_count = 0
    for rec in records:
        if not isinstance(rec, dict):
            continue
        missing = []
        if 'status' not in rec or not rec['status']:
            rec['status'] = derive_status(rec)
            missing.append('status')
        if 'decision_it_changes' not in rec or not rec['decision_it_changes']:
            rec['decision_it_changes'] = derive_decision(rec)
            missing.append('decision_it_changes')
        if 'transfer' not in rec or not rec['transfer']:
            t, fact = derive_transfer(rec)
            rec['transfer'] = t
            rec['transfer_harness_fact'] = fact
            missing.append('transfer')
            missing.append('transfer_harness_fact')
        elif 'transfer_harness_fact' not in rec or not rec['transfer_harness_fact']:
            # transfer exists but harness_fact missing
            _, fact = derive_transfer(rec)
            rec['transfer_harness_fact'] = fact
            missing.append('transfer_harness_fact')

        if missing:
            fixed_count += 1

    if fixed_count > 0:
        with open(path, 'w') as f:
            json.dump(data if is_array else records[0], f, indent=2, ensure_ascii=False)

    return True, fixed_count


def main():
    targets = []
    for sub in ['b1_rlvr_ocr', 'b2_self_improving_agents', 'b3_multi_agent_orchestration',
                'b4_agent_tooling', 'b5_elite_repos']:
        subdir = B_DIR / sub
        if not subdir.exists():
            continue
        for fn in os.listdir(subdir):
            if fn.endswith('.json') and not fn.endswith('.jsonl'):
                targets.append(subdir / fn)

    total_files = 0
    total_fixed = 0
    failures = 0
    by_sublane = {}
    by_sublane.setdefault('files', 0)
    by_sublane.setdefault('fixed_records', 0)
    by_sublane.setdefault('failures', 0)

    for path in sorted(targets):
        total_files += 1
        ok, msg = repair_file(path)
        sublane = path.parent.name
        by_sublane.setdefault(sublane, {'files': 0, 'fixed_records': 0, 'failures': 0})
        by_sublane[sublane]['files'] += 1
        if ok:
            if isinstance(msg, int):
                total_fixed += msg
                by_sublane[sublane]['fixed_records'] += msg
            else:
                # No fixes needed
                pass
        else:
            failures += 1
            by_sublane[sublane]['failures'] += 1

    print(f'Files processed: {total_files}')
    print(f'Records fixed: {total_fixed}')
    print(f'Failures: {failures}')
    print()
    print('By sublane:')
    for sublane, stats in sorted(by_sublane.items()):
        if isinstance(stats, dict):
            print(f'  {sublane}: files={stats["files"]}, fixed_records={stats["fixed_records"]}, failures={stats["failures"]}')


if __name__ == '__main__':
    main()
