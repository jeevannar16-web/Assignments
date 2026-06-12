#include <iostream>
using namespace std;
int main(){
 char ch;
 cout<<"Enter a alphabet"<<"";
 cin>>ch;
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
cout<<ch<<"is a vowel letter"<<"";
break;
default:
if((ch>='a' && ch<='z') || (ch>='A' && ch<='Z')){
   cout<<ch<<""<<"is a consonant"<<"";
}

else{
   cout<<"please enter a valid alphabet"<<"";
}


 }
return 0;

}

