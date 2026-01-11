import random

rock = "✊"
paper = "✋"
scissors = "✌️"
computer = random.randint(1, 3)
player = int(input("\n===================\nRock Paper Scissors\n===================\n\n1) ✊\n2) ✋\n3) ✌️\n\nPick a number: "))
if player == 1 and computer == 1:
    print(f"\nYou chose : {rock}")
    print(f"Computer chose : {rock}")
    print("It's a tie")
elif player == 2 and computer == 2:
    print(f"\nYou chose : {paper}")
    print(f"Computer chose : {paper}")
    print("It's a tie")
elif player == 3 and computer == 3:
    print(f"\nYou chose : {scissors}")
    print(f"Computer chose : {scissors}")
    print("It's a tie")

elif player == 2 and computer == 1:
    print(f"\nYou chose : {paper}")
    print(f"Computer chose : {rock}")
    print("The player won!")
elif player == 3 and computer == 1:
    print(f"\nYou chose : {scissors}")
    print(f"Computer chose : {rock}")
    print("The computer won!")
elif player == 3 and computer == 2:
    print(f"\nYou chose : {scissors}")
    print(f"Computer chose : {paper}")
    print("The player won!")

elif player == 1 and computer == 2:
    print(f"\nYou chose : {rock}")
    print(f"Computer chose : {paper}")
    print("The computer won!")
elif player == 1 and computer == 3:
    print(f"\nYou chose : {rock}")
    print(f"Computer chose : {scissors}")
    print("The player won!")
elif player == 2 and computer == 3:
    print(f"\nYou chose : {paper}")
    print(f"Computer chose : {scissors}")
    print("The computer won!")
