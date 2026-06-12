#include <iostream>
#define pi 3.14
using namespace std;
class shape{
 public:
 int radius;
 int length;
 int width;
 int breadth;
 int calculate_area(){
    return 2*pi*radius;
 }
 int calculate_perimeter(){
    return 2*length*breadth;
 }
};
int main(){
    shape s1;
    s1.radius=10;
    s1.length=10;
    // s1.width=10;
    s1.breadth=10;
    cout<<s1.calculate_area();
    cout<<s1.calculate_perimeter();
}
