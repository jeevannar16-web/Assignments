//finding volume of circle using class and object predefined length,breadth and height

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
    Cuboid cubo;
    cubo.length=5;
    cubo.breadth=5;
    cubo.height=1;
   // /*int*/ cubo.volume();
   int cubo_volume=cubo.volume();
    cout<<"Length:"<<cubo.length<<endl;
    cout<<"Breadth:"<<cubo.breadth<<endl;
    cout<<"Height:"<<cubo.height<<endl;
    cout<<"Volume:"<<cubo_volume<<endl;
    //cout<<"Volume:"<<cubo.volume();

return 0;

}

