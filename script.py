import random

print("Bienvenue dans le jeu de devinette !")
print("J'ai choisi un nombre entre 1 et 100. Devine lequel.")

nombre_secret = random.randint(1, 100)
tentatives = 0

while True:
    essai = int(input("Entrez un nombre : "))
    tentatives += 1

    if essai < nombre_secret:
        print("Trop bas ! Essaye encore.")
    elif essai > nombre_secret:
        print("Trop haut ! Essaye encore.")
    else:
        print(f"Bravo ! Tu as deviné le nombre en {tentatives} tentatives !")
        break 