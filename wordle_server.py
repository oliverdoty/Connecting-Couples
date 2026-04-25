import socket

def custom_wordle_server():
    # connect
    HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    PORT_S = 65432        # The port used by the server
    PORT_D = 23456

    print(f"[server] Waiting for smart client on {HOST}:{PORT_S} …")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
        ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ss.bind((HOST, PORT_S))
        ss.listen(1)
        conn_s, addr_s = ss.accept()
        print(f"[server] Secret-setter connected from {addr_s}")

        with conn_s:
            print('awaiting secret input')
            secret = list(conn_s.recv(1024).decode())
            print(f'Server received secret: {secret}')

        print(f"[server] Waiting for guesser on {HOST}:{PORT_D} …")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sd:
            sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sd.bind((HOST, PORT_D))
            sd.listen(1)
            conn_d, addr_d = sd.accept()
            print(f"[server] Guesser connected from {addr_d}")

            with conn_d:
                conn_d.sendall(str(len(secret)).encode())
                while True:
                    guess = list(conn_d.recv(1024).encode())
                    if guess == []:
                        break
                    if guess == secret: # client_d wins!
                        conn_d.sendall('Congrats, you win!'.encode())
                        break

                    #give feeback for guess
                    result = [''] * len(guess)
                    secret_remaining = list(secret)

                    # First pass: mark greens
                    for i in range(len(guess)):
                        if guess[i] == secret[i]:
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
                            result[i] = guess[i]                        # no colour

                    correct = all(guess[i] == secret[i] for i in range(len(guess)))
                    return ''.join(result), correct
                
                    for j in range(len(secret)):
                        for k in range(len(guess)):
                            if guess[k] == secret[j]:
                                if '033' not in guess[k]:
                                    guess[k] = '\033[33m' + guess[k] + '\033[0m' # makes yellow
                                if j == k:
                                    guess[k] = '\033[32m' + guess[k][5] + '\033[0m' # makes green
                    accuracy = ''.join(guess)
                    conn_d.sendall(accuracy.encode())
