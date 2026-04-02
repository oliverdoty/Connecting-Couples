def twentyquestions():
    return

def custom_wordle():
    secret = input('What is the key word? ')
    digits = len(secret)
    for i in range(6):
        guess = input('What is your guess? ')
        while True:
            if guess != digits:
                guess = input(f'Input a guess with {digits}: ')
            elif guess.alpha() == False:
                guess = input('You guess must be all letters: ')
            else:
                break
        for j in range(list(guess)):
            for k in range(list(secret)):
                if list(guess)[j] == list(secret)[k]:
                    #yellow
                    if j == k:
                        pass#green

                        # ....
    return

def tanks():
    return
