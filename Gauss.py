#!/usr/bin/env python3.8
#NAME: Metodo de Gauss
#VERSION: 0.1
#DESCRIPTION:		
#DATE OF CREATION: 26/08/2020
#WRITTEN BY: Karan Luciano Silva
#E-MAIL: karanluciano1@gmail.com			
#DISTRO: Pop!_OS 20.04 LTS
#LICENSE: GPLv3 			
#PROJECT: https://github.com/lkaranl/

# EXEMPLO 
# 10x + 2y + z = 7
# x + 5y + z = -8
# 2x + 3y + 10z = 6

# x = (7 - 2y -z)/10
# y = (-8 -x -z)/5
# z = (6 -2x -3y)/10
import os
class Gauss():
    
    def f1(self,x,y,z):
        fx = ((7-2*y-z)/10) #Edite aqui a sua funcao
        return fx

    def f2(self,x,y,z):
        fx = ((-8-x-z)/5) #Edite aqui a sua funcao
        return fx

    def f3(self,x,y,z):
        fx = ((6-2*x-3*y)/10) #Edite aqui a sua funcao
        return fx

    def main(self):
        print("#### Método de Gauss####\nDiga o metodo que prefere (1 ou 2)")
        print("")
        x = input("Metodo de Gauss-Jacobi (1)\nMetodo de Gauss-Seidel (2)\nOpcao: ")
        Gauss().escolha(x)

    def escolha(self,x):
        if ((x == 1) or (x == '1')):
            os.system("clear")
            Gauss().jabobi()
        elif ((x == 2) or (x == '2')):
            os.system("clear")
            Gauss().seidel()
        else:
            os.system("clear")
            print("OPCAO INVALIDA")
            Gauss().main()

    def maior_menor(self,a,b,c):
        if(a>b):
            maior = a
        else:
            maior = b
        if(c>maior):
            maior = c
        return (maior) 

    def jabobi(self):
        x0,y0,z0 = 0,0,0
        dr=9999999
        contador = 1
        #erro = float(input("Diga o erro: "))
        erro = 0.001
        print("\nIte\tx\t\t\ty\t\t\tz")
        
        while(erro<dr):
            x1 = Gauss().f1(x0,y0,z0)
            y1 = Gauss().f2(x0,y0,z0)
            z1 = Gauss().f3(x0,y0,z0)
            
            x_aux = abs(x1)
            y_aux = abs(y1)
            z_aux = abs(z1)
            print("{}\t{:.6f}\t\t{:.6f}\t\t{:.6f}".format(contador,x1,y1,z1))

            maior_anterior = Gauss().maior_menor(x_aux,y_aux,z_aux)
            
            e1 = abs(x0-x1)
            e2 = abs(y0-y1)
            e3 = abs(z0-z1)

            maior_atual = Gauss().maior_menor(e1,e2,e3)

            dr = (maior_atual / maior_anterior)

            contador +=1

            x0 = x1
            y0 = y1
            z0 = z1

        print("-"*88)
        print("x: {:.6f}\ny: {:.6f}\nz: {:.6f}".format(x1,y1,z1))
        print("Erro aproximado da solucao: {:.6f}".format(dr))
        print("")
        Gauss().main()

    def seidel(self):
        x0,y0,z0 = 0,0,0
        dr=9999999
        contador = 1
        #erro = float(input("Diga o erro: "))
        erro = 0.001
        print("\nIte\tx\t\t\ty\t\t\tz")
        x1 = Gauss().f1(x0,y0,z0)
        y1 = Gauss().f2(x0,y0,z0)
        z1 = Gauss().f3(x0,y0,z0)
        print("{}\t{:.6f}\t\t{:.6f}\t\t{:.6f}".format(contador,x1,y1,z1))
        contador +=1

        while(erro<dr):
            x1 = Gauss().f1(x0,y1,z1)
            y1 = Gauss().f2(x1,x1,z1)
            z1 = Gauss().f3(x1,y1,z1)
            print("{}\t{:.6f}\t\t{:.6f}\t\t{:.6f}".format(contador,x1,y1,z1))
            
            x_aux = abs(x1)
            y_aux = abs(y1)
            z_aux = abs(z1)
            

            maior_anterior = Gauss().maior_menor(x_aux,y_aux,z_aux)
            
            e1 = abs(x0-x1)
            e2 = abs(y0-y1)
            e3 = abs(z0-z1)

            maior_atual = Gauss().maior_menor(e1,e2,e3)

            dr = (maior_atual / maior_anterior)

            contador +=1

            x0 = x1
            y0 = y1
            z0 = z1

        print("-"*88)
        print("x: {:.6f}\ny: {:.6f}\nz: {:.6f}".format(x1,y1,z1))
        print("Erro aproximado da solucao: {:.6f}".format(dr))
        print("")
        Gauss().main()

if __name__ == "__main__":
    os.system("clear")
    Gauss().main()
