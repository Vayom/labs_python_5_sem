import random
import time
import threading


class ProfileDecorator:
    def __init__(self, func):
        self.func = func
        self.lock = threading.Lock()
        self.call_count = 0
        self.total_execution_time = 0.0

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with self.lock:
            self.call_count += 1
            self.total_execution_time += execution_time
        return result

    def stats(self):
        with self.lock:
            return {
                "function_name": self.func.__name__,
                "call_count": self.call_count,
                "total_execution_time": self.total_execution_time
            }