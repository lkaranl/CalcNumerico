#include<iostream>
#include<iomanip>
#include<math.h>

/* Arrange systems of linear
equations to be solved in
diagonally dominant form
and form equation for each
unknown and define here
*/
/* In this example we are solving
3x + 20y - z = -18
2x - 3y + 20z = 25
20x + y - 2z = 17
*/
/* Arranging given system of linear
equations in diagonally dominant
form:
20x + y - 2z = 17
3x + 20y -z = -18
2x - 3y + 20z = 25
*/

/* 
EXEMPLO VIDEO
10x + 2y + z = 7
x + 5y + z = -8
2x + 3y + 10z = 6
*/

/* EXEMPLO VIDEO
x = (7 - 2y -z)/10
y = (-8 -x -z)/5
z = (6 -2x -3y)/10
*/
/* Equations:
x = (17-y+2z)/20
y = (-18-3x+z)/20
z = (25-2x+3y)/20
*/
/* Defining function */
// #define f1(x,y,z)  (17-y+2*z)/20
// #define f2(x,y,z)  (-18-3*x+z)/20
// #define f3(x,y,z)  (25-2*x+3*y)/20

// # x = ((6 -y -z)/3)
// # y = ((-x - 8 + z)/3)
// # z = ((-x - y - 6)/3)
// 4x + y + 0 = 10
// x + 4y + 0 = 6
// 0 + 0 + 0 = 0

// (10 - y) /4
// (-x +6)/4
// 0

// # (5-y-z)/5
// # (-3*x +6 -z)/1
// # (-3*x - y + 0)/6

// # (3 - 2*y - w)/3
// # (-9*x +6 -3*z - 4*w)/8
// # (6*x -4*y +16)/8
// # (-3*x +8*x -3x* +18)/4


// # (231 - y) / 1
// # (242 - z) / 1
// # (-x + 281) / 1


// #  (-3 -2*y -2*w - 4*z) /1
// #  (-2x +14 -3*w +3*z) / 1
// # (+3*x -y -7 +0) / 2
// # (-4*y +6 - z) / 4



#define f1(x,y,z,w)  (-3 -2*y -2*w - 4*z) /1
#define f2(x,y,z,w)  (-2*x +14 -3*w +3*z) / 1
#define f3(x,y,z,w)  (+3*x -y -7) / 2
#define f4(x,y,z,w)  (-4*y +6 -z) / 4


using namespace std;
float maior_ant;
float maior_atu;
float dr;
/* Main function */
int main(){
   float x0=0, y0=0, z0=0, w0=0, x1, y1, z1, w1, e1, e2, e3, e4, e;
   float x11,y11,z11,w11;
   int step=1;

   /* Setting precision and writing floating point values in fixed-point notation. */
   cout<< setprecision(8)<< fixed;

   /* Input */
   /* Reading tolerable error */
   cout<<"Digite o erro toleravel: ";
   cin>>e;

   cout<< endl<<"Ite\tx\t\ty\t\tz"<< endl;
   do{
      /* Calculation */
      x1 = f1(x0,y0,z0,w0);
      y1 = f2(x1,y0,z0,w0);
      z1 = f3(x1,y1,z0,w0);
      w1 = f3(x1,y1,z1,w0);
      cout<< step<<"\t"<< x1<<"\t"<< y1<<"\t"<< z1<< w1<< endl;

      x11 = fabs(x1);
      y11 = fabs(y1);
      z11 = fabs(z1);
      w11 = fabs(w1);


      if(x11>y11){
         maior_ant = x11;
      }else{
         maior_ant = y11;
      }
      if ( z11 > maior_ant){
         maior_ant = z11;
      }
      if ( w11 > maior_ant){
         maior_ant = w11;
      }


      /* Error */
      //   e1 = fabs(x0-x1);
      //   e2 = fabs(y0-y1);
      //   e3 = fabs(z0-z1);
      e1 = fabs(x0-x1);
      e2 = fabs(y0-y1);
      e3 = fabs(z0-z1);
      e4 = fabs(w0-w1);


      if(e1>e2){
         maior_atu = e1;
      }else{
         maior_atu = e2;
      }
      if(e3 > maior_atu){
         maior_atu = e3;
      }
      if(e4 > maior_atu){
         maior_atu = e4;
      }


      dr = maior_atu / maior_ant;
      
      step++;
      /* Set value for next iteration */
      x0 = x1;
      y0 = y1;
      z0 = z1;
      w0 = w1;
   }while(e<dr);
   //}while(e1>e && e2>e && e3>e);
   //cout << endl <<e1 << endl <<e2 << endl <<e3;
   //  cout<<"Maior atual (e1,e2,e3): "<<maior_atu<<endl
   //    <<"Maior anterior (x1,y1,z1): "<<maior_ant<<endl
   //    <<"dr: "<<dr;
   cout<< endl<<"Solucao: x = "<< x1<<", y = "<< y1<<" and z = "<< z1<<" and w = "<<w1<<endl;
   cout<<"Erro obtido com a solucao: "<<dr<<endl;
   return 0;
}
