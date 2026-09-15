# Day 6 — Context Managers

## Learned

### 1. Context managers

Context managers control setup and cleanup around a block of code.

```python
with TimerContext():
    print("Doing some work")
```

The basic flow is:

```text
__enter__()
    ↓
with block
    ↓
__exit__()
```

### 2. `__enter__()`

Runs when entering the `with` block.

It can return a value:

```python
def __enter__(self):
    return self
```

That value can be received using `as`:

```python
with TimerContext() as timer:
    timer.message()
```

### 3. `__exit__()`

Runs when leaving the `with` block, including when an exception occurs.

```python
def __exit__(self, exc_type, exc_value, traceback):
    ...
```

The three arguments provide information about an exception:

* `exc_type` → exception type, e.g. `ValueError`
* `exc_value` → actual exception object/message
* `traceback` → traceback information about where the exception occurred

If no exception occurs, these values are `None`.

### 4. Exception suppression

Returning `True` from `__exit__()` suppresses the exception:

```python
return True
```

Returning `False`, or returning nothing (`None`), allows the exception to propagate.

Important:

> Only return `True` when the context manager intentionally handled the exception.

### 5. `@contextmanager`

`contextlib` provides an easier way to create context managers:

```python
from contextlib import contextmanager

@contextmanager
def timer_context():
    print("Starting...")

    yield "Timer is running"

    print("Finishing")
```

The `yield` separates the setup from the code inside the `with` block.

```text
setup
  ↓
yield
  ↓
with block
  ↓
code after yield
```

### 6. Connection to generators

A `@contextmanager` function uses the generator mechanism you learned on Day 2.

`yield` pauses the function, allows the `with` block to execute, and then resumes the function afterward.

---

## Built

You built a custom class-based context manager:

```python
class TimerContext:

    def __enter__(self):
        print("Starting...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception: {exc_value}")

        print("Finishing")
```

You also built the `contextlib` version:

```python
from contextlib import contextmanager

@contextmanager
def timer_context():
    print("Starting..")

    yield "Timer is running"

    print("Finishing")
```

And successfully used:

```python
with timer_context() as message:
    print(message)
```

---

## Questions

* No open questions today.

## Tomorrow

### Day 7 — Exceptions & Error Handling

We'll go deeper into:

* `try`
* `except`
* `else`
* `finally`
* multiple exception types
* custom exceptions
* exception chaining
* when to catch vs propagate exceptions
* backend/API error-handling patterns

The goal will be to understand **production-quality error handling**, not just Python syntax.
