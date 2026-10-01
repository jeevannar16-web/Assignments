#include <iostream>
using namespace std;
int main(){
    int number,remainder,revNum;
    cout<<"enter the integer"<<endl;
    cin>>number;

    while(number>0){
        remainder=number%10;
        cout<<remainder;
        number=number/10;
        };
}