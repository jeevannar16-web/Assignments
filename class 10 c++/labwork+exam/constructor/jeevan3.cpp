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
        student(student &s){ 
            name=s.name;
            rollno=s.rollno;
            Class=s.Class;
            mark1=s.mark1;
            mark2=s.mark2;
            mark3=s.mark3;

        }
    };
        int main(){
            student s1("JEEVAN",21,10,30,40,50);
            student s2 =s1;
            cout<<"name="<<s2.name<<endl;
            cout<<"student rollno "<<s2.rollno<<endl;
            cout<<"Class="<<s2.Class<<endl;
            cout<<"marks of student "<<s2.mark1 <<""<<s2.mark2 <<""<<s2.mark3 <<endl;
            cout<<"total marks=" <<s2.mark1+s2.mark2+s2.mark3<<endl;

        return 0;
    }