# C++ OOP Final Project — Employee Pay Calculator

## Assigned Task

Design a C++ program that:
- Computes employee pay using dynamically allocated pay components.
- Uses an abstract base class `PayCalc` with two derived classes:
  - `FixedPayCalc` – sums all components.
  - `CommissionPayCalc` – uses base pay plus 10% of other components.
- Demonstrates inheritance, polymorphism, and pointer arithmetic.
- Supports adding and removing pay components dynamically.

## How It Was Completed

- Defined a `PayComponent` struct to store pay items.
- Used dynamic allocation to manage an array of components.
- Created an abstract class `PayCalc` with a pure virtual function `compute()`.
- Derived `FixedPayCalc` and `CommissionPayCalc` from `PayCalc` to handle different logic.
- Used pointer arithmetic for accessing and summing data.
- Implemented functions to add and remove components by resizing the array.
- Fully annotated the code with comments explaining each section.

## Annotated Code Snippet

```cpp
struct PayComponent {
    char desc[30];
    float amount;
};

class PayCalc {
public:
    virtual float compute(const PayComponent* comps, int n) = 0;
    virtual ~PayCalc() {}
};

class FixedPayCalc : public PayCalc {
public:
    float compute(const PayComponent* comps, int n) override {
        float total = 0;
        for (int i = 0; i < n; ++i)
            total += (comps + i)->amount;
        return total;
    }
};

class CommissionPayCalc : public PayCalc {
public:
    float compute(const PayComponent* comps, int n) override {
        float base = 0, commission = 0;
        for (int i = 0; i < n; ++i) {
            if (strcmp((comps + i)->desc, "Base") == 0)
                base += (comps + i)->amount;
            else
                commission += (comps + i)->amount * 0.10f;
        }
        return base + commission;
    }
};
