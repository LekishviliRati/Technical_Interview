print("Bienvenu(e) ! Amusez-vous en testant vos connaissances en Python ! ")

playing = input("Est-ce que tu es prêt ? 🔥 ")

if playing.lower() != "oui":
    print("A bientôt ! 😬")
    quit()

print(" Les règles : ✅ = 1 point ❌ : -1 point 🤷‍ = 0 point \n")
score = 0

# Question 1

print("NOUVELLE QUESTION \n"
      "Choix possibles : \n"
      "1 > Un serpent \n"
      "2 > Une série \n"
      "3 > Python est un langage de programmation généraliste interprété de haut niveau. \n"
      "4 > Je ne sais pas 🤷‍ \n"
      "Q > Quitter le programme.\n")

answer = input(
    "Question : Qu'est-ce que Python? \n "
    "-> Réponse : "
)

if answer.lower() == "q":
    print("Votre score est de " + str(score))
    print("A bientôt ! 😬")
    quit()

if answer.lower() == "3":
    print("✅")
    score += 1
elif answer.lower() == "4":
    print("🤷‍")
    print("Bonne réponse : 3 \n\n")
else:
    print("❌")
    score -= 1
    print("Bonne réponse : 3 \n\n")

# Question 2

print("NOUVELLE QUESTION \n"
      "Choix possibles : \n"
      "1 > Division entière \n"
      "2 > Retourne le reste \n"
      "3 > Division du float par zéro \n"
      "4 > Je ne sais pas 🤷‍ \n"
      "Q > Quitter le programme.\n")

answer = input(
    "Question : En python 3, que fait l’opérateur // ? \n "
    "-> Réponse : "
)

if answer.lower() == "q":
    print("Votre score est de " + str(score))
    print("A bientôt ! 😬")
    quit()

if answer.lower() == "1":
    print("✅")
    score += 1
elif answer.lower() == "4":
    print("🤷‍")
    print("Bonne réponse : 1 \n\n")
else:
    print("❌")
    score -= 1
    print("Bonne réponse : 1 \n\n")

# Question 3

print("NOUVELLE QUESTION \n"
      "Choix possibles : \n"
      "1 > char  \n"
      "2 > python ne possède aucun type de données pour les caractères, "
      "ils sont traités comme des chaînes de caractères (String)  \n"
      "3 > character  \n"
      "4 > Je ne sais pas 🤷‍ \n"
      "Q > Quitter le programme.\n")

answer = input(
    "Question : Quel est le type de données pour un caractère en python? \n "
    "-> Réponse : "
)

if answer.lower() == "q":
    print("Votre score est de " + str(score))
    print("A bientôt ! 😬")
    quit()

if answer.lower() == "2":
    print("✅")
    score += 1
elif answer.lower() == "4":
    print("🤷‍")
    print("Bonne réponse : 2 \n\n")
else:
    print("❌")
    score -= 1
    print("Bonne réponse : 2 \n\n")

# Question 4

print("NOUVELLE QUESTION \n"
      "Choix possibles : \n"
      "1 > lower()  \n"
      "2 > lstrip()  \n"
      "3 > upper(str)  \n"
      "4 > Je ne sais pas 🤷‍ \n"
      "Q > Quitter le programme.\n")

answer = input(
    "Question : Laquelle des fonctions suivantes renvoie le plus petit caractère de la chaîne str? \n "
    "-> Réponse : "
)

if answer.lower() == "q":
    print("Votre score est de " + str(score))
    print("A bientôt ! 😬")
    quit()

if answer.lower() == "1":
    print("✅")
    score += 1
elif answer.lower() == "4":
    print("🤷‍")
    print("Bonne réponse : 1 \n\n")
else:
    print("❌")
    score -= 1
    print("Bonne réponse : 1 \n\n")


# Question 5

print("NOUVELLE QUESTION \n"
      "Choix possibles : \n"
      "1 > fopen(file_name, mode)  \n"
      "2 > open(file_name, mode)  \n"
      "3 > openfile(file_name, mode)  \n"
      "4 > Je ne sais pas 🤷‍ \n"
      "Q > Quitter le programme.\n")

answer = input(
    "Question : Quelle fonction est utilisée pour ouvrir le fichier en lecture en Python? \n "
    "-> Réponse : "
)

if answer.lower() == "q":
    print("Votre score est de " + str(score))
    print("A bientôt ! 😬")
    quit()

if answer.lower() == "2":
    print("✅")
    score += 1
elif answer.lower() == "4":
    print("🤷‍")
    print("Bonne réponse : 2 \n\n")
else:
    print("❌")
    score -= 1
    print("Bonne réponse : 2 \n\n")


print("Votre score est de " + str(score))
print("Vous avez obtenu " + str((score / 5) * 100) + "%")
print("A bientôt ! 😬")