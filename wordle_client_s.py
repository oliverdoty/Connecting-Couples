import socket

def custom_wordle_client_s():

    HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    PORT_S = 65432        # The port used by the server

    print('## Welcome to wordle! ##')

    secret = list(input('What is the key word? ').lower()) # all lowercase for consistency
    while True:
        if ''.join(secret).isalpha() == False:
            secret = list(input('Please enter a real word consisting of only characters in the alphabet: ').lower())
        else:
            break
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT_S))
        s.sendall(secret.encode())

if __name__ == '__main__':
    custom_wordle_client_s()
