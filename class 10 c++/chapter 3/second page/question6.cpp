#include <iostream>
using namespace std;

class Student {
public:
    string name;
    int rollNo;
    int marks1, marks2, marks3;

    // void inputDetails();   
    int calculateTotal();     
    void displayDetails(); 
};        

// void Student::inputDetails() {
    // cout << "Enter name: ";
    // cin >> name;
    // cout << "Enter roll number: ";
    // cin >> rollNo;
    // cout << "Enter marks in three subjects:\n";
    // cin >> marks1 >> marks2 >> marks3;
// }

int Student::calculateTotal() {
    return marks1 + marks2 + marks3;
}

void Student::displayDetails() {
    cout << "\n--- Student Details ---\n";
    cout << "Name: " << name << endl;
    cout << "Roll No: " << rollNo << endl;
    cout << "Marks: " << marks1 << ", " << marks2 << ", " << marks3 << endl;
    cout << "Total Marks: " << calculateTotal() << endl;
}

int main() {
    Student s;
    s.name="jeevan";
    s.rollNo=21;
    s.marks1=21;
    s.marks2=23;
    s.marks3=23;

    // s.inputDetails();
    s.displayDetails();
    return 0;
}