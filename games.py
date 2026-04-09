import numpy as np
import matplotlib as plt

def twentyquestions():
    return

def custom_wordle():

    '''Custom Wordle Game
    Works with any size secret word (must be letters)
    Returns T or F corresponding to a win or loss'''

    secret = list(input('What is the key word? ').lower()) # all lowercase for consistency
    while:
        if ''.join(secret).isalpha() == False: # no length restricitons on secret word
            secret = list(input('Please enter a key word consisting of only characters in the alphabet: ').lower())
        else:
            break
    green_letters = 0
    for i in range(6):
        guess = list(input('What is your guess? ').lower())
        while:
            if len(guess) != len(secret) or ''.join(guess).isalpha() == False:
                guess = list(input(f'Input a guess with {len(secret)} letters: '))
            else:
                break
        for j in range(len(secret)):
            for k in range(len(guess)):
                if guess[k] == secret[j]:
                    if '033' not in guess[k]:
                        guess[k] = '\033[33m' + guess[k] + '\033[0m' # makes yellow
                    if j == k:
                        guess[k] = '\033[32m' + guess[k][5] + '\033[0m' # makes green
                        green_letters += 1
        if green_letters == len(secret):
            return True
        print(''.join(guess))
    return False

def tanks():
    theta = input('What angle would you like to launch shoot at? (0 - 90) ')
    while:
        if theta.isdigit() == False or 

    power = input('What power would you like to shoot at? (1-100) ')
    return

tanks()
