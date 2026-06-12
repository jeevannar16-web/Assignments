#include <iostream>
using namespace std;
class Person{
    public:
    string name,address;
    void setPersoninfo(){
        cout<<"Enter name and adress:";
        cin>>name>>address;
    }
    void showPersoninfo(){
        cout<<"Name and address="<<name<<address<<endl;
    }
};
class Student{
    public:
    string major;
    double gpa;
    void setStudentinfo(){
        cout<<"Enter major and gpa:";
        cin>>major>>gpa;
    }
    void showStudentinfo(){
        cout<<"The major and gpa="<<major<<gpa<<endl;
    }
};
class Graduatestudent:public Person,public Student{
    public:
    string tthesistopic;
    void setGraduatestudentinfo(){
        setPersoninfo();
        setStudentinfo();
        cout<<"Enter the thesis topic";
        cin>>tthesistopic;
    }
    void showGraduatesstudentinfo(){
        showPersoninfo();
        showStudentinfo();
        cout<<"The thesis topic="<<tthesistopic;
    }
};
int main(){
    Graduatestudent g1;
    g1.setGraduatestudentinfo();
    g1.showGraduatesstudentinfo();
    return 0;
}