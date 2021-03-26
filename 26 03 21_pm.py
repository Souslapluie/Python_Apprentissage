
# 1)

def som_div_propres(n) :
    som_div = 0
    for div in range(1, n) :
        if n % div == 0:
                som_div += div #som_div = som_div + div
    return som_div

# 2)
"""
def est_parfait(n) :
        if 

        return True
"""


# 1 ) Fonction retournant true si n = presque parfait
"""
def est_presque_parfait(n):
        
        for div in range(1, n) :
                if n % div == range(**2) :
                        return True
                
        print("n = ", n, "div = ", div)
"""
"""
# Correction 1)

def est_presque_parfait(n):
        return som_div_propres(n) == n-1

# 2) Procédure affichant tous nombres presques parfaits plus petits que 2^k

def affiche_presque_parfait(k) :
        for n in range(1, 2**k) :
                if est_presque_parfait(n):
                        print(n, end=' ')
"""

# Fonction amicaux(n, m) retournant booleen True si n et m = amicaux

def amicaux(n, m) :
        return (som_div_propres(n) == m) and (som_div_propres(m) == n)


def affiche_amicaux(k) :
        for n in range(1, 2**k) :
                m = som_div_propres(n)
                if amicaux(n, m) :
                        print('(' + str(n) + ',' + str(m) + ') ')
# time clock

from time import time

start = time()
k = 12
print("\nNombres amicaux < 2**k : \n")
affiche_amicaux(k)
end = time()
print("\nDurée d'exécution : ", end - start, "s")
        




        
