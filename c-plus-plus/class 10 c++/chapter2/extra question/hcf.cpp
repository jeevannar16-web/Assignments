#include <iostream>
using namespace std;

int main() {
    int a, b, hcf = 1;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    // Find HCF using loop
    for (int i = 1; i <= a && i <= b; i++) {
        if (a % i == 0 && b % i == 0) {
            hcf = i;
        }
    }

    // Find LCM
    int lcm = (a * b) / hcf;

    cout << "HCF = " << hcf << endl;
    cout << "LCM = " << lcm << endl;

    return 0;
}
