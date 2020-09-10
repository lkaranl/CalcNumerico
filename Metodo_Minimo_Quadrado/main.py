import MMQ_aux

xi = [0,0.25,0.5,0.75,1] # PONTOS X
yi = [1,1.2840,1.6487,2.1170,2.7183] # PONTOS Y
x = float(input("Valor de x: ")) # PONTO X ESPECIFICO



# CHAMA AS FUNCOES
if __name__ == "__main__":
    print("\nReta")
    MMQ_aux.reta(xi,yi,x)
    print("\nParabola")
    MMQ_aux.parabola(xi,yi,x)