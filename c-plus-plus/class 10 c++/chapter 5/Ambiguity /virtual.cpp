//Solution using virtual functions to resolve ambiguity in multiple inheritance
#include <iostream>
using namespace std;
class A{
public:   
 virtual void display(){
        cout<<"Base class A"<<endl;
    }
};
class B{
public:   
 virtual void display(){
        cout<<"Base class B"<<endl;
    }
};
class C:public A,public B{
public:    
void display(){
        cout<<"Derived class C"<<endl;
    }
};
int main(){
            C c;    
            c.display(); // Calls C's display()
            c.A::display(); // Calls A's display()
            // c.B::display(); // Calls B's display()
            return 0;
}  

// Diamond class problem solution using virtual inheritance

#include <iostream>
using namespace std;
class A{        
public:   
 virtual void display(){
        cout<<"Base class A"<<endl;
    }
};
class B:virtual public A    {   
public:   
 virtual void display(){
        cout<<"Base class B"<<endl;
    }
};
class C:virtual public A{   
public:    
void display(){
        cout<<"Derived class C"<<endl;
    }
};
class D:public B,public C{  

public:    
void display(){             
        cout<<"Derived class D"<<endl;
    }
};  
int main(){
            D d;    
            d.display(); // Calls D's display()
            d.B::display(); // Calls B's display()
            d.C::display(); // Calls C's display()
            return 0;           
}