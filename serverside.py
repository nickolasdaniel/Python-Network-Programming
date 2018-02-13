import socket
import argparse
import sys

def init_server(server_address):
    MAX_BUFFER_SIZE = 1024
    ECHO_MESSAGE = 'Welcome to our server'


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(server_address)
    except socket.error as e:
        print(e)

    server_socket.listen(5)
    print ("Started connection at {}:{}".format(server_address[0], server_address[1]))

    while True:
        client_socket, client_address = server_socket.accept()
        print ('Client just connected at {}:{}'.format(client_address[0], client_address[1]))
        try:
            client_socket.send(ECHO_MESSAGE.encode('utf-8'))
        except IOError as error:
            print(error)

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=str, required=True, help='Address like 192.168.10.1')
parser.add_argument('-p', type=int, required=True, help='Port like 8080')
args = parser.parse_args(['127.0.0.1', '8080'])

if __name__ == '__main__':
    init_server('127.0.0.1')