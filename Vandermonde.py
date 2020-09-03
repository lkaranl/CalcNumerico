import numpy as np
import sympy        

#   EXEMPLOS DE PONTOS
# pontos = [(x,y), (x,y) ...]
# pontos = [(1,0),(-1,0),(0,1)]
# pontos = [(3,120),(5,195),(9,225)]
#pontos = [(-1,0),(1,2),(2,7),(3,26)]
pontos = [(3,20),(5,30),(7,50)]

n = len(pontos)
def vandermond(pontos):
    xs,ys = zip(*pontos)
    A = [[x ** k for k in range(n)] for x in xs]
    B = ys
    a = np.linalg.solve(A,B)
    return a

def aux_a():
    return vandermond(pontos)

def p(x):
    a = aux_a()
    px = sum([a[k] * x ** k for k in range(n)])
    return  px

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

def equation(pontos):
    # eq = "p(x) = "
    a = aux_a()
    eq = "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
    return eq

def imprimir():
    print("Método de Vandermonde\n")
    eq = equation(pontos)

    aa = sympy.expand(eq)
    print("Polinomio -->",eq)
    print("Polinomio Simplificado --> ",aa)

    px = float(input("Qual ponto deseja? "))
    ppx = p(px)
    print("Se P (x) = {} --> {}".format(px,ppx))

if __name__ == "__main__":
    imprimir()

