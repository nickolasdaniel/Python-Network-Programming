import socket

def init_client(server_address):
    connected = True
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting {} to server ...'.format(server_address))
    client_socket.connect(server_address)

    while connected:
        allowed__commands = ['ls, cd, ls-l']
        try:
            if server_address[0] == '127.0.0.1':
                message = input('\nlocalhost@localhost' + '>> ')
            else:
                message = input(server_address[0] + '@' + server_address[1] + '>> \n')
            print('Sending message: {}'.format(message))
            client_socket.sendall(message.encode('utf-8'))

        except socket.error as e:
            print('Socket error: {}'.format(e))
        except Exception as e:
            print('Other error: {}'.format(e))
        except KeyboardInterrupt:
                connected = False
if __name__ == '__main__':
    init_client(('127.0.0.1', 8080))