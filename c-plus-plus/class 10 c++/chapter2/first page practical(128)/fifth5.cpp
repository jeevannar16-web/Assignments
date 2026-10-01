#include <iostream>
using namespace std;
int main(){
    int num=1,product=1;
    while(num<=10){
        if(num%2==0){
            product=product*num;
            
        }

        num++;
    }
    cout<<"the product is:"<<product;

return 0;

}
