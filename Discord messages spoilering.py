# -*-coding:Latin-1 -*
print("/!\ VERSION BETA : le programme ne prend pas en charge les sauts de ligne /!\ ")
message = input("Dans quel message voulez-vous ajouter des spoilers entre chaque lettre ?")  # On demande la phrase.
message = str(message)  # Pour qu'il n'y ai pas de probl�me avec les chiffres, on assure la conversion en texte.
nombreDeCaractere = len(message)  # On regarde combien il y a de carat�res
caractere = 0
print()  # Saut de ligne avant le r�sultat.
while nombreDeCaractere > caractere:  # Tant qu'on a pas trait� chaque caract�re.
    print("||" + message[caractere] + "||", end="")  # On poste le message avec les spoilers, sans saut de ligne entre chaque.
    caractere = caractere + 1
input("\n\nAppuyez sur la touche \"Entrer\" pour quitter le programme.")  # Quitter le programme.