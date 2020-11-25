import math

'''
INTEGRAÇÃO NUMÉRICA - REGRA DOS TRAPÉZIOS SIMPLES
  y2
  1.5 
S   xlnx dx = h/2(y1+y2)
  1.2
  y1


EXERCICIO
     2
EX: S sqrt(1+x**3) dx
     0

BEM SIMPLES, SUBSTITUI OS VALORES NA FUNCAO DX
'''
# # EXEOMPLO 1
# y1 = 1.2 
# y2 = 1.5

# h = y2-y1

# # RELEMBRE --> (h/2) * (y1+y2) 
# dx = (h/2)*(y1*math.log(y1)+(y2*math.log(y2)))

# print("Aproximadamente {:.4f}".format(dx))

# def simples():
#     #EXEMPLO 2
#     y1 = 2
#     y2 = 5

#     h = y2-y1

#     dx = (h/2)* (y1+y2)
#     #dx = (h/2)*(y1**2 + (1/y1**(1/3)) + (y2**2 + (1/y2**(1/3))))

#     print(dx)
# simples()

# EXERCICIO 1
def simples():
    y1 = 0
    y2 = 0.5

    h = abs(y2-y1)

    #dx = ((h/2) * (1/(1+y1**2)) + (1/(1+y2**2)))
    dx = (h/2) * (y1 + y2)
    #dx = (h/2)* (math.sqrt(1+y1**3) + math.sqrt(1+y2**3))
    print(dx)
simples()



'''
INTEGRAÇÃO NUMÉRICA - REGRA DOS TRAPÉZIOS COMPOSTO

'''
# def composto():
#     y1 = 0
#     y2 = 0.2
#     y3 = 0.4
#     y4 = 0.6
#     y5 = 0.8
#     y6 = 1
    
#     h = abs((y6-y1)/5) # DIVIDE PELO NUMERO DE SUB INTERVALOS

#     dx_composto = ((h/2) * (1/(1+(y1**2))) + (2*(1/(1+(y2**2)))) + (2*(1/(1+(y3**2)))) + (2*(1/(1+(y4**2)))) + (2*(1/(1+(y5**2)))) + (1/(1+(y6**2))))
    
    
#     #dx_composto = (h/2) * (((y1**2 + 3*y1)/(y1**2+1)) + 2*((y2**2 + 3*y2)/(y2**2+1)) + 2*((y3**2 + 3*y3)/(y3**2+1)) + 2*((y4**2 + 3*y4)/(y4**2+1)) + 2*((y5**2 + 3*y5)/(y5**2+1)) + (y6**2 + 3*y6)/(y6**2+1))

#     #dx_composto = (h/2) * ((1/(1+y1**2)) + 2*((1/(1+y2**2))) + 2*((1/(1+y3**2))) + 2*((1/(1+y4**2))) + 2*((1/(1+y5**2))) + (1/(1+y6**2)))

#     #dx_composto = (h/2) * ( y1 + 2*(y2) + 2*(y3) + 2*(y4) + 2*(y5) + y6)
#     #dx_composto = (h/2) * (1/(1+y1**2)) + (2*(1/(1+y2**2))) + (2*(1/(1+y3**2))) + (2*(1/(1+y4**2))) + (2*(1/(1+y5**2)))  + (1/(1+y6**2))
    
#     print(dx_composto)
# composto()


def composto():
    y1 = 0
    y2 = 0.1
    y3 = 0.2
    y4 = 0.3
    y5 = 0.4
    y6 = 0.5
    
    h = abs((y6-y1)/5) # DIVIDE PELO NUMERO DE SUB INTERVALOS

    dx_composto = ((h/2) * (1/(1+(y1**2))) + (2*(1/(1+(y2**2)))) + (2*(1/(1+(y3**2)))) + (2*(1/(1+(y4**2)))) + (2*(1/(1+(y5**2)))) + (1/(1+(y6**2))))
    
    
    #dx_composto = (h/2) * (((y1**2 + 3*y1)/(y1**2+1)) + 2*((y2**2 + 3*y2)/(y2**2+1)) + 2*((y3**2 + 3*y3)/(y3**2+1)) + 2*((y4**2 + 3*y4)/(y4**2+1)) + 2*((y5**2 + 3*y5)/(y5**2+1)) + (y6**2 + 3*y6)/(y6**2+1))

    #dx_composto = (h/2) * ((1/(1+y1**2)) + 2*((1/(1+y2**2))) + 2*((1/(1+y3**2))) + 2*((1/(1+y4**2))) + 2*((1/(1+y5**2))) + (1/(1+y6**2)))

    #dx_composto = (h/2) * ( y1 + 2*(y2) + 2*(y3) + 2*(y4) + 2*(y5) + y6)
    #dx_composto = (h/2) * (1/(1+y1**2)) + (2*(1/(1+y2**2))) + (2*(1/(1+y3**2))) + (2*(1/(1+y4**2))) + (2*(1/(1+y5**2)))  + (1/(1+y6**2))
    
    print(dx_composto)
composto()


'''

(1/(1+(x**2)))

'''