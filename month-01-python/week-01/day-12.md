# Day 12 — End-of-Day Notes

## Learned

1. **Abstract Base Classes (ABC)**

   * ABCs define a contract that subclasses must follow.
   * They use `ABC` and `@abstractmethod`.

2. **Abstract methods**

   * An abstract method defines a required behavior.
   * A subclass must implement it before the subclass can be instantiated.

3. **ABC enforcement**

   * An ABC cannot be instantiated while it still has unimplemented abstract methods.
   * A subclass that doesn't implement the required abstract method also cannot be instantiated.

4. **Protocol vs ABC**

   **Protocol**

   * Primarily defines a structural contract.
   * A class doesn't need to inherit from the Protocol.
   * It focuses on whether an object provides the required behavior.

   **ABC**

   * Defines an inheritance-based contract.
   * The subclass must inherit from the ABC.
   * Python enforces abstract methods when creating an instance.

5. **The key mental model**

   Protocol:

   ```
   "Does this object provide the behavior I need?"
   ```

   ABC:

   ```
   "You inherited from me, so you must implement my required behavior."
   ```

6. **Shared implementation**

   * A Protocol is primarily used to describe an interface/contract.
   * An ABC can also provide shared implementation for subclasses.

## Built

Created a payment-processing example using:

* `PaymentProcessor` as an ABC
* `StripePayment`
* `PayPalPayment`
* `TestPayment`

Tested what happens when:

* A valid subclass implements the abstract method.
* A subclass doesn't implement the abstract method.
* The ABC itself is instantiated.

## Key Takeaway

The most important distinction from today:

```
Protocol
    ↓
Structural typing
    ↓
"If it provides the required behavior, it can be compatible."

ABC
    ↓
Inheritance + enforcement
    ↓
"You must inherit and implement the required behavior."
```

## Questions

The main question about Protocols vs ABCs was resolved:

A class using a Protocol is not forced to implement the Protocol at runtime simply because it exists. An ABC, however, prevents instantiation of subclasses that haven't implemented its abstract methods.

## Tomorrow

**Day 13 — Protocol vs ABC in a realistic backend design**

We'll use both approaches in a practical example and learn how to decide which one to use.
