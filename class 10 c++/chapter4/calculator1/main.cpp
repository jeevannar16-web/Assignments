#include <iostream>
#include "calculator.h"

using namespace std;

int main() {
    calculator calc;
    cout << "Addition: " << calc.add(10, 10) << endl;
    cout << "Subtraction: " << calc.sub(10, 4) << endl;
    return 0;
}