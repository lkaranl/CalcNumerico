'''
Se p(x) eh o polimonio interpoladro para o conjunto de dados
{(1,3),(2,7),(3,15),(4,31),(5.59)}, encontre uma aproximacao 
para o valor de 
     5
    S p(x) dx
     1
'''

# x = [1,2,3,4,5]
# y = [3,7,15,31,59]


# # dx = (h/2) * (p(y0) + 2 *(y1) + 2*(y2) + 2*(y3) + (y4))

# dx = ((1/2) * (y[0] + 2*(y[1]) + 2*(y[2]) + 2*(y[3]) + y[4]))
# print(dx)

x = [1,2,3,4,5]
y = [1,1.10517,1.22140,1.34986,1.49182,1.64872,1.82212,2.01375,2.22554,2.45960,2.71828]


#dx = (h/2) * (p(y0) + 2 *(y1) + 2*(y2) + 2*(y3) + (y4))

dx = ((1/2) * (y[0] + 2*(y[1]) + 2*(y[2]) + 2*(y[3]) + 2*(y[4]) + 2*(y[5]) + 2*(y[6]) + 2*(y[7]) + 2*(y[8]) + 2*(y[9]) + y[10]))
print(dx)