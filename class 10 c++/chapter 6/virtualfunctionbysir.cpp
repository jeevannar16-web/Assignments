// A virtual function is a member function of a class that is declared using the keyword virtual and is overridden in a derived class. Its ensures that the correct functio is called at runtine based on the object type,not the pointer type.


#include <iostream>
using namespace std;        
class Base {
public:
    virtual void display() { // Virtual function
        cout << "Base class display function" << endl;
    }
};              

class Derived : public Base {
public:   
void display(){
    cout<<"This is the show function of derived class"<<endl;
}
};
int main(){
   Derived d;
    Base* ptr = &d; // Base class pointer pointing to Derived class object
    ptr->display(); // Calls the display function of the Derived class due to virtual function mechanism
    return 0;
}

