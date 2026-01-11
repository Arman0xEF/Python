import random

number = random.randint(1, 9)
question = input("Question : ")

if number == 1:
  print("Yes - definitely.")
elif number == 2:
  print("It is decidedly so.")
elif number == 3:
  print("Without a doubt.")
elif number == 4:
  print("Reply hazy, try again.")
elif number == 5:
  print("Ask again later.")
elif number == 6:
  print("Better not tell you now.")
elif number == 7:
  print("My sources say no.")
elif number == 8:
  print("Outlook not so good.")
else:
  print("Very doubtful.")
