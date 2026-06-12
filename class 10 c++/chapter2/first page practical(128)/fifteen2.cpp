/*largest among three number using if else statement*/


#include <iostream>
using namespace std;
int main(){
    int num1,num2,num3;
    cout<<"enter the numbers:";
    cin>>num1>>num2>>num3;
    if(num1>num2 && num1>num3){
        cout<<num1<<"is largest";
    }
    else{
        if(num2>num3){
            cout<<num2<<"is largest";
        }
        else{
        cout<<num3<<"is largest";
        }

    }
return 0;

}
