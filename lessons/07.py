# Program that tracks favorite foods for different people using a dictionary

favorites = {"Aurelia": "Pizza", "Robert": "Steak"}
name = input("Enter a name: ")
if name in favorites:
    print(f"{name}'s favorite food is {favorites[name]}.")
else:
    food = input(f"What is {name}'s favorite food? ")
    favorites[name] = food
    print(f"Added {name}'s favorite food: {food}.")
