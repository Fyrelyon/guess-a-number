#Guess a Number A.I.
#Gavin B.

import math

# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    print("*************************")
    print("*  Gavin     10/1/2017  *") #CHANGE THE DATE WHEN COMPLETED
    print("*************************")
    
def get_guess(low, high):
    """
    Return a truncated average of current low and high.
    """
    return (low + high)//2

def get_tries(low, high):
    #This function will get the number of tries the computer gets.
    #It is completely cosmetic if playing correctly, but detects if the player is cheating.
    tries = math.log((high-1)-(low+1),2) + 1
    tries = round(tries)
    return (tries)

def get_name():
    name = input("What is your name? ")
    return name

def get_range():
    #This function is the configuration that sets the lowest and highest numbers.
    lowest = -1
    highest = -1
    
    print("I will now ask for the range of numbers that your number can be on, "+name+".")

    while lowest < 0:
        lowest = input("What is the lowest possible number, "+name+"? ")
        
        if lowest.isnumeric():
            lowest = int(lowest)
        
        else:
            print("")
            print("You must enter a number, "+name+".")
            print("")
            lowest = -1

    while highest < 0 and highest < lowest:
        highest = input("What is the highest possible number, "+name+"? ")
        
        if highest.isnumeric():
            if int(highest) > int(lowest):
                highest = int(highest)
                
            else:
                print("")
                print("The highest value must be higher than the lowest, "+name+".")
                print("")
                highest = -1
            
        else:
            
            print("")
            print("You must enter a number, "+name+".")
            print("")
            highest = -1

    return lowest, highest

def pick_number(low, high, orig_tries):
    """
    Ask the player to think of a number between low and high.
    Then wait until the player presses enter.
    """
    print("Please think of a number from "+str(low)+" to "+str(high)+", "+name+", and I will try to guess it.")
    print("I have "+str(orig_tries)+" tries to guess your number.")
    print("")
    input("Press any [ENTER] to continue...")

def check_guess(guess, tries):
    """
    Computer will ask if guess was too high, low, or correct.
    

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    while True:
        print("")
        print("I have "+str(tries)+" tries remaining.")
        print("I know! The answer is " + str(guess) + "!")
        is_it_correct = input("Was my answer \"too high\" {h), \"too low\" (l), or just \"right\" (y), "+name+"? ")
        
        if is_it_correct.lower() == 'too high' or is_it_correct.lower() == 'h':
            return 1
        elif is_it_correct.lower() == 'too low' or is_it_correct.lower() == 'l':
            return -1
        elif is_it_correct.lower() == 'right' or is_it_correct.lower() == 'y' or is_it_correct.lower() == 'yes':
            return 0

        else:
            print("")
            print("I do not understand, "+name+". You must enter one of the phrases between the quotation marks.")

def show_result(guess, orig_tries, tries_left):
    """
    Says the result of the game. (The computer might always win.)
    Can also detect if the player cheated.
    Tells how many tries were used.
    """
    if guess != -1:
        print("")
        print("Hah! I won! The answer IS " + str(guess) + ", "+name+"!")
        
    else:
        print("")
        print("Hey! You cheated, "+name+"! I want a rematch!")
        

    print("I used "+str(orig_tries - tries_left)+" tries during that match.")
    print("")

def play_again():
    while True:
        decision = input("Would you like to play again, "+name+"? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes':
            print("")
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            print("")
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n', "+name+".")
            print("")

def play():
    low, high = get_range()
    check = -1

    #Tries the computer has remaining.
    tries = get_tries(low, high)

    #Used to print how many tries were used.
    orig_tries = tries
    
    pick_number(low, high, orig_tries)
    
    while check != 0 and tries > 0:
        guess = get_guess(low, high)
        check = check_guess(guess, tries)

        if check == -1:
            # adjust low

            low = guess
            tries = tries - 1
            
        elif check == 1:
            # adjust high
            high = guess
            tries = tries - 1

    if tries == 0:
        guess = -1

    show_result(guess, orig_tries, tries)


# Game starts running here
show_start_screen()

playing = True

while playing:
    name = get_name()
    play()
    playing = play_again()

show_credits()
