import numpy as np

'''
 3
S   1/x dx = len(3) - ln(1) = 1.0986
 1

O ponto 1 ao 3(x), foi dividido em 5 partes (xx)
usando 4 pontos
'''

# x = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
# xx = [1,1.10517,1.22140,1.34986,1.49182,1.64872,1.82212,2.01375,2.22554,2.45960,2.71828]
# n = 10

x = [0,0.1,0.2,0.3,0.4,0.5]
xx = [1,1.10517,1.22140,1.34986,1.49182,1.64872]
n = 6

e = 2.718281828

y = []
fx = []

tamanho = len(x)
tamanhoxx = len(xx)
b = x[tamanho-1]
a = x[0]
nx = []
h = (b-a)/n

i=0
j=0
for k in xx:
    nx.append(j)
    j = j+h
    #aux_y = 1/nx[i]
    aux_y = e**nx[i] 
    y.append(aux_y)
    i+=1
    # print(At)

i=0
sumNX=0
for soma in xx:
    aux_sum = y[i]
    sumNX = sumNX + aux_sum
    i+=1
sumNX = sumNX - y[0] - y[tamanhoxx-1]

s = ((h/2)*(y[0]+2*(sumNX) + y[tamanhoxx-1]))

valorintegral = 1.0986
erro = ((s - valorintegral) / valorintegral) * 100
error = n * ((h**3/12))
#print("O erro foi de aproximadamente: {:.2f}%".format(erro))

print(s)






# x = [0,1]
# xx = [0,1,2,3,4,5,6,7,8,9]
# n = 10


# y = []
# fx = []

# tamanho = len(x)
# b = x[tamanho-1]
# a = x[0]
# nx = []
# h = (b-a)/n

# e = 2.718281828

# i=0
# j=1
# for k in xx:
#     nx.append(j)
#     j = j+h
    
#     # aux_y = 1/nx[i] # INTEGRAL
    
#     aux_y = e**nx[i]

#     y.append(aux_y)
#     i+=1


# s = ((h/2)*(y[0]+2*(y[1]+y[2]+y[3]) + y[4]))

# valorintegral = 1.0986
# erro = ((s - valorintegral) / valorintegral) * 100
# print("O erro foi de aproximadamente: {:.2f}%".format(erro))

# print(s)



