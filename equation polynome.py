from math import sqrt

def polynome_second_degré ():
    a=float(input("Rentrez la valeur de a"))
    b=float(input("Rentrez la valeur de b"))
    c=float(input("Rentrez la valeur de c"))
    delta = b**2 - 4*a*c
    if delta < 0 :
        print ("Delta est négatif donc il n'y a pas de racine ")
    elif delta == 0 :
        x_0= -b/2*a
        print ("Delta est nul, il y a donc une seule racine qui est x_0 = "+str(x_0))
    elif delta > 0 :
        x_1= (-b -sqrt(delta))//2*a
        x_2= (-b +sqrt(delta))//2*a
        print (" Delta est positif donc il y a deux racines \n"+"x_1 = "+str(x_1)+" \n"+"x_2 = "+str(x_2))


str(polynome_second_degré())

