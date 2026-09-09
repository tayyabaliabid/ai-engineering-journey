from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence


app = FastAPI()

"""
FUNCTIONS ARE OBJECTS
"""

def greet(name: str) -> str:
    return f"Hello {name}"

my_function = greet

# print(greet("tayyab"))
# print(my_function("abid"))

"""
FUNCTIONS CAN BE PASSED TO OTHER FUNCTIONS
"""

def execute(func, value):
    return func(value)

def double(value: int):
    return value * 2

def square(value: int):
    return value * value

result = execute(double, 10)
result2 = execute(square, 10)

# print(result)
# print(result2)

"""
FUNCTON CAN RETURN FUNCTIONS
"""

def multiplier(factor: int):
    def multiply(number: int):
        return number * factor
    return multiply

m_double = multiplier(5)
m_triple = multiplier(10)

# print(m_double(1))
# print(m_triple(2))

def power(exponent: int):
    def calculate(number: int) -> int:
        return number ** exponent
    
    return calculate

e_square = power(2)
e_qube = power(3)

# print(e_square(5))
# print(e_qube(5))



