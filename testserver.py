import socket

def server_example():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_ADDRESS = '127.0.0.1'
    MESSAGE = 'Welcome!'
    try:
        server_socket.bind(IP_ADDRESS)

        print(MESSAGE)
    except socket.error as error:
        print(error)

    server_socket.listen(5)

if __name__ == '___main__':
    server_example()