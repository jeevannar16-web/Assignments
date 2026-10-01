#include <iostream>
using namespace std;

// Base class
class Employee {
public:
    double basicSalary;
    double allowances;
    double deductions;

    // Method to calculate Gross Pay
    double calculateGrossPay() {
        return basicSalary + allowances;
    }

    // Method to calculate Net Pay
    double calculateNetPay() {
        return calculateGrossPay() - deductions;
    }
};

// Derived class Manager (inherits Employee)
class Manager : public Employee {
public:
    // Method to calculate Bonus
    double calculateBonus() {
        return 0.10 * calculateGrossPay(); // 10% of Gross Pay
    }
};

// Derived class Executive (inherits Manager)
class Executive : public Manager {
public:
    // Method to calculate Stock Options
    double calculateStockOptions() {
        return 0.05 * calculateGrossPay(); // 5% of Gross Pay
    }
};

int main() {
    Executive e;

    // Assign values
    e.basicSalary = 50000;
    e.allowances = 10000;
    e.deductions = 5000;

    // Display results
    cout << "Gross Pay: " << e.calculateGrossPay() << endl;
    cout << "Net Pay: " << e.calculateNetPay() << endl;
    cout << "Bonus (Manager): " << e.calculateBonus() << endl;
    cout << "Stock Options (Executive): " << e.calculateStockOptions() << endl;

    return 0;
}
