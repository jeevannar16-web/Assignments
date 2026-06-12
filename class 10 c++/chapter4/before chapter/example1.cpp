#include <iostream>
using namespace std;
class car{
    private:
    void fuelInjection(){
        cout<<"Fuel injected into engine"<<endl;
    }
    public:
    void startcar(){
        fuelInjection();
        cout<<"Car started successfully"<<endl;
    }
    void stopcar(){
        cout<<"car stopped"<<endl;
    }
};
int main(){
    car mycar;
    mycar.startcar();
    mycar.stopcar();
    return 0;
}