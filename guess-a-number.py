import random
import math
import time

#title screen
print("  ________                                            _____             _______                   ___.                    ._.")
print(" /  _____/  __ __   ____    ______  ______           /  _  \            \      \   __ __   _____  \_ |__    ____  _______ | |")
print("/   \  ___ |  |  \_/ __ \  /  ___/ /  ___/  ______  /  /_\  \   ______  /   |   \ |  |  \ /     \  | __ \ _/ __ \ \_  __ \| |")
print("\    \_\  \|  |  /\  ___/  \___ \  \___ \  /_____/ /    |    \ /_____/ /    |    \|  |  /|  Y Y  \ | \_\ \\  ___/  |  | \/ \|")
print(" \______  /|____/  \___  >/____  >/____  >         \____|__  /         \____|__  /|____/ |__|_|  / |___  / \___  > |__|    __")
print("        \/             \/      \/      \/                  \/                  \/              \/      \/      \/          \/")

#config
low = 0
high = 0

#helper functions
def get_guess():
    while True:
        print("")
        guess = input("Take a guess: ")
        print("")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("")
            print("You must enter a number.")
            print("")

#calculates number of tries the player gets
def get_tries():
    tries = math.log(high-low,2) + 1
    tries = round(tries)
    return tries

def rando_numero():
    rando = random.randint(low,high)
    rando = round(rando)
    return rando

#end game screen
def end_game():
    print("  ________                            ________                           ._.")
    print(" /  _____/ _____     _____    _ ___   \_____  \  ___  __  ____  _______  | |")
    print("/   \  ___ \__  \   /     \  _/ __ \   /   |   \ \  \/ /_/ __ \ \_  __ \ | |")
    print("\    \_\  \ / __ \_|  Y Y  \ \  ___/  /    |    \ \   / \  ___/  |  | \/  \|")
    print(" \______  /(____  /|__|_|  /  \___  > \_______  /  \_/   \___  > |__|     __")
    print("        \/      \/       \/       \/          \/             \/           \/")

    time.sleep(5)

def restart():
    print("")
    print("Would you like you play again? (y/n)")
    print("")
    answer = input("")
    if answer == 'y':
        playing_game()
        
    elif answer == 'n':
        end_game()
        
    else:
        print("You must enter a \"y\" or \"n.\"")
        print("")

print("")
print("Before we begin, we'll need the highest and lowest numbers.")
print("")

#calculates low
print("What is the lowest possible value I should guess?")
print("")

while True:
    low = input()

    if low.isnumeric():
        low = int(low)
        break
    else:
        print("")
        print("You must enter a number.")
        print("")

#calculates high
print("")
print("And the highest possible value I should guess?")
print("")

while True:
    high = input()
    if high.isnumeric():
        if int(high) <= low:
            print("")
            print("Your number must be higher than the lowest value.")
            print("")
        else:
            high = int(high)
            break
    else:
        print("")
        print("You must enter a number.")
        print("")

#start game
def playing_game():

    print("")
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + "...")

    tries = get_tries()

    rando = rando_numero()

    while tries > 0:

        print("")
        print("You have " + str(tries) + " tries left.")

        guess = get_guess() 
            
        if guess == rando:
            print("You win!")
            tries = 0

        elif guess < rando:
            print("You guessed too low.")
            tries = tries-1
            
        elif guess > rando:
            print("You guessed too high.")
            tries = tries-1

        else:
            print("You lose!")
            
    restart()
    
playing_game()
