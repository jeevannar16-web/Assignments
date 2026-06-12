#include <iostream>
using namespace std;
int main(){
 int num;
 cout<<"Input the number"<<endl;
 cin>>num;
 if(num>0){
    cout<<num<<"is positive"<<"";

 }
else if(num<0){
    cout<<num<<"is negative"<<"";

}
else{
    cout<<"Number is zero"<<"";

}
return 0;
}
