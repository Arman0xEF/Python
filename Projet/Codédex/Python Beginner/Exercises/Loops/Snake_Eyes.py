import random

total = 0

while total != 2:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    if total == 2:
        print("Snake eyes!")
    else:
        print("Nope")
