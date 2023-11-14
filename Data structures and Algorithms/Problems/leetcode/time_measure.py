import time
from functools import wraps
from typing import Callable

def timer(funct:Callable) -> Callable:
    @wraps(funct)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funct(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start} sec.")
        return result
    return wrapper
