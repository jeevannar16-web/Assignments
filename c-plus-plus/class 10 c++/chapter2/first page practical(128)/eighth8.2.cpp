#include <iostream>
using namespace std;
int main(){
    char  ch;
    cout<<"enter the alphabet";
     cin>>ch;
     if((ch>='a'&& ch<='z')||(ch>='A' && ch<='Z')){
        switch(ch){
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
    case 'A':
    case 'E':
    case 'I':
    case 'O':
    case 'U':
    cout<<ch<<"is  a vowel";
    break;  
    default:
    cout<<ch<<"is a consonant"<<endl;
     }}
    else{
        cout<<"Invalid input!Please enter a alphabet character"<<endl;
    }
     
return 0;

}