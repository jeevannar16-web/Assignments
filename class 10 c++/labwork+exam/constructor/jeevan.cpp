#include <iostream>
using namespace std;
    class student{
        public:
        string name;
        int rollno;
        int Class;
        int mark1,mark2,mark3;
        student(){
            name="jeevan";
            rollno=1;
            Class=10;
            mark1=30;
            mark2=40;
            mark3=50;
        }
    };
        int main(){
            student s1;
            cout<<"name="<<s1.name<<endl;
            cout<<"student rollno "<<s1.rollno<<endl;
            cout<<"class"<<s1.Class<<endl;
            cout<<"marks of student "<<s1.mark1<<s1.mark2<<s1.mark3<<endl;
            cout<<"total marks=" <<s1.mark1+s1.mark2+s1.mark3<<endl;
        return 0;
    }