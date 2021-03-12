from math import pi
"""
print("                     Calcul du périmètre d'un cercle avec son rayon : \n")

rayon = float (input ("Entrez le rayon du cercle : "))

perim = 2 * pi * rayon

print("Le périmètre de votre cercle est probablement : ", perim)
       
print("\n ----------- Fin du calculs concernant le cercle -----------")

print ("\n          Calcul de l'aire d'un triangle avec la longueur des trois côtés : \n")
       
C1 = float (input ("Entrez la longueur du côté n¤1 : "))
C2 = float (input ("Entrez la longueur du côté n¤2 : "))
C3 = float (input ("Entrez la longueur du côté n¤3 : "))

aire = (C1 + C2 + C3)/2
print("L'aire de votre triangle est probablement : ", aire)


print("\n ------------- Fin du calcul concernant le triangle ----------\n")



"""



print("        \n        Conversion entre les différentes valeures représentant le temps : ")

# 60 secondes = 1 minute, 60 minutes = 1 heure,

str_ini = (input ("\nVotre nombre est-il de l'ordre de la seconde, de la minute ou de l'heure ? Choisissez en entrant soit ' S ', soit ' M ', soit ' H ' : "))
tps_ini = float (input ("\nEntrez votre nombre temporel : "))
str_conv = (input ("\nQuelle est l'indicateur de temps dans lequel vous souhaitez convertir votre nombre ? Choisissez en entrant soit ' S ', soit ' M ', soit ' H ' : "))



tps_s = 0

if str_ini == "S" and str_conv == "M" :
    tps_s = tps_ini/60
    print ("\nVotre nombre de seconde(s) représente : ", tps_s, " minute(s)")

if str_ini == "S"  and str_conv == "H" :
    tps_s = tps_ini/3600
    print ("\nVotre nombre de secondes représente : ", tps_s, " heure(s)")



tps_m = 0

if str_ini == "M" and str_conv == "S" :
    tps_m = tps_ini*60
    print ("\nVotre nombre de minute(s) représente : ", tps_m, " seconde(s)")

if str_ini == "M" and str_conv == "H" :
    tps_m = tps_ini/60
    print ("\nVotre nombre de minute(s) représente : ", tps_m, " heure(s)")



tps_h = 0

if str_ini == "H" and str_conv == "M" :
    tps_h = tps_ini/60
    print ("\nVotre nombre d'heure(s) représente : ", tps_h, " minutes")

if str_ini == "H" and str_conv == "S" :
    tps_h = tps_ini*3600
    print ("\nVotre nombre d'heure(s) représente : ", tps_h, " secondes")





               

