#!/usr/bin/env python3
"""Immutable Decision Log — every architectural decision recorded."""
from __future__ import annotations
import json
import hashlib
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional

LOG_FILE = Path("level2/governance/DECISIONS.log")

@dataclass
class Decision:
    id: str
    timestamp: str
    author: str
    title: str
    context: str
    decision: str
    rationale: str
    alternatives_considered: list[str]
    consequences: str
    links: list[str]
    tags: list[str]
    previous_decision_id: str | None = None
    hash: str = ""

class DecisionLog:
    def __init__(self, log_file: Path = Path("level2/governance/DECISIONS.log")):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_file.exists():
            self.log_file.write_text('')
    
    def _hash_chain(self, decision: Decision) -> str:
        content = f'{decision.id}{decision.timestamp}{decision.decision}{decision.previous_decision_id or ""}'
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def append(self, decision: Decision) -> str:
        prev_hash = None
        if self.log_file.exists() and self.log_file.stat().st_size > 0:
            lines = self.log_file.read_text().strip().split('\n')
            if lines:
                last = json.loads(lines[-1])
                prev_hash = last.get('hash')
        
        decision.previous_decision_id = prev_hash
        decision.id = hashlib.sha256(f'{decision.timestamp}{decision.title}'.encode()).hexdigest()[:12]
        decision.hash = self._hash_chain(decision)
        
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(asdict(decision), ensure_ascii=False) + '\n')
        return decision.id
    
    def get_recent(self, n: int = 10):
        if not self.log_file.exists(): return []
        lines = self.log_file.read_text().strip().split('\n')
        return [json.loads(l) for l in lines[-n:]]

def log_decision(
    title: str, context: str, decision: str, rationale: str,
    alternatives: list[str], consequences: str, links: list[str],
    tags: list[str], author: str = 'system'
) -> str:
    d = Decision(
        id='', timestamp=datetime.utcnow().isoformat() + 'Z', author=author,
        title=title, context=context, decision=decision, rationale=rationale,
        alternatives_considered=alternatives, consequences=consequences,
        links=links, tags=tags,
    )
    return DecisionLog().append(d)

if __name__ == '__main__':
    log_decision(
        title='Adopt cascade routing architecture',
        context='10-engine benchmark shows 382/400 coverage but 7.1% gap',
        decision='Implement 3-tier cascade router with uncertainty calibration',
        rationale='Early exit on 60% pages saves 3× compute; uncertainty head routes hard pages to ensemble',
        alternatives=['Single large model', 'Static ensemble', 'All engines always'],
        consequences=['+3× throughput', '-15% CER on hard pages', 'New model to maintain'],
        links=['#142'], tags=['architecture', 'cascade', 'performance'],
    )
    print('Decision logged')
