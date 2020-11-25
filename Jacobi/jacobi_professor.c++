#include<iostream>
#include<iomanip>
#include<math.h>

using namespace std;

int main(){

float a0=0.7;
float b0=-1.6;
float c0=0.6;

float maior1=1;
float maior2=1;

int n = 0;
float a=0,b=0,c=0;
float er1=0,er2=0,er3=0;

while((maior2/maior1)>0.01)
    n = n+1;
    a = (-2*b0 - c0 + 7)/10;
    b = (1/5)*(-8 - a0- c0);
    c = (1/10)*(6 - 2*a0 - 3*b0);

    er1=abs(a-a0);
    er2=abs(b-b0);
    er3=abs(c-c0);

    if (abs (a)> abs(b)){
        maior1=a;
    }else{maior1=b;}
    
    if (c>maior1){
        maior1=c;
    }
        
    if (er1<er2){
        maior2 = er2;
    }else{maior2 = er1;}
    
    if (er3>maior2){
        maior2 = er3;
        }
        
    cout<<c<<b<<a<<n<<endl;
    
    a0=a;
    b0=b;
    c0=c;
}