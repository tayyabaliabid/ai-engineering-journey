from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence, Iterator
import time

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

"""
print numbers even numbers
"""

def even_numbers(limit: int = 10) -> Iterator[int]:
    for i in range(1, limit + 1):
        if i % 2 == 0:
            time.sleep(1)
            yield i

def get_even_numbers():
    enums = even_numbers()
    for enum in enums:
        print(enum)
        
get_even_numbers()
