

#include <iostream>
using namespace std;
class Vehicle{
    public:
    string make;
    int year;
    string model;
    void setvehicleinfo(){
        cout<<"Enter vehicle make:"<<endl;
        cin>>make;
        cout<<"Enter vehicle year"<<endl;
        cin>>year;
        cout<<"Enter vehicle model"<<endl;
        cin>>model;   
    }
    void showvehicleinfo(){
        cout<<"Vehicle make: "<<make<<endl;
        cout<<"Vehicle year: "<<year<<endl;
        cout<<"vehicle model: "<<model<<endl;;
    }
};
class Car:public Vehicle{
    public:
    int eng_size;
    void setcarinfo(){
        setvehicleinfo();
        cout<<"Enter engine size: "<<endl;
        cin>>eng_size;
    }
    void showcarinfo(){
        showvehicleinfo();
        cout<<"Engine size: "<<eng_size<<endl;
    }
};
int main(){
    Car mycar;
    mycar.setcarinfo();
    mycar.showcarinfo();
    return 0;
}