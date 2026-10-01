#include <iostream>
using namespace std;
class Person{
    public:
    string name,address;
    // string address;
    void setPersoninfo(){
        cout<<"enter name and address"<<endl;
        cin>>name>>address;
    }
    void showPersoninfo(){
        cout<<"Name and address is="<<name<<address<<endl;
    }
};
class Employee{
    public:
    float salary;
    string jobtitle;
    void setEmployeeinfo(){
        cout<<"Enter salary and jobtitle";
        cin>>salary>>jobtitle;
    }
    void showEmployeeinfo(){
        cout<<"The salary and jobtitle is:"<<salary<<jobtitle<<endl;
    }
};
class Manager:public Person,public Employee{
    public:
    int no_ofemployee;
    void setManagerinfo(){
        setPersoninfo();
        setEmployeeinfo();
        cout<<"enter the no of employee"<<endl;
        cin>>no_ofemployee;
    }
    void showManagerinfo(){
        showPersoninfo();
        showEmployeeinfo();
        cout<<"THE number of employee they manage="<<no_ofemployee;
    }
    };
    int main(){
        Manager M1;
        M1.setManagerinfo();
        M1.showManagerinfo();
        return 0;
    }
