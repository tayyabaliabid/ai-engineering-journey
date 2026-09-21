from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec, Literal, Protocol
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable
from contextlib import contextmanager
from dataclasses import dataclass, field
from pydantic import BaseModel
from enum import Enum
from abc import ABC, abstractmethod
import asyncio
import time

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")

async def fetch_data():
    await asyncio.sleep(2)
    print(f"fetching data")
    return "Hello from async"

async def fetch_users() -> str:
    await asyncio.sleep(2)
    print("fetching users")
    return "users found"

async def fetch_bookings() -> str:
    await asyncio.sleep(2)
    print("fetching bookings")
    return "bookings found"

async def main():
    start = time.perf_counter()

    # code you want to measure
    users, bookings = await asyncio.gather(fetch_users(), fetch_bookings())
    
    # users = await fetch_users()
    # bookings = await fetch_bookings()
    print(f"users: {users}")
    print(f"bookings: {bookings}")
    

    elapsed = time.perf_counter() - start

    print(f"Elapsed: {elapsed:.2f} seconds")
    return True

result = asyncio.run(main())
print(result)


