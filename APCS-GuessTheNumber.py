#Andrew Zhou
#Guess the Number Program - Final Project

# ------ Importing Modules and Libraries ------

import random
import sys

# ------ Class Definition -------

class RandomNumberGame:
    'The class that runs the game'

    # Initializing Method
    # Creates variables
    
    def __init__(self):
        self.randomNum = 0      # Variable for Random Integer
        self.guessNum = 0       # Variable for user input
        self.guesses = 0        # Varaible for number of guesses

    def generateNum(self):                                                  # Generates a Random integer between 1 and 10, inclusive
        self.randomNum = random.randint(1, 10)
    
    def getUserInput(self):                                                 # Gets user input - an integer
        self.guessNum = int(input("Guess a number between 1 and 10: ")) 
        self.compareNumbers()

    def restart(self):                                                      # Restart Method - asks if user wants to play another game
        print("Do you want to play another round?")
        self.restart = input()
        if (self.restart == "yes") or (self.restart == "Yes"):
            x = RandomNumberGame()
            x.runGame()
        else:
            sys.exit()

    def checkLoss(self):                                                    # Checks if player has lost the game
        if (self.guesses >= 3):
            print("You lose!")
            self.restart()

    def compareNumbers(self):                                               # Compares the User Input to the Random Integer
        if (self.randomNum == self.guessNum):
            print("You won!")
            self.restart()
        elif (self.randomNum > self.guessNum):
            print("Too low!")
            self.guesses += 1
            self.checkLoss()
            self.getUserInput()
        elif (self.randomNum < self.guessNum):
            print("Too high!")
            self.guesses += 1 
            self.checkLoss()
            self.getUserInput()

    def runGame(self):                                                      # Game Method - runs the game
        self.generateNum()
        self.getUserInput()

# ------ Main Code ------

print("\t------GUESS THE NUMBER------")     # Create Title

test = RandomNumberGame()                   # Creates Game Object
test.runGame()                              # Runs Game

