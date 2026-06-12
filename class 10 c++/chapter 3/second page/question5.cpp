#include <iostream>
#include <string>
using namespace std;
class Person{
    public:
    string name;
    int age;
  Person(string n,int a){
    name=n;
    age=a;
  }
  ~Person(){
    cout<<"deconstructor was called"<<endl;
  }
};
int main()
{
    Person p1("jeevan",15);
    cout<<"name="<<p1.name<<endl;
    cout<<"age="<<p1.age<<endl;
return 0;
}
