from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable
from contextlib import contextmanager

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")


class PaymentError(Exception):
    pass

class PaymentDeclineError(PaymentError):
    pass


def withdraw(amount: float) -> str:
    if amount <= 0:
        raise PaymentError("Invalid payment amount")
    elif amount > 1000:
        raise PaymentDeclineError("Payment Declined")
    return "payment successful"


try:
    # print(withdraw(1500))
    print(withdraw(0))
except PaymentError as e:
    print(f"Error: {e}")

# def process():
#     try:
#         value = int("abc")
#     except ValueError as e:
#         raise RuntimeError("Failed to process user data") from e

# try:
#     process()
# except Exception as e:
#     print(e)

# def process(value: str) -> int:
#     try:
#         return int(value)
#     except ValueError:
#         print("Invalid input received")
#         raise


# try:
#     process("abc")
# except ValueError as e:
#     print(f"Original error:: {e}")


# def withdraw(balance: float, amount: float) -> float:
#     if amount > balance:
#         raise ValueError("Insufficient balance")
#     return balance - amount


# try:
#     print(withdraw(100, 50))
#     print(withdraw(100, 150))
# except ValueError as e:
#     print(f"Error: {e}")
    
    
# try:
#     balance = withdraw(100, 150)
# except ValueError as e:
#     print(e)
# def calculate(value: str) -> float:
#     result = 0.0
#     try:
#         result = 100 / int(value)
#     except ValueError:
#         print("Invalid number")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
        
#     return result

# print(calculate("10"))
# print(calculate("0"))
# print(calculate("abc"))
    
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Failed")
# else:
#     print("Division succeeded")
    

# def divide(a: int, b: int) -> float:
#     result = 0.0
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     else:
#         print("Division successful")
#     finally:
#         print("Division attempt finished")
#     return result
        
# print(divide(10, 2))
# print("----")
# print(divide(10, 0))


# # result = 10 / 0
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# print("Program continues")

# # user_input = "10"

# # age = int(user_input)
# try:    
#     age = int(user_input)
# except ValueError:
#     print("Invalid age")
    
