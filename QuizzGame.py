print("Bienvenu(e) ! Amusez-vous en testant vos connaissances en Python ! ")

playing = input("Est-ce que tu es prêt ? 🔥 ")

if playing.lower() != "oui":
    print("A bientôt ! 😬")
    quit()

print(" Les règles : ✅ = 1 point ❌ : -1 point 🤷‍ = 0 point \n")
score = 0

# Question 1

print("NOUVELLE QUESTION \n"
      "Choix possible : \n"
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
      "Choix possible : \n"
      "1 > L'interpréteur traduit une instruction à la fois en code machine, "
      "tandis que le compilateur traduit le code entier à la fois en code machine. \n"
      "2 > .... \n"
      "3 > ... \n"
      "4 > Je ne sais pas 🤷‍ \n"
      "Q > Quitter le programme.\n")

answer = input(
    "Question : Quelle est la principale différence entre un interpréteur et un compilateur ? \n "
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
      "Choix possible : \n"
      "1 > ...  \n"
      "2 > Python est un langage à typage dynamique.  \n"
      "3 > ...  \n"
      "4 > Je ne sais pas 🤷‍ \n"
      "Q > Quitter le programme.\n")

answer = input(
    "Question : Python est-il un langage à typage statique ou à typage dynamique ? \n "
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
print("A bientôt ! 😬")