// #!/usr/bin/env python3.8
// NAME:				Binario
// VERSION:			0.3
// DESCRIPTION:			Conversao base 10 para binario  
// DATE OF CREATION:		19/08/2020
// LAST RELEASE			19/08/2020
// WRITTEN BY:			KARAN LUCIANO SILVA
// E-MAIL:				karanluciano1@gmail.com			
// DISTRO:				ARCH LINUX
// LICENSE:			GPLv3 			
// PROJECT:			https://github.com/lkaranl/Inducao

#include <iostream>
using namespace std;

int main (){
    int num;
    int bin[8];
    int aux;

    cout<<"Diga o numero (base decimal) para ser convertido: ";
    cin>>num;

    for(aux = 7; aux >= 0;aux--){
        if(num % 2 == 0){
            bin[aux] = 0;
        }else{
            bin[aux] = 1;
        }
        num = num / 2;    
    }

    for(aux = 0; aux < 8; aux++){
        cout<<bin[aux];
    }
    cout<<"\n"<<endl;
}