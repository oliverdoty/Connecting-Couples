import socket

def custom_wordle_client_d():

    HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    PORT_D = 23456        # The port used by the server

    print('## Welcome to wordle! ##')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT_D))

        # Receive word length from server
        length_bytes = s.recv(1024)
        secret_length = int(length_bytes.decode())
        for i in range(6):
            guess = input(f'Guess a word of length {secret_length}:  ').lower()
            while True:
                if len(guess) != secret_length or guess.isalpha() == False:
                    guess = input(f'Input a guess with {secret_length} letters: ')
                else:
                    break
            s.sendall(guess.encode())
            accuracy = s.recv(1024).encode()
            print(accuracy)
            if accuracy == 'Congrats, you win!':
                break

if __name__ == '__main__':
    custom_wordle_client_d()
