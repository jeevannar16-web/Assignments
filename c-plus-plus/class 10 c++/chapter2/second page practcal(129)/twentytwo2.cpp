/*a simple calculator to calculate   addition ,subtraction,multiplication ,and division using switch case*/

#include <iostream>
using namespace std;

int main() {
        int num1,num2,sum,sub,mul,div;
        cout<<"enter two numbers: ";
        cin>>num1>>num2;
        int choice;
        cout<<"\n1.Find sum:\n2.Find sub:\n3.Find mul:\n4'Find div:";
        cin>>choice;
       
        switch(choice){
               case 1:
               sum=num1+num2;
               cout<<"Sum of"<<num1<<"and"<<num2<<"is:"<<sum;// num1+num2;
               break;
               case 2:
               sub=num1-num2;
               cout<<"Sub of"<<num1<<"and"<<num2<<"is:"<<sub;// num1-num2;
               break;
               case 3:
               mul=num1*num2;
               cout<<"Mul of"<<num1<<"and"<<num2<<"is:"<<mul;// num1*num2;
               break;
               case 4:
                div=num1/num2;
            if (num2 != 0){
                cout<<"Div of"<<num1<<"and"<<num2<<"is:"<<div;// num1/num2;
            }
            else{
                cout <<"Error: Division by zero!" << endl;
            }
            break;
        default:
            cout << "Invald choice" << endl;
        }
    return 0;
}