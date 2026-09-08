from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
import time

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

def iterable(items: Iterable[str]):
    iterator = iter(items)
    while iterator:
        try:
            print(next(iterator))
        except StopIteration:
            break

response = iterable(("Ali", "John"))
