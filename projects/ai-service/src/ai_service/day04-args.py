from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps


app = FastAPI()

def args_example(*args):
    print(args)
    
# args_example(5, 10)
# args_example("ali", "abid", 34)

def kwargs_example(**args):
    print(args)
    
# kwargs_example(a=5, b=10)
# kwargs_example(fname="ali", lname = "abid", age=34)

"""
Excercise
"""

def temp_add_log():
    return "hello"

def add_log(func):
    def wrapper():
        print("adding log")
        
        result = func()
        print(result)
        
        print("fininshing log")
        
        return result
    return wrapper

dec_var = add_log(temp_add_log)
# result = dec_var()
# print("----")
# print(f"result: {result}")

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("adding log")
        
        result = func(*args, **kwargs)
        
        print("fininshing log")
        
        return result
    return wrapper


@logger
def show_lat_lng_kwargs(lat: float, lng: float):
    return f"lat: {lat}, long: {lng}"

result = show_lat_lng_kwargs(lat=1.387845, lng=57.156546)
print(result)

@logger
def add(*args):
    total: int = 0
    for number in args:
        total += int(number)
    return total

@logger
def greet(name: str) -> str:
    return f"Hello {name}!"

# result = add(1, 2)
# print(result)

print("------------")

# result = greet("Tayyab")
# print(result)

@logger
def show_lat_lng(lat: float, lng: float):
    return f"lat: {lat}, long: {lng}"

# result = show_lat_lng(1.387845, 57.156546)
# print(result)


@logger
def show_lat_lng_kwargs(lat: float, lng: float):
    return f"lat: {lat}, long: {lng}"

result = show_lat_lng_kwargs(lat=1.387845, lng=57.156546)
print(result)


@logger
def show_lat_lng_mix(lat: float, lng: float):
    return f"lat: {lat}, long: {lng}"

result = show_lat_lng_mix(1.111, lng=2.222)
print(result)

print(show_lat_lng_mix.__name__)




