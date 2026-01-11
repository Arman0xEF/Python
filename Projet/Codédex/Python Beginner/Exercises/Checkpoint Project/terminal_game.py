import random

user = ""
user_health = 20
state = "alive"

rocket_launcher = 0
brass_knuckles = 0
fist = 0
shotgun = 0
baseball_bat = 0
weapon_name = ""
weapon_choice = 0
weapon_name2 = ""
weapon_choice2 = 0
weapon_name3 = "" 
weapon_choice3 = 0

xarthium_jelly = 10
korallin_thunder_mushroom = 20
veyrrksa_shell = 40

veyrrksan_health = 60
chipped_bite = 0 
shell_shard = 0
veyrrksan_choice = 0

xarthium_beast_health = 110
ionized_charge = 0
voltic_spit = 0
xarthium_choice = 0

myco_fulgurant_health = 150
spore_pulse = 0
shock_tendril = 0
fungal_overgrowth = 0
myco_fulgurant_choice = 0

celestial_archimandrite = 200
crystal_lance = 0
astral_wave = 0
gravity_wrap = 0
starfall_obliteration = 0
celestial_archimandrite_choice = 0

yes_or_no = ""
choice1_weapon = 0
choice2_lvl1_room = 0
choice3_lvl1_room = 0

choice4_lvl2_room = 0
choice5_lvl2_room = 0
choice6_lvl2_room = 0

choice7_lvl3_room = 0
choice8_lvl3_room = 0
choice9_lvl3_room = 0
choice10_lvl3_room = 0
choice11_lvl3_room = 0

choice12_lvl4_room = 0
choice13_lvl4_room = 0
choice14_lvl4_room = 0
choice15_lvl4_room = 0

