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
guess = -1
playing_game = True

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

def restart():
    while True:
        print("Would you like to play again? (y/n)")
        print("")
        answer = input()
        
        if answer == "y":
            return True
        
        elif answer == "n":
            return False

        else:
            print("You must enter \"y\" or \"n\".")

#start game
while playing_game:

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

    #calculates number of tries the player gets
    tries = math.log(high-low,2)
    tries = round(tries)

    guess = get_guess()

    if guess == 10:
        print("You win!")
        print("")
        
        playing_game = restart()
        
    else:
        print("You lose.")
        print("")
        
        playing_game = restart()

#end game screen
print("  ________                            ________                           ._.")
print(" /  _____/ _____     _____    _ ___   \_____  \  ___  __  ____  _______  | |")
print("/   \  ___ \__  \   /     \  _/ __ \   /   |   \ \  \/ /_/ __ \ \_  __ \ | |")
print("\    \_\  \ / __ \_|  Y Y  \ \  ___/  /    |    \ \   / \  ___/  |  | \/  \|")
print(" \______  /(____  /|__|_|  /  \___  > \_______  /  \_/   \___  > |__|     __")
print("        \/      \/       \/       \/          \/             \/           \/")

time.sleep(5)
