#AUX_NEWTON

print('\033[1;31m'+"\n\t**** Metodo da NEWTON-RAPHSON ****\033[0;0m")
print('\nFuncao exemplo: x^3 - 9x + 5\nComo digitar: x**3 - 9*x + 5\n')
#v = [-4,-3,-2,-1,0,1,2,3,4] #VETOR DE POSSICOES, ORDEM CRESCENTE
v = [-4,-3,-2,-1,1,2,3,4] #VETOR DE POSSICOES, ORDEM CRESCENTE
vv = [] #VETOR ONDE FICA APENAS OS NUMEROS QUE SAO UM FX POSITIVO E O OUTRO NEGATIVO EX:[-4-,-3+,0+,+1-]
medd = [] #ARMAZENAS AS MEDIAS
erro = 0.001 # TAXA DE ERRO EXIGIDA
gx = [] #ARMAZENA OS NUMEROS POSITIVOS COMO 1 E NEGATIVOS COMO 0
str_exp = input("DIGITE SUA FUNCAO: ")
fx = str_exp
#erro = float(input("TAXA DE ERRO DESEJADA: "))

def efedeX():
	for x in v:	# LACO QUE PEGA A FUNCAO (FX) E ADD OS RESULTADOS EM GX
		fx = eval(str_exp)# FUNCAO MAGICA QUE PEGA A STRING
		gx.append(fx)
	return fx

def gedeX():
	i = 0
	for y in v: # LACO QUE TRANSFORMA OS VALORES EM 1 OU 0 (1 POSITIVO, 0 NEGATIVO)
		if gx[i] > 0:
			gx[i] = 1
		else:
			gx[i] = 0
		i = i + 1

def calculo():# FUNCAO QUE FAZ O CALCULO INICIAL DE FX E OS LACOS DE REPETICAO ENVOLVENDO OS VETORES UTILIZADOS
	j = 0 #
	k = 1
	l = 1
	efedeX()
	gedeX()
	#for z in range(8):
	for z in range(7): # LACO QUE VERIFICA OS VALORES QUE PROVAVELMENTE TEMHAM RAIZES
		if gx[j] != gx[k]:
			med = ((v[j] + v [k]) / 2)
			medd.append(med)
			print("Sujestao de raizes =  {} ({} e {})".format(med,v[j],v[k]))
			vv.append(v[k])
			vv.append(v[j])
			l = l + 1
		j = j + 1
		k = k + 1	

def function(m,n):# FUNCAO QUE FAZ O CALCULO
	cont = 0
	a = vv[m]
	b = vv[n]
	medd[0] = ((a + b) / 2)
	x = medd[0]
	ff = 1
	while (ff > erro and cont < 50):
		cont = cont +1
		fx = eval(str_exp)# FUNCAO MAGICA QUE PEGA A STRING
		ff = abs(fx)
		print("a+ = {:.3f} | b- = {:.3f} | X = {:.3f} | f(x) = {} -> {}".format(a,b,medd[0],fx,cont))
		if (fx > 0):
			a = medd[0]
		else:
			b = medd[0]
		medd[0] = ((a + b) / 2)
		x = medd[0]
	if (cont > 49):
		print("\nGEROU UMA INDETERMINACAO")
	else:
		print("+"*70)
		print("O zero da funcao para o erro {} esta na possicao \033[1;31m{}\033[0;0m".format(erro,cont))
		print("|{}|".format(abs(fx)))
		print("#"*23)
		print("FIM\n\n")
	return __main__()	

# FUNCAO PRINCIPAL
def __main__():
	calculo()

__main__()