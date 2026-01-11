height = int(input("What is your height in cm ? : "))
credit = int(input("How much credit do you have ? : "))

if height >= 137 and credit >= 10:
  print("Enjoy the ride !")
elif height < 137 and credit >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credit < 10:
  print("You don't have enough credits.")
else:
  print("Your not meeting any requirements.")
