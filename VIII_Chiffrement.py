"""
printer = "hello, friend"

print(printer[2:5])

# >>> llo

# Script déterminant et affichant nb d'occurrences de la lettre a (nb de fois où la lettre a été tapée), min / maj / spé.

a_count = 0
cpt = 0
machine = input("Saisissez votre texte ici. Copiez / coller depuis wikipédia la page sur les hyppocampes du sud-diagonale-gauche sinon ça ne marchera pas : ")

while cpt < len(machine) :
	if machine[cpt] == 'a' or machine[cpt] == 'à' or machine[cpt] == 'A' or machine[cpt] == 'â' :
		a_count = a_count + 1
	cpt = cpt + 1

print("Y'a", a_count, "'A'")


			# Créer un script remplaçant certains charactères par d'autres charactères ( chiffrement )


a_remp_1 = ''
b_remp_2 = ''
c_remp_3 = ''

modif = input("Saisissez votre texte à modfier : ")



			# AU DESSUS = PAS FINi
""" 
""" 
# CORRECTION SCRIPT CHIFFREMENT du DESSUS en dessous

s = input("saisissez")
s_result = ''
i = 0

while i < len(s) :

	if s[i] == 'a' :
		s_result = s_result + '1'

	elif s[i] == 'b' :
		s_result = s_result + '2'

	elif s[i] == 'c' :
		s_result = s_result + '3'

	else :
		s_result = s_result + s[i]
	i = i + 1

print(s_result)

"""
			# QUE FAIRE ? ( en dessous )

"""

s = input ("Saisir une chaîne de caractères : ")
i = 0

cpt_char_min = 0
cpt_char_maj = 0
cpt_char_spe = 0
cpt_int = 0

while i < len(s):

	if ord('a') <= ord(s[i]) <= ord('z') :
		msg = "caractères"
		cpt_char_min = cpt_char_min + 1

	elif ord ('A') <= ord(s[i]) <= ord('Z') :
		msg = "caractère"
		cpt_char_maj = cpt_char_maj + 1

	elif ord('0') <= ord(s[i]) <= ord('9') :
		msg = "chiffre"
		cpt_int = cpt_int + 1

	else : 
		msg = "special"
		cpt_char_spe = cpt_char_spe + 1

	print(s[i] + " : " + msg)
	i = i + 1

print("\nMinuscules = ", cpt_char_min, "\nMajuscules = ", cpt_char_maj, "\nChiffres = ", cpt_int, "\nSpécialChar = ", cpt_char_spe)

"""




"""

mdp = input("Entrez votre mot de passe : (Entrer un faux évidemment) ")

password_ok = True

password_ok = ord('A') <= ord(mdp[0]) <= ord('Z')

if password_ok :
	special_char = 0

	for c in mdp[1:] :
		digit = ord('0') <= ord(c) <= ord('9')
		low_char = ord('a') <= ord(c) <= ord('z')
		upp_char = ord('A') <= ord(c) <= ord('Z')

		if not digit and not low_char and not upp_char :
			special_char = special_char + 1

	password_ok = special_char >= 2

# Le mdp doit avoir une longueur comprise entre 10 et 15

if password_ok :
	password_ok = 10 <= len(mdp) <= 40

print("Mot de passe", end=' ')

if password_ok :
	print("correct")

else :
	print("incorrect")


"""

					# ------------------------- CHIFFREMENT DE CéSAR ----------------------

# (nom_var - 65 + key ) % 26 + 65			= Algo Chiffrement
# ord() =/= chr()


crypt_cd = input("Voulez-vous chiffrer ou déchiffrer ? Choisissez avec 'C' ou 'D' : ")
clear_txt = input("Saisissez le texte clair dont vous voulez modifier : ")
crypt_key = input("Choisissez la variable définissant votre clef : ")


crypt_key_choice = 0
crypt_cd_choice = ''




Chiffr = ord(clear_text)

print(Chiffr)







