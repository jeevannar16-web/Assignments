#include <iostream>
using namespace std;
int main(){
    int num=2,product=1,count=0;
    while(count<5){
       product*=num;
        num+=2;
        count++;
    }
    cout<<"the product is:"<<product;

return 0;

}
