#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    if (number % 2 == 0){
        cout << "The number is even"<< endl;
    }
    if (number % 2 != 0){
        cout << "The number is odd" << endl;
    }

    return 0;
}