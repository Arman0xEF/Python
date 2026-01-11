import json
import os

# Chemin du fichier JSON
chemin = "C:/Users/Arman/Desktop/py/projet_courses/courses.json"

# Initialisation de la liste
liste_courses = []

# Charger les données existantes si le fichier existe et n'est pas vide
if os.path.exists(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            if os.stat(chemin).st_size > 0:
                liste_courses = json.load(f)
    except json.JSONDecodeError:
        print("Le fichier JSON est corrompu ou mal formaté. Initialisation d'une nouvelle liste.")

# Boucle principale pour l'interface utilisateur
while True:
    user_input = input("Choisissez parmi les 5 options suivantes : \n1: Ajouter un élément à la liste\n2: Retirer un élément de la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter\n👉 Votre choix : ")
    
    if not user_input.isdigit():
        print("______________________________________________________\n ⚠️ Veuillez rentrer le bon numéro entre 1 et 5 !\n______________________________________________________")
        continue
    
    user_input = int(user_input)
    
    if user_input < 1 or user_input > 5:
        print("______________________________________________________\n ⚠️ Veuillez rentrer le bon numéro entre 1 et 5 !\n______________________________________________________")
        continue
    
    modification = False

    if user_input == 1:
        ajouter = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste_courses.append(ajouter)
        modification = True
        print(f"L'élément '{ajouter}' a bien été ajouté à votre liste !\n______________________________________________________")
    
    elif user_input == 2:
        retirer = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if retirer in liste_courses:
            liste_courses.remove(retirer)
            modification = True
            print(f"L'élément '{retirer}' a bien été retiré de la liste de courses !\n______________________________________________________")
        else:
            print("Cet élément n'est pas dans votre liste\n______________________________________________________")
    
    elif user_input == 3:
        if not liste_courses:
            print("Il n'y a rien dans votre liste de courses !\n______________________________________________________")
        else:
            print("Voici le contenu de votre liste :")
            for i, element in enumerate(liste_courses):
                print(f"{i + 1} : {element}")
            print("______________________________________________________")
    
    elif user_input == 4:
        liste_courses.clear()
        modification = True
        print("La liste de courses a bien été supprimée !\n______________________________________________________")
    
    elif user_input == 5:
        print("A bientôt !")
        break
    
    # Écrire la liste mise à jour dans le fichier JSON si une modification a été effectuée
    if modification:
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(liste_courses, f, ensure_ascii=False, indent=4)
