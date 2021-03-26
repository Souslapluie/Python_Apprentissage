"""
				Ici, nous voulons améliorer l'intimité de nos clefs de passe.
	Commandes claviers en public :
		
    Maj + Shift = Annulation des deux = Tromper quiconque regardant le clavier en tapant
    Caractère spécial du style ' Ï '  = Tromper quiconque regardant le clavier en tapant
    Avoir son propre "langage"+random = Tromper quiconque regardant le clavier en tapant
    S'entraîner à taper à vitesse V   = Tromper quiconque regardant le clavier en tapant
    
    
		Il faut une clef de passe la plus éloignée de notre vie et de notre personne 
			pour diminuer les pistes de l'inginérie sociale.
			Les ondes sinusoïdales constitutives.
	    	 =  |_35 0nd35 51n|_|50Ïd4|es [onstituti\/e.e.s.
			GOTTA GO FAST = |_35 0nd35 51n|_|50Ïd4|35 [onstituti\e.e.s.
			1 - |_35 0nd35 51n|_|50Ïd4|es [onstituti\/e.e.s.
			2 -
			3 - 
			4 -
			5 -
		
"""


from datetime import datetime
from time import time
from time import sleep

print("\n             Bienvenue au camp d'entraînement. ")
print("                  L'objectif étant de trouver la clef la plus impénétrable possible.")
print("                     Et de s'entraîner à la taper le plus rapidement possible lorsque d'autres personnes sont à proximité.")


#while True:

SPass = input("\nEntrez votre clef de passe sur lequel vous souhaitez vous entraîner.\nSoyez attentif : ")

print("\nVous allez vous entraîner sur la clef de passe suivante : ", SPass)

Confirm = input ("\nConfirmez que c'est bel et bien avec cette clef de passe que vous allez vous entraîner.\n(Y/N ou Q pour quitter) : ")

if Confirm.upper() == 'Q' :
	exit()

elif Confirm.upper() == 'N' :
	break

elif Confirm.upper() == 'Y' :
    print("\nEntraînement de tapage de mot de passe ! Ecrivez-le, le plus rapidement possible.\n")
    print("           Commencement au 'GO' dans 4 secondes :")
    sleep(1)
    print(" 3... ")
    sleep(1)
    print(" 2... ")
    sleep(1)
    print(" 1... ")
    sleep(1)
                
    ChronoDeb = time.clock()
    VPass = input("\n GO ! : ")
    ChronoFin = time.clock()
    result = ChronoFin - ChronoDeb
            
elif VPass == SPass :
	print("\nVous avez correctement recopié votre création. Temps d'exécution : ", result)
      
else VPass != SPass :
	print("Votre création n'a pas été parfaitement recopiée. Temps d'exécution : ", result)


print("Fin")
