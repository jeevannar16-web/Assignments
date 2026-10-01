#include <iostream>
using namespace std;

class Box
{
private:
    double length, breadth, height;

    // private function to calculate volume
    double getVolume() const
    {
        return length * breadth * height;
    }

public:
    // public function to set box information
    void setBoxInfo(double l, double b, double h)
    {
        length = l;
        breadth = b;
        height = h;
    }

    // operator overloading for 
    Box operator+(const Box& b)
    {
        Box temp;
        temp.length = this->length + b.length;
        temp.breadth = this->breadth + b.breadth;
        temp.height = this->height + b.height;
        return temp;
    }

    // function to display volume
    void displayVolume() const
    {
        cout << "Volume = " << getVolume() << endl;
    }
};

int main()
{
    Box box1, box2, box3;
    double volume=0.0;

    // setting values for box1 and box2
    box1.setBoxInfo(2, 3, 4);
    box2.setBoxInfo(1, 2, 3);
    // box3.setBoxInfo(0, 0, 2); // initializing box3 with zero dimensions
   

    // adding box1 and box2, storing in box3
    box3 = box1 + box2;

    cout << "Box 1 ";
     box1.displayVolume();
    

    cout << "Box 2 ";
    box2.displayVolume();

    cout << "Box 3 (Box1 + Box2) ";
    box3.displayVolume();

    return 0;
}