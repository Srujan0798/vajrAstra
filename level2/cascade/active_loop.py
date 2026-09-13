#!/usr/bin/env python3
"""Active Learning Loop — max uncertainty → human review → retrain."""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict

@dataclass
class ReviewItem:
    page_id: str
    image_path: str
    engine_outputs: dict
    uncertainties: dict
    aggregate_uncertainty: float
    predicted_tier: str
    human_label: str | None = None

class ActiveLearningLoop:
    def __init__(self, review_dir: Path, budget_per_cycle: int = 50):
        self.review_dir = Path(review_dir)
        self.review_dir.mkdir(parents=True, exist_ok=True)
        self.budget = budget_per_cycle
        self.queue_file = self.review_dir / 'review_queue.jsonl'
        self.completed_file = self.review_dir / 'completed.jsonl'
        self.retrain_trigger = 100
    
    def score_uncertainty(self, engine_outputs: dict, char_entropies: dict) -> float:
        entropies = []
        for eng, ent in char_entropies.items():
            if ent:
                entropies.append(sum(ent) / len(ent))
        avg_entropy = sum(entropies) / len(entropies) if entropies else 0
        return avg_entropy
    
    def select_for_review(self, candidates: List[dict], n: int) -> List[dict]:
        scored = [(c['uncertainty'], c) for c in candidates]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [c for _, c in scored[:n]]
    
    def add_to_queue(self, items: List):
        with open(self.queue_file, 'a', encoding='utf-8') as f:
            for item in items:
                f.write(json.dumps(asdict(item), ensure_ascii=False) + '\n')
    
    def complete_review(self, page_id: str, human_label: str):
        pass

if __name__ == '__main__':
    print('ActiveLearningLoop ready')
