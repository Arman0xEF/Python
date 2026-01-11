import math

user_choice = 0
side = 0
length = 0
width = 0
height = 0
base = 0
radius = 0

while user_choice != 5:
    user_choice = int(input("\n==================\nArea Calculator 📐\n==================\n\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nWhich shape : "))

    if user_choice == 1:
        height = int(input("Height : "))
        base = int(input("Base : "))
        print(f"\nThe area is {(height * base)/2}.")
    elif user_choice == 2:
        length = int(input("Length : "))
        width = int(input("Width : "))
        print(f"\nThe area is {length * width}.")
    elif user_choice == 3:
        side = int(input("Side : "))
        print(f"\nThe area is {side ** 2}.")
    elif user_choice == 4:
        radius = int(input("Radius : "))
        print(f"\nThe area is {math.pi * radius ** 2}")
    else:
        print("\nPlease enter a valid number !")
