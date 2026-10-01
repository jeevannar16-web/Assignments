#include <iostream>
using namespace std;
class Car{
    public:
    string make,model;
    int year;
    void setCarinnfo(){
        cout<<"Enter car make,model,year";
        cin>>make>>model>>year;
    }
    void showCarinfo(){
        cout<<"The car make,model,year="<<make<<""<<model<<""<<year;
    }
};
class Sportcar:public Car{
    public:
    int cartopspeed;
    void setSportcarinfo(){
        setCarinnfo();
        cout<<"Enter the car speed";
        cin>>cartopspeed;
    }
    void showSportcarinfo(){
        showCarinfo();
        cout<<"The car speed is:"<<cartopspeed;
    }

};
int main(){
    Sportcar s1;
    s1.setSportcarinfo();
    s1.showSportcarinfo();
    return 0;
}