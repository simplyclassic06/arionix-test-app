from collections import defaultdict
import time
//zero//
RATE_LIMIT = 100
WINDOW_SECONDS = 60

_buckets: dict = defaultdict(list)

def is_allowed(api_key: str) -> tuple:
    now = time.time()
    window_start = now - WINDOW_SECONDS
    _buckets[api_key] = [t for t in _buckets[api_key] if t > window_start]

    if len(_buckets[api_key]) >= RATE_LIMIT:
        retry_after = int(WINDOW_SECONDS - (now - _buckets[api_key][0])) + 1
        return False, retry_after

    _buckets[api_key].append(now)
    return True, 0
