import numpy
import math
x = [1,2,3,4,5,6,7,8]
y = [0.5,0.6,0.9,0.8,1.2,1.5,1.7,2.0]


zippedxy = zip(x,y)
zippedxx = zip(x,y)

xx = []
xy = []
logyVet = []

for listaA, listaB in zippedxy:
    xx_ = xx.append(listaA*listaB)

for listaA, listaB in zippedxx:
    xy_ = xy.append(listaA*listaA)

resutadoxx = numpy.sum(xx)
resutadoxy = numpy.sum(xy)

xxyVet = []
i=0
for logY in x:
    logy = math.log(y[i])
    i = i+1
    logy = logyVet.append(logy)    
resutadoLogVet = numpy.sum(logyVet)


i=0
for XxY in x:
    xxy = xxyVet.append(x[i]*logyVet[i])
    i = i+1

sumxxyVet = numpy.sum(xxyVet)

XXX=[]
i=0
for XxX in x:
    xxx = XXX.append(x[i] * x[i])
    i = i+1

sumXXX= numpy.sum(XXX)

sumx = numpy.sum(x)

QTDPontos = len(x)


a = ((QTDPontos * sumxxyVet - sumx * resutadoLogVet) / (QTDPontos * sumXXX - sumx*sumx))
b = ((sumx * sumxxyVet - resutadoLogVet * sumXXX) / (sumx*sumx - QTDPontos*sumXXX))

logb = math.exp(b)


e = float(2.718281828)
x=1
gx = (b*(e**(a*x)))

print(gx)