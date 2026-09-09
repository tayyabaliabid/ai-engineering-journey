from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence


app = FastAPI()

"""
FUNCTIONS ARE OBJECTS
"""

def wrapper():
    print("before")
    greet()
    print("after")
    
# wrapper()

def greet():
    print("Hello")

def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

my_d = my_decorator(greet)

# my_d()

@my_decorator
def new_function():
    print("this is my first decorator practice")

new_function()






