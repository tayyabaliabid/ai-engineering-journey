# Day 10 — End-of-Day Notes

## Learned

1. **Combining Python data-modeling tools**

   * `Enum` for named domain values.
   * `Literal` for a small set of allowed values.
   * `Pydantic` for runtime validation and parsing.
   * `dataclass` for structured internal application data.

2. **Enum + Pydantic**

   * Pydantic can validate an incoming string against an Enum.
   * `"confirmed"` can become `BookingStatus.CONFIRMED`.

3. **Literal + Pydantic**

   * `Literal["standard", "deluxe", "suite"]` restricts the allowed values.
   * Pydantic enforces this restriction at runtime.

4. **Dataclass vs Pydantic**

   * Pydantic is useful at application boundaries, such as API requests.
   * Dataclasses are useful for internal Python data structures.
   * Dataclass type annotations alone do not perform runtime validation.

5. **Important mental model**

   `Type hints describe.`
   `Pydantic validates.`

## Built

Created a small booking data model:

* `BookingStatus` Enum
* `Booking` Pydantic model
* `BookingDetails` dataclass
* `room_type` using `Literal`

Data flow:

```
API input
   ↓
Pydantic
   ↓
validation/parsing
   ↓
internal dataclass
   ↓
application logic
```

## Questions

No major open questions from today's exercises.

## Tomorrow

**Day 11 — Protocols**

We'll learn how Python can define an interface/contract without requiring classes to inherit from a common base class, and why this is useful for loosely coupled backend and AI services.
