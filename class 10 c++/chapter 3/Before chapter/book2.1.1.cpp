#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define PI 3.14

class Circle {
public:
    float radius;
    float diameter;

    // Calculates diameter from radius
    float calculate_diameter() {
        return 2 * radius;
    }

    // Calculates area using radius
    float calculate_area() {
        return PI * radius * radius;
    }

    // Calculates circumference using radius
    float calculate_circumference() {
        return 2 * PI * radius;
    }

    // Calculates radius from diameter
    float calculate_radius() {
        return diameter / 2;
    }

    /*void display(){
    cout<<"Radius:"<<radius<<endl;
    cout<<"diameter"<<calculateDiameter()<<endl;
    cout<<"Circumference"<<calculatecircumference()<<endl;
    cout<<"area:"<<calculatearea()<<endl;
    }*/
};

int main() {
    Circle cric;

    // Input radius
    cout << " Enter the radius of the circle: ";
    cin >> cric.radius;

    // Display results based on radius
    cout << "\n📐 Circle Properties (from radius):\n";
    cout << "➤ Diameter       : " << cric.calculate_diameter() << endl;
    cout << "➤ Area           : " << cric.calculate_area() << endl;
    cout << "➤ Circumference  : " << cric.calculate_circumference() << endl;

    // Input diameter
    cout << "\nEnter the diameter of the circle: ";
    cin >> cric.diameter;

    // Display radius from diameter
    cout << "\n📐 Derived Radius:\n";
    cout << "➤ Radius         : " << cric.calculate_radius() << endl;

    return 0;
}