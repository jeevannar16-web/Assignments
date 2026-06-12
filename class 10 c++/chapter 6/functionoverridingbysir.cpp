//function overrriding is a feature where a derived class provides its own definition of a member function that is already defined in its base class with the same name and signature.
//name , return type and parameters
#include <iostream>
using namespace std;
class Parent{
    public:
    void display(){
        cout<<"This is Parent class display function."<<endl;
    }
    };

    class child:public Parent{
    public:
    void display(){
        cout<<"This is Child class display function."<<endl;
    }
};
int main(){
    
    child c;
    c.display(); // Calls child class display function

    return 0;
}

    
