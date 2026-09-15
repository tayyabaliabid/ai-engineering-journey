from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")

def execute(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print("initial statement")
        result = func(*args, **kwargs)
        print("ending statement")
        return result 
    return wrapper

@execute
def greet(name: str) -> str:
    return name

@execute
def add(a: int, b: int) -> int:
    return a + b

print(greet("tayyab"))
print(add(2, 5))