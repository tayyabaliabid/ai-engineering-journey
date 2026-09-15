# Day 7 — Python Error Handling

## Learned

### 1. `try / except`

Used `try` to execute code that may fail and `except` to handle expected exceptions.

```python
try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 2. `else`

`else` runs only when the `try` block succeeds without an exception.

```python
try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
```

### 3. `finally`

`finally` runs whether an exception occurs or not.

```python
try:
    ...
except SomeError:
    ...
finally:
    print("Finished")
```

It is commonly used for cleanup.

---

### 4. Handling multiple exceptions

Different exceptions can have different handlers:

```python
except ValueError:
    ...
except ZeroDivisionError:
    ...
```

Or multiple exceptions can intentionally share one handler:

```python
except (ValueError, TypeError) as e:
    print(e)
```

---

### 5. `raise`

`raise` allows us to deliberately raise an exception.

```python
if amount > balance:
    raise ValueError("Insufficient balance")
```

The function that detects the problem doesn't necessarily have to handle it.

---

### 6. Re-raising an exception

A bare:

```python
raise
```

inside an `except` block re-raises the **same exception**.

Useful when a lower layer wants to log or perform some diagnostics but still wants a higher layer to handle the exception.

---

### 7. Exception chaining

```python
try:
    value = int("abc")
except ValueError as e:
    raise RuntimeError("Failed to process user data") from e
```

This means:

> Raise a new `RuntimeError`, but preserve the original `ValueError` as its cause.

The original exception can be accessed through:

```python
e.__cause__
```

---

### 8. Traceback

A traceback is **not the exception itself**.

It shows the path/location where Python encountered the unhandled exception.

When an exception reaches the top level without being caught, Python displays the traceback.

If we catch the final exception ourselves and only do:

```python
print(e)
```

we won't automatically see the traceback.

---

### 9. Custom exceptions

We can create application-specific exceptions:

```python
class PaymentError(Exception):
    pass
```

This makes our application errors more meaningful than using generic exceptions everywhere.

---

### 10. Exception inheritance

Related exceptions can form a hierarchy:

```python
class PaymentError(Exception):
    pass


class PaymentDeclineError(PaymentError):
    pass
```

Now `PaymentDeclineError` is also a `PaymentError`.

Therefore:

```python
except PaymentError:
```

can catch both `PaymentError` and its child exceptions.

This allows us to choose between:

```python
except PaymentDeclineError:
```

for specific handling, or:

```python
except PaymentError:
```

for general payment-error handling.

---

### 11. When to catch vs propagate

The most important production rule:

> **Catch an exception when you can meaningfully handle it. Otherwise, let it propagate to a layer that can handle it.**

Example:

```text
Hotel Provider
      ↓
raises RoomUnavailableError
      ↓
Booking Service
      ↓
propagates
      ↓
API Layer
      ↓
handles the error
      ↓
appropriate response to user
```

Don't catch exceptions just because you can.

---

## Built / Practiced

* Division function with `try / except`
* `else` for successful execution
* `finally` for cleanup
* Multiple exception handlers
* `raise`
* Re-raising with bare `raise`
* Exception chaining with `from e`
* Custom payment exceptions
* Exception inheritance
* Propagation of exceptions through application layers

## Key Mental Models

### Exception flow

```text
Something fails
      ↓
Exception is raised
      ↓
Can this layer handle it?
   ↙          ↘
 YES           NO
  ↓             ↓
catch it     propagate it
                ↓
          higher layer
```

### Exception hierarchy

```text
Exception
   │
   └── PaymentError
          │
          └── PaymentDeclineError
```

### Exception chaining

```text
ValueError
    ↓
    ↓ from e
    ↓
RuntimeError
```

## Questions

No major open questions. Exception handling, chaining, tracebacks, custom exceptions, inheritance, and propagation are understood.

## Tomorrow

### Day 8 — Dataclasses & Data Modeling

We'll learn:

* `@dataclass`
* Why dataclasses exist
* Dataclass fields
* Default values
* `field()`
* Immutable/frozen dataclasses
* Dataclasses vs normal classes
* Dataclasses vs Pydantic models
* When to use each in an AI/backend application
