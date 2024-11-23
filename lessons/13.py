import random

# Game data
locations = {
    "lava_field": "A vast field of cooled lava stretches before you. Steam rises from the cracks.",
    "geyser": "A massive geyser erupts, spraying water high into the air.",
    "aurora": "The sky glows with shimmering greens and purples of the northern lights."
}
items = ["magic stone", "lava crystal", "aurora shard"]

# Functions
def explore_location(location):
    print(f"\nYou arrive at the {location}.")
    print(locations[location])
    found_item = random.choice(items)
    print(f"You discover a {found_item}!")
    return found_item

def make_choice():
    print("\nWhere will you go next?")
    print("1. Lava Field")
    print("2. Geyser")
    print("3. Aurora Spot")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        return "lava_field"
    elif choice == "2":
        return "geyser"
    elif choice == "3":
        return "aurora"
    else:
        print("Invalid choice. Staying where you are.")
        return None

# Main game loop
def play_game():
    print("Welcome to Iceland, Robert!")
    print("Your quest is to collect three magical items to save your sister Aurelia.")
    backpack = []

    while len(backpack) < 3:
        location = make_choice()
        if location:
            item = explore_location(location)
            if item not in backpack:
                backpack.append(item)
                print(f"You put the {item} in your backpack.")
            else:
                print(f"You already have the {item}. Keep exploring!")
    
    print("\nCongratulations, Robert!")
    print("You've collected all the magical items:")
    print(", ".join(backpack))
    print("You use their power to summon a protective aurora for Aurelia. She is safe!")

# Start the game
play_game()
