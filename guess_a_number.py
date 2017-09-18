import random
import math

#config
low = 1
high = 100
tries = 1

#calculates the number of tries the player gets
x = 2
while x <= high:
    x = x*2
    tries = tries + 1

#helperfunction
def get_guess():
    while True:
        guess = input("Take a guess: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def get_high():
    #YOU LEFT OFF HERE

#choose a game mode
print("Choose a gamemode. Select \"1\" or \"2\" for You Guess or Computer Guesses.")

def get_gamemode():
    while True:
            guess = input("Take a guess: ")

            if guess.isnumeric() and guess == "1" or guess == "2":
                guess = int(guess)
                return guess
            else:
                print("You must enter the number \"1\" or \"2\".")

#start game 1
if guess = 1:
    rand = random.randint(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");


    guess = -1

    while guess != rand and tries > 0:
        guess = get_guess()
    
        if guess < rand:
            tries = tries - 1
            print("You guessed too low. " + str(tries) + " tries left.")
        elif guess > rand:
            tries = tries - 1
            print("You guessed too high. " + str(tries) + " tries left.")
        else:
            print("You got it!")

    print("Game over. The number was " + str(rand) + ".")

#start game 2
if guess = 2:
    print("Before we start, I will need the range of the numbers.")
    time.sleep(2)
    get_high() = 
