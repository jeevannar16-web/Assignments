#include <iostream>
using namespace std;
int main(){
	int num;
    cout<<"enter the number";
    cin>>num;
    if(num==0){
        cout<<" number is zero"<<endl;

    }
    else if(num%2==0)
    {
        cout<<num<<"is even";

    }
    else{
        cout<<"odd number";
    }
return 0;
}
