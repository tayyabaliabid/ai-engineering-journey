from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec, Literal
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable
from contextlib import contextmanager
from dataclasses import dataclass, field
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")


def set_log_level(level: Literal["debug", "info", "error"]):
    print(f"Log level: {level}")

set_log_level("debug")
set_log_level("info")
set_log_level("error")
set_log_level("no")


# class Bookingstatus(str, Enum):
#     PENDING: str = "pending"
#     CONFIRMED: str = "confirmed"
#     CANCELLED: str = "cancelled"
    
# status = Bookingstatus.CONFIRMED

# print(status)
# print(status.value)
# print(status == "confirmed")