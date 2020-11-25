import numpy as np
import math

'''
     3
EX: S 1/x dx, com 4 subintervalos
     1

EXERCICIO
     2
EX: S sqrt(1+x^3) dx, com 4 subintervalos
     0
'''
#Valores da integral
erro = (math.log(1) - math.log(0))

#Para n= subintervalos h=(b-a)/n
a = 1
b = 0
n=1
h= abs((b-a)/n)

xi = []
yi = []
for inter in range(0,n+1):
    xi.append(b)
    b = b+h
i=0
for inter in xi:
    aux_yi = 1/xi[i]
    yi.append(aux_yi)
    i+=1

s = (h/2) * (yi[0]+2*(yi[1]+yi[2]+yi[3])+yi[4])
print("A soma foi ~= {}".format(s))

ss = abs(erro - s)
print("Erro ~= {}".format(ss))
sss = (ss/erro)*100
print("Erro aproximado de {:.2f}%".format(sss))