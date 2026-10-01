#include <iostream>
#include <string>

using namespace std;
int main(){
    string grade;
    int code=0;
    cout<<"enter your grade (eg:A+,a,c+)"<<endl;
    cin>>grade;
if(grade == "A+" || grade == "a+") code = 1;
else if(grade == "A" || grade == "a") code = 2;
else if(grade == "B+" || grade == "b+") code = 3;
else if(grade == "B" || grade == "b") code = 4;
else if(grade == "C+" || grade == "c+") code = 5;
else if(grade == "C" || grade == "c") code = 6;
else if(grade == "D+" || grade == "d+") code = 7;
else if(grade == "D" || grade == "d") code = 8;
else if(grade == "F" || grade == "f") code = 9;
else code = 0; 

   /* if(grade=="A+"|| "a+") code=1;
  else if(grade=="A"|| "a") code=2;
   else if(grade=="B+"|| "b+") code=3;
   else if(grade=="B"|| "b") code=4;
   else if(grade=="C+"|| "c+") code=5;
   else if(grade=="C"|| "c") code=6;
   else if(grade=="D+"|| "d+") code=7;
   else if(grade=="D"|| "D") code=8;
   else  if(grade=="F"|| "F") code=9;
    else code=0;*/
    switch(code){
        case 1:
        cout<<"gpa:4.00"<<endl;
        break;
        case 2:
        cout<<"gpa:3.6"<<endl;
        break;
        case 3:
        cout<<"gpa:3.2"<<endl;
        break;
        case 4:
        cout<<"gpa:2.8"<<endl;
        break;
        case 5:
        cout<<"gpa:2.4"<<endl;
        break;
        case 6:
        cout<<"gpa:2.0"<<endl;
        break;
        case 7:
        cout<<"gpa:1.6"<<endl;
        break;
        case 8:
        cout<<"gpa:1.2"<<endl;
        break;
        case 9:
        cout<<"gpa:0.00"<<endl;
        break;
        default:
        cout<<"The corresponding gpa doesnt exist"<<endl;   
    }
  return 0;
    }
