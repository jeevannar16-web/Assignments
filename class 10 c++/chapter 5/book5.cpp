#include<iostream>
using namespace std;
class Vehicle{
    public:
    string make,model;
    int year;
    void setVehicleinfo(){
        cout<<"Enter  vehicle make,model,year"<<endl;
        cin>>make>>model>>year;
    }
    void showVehicleinfo(){
        cout<<"The vehicle make,model ,year is"<<make<<model<<year;
    }

};
class Car:public Vehicle{
    public:
    double enginecapacity;
    void setCarinfo(){
        setVehicleinfo();
        cout<<"enter engine capacity";
        cin>>enginecapacity;
    }
    void showCarinfo(){
        showVehicleinfo();
        cout<<"The car engine capacity is:"<<enginecapacity;
    }
};
class Truck:public Vehicle{
    public:
    int wheels;
    void setTruckinfo(){
        setVehicleinfo();
        cout<<"enter the wheels";
        cin>>wheels;
    }
    void showTruckinfo(){
        showVehicleinfo();
        cout<<"The number of wheels is"<<wheels;
    }
};
class Bicycle:public Vehicle{
    public:
    double wheelsize;
    void setBicycleinfo(){
        setVehicleinfo();
        cout<<"enter the wheelsize";
        cin>>wheelsize;
    }
        void showBicycleinfo(){
            showVehicleinfo();
            cout<<"The wheelsize is:"<<wheelsize;
        }
};
class Sedan:public Car{
    public:
    string luxarylevel;
    void setSedaninfo(){
        setCarinfo();
        cout<<"enter the luxary level";
        cin>>luxarylevel;
    }
    void showSedaninfo(){
        showCarinfo();
        cout<<"the luxary level is:"<<luxarylevel;
    }
};
class Pickup:public Truck{
    public:
    string cabtype;
    void setPickupinfo(){
        setTruckinfo();
        cout<<"enter the cabtype";
        cin>>cabtype;
    }
    void showPickupinfo(){
        showTruckinfo();
        cout<<"the cabtype is:"<<cabtype<<endl;
    }
};
class Mountainbike:public Bicycle{
    public:
    double frameweight;
    void setMountainbikeinfo(){
        setBicycleinfo();
        cout<<"enter teh frameweight";
        cin>>frameweight;
    }
    void showMountainbikeinfo(){
        showBicycleinfo();
        cout<<"The frameweight is:"<<frameweight;
    }
     
};
int main(){
    Sedan s1;
    s1.setSedaninfo();
    s1.showSedaninfo();

    Pickup p1;
    p1.setPickupinfo();
    p1.showPickupinfo();

    Mountainbike m1;
    m1.setMountainbikeinfo();
    m1.showMountainbikeinfo();
    return 0;
}
