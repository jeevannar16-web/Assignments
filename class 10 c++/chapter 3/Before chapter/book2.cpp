#include <iostream>
using namespace std;

class Circle {
private:
    double radius;
    double diameter;
    double circumference;

public:
    // Constructor
    Circle(double r) {
        radius = r;
        calculateDiameter();
        calculateCircumference();
    }

    // Method to calculate diameter
    void calculateDiameter() {
        diameter = 2 * radius;
    }

    // Method to calculate circumference
    void calculateCircumference() {
        circumference = 2 * 3.14159 * radius;
    }

    // Method to display all values
    void displayValues() {
        cout << "Radius: " << radius << endl;
        cout << "Diameter: " << diameter << endl;
        cout << "Circumference: " << circumference << endl;
    }
};

int main() {
    double inputRadius;
    cout << "Enter the radius of the circle: ";
    cin >> inputRadius;

    Circle c(inputRadius);
    c.displayValues();

    return 0;
}