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
            secret_bytes = conn_s.recv(1024)
            secret = list(secret_bytes.decode())
            print(f'Server received secret: {secret}')

        print(f"[server] Waiting for guesser on {HOST}:{PORT_D} …")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sd:
            sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sd.bind((HOST, PORT_D))
            sd.listen(1)
            conn_d, addr_d = sd.accept()
            print(f"[server] Guesser connected from {addr_d}")

            with conn_d:
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
