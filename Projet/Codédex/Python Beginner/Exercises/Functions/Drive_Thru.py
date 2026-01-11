food = [
    '🍔 Cheeseburger',
    '🍟 Fries',
    '🥤 Soda',
    '🍦 Ice Cream',
    '🍪 Cookie'
]



def get_item(a):
    return food[a-1]

def welcome():
    number = 1
    print("Hello this is our menu :")
    for i in food:
        print(f"\n{number}) {i}")
        number += 1

welcome()
user = int(input("\nWhat would you like to choose : "))
print(f"\nThis is your order : {get_item(user)}")
