#include <iostream>
using namespace std;
class Employee{
public:
string name;
float salary;
void setEmployeeinfo(){
    cout<<"Enter name and salary:"<<endl;
    cin>>name>>salary;
}
void showEmployeeinfo(){
    cout<<"Name and salary is="<<name<<salary;
}
};
class Manager:public Employee{
    public:
    int no_ofemployee;
    void setManagerinfo(){
        setEmployeeinfo();
        cout<<"Enter the no of employee:"<<endl;
        cin>>no_ofemployee;
    }
    void showManagerinfo(){
        showEmployeeinfo();
        cout<<"Employee they manage is:"<<no_ofemployee<<endl;
    }        
};
class Executive:public Manager{
    public:
    int no_ofdepartment;
    void setExecutiveinfo(){
        setManagerinfo();
        cout<<"enter the no of department"<<endl;
        cin>>no_ofdepartment;
    }
    void showExecutiveinfo(){
        showManagerinfo();
        cout<<"The number of department they observe="<<no_ofdepartment;
        }
};
int main(){
    Executive E1;
    E1.setExecutiveinfo();
    E1.showExecutiveinfo();
    return 0;
}
