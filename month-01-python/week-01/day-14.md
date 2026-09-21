# Day 14 — Async / Await and asyncio

## Learned

### 1. `async def`

Used to define an asynchronous function:

```python
async def fetch_data():
    ...
```

Calling an async function does not immediately execute it. It creates a **coroutine object**.

---

### 2. Coroutine

A coroutine is the object produced when calling an `async def` function.

```python
result = fetch_data()
```

At this point, `result` is a coroutine, not the function's returned value.

The coroutine needs to be awaited or executed through an event loop.

---

### 3. `await`

`await` waits for an asynchronous operation to complete:

```python
result = await fetch_data()
```

While the operation is waiting on something such as I/O, the event loop can work on other asynchronous tasks.

---

### 4. `asyncio.run()`

Used to start an asynchronous program from normal synchronous Python code:

```python
result = asyncio.run(main())
```

It runs the coroutine and returns its final result.

---

### 5. `asyncio.sleep()`

Used to simulate an asynchronous wait:

```python
await asyncio.sleep(2)
```

Unlike `time.sleep()`, this does not block the entire event loop during the wait.

---

### 6. Sequential async execution

This:

```python
users = await fetch_users()
bookings = await fetch_bookings()
```

runs the operations sequentially.

If each takes approximately 2 seconds:

```text
fetch_users()      → ~2 sec
fetch_bookings()  → ~2 sec

Total              → ~4 sec
```

---

### 7. `asyncio.gather()`

Used to run multiple awaitable operations concurrently:

```python
users, bookings = await asyncio.gather(
    fetch_users(),
    fetch_bookings()
)
```

Both operations can make progress while waiting.

```text
fetch_users()     ────────┐
                          │
fetch_bookings()  ────────┤
                          ↓
                       results
```

With both operations taking about 2 seconds:

```text
Total ≈ 2 seconds
```

rather than approximately 4 seconds.

---

### 8. `time.perf_counter()`

Used to accurately measure elapsed time:

```python
start = time.perf_counter()

# code

elapsed = time.perf_counter() - start
```

Used this to demonstrate the difference between sequential execution and `asyncio.gather()`.

---

## Important Understanding

**Async does not mean everything runs in parallel.**

The important concept is:

> Async allows multiple tasks to make progress concurrently, especially whil
