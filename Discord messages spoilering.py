# -*-coding:Latin-1 -*
print("/!\ VERSION BETA : le programme ne prend pas en charge les sauts de ligne /!\ ")
message = input("Dans quel message voulez-vous ajouter des spoilers entre chaque lettre ?")  # On demande le message à traiter.
print("Voici votre message à copier-coller :")
message = str(message)  # Pour qu'il n'y ai pas de problème avec les chiffres, on assure la conversion en texte.
nombreDeCaractere = len(message)  # On regarde combien il y a de caratères.
caractere = 0
print()  # Saut de ligne avant le résultat.
while nombreDeCaractere > caractere:  # Tant qu'on a pas traité chaque caractère du message.
    print("||" + message[caractere] + "||", end="")  # On poste le message avec les spoilers, sans saut de ligne entre chaque.
    caractere = caractere + 1
input("\n\nAppuyez sur la touche \"Entrer\" pour quitter le programme.")  # Quitter le programme.
