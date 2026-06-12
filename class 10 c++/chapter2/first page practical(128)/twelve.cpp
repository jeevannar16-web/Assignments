#include <iostream>
using namespace std;
int main(){
    char ch;
    cout<<"enter the character";
    cin>>ch;
    if((ch>='a'&&ch<='z')||(ch>='A'&&ch<='Z')){
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'){
            cout<<ch<<"is a vowel";
        }
        else{
            cout<<ch<<"is a consonant";

        }
    }
    else if(ch>='0' && ch<='9'){
        cout<<"its a digit";

    }
    else{
        cout<<"special character";
    }
	
return 0;
}
