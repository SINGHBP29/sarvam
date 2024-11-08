# rate_limit_cache.py

import time

RATE_LIMIT_TIME = 1  # 1 second rate limit

last_request_time = 0

def rate_limited():
    """Ensures there's at least RATE_LIMIT_TIME between API calls."""
    global last_request_time
    current_time = time.time()
    if current_time - last_request_time < RATE_LIMIT_TIME:
        time.sleep(RATE_LIMIT_TIME - (current_time - last_request_time))
    last_request_time = time.time()
