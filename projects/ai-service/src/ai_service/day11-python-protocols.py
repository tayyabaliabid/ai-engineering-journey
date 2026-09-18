from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec, Literal, Protocol
from pydantic import BaseModel
from collections.abc import Iterable, Sequence
from functools import wraps
from collections.abc import Callable
from contextlib import contextmanager
from dataclasses import dataclass, field
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")


class PaymentProcessor(Protocol):
    def process_payment(self, amount: float) -> bool:
        ...
        
class StripePayment:
    def process_payment(self, amount: float) -> bool:
        print(f"Stripe Processing: ${amount}")
        return True
    
class PayPalPayment:
    def process_payment(self, amount: float) -> bool:
        print(f"PayPal processing: ${amount}")
        return True
    
class MockPayment:
    def process_payment(self, amount: float) -> bool:
        print(f"Mock Payment Processing: ${amount}")
        return True

def checkout(payment_processor: PaymentProcessor, amount: float) -> bool:
    return payment_processor.process_payment(amount)

stripe = StripePayment()
payment = checkout(stripe, 50.0)
print(payment)

paypal = PayPalPayment()
payment = checkout(paypal, 50.0)
print(payment)

mock = MockPayment()
payment = checkout(mock, 50.0)
print(payment)



# mockPayment = MockPayment()
# print(mockPayment.process_payment(50.0))

# paypal = PayPalPayment()
# print(paypal.process_payment(100.0))

# stripe = StripePayment()

# print(stripe.process_payment(100.0))