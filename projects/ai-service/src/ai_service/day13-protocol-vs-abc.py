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
from abc import ABC, abstractmethod

app = FastAPI()


P = ParamSpec("P")
T = TypeVar("T")

# Email
# SMS
# Push notification

class NotificationSender(Protocol):
    def send(message: str) -> bool:
        ...
        
class EmailSender():
    def send(self, message: str) -> bool:
        print(f"Email: {message}")
        return True
        
        
class SMSSender():
    def send(self, message: str) -> bool:
        print(f"SMS: {message}")
        return True
    
class RandomSender():
    def something_else(self, message: str) -> bool:
        print(f"hello")
        return True
        

def send_notification(sender: NotificationSender, message: str) -> bool:
    return sender.something_else(message)


sender = RandomSender()
result = send_notification(sender, "Payment Successfully Trasferred")
print(result)

# sender = EmailSender()
# result = send_notification(sender, "Payment Successfully Trasferred")
# print(result)


# sender = SMSSender()
# result = send_notification(sender, "Payment Successfully Trasferred")
# print(result)



class NotificationSenderABC(ABC):
    @abstractmethod
    def send(self, message: str) -> bool:
        ...
    
class EmailSender(NotificationSenderABC):
    def send(self, message: str) -> bool:
        print(f"Email: {message}")
        return True
        
        
class SMSSender(NotificationSenderABC):
    def send(self, message: str) -> bool:
        print(f"SMS: {message}")
        return True

# sender = SMSSender()
# result = sender.send("Payment Successfully Trasferred")
# print(result)

# class BrokenSender(NotificationSenderABC):
#     pass

# BrokenSender()