#include <iostream>
#include <cmath>
using namespace std;
#define pi 3.14
class Shape {
public:
    string type;
    double radius;
    double length;
    double width;

    double area() {
        if (type == "circle") {
            return pi * radius * radius;
        } else if (type == "rectangle") {
            return length * width;
        } else {
            return 0;
        }
    }

    double perimeter() {
        if (type == "circle") {
            return 2 * pi * radius;
        } else if (type == "rectangle") {
            return 2 * (length + width);
        } else {
            return 0;
        }
    };
};

int main() {
    Shape s1, s2;

    // Circle
    s1.type = "circle";
    s1.radius = 5;

    // Rectangle
    s2.type = "rectangle";
    s2.length = 10;
    s2.width = 4;

    cout << "Circle Area: " << s1.area() << endl;
    cout << "Circle Perimeter: " << s1.perimeter() << endl;

    cout << "\nRectangle Area: " << s2.area() << endl;
    cout << "Rectangle Perimeter: " << s2.perimeter() << endl;

    return 0;
}