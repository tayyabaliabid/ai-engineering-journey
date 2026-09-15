# Day 4

## Learned

* `*args` collects positional arguments into a tuple.
* `**kwargs` collects keyword arguments into a dictionary.
* `*args` can also be used to unpack positional arguments when calling a function.
* `**kwargs` can also be used to unpack keyword arguments when calling a function.
* Decorators can use `*args` and `**kwargs` to support functions with different argument signatures.
* `functools.wraps` preserves metadata from the original function when using decorators.
* Without `@wraps(func)`, the decorated function's `__name__` becomes `wrapper`.
* With `@wraps(func)`, important metadata such as `__name__`, `__doc__`, and annotations are preserved.
* A generic decorator commonly follows this pattern:

```python
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
```

## Built

Created a generic `logger` decorator that:

* Accepts any number of positional arguments.
* Accepts any number of keyword arguments.
* Passes arguments to the original function.
* Preserves the original return value.
* Preserves the original function's metadata.

Final version:

```python
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("adding log")

        result = func(*args, **kwargs)

        print("finishing log")

        return result

    return wrapper
```

## Key Mental Model

### Receiving arguments

```python
def wrapper(*args, **kwargs):
```

means:

```text
*args    → collect positional arguments → tuple
**kwargs → collect keyword arguments   → dictionary
```

### Passing arguments

```python
func(*args, **kwargs)
```

means:

```text
*args    → unpack tuple
**kwargs → unpack dictionary
```

So:

```text
Function call
     ↓
wrapper(*args, **kwargs)
     ↓
args / kwargs collected
     ↓
func(*args, **kwargs)
     ↓
original function receives arguments
```

## Important Lesson

A decorator should ideally not change the original function's behavior or metadata unintentionally.

For example:

```python
result = func(*args, **kwargs)
return result
```

ensures the decorated function still returns its original result.

And:

```python
@wraps(func)
```

ensures the decorated function still looks like the original function to introspection, debugging, documentation tools, and frameworks.

## Questions

* No open questions today.
* `*args`, `**kwargs`, and `functools.wraps` are understood.

## Tomorrow

* Properly type decorators.
* Understand why normal type hints are not enough for a generic decorator.
* Learn `ParamSpec`.
* Learn `TypeVar`.
* Use `Callable`.
* Build a fully typed production-quality decorator.
* Connect this knowledge to the kind of typed Python code used in FastAPI and AI services.
