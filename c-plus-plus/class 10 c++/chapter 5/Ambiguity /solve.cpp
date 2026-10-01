//Using scope resolution operator to solve ambiguity

#include <iostream>
using namespace std;
class A{
public:
    void display(){
        cout<<"Base class A"<<endl;
    }
};
class B{
public:  
  void display(){
        cout<<"Base class B"<<endl;
    }
};
class C:public A,public B{
public:  
//   void display(){
//         // cout<<"Derived class C"<<endl;
//     }
};      
int main(){
            C c;    
            // c.display(); // Calls C's display() 

            c.A::display(); // Calls A's display()
            c.B::display(); // Calls B's display()
            // c.C::display(); // Calls C's display() again
            return 0;
}
// Methos 2 
// Overriding the display function in class C to resolve ambiguity  
// #include <iostream>
// using namespace std;
// class A{
// public:          
//     void display(){
//         cout<<"Base class A"<<endl;
//     }
// };   
// class B{
// public:  
//   void display(){
//         cout<<"Base class B"<<endl;
//     }
// };
// class C:public A,public B{   
// public:  
//     void display(){      

//         cout<<"Derived class C"<<endl;
//     }
// };
// int main(){
//             C c;    
//             c.display(); // Calls C's display()
//             return 0;
// }        


