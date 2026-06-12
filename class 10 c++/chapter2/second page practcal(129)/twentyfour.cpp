/*a simple calculator to calculate   addition ,subtraction,multiplication ,and division using switch case*/

#include <iostream>
using namespace std;

int main() {
        int num1,num2,num3;
        cout<<"Enter three numbers: ";
        cin>>num1>>num2>>num3;
        int largest;
        if(num1>num2 && num1>num3){
            largest=num1;
        }
        else{
            if(num2>num3){
                largest=num2;
            }
            else{
                largest=num3;
            }
        }
        cout<<"The largest number is"<<largest<<endl;
        if(num1==num2 && num2==num3 && num1==num3){
            cout<<"All three numbers are  equal"<<endl;
        }
        else if(num1==num2 || num2==num3){
            cout<<"Two numbers are equal";
        }
        else{
            cout<<"All are different";
        }
        
    return 0;
}