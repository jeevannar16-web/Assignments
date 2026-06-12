#include <iostream>
using namespace std;
    class student{
        public:
        string name;
        int rollno;
        int Class;
        int mark1,mark2,mark3;
        student(string n,int roll,int cls,int m1,int m2,int m3){
            name = n;
            rollno =roll,
            Class =cls;
            mark1 = m1;
            mark2 =m2;
            mark3 = m3;
        }
    };
        int main(){
            student s1("JEEVAN",21,10,30,40,50);

            cout<<"name="<<s1.name<<endl;

            cout<<"student rollno "<<s1.rollno<<endl;

            cout<<"class"<<s1.Class<<endl;

            cout<<"marks of student "<<s1.mark1 <<""<<s1.mark2 <<""<<s1.mark3 <<endl;
            
            cout<<"total marks=" <<s1.mark1+s1.mark2+s1.mark3<<endl;

        return 0;
    }