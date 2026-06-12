#include <iostream>
using namespace std;
int main(){
    int num;
    cout<<"enter the number";
    cin>>num;
        if(num%2==0 && num%3==0 && num%5==0 && num%7==0){
    cout<<num<<"divisible by 2,3,5,7"<<endl;
        }
    else if(num%2==0){
        cout<<num<<"is divisible by 2";
    }
    else if(num%3==0){
        cout<<num<<"is divisible by 3";
    }
    else if(num%5==0){
        cout<<num<<"is divisible by 5";
    }
    else if(num%7==0){
        cout<<num<<"is divisible by 7";
    }
    else{
        cout<<"is not divisible by 2,3,5,7";
    }

return 0;

}
