#include <iostream>
using namespace std;
int main(){
    int number,remainder,revNum=0;
    cout<<"Enter the integer"<<endl;
    cin>>number;
    int orginalnum=number;

    while(number>0){
        remainder=number%10;
        number=number/10;
        revNum=(revNum*10)+remainder;
        // number=number/10;
        };

        if(revNum==orginalnum){
            cout<<"palindrome";
        }
        else{
            cout<<"not palindrome";
        }
        return 0;
}