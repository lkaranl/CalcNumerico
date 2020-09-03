import sympy        
from sympy import *                                             
x=sympy.Symbol('x')
import matplotlib.pyplot
import matplotlib.pyplot as mpl

class Poli():
    def Lagrange(self,z,xn):                                                 
        #1-b e c)
        escolha = int(input("Qual tabela: "))
        if (escolha == 1):
            lista=[-1,0,1,2] # X
            y=[7,4,1,4] # Y
        
        if (escolha == 2):
            #2-a)
            lista=[-2,-1,0,1] # X
            y=[-8,-3,-4,-5] # Y

        if (escolha == 3):
            #2-b)
            lista=[-2,0,1,2] # X
            y=[-8,4,4,16] # Y

        if (escolha == 4):
            #VIDEO
            lista=[3,7,10] # X
            y=[5,9,11] # Y

        if (escolha == 5):
            #Atividade 2
            lista=[1,1,2,3] # X
            y=[0,2,7,26] # Y    
        
        if (escolha == 6):
            #Atividade 2
            lista=[3,5,9] # X
            y=[120,195,225] # Y 

        xf=xn+z                                                      
        xu=xn        
        p=0                                                            
        for j in range(xu,xf): 
            resultado=1                                                 
            for i in range(0,z):                                        
                if xn!=i:                                             
                    resultado=resultado*((x-lista[i])/(lista[xn]-lista[i]))
            #print(resultado)
            p=p+(resultado*(y[j]))
            xn=xn+1                                                      
        print("Polinomio --> ",p)
        
        aa = sympy.expand(p)
        aaa = str(aa)
        dderivada = Poli().calDerivada(aaa)
        derivada = str(dderivada)

        print("Polinomio Simplificado --> ",aaa)
        print("Derivada do Polinomio  --> ",derivada)
        
        

        Poli().imprimir_(aaa,derivada)
            
    def imprimir_(self,p,derivada):
        self.p = p
        self.derivada = derivada
        x = float(input("P(x): "))
        
        c = eval(p)
        cc = eval(derivada)
        
        print("Se P (x) = {} --> {}".format(x,c))
        print("Se P'(x) = {} --> {}".format(x,cc))
 
    def calDerivada(self,fx):
        aux_derivada = diff(fx)
        return aux_derivada

    def main(self):
        Poli().Lagrange(3,0)


if __name__ == "__main__":
    Poli().main()

