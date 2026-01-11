rating = float(input("Enter your rating of statisfaction between 0 and 5 : "))

if rating > 4.5:
    print("Extraordinary")
elif rating > 4:
    print("Excellent")
elif rating > 3:
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")
