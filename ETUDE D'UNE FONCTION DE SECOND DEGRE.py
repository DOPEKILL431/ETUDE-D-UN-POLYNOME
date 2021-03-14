from  math import *


a=eval(input("Entrez la valeur de a : "))
b=eval(input("Entrez la valeur de b : "))
c=eval(input("Entrez la valeur de c : "))

print("       ")
print("       ")
print("       ")

print("CALCUL DU DISCRIMINANT")

delta=b**2-4*a*c
print("le discriminant est : ",delta)

if delta<0:
    print("       ")
    print("       ")
    print(" Pas de racine possible ")

if delta==0:
    print (" Il y a une racine double qui est : ")
    x3=(-b-sqrt(delta))/2*a
    print ("L racine doubl est : ")

if delta>0:
    print("Il ya 2 racines qui sont : ")

    x1=(-b-sqrt(delta))/2*a
    print ("la première racine est : ",x1)

    x2=(-b+sqrt(delta))/2*a
    print ("la deuxième racine est : ",x2)

alpha=-b/2*a
print ("la valeur de alpha est :" , alpha)

beta=(-b**2-4*a*c)/4*a
print ("la valeur de beta est : ", beta)




