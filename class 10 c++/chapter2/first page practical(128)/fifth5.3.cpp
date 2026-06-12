#include <iostream>
using namespace std;
int main(){
    int num=2,product=1,count=0;
    while(count<5){
        if(num%2==0){
       product*=num;
       count++;
        }
        num++;

    }
    cout<<"the product is:"<<product;

return 0;

}
