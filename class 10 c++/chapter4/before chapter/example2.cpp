#include <iostream>
using namespace std;

class calculator{
    private:
    int add(int a,int b){
        return a+b;
    }
    int sub(int a,int b){
        return a-b;
    }
    public:
    void showdetails(int x,int y){
        cout<<"addition"<<add(x,y)<<endl;
        cout<<"subtraction"<<sub(x,y)<<endl;
    }
};
int main(){
    calculator calc;
    calc.showdetails(10,6);
    return 0;
}
