class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills
    
    def display_info(self):
        skills_str = ', '.join(self.skills)
        return f"Name: {self.name}, Group: {self.group}, Legs: {self.number_of_legs}, Skills: {skills_str}"


animals = [
    Animal("Wolf", "Mammals", 4, ["Running", "Hunting", "Howling"]),
    Animal("Eagle", "Birds", 2, ["Flying", "Hunting", "Sharp Vision"]),
    Animal("Leopard", "Mammals", 4, ["Jumping", "Hunting", "Climbing"]),
    Animal("Horse", "Mammals", 4, ["Running", "Carrying Loads"]),
    Animal("Cobra", "Reptiles", 0, ["Slithering", "Venomous Bite"])
]


for animal in animals:
    print(animal.display_info())
