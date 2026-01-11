gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1 = int(input("Q1) Do you like Dawn or Dusk ?\n1) Dawn 🌅 \n2) Dusk 🌆\n : "))
print("_______________________________________________________________________\n")

if q1 == 1:
    gryffindor += 1; ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1; slytherin += 1
else:
    print("Wrong input.")

q2 = int(input("Q2) When I'm dead, I want people to remember me as : \n1) The Good 👍\n2) The Great ✨\n3) The Wise 🧙🏻‍♂️\n4) The Bold 👨‍🦲\n : "))
print("_______________________________________________________________________\n")

if q2 == 1:
    hufflepuff += 2
elif q2 == 2:
    slytherin += 2
elif q2 == 3:
    ravenclaw += 2
elif q2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

q3 = int(input("Q3) Which kind of instrument most pleases you ear ? \n1) The violin 🎻\n2) The trumpet 🎺\n3) The piano 🎹\n4) The drum 🥁\n : "))

if q3 == 1:
    slytherin += 4
if q3 == 2:
    hufflepuff += 4
if q3 == 3:
    ravenclaw += 4
if q3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")
print("_______________________________________________________________________\n")

print(f"🦁 Gryffindor = {gryffindor}\n🦅 Ravenclaw = {ravenclaw}\n🦡 Hufflepuf = {hufflepuff}\n🐍 Slytherin = {slytherin}")
