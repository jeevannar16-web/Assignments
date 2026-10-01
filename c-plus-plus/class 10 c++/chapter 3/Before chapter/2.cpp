//finding area,diameter,circumference and radius of circle using class and object
#include <iostream>
using namespace std;

#define pi 3.14

class Circle{
    public:
    int radius;
    float diameter;
    float calculate_diameter();
    float  calculate_area();
    float calculate_circumference();
    //float calculate_radius();
};

float Circle::calculate_diameter(){
    return 2*radius;
}
float Circle::calculate_area(){
    return pi*radius*radius;
}
float Circle::calculate_circumference(){
    return 2*pi*radius;
}
//float Circle::calculate_radius(){
   // return diameter/2;}


int main(){
    Circle cric;
    cout<<"Enter the radius";
    cin>>cric.radius;
    //cric.calculate_diameter();
    //cric.calculate_area();
    //cric.calculate_circiumference();


    cout<<"The diameter of circle having radius "<<cric.radius<<"is"<<cric.calculate_diameter()<<endl;

cout<<"And"<<endl;

cout<<"The araa of circle having radius "<<cric.radius<<"is"<<cric.calculate_area()<<endl;
cout<<"And"<<endl;

cout<<"The circumference of circle having radius "<<cric.radius<<"is"<<cric.calculate_circumference()<<endl;
cout<<"And"<<endl;

//cout<<"Enter the diameter";
  //  cin>>cric.diameter;

//cout<<"The radius having diameter"<<cric.diameter<<"is"<<cric.calculate_radius()<<endl;
return 0;

}