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
import httpx

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")

# async def fetch_data():
#     async with httpx.AsyncClient(timeout=2.0) as client:
#         print(f"Starting http call")
#         response = await client.get("https://httpbin.org/delay/5")
#         # response = await client.get("https://httpbin.org/status/404")
#         # response = await client.get("https://httpbin.org/get")
        
#         response.raise_for_status()
        
#         return {
#             "statusCode": response.status_code,
#             "data": response.json(),
#         }
        
async def fetch_users():
    async with httpx.AsyncClient(timeout=2.0) as client:
        print(f"Fetch users")
        response = await client.get("https://jsonplaceholder.typicode.com/users")
        
        response.raise_for_status()
        
        return {
            "statusCode": response.status_code,
            "data": response.json(),
        }
        
async def fetch_posts():
    async with httpx.AsyncClient(timeout=2.0) as client:
        print(f"Fetch posts")
        response = await client.get("https://jsonplaceholder.typicode.com/posts")
        
        response.raise_for_status()
        
        return {
            "statusCode": response.status_code,
            "data": response.json(),
        }

async def main():
    start = time.perf_counter()
    try:
        users, posts = await asyncio.gather(fetch_users(), fetch_posts())
    except httpx.HTTPStatusError:
        print("HTTP request failed")
    except httpx.TimeoutException:
        print("HTTP request timed out")
    else:
        print(f"total users: {len(users['data'])}")
        print(f"total posts: {len(posts['data'])}")
    finally:
        total = time.perf_counter() - start
        print(f"total time: {total:.2f}")
    
asyncio.run(main())