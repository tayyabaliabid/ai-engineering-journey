# Day 13 — Protocol vs ABC in Real Backend Design

## Learned

### 1. Protocol

A `Protocol` defines a behavioral contract without requiring inheritance.

```python
class NotificationSender(Protocol):
    def send(self, message: str) -> bool:
        ...
```

A class does not need to inherit from the Protocol:

```python
class EmailSender:
    def send(self, message: str) -> bool:
        ...
```

This is called **structural typing**.

The important question is:

> Does this object provide the behavior I need?

---

### 2. ABC

An Abstract Base Class requires explicit inheritance and can enforce implementation of abstract methods.

```python
class NotificationSenderABC(ABC):

    @abstractmethod
    def send(self, message: str) -> bool:
        ...
```

A subclass must implement the abstract method before it can be instantiated.

---

### 3. Protocol vs ABC

| Protocol                         | ABC                                        |
| -------------------------------- | ------------------------------------------ |
| Inheritance not required         | Inheritance required                       |
| Structural typing                | Explicit class hierarchy                   |
| Flexible                         | More restrictive                           |
| No runtime enforcement by itself | Abstract methods enforced at instantiation |
| Good for loose coupling          | Good for enforced contracts/hierarchies    |
| Can work with existing classes   | Classes must participate in the hierarchy  |

### Mental model

**Protocol:**

> "Can you provide this behavior?"

**ABC:**

> "You must inherit from me and implement this behavior."

---

## Built

Created a realistic notification-provider example:

```text
NotificationSender
       │
       ├── EmailSender
       └── SMSSender
```

Tested a `RandomSender` that did not follow the expected method name.

This demonstrated that Protocol itself doesn't force a class to implement `send()` at runtime.

Also tested an ABC implementation where a subclass missing the abstract `send()` method could not be instantiated.

---

## Important Understanding

Python type hints and Protocols primarily describe what code **should** look like.

They are not automatically runtime validation.

For example, if a Protocol expects:

```python
send(message: str) -> bool
```

but the runtime code calls:

```python
sender.send(message)
```

and the object doesn't have `send`, Python will raise an `AttributeError`.

A static type checker can catch many of these mistakes before runtime.

This differs from Pydantic, which performs explicit runtime validation.

---

## Key Takeaway

For backend architecture:

```text
Protocol
    ↓
Loose coupling
    ↓
"Any object providing this behavior is acceptable"

ABC
    ↓
Enforced hierarchy
    ↓
"Implementations must belong to this abstraction"
```

Both are useful; the choice depends on how strict and explicit the design needs to be.

## Tomorrow

**Day 14 — Async / Await**

We'll begin asynchronous Python and understand:

* `async def`
* coroutine objects
* `await`
* `asyncio`
* why async is important for FastAPI and AI APIs
* synchronous vs asynchronous execution
