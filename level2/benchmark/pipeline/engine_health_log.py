import json
from pathlib import Path
from datetime import datetime, timezone

LOG = Path('/Users/srujansai/Desktop/South/level2/benchmark/logs/engine_health_log.jsonl')

def log_event(event_type, **kwargs):
    entry = {'timestamp': datetime.now(timezone.utc).isoformat(), 'event': event_type, **kwargs}
    with LOG.open('a') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    import sys
    event = sys.argv[1] if len(sys.argv) > 1 else 'manual'
    details = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    log_event(event, **details)
    print(f'Logged: {event}')