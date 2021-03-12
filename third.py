print("\n")
"""  # Résolution de l'équation ax + b = 0


# Ecrire un script qui résoud l'équation ax + b = 0, avec a et b saisissables

a = float (input ("Ecrivez une valeure pour a : "))
b = float (input ("Ecrivez une valeure pour b : "))

if b != 0 :
    if a != 0 :
        result_message = "L'équation admet une solution unique"
        result_message += str(-b/a)

    else :
        result_message = (L'équation n'admet pas de solution. a est égal à 0, et restera 0 même multiplié à x. Tout ce qui reste est la valeure b : b)

else :
    if a != 0 :
        result_message = "L'équation admet 0 solution."
    else :
        result_message = "L'équation admet une infinité de solutions."

print(result_message)



"""    # Savoir si on a une bonne note :
"""

note = float(input("Ecrivez votre note / 20 afin que le gouvernement puisse vous tracer et vous juger : "))
GG = "\nRéussite !"

if note <= 9 :
    print("\nEchec critique !")
elif note >= 10 and note <= 11.99 :
        print(GG)

elif note >= 12 and note <= 13.99 :
    print (GG)
    print ("    Mention : Assez bien.")

elif note >= 14 and note <= 15.99 :
    print (GG)
    print ("    Mention : Bien.")

elif note >= 16 and note <= 20 :
    print (GG)
    print ("    Mention : Très bien.")

elif note >= 20 :
    print ("\nNous avions demandé une note maximale sur 20. Votre note est au-dessus de 20.")
    print ("Vous êtes dorénavant soupçonné de terrorisme et le gouvernement va venir vous chercher.")


""" # Savoir si on a réussi avec la moyenne de 3 notes :

note_python = float(input("Ecrivez votre notre / 20 sur le cours de Python : "))
note_sql = float(input("Ecrivez votre note / 20 sur le cours de SQL : "))
note_assembleur = float(input("Ecrivez votre note / 20 sur le cours d'Assembleur : "))

moyenne = (note_python + note_sql + note_assembleur)/3

print("\n     Votre moyenne est de ", moyenne)

if moyenne <= 9.99 :
    print("       Votre moyenne n'est pas égale ou supérieure à 10. Retentez votre chance !")
elif moyenne >= 10 :
    print("        Votre moyenne est bonne. Vous avez réussi le test !")

if note_python < 10 or note_sql < 10 or note_assembleur :
    print("\nUne et / ou plusieurs notes a dûe être compensée par une et / ou plusieurs autre(s) note(s).")
