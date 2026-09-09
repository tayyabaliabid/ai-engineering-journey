from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence


app = FastAPI()

def log_call(func):
    def wrapper(a, b):
        print("calling add")
        result = func(a, b)       
        print("finished add")
        return result        
    return wrapper

@log_call
def add(a: int, b:int) -> int:
    return a + b

result = add(2, 3)

print(result)







