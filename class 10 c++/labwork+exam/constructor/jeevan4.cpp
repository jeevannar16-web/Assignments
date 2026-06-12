#include <iostream>
using namespace std;
class book{
    public:
    string title;
    string author;
    string publisher;
    book(string t,string a,string p){
        title=t;
        author=a;
        publisher=p;
    }
    /* void displaydetails(){
    cout<<"book drtails"<<endl;
   cout<<"tite<<title<<endl; 
   cout<<"author"<<author<<endl;
   cout<<"publisher"<<publisher<<endl;
}*/
};

int main(){
    book s1("hello","jeevan","diwash");
    cout<<"title name="<<s1.title<<endl;
    cout<<"author="<<s1.author<<endl;
    cout<<"PUBLISHER="<<s1.publisher<<endl;
    // s1.displaydetails();
    return 0;
}
