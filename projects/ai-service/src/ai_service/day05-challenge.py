from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable

import time

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")

def measure_time(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Execution time: {elapsed:.6f} seconds")
        return result 
    return wrapper

@measure_time
def add(a: int, b: int) -> int:
    return a + b

result = add(10, 20)

print(result)