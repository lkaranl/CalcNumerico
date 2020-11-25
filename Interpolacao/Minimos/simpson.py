import math
'''
REGRA DE SIMPSON
ESSA REGRA 1/3 EH UTILIZADA NA QUANTIDADE DE INTERVALOS PAR

CALCULAR O VALOR DE:
     2
I = S x*e^x dx
     1.6
USANDO A REGRA 1/3 DE SIMPSON
'''
e = 2.718281828

# y1 = 1.6
# y3 = 2.0

# y2 = abs(y1 + y3) / 2

# h = abs(y1 - y2)

# i = (h/3) * ((y1*e**y1) + 4*y2*(e**y2) + (y3*e**y3))

# print(i)


# y1 = 0.5
# y3 = 1
# y2 = abs(y1 + y3) / 2
# h = abs(y1 - y2)

# i = (h/3) * ((y1*math.sin(y1) + 4*y2*math.sin(y2) + y3*math.sin(y3)))

# print(i)


y1 = 1.4
y2 = 1.5
y3 = 1.6
y4 = 1.7
y5 = 1.8
# y2 = abs(y1 + y3) / 2
h = abs(y1 - y5) / 4

# I = h/3 * (y1+4y2+2y3+4y4+y5)
i = (h/3) *( (math.sqrt(y1)+1/y1) + (4*(math.sqrt(y2)+1/y2)) + (2*(math.sqrt(y3)+1/y3)) + (4*(math.sqrt(y4)+1/y4)) + ((math.sqrt(y5)+1/y5)))

print(i)