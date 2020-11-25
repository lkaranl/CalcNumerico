#! /usr/bin/python

def integrate(function, a, b):
    coeff = [7,32,12,32,7]
    result = 0
    for i in range(0,len(coeff)):
        x = a + (i*(b-a))/(len(coeff)-1)
        result += coeff[i]*function(x)
        #print function(x)
    result = result*((b-a)/90.)
    return result

def func(x):
    return x**3-4*x+9

print (integrate(func,-7.0,7.0))