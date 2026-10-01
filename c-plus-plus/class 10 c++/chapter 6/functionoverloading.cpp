#include <iostream>
using namespace std;
class Addition{
    public:
    int Add(int X, int Y){
       return X+Y;
        }
        string Add(){
        string a="Jeevan";
        string b="Neupane";
       string  c=a+b;
       cout<<c<<endl;
       return c;
        }
};
int main(){
    Addition a1;
   cout<< a1.Add(5,10)<<endl;;
    a1.Add();
return 0;
}