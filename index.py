import math

# Additionner deux chiffre
def sum():
    try:
        a = int(input('Donner le premier chiffre :\n'))
        b = int(input('Donner le deuxième chiffre :\n'))
        print("La somme de ",a," + ",b," = ",a+b)
    except ValueError:
        print('Veuillez saisir un chiffre')



# Résoudre une équation du second degré
def puissanceDeux():
    try:
        a = int(input("Donner la valeur de a :\n"))
        b = int(input("Donner la valeur de b :\n"))
        c = int(input("Donner la valeur de c :\n"))
        print(a,b,c)
        delta = b**2 - 4*a*c
        if(delta < 0):
            print('Pas de solution')
        elif(delta == 0 ):
            x= -b/2*a
            print('Ya une solution x = ',x)
        else: 
            x1 = -b-math.sqrt(delta)/2*a
            x2 = -b+math.sqrt(delta)/2*a
            print("Ya deux solution x1 = ",x1," et x2 = ",x2)
    except ValueError:
        print("Veuillez Saisir un chiffre")



