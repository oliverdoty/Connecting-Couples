import socket

def custom_wordle_client_d():

    HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    PORT_D = 23456        # The port used by the server

    print('## Welcome to wordle! ##')

    with socket.socket() as sd:
        sd.connect((HOST, PORT_D))
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
