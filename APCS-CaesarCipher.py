# Andrew Zhou
# Caesar Cipher - Final Project

import sys

print("\t------CAESAR CIPHER------\n")

# --- Methods ---

def encode(text, shift):
    shifttext = []
    ciphertext = ""
    for letter in text:
        textNum = ord(letter)
        textNum += shift
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
        elif textNum == (32 + shift):
            textNum = 32
        shifttext.append(textNum)
    for num in shifttext:
        letter = chr(num)
        ciphertext += letter
    print("Ciphertext: " + ciphertext)

def decode(text, shift):
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

print("Are you encrypting a message or decrypting a message? (use a lowercase 'e' or 'd')")
crypto = input("Input: ")

if crypto == "e":
    plaintext = input("Please input the plaintext to be encrypted: ")
    change = int(input("Please input the amount of shift (1 - 26): "))
    if (change > 26) or (change < 1):
        print("ERROR: invalid shift, must be betweeen 1 and 26, inclusive")
        sys.exit()
    encode(plaintext, change)
    
elif crypto == "d":
    plaintext = input("Please input the ciphertext to be decrypted: ")
    change = int(input("Please input the amount of shift (1 - 26): "))
    if (change > 26) or (change < 1):
        print("ERROR: invalid shift, must be betweeen 1 and 26, inclusive")
        sys.exit()
    decode(plaintext, change)
