import random
import math

#config
low = 1
high = 100
guesses = 1
x = 2 #this helps decide how many guesses the player needs

while x < high:
    x = x*2
    guesses = guesses + 1

#start game
rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1

while guess != rand and guesses > 0:

    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        guesses = guesses - 1
        print("You guessed too low. " + str(guesses) + " guesses left.")
    elif guess > rand:
        guesses = guesses - 1
        print("You guessed too high. " + str(guesses) + " guesses left.")
    else:
        print("You got it!")

print("Game over.")
