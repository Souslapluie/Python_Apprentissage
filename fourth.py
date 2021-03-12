"""

x = -3
while x < 0 :
    x = x+1
    print(x)

testend = "testestestestestestestestestestestestestestset"

print(testend, end = 'alors')

"""
# --------------- Boucle calculant la somme de la boucle ------------------------
"""

boucle = 0
somme = 0


while boucle <= 99 :
    boucle = boucle + 1
    somme = somme + boucle
    print(somme)
    
""" # Calculs de la somme des nombres, l'input s'arrêtant lorsque la valeur "0" est saisie.

cont = True
total = 0

while cont :
    a = int(input("Saisissez un entier : "))
    total = total + a
    cont = (a != 0)

print(total)
        

