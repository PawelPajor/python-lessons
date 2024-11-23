# Simple guessing game where the computer picks a random number, and the user has to guess it

import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You guessed it!")