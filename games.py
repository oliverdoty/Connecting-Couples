def twentyquestions():
    return

def custom_wordle():
    secret = list(input('What is the key word? ').lower()) # all lowercase for consistency
    while True:
        if secret.isalpha() == False: # no length restricitons on secret word
            secret = input('Please enter a key word consisting of only characters in the alphabet: ').lower()
        else:
            break
    length = len(secret)
    for i in range(6):
        guess = list(input('What is your guess? ').lower())
        while True:
            if guess != length or guess.isalpha() == False:
                guess = input(f'Input a guess with {length} letters: ')
            else:
                break
        for j in range(secret):
            for k in range(guess):
                if guess[k] == secret[j]:
                    guess[k] = '\033[33m' + guess[k] + '\033[0m' # makes yellow
                    if j == k:
                        guess[k] = '\033[32m', guess[k], + '\033[0m' # makes green
        print(''.join(guess))

def tanks():
    return

custom_wordle()
