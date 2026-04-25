import socket

def custom_wordle_server():
    # connect
    HOST = '127.0.0.1'  # The server's hostname or IP address (self)
    PORT_S = 65432        # The port used by the server
    PORT_D = 23456
    
    with socket.socket() as ss:
        # Bind socket to address and publish contact info
        ss.bind((HOST, PORT_S))
        ss.listen()
        print("Worlde server started. Listening on", (HOST, PORT_S))

        # Answer incoming connection
        cs, addrs = ss.accept()
        print('Connected by', addrs)

        with cs:
            print('awaiting secret input')
            secret = cs.recv()#1024)

            with socket.socket() as sd:

                cd, addrd = sd.accept()
                print('Connected by', addrd)

                with cd:
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
