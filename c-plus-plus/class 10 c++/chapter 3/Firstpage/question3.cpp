#include <iostream> 
using namespace std;
#define pi 3.14
class Circle{
    public:
    float radius;
    float diameter;
    float circumference;
    float calculate_diameter();
    float calculate_radius();
    float calculate_circumference();
};
float Circle::calculate_diameter(){
return 2*radius;
}
float Circle::calculate_radius(){
return diameter/2;
}
float Circle::calculate_circumference(){
return 2*pi*radius;
}
int main(){
    Circle c1;
    cout<<"enter the radius";
    cin>>c1.radius;
    cout<<"the diameter is"<<c1.calculate_diameter()<<endl;
    c1.diameter=5;
    cout<<"the radius is"<<c1.calculate_radius()<<endl;
    cout<<"the circumference is"<<c1.calculate_circumference()<<endl;
    return 0;
}

