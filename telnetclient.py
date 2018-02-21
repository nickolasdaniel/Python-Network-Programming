import socket

def init_client(server_address):
    connected = True
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting {} to server ...'.format(server_address))
    client_socket.connect(server_address)

    while connected:
        # allowed__commands = ['ls, cd, ls-l']
        try:
            if server_address[0] == '127.0.0.1':
                message = input('\nlocalhost@localhost' + '>> ')
            else:
                message = input(server_address[0] + '@' + server_address[1] + '>> \n')
            print('Sending message: {}'.format(message))
            client_socket.sendall(message.encode('utf-8'))

            recv_data(client_socket)

        except IOError as e:
            print('Error: {}'.format(e))

        except Exception as e:
            print('Other error: {}'.format(e))

        except KeyboardInterrupt:
                connected = False
def recv_data(client_socket):
    recv_size = 1
    MAX_RECV_BUFFER = 1024
    while recv_size:
        data_buffer = client_socket.recv(MAX_RECV_BUFFER)
        message = data_buffer.decode('utf-8')
        print('Received data: '.format(message))

        if not data_buffer:
            break
        recv_size += len(data_buffer)

    data_buffer = ''
    client_socket.close()

if __name__ == '__main__':
    init_client(('127.0.0.1', 8080))
