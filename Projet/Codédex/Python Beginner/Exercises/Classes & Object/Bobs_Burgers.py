class Restaurant:
  name = ""
  category = ""
  rating = 0.0
  delivery = False

bobs_burger = Restaurant()
bobs_burger.name = "Bob\'s Burgers"
bobs_burger.category = "American Diner"
bobs_burger.rating = 4.7
bobs_burger.delivery = False

mcdonald = Restaurant()
mcdonald.name = "McDonald"
mcdonald.category = "Fast Food"
mcdonald.rating = 3.4
mcdonald.delivery = True

sushi = Restaurant()
sushi.name = "SushiPlanet"
sushi.category = "Sushi"
sushi.rating = 4.5
sushi.delivery = True


print(vars(bobs_burger))
print(vars(mcdonald))
print(vars(sushi))
