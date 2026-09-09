# Day 3

## Learned

* Functions are **first-class objects** in Python.
* Functions can be:

  * Assigned to variables
  * Passed as arguments to other functions
  * Returned from other functions
* Higher-order functions
* Closures
* A closure can remember values from its enclosing scope.
* Decorators
* The `@decorator` syntax is syntactic sugar for:

  ```python
  function = decorator(function)
  ```
* A decorator can modify or extend the behavior of a function without changing the original function's code.
* The decorator function receives the original function as an argument.
* The decorator normally returns a wrapper function.
* The wrapper can execute code before and/or after the original function.
* Important: the wrapper must **return the original function's result** if the decorated function is expected to return a value.

## Built

* Practiced assigning functions to variables.
* Practiced passing functions as arguments.
* Practiced returning functions.
* Built closure examples using `multiplier()` and `power()`.
* Built a basic `log_call` decorator.
* Used the `@log_call` syntax.
* Practiced preserving the decorated function's return value.

## Key Example

```python
def log_call(func):

    def wrapper(a, b):
        print("calling add")

        result = func(a, b)

        print("finished add")

        return result

    return wrapper


@log_call
def add(a: int, b: int) -> int:
    return a + b


result = add(2, 3)

print(result)
```

Output:

```text
calling add
finished add
5
```

## Important Lesson

A decorator should not accidentally change the behavior of the original function.

For example:

```python
result = func(a, b)
return result
```

is important because simply doing:

```python
print(func(a, b))
```

would print the result but cause the decorated function to return `None`.

## Questions

* No open questions today.
* All questions that came up during Day 3 were clarified.

## Tomorrow

* Learn `*args`
* Learn `**kwargs`
* Make decorators work with functions having different arguments
* Learn `functools.wraps`
* Understand why function metadata gets lost with decorators
* Add proper typing to decorators
* Build a generic, production-quality decorator
