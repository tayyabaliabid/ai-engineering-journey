# Day 11 — End-of-Day Notes

## Learned

1. **`Protocol`**

   * Defines a contract that an object can follow.
   * It describes what methods/behavior are required.

2. **Structural typing**

   * A class does not need to inherit from the Protocol.
   * If it provides the required methods with the expected structure, it can satisfy the Protocol.

3. **Loose coupling**

   * Code can depend on an interface/contract rather than a specific implementation.
   * This makes components easier to replace and test.

4. **Why this matters in backend/AI systems**

   * Multiple implementations can provide the same behavior.

   * For example:

     PaymentProcessor
     ↓
     ┌── StripePayment
     ├── PayPalPayment
     └── MockPayment

   * Later, the same pattern can be used for LLM providers, storage providers, external APIs, and other services.

## Built

Created:

* `PaymentProcessor` Protocol
* `StripePayment`
* `PayPalPayment`
* `MockPayment`
* `checkout()` function that depends on the Protocol rather than a specific payment provider

The important implementation was:

```python
def checkout(payment_processor: PaymentProcessor, amount: float) -> bool:
    return payment_processor.process_payment(amount)
```

The same `checkout()` function successfully worked with different payment providers.

## Key Mental Model

**Inheritance-based thinking:**

```
"This class must inherit from X."
```

**Protocol-based thinking:**

```
"This object must provide the behavior I need."
```

## Questions

No major questions remained after today's exercises.

## Tomorrow

**Day 12 — Abstract Base Classes (ABC)**

We'll compare `Protocol` with `ABC` and understand when you would choose one over the other.
