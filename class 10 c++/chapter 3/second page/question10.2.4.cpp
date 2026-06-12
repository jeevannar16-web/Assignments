#include <iostream>
#include <cmath>
using namespace std;

class Shape {
private:
    string type;
    double radius;
    double length;
    double width;

public:
    // Constructor
    Shape(string t, double r = 0, double l = 0, double w = 0) {
        type = t;
        radius = r;
        length = l;
        width = w;
    }

    // Method to calculate area
    double area() {
        if (type == "circle") {
            return M_PI * radius * radius;
        } else if (type == "rectangle") {
            return length * width;
        } else {
            cout << "Unknown shape type.\n";
            return 0;
        }
    }

    // Method to calculate perimeter
    double perimeter() {
        if (type == "circle") {
            return 2 * M_PI * radius;
        } else if (type == "rectangle") {
            return 2 * (length + width);
        } else {
            cout << "Unknown shape type.\n";
            return 0;
        }
    }

    // Display method
    void display() {
        cout << "Shape: " << type << endl;
        cout << "Area: " << area() << endl;
        cout << "Perimeter: " << perimeter() << endl;
    }
};

// 🧪 Example usage
int main() {
    Shape circle("circle", 7);
    Shape rectangle("rectangle", 0, 10, 5);

    circle.display();
    cout << endl;
    rectangle.display();

    return 0;
}