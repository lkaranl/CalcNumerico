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

def reta(xi,yi,x):
    X=sympy.Symbol('X')
    n = len(xi)
    xii = []
    xiVyi = []
    j=0

    for v in xi:
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

    A = np.array([[sum_xii,sum_xi],[sum_xi,n]])
    B = np.array([[sum_xiVyi],[sum_yi]])
    y = np.linalg.solve(A,B)
    yy = (y[0]*X) + (y[1])
    fy = (y[0]*x) + (y[1])

    print("y = ax + b")
    print("y = {}".format(yy))
    print("Para x = {} --> f(y) aproximadamente {}".format(x,fy))

def parabola(xi,yi,x):
    X=sympy.Symbol('X')
    xiVyi = []
    xiiVyi = []
    xii = []
    xiii = []
    xiiii = []

    n = len(xi)

    j=0

    for v in xi:
        #xi vezes yi
        aux_xiVyi = xi[j] * yi[j]
        xiVyi.append(aux_xiVyi)
        
        #xi quadrado ** yi
        aux_xiiVyi = ((xi[j]**2)) * (yi[j])
        xiiVyi.append(aux_xiiVyi)

        #xi ao quadrado
        aux_xii = xi[j]**2
        xii.append(aux_xii)

        #xi ao cubo
        aux_xiii = xi[j]**3
        xiii.append(aux_xiii)

        #xi a quarta
        aux_xiiii = xi[j]**4
        xiiii.append(aux_xiiii)

        j+=1
    #Somatorias
    sum_xi = sum(xi)
    sum_yi = sum(yi)
    sum_xiVyi = sum(xiVyi)
    sum_xii = sum(xii)
    sum_xiiVyi = sum(xiiVyi)
    sum_xiii = sum(xiii)
    sum_xiiii = sum(xiiii)

    A = np.array([[n,sum_xi,sum_xii],[sum_xi,sum_xii,sum_xiii],[sum_xii,sum_xiii,sum_xiiii]])
    B = np.array([[sum_yi],[sum_xiVyi],[sum_xiiVyi]])
    y = np.linalg.solve(A,B)

    c = y[0]
    b = y[1]
    a = y[2]

    rx = ((c) + (b*X) + (a*X**2))

    print("r(x) = ax^2 + bx + c")
    print("r(x) = {}".format(rx))

    fx =  ((c) + (b*x) + (a*x**2)) 
    print("Para x = {} --> f(y) aproximadamente {}".format(x,fx))