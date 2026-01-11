import random

pv_player = 50
pv_ennemy = 50
potion = random.randint(15, 50)
number_of_potion = 3
attack_player = random.randint(5, 10)
attack_ennemy = random.randint(5, 15)

while True:
    user_input = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    if not user_input.isdigit():
        continue
    
    user_input = int(user_input)

    if user_input != 1 and user_input != 2:
        continue

    if user_input == 2:
        if number_of_potion == 0:
            print(f"Vous n'avez plus de potion {number_of_potion}.")
            continue
        pv_player += potion
        number_of_potion -= 1
        print(f"Vous récupérez {potion} points de vie ({number_of_potion} potions restantes).")
        pv_player -= attack_ennemy
        if pv_player < 0:
            pv_player = 0
            print("Tu as perdu !\nFin du jeu.")
            break
        print(f"L'énnemi vous a infligé {attack_ennemy} points de dégats.")
        print(f"Il vous reste {pv_player} points de vie.\nIl reste {pv_ennemy} points de vie à l'énnemi.\n__________________________________________")

    if user_input == 1:
        pv_ennemy -= attack_player
        if pv_ennemy < 0:
            pv_player = 0
            print("Tu as gagné !\nFin du jeu.")
            break
        print(f"Vous avez infligé {attack_player} points de dégats à l'énnemi ! ")
        pv_player -= attack_ennemy
        if pv_player < 0:
            pv_player = 0
            print("Tu as perdu !\nFin du jeu.")
            break
        print(f"L'énnemi vous a infligé {attack_ennemy} points de dégats.")
        print(f"Il vous reste {pv_player} points de vie.\nIl reste {pv_ennemy} points de vie à l'énnemi.\n__________________________________________") 
