#include <iostream>
using namespace std;

int main(){
    int num;

    do{
   cout<<"Enter the positive number: ";
   cin>>num;
    }while(num<=0);
     cout<<"You entered:"<<num<<endl;
    return 0;
}
/*
#include <iostream>
using namespace std;

int main() {
    int number;

    // do-while loop to ensure the prompt runs at least once
    do {
        cout << "Enter a positive number: ";
        cin >> number;

        if (number <= 0) {
            cout << "Invalid input. Please enter a positive number." << endl;
        }

    } while (number <= 0);

    cout << "You entered: " << number << endl;

    return 0;
}*/