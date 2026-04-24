import numpy as np
import matplotlib as plt
import random
import socket


def twentyquestions():
    return

def custom_wordle():

    '''Custom Wordle Game
    Works with any size secret word (must be letters)
    Returns T or F corresponding to a win or loss'''

    secret = list(input('What is the key word? ').lower()) # all lowercase for consistency
    while True:
        if ''.join(secret).isalpha() == False: # no length restricitons on secret word
            secret = list(input('Please enter a key word consisting of only characters in the alphabet: ').lower())
        else:
            break
    for i in range(6):
        guess = list(input('What is your guess? ').lower())
        while True:
            if len(guess) != len(secret) or ''.join(guess).isalpha() == False:
                guess = list(input(f'Input a guess with {len(secret)} letters: '))
            else:
                break
        green_letters = 0
        for j in range(len(secret)):
            for k in range(len(guess)):
                if guess[k] == secret[j]:
                    if '033' not in guess[k]:
                        guess[k] = '\033[33m' + guess[k] + '\033[0m' # makes yellow
                    if j == k:
                        guess[k] = '\033[32m' + guess[k][5] + '\033[0m' # makes green
                        green_letters += 1
        print(''.join(guess))
        if green_letters == len(secret):
            return True
    return False

HOST = '127.0.0.1'
PORT = 65431

def custom_wordle_server():
    # connect
    #HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    #PORT = 65432        # The port used by the server
    with socket.socket() as ss:
        # Bind socket to address and publish contact info
        ss.bind((HOST, PORT))
        ss.listen()
        print("Worlde server started. Listening on", (HOST, PORT))

        # Answer incoming connection
        conn_s, addrs = ss.accept()
        print('Connected by', addrs)

        with conn_s as cs:
            print('awaiting secret input')
            secret = cs.recv()#1024)

            with socket.socket() as sd:

                conn_d, addrd = sd.accept()
                print('Connected by', addrd)

                with conn_d as cd:
                    for i in range(6):
                        guess = cd.recv(1024)
                        if guess == '':
                            break
                        green_letters = 0
                        for j in range(len(secret)):
                            for k in range(len(guess)):
                                if guess[k] == secret[j]:
                                    if '033' not in guess[k]:
                                        guess[k] = '\033[33m' + guess[k] + '\033[0m' # makes yellow
                                    if j == k:
                                        guess[k] = '\033[32m' + guess[k][5] + '\033[0m' # makes green
                                        green_letters += 1
                        accuracy = ''.join(guess)
                        if green_letters == len(secret):
                            cd.sendall(0)
                            break
                        else:
                            cd.sendall(accuracy)


    return

def custom_wordle_client_s():

    #HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    #PORT = 65432        # The port used by the server

    print('## Welcome to wordle! ##')

    with socket.socket() as ss:
        ss.connect((HOST, PORT))
        print('connected')
        # game
        secret = list(input('What is the key word? ').lower()) # all lowercase for consistency
        while True:
            if ''.join(secret).isalpha() == False:
                secret = list(input('Please enter a real word consisting of only characters in the alphabet: ').lower())
            else:
                break
        ss.sendall(secret)
        answer = ss.recv(1024)
        print(answer)

def custom_wordle_client_d():

    #HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    #PORT = 65432        # The port used by the server

    print('## Welcome to wordle! ##')

    with socket.socket() as sd:
        sd.connect((HOST, PORT))
        # game
        length = sd.recv(1024)
        for i in range(6):
            guess = list(input(f'Guess a word of length {length}:  ').lower())
            while True:
                if len(guess) != length or ''.join(guess).isalpha() == False:
                    guess = list(input(f'Input a guess with {length} letters: '))
                else:
                    break
            sd.sendall(guess)
            accuracy = sd.recv(1024)

    return

def valid_input(inp,up_lim,low_lim=0):
    while True:
        try:
            if (low_lim <= int(inp) <= up_lim):
                return int(inp) # valid
        except:
            pass
        inp = input(f'Please input a digit {low_lim} - {up_lim}: ')

def tanks():
    loc = input('Where would you like to place your tank? (0-20) ')
    loc = valid_input(loc,20)
    for i in range(5):
        theta = input('What angle would you like to launch shoot at? (0 - 90) ')
        theta = valid_input(theta,90)
        power = input('What power would you like to shoot at? (1-100) ')
        power = valid_input(power,100)
        target = 255 # example
        if (target - 20) <= (power**2*np.sin(2*np.deg2rad(theta))/9.8) <= (target + 20):
            print('BOOM') # hit
            break
        else:
            print('miss')
    return

#custom_wordle()
#tanks()
