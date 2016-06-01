# Andrew Zhou
# Caesar Cipher - Final Project

# ------ Importing Libraries ------

import sys

# ------ Functions ------

def encode(text, shift):                                # Function that encodes a message
    shifttext = []                      
    ciphertext = ""
    for letter in text:                 # for all letters in the plaintext
        textNum = ord(letter)           # change all letters into unicode values
        textNum += shift                # adds shift number to unicode value
        if letter.isupper():            # makes sure that the value is still a letter
            if textNum > ord('Z'):
                textNum -= 26
            elif textNum < ord('A'):
                textNum += 26
        elif letter.islower():
            if textNum > ord('z'):
                textNum -= 26
            elif textNum < ord('a'):
                textNum += 26
        elif textNum == (32 + shift):   # Makes sure spaces remain spaces
            textNum = 32
        shifttext.append(textNum)       # Adds values onto a list of unicode values
    for num in shifttext:               # for all numbers in the unicode value array
        letter = chr(num)               # Converts unicode back into string
        ciphertext += letter            # Adds letter into a string
    print("Ciphertext: " + ciphertext)  # prints string

def decode(text, shift):                                # Function that decodes a message
    shifttext = []
    ciphertext = ""
    for letter in text:
        textNum = ord(letter)
        textNum -= shift
        if letter.isupper():
            if textNum > ord('Z'):
                textNum -= 26
            elif textNum < ord('A'):
                textNum += 26
        elif letter.islower():
            if textNum > ord('z'):
                textNum -= 26
            elif textNum < ord('a'):
                textNum += 26
        elif textNum == (32 - shift):
            textNum = 32
        shifttext.append(textNum)
    for num in shifttext:
        letter = chr(num)
        ciphertext += letter
    print("Ciphertext: " + ciphertext)

# --- Main Code ---

print("\t------CAESAR CIPHER------\n")

print("Are you encrypting a message or decrypting a message? (use a lowercase 'e' or 'd')")
crypto = input("Input: ")                                                                       # User input

if crypto == "e":
    plaintext = input("Please input the plaintext to be encrypted: ")                           # User Input - plaintext
    change = int(input("Please input the amount of shift (1 - 26): "))                          # User Input - Shift
    if (change > 26) or (change < 1):                                                           # Ensuring a good shift number
        print("ERROR: invalid shift, must be betweeen 1 and 26, inclusive")
        sys.exit()
    encode(plaintext, change)
    
elif crypto == "d":
    plaintext = input("Please input the ciphertext to be decrypted: ")                          # User Input - ciphertext
    change = int(input("Please input the amount of shift (1 - 26): "))                          # User Input - Shift
    if (change > 26) or (change < 1):                                                           # Ensuring a good shift number
        print("ERROR: invalid shift, must be betweeen 1 and 26, inclusive")
        sys.exit()
    decode(plaintext, change)
