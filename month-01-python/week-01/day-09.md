# Day 9 — Enums, `Literal` & Type-Safe Values

## Learned

### 1. `Enum`

`Enum` represents a fixed set of named values.

```python
from enum import Enum

class BookingStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
```

Access a member:

```python
BookingStatus.CONFIRMED
```

Get its underlying value:

```python
BookingStatus.CONFIRMED.value
# "confirmed"
```

An Enum creates actual Python members.

---

### 2. `str, Enum`

For API/backend applications, we can combine `str` with `Enum`:

```python
class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
```

This gives the Enum string-like behavior:

```python
status = BookingStatus.CONFIRMED

status == "confirmed"
# True
```

This pattern is particularly common with FastAPI APIs and JSON values.

---

### 3. `Literal`

`Literal` allows us to describe a fixed set of allowed values at the type-hint level.

```python
from typing import Literal

def set_log_level(
    level: Literal["debug", "info", "error"]
):
    print(level)
```

The intended values are:

```text
"debug"
"info"
"error"
```

But we discovered an important point:

```python
set_log_level("warning")
```

still runs in normal Python.

Why?

Because `Literal` is primarily for **static type checking**. Python does not automatically enforce ordinary type hints at runtime.

---

### 4. `Enum` vs `Literal`

The key distinction:

```text
Enum
    ↓
Creates a reusable type with named members

Literal
    ↓
Restricts a value to specific choices at the type-hint level
```

Example:

```python
class LLMProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
```

This gives us:

```python
LLMProvider.OPENAI
```

Whereas:

```python
Literal["openai", "anthropic", "google"]
```

doesn't create named members.

---

### 5. Runtime validation vs type hints

This was one of the most important concepts today.

Neither:

```python
Enum
```

nor:

```python
Literal
```

should be thought of as a general runtime validation mechanism.

For runtime validation, Pydantic is useful:

```python
class LogConfig(BaseModel):
    level: Literal["debug", "info", "error"]
```

Now invalid input can produce a Pydantic `ValidationError`.

So remember:

```text
Type hints
    ↓
Help describe/check code

Pydantic
    ↓
Runtime validation/parsing
```

---

## Built

Today you:

* Created a `BookingStatus` Enum.
* Accessed Enum members with `.CONFIRMED`.
* Accessed underlying values with `.value`.
* Used `str, Enum`.
* Tested Enum/string comparison.
* Created a `Literal` type.
* Tested an invalid Literal value.
* Discovered that Python doesn't automatically enforce `Literal` at runtime.
* Compared Enum, Literal, and Pydantic.

---

## Questions

No major open questions.

The most important mental model to retain is:

```text
Enum
  → reusable named domain values

Literal
  → specific allowed values at the type-hint level

Pydantic
  → runtime validation/parsing
```

Also remember:

> Type annotations describe what code is expected to receive; they don't automatically enforce those expectations at runtime.

---

## Tomorrow — Day 10

We'll start moving from individual Python features toward **combining these concepts in practical backend code**.

The goal from here is to gradually shift from:

```text
"Learn a Python feature"
```

toward:

```text
"Use Python features to build production-style backend code."
```
