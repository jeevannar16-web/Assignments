#include <iostream>
using namespace std;
int main(){
 int num;
 do{
    cout<<"Enter a number"<<endl;
    cin>>num;
    if(num!=0){
if(num%2==0){
    cout<<num<<"is even"<<endl;
}else{
    cout<<num<<"is odd"<<endl;
}
    }

 }while(num!=0);
return 0;
}
