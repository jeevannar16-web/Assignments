#include <iostream>
using namespace std;

int main(){
    int n,fact=1;
    cout<<"Enter the number:";
    cin>>n;
    int i=1;
    while(i<=n){
        fact=fact*i;
        i++;
    }
    cout<<"The factorial of "<<n<<"is:"<<fact;


    return 0;
}