#include <iostream>
#include <cstring>

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

class Employee {
private:
    PayComponent* comps;
    int count;

public:
    Employee() : comps(nullptr), count(0) {}
    ~Employee() { delete[] comps; }

    void addComponent(const PayComponent& pc) {
        PayComponent* newComps = new PayComponent[count + 1];
        for (int i = 0; i < count; ++i)
            newComps[i] = comps[i];
        newComps[count] = pc;
        delete[] comps;
        comps = newComps;
        ++count;
    }

    void removeComponent(int index) {
        if (index < 0 || index >= count) return;
        PayComponent* newComps = new PayComponent[count - 1];
        for (int i = 0, j = 0; i < count; ++i) {
            if (i != index)
                newComps[j++] = comps[i];
        }
        delete[] comps;
        comps = newComps;
        --count;
    }

    PayComponent* getComponents() const { return comps; }
    int getCount() const { return count; }
};

int main() {
    Employee emp;

    PayComponent base = {"Base", 1000.0f};
    PayComponent bonus = {"Bonus", 200.0f};
    PayComponent overtime = {"Overtime", 150.0f};

    emp.addComponent(base);
    emp.addComponent(bonus);
    emp.addComponent(overtime);

    PayCalc* calculators[2];
    calculators[0] = new FixedPayCalc();
    calculators[1] = new CommissionPayCalc();

    for (int i = 0; i < 2; ++i) {
        float pay = calculators[i]->compute(emp.getComponents(), emp.getCount());
        std::cout << "Pay using calculator " << i << ": " << pay << std::endl;
    }

    for (int i = 0; i < 2; ++i)
        delete calculators[i];

    return 0;
}
