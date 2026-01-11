import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

results = random.choices(symbols, k=3)

print(f"{results[0]} | {results[1]} | {results[2]}")
if results == ['7️⃣','7️⃣','7️⃣']:
    print("Jackpot! 💰")
else:
    print("Thanks for playing.")
