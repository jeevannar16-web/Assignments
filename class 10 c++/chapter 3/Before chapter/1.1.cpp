//finding volume of circle using class and object user definedlength,breadth and height
#include <iostream>
using namespace std;
class Cuboid{
    public:
    int length;
    int breadth;
    int height;
    int volume();
};
int Cuboid::volume(){
    return length*breadth*height;
}
int main(){
    /*Cuboid cubo;
    cubo.length=5;
    cubo.breadth=5;
    cubo.height=1;*/
   Cuboid c;
   cout<<"Enter length,breadth,height: ";
   cin>>c.length>>c.breadth>>c.height;
   cout<<"The volume of cuboid having length "<<c.length<<""<<"breadth "<<c.breadth<<""<<"&height "<<c.height<<""<<"is"<<c.volume();
   // int cubo.volume();
   /*int cubo_volume=cubo.volume();
    cout<<"Length:"<<cubo.length<<endl;
    cout<<"Breadth:"<<cubo.breadth<<endl;
    cout<<"Height:"<<cubo.height<<endl;
    cout<<"Volume:"<<cubo_volume<<endl;*/
    //cout<<"Volume:"<<cubo.volume();

return 0;

}

