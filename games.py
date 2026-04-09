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
        for j in range(guess):
            for k in range(secret):
                if guess[j] == secret[k]:
                    guess[j] = k
                    if j == k:
                        pass #green

                        # ....
    return

def tanks():
    return
