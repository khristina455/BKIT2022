import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self._start_time = None

    def __enter__(self):
        self._start_time = time.perf_counter()
        return self

    def __exit__(self, *exc_info):
        all_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"time: {all_time:0.4f}")

@contextmanager
def cm_timer_2():
    start_time = time.perf_counter()
    try:
        yield start_time
    finally:
        print(f"time: {time.perf_counter() - start_time: 0.4f}")


