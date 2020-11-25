import MMQ_aux
# xi = [0,0.25,0.5,0.75,1] # PONTOS X
# yi = [1,1.2840,1.6487,2.1170,2.7183] # PONTOS Y

# xi = [-1,-0.7,-0.4,-0.1,0.2,0.5,0.8,1.0] # PONTOS X
# yi = [36.547,17.267,8.155,3.852,1.82,0.86,0.406,0.246] # PONTOS Y

# xi = [1,2,3,4,5,6,7,8] # PONTOS X
# yi = [0.5,0.6,0.9,0.8,1.2,1.5,1.7,2.0] # PONTOS Y

xi = [1,2,3,4,5,6,7,8] # PONTOS X
yi = [0.5,0.6,0.9,0.8,1.2,1.5,1.7,2]# PONTOS Y

x = float(input("Valor de x: ")) # PONTO X ESPECIFICO

# CHAMA AS FUNCOES
if __name__ == "__main__":
    print("\nReta")
    MMQ_aux.reta(xi,yi,x)
    print("\nParabola")
    MMQ_aux.parabola(xi,yi,x)
    print("\nAjuste Exponencial")
    MMQ_aux.exponecial(xi,yi,x)