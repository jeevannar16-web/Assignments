

#include <iostream>
using namespace std;

int main() {
        int i=1;
        loop:
        if(i<=10){
            if(i%2==0){
                cout<<i<<"";
            }

            i++;
           goto loop;
        }
    return 0;
}