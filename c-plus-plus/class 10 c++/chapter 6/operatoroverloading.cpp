#include <iostream>
using namespace std;
#define pi 3.14
class Shape{
    public:
    virtual void area()=0;
    virtual Shape & operator++()=0;
    virtual Shape & operator--()=0;
};
class Rectangle:public Shape{
    int length,width;
    public:
    Rectangle(int l=0,int w=0):length(l),width(w){}
    void area(){
        cout<<"Area of rectangle:"<<length*width<<endl;
    }
    Rectangle & operator++(){
        ++length;
        ++width;
        return *this;
    }
    Rectangle&operator --(){
        --length;
        ++width;
        return *this;
    }
};
class Circle:public Shape{
    int radius;
public:
Circle(int r=0):radius(r){}
void area(){
    cout<<"Area of circle:"<<pi*radius*radius<<endl;
}
Circle& operator++(){
    ++radius;
    return *this;
}
    Circle& operator--(){
        --radius;
        return *this;
    }

};
int main(){
    Rectangle rect(10,5);
    Circle circ(5);
    Shape *ptr1=&rect;
    Shape *ptr2=&circ;
    ptr1->area();
    ++(*ptr1);
    ptr1->area();

    ptr2->area();
    ++(*ptr2);
    ptr2->area();

    return 0;

}