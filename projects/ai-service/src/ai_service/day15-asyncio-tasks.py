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

async def main_old():
    start = time.perf_counter()

    users_task = asyncio.create_task(fetch_users())
    bookings_task = asyncio.create_task(fetch_bookings())
    # print("tasks created")
    print("Preparing response...")
    
    users = await users_task 
    bookings = await bookings_task 
    
    # print("Preparing response...")
    # code you want to measure
    # users, bookings = await asyncio.gather(fetch_users(), fetch_bookings())
    
    # users = await fetch_users()
    # bookings = await fetch_bookings()
    print(f"users: {users}")
    print(f"bookings: {bookings}")
    

    elapsed = time.perf_counter() - start

    print(f"Elapsed: {elapsed:.2f} seconds")
    return True

# result = asyncio.run(main_old())
# print(result)


# async def main():
#     start = time.perf_counter()

#     try:
#         result = await asyncio.wait_for(
#             fetch_data(),
#             timeout=2
#         )
#     except asyncio.TimeoutError as e:
#         print(f"Operation timed out: {e}")
        
#     elapsed = time.perf_counter() - start

#     print(f"Elapsed: {elapsed:.2f} seconds")
#     return True


# result = asyncio.run(main())


async def slow_operation():
    await asyncio.sleep(5)
    return "completed"

async def main():
    start = time.perf_counter()

    task = asyncio.create_task(slow_operation())
    await asyncio.sleep(1)

    task.cancel()
    
    try:
        result = await task
    except asyncio.CancelledError:
        print(f"Operation cancelled")
        
    elapsed = time.perf_counter() - start

    print(f"Elapsed: {elapsed:.2f} seconds")
    return True


result = asyncio.run(main())
