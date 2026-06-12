#include <iostream>
using namespace std;
int main(){
    int age;
  float income;
  cout<<"Enter your age: ";
  cin>>age;
  if(age<18){
    cout<<"You are not eligible to vote"<<endl;
  }
  else if(age>=18 && age<=65){
    /* The line `cout<<"Enter your income";` is prompting the user to enter their income. This message
    will be displayed on the console, indicating to the user that they should input their income
    value. */
    cout<<"Enter your income";
    
    
    
    
    cin>>income;

    if(income<100000){
      cout<<"You are not eligible to pay taxes"<<endl;
    }
    else{
        cout<<"You are eligible to pay taxes";
    }
  }    
    return 0;
}