# Day 5

## Learned

* `Callable`
* `TypeVar`
* `ParamSpec`
* Generic functions
* Generic decorators
* `P.args`
* `P.kwargs`
* Preserving function parameter types
* Preserving function return types
* Combining `Callable`, `ParamSpec`, and `TypeVar`
* Using `functools.wraps` with typed decorators
* Measuring execution time with `time.perf_counter()`

## TypeVar

`TypeVar` represents a type that should remain consistent across a function.

Example:

```python
T = TypeVar("T")

def identity(value: T) -> T:
    return value
```

Mental model:

```text
T goes in
   ↓
T comes out
```

`TypeVar` is useful when there is a relationship between input and output types.

It should not simply be used to mean "any type."

## Callable

`Callable` describes a callable's parameters and return type.

```python
Callable[[int, int], int]
```

means:

> A callable that accepts two integers and returns an integer.

## ParamSpec

`ParamSpec` is useful when we need to preserve an entire function's parameter specification.

```python
P = ParamSpec("P")
```

Then:

```python
Callable[P, T]
```

means:

> A callable that accepts parameters represented by `P` and returns `T`.

For decorators, this is especially useful because different functions can have completely different parameter lists.

## P.args and P.kwargs

```python
def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
```

means the wrapper accepts the same parameter structure as the original function.

* `P.args` → positional arguments
* `P.kwargs` → keyword arguments

## Fully Typed Decorator

Built a generic decorator:

```python
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def execute(func: Callable[P, T]) -> Callable[P, T]:

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print("initial statement")

        result = func(*args, **kwargs)

        print("ending statement")

        return result

    return wrapper
```

## Final Challenge — `measure_time`

Built a fully typed execution-time decorator:

```python
def measure_time(func: Callable[P, T]) -> Callable[P, T]:

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:

        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        print(f"Execution time: {elapsed} seconds")

        return result

    return wrapper
```

This decorator:

* Accepts any function.
* Supports positional arguments.
* Supports keyword arguments.
* Preserves parameter typing.
* Preserves return typing.
* Preserves function metadata.
* Measures execution time.
* Returns the original result.

## Important Mental Model

A properly typed generic decorator:

```text
             Original Function
                    │
                    ↓
             Callable[P, T]
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
     ParamSpec P          TypeVar T
          │                   │
     Parameters          Return type
          │                   │
          └─────────┬─────────┘
                    ↓
                 wrapper
                    │
                    ↓
             Callable[P, T]
```

### Questions

* No open questions today.
* `Callable`, `TypeVar`, and `ParamSpec` were understood through implementation and the final challenge.

### Tomorrow

* Move beyond decorators.
* Learn **context managers**.
* Understand `with`.
* Learn `__enter__` and `__exit__`.
* Build custom context managers.
* Understand why context managers are important for resources such as database connections, files, locks, and transactions.
* Connect the concept to real backend/AI service code.
