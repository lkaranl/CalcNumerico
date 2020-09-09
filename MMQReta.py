import numpy as np
import sympy
'''
1) Encontrar a melhor reta que ajusta os valores abaixo: Reta --> y=ax*b
x  =  0,0.25,0.5,0.75,1
fx =  1,1.12840,1.6487,2.1170,2.7183

EXEMPLO VIDEO
xi  |yi
0   |1
1   |2
2   |3
2   |4
'''
X=sympy.Symbol('X')

# EXEMPLO VIDEO
# xi = [0,1,2,2]
# yi = [1,2,3,4]

#
xi = [0,0.25,0.5,0.75,1]
yi = [1,1.2840,1.6487,2.1170,2.7183]

# xi = [0,0.6931,1.0989,1.3863]
# yi = [3,5,6,8]


n = len(xi)
xii = []
xiVyi = []
j=0

for x in xi:
    #xi ao quadrado
    aux_xii = xi[j]**2
    xii.append(aux_xii)
    #xi vezes yi
    aux_xiVyi = xi[j] * yi[j]
    xiVyi.append(aux_xiVyi)
    j+=1
#Somatorias
sum_xi = sum(xi)
sum_yi = sum(yi)
sum_xii = sum(xii)
sum_xiVyi = sum(xiVyi)

print("{}a + {}b = {:.5f}".format(sum_xii,sum_xi,sum_xiVyi))
print("{}a + {}b = {:.5f}".format(sum_xi,n,sum_yi))

A = np.array([[sum_xii,sum_xi],[sum_xi,n]])
B = np.array([[sum_xiVyi],[sum_yi]])
y = np.linalg.solve(A,B)
yy = (y[0]*X) + (y[1])
fy = (y[0]*x) + (y[1])

x=1
print("y = ax + b")
print("y = {}".format(yy))
print("Para x = {} --> f(y) aproximadamente {}".format(x,fy))