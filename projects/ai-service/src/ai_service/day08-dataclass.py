from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable
from contextlib import contextmanager
from dataclasses import dataclass, field
from pydantic import BaseModel

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")

@dataclass
class Product:
    name: str
    price: float

class ProductModel(BaseModel):
    name: str
    price: float
    
product = Product(name="Cup", price="5.99")
product_model = ProductModel(name="Cup", price="5.99")

print(product)
print(product_model)

# @dataclass(frozen=True)
# class ModelConfig:
#     provider: str
#     model: str
#     temperature: float
    
# config = ModelConfig(provider="openai", model="some-model", temperature=1.7)
# config.temperature = 3.5
# print(config)


# @dataclass
# class Product:
#     name: str
#     price: float
#     internal_code: str = field(default="", repr=False)
#     tag: list[str] = field(default_factory=list)


# product = Product(name = "Cup", price = 5.99)

# print(product)

# @dataclass
# class User:
#     id: int
#     name: str
#     email: str
#     age: int    
#     active: bool = True
#     roles: list[str] = field(default_factory=list)
    
    
# user1 = User(id = 1, name = "Tayyab", email = "tayyab@example.com", age = 35)
# user2 = User(id = 1, name = "Tayyab", email = "tayyab@example.com", age = 35, active = False)

# user1.roles.append("admin")
# print(user1.roles)
# print(user2.roles)