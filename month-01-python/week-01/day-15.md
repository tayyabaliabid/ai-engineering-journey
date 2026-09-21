# Day 15 — Asyncio Tasks, Timeouts & Cancellation

## Learned

### 1. Coroutine vs Task

A coroutine is created when calling an `async def` function:

```python
fetch_users()
```

A Task schedules that coroutine on the event loop:

```python
task = asyncio.create_task(fetch_users())
```

Mental model:

```text
async def function
      ↓
   coroutine
      ↓
create_task()
      ↓
     Task
      ↓
event loop schedules it
```

A Task is useful when we want an async operation to start running while the current coroutine continues doing other work.

---

### 2. `asyncio.create_task()`

Example:

```python
users_task = asyncio.create_task(fetch_users())
bookings_task = asyncio.create_task(fetch_bookings())

print("Preparing response...")

users = await users_task
bookings = await bookings_task
```

Both tasks are scheduled before we await either result.

Therefore, two independent 2-second operations can complete in roughly:

```text
~2 seconds
```

rather than:

```text
~4 seconds
```

---

### 3. Timeout with `asyncio.wait_for()`

Used when an operation should not be allowed to run indefinitely:

```python
result = await asyncio.wait_for(
    slow_operation(),
    timeout=2
)
```

If the operation doesn't finish within 2 seconds:

```python
asyncio.TimeoutError
```

is raised.

The correct approach is to catch the specific exception:

```python
try:
    result = await asyncio.wait_for(
        slow_operation(),
        timeout=2
    )
except asyncio.TimeoutError:
    print("Operation timed out")
```

Avoid:

```python
except Exception:
```

when you know exactly which exception you expect.

---

### 4. Task Cancellation

A running Task can be manually cancelled:

```python
task.cancel()
```

Important: `task.cancel()` requests cancellation. The `CancelledError` is observed when awaiting the task:

```python
task.cancel()

try:
    await task
except asyncio.CancelledError:
    print("Operation cancelled")
```

Mental model:

```text
task.cancel()
     ↓
Cancellation requested
     ↓
await task
     ↓
CancelledError
     ↓
Handle cancellation
```

---

## Built

You practiced:

* Creating Tasks with `asyncio.create_task()`
* Continuing execution before awaiting Task results
* Applying timeouts with `asyncio.wait_for()`
* Catching `asyncio.TimeoutError`
* Manually cancelling Tasks with `.cancel()`
* Catching `asyncio.CancelledError`
* Measuring async execution time with `time.perf_counter()`

---

## Important Understanding

### Timeout vs Cancellation

```text
Timeout
  ↓
"The operation took too long."
  ↓
Automatically stop/wait-limit the operation
```

```text
Cancellation
  ↓
"I don't need this operation anymore."
  ↓
Explicitly request that the Task stop
```

These are especially important in backend services dealing with:

* External APIs
* Payment providers
* Hotel providers
* Database operations
* LLM APIs
* Network requests

---

## Key Mental Model

```text
                Async Operation
                      │
          ┌───────────┴───────────┐
          │                       │
      Timeout                 Cancellation
          │                       │
 wait_for(..., 2)             task.cancel()
          │                       │
 TimeoutError              CancelledError
```

## Tomorrow

**Day 16 — Async HTTP & Real Backend I/O**

We'll connect the async concepts you've learned to actual backend work:

```text
FastAPI
   ↓
async endpoint
   ↓
HTTP API call
   ↓
await response
   ↓
return result
```

We'll start using `httpx`, which will be particularly relevant later when you build AI services that call LLM APIs and other external services.
