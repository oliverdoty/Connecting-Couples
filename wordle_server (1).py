import socket
import random

# D is client_d standing for dumb client (guesses)
# S is client_s standing for smart client (sends secret)

def check_guess(guess,secret):

    '''Gives feeback for guess. Colors correct letters.
    If they are in the wrong spot, they are yellow. If they
    are in the correct location, they are green.'''

    result = [''] * len(guess) # set result list to size of guess
    secret_remaining = list(secret) # create a new copy of secret

    # First pass: mark greens
    for i in range(len(guess)):
        if guess[i] == secret_remaining[i]:
            result[i] = f'\033[32m{guess[i]}\033[0m'   # marks green
            secret_remaining[i] = None                  # consumed/done marking

    # Second pass: mark yellows
    for i in range(len(guess)):
        if result[i]:                                   # already green
            continue
        if guess[i] in secret_remaining:
            result[i] = f'\033[33m{guess[i]}\033[0m'   # marks yellow
            secret_remaining[secret_remaining.index(guess[i])] = None
        else:
            result[i] = guess[i]                        # keep white

    return ''.join(result)

def custom_wordle_server():

    HOST = '127.0.0.1'
    PORT_S = 65432
    PORT_D = 23456

    print(f"Waiting for smart client on {HOST}:{PORT_S} …")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss: # connect to smart client
        ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ss.bind((HOST, PORT_S))
        ss.listen(1)
        conn_s, addr_s = ss.accept()
        print(f"Smart client connected from {addr_s}")

        with conn_s:
            # capture secret
            print('awaiting secret input')
            secret = list(conn_s.recv(1024).decode())
            print(f'Server received secret: {''.join(secret)}')

            print(f"Waiting for dumb client on {HOST}:{PORT_D} …")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sd: # connect to dumb client
                sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sd.bind((HOST, PORT_D))
                sd.listen(1)
                conn_d, addr_d = sd.accept()
                print(f"Dumb client connected from {addr_d}")

                with conn_d:
                    conn_d.sendall(str(len(secret)).encode()) # send length of secret to client_d
                    turn = 0 # initialize turn count

                    # Game loop
                    while True:
                        guess = list(conn_d.recv(1024).decode()) # capture guess
                        # special cases for guess
                        if guess == '': # Disconnected
                            break
                        elif guess == secret: # client_d wins!
                            conn_d.sendall(f'\033[32m{''.join(secret)}\033[0m\n\nCongrats, you win!'.encode()) # winning messages
                            conn_s.sendall(f'\033[32m{''.join(secret)}\033[0m\nThe other player won!'.encode())
                            print('Dumb client wins.')
                            break
                        elif ''.join(guess) == 'hint please': # client_d requests a hint
                            hint = secret[random.randint(0,len(secret)-1)] # give client_d a random letter in secret
                            conn_d.sendall(f'Hint: the word contains the letter \033[31m{hint}\033[0m'.encode())
                            conn_s.sendall(f'Your opponent used a hint: \033[31m{hint}\033[0m'.encode())
                            continue # do not count as a turn

                        feedback = check_guess(guess,secret) # check guess against secret
                        
                        turn += 1
                        if turn == 6: # too many guesses. game over.
                            conn_s.sendall(f'{feedback}\nThe other player lost! They could\nnot guess {''.join(secret)}'.encode()) # losing messages
                            conn_d.sendall(f'{feedback}\n\nSorry, you lost! The answer was \033[31m{''.join(secret)}\033[0m'.encode())
                            print('Dumb client loses')
                            break

                        # send updates to both clients
                        conn_d.sendall(feedback.encode())
                        conn_s.sendall(feedback.encode())

if __name__ == '__main__':
    custom_wordle_server()
