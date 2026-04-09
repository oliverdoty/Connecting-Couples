def twentyquestions():
    return

def custom_wordle():
    secret = list(input('What is the key word? ').lower()) # all lowercase for consistency
    while True:
        if ''.join(secret).isalpha() == False: # no length restricitons on secret word
            secret = list(input('Please enter a key word consisting of only characters in the alphabet: ').lower())
        else:
            break
    length = len(secret)
    for i in range(6):
        guess = list(input('What is your guess? ').lower())
        while True:
            if len(guess) != length or ''.join(guess).isalpha() == False:
                guess = list(input(f'Input a guess with {length} letters: '))
            else:
                break
        for j in range(len(secret)):
            for k in range(len(guess)):
                if guess[k] == secret[j]:
                    guess[k] = '\033[33m' + guess[k] + '\033[0m' # makes yellow
                    if j == k:
                        guess[k] = '\033[32m' + guess[k] + '\033[0m' # makes green
        print(''.join(guess))

def tanks():
    return

custom_wordle()
