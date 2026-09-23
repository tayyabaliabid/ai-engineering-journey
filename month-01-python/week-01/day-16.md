# Day 16 — Async HTTP with httpx

## Learned

### 1. Async HTTP with `httpx`

`httpx` provides an asynchronous HTTP client:

```python
async with httpx.AsyncClient() as client:
    response = await client.get("https://example.com")
```

Two concepts you've already learned are being combined here:

* `async with` → async context manager
* `await` → wait for an async I/O operation

Mental model:

```text
async with AsyncClient
        ↓
    HTTP request
        ↓
       await
        ↓
   HTTP response
```

---

### 2. HTTP Response

An `httpx.Response` contains information about the HTTP response.

Commonly used properties/methods:

```python
response.status_code
response.json()
response.raise_for_status()
```

Example:

```python
response = await client.get(url)

response.raise_for_status()

data = response.json()
```

---

### 3. `raise_for_status()`

`raise_for_status()` checks the HTTP status.

```text
2xx
 ↓
continue normally

4xx / 5xx
 ↓
HTTPStatusError
```

Example:

```python
response.raise_for_status()
```

The important point:

`raise_for_status()` doesn't return the response data. Its job is to **raise an exception when the HTTP status represents an error**.

---

### 4. HTTP Error Handling

You learned to catch the specific `httpx` exception:

```python
try:
    result = await fetch_data()
except httpx.HTTPStatusError:
    print("HTTP request failed")
```

Avoid unnecessarily broad:

```python
except Exception:
```

when you know what error you're expecting.

---

### 5. HTTP Timeouts

`httpx` has its own timeout mechanism.

```python
async with httpx.AsyncClient(timeout=2.0) as client:
```

This tells the HTTP client not to wait indefinitely for the HTTP operation.

If the timeout is exceeded:

```python
except httpx.TimeoutException:
    print("HTTP request timed out")
```

Mental model:

```text
AsyncClient(timeout=2)
        ↓
    HTTP request
        ↓
    waiting...
        ↓
   2 seconds
        ↓
TimeoutException
```

---

### 6. `asyncio.wait_for()` vs `httpx` timeout

You learned that these operate at different levels.

`asyncio.wait_for()`:

```python
await asyncio.wait_for(
    some_async_operation(),
    timeout=2
)
```

Controls an arbitrary async operation.

`httpx` timeout:

```python
httpx.AsyncClient(timeout=2.0)
```

Controls the HTTP operation.

Mental model:

```text
asyncio.wait_for()
    ↓
any async operation

httpx timeout
    ↓
HTTP operation
```

---

### 7. Concurrent HTTP Requests

You used:

```python
users, posts = await asyncio.gather(
    fetch_users(),
    fetch_posts()
)
```

This allows both HTTP requests to progress concurrently.

```text
                gather()
                /      \
               /        \
      fetch_users()   fetch_posts()
           ↓               ↓
       HTTP call        HTTP call
           ↓               ↓
           └───────┬───────┘
                   ↓
                results
```

This is one of the most useful patterns for backend services that need to call multiple independent APIs.

---

## Built

You built async HTTP functions using:

* `httpx.AsyncClient`
* `async with`
* `await client.get()`
* `response.status_code`
* `response.json()`
* `response.raise_for_status()`
* `httpx.HTTPStatusError`
* `httpx.TimeoutException`
* `asyncio.gather()`

You also built a concurrent example that retrieves:

```text
Users API
+
Posts API
    ↓
asyncio.gather()
    ↓
both results
```

---

## Important Backend Pattern

You've now learned this general pattern:

```text
Backend Service
      ↓
Async HTTP Client
      ↓
External API
      ↓
await response
      ↓
validate HTTP status
      ↓
parse JSON
      ↓
return structured data
```

This pattern will become extremely important when you start calling:

* OpenAI/LLM APIs
* embedding APIs
* payment services
* hotel providers
* internal microservices

---

## Important Observation

Your current implementation creates a separate `AsyncClient` inside each function:

```python
fetch_users()
    ↓
AsyncClient()

fetch_posts()
    ↓
AsyncClient()
```

This works.

However, production applications often **reuse HTTP clients** so that connections can be reused instead of creating a new client for every operation.

We'll cover this when we discuss reusable HTTP client design.

---

## Key Mental Model

```text
             Async Backend
                  │
                  ↓
             httpx Client
                  │
            ┌─────┴─────┐
            ↓           ↓
        API call     API call
            │           │
          await        await
            │           │
            └─────┬─────┘
                  ↓
             gather()
                  ↓
              Results
```

## Tomorrow

### Day 17 — Reusable Async HTTP Client

We'll move from:

```python
async def fetch_users():
    create client
    request
    destroy client
```

toward a more production-oriented design:

```text
Application
     ↓
Reusable HTTP Client
     ↓
Multiple API requests
```

We'll also start connecting this pattern with **FastAPI**, which will bring us closer to your `ai-service` project.