while state != "end":
    user = input("(Mothership Assistant): Hello adventurer, I will be your companion during our journey, what is your name?\n-> ")
    print(f"\n(Narrator): It has been many long years since the human race vanished from almost every corner of the known universe. Once-great cities now lie in silent ruins, swallowed by time and war. Even the stars seem scarred by the collapse of a broken future.\n\nOnly a handful of survivors managed to escape Earth during the final days of the invasion. Among them is you, {user}, one of the last heirs of a fallen humanity.The aliens had invaded without warning: colossal black fleets covered the sky, their weapons tearing through our defenses as if they were nothing. The oceans boiled under the force of orbital bombardments. The continents burned, united in a single tragic fate.\n\nThe survivors fled aboard the mothership Arkos Prime, a drifting metal ark searching for a new world, a spark of hope, a reason for humanity’s final breath. But the journey is far from safe. In the darkness of the galaxy, new threats lurk: unknown creatures, hostile worlds, and above all… the lingering presence of the invaders, still hunting us.\n\nYou are one of the few capable of leaving the ship to explore, fight, investigate. Your destiny is not yours alone: it carries the weight of all humankind.\n\nAnd thus begins your journey. A new page. A final hope.")

    print(f"\n(Mothership Assistant): Mr. {user}, we need to land on a planet in order to restock our supplies. I am detecting a planet currently close to our position.")
    print(f"\n(Mothership Assistant): After a quick analysis, the ship has landed on the planet Xarthium.\n\nXarthium was once a thriving world, but centuries of violent electrical storms have reshaped its surface into a maze of crystal canyons and glowing fissures. The atmosphere crackles with unstable energy, and strange bioluminescent organisms pulse beneath the ground like veins of living light.\n\nExplorers who once tried to chart this place never returned, leaving behind only fragments of recordings describing creatures feeding on raw electricity and a strange jelly substance capable of altering organic matter.\n\nWhat remains clear is simple: Xarthium is dangerous, unpredictable… but rich in rare resources. If humanity is to survive, this hostile world may provide exactly what the *Arkos Prime* needs.\n\nYour mission begins now, {user}.")

    while choice1_weapon != 1 and choice1_weapon != 2:
        choice1_weapon = int(input("\n(Mothership Assistant): Please select a weapon from the following options :\n1) Brass Knuckles 🥊\n2) BaseBall Bat 🏑\n-> "))
        if choice1_weapon == 1:
            weapon_name = "Brass Knuckles 🥊"
            weapon_choice = brass_knuckles
        elif choice1_weapon == 2:
            weapon_name = "BaseBall Bat 🏑"
            weapon_choice = baseball_bat
        else:
            print("\n⚠️  Please, enter a valid number !")

    print(f"\n(Mothership Assistant): Mr. {user}, I am detecting a dungeon with 4 levels. Each level grants you different resources, but the difficulty increases as you progress!")

    while choice2_lvl1_room != 1 and choice2_lvl1_room != 2:
        choice2_lvl1_room = int(input("\n(Mothership Assistant): Please choose which room you want to enter first: :\n1) The Xarthium Canteen 🍽️\n2) The Veyrrksan Chamber 🚪\n-> "))
        if choice2_lvl1_room == 1:
            print(f"\n{user}: I see there is food around here !\n\n(Mothership Assistant) : You have discovered two types of food! The first one is the Xarthium Jelly, and the second is the Korallin Thunder Mushroom. These items will regenerate your health. Currently, you have {user_health} of health.")
            while yes_or_no != "Y" and yes_or_no != "N":
                yes_or_no = input("\nWould you like to eat 2 Xarthium Jelly and 1 Korallin Thunder Mushroom ?\n-> Y|N : ")
                if yes_or_no == "Y":
                    user_health += xarthium_jelly * 2 + veyrrksa_shell
                    print(f"You now have {user_health} of health !")
                elif yes_or_no == "N":
                    print(f"\n{user}: This thing disgusts me, I could never eat that !")
                else:
                    print("\n⚠️  You must enter either \"Y\" or \"N\"!")
        elif choice2_lvl1_room == 2:
            print(f"\n{user}: Alright, I’ll go see what else is on this floor!")
        else:
            print("\n⚠️  Please, enter a valid number !")
    
    print(f"\n[*Shaking*] {user}: Wow, everything is moving around!\n\n{user}: BUT… WHAT IS THIS HIDEOUS CREATURE! ! ")
    print("\n(Veyrrksan): Mouahahaha, I'm the boss on this floor, if you want to go up you need to beat me !")

    while user_health > 0 and veyrrksan_health > 0:
        print(f"\n(Mothership Assistant): Veyrrksan has {veyrrksan_health} HP and you have {user_health} HP!")
        
        choice3_lvl1_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n-> "))
        
        veyrrksan_choice = random.randint(1, 2)
        fist = random.randint(5, 15)
        chipped_bit = random.randint(1, 5)
        shell_shard = random.randint(1, 5)
        weapon_choice = random.randint(15, 25)
        
        if choice3_lvl1_room == 1:
            veyrrksan_health -= fist
            print(f"\n({user}): Take my fist in your face ! (-{fist} HP)")
        elif choice3_lvl1_room == 2:
            veyrrksan_health -= weapon_choice
            print(f"\n({user}): Take this {weapon_name} right in your face ! (-{weapon_choice} HP)")
        else:
            print("\n⚠️  Please, enter a valid number !")

        if veyrrksan_choice == 1:
            user_health -= chipped_bit
            print(f"\n(Veyrrksan): Using the Chipped Bite technique! (-{chipped_bit} HP)")
        else:
            user_health -= shell_shard
            print(f"\n(Veyrrksan): Using the Shell Shard technique! (-{shell_shard} HP)")            

    if veyrrksan_health <= 0:
        print("\n(Mothership Assistant): You have killed the Boss Veyrrksan !")
    else:
        print("\n(Narrator): Unfortunately, the adventure ends here for you...")
        state = "end"
        break

    print(f"\n(Mothership Assistant): You are now on floor number 2 !")

    while choice4_lvl2_room != 1 and choice4_lvl2_room != 2:
        choice4_lvl2_room = int(input("\n(Mothership Assistant): Please choose which room you want to enter first: :\n1) The Xarthium Beast Arena 🏟️\n2) Xarthium Beast Armory 🛡️\n-> "))
        if choice4_lvl2_room == 2:
            print(f"\n{user}: I see there is food around here and a new weapon !")
            yes_or_no = input("\nWould you like to eat 3 Xarthium Jelly and take a ShotGun ?\n-> Y|N : ")
            if yes_or_no == "Y":
                user_health += xarthium_jelly * 3
                weapon_name2 = "ShotGun 🔫"
                print(f"You now have {user_health} of health !")
            elif yes_or_no == "N":
                print(f"\n{user}: This thing disgusts me, I could never eat that !")
            else:
                print("\n⚠️  You must enter either \"Y\" or \"N\"!")
        elif choice4_lvl2_room == 1:
            print(f"\n{user}: Alright, I’ll go see what else is on this floor!")
        else:
            print("\n⚠️  Please, enter a valid number !")
    
    print(f"\n({user}): [*TRAP OPEN*] AAAAAAAH I'M FALLING!!!")
    print("\nWelcome little human, I’m the Xarthium Beast here, everyone is scared of me !\nI’M GOING TO DESTROY YOU !")

    while user_health > 0 and xarthium_beast_health > 0:
        print(f"\n(Mothership Assistant): Xarthium Beast has {xarthium_beast_health} HP and you have {user_health} HP!")
        
        if weapon_name2 == "":
            choice5_lvl2_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n-> "))
        else:
            choice6_lvl2_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n3) {weapon_name2}\n-> "))

        xarthium_choice = random.randint(1, 2)
        fist = random.randint(5, 15)
        ionized_charge = random.randint(10, 20)
        voltic_spit = random.randint(8, 18)
        weapon_choice = random.randint(15, 25)
        weapon_choice2 = random.randint(30, 50)

        if choice5_lvl2_room == 1 or choice6_lvl2_room == 1:
            xarthium_beast_health -= fist
            print(f"\n({user}): Take my fist in your face ! (-{fist} HP)")
        elif choice5_lvl2_room == 2 or choice6_lvl2_room == 2:
            xarthium_beast_health -= weapon_choice
            print(f"\n({user}): Take this {weapon_name} right in your face ! (-{weapon_choice} HP)")
        elif choice6_lvl2_room == 3:
            xarthium_beast_health -= weapon_choice2
            print(f"\n({user}): Take my {weapon_name2} right in your face ! (-{weapon_choice2} HP)")
        else:
            print("\n⚠️  Please, enter a valid number !")

        if xarthium_choice == 1:
            user_health -= ionized_charge
            print(f"\n(Xarthium Beast): Using the Ionized Charge technique! (-{ionized_charge} HP)")
        else:
            user_health -= voltic_spit
            print(f"\n(Xarthium Beast): Using the Voltic Spit technique! (-{voltic_spit} HP)")  

    if xarthium_beast_health <= 0:
        print("\n(Mothership Assistant): You have killed the Boss Xarthium Beast !")
    else:
        print("\n(Narrator): Unfortunately, the adventure ends here for you...")
        state = "end"
        break

    print(f"\n(Mothership Assistant): You are now on floor number 3 !")

    while choice7_lvl3_room != 1 and choice7_lvl3_room != 2:
        choice7_lvl3_room = int(input("\n(Mothership Assistant): Please choose which room you want to enter first: :\n1) The Luminescent Myco-Lab 🧪\n2) The Spore Reactor Chamber ☢️\n-> "))
        if choice7_lvl3_room == 1:
            print(f"\n{user}: I see there is food around here and a new weapon !")
            yes_or_no = input("\nWould you like to eat one Xarthium Jelly, one Veryrksa Shell and take the Rocher Launcher ?\n-> Y|N : ")
            if yes_or_no == "Y":
                user_health += xarthium_jelly + veyrrksa_shell
                weapon_name3 = "Rocket Launcher 🚀"
                print(f"You now have {user_health} of health !")
            elif yes_or_no == "N":
                print(f"\n{user}: This thing disgusts me, I could never eat that !")
            else:
                print("\n⚠️  You must enter either \"Y\" or \"N\"!")
        elif choice7_lvl3_room == 1:
            print(f"\n{user}: Alright, I’ll go see what else is on this floor!")
        else:
            print("\n⚠️  Please, enter a valid number !")

    print(f"\n({user}): [*EXPLOSION*] THE NUCLEAR POWER PLANT HAS EXPLODED!!")
    print("\n(Myco Fulgurant): I am the right hand of the Celestial Boss, the undeniable one. You may have defeated the two underlings, but against me, you stand no chance.\nNow… die.")

    while user_health > 0 and myco_fulgurant_health > 0:
        print(f"\n(Mothership Assistant): Myco Fulgurant has {myco_fulgurant_health} HP and you have {user_health} HP!")
        
        if weapon_name2 == "" and weapon_name3 == "":
            choice8_lvl3_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n-> "))
        elif weapon_name2 == "ShotGun 🔫" and weapon_name3 == "":
            choice9_lvl3_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n3) {weapon_name2}\n-> "))
        elif weapon_name2 == "" and weapon_name3 == "Rocket Launcher 🚀":
            choice10_lvl3_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n3) {weapon_name3}\n-> "))
        else:
            choice11_lvl3_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n3) {weapon_name2}\n4) {weapon_name3}\n-> "))

        myco_fulgurant_choice = random.randint(1, 3)
        fist = random.randint(5, 15)
        spore_pulse = random.randint(15, 25)
        shock_tendril = random.randint(13, 23)
        fungal_overgrowth = random.randint(5, 12)
        weapon_choice = random.randint(15, 25)
        weapon_choice2 = random.randint(30, 50)
        weapon_choice3 = random.randint(60, 80)

        if choice8_lvl3_room == 1 or choice9_lvl3_room == 1 or choice10_lvl3_room == 1 or choice11_lvl3_room == 1:
            myco_fulgurant_health -= fist
            print(f"\n({user}): Take my fist in your face ! (-{fist} HP)")
        elif choice8_lvl3_room == 1 or choice9_lvl3_room == 1 or choice10_lvl3_room == 1 or choice11_lvl3_room == 1:
            myco_fulgurant_health -= weapon_choice
            print(f"\n({user}): Take this {weapon_name} right in your face ! (-{weapon_choice} HP)")
        elif choice9_lvl3_room == 3 or choice11_lvl3_room == 3:
            myco_fulgurant_health -= weapon_choice2
            print(f"\n({user}): Take my {weapon_name2} right in your face ! (-{weapon_choice2} HP)")
        elif choice11_lvl3_room == 4:
            myco_fulgurant_health -= weapon_choice3
            print(f"\n({user}): Take my {weapon_name3} right in your face ! (-{weapon_choice3} HP)")            
        else:
            print("\n⚠️  Please, enter a valid number !")

        if myco_fulgurant_choice == 1:
            user_health -= spore_pulse
            print(f"\n(Myco Fulgurant): Using the Spore Pulse technique! (-{spore_pulse} HP)")
        elif myco_fulgurant_choice == 2:
            user_health -= shock_tendril
            print(f"\n(Myco Fulgurant): Using the Shock Tendril technique! (-{shock_tendril} HP)") 
        else:
            user_health -= fungal_overgrowth
            print(f"\n(Myco Fulgurant): Using the Fungal Overgrowth technique! (-{fungal_overgrowth} HP)") 

    if myco_fulgurant_health <= 0:
        print("\n(Mothership Assistant): You have killed the Boss Myco Fulgurant !")
    else:
        print("\n(Narrator): Unfortunately, the adventure ends here for you...")
        state = "end"
        break

    print(f"\n(Mothership Assistant): Good job, you are now on floor 4 ! Take this heal to beat the Monster !")
    user_health += 150

    print("\n(Celestial Archimandrite): I see that you have defeated my three loyal servants. Allow me to show you…\nTHE TRUE POWER !")
    print(f"\n({user}): He has just transformed into a Fallen Angel !")

    print(f"\n(Mothership Assistant): Mr. {user}, I wish you good luck. The future of humanity is in your hands!")

    while user_health > 0 and celestial_archimandrite > 0:
        print(f"\n(Mothership Assistant): Celestial Archimandrite has {celestial_archimandrite} HP and you have {user_health} HP!")
        
        if weapon_name2 == "" and weapon_name3 == "":
            choice12_lvl4_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n-> "))
        elif weapon_name2 == "ShotGun 🔫" and weapon_name3 == "":
            choice13_lvl4_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n3) {weapon_name2}\n-> "))
        elif weapon_name2 == "" and weapon_name3 == "Rocket Launcher 🚀":
            choice14_lvl4_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n3) {weapon_name3}\n-> "))
        else:
            choice15_lvl4_room = int(input(f"Which attack are you going to use ?\n1) Fist 🤜\n2) {weapon_name}\n3) {weapon_name2}\n4) {weapon_name3}\n-> "))

        celestial_archimandrite_choice = random.randint(1, 4)
        fist = random.randint(5, 15)
        crystal_lance = random.randint(10, 15)
        astral_wave = random.randint(20, 30)
        gravity_wrap = random.randint(5, 10)
        starfall_obliteration = random.randint(30, 60)
        weapon_choice = random.randint(15, 25)
        weapon_choice2 = random.randint(30, 50)
        weapon_choice3 = random.randint(60, 80)

        if choice12_lvl4_room == 1 or choice13_lvl4_room == 1 or choice14_lvl4_room == 1 or choice15_lvl4_room == 1:
            celestial_archimandrite -= fist
            print(f"\n({user}): Take my fist in your face ! (-{fist} HP)")
        elif choice12_lvl4_room == 1 or choice13_lvl4_room == 1 or choice14_lvl4_room == 1 or choice15_lvl4_room == 1:
            celestial_archimandrite -= weapon_choice
            print(f"\n({user}): Take this {weapon_name} right in your face ! (-{weapon_choice} HP)")
        elif choice13_lvl4_room == 3 or choice15_lvl4_room == 3:
            celestial_archimandrite -= weapon_choice2
            print(f"\n({user}): Take my {weapon_name2} right in your face ! (-{weapon_choice2} HP)")
        elif choice15_lvl4_room == 4:
            celestial_archimandrite -= weapon_choice3
            print(f"\n({user}): Take my {weapon_name3} right in your face ! (-{weapon_choice3} HP)")            
        else:
            print("\n⚠️  Please, enter a valid number !")

        if celestial_archimandrite_choice == 1:
            user_health -= crystal_lance
            print(f"\n(Celestial Archimandrite): Using the Crystal Lance technique! (-{crystal_lance} HP)")
        elif celestial_archimandrite_choice == 2:
            user_health -= astral_wave
            print(f"\n(Celestial Archimandrite): Using the Astral Wave technique! (-{astral_wave} HP)") 
        elif celestial_archimandrite_choice == 3:
            user_health -= gravity_wrap
            print(f"\n(Celestial Archimandrite): Using the Gravity Wrap technique! (-{gravity_wrap} HP)") 
        else:
            user_health -= starfall_obliteration
            print(f"\n(Celestial Archimandrite): Using the Starfall Obliteration technique! (-{starfall_obliteration} HP)") 

    if celestial_archimandrite <= 0:
        print("\n(Mothership Assistant): You have killed the Boss Celestial Archimandrite !")
    else:
        print("\n(Narrator): Unfortunately, the adventure ends here for you...")
        state = "end"
        break

    print(f"\n(Narrator): {user}, you have managed to defeat one of the most feared monsters in the universe. Your adventure is only just beginning !")
    state = "end"
