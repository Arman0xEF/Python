planet_weight = float(input("What is your Earth weight : "))
planet = int(input("What is you planet number : "))

gravity = 0

if planet == 1:
    gravity = 0.38
elif planet == 2:
    gravity = 0.91
elif planet == 3:
    gravity = 0.38
elif planet == 4:
    gravity = 2.53
elif planet == 5:
    gravity = 1.07
elif planet == 6:
    gravity = 0.89
elif planet == 7:
    gravity = 1.14
else:
    print("Invalid planet number")

print(f"The destination weight is {gravity * planet_weight}")

