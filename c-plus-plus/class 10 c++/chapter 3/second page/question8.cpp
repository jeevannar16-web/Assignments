#include <iostream>
#include <cmath> 
using namespace std;

class Car {
public:
    string make;
    string model;
    int year;
    float price;


    //  void inputDetails();
    // void displayDetails();
    float calculateResaleValue();
};

// void Car::inputDetails() {
//     cout << "Enter car make: ";
//     cin >> make;

//     cout << "Enter car model: ";
//     cin >> model;

//     cout << "Enter car year: ";
//     cin >> year;

//     cout << "Enter car price: ";
//     cin >> price;
// }

// void Car::displayDetails() {
//     cout << "\nCar Information:\n";
//     cout << "Make: " << make << endl;
//     cout << "Model: " << model << endl;
//     cout << "Year: " << year << endl;
//     cout << "Price: $" << price << endl;
// }
float Car::calculateResaleValue() {
    int currentYear;
    cout << "\nEnter the current year to calculate resale value: ";
    cin >> currentYear;
    int age = currentYear - year;
    float resale = price * pow(0.85, age);

    return resale;
}


int main() {
    Car myCar;

    //  myCar.inputDetails();
    myCar.make="jeevan";
    myCar.model="toyata";
    myCar.year=2024;
    myCar.price=3000;
    // myCar.displayDetails();
    cout<<myCar.make;
    cout<<myCar.model;
    cout<<myCar.year;
    cout<<myCar.price;
    float resaleValue = myCar.calculateResaleValue();
    cout << "Estimated Resale Value: $" << resaleValue << endl;

    return 0;
}