from datetime import datetime
print("Début\n")

while True:
	SPass = input("\nEntrez votre mot de passe sur lequel vous souhaitez vous entraîner. Soyez attentif : ")

	print("\nVous allez vous entraîner sur la clef de passe suivante : ", SPass)

	Confirm = input ("\nConfirmez que c'est bel et bien avec ce mot de passe que vous allez vous entraîner (Y/N ou Q pour quitter) : ")

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