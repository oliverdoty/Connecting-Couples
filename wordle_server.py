import socket


def check_guess(guess,secret):

    #give feeback for guess
    result = [''] * len(guess) # set result list to size of guess
    secret_remaining = list(secret) # create a new copy of secret

    # First pass: mark greens
    for i in range(len(guess)):
        if guess[i] == secret_remaining[i]:
            result[i] = f'\033[32m{guess[i]}\033[0m'   # green
            secret_remaining[i] = None                  # consumed

    # Second pass: mark yellows
    for i in range(len(guess)):
        if result[i]:                                   # already green
            continue
        if guess[i] in secret_remaining:
            result[i] = f'\033[33m{guess[i]}\033[0m'   # yellow
            secret_remaining[secret_remaining.index(guess[i])] = None
        else:
            result[i] = guess[i]                        # no color

    return ''.join(result)

def custom_wordle_server():
    # connect
    HOST = '127.0.0.1'
    PORT_S = 65432
    PORT_D = 23456

    print(f"Waiting for smart client on {HOST}:{PORT_S} …")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
        ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ss.bind((HOST, PORT_S))
        ss.listen(1)
        conn_s, addr_s = ss.accept()
        print(f"Smart client connected from {addr_s}")

        with conn_s:
            print('awaiting secret input')
            secret = list(conn_s.recv(1024).decode())
            print(f'Server received secret: {''.join(secret)}')

            print(f"Waiting for dumb client on {HOST}:{PORT_D} …")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sd:
                sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sd.bind((HOST, PORT_D))
                sd.listen(1)
                conn_d, addr_d = sd.accept()
                print(f"Dumb client connected from {addr_d}")

                with conn_d:
                    conn_d.sendall(str(len(secret)).encode())
                    for i in range(6):
                        guess = list(conn_d.recv(1024).decode())

                        if guess == []:
                            break
                        if guess == secret: # client_d wins!
                            conn_d.sendall(f'\033[32m{''.join(secret)}\033[0m\n\nCongrats, you win!'.encode()) # winning messages
                            conn_s.sendall(f'\033[32m{''.join(secret)}\033[0m\nThe other player won!'.encode())
                            print('Dumb client wins')
                            break

                        feedback = check_guess(guess,secret)
                        if i == 5:
                            conn_s.sendall(f'{feedback}\nThe other player lost! They could not guess {''.join(secret)}'.encode()) # losing messages
                            feedback = f'{feedback}\n\nSorry, you lost. The answer was {''.join(secret)}'
                            print('Dumb client loses')
                        conn_d.sendall(feedback.encode())
                        conn_s.sendall(feedback.encode())

if __name__ == '__main__':
    custom_wordle_server()
