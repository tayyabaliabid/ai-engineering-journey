from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable
from contextlib import contextmanager

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")

@contextmanager
def timer_context():
    print("Starting..")
    
    yield "Timer is running"
    
    print("Finishing")
    
with timer_context() as message:
    print(message)