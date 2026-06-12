#include <iostream>
#include <cmath>
using namespace std;

class Shape {
public:
    string type;
    double radius;
    double length;
    double width;

    void setCircle(double r) {
        type = "circle";
        radius = r;
    }

    void setRectangle(double l, double w) {
        type = "rectangle";
        length = l;
        width = w;
    }

    double area() {
        if (type == "circle") {
            return M_PI * radius * radius;
        } else if (type == "rectangle") {
            return length * width;
        } else {
            return 0;
        }
    }

    double perimeter() {
        if (type == "circle") {
            return 2 * M_PI * radius;
        } else if (type == "rectangle") {
            return 2 * (length + width);
        } else {
            return 0;
        }
    }

    void display() {
        cout << "Shape: " << type << endl;
        cout << "Area: " << area() << endl;
        cout << "Perimeter: " << perimeter() << endl;
    }
};

// 🧪 Example usage
int main() {
    Shape s1, s2;

    s1.setCircle(5);
    s2.setRectangle(10, 4);

    s1.display();
    cout << endl;
    s2.display();

    return 0;
}