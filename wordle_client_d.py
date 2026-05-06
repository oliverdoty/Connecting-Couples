import socket

def custom_wordle_client_d():

    HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    PORT_D = 23456        # The port used by the server

    print('## Welcome to wordle! ##\nYou have 6 guesses to guess the other \nplayer\'s word.\n   If you ever need a hint, guess\n   "hint please" and you will be\n   given a hint without costing a\n   guess. It will notify the other\n   player.')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # connect to server
        s.connect((HOST, PORT_D))

        # Game starts
        secret_length = int(s.recv(1024).decode())
        while True:
            guess = input(f'Guess a word of length {secret_length}:  ').lower()
            # verifies guess
            while True:
                if guess == 'hint please':
                    break
                elif len(guess) != secret_length or guess.isalpha() == False:
                    guess = input(f'Input a guess with {secret_length} letters: ')
                else:
                    break
            s.sendall(guess.encode()) #send guess to server

            # feedback from server
            feedback = s.recv(1024).decode()
            print('\n',feedback,'\n')
            # special cases for feedback
            if feedback == '':
                print('disconnected')
                break
            elif '!' in feedback: # game has ended
                break

if __name__ == '__main__':
    custom_wordle_client_d()
