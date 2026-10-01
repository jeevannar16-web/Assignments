#include <iostream>
using namespace std;
int main(){
    int number,remainder,revNum=0;
    cout<<"enter the integer"<<endl;
    cin>>number;

    while(number>0){
        remainder=number%10;
        // number=number/10;
        revNum=(revNum*10)+remainder;
        number=number/10;
        };
        cout<<"reverse number is"<<revNum;
        return 0;
}