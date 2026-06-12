#include <iostream>
using namespace std;
class car{
  public:
  string name;
  string model;
  car(string n,string m){
    name=n;
    model=m;
  }
  car(const car&c){
      name=c.name;
     model=c.model;
  }
};
int main(){
    car c1("bugati","Rh554");
    car c2=c1;
    cout<<"name="<<c2.name<<endl;
    cout<<"model="<<c2.model<<endl;
}