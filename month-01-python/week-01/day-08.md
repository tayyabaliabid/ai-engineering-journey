# Day 8 — Dataclasses & Data Modeling

## Learned

### 1. `@dataclass`

A dataclass is a convenient way to create classes that primarily hold data.

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
```

Python automatically provides useful methods such as:

* `__init__()`
* `__repr__()`
* `__eq__()`

So:

```python
user1 = User(1, "Tayyab", "tayyab@example.com")
user2 = User(1, "Tayyab", "tayyab@example.com")

user1 == user2
```

returns:

```text
True
```

---

### 2. Default values

Dataclass fields can have default values:

```python
@dataclass
class User:
    name: str
    age: int
    active: bool = True
```

The fields without defaults must come before fields with defaults.

---

### 3. Mutable vs immutable

**Mutable** means an object can be changed after creation.

Examples:

```text
list
dict
set
```

**Immutable** means it cannot be changed in place.

Examples:

```text
int
float
str
bool
tuple
```

---

### 4. `field(default_factory=...)`

Don't use mutable objects directly as dataclass defaults:

```python
# ❌
roles: list[str] = []
```

Instead:

```python
# ✅
roles: list[str] = field(default_factory=list)
```

`default_factory=list` means:

> Create a new empty list for every instance.

Therefore:

```python
user1 = User("Tayyab")
user2 = User("Ali")

user1.roles.append("admin")
```

results in:

```text
user1.roles → ['admin']
user2.roles → []
```

Each object has its own list.

---

### 5. `field()`

`field()` allows additional configuration for a dataclass field.

Example:

```python
internal_code: str = field(repr=False)
```

This means the field won't appear when the dataclass object is printed.

Important:

```python
field(repr=False)
```

does **not** make the field optional.

It only controls its representation.

---

### 6. `frozen=True`

A frozen dataclass prevents normal attribute reassignment:

```python
@dataclass(frozen=True)
class ModelConfig:
    provider: str
    model: str
    temperature: float
```

Then:

```python
config.temperature = 3.5
```

raises:

```text
FrozenInstanceError
```

Useful for data/configuration that should remain unchanged after creation.

---

### 7. Dataclass vs Pydantic

This is an important distinction for backend and AI engineering.

**Dataclass:**

```text
Internal Python data
        ↓
Convenient data structure
```

**Pydantic:**

```text
External/untrusted data
        ↓
Validation + parsing
        ↓
Python object
```

Example:

```python
@dataclass
class Product:
    name: str
    price: float
```

Type annotations alone don't perform runtime validation.

Pydantic:

```python
class ProductModel(BaseModel):
    name: str
    price: float
```

Pydantic validates/parses data at runtime.

This is why Pydantic is heavily used with FastAPI.

---

## Built

During today's exercises, you built:

* `User` dataclasses
* Dataclasses with default values
* Dataclasses with mutable list fields
* Fields using `default_factory`
* Fields using `repr=False`
* Frozen configuration objects
* A `Product` dataclass
* A Pydantic `ProductModel`
* A practical comparison between dataclasses and Pydantic

---

## Questions

No major open questions from Day 8.

The most important concepts to retain are:

```text
@dataclass
    ↓
convenient Python data structure

field(default_factory=list)
    ↓
new list for every instance

field(repr=False)
    ↓
hide field from repr()

@dataclass(frozen=True)
    ↓
prevent attribute reassignment

Pydantic
    ↓
runtime validation/parsing
```

---

## Tomorrow — Day 9

We'll move on from dataclasses and continue with **Python data modeling / type-system concepts**, building toward the patterns you'll use in FastAPI and AI backend code.

The goal remains the same:

> Don't just know Python syntax — become comfortable reading and writing production-quality Python.
