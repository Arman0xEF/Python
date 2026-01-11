import random

nombre_aleatoire = random.randint(0, 101)
nombre_essais = 5 

while True:
    nombre_saisie = input(f"_________________________________________\n🍀 Le jeu du nombre mystère 🍀\nIl te reste {nombre_essais} essais\nDevine le nombre : ")
   
    if not nombre_saisie.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    
    nombre_saisie = int(nombre_saisie)
    
    if nombre_saisie == nombre_aleatoire:
        print(f"Tu as trouvé le nombre en {nombre_essais} essai.\nFin du jeu.")
        break

    if  not nombre_saisie == nombre_aleatoire:
        nombre_essais -= 1
        if nombre_saisie > nombre_aleatoire:
            print(f"Le nombre mystère est plus petit que {nombre_saisie}.")
        elif nombre_saisie < nombre_aleatoire:
            print(f"Le nombre mystère est plus grand que {nombre_saisie}.")
        elif nombre_essais > 1:
            print(f"Il te reste {nombre_essais}.")

    if nombre_essais == 0:
        print(f"Dommage ! le nombre mystère était {nombre_aleatoire}.\nFin du jeu.")
        break
