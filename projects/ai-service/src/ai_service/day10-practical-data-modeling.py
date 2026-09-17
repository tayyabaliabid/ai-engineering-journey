from fastapi import FastAPI
from typing_extensions import TypedDict, TypeVar, ParamSpec, Literal
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

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    
        
class Booking(BaseModel):
    hotel_id: int
    guest_name: str
    status: BookingStatus
    room_type: Literal["standard", "deluxe", "suite"]
    

booking = Booking(hotel_id = 101, guest_name= "tayyab ali", status= "confirmed", room_type="premium")

@dataclass
class BookingDetails:
    hotel_id: int
    guest_name: str
    status: BookingStatus
    room_type: str
    
details = BookingDetails(
    hotel_id=booking.hotel_id,
    guest_name=booking.guest_name,
    status=booking.status,
    room_type=booking.room_type
)

print(details)


print(booking)
print(booking.status)
print(booking.status.value)
print(type(booking.status))
