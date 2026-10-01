#include <iostream>
using namespace std;
int main(){
	int num;
    
    do{
    
        cout<<"enter number between(1-10):";
        cin>>num;
    }
    while(num<=1 || num>=10);
return 0;
}
