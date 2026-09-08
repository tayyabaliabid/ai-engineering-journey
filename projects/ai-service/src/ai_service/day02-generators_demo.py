from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
import time

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

"""
print numbers from 1 to 5
"""
    
def get_numbers():
    items = [1,2,3,4,5]
    nums = make_numbers(items)
    for number in nums:
        print(number)
        
def make_numbers(items: Iterable[int]):
    iterator = iter(items)    
    while iterator:
        try:
            time.sleep(1)
            yield next(iterator)
        except StopIteration:
            break    
    

def get_even_numbers(limit: int = 10):
    even_numbers = []
    i = 1
    while i <= limit:
        if i % 2 == 0:
            even_numbers.append(i)
        i += 1
        
    nums = make_numbers(even_numbers)
    for number in nums:
        print(number)

# get_numbers()
get_even_numbers()
