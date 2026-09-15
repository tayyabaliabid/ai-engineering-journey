from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")


class TimerContext:
    
    def message(self):
        return "Timer is running"
    
    def __enter__(self):
        print("Starting..")
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception: {exc_value}")
            print("Type:", exc_type)
            print("Value:", exc_value)
            print("Traceback:", traceback) 
            return True     
        
        print("Finishing")
        
# with TimerContext() as timer:
#     print(timer.message())
      
#     raise ValueError("Something went wrong")

with TimerContext():
    print("Doing some work")
    raise ValueError("Something went wrong")

print("Program continues")