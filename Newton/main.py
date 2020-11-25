#!/usr/bin/env python3.8
#####	NAME:				ALGORITMO NEWTON
#####	VERSION:			0.3
#####	DESCRIPTION:		
#####	DATE OF CREATION:	11/03/2020
#####	WRITTEN BY:			KARAN LUCIANO SILVA | JACKSON DURAES
#####	E-MAIL:				karanluciano1@gmail.com			
#####	DISTRO:				ARCH LINUX
#####	LICENSE:			GPLv3 			
#####	PROJECT:			https://github.com/lkaranl/

import derivada
import aux_newton

def newton():

	fx = aux_newton.fx
	xn = float(input("DIGA A RAIZ DESEJADA: "))
	erro = float(input("TAXA DE ERRO DESEJADA: "))
	n = 0
	aux_a = 1
	iteracao = 0
	ffx = str(derivada.calDerivada(fx))
	x = xn
	test = []
	print("\n")
	print("─"*88)
	while aux_a > erro:
		a = eval(fx)
		aux_a = abs(a)
		b = eval(ffx)
		c = xn - (a/b)
		x = c
		print("n = {}\txn = {:.4f}\tf({:.4f}) = {:.4f}\tf'({:.4f}) = {:.4f}\t  x{}+1 = {:.4f}".format(n,xn,xn,a,xn,b,n,c))
		n = n+1
		xn = c
		test.append(xn)
		iteracao = iteracao +1
	print("─"*88)
	print("A taxa de erro desejada esta na {} iteracao\nPossivel raiz do erro desejado = {}\nTaxa de erro = |{}|".format(iteracao-1,test[iteracao-2],a))
	#print("{:.4f}".format(test[iteracao-2]))


newton()
