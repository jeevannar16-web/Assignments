#include <iostream>
#include <cmath> // for M_PI

// Base class
class Shape {
public:
    void calculateArea() {
        std::cout << "Area of shape cannot be determined in base class." << std::endl;
    }
};

// Circle class
class Circle : public Shape {
public:
    double radius;
    void calculateArea() {
        double area = M_PI * radius * radius;
        std::cout << "Area of Circle: " << area << std::endl;
    }
};

// Triangle class
class Triangle : public Shape {
public:
    double base, height;
    void calculateArea() {
        double area = 0.5 * base * height;
        std::cout << "Area of Triangle: " << area << std::endl;
    }
};

// Rectangle class
class Rectangle : public Shape {
public:
    double length, width;
    void calculateArea() {
        double area = length * width;
        std::cout << "Area of Rectangle: " << area << std::endl;
    }
};

int main() {
    Circle c;
    c.radius = 5;   // set value directly
    c.calculateArea();

    Triangle t;
    t.base = 10;
    t.height = 6;
    t.calculateArea();

    Rectangle r;
    r.length = 8;
    r.width = 4;
    r.calculateArea();

    return 0;
}
