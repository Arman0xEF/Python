class Pokemon:
    def __init__(self, entry, name, types, level, region, height, weight, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.level = level
        self.region = region
        self.height = height
        self.weight = weight
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name, self.name)

    def display_details(self):
        print(f"Entry Number: {self.entry}\nName: {self.name}\nType: {self.types}\nDescription: {self.description}")
    
pickachu = Pokemon(25, 'Pickachu', ['Electric'], 15, 'Kanto',1.4, 13.2,'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs. Pikachu has already been caught!', True)
charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 23, 'Kanto',5.07, 199.5,'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 45, 'Kalos',21.04, 518.1,'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', False)

pickachu.speak()
pickachu.display_details()

charizard.speak()
charizard.display_details()

gyarados.speak()
gyarados.display_details()
