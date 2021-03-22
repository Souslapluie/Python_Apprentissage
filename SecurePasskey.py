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
print("Début\n")

while True:
	SPass = input("\nEntrez votre clef de passe sur lequel vous souhaitez vous entraîner. Soyez attentif : ")

	print("\nVous allez vous entraîner sur la clef de passe suivante : ", SPass)

	Confirm = input ("\nConfirmez que c'est bel et bien avec cette clef de passe que vous allez vous entraîner (Y/N ou Q pour quitter) : ")

	if Confirm.upper() == 'Y' :
		timestamp1 = datetime.timestamp(datetime.now())
		VPass = input("\nEntraînement de tapage de mot de passe ! Ecrivez-le, le plus rapidement possible : ")
		timestamp2 = datetime.timestamp(datetime.now())
		if VPass == SPass :
			result = timestamp2 - timestamp1
			print("\nBingo vous avez gagné : Temps d'exécution : ", result)
			break

	elif Confirm.upper() == 'Q' :
		break

	elif Confirm.upper() == 'N' :
		return


print("Fin")
