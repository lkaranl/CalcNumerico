import MMQ_aux

xi = [1,1.5,2,2.5,3] # PONTOS X
yi = [66,52,18,11,10] # PONTOS Y
x = float(input("Valor de x: ")) # PONTO X ESPECIFICO



# CHAMA AS FUNCOES3.2
if __name__ == "__main__":
    print("\nReta")
    MMQ_aux.reta(xi,yi,x)
    print("\nParabola")
    MMQ_aux.parabola(xi,yi,x)