# Class for a “Pet” with attributes like name and species,
# and a method to display a greeting

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f"Woof! My name is {self.name} and I'm a {self.species}!")

my_pet = Pet("Max", "dog")
my_pet.greet()
