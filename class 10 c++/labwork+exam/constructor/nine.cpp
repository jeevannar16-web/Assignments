#include <iostream>
using namespace std;
  class Book{
    private:
    string ti;
    string at;
    string pub;
    bool isA;
    public:
    Book(string t,string a,string p,bool av){
    ti=t;
    at=a;
    pub=p;
    isA=av;
    }
    ~Book(){
        cout<<"Deconstructor called"<<endl;
    }
    void displaydetails(){
        cout<<"Title="<<ti<<endl;
        cout<<"Author="<<at<<endl;
        cout<<"Publisher"<<pub<<endl;
        cout<<"Avaibility"<<(isA?"Available":"not available")<<endl;
        /*if (isA) {
        cout << "Availability = Yes" << endl;
    } else{
        cout << "Availability = No" << endl;
    }
*/
    }
  };
  int main(){
    Book b1("the old man","Jeevan","jeevan publication",0);
    Book b2("Puspha","Jeevan","jeevan.1 publication",2);
    cout<<"Book details"<<endl;
    b1.displaydetails();
    b2.displaydetails();
  }
