#!/usr/bin/env python3
"""SLO Definitions + Error Budget Tracking."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime
import json

@dataclass
class SLO:
    name: str
    target: float
    window_days: int
    description: str

SLO_DEFINITIONS = [
    SLO('availability', 0.999, 30, 'API uptime'),
    SLO('latency_p99', 2.0, 7, 'p99 latency < 2s'),
    SLO('cer_telugu', 0.05, 30, 'Telugu CER < 5%'),
    SLO('cer_tamil', 0.05, 30, 'Tamil CER < 5%'),
    SLO('cer_kannada', 0.07, 30, 'Kannada CER < 7%'),
    SLO('cer_malayalam', 0.08, 30, 'Malayalam CER < 8%'),
    SLO('cascade_accuracy', 0.98, 7, 'Cascade routing accuracy > 98%'),
]

@dataclass
class ErrorBudget:
    slo: SLO
    consumed: float
    remaining: float
    burn_rate: float
    alert: bool

def compute_error_budget(slo: SLO, actual_performance: float):
    if actual_performance >= slo.target:
        consumed = 0.0
    else:
        consumed = (slo.target - actual_performance) / (1 - slo.target)
    consumed = max(0.0, min(1.0, consumed))
    window_hours = slo.window_days * 24
    burn_rate = consumed / max(window_hours * 0.01, 1)
    return ErrorBudget(slo, consumed, 1.0 - consumed, burn_rate, burn_rate > 1.0)

def generate_slo_report(metrics: Dict[str, float]):
    report = {'timestamp': datetime.utcnow().isoformat() + 'Z', 'slos': [], 'overall_healthy': True}
    for slo in SLO_DEFINITIONS:
        actual = metrics.get(slo.name, slo.target)
        budget = compute_error_budget(slo, actual)
        report['slos'].append({
            'name': slo.name, 'target': slo.target, 'actual': actual,
            'consumed_pct': round(budget.consumed * 100, 2),
            'remaining_pct': round(budget.remaining * 100, 2),
            'burn_rate_per_hour': round(budget.burn_rate, 4),
            'alert': budget.alert,
        })
        if budget.alert:
            report['overall_healthy'] = False
    return report

if __name__ == '__main__':
    print(json.dumps(generate_slo_report({'availability': 0.9995, 'latency_p99': 1.8, 'cer_telugu': 0.042, 'cer_tamil': 0.048, 'cer_kannada': 0.065, 'cer_malayalam': 0.075, 'cascade_accuracy': 0.985}), indent=2))
