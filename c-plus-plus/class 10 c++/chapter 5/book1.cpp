#include <iostream>
using namespace std;
class Animal{
    public:
    int age;
    string name;
    void setanimalinfo(){
        cout<<"Enter animal name: "<<endl;
        cin>>name;
        cout<<"Enter animal age: "<<endl;
        cin>>age;
    }
    void showanimalinfo(){
        cout<<"Animal name: "<<name<<endl;
        cout<<"Animal age: "<<age<<endl;
    }
};
class Dog:public Animal{
    public:
    string breed;
    void setdoginfo(){
        setanimalinfo();
        cout<<"Enter dog breed: "<<endl;
        cin>>breed;
    }
    void showdoginfo(){
        showanimalinfo();
        cout<<"Dog breed: "<<breed<<endl;
    }    
};
int main(){
    Dog mydog;
    mydog.setdoginfo();
    cout<<"Dog information = "<<endl;
    mydog.showdoginfo();
    return 0;
}