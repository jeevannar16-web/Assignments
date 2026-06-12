#include <iostream>
using namespace std;
class Animal{
    public:
    string name;
    int age;
    void setAnimalinfo(){
        cout<<"Enter name and age:";
        cin>>name>>age;
    }
    void showAnimalinfo(){
        cout<<"The name and age is:"<<name<<age;
    }
};
class Mammal:public Animal{
    public:
    string animaltype;
    void setMammalinfo(){
        setAnimalinfo();
        cout<<"Enter the animal type:"<<endl;
        cin>>animaltype;
    }
    void showMammalinfo(){
        showAnimalinfo();
        cout<<"The animal type="<<animaltype;
    }
};
class Dog:public Mammal{
    public:
    string breed;
    void setDoginfo(){
        setMammalinfo();
        cout<<"enter the dog breed";
        cin>>breed;
    }
    void showDoginfo(){
        showMammalinfo();
        cout<<"The dog breed="<<breed;
    }
};
int main(){
    Dog D1;
    D1.setDoginfo();
    D1.showDoginfo();
    return 0;
    
}