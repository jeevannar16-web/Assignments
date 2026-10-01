#include <iostream>
#include <string>
using namespace std;

class BankAccount{
    private:
    string accountnumber;
    string accountholdername;
    double balance;
    public:
    BankAccount(string num,string name,double bal){
        accountnumber=num;
        accountholdername=name;
        balance=bal;
    }
    void deposit(double amount){
        if(amount>0){
            balance=balance+amount;
            cout<<"deposited:Rs"<<amount<<endl;
            cout<<"balance after deposited=Rs"<<balance<<endl;
        }
        else{
            cout<<"invalid deposit amount"<<endl;
        }
    }
    void withdraw(double amount){
if(amount>0 && amount<=balance){
    balance=balance-amount;
    cout<<"withdrew:Rs"<<amount<<endl;
    cout<<"balance after withdrew="<<balance<<endl;
}
else if(amount>balance){
    cout<<"insufficient fund"<<endl;
}
else{
    cout<<"invalid withdraw amount"<<endl;
}
    }
    void displayaccountdetails() {
        cout<<"Account number"<<accountnumber<<endl;
        cout<<"Account holder Name"<<accountholdername<<endl;
        cout<<"balance:Rs"<<balance<<endl;
    }
};
int main(){
   BankAccount myaccount("123456789","mr.XYZ",5000.0); 
    myaccount.displayaccountdetails();
   myaccount.withdraw(12);
   myaccount.deposit(12);
     myaccount.displayaccountdetails();
  

   return 0;
}