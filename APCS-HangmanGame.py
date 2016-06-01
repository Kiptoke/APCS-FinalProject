# Andrew Zhou
# Hangman Game - Final Project

# ------ Importing Libraries ------

import random
import sys

# ------ Class Definition ------

class Hangman:

    def __init__(self):                                     # Intitialization Method - creates variables
        self.wordList = ["computer", "airplane", "nation", "birdhouse", "explosion", "programming", "tablet"]
        self.pictures = [
        """
           /-----\\
           |     |
           |     0
           |
           |
           |
           |
           |
           |
        ___|____________

        """,
        """
           /-----\\
           |     |
           |    ***
           |    * *
           |    ***
           |
           |
           |
           |
        ___|____________

        """,
        """
           /-----\\
           |     |
           |    ***
           |    * *
           |    ***
           |     |
           |     |
           |     |
           |
        ___|____________

        """,
        """
           /-----\\
           |     |
           |    ***
           |    * *
           |    ***
           |    /|\\
           |   / | \\
           |     |
           |
        ___|____________

        """,
        """
           /-----\\
           |     |
           |    ***
           |    * *
           |    ***
           |    /|\\
           |   / | \\
           |     |
           |    / 
        ___|____|________

        """,
        """
           /-----\\
           |     |
           |    ***
           |    * *
           |    ***
           |    /|\\
           |   / | \\
           |     |
           |    / \\
        ___|____|_|______

        """]

        self.goodGuesses = 0                                                        # No. of good Guesses made
        self.badGuesses = 0                                                         # No. of bad Guesses made

        self.wordDisplay = []                                                       # Array of letters

        self.randomWord = self.wordList[random.randint(0, len(self.wordList) - 1)]  # Chooses a Random Word in the list
        self.wordLength = len(self.randomWord)                                      # Finds length of that word
        self.gameOver = False                                                       # Flag to run game

    def startupGame(self):

        # ------ Startup Code ------

        print(self.pictures[self.badGuesses])                       # Prints picture
        print("Welcome to HANGMAN! Try to guess the word I'm thinking of.\n")
        for letter in self.randomWord:                              # Writes a set of blanks equal to the length of the word                     
            self.wordDisplay.append("_")                

        self.displayConversion()                                    # Converts array to a string
        print("")

        while self.gameOver == False:                               # WHILE: the game is not over, run the game
            self.runGame()
        
    def displayConversion(self):

        display = ""                                                # String to convert to
        index = 0
        
        for index in self.wordDisplay:                              # FOR: all indicies in wordDisplay, add that to a string
            display += index + " "

        print(display)

    def checkLetter(self, letter):

        index = 0

        while index < self.wordLength:                              # Searches all letters in the word
            if letter == self.randomWord[index]:                    # IF: the given letter is equal to the letter in the word
                self.goodGuesses += 1                               # +1 to good guesses
                self.wordDisplay[index] = letter                    # Change the list
                index += 1
            else:   
                index += 1

        if letter in self.randomWord:                               # Returns message based off whether the letter was in the word
            print("That letter is in the word.")
        else:
            print("That letter is not in the word.")
            self.badGuesses += 1                                    # +1 to bad guesses
            print(str(self.badGuesses))

        if (self.badGuesses == 5):                                  # Game Over Conditions
            print("You lose!")
            print("The word was: " + self.randomWord)
            self.gameOver = True
        elif (self.goodGuesses == self.wordLength):
            print("You win!")
            print("The word was: " + self.randomWord)
            self.gameOver = True
        else:
            self.display()

    def display(self):                                              # Displays picture and blanks
        print(self.pictures[self.badGuesses])   
        self.displayConversion()
        print("")

    def runGame(self):                                              # Central Method - runs the game
        userLetter = input("Guess a letter in lowercase: ")         
        print("")
        
        self.checkLetter(userLetter)
        
# ------ Testing Code ------

print("\t------ Hangman Game ------\n")
testGame = Hangman()
testGame.startupGame()
    
