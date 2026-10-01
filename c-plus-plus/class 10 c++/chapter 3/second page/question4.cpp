#include <iostream>
using namespace std;
class Rectangle{
    public:
    int length;
    int breadth;
    int calculate_area();

};
int Rectangle::calculate_area(){
    return length*breadth;
}
int main(){
    Rectangle R1;
    cout<<"enter length and breadth"<<endl;
    cin>>R1.length>>R1.breadth;
    cout<<"the area having length"<<R1.length<<"and"<<"breadth"<<R1.breadth<<"is="<<R1.calculate_area();
return 0;
}