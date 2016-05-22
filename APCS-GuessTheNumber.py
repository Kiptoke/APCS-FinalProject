#Andrew Zhou
#Guess the Number Program - Final Project


# TODO: finish restart error


import random
import sys

# --- Class Definition ---

class RandomNumberGame:
    'The class that runs the game'
    rounds = 1

    def __init__(self):
        self.randomNum = 0
        self.guessNum = 0
        self.guesses = 0
        RandomNumberGame.rounds += 1

    def generateNum(self):
        self.randomNum = random.randint(0, 10)
    
    def getUserInput(self):
        self.guessNum = int(input("Guess a number between 1 and 10: "))
        self.compareNumbers()

    def restart(self):
        print("Do you want to play another round?")
        self.restart = input()
        if (self.restart == "yes") or (self.restart == "Yes"):
            x = RandomNumberGame
        else:
            sys.exit()

    def checkLoss(self):
        if (self.guesses >= 3):
            print("You lose!")
            self.restart()

    def compareNumbers(self):
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

    def runGame(self):
        self.generateNum()
        self.getUserInput()

# --- Main Code ---

print("\t------GUESS THE NUMBER------")

test = RandomNumberGame()
test.runGame()
