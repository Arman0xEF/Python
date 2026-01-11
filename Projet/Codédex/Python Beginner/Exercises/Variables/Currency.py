pesos = int(input("What do you have left in pesos ? "))
soles = int(input("What do you have left in soles ? "))
reais = int(input("What do you have left in reais ? "))

usd = ((pesos * 0.00026) + (soles * 0.29) + (reais * 0.19))
print(usd)
